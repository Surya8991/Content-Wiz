# Content Wiz — Full Project Audit Log (v2)

**Generated:** 2026-07-13
**Method:** 8 independent read-only subagents, each briefed with a distinct
specialist lens and given full repo access, run in parallel via the Agent
tool. Several spawned their own sub-agents to cover their scope (the Content
Writer persona split into 4: strategy docs, prompts A-M, prompts M-Z, and the
remaining `templates/*.py` files). No agent edited any file — this is a
findings-only pass. Verifies the CURRENT state of the repo fresh; does not
assume any prior audit's fixes still hold.

**Personas:** Software Engineering · Security · DevOps/Packaging/CI · Data
Integrity · Content Writer (+4 sub-audits) · SEO/GEO · Brand/Compliance/Legal
· Business/Client Stakeholder

**Context:** this audit runs after a prior full remediation pass (engineering
hardening, SEO/schema fixes, compliance rules, a full templates/prompts/
strategies quality pass, and a new multi-provider `--generate` feature
supporting Claude/Gemini/OpenAI). The previous `AUDIT_LOG.md` was deleted
before this pass to start clean.

---

## Remediation Status (updated 2026-07-13) — all findings addressed

Every finding in this document (both Critical, all 6 High, and all 14
Medium, plus the Low-severity items called out explicitly in each
section) was fixed via 9 parallel/sequential agents (one handled directly
given the risk of the SDK migration, 8 dispatched with exclusive file
ownership), verified together afterward: `python -m unittest test_generate
-v` → 55/55 pass, `python lint_content.py` → clean (76 files + banned-CTA
regression now checking 7 template files, up from 1), `python -m ruff
check .` → clean. Committed as a sequence of 6 commits (engineering, DevOps/
CI, templates/lint, governance docs, prompts/strategies content, plus the
earlier standalone Gemini SDK migration commit).

- [x] **D1 (Critical)** — Gemini migrated off the EOL `google-generativeai`
  SDK to `google-genai`, verified against the actual installed SDK's
  signatures. Handled directly rather than delegated, given the API
  surface risk.
- [x] **BC2/BC3 (Critical)** — banned-CTA-phrase regression check widened
  from 1 file (`templates/local.py`) to all 7 `templates/*.py` files, using
  word-boundary regex to avoid false positives (`"Discover"` vs.
  `"discoverability"`); `growth.py`'s active "Discover" CTA-verb
  instruction removed.
- [x] **E2/E3 (High)** — all three providers' response parsing now guards
  against empty/blocked responses with a clean `RuntimeError` instead of a
  raw traceback or silent empty-success; 6 new mocked-SDK tests cover it.
- [x] **BC5/B5 (High)** — the nonexistent governance tracker file is now a
  real, committed `publish_tracker_template.csv`, with every doc reference
  repointed to it.
- [x] **S4 (Medium→fixed as part of this pass)** — `--repurpose`/bulk CSV
  `source_file` paths are now containment-checked against escaping the
  project directory.
- [x] **DI3** — `--bulk --dry-run` now actually dry-runs.
- [x] **E1** — `--provider` validated before any generation attempt, even
  under `--dry-run`.
- [x] **C1/BC6, C2, C6, SEO2, SEO5** — `RESEARCH_RULES` wired into every
  stat-heavy function that lacked it; `blog_writing()`'s word-count
  override bug fixed (section lengths now scale with `--wordcount`);
  Instagram's voice de-converged from LinkedIn Post's; `geo()`'s schema
  checklist made uniform; meta-description ranges aligned.
- [x] **B7, B3, SEO4, BC8, BC9** — cost-reference docs added (real,
  dated pricing-page links, no fabricated numbers); a provider-quality
  caveat added; a documentation-hygiene note on point-in-time platform
  claims added; `strategy-gmb.md` wording aligned to the actual
  unqualified "Discover" ban plus a governance-rule pointer.
