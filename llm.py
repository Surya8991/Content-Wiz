"""Optional LLM generation. Turns an assembled prompt into finished content.

Supports multiple providers (Anthropic/Claude, Google/Gemini, OpenAI/Codex-GPT)
behind one interface, so the same prompt produces the same house-style content
regardless of which model the caller has a key for. Each provider's SDK is only
imported when that provider is actually used, so the core prompt generator has
zero required dependencies.
"""
import os

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
        "package": "google.generativeai",
        "pip_name": "google-generativeai",
        "default_model": "gemini-2.5-pro",
    },
    "openai": {
        "env_var": "OPENAI_API_KEY",
        "package": "openai",
        "pip_name": "openai",
        "default_model": "gpt-5",
    },
}


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
    }[provider]
    return handler(prompt, api_key, model, max_tokens)


def _missing_sdk(provider):
    spec = _PROVIDERS[provider]
    return RuntimeError(
        f"The '{spec['pip_name']}' package is required for --provider {provider}. "
        f"Install it with: pip install {spec['pip_name']}"
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
    return "".join(block.text for block in message.content if block.type == "text")


def _generate_gemini(prompt, api_key, model, max_tokens):
    try:
        import google.generativeai as genai
    except ImportError as exc:
        raise _missing_sdk("gemini") from exc
    genai.configure(api_key=api_key)
    client = genai.GenerativeModel(model)
    response = client.generate_content(prompt, generation_config={"max_output_tokens": max_tokens})
    return response.text


def _generate_openai(prompt, api_key, model, max_tokens):
    try:
        import openai
    except ImportError as exc:
        raise _missing_sdk("openai") from exc
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
