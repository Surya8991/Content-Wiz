# agents.md - Content Wiz

## Project overview
A generic, multi-brand B2B content-distribution **prompt generator**. It is not
built for one company: `config.json`'s `brands` map (keyed by domain) holds each
brand's name, description, audience, and hashtag, and `--url yourdomain.com` at
generation time auto-fills the audience from the matching entry. Edstellar and
Invensis Learning ship as example brand configs in `config.json`, not the tool's
identity - add, edit, or delete brand entries freely. By default the tool assembles
fully-specified prompts and writes them to `output/` for a human to paste into an AI
tool. With `--generate` it can also call the Anthropic API and write finished content
directly. Prompts encode channel strategy, brand voice, and formatting rules so
output is consistent.

Two prompt layers, one unified CLI:
1. **Rich templates** - `templates/`: 27 parameterized prompt builders, split by
   domain (`local.py`, `blog.py`, `social.py`, `community.py`, `video.py`,
   `growth.py`, `pr.py`), re-exported at the package level via `__init__.py` so
   `templates.<fn>` and `getattr(templates, key)` work exactly as before.
2. **Text prompts** - `textprompts.py`: loads the flat `prompts/*.txt` files and
   substitutes tokens. Every prompt file is now reachable from the CLI.
`generate.resolve(alias)` dispatches to the right layer. `python generate.py --list`
prints the authoritative alias list.

## Stack
- Python 3 (standard library only for the core tool). No required deps.
- Optional: `anthropic` (only for `--generate`), `ruff` (dev lint).
- `pyproject.toml` defines the `content-wiz` console entry point.

## Key files & dirs
- `generate.py` - CLI entry point. `PLATFORM_MAP` (alias → template key),
  `SUBFOLDER_MAP` (key → folder), `resolve()`/`build_prompt()`, single + `--bulk` modes.
  Reconfigures stdout to UTF-8 so prompt printing never crashes on Windows consoles.
- `templates/` - one function per template key; each returns a prompt string.
  All take `**_` so extra kwargs never raise. `_shared.py` holds the three
  cross-cutting rule blocks (`HUMAN_WRITING_RULES`, `RANKABILITY_RULES`,
  `RESEARCH_RULES`); every other file imports from it. New template: add the
  function to whichever domain module fits (or start a new one), then add its
  name to that module's import line in `__init__.py`.
- `textprompts.py` - `TEXT_PROMPT_MAP` (alias → file + folder) + `render()`.
- `config.py` / `config.json` - brands + defaults (audience, wordcount, LLM model).
- `llm.py` - optional Anthropic call; raises a clean RuntimeError if key/SDK missing.
- `lint_content.py` - fails on em-dashes in prompt/strategy/template source.
- `prompts/` - standalone prompt text; `_Brand_Detection_Rules.txt` is shared by all.
- `strategies/` - one strategy doc per channel (goal, structure, cadence, failure modes).
- `data/HARO_DataBank.csv` - citable stats. Columns: Claim | Source | URL | Year |
  Context | Quotable Version | Topic Tags. Add a row per new first-party stat.
- `output/` - generated prompts/content, auto-routed into per-type subfolders.
  `LiveJournal/` (`livejournal_post`, aliases `livejournal`/`lj`) and `Tumblr/`
  (`tumblr_post`, alias `tumblr`) are CLI-routed like every other platform; any
  files in those folders not matching the CLI's date-stamped naming were placed
  there manually.

## How to run
```bash
python generate.py --list                                   # every alias
python generate.py --platform newsletter --topic "L&D budget planning"
python generate.py --platform whitepaper --topic "AI skills gap"   # a text prompt
python generate.py --platform blog --topic "..." --dry-run  # print, don't write
python generate.py --repurpose src.md --platform twitter --topic "..."
python generate.py --bulk bulk_template.csv                 # ZIP + run-log CSV

# Live content generation (needs a key + SDK)
export ANTHROPIC_API_KEY=sk-ant-...
python generate.py --platform faq --topic "..." --generate
```

## How to test / lint
```bash
python -m unittest test_generate -v   # 21 smoke tests
python lint_content.py                # content-rule lint
ruff check .                          # style lint
git config core.hooksPath hooks       # enable pre-commit hook (once per clone)
```
CI runs all three (`.github/workflows/ci.yml`).

## Env vars
- `ANTHROPIC_API_KEY` - only needed for `--generate`. Never commit it.

## Agent notes / gotchas
- **`gmb` and `pinterest` are print-only** in single-run mode (`PRINT_ONLY`) unless
  `--generate` is used; they still get a folder inside the bulk ZIP.
- **Alias trap:** `--platform linkedin` → `blog_writing` (a blog), NOT a LinkedIn post.
  Use `linkedin_post`.
- **No em-dashes anywhere** is a hard rule; `lint_content.py` + tests enforce it.
- **Two alias maps must not collide** - a test asserts `PLATFORM_MAP` and
  `TEXT_PROMPT_MAP` share no aliases. Keep new aliases unique.
- Adding a rich type: fn in a `templates/*.py` module + its `__init__.py` import
  + `PLATFORM_MAP` alias + `SUBFOLDER_MAP` entry + README row, same change.
  Adding a flat type: drop the `.txt` + one `TEXT_PROMPT_MAP` row. Tests and the
  doc tables will otherwise drift.
- Templates are large; grep for `def <key>(` across `templates/`, don't read whole files.
- **Citations are not auto-verified.** Rule 4/8 in README's Global Content Rules
  requires every statistic to name a real source, org, and year, but nothing in
  `generate.py`/`lint_content.py` checks that the citation is actually accurate,
  a model can name a real report and still misstate the finding. Before marking
  a batch ready to publish, run the citation-verification pass described in
  README's "Citation Verification" section (per-batch web research against every
  cited claim, tighten/correct/soften as needed). `data/HARO_DataBank.csv` rows
  marked `[PLACEHOLDER]` are first-party internal data, not web-researchable;
  they live in `data/HARO_DataBank_PENDING.csv` until filled in and moved over.
- **"Companion piece" cross-links can't be added before publish.** A post can
  reference a related piece by topic in plain text, but never link to a
  fabricated URL, Dev.to/Hashnode/etc. assign the real URL at publish time.
  Once the companion piece's `Published URL` is filled in on the content
  calendar tracker, go back and turn the plain-text reference into a real link.
