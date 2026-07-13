# agents.md - Edstellar Content Creation

## Project overview
A B2B content-distribution **prompt generator** for Edstellar (and Invensis Learning).
It does not call any LLM. It assembles fully-specified prompts from parameterized
templates and writes them to `output/` for a human to paste into an AI tool. Prompts
encode channel strategy, brand voice, and formatting rules so output is consistent.

Two layers, partially overlapping:
1. **Automated layer** - `generate.py` + `templates.py`: 25 content types wired to a CLI.
2. **Manual layer** - `prompts/*.txt`: 49 hand-run prompt files, some not yet in the CLI.
   See the CLI Coverage table in `README.md` for exactly which is which.

## Stack
- Python 3 (standard library only - `argparse`, `csv`, `zipfile`, `datetime`). No deps.
- No package manager, no build step. `test_generate.py` uses stdlib `unittest`.

## Key files & dirs
- `generate.py` - CLI entry point. `PLATFORM_MAP` (alias → template key),
  `SUBFOLDER_MAP` (key → output folder), single-run + `--bulk` CSV modes.
- `templates.py` - one function per template key; each returns a prompt string.
  All take `**_` so extra kwargs never raise. ~3.3k lines, pure string building.
- `prompts/` - standalone prompt text; `_Brand_Detection_Rules.txt` is shared by all.
- `strategies/` - one strategy doc per channel (goal, structure, cadence, failure modes).
- `data/HARO_DataBank.csv` - citable stats. Columns: Claim | Source | URL | Year |
  Context | Quotable Version | Topic Tags. Add a row per new first-party stat.
- `output/` - generated prompts, auto-routed into per-type subfolders. `LiveJournal/`
  and `Tumblr/` are legacy manual content, not produced by the CLI.
- `bulk_template.csv` - column template for `--bulk`.

## How to run
```bash
# Single prompt (prints + saves to output/<Type>/)
python generate.py --platform newsletter --topic "L&D budget planning"

# See all platform aliases
python generate.py                      # errors with usage
python generate.py --platform blog --topic "..." --wordcount 1500 --cta "https://edstellar.com/x"

# Repurpose an existing file into a target platform
python generate.py --repurpose path/to/source.md --platform twitter --topic "..."

# Bulk: reads a CSV, writes a ZIP + run-log CSV into output/
python generate.py --bulk bulk_template.csv
```

## How to test
```bash
python -m unittest test_generate -v
```
Tests guard against drift: every alias must resolve to a template, every key must
render a non-empty prompt and have a `SUBFOLDER_MAP` entry, and no em-dash may leak
into rendered output.

## Env vars
None. No secrets, no API keys, no network calls.

## Agent notes / gotchas
- **`gmb` and `pinterest` are print-only** in single-run mode (`PRINT_ONLY`); they
  write no file. They still get a folder inside the bulk ZIP.
- **Alias trap:** `--platform linkedin` → `blog_writing` (a blog), NOT a LinkedIn post.
  Use `linkedin_post` for posts.
- **No em-dashes anywhere** is a hard content rule (README rule #1). Keep prompt files,
  templates, and generated output free of `—`. The test suite enforces it for output.
- Every statistic in generated content must name source + organization + year.
- When adding a new content type: add the `templates.py` function, a `PLATFORM_MAP`
  alias, a `SUBFOLDER_MAP` entry, and a `README.md` CLI Coverage row **in the same
  change** - the tests and doc table will otherwise drift.
- Templates are large; grep for the `def <key>(` line, don't read the whole file.
