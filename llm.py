"""Optional LLM generation. Turns an assembled prompt into finished content.

Supports multiple providers (Anthropic/Claude, Google/Gemini, OpenAI/Codex-GPT,
local OpenAI-compatible endpoints) behind one interface, so the same prompt
produces the same house-style content regardless of which model the caller has
a key for. Each provider's SDK is only imported when that provider is actually
used, so the core prompt generator has zero required dependencies.
"""
import os
import random
import time

from config import DEFAULTS

_PROVIDERS = {
    "anthropic": {
        "env_var": "ANTHROPIC_API_KEY",
        "package": "anthropic",
        "pip_name": "anthropic",
        "default_model": "claude-sonnet-5",
    },
    "gemini": {
        "env_var": "GEMINI_API_KEY",
        "fallback_env_var": "GOOGLE_API_KEY",
        "package": "google.genai",
        "pip_name": "google-genai",
        "default_model": "gemini-2.5-pro",
    },
    "openai": {
        "env_var": "OPENAI_API_KEY",
        "package": "openai",
        "pip_name": "openai",
        "default_model": "gpt-5",
    },
    # OpenAI-compatible local endpoints: Ollama, vLLM, LM Studio, llama.cpp
    # server, etc. Uses the openai SDK under the hood; base_url from
    # LOCAL_LLM_BASE_URL (default http://localhost:11434/v1 for Ollama).
    # API key is nominally required by the SDK but can be any string for
    # keyless endpoints; set LOCAL_LLM_API_KEY explicitly if the endpoint
    # actually validates it. Enables data-doesn't-leave-premises workflows
    # for enterprise reviewers who cannot ship prompts to a hosted API.
    "local": {
        "env_var": "LOCAL_LLM_API_KEY",
        "package": "openai",
        "pip_name": "openai",
        "default_model": "llama3.1",
        "base_url_env": "LOCAL_LLM_BASE_URL",
        "default_base_url": "http://localhost:11434/v1",
        "keyless_ok": True,
    },
}


# Approximate per-1K-token pricing (USD). Used by generate.py's --estimate-cost
# pre-flight. These are intentionally coarse; overrides can be supplied under
# `defaults.llm_pricing` in config.json. `local` costs $0 by default.
_DEFAULT_PRICING = {
    # provider -> {model_prefix: {"input": $/1K, "output": $/1K}}
    "anthropic": {
        "claude-opus-4":     {"input": 15.00, "output": 75.00},
        "claude-opus-4.7":   {"input": 15.00, "output": 75.00},
        "claude-sonnet-5":   {"input":  3.00, "output": 15.00},
        "claude-sonnet-4":   {"input":  3.00, "output": 15.00},
        "claude-haiku-4.5":  {"input":  1.00, "output":  5.00},
        "claude-haiku-4":    {"input":  0.80, "output":  4.00},
    },
    "openai": {
        "gpt-5":     {"input":  5.00, "output": 15.00},
        "gpt-4o":    {"input":  5.00, "output": 15.00},
        "gpt-4":     {"input": 30.00, "output": 60.00},
        "o1":        {"input": 15.00, "output": 60.00},
        "o3":        {"input": 15.00, "output": 60.00},
        "o4":        {"input": 15.00, "output": 60.00},
        "gpt-3.5":   {"input":  0.50, "output":  1.50},
    },
    "gemini": {
        "gemini-2.5-pro":   {"input":  1.25, "output":  5.00},
        "gemini-2.5-flash": {"input":  0.30, "output":  2.50},
        "gemini-1.5-pro":   {"input":  1.25, "output":  5.00},
    },
    "local": {"": {"input": 0.0, "output": 0.0}},
}


def _pricing_for(provider, model):
    """Return {'input': $/1K, 'output': $/1K} for (provider, model) or None
    if no pricing is known. Longest-matching model prefix wins so
    `claude-sonnet-5-20261101` matches `claude-sonnet-5`."""
    overrides = (DEFAULTS.get("llm_pricing") or {}).get(provider) or {}
    table = {**_DEFAULT_PRICING.get(provider, {}), **overrides}
    if not table:
        return None
    model = (model or "").lower()
    best = None
    for prefix in sorted(table, key=len, reverse=True):
        if not prefix or model.startswith(prefix.lower()):
            best = table[prefix]
            break
    return best


