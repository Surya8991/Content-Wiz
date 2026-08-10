"""Optional single-source registry for templates (v0.10.7).

The historical shape of Content-Wiz is that every new template requires touching
three places in generate.py: `PLATFORM_MAP` (alias -> template key),
`SUBFOLDER_MAP` (template key -> output subfolder), and sometimes
`_SPECIALIZED_KWARGS` (template key -> extra kwargs). That's error-prone and
easy to leave inconsistent - a template can be added to `templates/__init__.py`
but omitted from either map and the CLI will happily accept it with a wrong
subfolder or `KeyError` at runtime.

This module gives new templates a `@register` decorator that co-locates all
three registrations with the template function itself. Existing templates are
NOT retrofitted (that would be a massive diff); instead this file offers a
`consistency_check()` used by test_generate.py to catch a template added to
`templates/__init__.py` but not to `PLATFORM_MAP`.

To use for a new template:

    from templates.registry import register

    @register(aliases=("my_thing", "mything"), subfolder="My_Thing")
    def my_thing(topic, audience, **_):
        return f"…prompt text…"

Then in generate.py, call `templates.registry.export_into_maps(PLATFORM_MAP,
SUBFOLDER_MAP)` once at import time to fold the registered entries in. Kept
optional so existing hand-maintained maps still win when both define an alias.
"""
from __future__ import annotations

# alias -> template_key
_ALIASES: dict[str, str] = {}
# template_key -> subfolder
_SUBFOLDERS: dict[str, str] = {}
# template_key -> callable that returns extra kwargs from (topic, audience, platform)
_SPECIALIZED: dict[str, object] = {}


def register(aliases, subfolder, specialized=None):
    """Decorator: co-locate a template's aliases, output subfolder, and
    optional specialized-kwargs factory with its function definition."""
    if isinstance(aliases, str):
        aliases = (aliases,)
    if not aliases:
        raise ValueError("register(): at least one alias is required")

    def wrap(fn):
        key = fn.__name__
        for alias in aliases:
            if alias in _ALIASES and _ALIASES[alias] != key:
                raise ValueError(
                    f"registry: alias '{alias}' already maps to '{_ALIASES[alias]}', "
                    f"cannot re-register to '{key}'"
                )
            _ALIASES[alias] = key
        _SUBFOLDERS[key] = subfolder
        if specialized is not None:
            _SPECIALIZED[key] = specialized
        return fn

    return wrap


def export_into_maps(platform_map, subfolder_map, specialized_map=None):
    """Fold registered entries into the hand-maintained maps in generate.py.
    Hand-maintained entries always win: existing keys are never overwritten,
    so the retrofit path stays backward-compatible."""
    for alias, key in _ALIASES.items():
        platform_map.setdefault(alias, key)
    for key, folder in _SUBFOLDERS.items():
        subfolder_map.setdefault(key, folder)
    if specialized_map is not None:
        for key, fn in _SPECIALIZED.items():
            specialized_map.setdefault(key, fn)


def consistency_check(templates_module, platform_map, subfolder_map):
    """Return a list of consistency problems between `templates_module`'s
    public callables and the hand-maintained maps in generate.py.

    Reports each of:
      - template functions with no PLATFORM_MAP alias
      - PLATFORM_MAP keys that don't map to any templates.<key> function
      - PLATFORM_MAP keys with no SUBFOLDER_MAP entry
    Returns an empty list if everything is aligned.
    """
    problems = []
    template_fns = {
        name for name in dir(templates_module)
        if not name.startswith("_") and callable(getattr(templates_module, name))
    }
    routed_keys = set(platform_map.values())
    # Known exempt keys that don't need their own PLATFORM_MAP alias:
    # `medium_step1` and `medium_step2` are handled specially in build_prompt.
    exempt_missing_alias = {"medium_step1", "medium_step2", "market_voice",
                             "tone_modifier", "market_persona_label"}
    for fn_name in sorted(template_fns):
        if fn_name in exempt_missing_alias:
            continue
        if fn_name not in routed_keys and fn_name != "medium":
            problems.append(
                f"template `{fn_name}` has no PLATFORM_MAP alias - won't be "
                f"reachable from the CLI"
            )
    for key in sorted(routed_keys):
        if key == "medium":
            continue  # handled specially in build_prompt
        if key not in template_fns:
            problems.append(
                f"PLATFORM_MAP routes to template key `{key}` but no "
                f"templates.{key} function exists"
            )
        if key not in subfolder_map:
            problems.append(
                f"PLATFORM_MAP key `{key}` has no SUBFOLDER_MAP entry - "
                f"would silently land in Misc/"
            )
    return problems