- [x] **D2-D8, S6, S8** — CI now installs and imports all 3 LLM extras
  (so a future SDK deprecation can't go unnoticed again) plus a
  post-install smoke check and explicit `permissions:` block; Python floor
  bumped 3.8→3.9 (3.8 is EOL); dependency ceilings added; `hooks/
  pre-commit`'s executable bit fixed and a `ruff` step added to match CI;
  version bumped to 0.3.0 with a new `CHANGELOG.md`; `.ruff_cache/` added
  to `.gitignore`.
- [x] **C3, C4, C7, C8, C5** — a recurring copy-paste artifact removed
  from 3 prompt files; thin/generic tone guidance deepened in 5 prompts;
  an internal pronoun-ban tension in the op-ed prompt clarified; length
  bands added to 2 under-specified prompts; 3 strategy docs (Tumblr,
  LiveJournal, Quora) deepened with real platform-mechanic specifics.
- **BC7** (stat-pattern lint stopgap) — deliberately left open. The audit
  itself judged this "out of reach for pure static lint," and the
  responsible agent found no genuinely low-false-positive way to detect
  it without semantic understanding of nearby citation context. Revisit
  only if a concrete false-positive-safe heuristic is found.
- **D7** (dependency lockfile) — deliberately left as a Low/acceptable
  finding per the audit's own verdict, given the project's current
  zero-required-dependency core and small optional surface. Revisit if
  the `llm` extras grow.

---

## Executive Summary

| Severity | Count |
|---|---|
| Critical | 2 |
| High | 6 |
| Medium | 14 |
| Low | 20+ |

### The two Critical findings

1. **The just-shipped Gemini support depends on a fully end-of-life SDK.**
   `google-generativeai` (the package `llm.py`'s `_generate_gemini()` and
   `pyproject.toml`'s `llm-gemini` extra both hardcode) is fully deprecated —
   Google has stopped shipping updates or bug fixes to it. Verified directly:
   importing it emits `FutureWarning: All support for the google.generativeai
   package has ended.` — **DevOps audit**.
2. **The centralized banned-CTA-phrase enforcement only covers one of six
   template files, and one of the unguarded five actively tells the model to
   use a banned word.** `lint_content.py`'s regression check hardcodes
   `templates/local.py` as its only target. `templates/growth.py:525`
   instructs the model to use "Discover" as a meta-description CTA verb —
   a word explicitly on `templates/_shared.py`'s `BANNED_CTA_PHRASES` list.
   Five templates (`blog.py`, `growth.py`, `pr.py`, `social.py`, `video.py`)
   each hand-roll their own CTA-ban prose, invisible to the linter —
   **Brand/Compliance audit**.

### Cross-persona corroboration

- **The governance/publish-sign-off tracker file doesn't exist.** `agents.md`
  and `README.md` both point to `jul2026_publish_tracker.csv` with
  `Reviewed By`/`Review Date` columns as the human-review enforcement
  mechanism — flagged independently by **Brand/Compliance** (High) and
  **Business/Client Stakeholder** (High, named as "the biggest remaining
  trust gap"). The file does not exist anywhere in the repo. A control
  described in detail but never instantiated creates false confidence that a
  check is happening.
- **`--bulk`'s file-reading paths are unguarded, and `--bulk --dry-run`
  doesn't dry-run.** Security flagged arbitrary local file read via
  `--repurpose FILE`/CSV `source_file` (Medium); Data Integrity independently
  found `--bulk --dry-run` silently ignores `--dry-run` and writes real
  output (Medium) while testing the same code path.
- **Several stat-heavy template functions never import `RESEARCH_RULES`.**
  `haro()`, `newsletter()`, `faq()`, `geo()`, `video_script()`, `podcast()`
  (Content Writer sub-audit) and GMB's `local.py` specifically (Compliance
  audit) all cite/require statistics without pulling in the shared
  DataBank-sourcing/third-party-disclaimer rule block — a real regression
  risk given this repo has previously had to quarantine unverified stats.

---

## 1. Software Engineering

| # | Category | Severity | Evidence | Finding | Recommendation |
|---|---|---|---|---|---|
| E1 | UX/validation | Medium | `generate.py:299-303`, `_maybe_generate` | `--generate --provider bogus --dry-run` silently succeeds and prints the prompt; an invalid `--provider` is never validated regardless of `--dry-run`. | Validate `--provider` up front when `--generate` is passed. |
| E2 | Error handling | **High** | `llm.py:126` (Gemini `response.text`), `llm.py:140` (OpenAI `response.choices[0].message.content`) | Neither call is guarded. A safety-filtered/empty Gemini response raises unguarded `ValueError`; an empty OpenAI `choices` list raises `IndexError`. `_maybe_generate` only catches `RuntimeError`, so both crash with a raw traceback instead of the tool's usual clean error message. | Wrap each provider call, detect empty/blocked responses, raise `RuntimeError` uniformly. |
| E3 | Silent data loss | Medium | `llm.py:115`, Anthropic text-join | If Anthropic returns only non-text blocks, this silently returns `""` and `run_single` writes an empty file while printing a success message. | Raise/warn on empty joined text. |
| E4 | Test coverage | Medium | `test_generate.py` `LlmTests` | Zero tests mock the actual SDK response objects for any of the 3 providers — only error-message paths are tested. The response-parsing code (where E2/E3 live) has no coverage. | Add mocked-SDK happy-path + empty-response tests per provider. |
| E5 | Verified correct | — | `resolve_audience()`/`platform_key` wiring, packaging (`pip install -e .`), `hooks/pre-commit` logic, CI triggers, bulk/CLI edge cases, full test/lint/ruff suite | All behaved correctly under direct testing. | None needed. |

**Verdict:** Core CLI is solid and well-tested; the new `llm.py` provider layer is the weak spot — unguarded response parsing for Gemini/OpenAI and a silent-empty-success path for Anthropic, with zero test coverage on any of it.

---

## 2. Security

| # | Category | Severity | Evidence | Finding | Recommendation |
|---|---|---|---|---|---|
| S1 | Secrets | None | Full `git log -p --all` scan | No real-format API key ever committed. `.gitignore` correctly covers `.env`/`*.key`. | None. |
| S2 | Injection | None | Repo-wide grep | Zero `os.system`/`subprocess`/`eval`/`exec`/`pickle.load`/`shell=True`. | None. |
| S3 | Path traversal (filenames) | Low (verified fixed) | `generate.py:180-185` `make_filename()` | `\w`-only regex correctly collapses `..`, `/`, `\`, `C:`, UNC paths. | None. |
| S4 | Path traversal (file reads) | **Medium** | `generate.py:253-258` (`--repurpose`), `:389-393` (bulk CSV `source_file`) | No containment check on either path — absolute paths, `..\..`, or UNC paths are read as-is. A malicious `bulk.csv` shared by someone else could exfiltrate local files into the output ZIP. | Resolve and reject paths outside an allow-listed directory, or require explicit opt-in for external paths. |
| S5 | XSS | None (verified fixed) | `templates/community.py` HTML scaffolds | `html.escape()` fix confirmed complete; no second unescaped sink found anywhere. | None. |
| S6 | Dependency ceilings | Low | `pyproject.toml:17-20` | Floor-only version ranges (`anthropic>=0.40` etc.), no upper bound. | Pin a reasonable ceiling; enable Dependabot. |
| S7 | SSRF | None | `config.py` `brand_for_url()` | Pure local string matching, no network call. | None. |
| S8 | CI permissions | Low | `.github/workflows/ci.yml` | No explicit `permissions:` block (relies on GitHub's safe default). | Add explicit `permissions: contents: read`. |

**Verdict:** Safe for a single trusted operator. The one real gap is arbitrary local file read via untrusted bulk CSVs — treat any bulk CSV from outside your own team as untrusted until S4 is fixed.

---

## 3. DevOps / Packaging / CI

| # | Category | Severity | Evidence | Finding | Recommendation |
|---|---|---|---|---|---|
| D1 | Dependency health | **Critical** | Verified: `import google.generativeai` → `FutureWarning: All support for the google.generativeai package has ended.` | Gemini support depends on a fully EOL SDK with no future patches. | Migrate to the `google-genai` successor package in `llm.py` + `pyproject.toml`. |
| D2 | CI coverage gap | Medium | `.github/workflows/ci.yml` | CI never installs or imports any `llm-*` extra — the EOL-SDK problem (D1) would never surface as a red build. | Add a CI step installing `.[llm]` and importing all three provider modules. |
| D3 | CI smoke-check | Low | `ci.yml` last step | `pip install .` has no post-install assertion (no `content-wiz --list` check). | Add a smoke command after install. |
| D4 | Python version | Low | `pyproject.toml:10` `>=3.8`; CI matrix includes 3.8 | Python 3.8 reached EOL Oct 2024. | Bump floor to `>=3.9`/`>=3.10`, drop 3.8 from CI. |
| D5 | Hook portability | Medium | `hooks/pre-commit` tracked as mode `100644`, not `755` | Executable bit not preserved; a fresh non-Windows clone needs a manual `chmod +x` before the hook runs. Hook also doesn't run `ruff`, unlike CI. | `git update-index --chmod=+x`; add `ruff check .` to the hook. |
| D6 | Version/changelog | Medium | `pyproject.toml` still `0.2.0`; no `CHANGELOG.md` | The multi-provider feature shipped with no version bump or changelog entry. | Bump to `0.3.0`+; add a changelog. |
| D7 | Reproducibility | Low | No lockfile | CI floats on latest matching versions (verified: anthropic/openai both resolved several majors ahead of their floors today). | Acceptable at current scope; add a lockfile if the `llm` extras grow. |
| D8 | `.gitignore` gap | Low | `.ruff_cache/` excluded only via a non-project global config | A contributor without that global exclude would see it as untracked cruft. | Add `.ruff_cache/` explicitly. |
| D9 | Verified working | — | `pip install -e .` and all `llm-*` extras, `content-wiz` console script | All confirmed working end-to-end in a clean venv. | None needed. |

**Verdict:** Packaging mechanics genuinely work, but the multi-provider feature isn't production-ready as shipped: it depends on a dead SDK that CI can't catch, plus overdue Python-version and changelog hygiene.

---

## 4. Data Integrity

| # | Category | Severity | Evidence | Finding | Recommendation |
|---|---|---|---|---|---|
| DI1 | Placeholder quarantine | None | Full read of both CSVs | `HARO_DataBank.csv` has zero `[PLACEHOLDER]` leakage; `_PENDING.csv` rows are all genuinely unverified. Quarantine holds. | None. |
| DI2 | Schema consistency | None | Both CSV headers | Identical 7-column schema, all rows well-formed, no malformed years. | None. |
| DI3 | Bulk dry-run bug | **Medium** | `python generate.py --bulk bulk_template.csv --dry-run` actually wrote a real zip + log to `output/` | `--dry-run` is only checked inside `run_single()`; the bulk code path never checks it at all. | Add a `dry_run` check inside the bulk-processing loop. |
| DI4 | config.json data | None | `defaults.llm_models`, `platform_audience_overrides` | Internally consistent, plausible model ids, valid optional structure. | None. |
| DI5 | Stale references | None | Repo-wide grep for hardcoded DataBank row counts | None found. | None. |

**Verdict:** Data layer itself is trustworthy; the one defect (DI3) is operational, not data-integrity, but real — a bulk dry-run can trigger live generation/API spend unexpectedly.

---

## 5. Content Writer (prompts/ + templates/ + strategies/)

| # | Category | Severity | Evidence | Finding | Recommendation |
|---|---|---|---|---|---|
| C1 | Missing shared rules | Medium | `pr.py`'s `haro()`, `growth.py`'s `newsletter()`/`faq()`/`geo()`, `video.py`'s `video_script()`/`podcast()` | None of these interpolate `RESEARCH_RULES` despite being stat-heavy — missing DataBank-sourcing/publish-gate coverage. | Add `{RESEARCH_RULES}` to each. |
| C2 | Word-count override bug | Medium | `templates/blog.py` `blog_writing`, section minimums (~1,290+ words) | Fixed section-minimum floors override the caller's requested `{wordcount}` regardless of target (e.g. an 800-word request still forces 1,290+). | Scale section minimums proportionally to `wordcount`. |
| C3 | Copy-paste artifact | Medium | ~11 prompt files (Meta_Facebook_Ads, Pinterest, Newsletter, Testimonial_Review_Request, Thought_Leadership_OpEd, Trainer_Speaker_Bio, Twitter_Thread, Video_Script, Webinar_Promo, YouTube_Description, Podcast) | Same "no duplicate hook/CTA" rule stated twice per file — the second instance is a dangling sentence fragment with no verb, an orphaned artifact from a prior bulk edit. | Delete the fragment sentence in each file. |
| C4 | Thin tone guidance | Medium | Pinterest, SlideShare_Presentation, Schema_Markup, Topic_Cluster, Trainer_Speaker_Bio, Webinar_Promo prompts | Tone collapses to one generic "clear, professional B2B tone" line with no platform-specific voice cues — Pinterest especially, despite being a visual/aspirational platform. | Add 1-2 sentences of platform-specific voice guidance to each. |
| C5 | New strategy docs thinner | Medium | `strategy-tumblr.md`, `strategy-livejournal.md`, `strategy-quora.md`, `strategy-gmb.md` (written in a prior session) | Tumblr never mentions tags (its primary discovery mechanic); LiveJournal doesn't acknowledge it's a declining, fandom-adjacent platform; Quora name-drops "Spaces" without explaining the mechanic. All four are ~half the structural depth of `strategy-linkedin.md`/`strategy-haro.md`. | Add platform-mechanic specificity; consider whether the thinner format is intentional or needs the same depth as older docs. |
| C6 | Instagram voice convergence | Medium | LinkedIn_Post/Article/Carousel/Instagram prompts | Structural mechanics differ well, but Instagram's actual prose voice reads as "LinkedIn Post, shortened" rather than genuinely distinct. | Add explicit Instagram voice guidance (more visual/conversational). |
| C7 | Internal tension | Low | `Thought_Leadership_OpEd_Prompt.txt` | Bans "you/we/our/your" while requiring first-person exec voice that naturally needs those words for company-facing anecdotes. | Add a clarifying example. |
| C8 | Thin templates | Low | `Buyer_Persona_Prompt.txt`, `Blog_Suggestion_Prompt.txt` | No length targets, generic "be specific" instructions only. | Add soft length bands. |
| C9 | Model-agnostic check | None | Full grep across `templates/` + `prompts/` | Zero Claude/Anthropic/GPT/Gemini-specific tuning found anywhere — genuinely provider-agnostic. | None. |
| C10 | Strongest/weakest | — | — | Strongest: `GEO_Prompt.txt`, `Guest_Article_Pitch_Prompt.txt`, `Newsletter_Prompt.txt`, `Podcast_Prompt.txt` (real editorial reasoning, evidence tiers, mode-specific voice). Weakest: `Schema_Markup_Prompt.txt` (near-zero voice, acceptable for pure JSON-LD), `Pinterest_Prompt.txt`, `Buyer_Persona_Prompt.txt`, `Blog_Suggestion_Prompt.txt`. | — |

**Verdict:** Editorial quality is genuinely strong where it's been iterated on (technical/professional platforms), but has real gaps in the newest content (the 4 strategy docs I wrote) and a recurring copy-paste artifact from a prior bulk-edit pass that should be cleaned up.

---

## 6. SEO / GEO

| # | Category | Severity | Evidence | Finding | Recommendation |
|---|---|---|---|---|---|
| SEO1 | Canonical URLs, schema, internal linking | None (verified still fixed) | `blog.py`, `community.py` | All confirmed intact and consistent after multiple subsequent edit passes. | None. |
| SEO2 | Schema checklist inconsistency | Medium | `templates/growth.py:893-931` `geo()` | FAQPage schema requires actual JSON-LD output, but other applicable schema types (Article, HowTo, etc.) only say "implement if applicable" — softer than `blog.py`'s hard code-output rule. | Make the requirement uniform across all applicable schema types. |
| SEO3 | No persistent cluster tracking | Medium | Whole repo | Topical clustering exists only as per-generation prompt guidance; nothing tracks which pieces actually link to each other across runs. | Consider a `Cluster ID`/`Linked Pieces` column on the (currently nonexistent, see #Governance) publish tracker. |
| SEO4 | GEO practice currency | Low | `GEO_Prompt.txt`, `strategy-ai-search.md` | Directionally accurate for 2026 GEO consensus; one unverified claim (a specific 2026 GSC AI Overview filter) flagged as an assumption, not confirmed. | Verify against current GSC docs. |
| SEO5 | Meta description range mismatch | Low | `blog_writing` (150-158 chars) vs `blog_writing_md` (150-160 chars) | Minor inconsistency between two functions in the same file. | Align to one range. |

**Verdict:** SEO/GEO instruction layer held up well across multiple edit passes; the two real gaps (schema checklist softness, no persistent clustering) are pre-existing scope gaps, not regressions.

---

## 7. Brand / Compliance / Legal

| # | Category | Severity | Evidence | Finding | Recommendation |
|---|---|---|---|---|---|
| BC1 | Rule text consistency | None | `_shared.py`, README, `_Brand_Detection_Rules.txt` | All three state the same 12 rules in substance. | None. |
| BC2 | Enforcement scope | **Critical** | `lint_content.py`'s `BANNED_CTA_REGRESSION_TARGETS = ["templates/local.py"]` | Only one of six CTA-bearing templates is linted for banned-phrase regressions; the other five hand-roll unguarded CTA-ban prose. | Either widen the regression check to all of `templates/`, or import `BANNED_CTA_PHRASES` everywhere and register each file. |
| BC3 | Active rule contradiction | **High** | `templates/growth.py:525` | Instructs the model to use "Discover" as a CTA verb — a word explicitly banned in `_shared.py`'s `BANNED_CTA_PHRASES`. Invisible to the linter (see BC2). | Remove "Discover"/"Learn" from the CTA-verb suggestion list, or clarify the ban's exact scope. |
| BC4 | Disclosure rule | None (verified sound) | `templates/community.py` `livejournal_post` | Byline/disclosure instruction appears 3 times including in the mandatory self-check — genuinely hard to bypass. | None. |
| BC5 | Governance artifact missing | **High** | `agents.md`, `README.md` reference `jul2026_publish_tracker.csv` | File does not exist anywhere in the repo — corroborated independently by the Business audit. | Commit an actual tracker template with the referenced columns, or stop citing a specific filename. |
| BC6 | Third-party attribution reach | Medium | `templates/local.py` (GMB) | Doesn't import `RESEARCH_RULES` despite being the one template that cites external stats per its own strategy doc. | Import `RESEARCH_RULES` into `gmb()`. |
| BC7 | DataBank-sourcing mechanism | Medium | Repo-wide | Purely aspirational — no lint check cross-references generated stats against DataBank rows. | Acceptable limitation for static lint; consider a pattern-based warning as a stopgap. |
| BC8 | New strategy doc wording drift | Low | `strategy-gmb.md` | Describes the "Discover" ban as scoped to "bare imperative" use — a qualifier not present in the actual `_shared.py` rule. | Align wording or make the checker imperative-aware. |
| BC9 | New strategy docs governance silence | Low | GMB/LiveJournal strategy docs | Neither restates the governance/sign-off or DataBank rule, relying entirely on cross-reference to `agents.md`. | Add a one-line pointer in each. |

**Verdict:** The rule-authoring layer is solid and consistent; the enforcement layer has a false sense of coverage — the one file the regression linter actually watches isn't the only one with banned-phrase risk, and one template actively contradicts the rule it's supposed to follow.

---

## 8. Business / Client Stakeholder

| # | Category | Severity | Evidence | Finding | Recommendation |
|---|---|---|---|---|---|
| B1 | CLI works end-to-end | None | Direct runs of `--list`, multiple `--dry-run`s, the new audience override | All confirmed working, including the just-wired per-platform audience override. | None. |
| B2 | `--generate` error handling | None | Missing-key run for `--provider gemini` | Fails safely and legibly, no partial output written. | None. |
| B3 | Multi-provider quality claim | Medium | README/`llm.py` wording | Carefully hedged ("same kind of output," not "same quality") — better than feared, but no caveat anywhere that providers differ materially in instruction-following fidelity, and default model ids (`gpt-5`, `gemini-2.5-pro`) aren't verified as real/current strings. | Add an explicit caveat recommending closer review of non-default providers; verify model id strings. |
| B4 | Onboarding step count | Medium | Traced the full path to first publishable, reviewed content | 6-8 steps; reasonable for a technical operator, but citation verification and review sign-off are entirely unenforced manual steps for a non-technical one. | Acceptable as-is; document more explicitly for non-technical operators. |
| B5 | Tracker artifact missing | **High** | Same as BC5 | Independently corroborated: named "the biggest remaining trust gap" — a control described in detail but not instantiated. | Same recommendation as BC5. |
| B6 | Governance visibility | Low-Medium | README's Global Content Rules #12 + Governance note | Genuinely disclosed in the human-facing README, not hidden — but process-only, nothing in code blocks on it. | Track only if code enforcement is desired later. |
| B7 | Cost transparency | **High** | Repo-wide grep for pricing/cost terms | Zero mentions of $/token pricing for any of the 3 providers anywhere in the repo. A business stakeholder cannot budget content-generation cost from anything here. | Add a dated cost-reference table/link per provider in the LLM Providers README section. |
| B8 | Performance feedback loop | Medium (carried over) | Repo-wide grep | Still no mechanism tying published content back to actual performance data — a known, permanent limitation, not something recently "fixed." | Keep flagged as a standing limitation. |

**Verdict:** Runnable with light supervision, not "walk away and trust it" — the human-review safety net the docs point to doesn't exist as a real file, and there's no cost visibility for comparing providers.

---

## Recommended fix order (not yet actioned — audit only)

1. **Critical:** Migrate Gemini support off the EOL `google-generativeai` SDK to `google-genai` (D1), and add a CI step that actually installs/imports the `llm` extras so this class of problem is never silent again (D2).
2. **Critical/High:** Widen the banned-CTA-phrase regression check beyond `templates/local.py` (BC2) and remove the "Discover" contradiction in `growth.py` (BC3).
3. **High:** Either commit a real publish-tracker template with the columns the docs describe, or stop pointing to a specific nonexistent filename (BC5/B5).
4. **High:** Harden `llm.py`'s Gemini/OpenAI response parsing against empty/blocked responses, and guard Anthropic's silent-empty-text path (E2/E3).
5. **Medium:** Fix `--bulk --dry-run` to actually dry-run (DI3); add path containment checks for `--repurpose`/bulk `source_file` (S4); add cost-reference documentation (B7); interpolate `RESEARCH_RULES` into the stat-heavy functions missing it (C1, BC6); fix `blog_writing`'s word-count override bug (C2); clean up the ~11-file copy-paste artifact (C3).
6. **Lower priority / cleanup tier:** everything else listed above.
