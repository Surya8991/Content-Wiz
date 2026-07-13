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
        "llm_model": "claude-sonnet-5",
        "llm_max_tokens": 4096,
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
