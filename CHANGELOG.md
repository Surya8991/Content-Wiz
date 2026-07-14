# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
