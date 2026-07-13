# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0]

### Added
- Market registers: each brand in `config.json` declares a `market` (`b2b`
  default, `b2c`, or `creator`) that selects a per-market voice block from
  `templates/_shared.py`'s `MARKET_VOICE_RULES`, resolved from `--url` and
  passed to every template. Fully backward compatible (no field = `b2b`).
- Four creator/influencer/personal-brand templates: `influencer_outreach`
  and `ugc_brief` (`templates/creator.py`, brand side, FTC-disclosure-aware),
  `personal_brand_post` and `creator_media_kit` (`templates/personal.py`,
  individual side, four-pillar rotation + no-fabricated-numbers rules).
- Four content-type templates: `short_form_video` (Reels/Shorts/TikTok
  scripts), `landing_page` (conversion copy), `comparison_page` ("X vs Y"
  SEO pages with competitor-fact guardrails), and `business_case_one_pager`
  (internal budget-justification memo).
- Six strategy docs: GMB, LiveJournal, Tumblr, Quora, influencer
  collaborations, and personal brand - the latter two grounded in cited
  2026 research.
- `publish_tracker_template.csv`: the real governance/review tracker the
  docs previously referenced without shipping.

### Fixed
- CI now installs the `llm` extras and imports all three provider SDKs
  (`anthropic`, `google.genai`, `openai`) so a future SDK deprecation or
  breaking change is caught automatically instead of going unnoticed.
- CI's post-install verification step now runs a `content-wiz --list` smoke
  check so a broken console-script entry point fails the build.
- `hooks/pre-commit` is now tracked as executable (`755`) in git, and now
  also runs `ruff check .` to match what CI enforces.
- `.ruff_cache/` is now explicitly ignored via `.gitignore`.
- Pinned upper bounds on the `anthropic`, `google-genai`, and `openai`
  dependency ranges to avoid silently picking up a future breaking major
  release.

### Changed
- Raised the minimum supported Python version from `3.8` to `3.9` (3.8
  reached end-of-life in October 2024); CI matrix updated to `3.9`/`3.12`.

## [0.3.0]

### Added
- Provider-agnostic `--generate` support: live content generation via
  Claude (Anthropic), Gemini (Google), or OpenAI/Codex, selectable per run.

### Changed
- Migrated Gemini support off the end-of-life `google-generativeai` SDK to
  its successor, `google-genai>=1.0`.

## [0.2.0] and earlier

- Multi-brand content-distribution prompt generator: single + bulk
  generation modes, per-platform templates (blog, social, growth,
  community, local, video, PR, and more), config-driven brand/audience
  overrides, content-rule linting, and CI/test tooling.
- See `git log` for the full history prior to this changelog's introduction.
