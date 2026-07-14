# Content-Wiz Improvement Plan
**Created:** 2026-07-13  
**Updated:** 2026-07-14 (v2 — full audit findings added)  
**Source for new content:** D:\Coding\marketing-academy (406 lessons, 16 disciplines)  
**Status tracking:** See CHANGELOG.md after each phase completes

---

## Phase 1 — New Prompt Files (11 files) ✅ COMPLETE
All 11 new prompts written and follow gold standard. See CHANGELOG v0.7.0.

---

## Phase 2 — New Strategy Files (8 files) ✅ COMPLETE
All 8 new strategy docs written. See CHANGELOG v0.7.0.

---

## Phase 3 — Enrich 6 Existing Prompts ✅ COMPLETE
See CHANGELOG v0.7.0.

---

## Phase 4 — New Python Templates (3 files) ✅ COMPLETE
cro.py, product.py, ugc.py written. **Note: not yet wired into CLI — see Phase 8.**

---

## Phase 5 — Resources File ✅ COMPLETE
RESOURCES.md created with 90+ curated links.

---

## Phase 6 — Documentation Updates ✅ COMPLETE
README, CHANGELOG, GLOSSARY.md all updated and pushed.

---

## Phase 7 — CLI Wiring Fixes (from audit) 🔄 IN PROGRESS

5 prompt files existed with zero CLI path. 3 template modules were written but never imported.

### 7A — Wire unwired prompt files into textprompts.py
- [x] Threads_Post_Prompt.txt → aliases `threads`, `threads_post`
- [x] TikTok_Ads_Prompt.txt → alias `tiktok_ads`
- [x] Product_Launch_Prompt.txt → aliases `product_launch`, `launch_copy`
- [x] Referral_Program_Copy_Prompt.txt → aliases `referral_copy`, `referral_program`
- [x] Sales_Email_Prompt.txt → aliases `sales_email`, `cold_email`, `outreach_email`

### 7B — Import and wire new template modules
- [x] cro.py → `__init__.py` + PLATFORM_MAP: `cro_lead_gen`, `cro_sales_page`, `cta_variants`, `trust_signals`, `hero_headline`
- [x] product.py → `__init__.py` + PLATFORM_MAP: `positioning_statement`, `launch_announcement`, `pre_launch_teaser`, `messaging_hierarchy`, `launch_email_sequence`
- [x] ugc.py → `__init__.py` + PLATFORM_MAP: `ugc_video_brief`, `testimonial_request_ugc`, `creator_brief_ugc`, `photo_brief`

### 7C — Duplicate file cleanup
- [ ] Merge Instagram_Content_Prompt.txt and Instagram_Prompt.txt → keep better one, wire it

---

## Phase 8 — New Prompt Files (17 gaps from audit)

| # | File | Priority | Status |
|---|------|----------|--------|
| 1 | `Facebook_Organic_Post_Prompt.txt` | High | ✅ |
| 2 | `Twitter_Ads_Prompt.txt` | High | ✅ |
| 3 | `LinkedIn_Newsletter_Prompt.txt` | High | ✅ |
| 4 | `YouTube_Shorts_Prompt.txt` | High | ✅ |
| 5 | `ASO_Copy_Prompt.txt` | High | ✅ |
| 6 | `Competitive_Battlecard_Prompt.txt` | High | ✅ |
| 7 | `Customer_Success_Email_Prompt.txt` | High | ✅ |
| 8 | `Chatbot_Flow_Prompt.txt` | Medium | ✅ |
| 9 | `ABM_Content_Prompt.txt` | Medium | ✅ |
| 10 | `Brand_Voice_Style_Guide_Prompt.txt` | Medium | ✅ |
| 11 | `Partnership_Comarketing_Prompt.txt` | Medium | ✅ |
| 12 | `Annual_Report_Prompt.txt` | Medium | ✅ |
| 13 | `Podcast_Ad_Read_Prompt.txt` | Medium | ✅ |
| 14 | `Survey_Feedback_Copy_Prompt.txt` | Medium | ✅ |
| 15 | `Newsletter_Sponsorship_Pitch_Prompt.txt` | Medium | ✅ |
| 16 | `Community_Welcome_Prompt.txt` | Medium | ✅ |
| 17 | `Bing_Ads_Prompt.txt` | Low | ✅ |

