# Content-Wiz Improvement Plan
**Created:** 2026-07-13  
**Source for new content:** D:\Coding\marketing-academy (406 lessons, 16 disciplines)  
**Status tracking:** See CHANGELOG.md after each phase completes

---

## Phase 1 — New Prompt Files (11 files)
Filling channel gaps identified by cross-referencing marketing-academy content.

| # | File | Source Lesson(s) | Priority |
|---|---|---|---|
| 1 | `Meta_Facebook_Ads_Prompt.txt` | `paid-ads/meta-ads.mdx` | High |
| 2 | `TikTok_Ads_Prompt.txt` | `paid-ads/tiktok-ads.mdx` | High |
| 3 | `Instagram_Content_Prompt.txt` | `social/instagram.mdx` | High |
| 4 | `TikTok_Content_Prompt.txt` | `social/tiktok.mdx` | High |
| 5 | `Threads_Post_Prompt.txt` | `social/threads.mdx` | Medium |
| 6 | `Landing_Page_Copy_Prompt.txt` | `copywriting/landing-page-copy.mdx` + `cro/landing-page-anatomy.mdx` | High |
| 7 | `Product_Launch_Prompt.txt` | `product-marketing/launches.mdx` | High |
| 8 | `UGC_Brief_Prompt.txt` | `social/ugc.mdx` | Medium |
| 9 | `Substack_Post_Prompt.txt` | `social/substack-notes.mdx` | Medium |
| 10 | `Referral_Program_Copy_Prompt.txt` | `growth/referral-programs.mdx` | Medium |
| 11 | `Sales_Email_Prompt.txt` | `copywriting/email-copy.mdx` | High |

**Standard for all new prompts:**
- Follow LinkedIn_Post_Prompt.txt as gold standard structure
- Include: REQUIRED INPUTS (with Voice/Tone field), ALGORITHM/PLATFORM RULES, FORMAT sections, RULES SUMMARY (with SELF-CHECK + BATCH DEDUP), FAILURE MODES, OUTPUT FORMAT
- Save paths follow existing convention: `output/[Channel]/`

---

## Phase 2 — New Strategy Files (8 files)
Filling channel gaps in strategies/ folder.

| # | File | Source Lesson(s) | Priority |
|---|---|---|---|
| 1 | `strategy-instagram.md` | `social/instagram.mdx` | High |
| 2 | `strategy-tiktok.md` | `social/tiktok.mdx` + `paid-ads/tiktok-ads.mdx` | High |
| 3 | `strategy-threads.md` | `social/threads.mdx` | Medium |
| 4 | `strategy-community-building.md` | `growth/community-led-growth.mdx` + `social/community-building.mdx` | Medium |
| 5 | `strategy-referral.md` | `growth/referral-programs.mdx` | Medium |
| 6 | `strategy-product-launch.md` | `product-marketing/launches.mdx` | High |
| 7 | `strategy-paid-social.md` | `paid-ads/meta-ads.mdx` + `paid-ads/tiktok-ads.mdx` | High |
| 8 | `strategy-substack.md` | `social/substack-notes.mdx` | Medium |

**Standard for all new strategies:**
- Follow strategy-seo-programmatic.md as gold standard structure
- Include: Goal + Success Metrics, Platform Overview, Content Pillars, Cadence, Distribution & Amplification, Common Mistakes, Recommended Tools, Adaptation for Your Brand

---

## Phase 3 — Enrich 6 Existing Prompts
Adding frameworks and platform-specific depth from marketing-academy lessons.

| # | Prompt | Enrichment | Source |
|---|---|---|---|
| 1 | `Blog_Writing_Prompt.txt` | Add AIDA / PAS / StoryBrand framework selector | `copywriting/aida-pas-frameworks.mdx` |
| 2 | `LinkedIn_Post_Prompt.txt` | Add psychology hook triggers (social proof, loss aversion, curiosity gap) | `psychology/` lessons |
| 3 | `Email_Drip_Sequence_Prompt.txt` | Add lifecycle stage mapping (welcome / activation / retention / win-back) | `email/` lessons |
| 4 | `Video_Script_Prompt.txt` | Add short-form algorithm rules for Reels/Shorts/TikTok format | `social/short-form-video-algorithms.mdx` |
| 5 | `GEO_Prompt.txt` | Add AI search ranking factors (citation signals, entity coverage) | `ai-marketing/ai-search-ranking.mdx` |
| 6 | `Google_Ads_Prompt.txt` | Add Quality Score optimisation guidance | `paid-ads/quality-score.mdx` |

---

## Phase 4 — New Python Templates (3 files)
Extending templates/ folder with new content type modules.

| # | File | Coverage |
|---|---|---|
| 1 | `templates/cro.py` | Landing page copy, CTA variants, hero formula, trust signals |
| 2 | `templates/product.py` | Product launch copy, positioning statements, messaging hierarchy |
| 3 | `templates/ugc.py` | UGC briefs, creator briefs, referral program copy |

---

## Phase 5 — Resources File
Create `RESOURCES.md` — curated marketing resource directory covering all major disciplines.  
Reference: marketing-academy tools directory (108 tools), lesson resource lists, and external sources.

**Sections:**
- SEO & GEO
- Paid Media (Search, Social, Programmatic)
- Social Media Marketing
- Content Marketing
- Email & Lifecycle
- Analytics & Attribution
- Copywriting & CRO
- Brand Strategy
- AI Marketing Tools
- Learning & Communities

---

## Phase 6 — Documentation Updates
Update all doc reference files to reflect new content:
- `README.md` — add new prompts and strategies to the feature table
- `CHANGELOG.md` — log all additions with date
- `config.json` — register new prompt types if applicable
- `textprompts.py` — register new prompts in the prompt registry
- `agents.md` — update agent capabilities list

---

## Execution Order
1. Phase 1 + 2 in parallel (independent new files)
2. Phase 3 (enrichments to existing files)
3. Phase 4 (templates)
4. Phase 5 (resources file)
5. Phase 6 (doc updates)
6. Git commit + push
7. 4-hour status check timer

---

## Definition of Done
- [ ] All 11 new prompt files written and follow gold standard
- [ ] All 8 new strategy files written and follow gold standard
- [ ] 6 existing prompts enriched
- [ ] 3 new template files written
- [ ] RESOURCES.md created with 50+ curated links
- [ ] README.md updated
- [ ] CHANGELOG.md updated
- [ ] Git committed and pushed
- [ ] 4-hour timer set
