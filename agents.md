# agents.md - Content Wiz

## Project overview
A generic, multi-brand content-distribution **prompt generator** covering B2B,
B2C, and creator/personal-brand markets. It is not built for one company:
`config.json`'s `brands` map (keyed by domain) holds each brand's name,
description, audience, hashtag, and `market` register (`b2b` default, `b2c`,
or `creator` - selects the voice block from `templates/_shared.py`'s
`MARKET_VOICE_RULES` that flows into templates via `build_prompt`'s `market`
kwarg), and `--url yourdomain.com` at generation time auto-fills the audience
and market from the matching entry. Edstellar and
Invensis Learning ship as example brand configs in `config.json`, not the tool's
identity - add, edit, or delete brand entries freely. By default the tool assembles
fully-specified prompts and writes them to `output/` for a human to paste into an AI
tool. With `--generate` it can also call an LLM directly and write finished content -
Anthropic/Claude, Google/Gemini, or OpenAI/Codex-GPT, chosen with `--provider` (see
`llm.py`) - so the same prompt/rule set produces the same house-style content
regardless of which model actually writes it. Prompts encode channel strategy, brand
voice, and formatting rules so output is consistent across platforms and providers.

Two prompt layers, one unified CLI:
1. **Rich templates** - `templates/`: 40 parameterized prompt builders, split by
   domain (`local.py`, `blog.py`, `social.py`, `community.py`, `creator.py`,
   `personal.py`, `video.py`, `growth.py`, `pr.py`), re-exported at the package
   level via `__init__.py` so `templates.<fn>` and `getattr(templates, key)`
   work exactly as before.
2. **Text prompts** - `textprompts.py`: loads the flat `prompts/*.txt` files and
   substitutes tokens. Every prompt file is now reachable from the CLI.
`generate.resolve(alias)` dispatches to the right layer. `python generate.py --list`
prints the authoritative alias list.

## Stack
- Python 3 (standard library only for the core tool). No required deps.
- Optional, only for `--generate`, install just the provider(s) you use:
  `anthropic` (`pip install .[llm-anthropic]`), `google-genai`
  (`.[llm-gemini]`), `openai` (`.[llm-openai]`), or `.[llm]` for all three.
  `ruff` (`.[dev]`) for style lint.
- `pyproject.toml` defines the `content-wiz` console entry point.

## Key files & dirs
- `generate.py` - CLI entry point. `PLATFORM_MAP` (alias → template key),
  `SUBFOLDER_MAP` (key → folder), `resolve()`/`build_prompt()`, single + `--bulk` modes.
  Reconfigures stdout to UTF-8 so prompt printing never crashes on Windows consoles.
- `templates/` - one function per template key (except `medium`, a 2-step
  builder dispatching to `medium_step1`/`medium_step2`); each returns a
  prompt string.
  All take `**_` so extra kwargs never raise. `_shared.py` holds the
  cross-cutting rule blocks (`HUMAN_WRITING_RULES`, `RANKABILITY_RULES`,
  `RESEARCH_RULES`, `BANNED_CTA_PHRASES`, `MARKET_VOICE_RULES` +
  `market_voice()`); every other file imports from it. New template: add the
  function to whichever domain module fits (or start a new one), then add its
  name to that module's import line in `__init__.py`.
- `textprompts.py` - `TEXT_PROMPT_MAP` (alias → file + folder) + `render()`.
- `config.py` / `config.json` - brands + defaults (audience, wordcount, LLM
  provider/model). `defaults.llm_provider` picks the default provider;
  `defaults.llm_models` maps provider name → default model id for that
  provider, so switching `--provider` without a `--model` override still
  gets a sane model.
- `llm.py` - optional live generation, provider-agnostic (Anthropic/Claude, Google/Gemini,
  OpenAI/Codex-GPT behind one interface, selected via `--provider` or `config.json`'s
  `defaults.llm_provider`). Raises a clean RuntimeError if that provider's key/SDK is missing.
  Every provider's SDK is imported lazily, so picking one never requires installing the others.
- `lint_content.py` - fails on em-dashes in prompt/strategy/template source.
- `prompts/` - standalone prompt text; `_Brand_Detection_Rules.txt` is shared by all.
- `strategies/` - one strategy doc per channel (goal, structure, cadence, failure modes).
- `data/HARO_DataBank.csv` - citable stats. Columns: Claim | Source | URL | Year |
  Context | Quotable Version | Topic Tags. Add a row per new first-party stat.
- `publish_tracker_template.csv` - the real, reusable governance/publish tracker
  template (repo root). Copy it to a dated file at the start of each publishing
  cycle; do not edit the template in place. See the "Governance / review gate"
  gotcha below for the sign-off rule it enforces.
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

# Live content generation (needs that provider's key + SDK installed)
export ANTHROPIC_API_KEY=sk-ant-...
python generate.py --platform faq --topic "..." --generate                    # defaults to anthropic

export GEMINI_API_KEY=...       # or GOOGLE_API_KEY
python generate.py --platform faq --topic "..." --generate --provider gemini

