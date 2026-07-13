"""Optional LLM generation. Turns an assembled prompt into finished content.

The `anthropic` SDK and an ANTHROPIC_API_KEY are only required when --generate is
used, so the core prompt generator has zero required dependencies.
"""
import os

from config import DEFAULTS


def is_available():
    """True if generation can run (SDK importable + API key present)."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return False
    try:
        import anthropic  # noqa: F401
    except ImportError:
        return False
    return True


def generate_content(prompt, model=None, max_tokens=None):
    """Send `prompt` to the Anthropic API and return the text response.

    Raises RuntimeError with an actionable message if the key or SDK is missing.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError(
            "ANTHROPIC_API_KEY is not set. Export it before using --generate, "
            "e.g. export ANTHROPIC_API_KEY=sk-ant-..."
        )
    try:
        import anthropic
    except ImportError as exc:
        raise RuntimeError(
            "The 'anthropic' package is required for --generate. "
            "Install it with: pip install anthropic"
        ) from exc

    client = anthropic.Anthropic(api_key=api_key)
    message = client.messages.create(
        model=model or DEFAULTS["llm_model"],
        max_tokens=max_tokens or DEFAULTS["llm_max_tokens"],
        messages=[{"role": "user", "content": prompt}],
    )
    return "".join(block.text for block in message.content if block.type == "text")