def estimate_tokens(text):
    """Very rough token estimator (~4 chars/token). Good enough for a
    pre-flight cost estimate; not a substitute for a real tokenizer."""
    return max(1, len(text or "") // 4)


def estimate_cost_usd(prompt, provider=None, model=None, expected_output_tokens=None):
    """Return (estimated USD, {'in_tokens', 'out_tokens', 'in_cost', 'out_cost'}).
    Returns (None, {...}) when no pricing is known for (provider, model)."""
    provider = _resolve_provider(provider)
    model = model or _default_model_for(provider)
    price = _pricing_for(provider, model)
    in_tokens = estimate_tokens(prompt)
    out_tokens = expected_output_tokens or DEFAULTS.get("llm_max_tokens", 4096)
    if price is None:
        return None, {"in_tokens": in_tokens, "out_tokens": out_tokens,
                       "in_cost": None, "out_cost": None,
                       "provider": provider, "model": model}
    in_cost = price["input"] * in_tokens / 1000.0
    out_cost = price["output"] * out_tokens / 1000.0
    return (in_cost + out_cost,
            {"in_tokens": in_tokens, "out_tokens": out_tokens,
             "in_cost": in_cost, "out_cost": out_cost,
             "provider": provider, "model": model})


class BudgetExceededError(RuntimeError):
    """Raised when a --budget-cap would be exceeded by this call."""


def _sleep_backoff(attempt):
    """Exponential backoff with jitter: 1s, 2s, 4s, 8s, 16s (+ up to 50% jitter)."""
    base = min(2 ** attempt, 16)
    time.sleep(base + random.uniform(0, base * 0.5))


def _is_retryable(exc):
    """True if `exc` is a transient LLM error worth retrying (rate limit or 5xx)."""
    code = getattr(exc, "status_code", None) or getattr(exc, "http_status", None)
    if code in (408, 425, 429, 500, 502, 503, 504):
        return True
    msg = str(exc).lower()
    return any(m in msg for m in ("rate limit", "overloaded", "timeout", "connection", "temporarily unavailable"))


def _resolve_provider(provider=None):
    provider = provider or DEFAULTS.get("llm_provider", "anthropic")
    if provider not in _PROVIDERS:
        raise RuntimeError(
            f"Unknown LLM provider '{provider}'. Choose one of: "
            f"{', '.join(sorted(_PROVIDERS))}"
        )
    return provider


def _api_key_for(provider):
    spec = _PROVIDERS[provider]
    key = os.environ.get(spec["env_var"])
    if not key and "fallback_env_var" in spec:
        key = os.environ.get(spec["fallback_env_var"])
    if not key and spec.get("keyless_ok"):
        # OpenAI-compatible local endpoints often accept any string as the
        # API key. Provide a sentinel so downstream SDK code doesn't refuse.
        key = "local-sk-not-required"
    return key


def _default_model_for(provider):
    return (DEFAULTS.get("llm_models") or {}).get(provider) or _PROVIDERS[provider]["default_model"]


def is_available(provider=None):
    """True if generation can run for `provider` (SDK importable + API key present)."""
    provider = _resolve_provider(provider)
    if not _api_key_for(provider):
        return False
    try:
        __import__(_PROVIDERS[provider]["package"])
    except ImportError:
        return False
    return True


def generate_content(prompt, model=None, max_tokens=None, provider=None):
    """Send `prompt` to the configured LLM provider and return the text response.

    `provider` defaults to `DEFAULTS["llm_provider"]` (config.json's `defaults.llm_provider`,
    "anthropic" if unset). Raises RuntimeError with an actionable message if the provider
    name is unrecognized, or if that provider's API key/SDK is missing.
    """
    provider = _resolve_provider(provider)
    spec = _PROVIDERS[provider]
    api_key = _api_key_for(provider)
    if not api_key:
        raise RuntimeError(
            f"{spec['env_var']} is not set. Export it before using --generate with "
            f"--provider {provider}, e.g. export {spec['env_var']}=..."
        )

    model = model or _default_model_for(provider)
    max_tokens = max_tokens or DEFAULTS["llm_max_tokens"]
    handler = {
        "anthropic": _generate_anthropic,
        "gemini": _generate_gemini,
        "openai": _generate_openai,
        "local": _generate_local,
    }[provider]
    max_retries = int(DEFAULTS.get("llm_max_retries", 3))
    last_exc = None
    for attempt in range(max_retries + 1):
        try:
            return handler(prompt, api_key, model, max_tokens)
        except RuntimeError:
            # Deterministic "empty response / bad config" errors from our own
            # code - do not retry.
            raise
        except Exception as exc:  # provider SDK errors: retry if transient
            last_exc = exc
            if attempt >= max_retries or not _is_retryable(exc):
                raise
            _sleep_backoff(attempt)
    raise last_exc  # unreachable; keeps type-checkers happy


def _missing_sdk(provider):
    spec = _PROVIDERS[provider]
    return RuntimeError(
        f"The '{spec['pip_name']}' package is required for --provider {provider}. "
        f"Install it with: pip install {spec['pip_name']}"
    )


def _empty_response_error(provider, detail=""):
    suffix = f" ({detail})" if detail else ""
    return RuntimeError(
        f"{provider} returned an empty response{suffix} - it may have been blocked by a "
        f"safety filter, hit a length limit before producing text, or the API call otherwise "
        f"succeeded without content. Try rephrasing the prompt or raising --model's max tokens."
    )


def _generate_anthropic(prompt, api_key, model, max_tokens):
    try:
        import anthropic
    except ImportError as exc:
        raise _missing_sdk("anthropic") from exc
    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    text = "".join(block.text for block in message.content if block.type == "text")
    if not text:
        raise _empty_response_error("anthropic", f"stop_reason={getattr(message, 'stop_reason', '?')}")
    return text


def _generate_gemini(prompt, api_key, model, max_tokens):
    try:
        from google import genai
        from google.genai import types
    except ImportError as exc:
        raise _missing_sdk("gemini") from exc
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(max_output_tokens=max_tokens),
    )
    if not response.candidates:
        feedback = getattr(response, "prompt_feedback", None)
        raise _empty_response_error("gemini", f"prompt blocked: {feedback}" if feedback else "no candidates")
    text = response.text
    if not text:
        finish_reason = getattr(response.candidates[0], "finish_reason", "?")
        raise _empty_response_error("gemini", f"finish_reason={finish_reason}")
    return text