---

## Phase 9 — New Strategy Files (21 gaps from audit)

| # | File | Priority | Status |
|---|------|----------|--------|
| 1 | `strategy-twitter.md` | High | ✅ |
| 2 | `strategy-google-ads.md` | High | ✅ |
| 3 | `strategy-linkedin-ads.md` | High | ✅ |
| 4 | `strategy-lifecycle-crm.md` | High | ✅ |
| 5 | `strategy-sales-enablement.md` | High | ✅ |
| 6 | `strategy-editorial-seo.md` | High | ✅ |
| 7 | `strategy-cro.md` | High | ✅ |
| 8 | `strategy-product-marketing.md` | High | ✅ |
| 9 | `strategy-reddit.md` | Medium | ✅ |
| 10 | `strategy-pinterest.md` | Medium | ✅ |
| 11 | `strategy-events-webinar.md` | Medium | ✅ |
| 12 | `strategy-crisis-comms.md` | Medium | ✅ |
| 13 | `strategy-employer-branding.md` | Medium | ✅ |
| 14 | `strategy-link-building.md` | Medium | ✅ |
| 15 | `strategy-gated-content.md` | Medium | ✅ |
| 16 | `strategy-mobile-messaging.md` | Medium | ✅ |
| 17 | `strategy-discord.md` | Medium | ✅ |
| 18 | `strategy-competitive-analysis.md` | Medium | ✅ |
| 19 | `strategy-technical-seo.md` | Medium | ✅ |
| 20 | `strategy-pr.md` | Medium | ✅ |
| 21 | `strategy-investor-comms.md` | Low | ✅ |

---

## Phase 10 — Tooling Improvements

| # | Feature | Priority | Status |
|---|---------|----------|--------|
| 1 | `--variants N` flag — A/B copy generator | High | ⬜ |
| 2 | `--keywords FILE` flag — keyword injection | High | ⬜ |
| 3 | Citation auto-verification in lint_content.py | High | ⬜ |
| 4 | `--tone` override flag (formal/conversational/urgent/educational/playful) | High | ⬜ |
| 5 | Social scheduler CSV export (Buffer/Later format) | Medium | ⬜ |
| 6 | `--language` / locale flag | Medium | ⬜ |
| 7 | `--log-publish` tracker integration | Medium | ⬜ |
| 8 | HARO DataBank builder prompt | Medium | ⬜ |
| 9 | `--format` CMS output (gutenberg/hubspot/contentful) | Medium | ⬜ |
| 10 | `--with-image-brief` visual direction flag | Medium | ⬜ |
| 11 | Content performance feedback CSV | Low | ⬜ |
| 12 | HARO DataBank population (currently 15 rows — needs 50+) | Low | ⬜ |

---

## Definition of Done (v1 — complete ✅)
- [x] All 11 new prompt files written and follow gold standard
- [x] All 8 new strategy files written and follow gold standard
- [x] 6 existing prompts enriched
- [x] 3 new template files written
- [x] RESOURCES.md created with 90+ curated links
- [x] README.md updated
- [x] CHANGELOG.md updated
- [x] Git committed and pushed
- [x] 4-hour timer set
- [x] GLOSSARY.md created (146 terms, 13 disciplines)

## Definition of Done (v2 — in progress)
- [x] All 5 unwired prompts wired into CLI
- [x] cro.py / product.py / ugc.py imported and reachable
- [ ] Duplicate Instagram prompt resolved
- [x] All 17 Phase 8 prompts written and wired
- [x] All 21 Phase 9 strategy docs written
- [ ] Phase 10 tooling features implemented
- [x] README updated to reflect all new content
- [x] CHANGELOG v0.8.0 written
- [x] Git committed and pushed
