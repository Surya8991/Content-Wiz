"""Loads config.json (brands + defaults). Single source of truth for config.

Falls back to hardcoded defaults if config.json is missing or unreadable, so the
tool never hard-fails on a config problem.
"""
import copy
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
        return copy.deepcopy(_FALLBACK)
    # Merge missing default keys from fallback so callers can rely on all keys.
    # Deep-copy the fallback so callers mutating merged["brands"] (or defaults)
    # never leak into the module-level _FALLBACK dict.
    merged = copy.deepcopy(_FALLBACK)
    for k, v in data.items():
        if k == "defaults":
            merged["defaults"].update(v)
        else:
            merged[k] = v
    return merged


CONFIG = load()
DEFAULTS = CONFIG["defaults"]
BRANDS = CONFIG["brands"]


def _hostname(url):
    """Extract a lowercased hostname from `url`, tolerating scheme-less input.

    `edstellar.com`, `www.edstellar.com`, `https://edstellar.com/x?y=1`, and
    `mailto:foo@edstellar.com` all normalize to `edstellar.com` (www stripped).
    """
    from urllib.parse import urlparse

    if not url:
        return ""
    s = url.strip()
    if "://" not in s and not s.startswith("//"):
        s = "//" + s  # let urlparse treat it as netloc, not path
    host = (urlparse(s).hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    return host


def brand_for_url(url):
    """Return the brand dict for a URL by matching its hostname against the
    registered brand keys in `config.json`, or None.

    A brand key `edstellar.com` matches hostnames `edstellar.com` and
    `blog.edstellar.com`, but NOT `edstellar.com.attacker.com` or
    `notedstellar.com` — the previous naive `in` check accepted both, which
    let a lookalike URL borrow a real brand's audience and voice.
    """
    if not url:
        return None
    host = _hostname(url)
    if not host:
        return None
    for domain, brand in BRANDS.items():
        d = domain.strip().lower().lstrip(".")
        if not d:
            continue
        if host == d or host.endswith("." + d):
            return brand
    return None


def market_for_brand(brand):
    """Return the brand's market register ("b2b", "b2c", or "creator").

    Defaults to "b2b" for a missing/empty/whitespace-only field or a falsy
    brand, so every pre-existing brand entry keeps its original voice
    unchanged. Whitespace is stripped so " b2c " resolves to "b2c" instead of
    silently falling back to the b2b voice.
    """
    if not brand:
        return "b2b"
    market = (brand.get("market") or "").strip().lower()
    return market or "b2b"


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