def _openai_uses_completion_tokens(model):
    """gpt-5, o1, o3, and o4 families reject `max_tokens` and require
    `max_completion_tokens`. Older gpt-4/gpt-3.5 chat models accept `max_tokens`."""
    m = (model or "").lower()
    return m.startswith(("gpt-5", "o1", "o3", "o4", "gpt-4.1", "gpt-4o"))


def _generate_local(prompt, api_key, model, max_tokens):
    """OpenAI-compatible local endpoint (Ollama, vLLM, LM Studio, llama.cpp).

    Reuses the openai SDK with `base_url` pointed at the local server. Sends
    `max_tokens` (not `max_completion_tokens`) since local endpoints follow
    the classic OpenAI schema, not the reasoning-model variant.
    """
    try:
        import openai
    except ImportError as exc:
        raise _missing_sdk("openai") from exc
    spec = _PROVIDERS["local"]
    base_url = os.environ.get(spec["base_url_env"], spec["default_base_url"])
    client = openai.OpenAI(api_key=api_key, base_url=base_url)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
    )
    if not response.choices:
        raise _empty_response_error("local", f"no choices returned from {base_url}")
    text = response.choices[0].message.content
    if not text:
        finish_reason = getattr(response.choices[0], "finish_reason", "?")
        raise _empty_response_error("local", f"finish_reason={finish_reason}")
    return text


def _generate_openai(prompt, api_key, model, max_tokens):
    try:
        import openai
    except ImportError as exc:
        raise _missing_sdk("openai") from exc
    client = openai.OpenAI(api_key=api_key)
    token_kwarg = ("max_completion_tokens" if _openai_uses_completion_tokens(model)
                   else "max_tokens")
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            **{token_kwarg: max_tokens},
        )
    except openai.BadRequestError as exc:
        # Fall back to the other kwarg if the server disagrees with our guess.
        msg = str(exc).lower()
        if "max_tokens" in msg or "max_completion_tokens" in msg:
            fallback_kwarg = ("max_tokens" if token_kwarg == "max_completion_tokens"
                              else "max_completion_tokens")
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                **{fallback_kwarg: max_tokens},
            )
        else:
            raise
    if not response.choices:
        raise _empty_response_error("openai", "no choices returned")
    text = response.choices[0].message.content
    if not text:
        finish_reason = getattr(response.choices[0], "finish_reason", "?")
        raise _empty_response_error("openai", f"finish_reason={finish_reason}")
    return text
