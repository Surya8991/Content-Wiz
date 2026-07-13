"""Loads config.json (brands + defaults). Single source of truth for config.

Falls back to hardcoded defaults if config.json is missing or unreadable, so the
tool never hard-fails on a config problem.
"""
import json
import os

_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

_FALLBACK = {
    "defaults": {
        "audience": "professionals in your target market",
        "wordcount": 1000,
        "llm_provider": "anthropic",
        "llm_model": "claude-sonnet-5",
        "llm_max_tokens": 4096,
        "llm_models": {
            "anthropic": "claude-sonnet-5",
            "gemini": "gemini-2.5-pro",
            "openai": "gpt-5",
        },
    },
    "brands": {},
}


def load():
    try:
        with open(_CONFIG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError):
        return _FALLBACK
    # Merge missing default keys from fallback so callers can rely on all keys.
    merged = dict(_FALLBACK)
    merged.update(data)
    defaults = dict(_FALLBACK["defaults"])
    defaults.update(data.get("defaults", {}))
    merged["defaults"] = defaults
    return merged


CONFIG = load()
DEFAULTS = CONFIG["defaults"]
BRANDS = CONFIG["brands"]


def brand_for_url(url):
    """Return the brand dict for a URL by matching its root domain, or None."""
    if not url:
        return None
    u = url.lower()
    for domain, brand in BRANDS.items():
        if domain in u:
            return brand
    return None


def audience_for_platform(brand, platform_key=None):
    """Return the effective audience for a brand, honoring an optional
    per-platform override.

    Precedence: `brand["platform_audience_overrides"][platform_key]` (if
    both `platform_key` and a matching override exist) > `brand["audience"]`
    > None (if `brand` is falsy). Backward compatible: a brand entry with no
    `platform_audience_overrides` key behaves exactly as before.

    `platform_key` should be the resolved template key or CLI alias (e.g.
    "livejournal", "devto") - match it against whatever keys you add under
    a brand's `platform_audience_overrides` map in config.json.

    Wired into generate.py's `resolve_audience()`, which passes the
    lowercased `--platform` string (single-run) or CSV `platform` value
    (bulk mode) through as `platform_key`.
    """
    if not brand:
        return None
    overrides = brand.get("platform_audience_overrides") or {}
    if platform_key and platform_key in overrides:
        return overrides[platform_key]
    return brand.get("audience")
