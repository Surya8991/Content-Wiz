# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.10.0] - 2026-07-14

### Added

**Content-strategy gap closure (repomix + codereview-driven audit found 3 strategy
docs with zero matching CLI prompt, and 5 wired prompts with no companion
strategy doc):**

- `prompts/Programmatic_SEO_Prompt.txt` - bulk template-page generator for
  variable combinations (e.g. "[Certification] + [Industry]", "[Service] +
  [City]"), closing `strategy-seo-programmatic.md`'s gap. Wired as
  `programmatic_seo`/`programmatic`, output subfolder `Programmatic_SEO`.
  Requires a combination-specific data point per page and flags rows with
  none rather than fabricating one, per the strategy doc's deindexation
  warning against template-only pages.
- `prompts/Technical_SEO_Audit_Prompt.txt` - structured audit report
  (crawlability, indexation, Core Web Vitals, canonical, internal linking)
  closing `strategy-technical-seo.md`'s gap. Wired as
  `technical_seo`/`technical_seo_audit`/`seo_audit`, output subfolder
  `Technical_SEO`. Never fabricates a CWV score or crawl error count not
  supplied as input.
- `prompts/Lead_Magnet_Prompt.txt` - short single-session lead magnets
  (checklist / calculator copy / fill-in template), distinct from
  `Whitepaper_eBook_Prompt.txt`'s long-form assets, closing
  `strategy-gated-content.md`'s short-form gap. Wired as
  `lead_magnet`/`checklist`/`calculator_copy`, output subfolder
  `Lead_Magnets`.
- 5 new strategy docs for prompts that existed with no companion strategy:
  `strategy-newsletter-sponsorship.md`, `strategy-abm.md`,
  `strategy-chatbot.md`, `strategy-partnerships.md`, `strategy-bing-ads.md`.
- `README.md`: added all 3 new prompts to the text-prompt alias table and
  all 5 new strategy docs to the strategy table; bumped the "channel
  strategy docs" count to 51 and "flat prompt files" count to 79.

### Verification

- `python -m unittest test_generate -v` - 74/74 tests pass.
- `python lint_content.py` - passes clean (153 files checked, up from 145).
- Manually resolved all 3 new CLI aliases via `--dry-run` to confirm wiring.

## [0.9.1] - 2026-07-14

### Fixed

**Whole-project code review (repomix + codereview pass):**

- `templates/community.py`: `discord_announcement()`'s word-count range only
  floored the low bound, not the high one - for `wordcount` under ~48 the
  printed range inverted (e.g. `wordcount=10` produced "60-12 words is
  acceptable"). Floored `high` the same way `low` already was.
- `templates/video.py`: `youtube_desc()` had no default for `wordcount`
  (every sibling template defaults it to `None`), so `max(wordcount, 350)`
  would raise `TypeError` if ever called without one. Matched the pattern
  used everywhere else in `templates/`.


**Persona-driven review pass:**

- `generate.py`: `--output-dir`/`--bulk` writes to a path on a different drive
  than the project (e.g. a Windows temp dir on `C:` while the repo lives on
  `D:`) crashed every "saved to"/"packaged into" print with
  `ValueError: path is on mount ... start on mount ...` (`os.path.relpath`
  can't cross drives on Windows). Added `safe_relpath()`, which falls back to
  an absolute path instead of raising. Same fix applied to `lint_content.py`'s
  `--check-urls`/`--check-banned-phrases` reporting.
- `lint_content.py`: fixed 152 pre-existing em-dash violations of the
  project's own "no em dashes anywhere" rule, present in `README.md`,
  `generate.py`, and 20 `strategies/*.md` files. `python lint_content.py` (run
  in CI on every push/PR) was failing before this fix.
- Phase 7C cleanup (tracked in `plan.md` since Phase 7): `prompts/Instagram_Prompt.txt`
  and `prompts/Instagram_Content_Prompt.txt` both existed but neither was wired
  into `textprompts.py`, so neither was reachable from the CLI despite the
  README listing both as "reachable from the same CLI." Deleted the
  superseded single-caption version (`Instagram_Prompt.txt`) and wired the
  richer 3-format version under new aliases `instagram_content`, `ig_content`,
  `instagram_reel` (distinct from the existing `instagram`/`ig` aliases, which
  resolve to the unrelated rich Python template in `templates/social.py`).
- `pyproject.toml`: version was frozen at `0.6.0` while `CHANGELOG.md` had
  already moved through 0.7.0-0.9.0; bumped to match.
- `plan.md`'s Phase 7B row documented `testimonial_request_ugc` and
  `creator_brief_ugc` as the CLI aliases for two UGC templates; the actual
  `PLATFORM_MAP` keys in `generate.py` are `testimonial_request` and
  `creator_brief` (no `_ugc` suffix, and never were). Corrected the doc to
  match the real aliases.

### Verification

- `python -m unittest test_generate -v` - 74/74 tests pass (was 73 passing +
  1 error before the `safe_relpath` fix).
- `python lint_content.py` - passes clean (was 152 errors).
- Manual CLI pass across first-time-user, power-user (`--variants`, `--tone`,
  `--keywords`, cross-drive `--output-dir`), bulk/marketer, admin/config
  (malformed `config.json`), and QA/edge-case (unknown platform, missing
  args, path traversal, invalid bulk row, missing API key, bad `--provider`)
  workflows. No other crashes found.

## [0.9.0] - 2026-07-14

### Added

**Phase 10 — CLI Tooling Layer:**

**New `generate.py` flags (8):**
- `--variants N` — generate N independently-differentiated versions of the same prompt in one run; each saved with an index suffix (`_v1`, `_v2`, …)
- `--keywords FILE` — inject a keyword list (CSV first-column or plain one-per-line) into the prompt as a mandatory incorporation block
- `--tone {formal,conversational,urgent,educational,playful}` — append a named tone-override block (sourced from `TONE_RULES` in `_shared.py`) after the main prompt
- `--language LANG` — instruct the model to output in a specific language (e.g. `--language French`)
- `--log-publish` — append a Draft row to a monthly tracker CSV (`output/publish_tracker_YYYY-MM.csv`) for every piece generated
- `--format {markdown,gutenberg,hubspot,contentful}` — reformat `--generate` output for a target CMS after generation
- `--with-image-brief` — append a 3-field image/visual brief block (concept, style, alt text) to every prompt
- `--export-scheduler {buffer}` — after a bulk run, export a Buffer-compatible import CSV (`bulk_buffer_YYYY-MM-DD.csv`) from the run log

**New `lint_content.py` flag:**
- `--check-urls DIR` — crawl all `.md` and `.txt` files under DIR, extract every `https?://` URL, HEAD-check each (deduplicated, 8s timeout), and report dead links (4xx/5xx/timeout) with file and line number

**New `_shared.py` exports:**
- `TONE_RULES` — dict of 5 named tone presets (formal, conversational, urgent, educational, playful)
- `tone_modifier(tone)` — returns the tone-override string for a given tone name, or empty string if unset

**New prompt file:**
- `prompts/HARO_DataBank_Builder_Prompt.txt` — internal research tool for mining reports and building the stat DataBank; 3 formats: Format A (mine a document), Format B (verify pending rows), Format C (generate research targets). Wired as `haro_databank`, `databank`, `stat_mining` aliases.

**`templates/__init__.py`:** Updated `_shared` import to expose `TONE_RULES` and `tone_modifier` at package level.

---

## [0.8.0] — 2026-07-14

### Added

**Prompt files (17 new channels — Phase 8):**

High priority:
- `prompts/Facebook_Organic_Post_Prompt.txt` — 3 formats (Standard/Video/Poll), external link suppression rules, 90-min comment velocity window, B2B and B2C pillar split
- `prompts/Twitter_Ads_Prompt.txt` — 5 paid formats (Promoted Post/Image/Video/Carousel/Follower), character limit table, 2026 safety tiers, frequency caps, 3-second video rule
- `prompts/LinkedIn_Newsletter_Prompt.txt` — newsletter vs article distinction, subscriber notification mechanic, 3 formats (Full Issue/Short-Form/Curated Roundup), dual-purpose title rule
- `prompts/YouTube_Shorts_Prompt.txt` — Shorts vs TikTok/Reels differences, watch-through rate primacy, timestamped scripts, subscribe CTA placement rules
- `prompts/ASO_Copy_Prompt.txt` — iOS and Google Play character limits table, iOS keyword field rules, A/B test variant structure with hypothesis statements
- `prompts/Competitive_Battlecard_Prompt.txt` — verified-only competitor claims, objection handles (feel-felt-found), landmine questions, mandatory review date metadata
- `prompts/Customer_Success_Email_Prompt.txt` — 6 email types with lifecycle trigger signals, personalization tokens per type, NPS detractor escalation rule

Medium priority:
- `prompts/Chatbot_Flow_Prompt.txt` — Lead Capture / Support Triage / Demo Booking flows with node structure
- `prompts/ABM_Content_Prompt.txt` — 1:1 Enterprise / 1:Few Named Account / 1:Many Segment tiers
- `prompts/Brand_Voice_Style_Guide_Prompt.txt` — Full Voice Guide / Channel Extension / Voice Audit formats
- `prompts/Partnership_Comarketing_Prompt.txt` — Co-Authored / Joint Announcement / Co-Branded Campaign
- `prompts/Annual_Report_Prompt.txt` — Corporate Annual Report / Nonprofit Impact Report
- `prompts/Podcast_Ad_Read_Prompt.txt` — Pre-Roll / Mid-Roll / Host-Endorsed with FTC disclosure rules
- `prompts/Survey_Feedback_Copy_Prompt.txt` — NPS / Post-Purchase Survey / Customer Interview Invitation
- `prompts/Newsletter_Sponsorship_Pitch_Prompt.txt` — Media Kit / Cold Email / 3-email Follow-Up Sequence
- `prompts/Community_Welcome_Prompt.txt` — Member Onboarding / Guidelines and Channel Descriptions / Moderation
- `prompts/Bing_Ads_Prompt.txt` — RSA / Expanded Text / Audience Ads with LinkedIn audience targeting guidance

**CLI wiring — textprompts.py:** 42 new aliases covering all 17 new prompt files plus the 5 previously-unwired prompts (Threads, TikTok Ads, Product Launch, Referral Copy, Sales Email).

**Strategy documents (21 new channels — Phase 9):**

High priority:
- `strategies/strategy-twitter.md` — impressions-first algo, bookmark signals, no-link penalty, reply-led growth
- `strategies/strategy-google-ads.md` — 4 campaign types, Quality Score optimization, RSA 15-headline pinning, bidding decision tree
- `strategies/strategy-linkedin-ads.md` — 6 ad formats, 4-layer targeting, 2026 CPL benchmarks, Lead Gen Form advantage
- `strategies/strategy-lifecycle-crm.md` — 5 lifecycle stages, trigger logic, 2-email/week cap, Apple Mail measurement caveat
- `strategies/strategy-sales-enablement.md` — content-to-buyer-stage map, SDR vs AE usage, 4 objection types, feedback loop
- `strategies/strategy-editorial-seo.md` — hub-and-spoke model, E-E-A-T implementation, original data as link asset, refresh cadence
- `strategies/strategy-cro.md` — 5-phase hypothesis-first methodology, 95% confidence requirement, HiPPO failure mode
- `strategies/strategy-product-marketing.md` — JTBD positioning, 3-phase launch sequence, 11-item launch asset checklist

Medium priority:
- `strategies/strategy-reddit.md` — karma-first participation, 90/10 contribution ratio, AMA planning
- `strategies/strategy-pinterest.md` — search-engine model, keyword-first pin anatomy, 45-to-60-day seasonal calendar
- `strategies/strategy-events-webinar.md` — 3-phase lifecycle, attended/no-show sequences, 8+ repurposing assets
- `strategies/strategy-crisis-comms.md` — 2-hour holding statement window, employees-first stakeholder sequencing
- `strategies/strategy-employer-branding.md` — EVP construction, full EB funnel, Glassdoor review management
- `strategies/strategy-link-building.md` — 5 prospecting methods, 3-touch outreach cadence, anchor text distribution ratios
- `strategies/strategy-gated-content.md` — gate/no-gate decision matrix, 4-email post-download sequence, progressive profiling
- `strategies/strategy-mobile-messaging.md` — TCPA/GDPR compliance, frequency caps (SMS 4/month, push 2/week), trigger hierarchy
- `strategies/strategy-discord.md` — channel architecture, 3-tier role system, MEE6/Carl-bot/Zapier stack, onboarding flow
- `strategies/strategy-competitive-analysis.md` — 3-tier monitoring, win/loss integration, battlecard structure
- `strategies/strategy-technical-seo.md` — 2026 Core Web Vitals targets, schema priorities, canonical strategy
- `strategies/strategy-pr.md` — full press office workflow, newsjacking 2-to-4-hour window, pitch construction formula
- `strategies/strategy-investor-comms.md` — monthly/quarterly/annual cadence, transparency tone rules, DocSend/Visible.vc stack

**CLI wiring — generate.py + templates/__init__.py:**
- `templates/cro.py`, `templates/product.py`, `templates/ugc.py` imported into `__init__.py` — all 14 functions now reachable
- 14 new `PLATFORM_MAP` aliases and 9 new `SUBFOLDER_MAP` entries (CRO/, Product_Marketing/, etc.)

## [0.7.0] — 2026-07-14

### Added

**Prompt files (11 new channels):**
- `prompts/TikTok_Ads_Prompt.txt` — TikTok Ads (Spark Ads, TopView, In-Feed) with hook + CTA structure and 2026 algorithm rules
- `prompts/Instagram_Content_Prompt.txt` — Instagram captions, Reels hooks, and Stories across 3 formats
- `prompts/TikTok_Content_Prompt.txt` — TikTok organic scripts with hook + body + CTA + trending-sound guidance
- `prompts/Threads_Post_Prompt.txt` — Threads posts optimised for replies and reshares
- `prompts/Landing_Page_Copy_Prompt.txt` — Landing page copy (lead-gen and sales page variants) with CRO framework
- `prompts/Product_Launch_Prompt.txt` — Product launch copy across pre-launch, launch-day, and post-launch phases
- `prompts/UGC_Brief_Prompt.txt` — UGC video and photo briefs for creators with platform-specific guidance
- `prompts/Substack_Post_Prompt.txt` — Substack essays, Notes, and restacks with paid-subscriber conversion hooks
- `prompts/Referral_Program_Copy_Prompt.txt` — Referral invite and incentive copy with viral-loop mechanics
- `prompts/Sales_Email_Prompt.txt` — Cold outreach and follow-up sales email sequences
- `prompts/Meta_Facebook_Ads_Prompt.txt` — Meta/Facebook Ads copy across awareness, consideration, and conversion objectives

**Strategy documents (8 new channels):**
- `strategies/strategy-instagram.md` — Instagram organic + Reels: goal, content pillars, cadence, failure modes
- `strategies/strategy-tiktok.md` — TikTok organic + TikTok Ads: watch-through rate focus, creator-native formats
- `strategies/strategy-threads.md` — Threads: reply-first strategy, cross-post cadence from Instagram
- `strategies/strategy-community-building.md` — Community-led growth: member retention, value loops, moderation
- `strategies/strategy-referral.md` — Referral programs: viral coefficient, incentive design, attribution
- `strategies/strategy-product-launch.md` — Product launches: pre-launch, launch week, post-launch nurture
- `strategies/strategy-paid-social.md` — Paid social (Meta + TikTok): ROAS benchmarks, creative testing, budget allocation
- `strategies/strategy-substack.md` — Substack: paid subscriber conversion, editorial cadence, growth loops

**Python template modules (3 new files):**
- `templates/cro.py` — `landing_page_lead_gen`, `landing_page_sales`, `cta_variants`, `trust_signals_block`, `hero_headline_formula`
- `templates/product.py` — `positioning_statement`, `launch_announcement`, `pre_launch_teaser`, `messaging_hierarchy`, `launch_email_sequence`
- `templates/ugc.py` — `ugc_video_brief` (platform-aware), `testimonial_request`, `creator_brief`, `photo_brief`

**Reference files:**
- `RESOURCES.md` — 90+ curated resources across SEO, paid media, social, email, analytics, copywriting, AI marketing, and learning communities
- `GLOSSARY.md` — 146-term marketing glossary across 13 disciplines, sourced from Marketing Academy

**Prompt enrichments (6 existing files):**
- `Blog_Writing_Prompt.txt` — added AIDA / PAS / StoryBrand framework selector
- `LinkedIn_Post_Prompt.txt` — added psychology hook patterns (social proof, loss aversion, curiosity gap)
- `Email_Drip_Sequence_Prompt.txt` — added lifecycle stage mapping (welcome / activation / retention / win-back)
- `Video_Script_Prompt.txt` — added short-form algorithm rules for Reels/Shorts/TikTok
- `GEO_Prompt.txt` — added AI search ranking factors (citation signals, entity coverage)
- `Google_Ads_Prompt.txt` — added Quality Score optimisation guidance

**Systematic gap audit (all 39 existing prompt files):**
- Every existing prompt reviewed and patched against 6 gap categories: VOICE (missing tone/register field), LENGTH-CHECK (no self-check rule), THIN-FORMAT (insufficient output structure), VAGUE-OUTPUT (no concrete spec), NO-FAILURE (no failure modes section), NO-DEDUP (no batch deduplication rule)

## [0.6.0]

### Added
- 24 new templates closing the gaps found in a systematic full-funnel
  workflow audit (paid channels, lifecycle marketing, sales enablement,
  events, PR/comms, employer branding, mobile messaging), each grounded in
  current 2026 platform/legal research before writing:
  - Lifecycle email (`templates/lifecycle.py`): onboarding, win-back (covers
    cart-abandonment as a trigger variant), churn-prevention, upsell/cross-sell.
  - Sales enablement (`templates/sales_enablement.py`): pitch deck narrative,
    cold call script, InMail/connection-request template, proposal copy.
  - Crisis and internal PR (`templates/pr.py`): crisis holding statement,
    internal company announcement, investor update, company press kit
    (distinct from the existing creator media kit).
  - Paid ad formats (`templates/paid_ads.py`): display/banner copy (IAB sizes),
    native ad copy (with FTC disclosure guidance), a 3-stage retargeting
    sequence, and :15/:30 CTV/streaming scripts.
  - Employer branding (`templates/recruitment.py`): job postings (with
    pay-transparency-law and inclusive-language awareness) and employee
    spotlights.
  - Event lifecycle (`templates/events.py`): webinar registration pages, a
    segmented attended/no-show post-event follow-up, and booth-lead follow-up.
  - Mobile messaging (`templates/mobile_messaging.py`): SMS (TCPA-aware),
    push notifications, and in-app messages.
- All 24 wired into `PLATFORM_MAP`/`SUBFOLDER_MAP` with new aliases and
  output subfolders; `templates/` grows from 9 to 15 modules, 40 to 64
  template keys.

## [0.5.0]

### Added
- Five new templates, each grounded in current platform research: `profile_bio`
  (LinkedIn About/X bio/Instagram bio/Substack About, with exact 2026 character
  limits), `review_response` (Google/Yelp/Trustpilot/G2 review replies, both
  sentiment branches), `substack_post` (Notes/restack-aware, distinct from the
  generic newsletter template), `glossary_page` (SEO definition pages with
  DefinedTerm schema), and `discord_announcement` (native Markdown, ping-usage
  discipline, reaction-emoji seeding).

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
