# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