export OPENAI_API_KEY=sk-...
python generate.py --platform faq --topic "..." --generate --provider openai --model gpt-5
```

## How to test / lint
```bash
python -m unittest test_generate -v   # smoke tests (grows over time - see test output for current count)
python lint_content.py                # content-rule lint
ruff check .                          # style lint
git config core.hooksPath hooks       # enable pre-commit hook (once per clone)
```
CI runs all three (`.github/workflows/ci.yml`).

## Env vars
- `ANTHROPIC_API_KEY` - only needed for `--generate --provider anthropic` (the default).
- `GEMINI_API_KEY` (or `GOOGLE_API_KEY` as a fallback) - only needed for `--generate --provider gemini`.
- `OPENAI_API_KEY` - only needed for `--generate --provider openai`.
Never commit any of these.

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
- **Source-diversity rule (standing rule).** Within any content cluster
  (multiple posts published close together on related topics), never reuse
  the exact same single source (e.g. "Gallup's State of the Global
  Workplace") as the sole statistical anchor across more than one post in
  that cluster. A vague reference like "Harvard Business Review has written
  extensively about..." with no article title or year is never acceptable;
  a citation must name a specific report/article and year every time.
- **Cluster Citation Diversity Pass (standing process, run before publish
  on any batch/cluster flagged for this).** Two variants depending on the
  problem:
  - (a) Repeated generic promotional stats in one batch (e.g. the GMB
    batch's unsourced "$438 billion annually" claims): list every
    stat-bearing sentence in the batch, WebSearch for the real source for
    each one, then either cite it with exact org + year + figure if found,
    or remove the stat / replace it with a qualitative claim if it cannot
    be confirmed after a real search effort. Never fabricate a
    precise-sounding replacement number.
  - (b) One cluster leaning on a single repeated source (e.g. the
    LiveJournal Gallup/HBR reuse): identify which posts in the cluster
    share a source, WebSearch for distinct, verifiable alternative reports
    covering the same underlying claim for all but one of the posts,
    confirm each alternative source actually supports the specific claim
    being made (not just the general topic), then replace and re-run
    `lint_content.py` to confirm no em-dash/passive-voice violations were
    introduced by the edit.
  This is the same research process described in README's "Citation
  Verification" section, this is just the name to refer to it by
  ("run a Cluster Citation Diversity Pass on X") when scoping the work.
- **Governance / review gate (standing rule, not yet code-enforced).** No
  content in this pipeline has an enforced human sign-off gate before
  landing in `output/`. The only automated enforcement anywhere in the
  pipeline is the em-dash/passive-voice linter (`lint_content.py`); it does
  not check citation accuracy, brand-safety, or claim validity. Standing
  rule going forward: any stat-bearing post, or any post using first-person/
  confessional voice, requires a human reviewer's sign-off (name + date,
  tracked on the content calendar tracker) before its `Status` can move to
  "Published." Use `publish_tracker_template.csv` (repo root) for this: it
  is a generic, reusable tracker template with `Reviewed By`/`Review Date`
  columns built in, plus `Status`, `Clicks`, `Leads/Conversions`, and
  `Last Checked` for basic performance follow-up. At the start of each
  publishing cycle, copy it to a dated working file (e.g.
  `jul2026_publish_tracker.csv`) and fill it in per batch, do not edit the
  template in place. This is currently a process discipline enforced by
  humans following the rule, not something `generate.py`/`lint_content.py`
  can block on.
- **Disclosure rule for first-person/confessional voice (standing rule,
  decided).** Any template using first-person "I" voice (e.g. LiveJournal's
  confessional style) must either (a) be clearly disclosed as a branded
  persona/sponsored content, or (b) not claim specific personal
  biographical detail that isn't true of any real author. This repo's
  templates already implement (a): `templates/community.py`'s
  `livejournal_post` requires a byline line immediately after the `<h1>`
  that either names a real configured persona ("Written by [Author Name],
  [Title] at [Brand]") or discloses brand authorship directly ("Posted on
  behalf of [Brand]") when no individual author is used. Never generate or
  approve first-person content with an undisclosed "I" voice and no byline.
- **Multi-provider output quality caveat.** `--generate` is provider-agnostic
  in the sense that the same prompt and house-style rules are sent to
  whichever provider is selected, it is not a guarantee of equal output
  quality. Providers vary in instruction-following fidelity, reasoning
  depth, and hallucination rate on long, structured prompts (the kind this
  repo's templates produce). Give closer editorial review to output from
  any non-default provider until it has been validated against this repo's
  specific templates; do not assume Gemini/OpenAI output needs the same
  degree of scrutiny as the Anthropic/Claude default.
- **Strategy-doc platform claims are point-in-time, not permanent facts.**
  Any strategy doc under `strategies/` that names a specific platform
  feature, filter, or API (e.g. a search console filter, an algorithm
  change, a named product surface) is describing that platform as of the
  doc's last-updated date. Platforms change these without notice, treat
  such claims as needing periodic re-verification against the platform's
  current documentation, not as durable facts to cite indefinitely.
- **DataBank-only sourcing rule (standing rule).** Any first-party or
  proprietary-sounding statistic in generated content (e.g. "40% larger
  L&D budgets" attributed to internal program analysis) should be
  traceable to a row in `data/HARO_DataBank.csv`, not generated ad hoc by
  the model from general knowledge. External academic/industry stats
  (Gartner, Verizon DBIR, Gallup, etc.) are exempt from this rule; they
  instead fall under the Citation Verification research process above.
