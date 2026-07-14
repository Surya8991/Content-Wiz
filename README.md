# Content Wiz - Multi-Brand, Multi-Market Content Generation Toolkit

Content Wiz assembles fully-specified, channel-ready content prompts - or, with
`--generate`, finished content - for any brand across B2B, B2C, and
creator/personal-brand markets. It is not tied to one company: `config.json`
holds a `brands` map keyed by domain, where each entry defines a brand's name,
description, audience, hashtag, and market register. Pass `--url yourdomain.com`
when generating and the audience and voice auto-fill from the matching brand
entry; without a matching entry (or without `--url`), it falls back to neutral
defaults. `--audience` always overrides. Edstellar and Invensis Learning ship as
working example brands, plus a placeholder creator-brand entry - edit them,
delete them, or add your own.

## What it can do

- **64 rich content-type templates** across blog/SEO (pillar posts, Dev.to/
  Hashnode, Medium, comparison pages, Substack, SEO glossary pages), social
  (LinkedIn, Twitter/X, Instagram, carousels, profile/bio optimization), video
  (YouTube, podcasts, Reels/Shorts/TikTok scripts, CTV/streaming ads), community
  (Quora, LiveJournal, Tumblr, Discord announcements), local (Google Business
  Profile, Pinterest, review responses), growth (newsletters, FAQs, GEO/
  AI-search, landing pages, repurposing), PR (HARO pitches, press releases,
  case studies, guest articles, business-case one-pagers, crisis statements,
  internal announcements, investor updates, company press kits), creator
  marketing (influencer outreach, UGC briefs, personal-brand posts, creator
  media kits), lifecycle email (onboarding, win-back, churn-prevention,
  upsell/cross-sell), sales enablement (pitch deck narratives, cold call
  scripts, InMail templates, proposal copy), paid ads (display/banner, native,
  retargeting sequences, CTV scripts), employer branding (job postings,
  employee spotlights), events (webinar registration pages, segmented
  post-event follow-up, booth follow-up), and mobile messaging (SMS, push
  notifications, in-app messages).
- **49 flat prompt files** covering everything from ad copy (Google, Meta,
  LinkedIn ads) to buyer personas, whitepapers, webinar promos, and schema
  markup - all reachable from the same CLI.
- **Market registers**: each brand declares `b2b` (default), `b2c`, or
  `creator`, and templates adapt their voice accordingly - professional
  business register, consumer register, or first-person personal-brand
  register - without touching any template code.
- **Provider-agnostic live generation**: `--generate` writes finished content
  via Claude (Anthropic), Gemini (Google), or OpenAI - same prompts, same
  house-style rules, whichever model you have a key for.
- **Phase 10 production tooling**: `--variants N` (generate N differentiated
  versions in one run), `--keywords FILE` (inject a keyword list), `--tone`
  (formal/conversational/urgent/educational/playful), `--language` (any
  target language), `--log-publish` (append to a monthly tracker CSV),
  `--format` (reformat output for Gutenberg/HubSpot/Contentful/Markdown),
  `--with-image-brief` (attach a 3-field visual brief), `--export-scheduler
  buffer` (generate a Buffer import CSV from a bulk run).
- **Dead-link linter**: `lint_content.py --check-urls DIR` crawls all `.md`
  and `.txt` files in a directory, deduplicates URLs, and HEAD-checks each
  with an 8-second timeout — reports dead links with file and line number.
- **HARO DataBank Builder**: internal research tool (Format A: mine a report,
  Format B: verify pending rows, Format C: generate research targets) for
  populating `data/HARO_DataBank.csv` with verified, citable statistics.
- **Single, bulk, and repurposing modes**: one post at a time, a CSV-driven
  batch (ZIP + run log), or transforming an existing piece into another
  platform's format with canonical/duplicate-content guidance built in.
- **Editorial guardrails encoded in every prompt**: human-writing rules (no
  AI-signature phrases, no em dashes, active voice), mandatory stat
  attribution (source + organization + year), banned-CTA-phrase enforcement
  (linted, not just requested), fabrication guardrails on competitor claims
  and first-party numbers, FTC disclosure requirements on sponsored/UGC
  content, and a first-person disclosure rule.
- **46 channel strategy docs** (goal, principles, structure, cadence, failure
  modes per channel), grounded in cited platform research.
- **76 flat prompt files** covering every major channel and content type — from ASO copy and competitive battlecards to chatbot flows, ABM content, podcast ad reads, brand voice guides, and the HARO DataBank Builder (internal research tool).
- **146-term marketing glossary** ([GLOSSARY.md](GLOSSARY.md)) covering 13 disciplines — Analytics, Brand, CRO, Email, Growth, Paid Ads, SEO, Social Media, and more — sourced from Marketing Academy.
- **90+ curated marketing resources** ([RESOURCES.md](RESOURCES.md)) across SEO, paid media, social, email, analytics, copywriting, AI, and learning communities.
- **Governance built in**: a publish/review tracker template, a documented
  citation-verification process, and a human sign-off rule for stat-bearing
  or first-person content.
- **Zero required dependencies** for the core tool (Python 3.9+ stdlib);
  provider SDKs install per-choice via extras.

## Directory Structure

```
Content Wiz/
├── README.md                         ← This file
├── RESOURCES.md                      ← 90+ curated marketing resources across 10 disciplines
├── GLOSSARY.md                       ← 146-term marketing glossary across 13 disciplines
├── strategies/                       ← Channel strategy documents (one per channel)
├── prompts/                          ← AI prompt files (one per content type)
├── output/                           ← Generated prompts, auto-routed into per-type subfolders
│                                        (may contain real generated content for whichever
│                                        brand you configured)
├── data/                             ← Persistent pitch-ready data bank (HARO_DataBank.csv)
├── bulk_template.csv
├── publish_tracker_template.csv      ← Publish/review governance tracker template (copy per cycle)
├── config.json                       ← Brands + defaults (edit here, not in code)
├── config.py                         ← Loads config.json with a safe fallback
├── generate.py                       ← CLI prompt generator (single + bulk + --generate)
├── templates/                        ← 64 rich, parameterized prompt builders, split by domain
│   ├── __init__.py                   ← Re-exports every function at package level
│   ├── _shared.py                    ← HUMAN_WRITING_RULES, RANKABILITY_RULES, RESEARCH_RULES
│   ├── local.py, blog.py, social.py, community.py, creator.py, personal.py, video.py, growth.py, pr.py, lifecycle.py, sales_enablement.py, paid_ads.py, recruitment.py, events.py, mobile_messaging.py
│   ├── cro.py                        ← Landing page copy, CTA variants, hero formula, trust signals
│   ├── product.py                    ← Product launch copy, positioning statements, messaging hierarchy
│   └── ugc.py                        ← UGC briefs, creator briefs, testimonial requests, photo briefs
├── textprompts.py                    ← Loader wiring the flat prompts/*.txt into the CLI
├── llm.py                            ← Optional live generation (--generate); provider-agnostic:
│                                        Anthropic/Claude, Google/Gemini, or OpenAI/Codex-GPT
├── lint_content.py                   ← Content-rule linter (no em-dashes, etc.)
├── pyproject.toml                    ← Packaging + ruff config (content-wiz entry point)
├── hooks/pre-commit                  ← Lint + tests before every commit
├── .github/workflows/ci.yml          ← CI: content lint + ruff + tests
└── test_generate.py                  ← Smoke tests (python -m unittest test_generate)
```

`generate.py` creates each `output/` subfolder on demand from `SUBFOLDER_MAP`.
The subfolders it can produce are:

```
Blog/                Blog_Suggestions/    Business_Case/       Case_Study/
Comparison_Pages/    Content_Brief/       Content_Calendar/    Crisis_Comms/
DataBank/            DevTo_Hashnode/      Discord/             Events/
FAQ/                 GEO/                 GMB/                 Glossary_Pages/
Guest_Articles/       HARO/                Influencer_Outreach/ Instagram/
Internal_Comms/       Investor_Updates/    Landing_Pages/        Lifecycle_Email/
LinkedIn/             LinkedIn_Carousel/   LiveJournal/          Media_Kit/
Medium/               Meta/                Mobile_Messaging/     Newsletter/
Paid_Ads/             Personal_Brand/      Pinterest/            Podcast/
Press_Kit/            Press_Release/       Profile_Bio/          Quora/
Recruitment/          Review_Response/     Sales_Enablement/     Short_Form_Video/
Substack/             Tumblr/              Twitter/              UGC_Briefs/
Video_Scripts/        YouTube/
Misc/  (fallback for any unmapped key)
```

Anything routed to a subfolder not produced via `generate.py --platform livejournal`
or `--platform tumblr` (e.g. hand-written posts dropped into `LiveJournal/` or
`Tumblr/` directly) was placed there manually.

> **Note:** `gmb` and `pinterest` are print-only (`PRINT_ONLY`) in single-run mode
> and write no file; they are still routed into their subfolders inside a bulk ZIP.

---

## Strategy Documents (`strategies/`)

One document per channel. Each doc contains: goal and metric, core principles, repeatable structure, proof system, distribution loop, cadence, and failure modes.

| File | Channel | Primary Metric |
|------|---------|---------------|
| [strategy-haro.md](strategies/strategy-haro.md) | HARO / Connectively / Featured | Media citations and backlinks per month |
| [strategy-linkedin.md](strategies/strategy-linkedin.md) | LinkedIn organic | Engagement rate and follower growth |
| [strategy-medium-blog.md](strategies/strategy-medium-blog.md) | Medium / long-form articles | Reads and referral traffic |
| [strategy-seo-programmatic.md](strategies/strategy-seo-programmatic.md) | SEO and programmatic content | Organic search traffic and rankings |
| [strategy-email-newsletter.md](strategies/strategy-email-newsletter.md) | Email newsletter | Open rate and click-through rate |
| [strategy-content-repurposing.md](strategies/strategy-content-repurposing.md) | Content repurposing system | Derivative pieces per source asset |
| [strategy-guest-articles.md](strategies/strategy-guest-articles.md) | Guest article bylines | Placements per month in Tier 1/2 publications |
| [strategy-youtube-video.md](strategies/strategy-youtube-video.md) | YouTube and video | Average view duration and subscriber growth |
| [strategy-case-studies.md](strategies/strategy-case-studies.md) | Case studies | Conversion rate on case study pages |
| [strategy-ai-search.md](strategies/strategy-ai-search.md) | AI search (GEO/AEO) | AI Overview citations for target keywords |
| [strategy-podcast-guesting.md](strategies/strategy-podcast-guesting.md) | Podcast guesting | Confirmed bookings per month |
| [strategy-gmb.md](strategies/strategy-gmb.md) | Google Business Profile posts | Learn-more CTR on profile views |
| [strategy-livejournal.md](strategies/strategy-livejournal.md) | LiveJournal personal-voice blog | Read-to-completion and return readers |
| [strategy-tumblr.md](strategies/strategy-tumblr.md) | Tumblr aphoristic posts | Reblog rate over raw views |
| [strategy-quora.md](strategies/strategy-quora.md) | Quora answers | Upvote-to-view ratio per answer |
| [strategy-influencer-collabs.md](strategies/strategy-influencer-collabs.md) | Influencer / UGC collaborations | Attributable CPA/ROAS per collaboration |
| [strategy-personal-brand.md](strategies/strategy-personal-brand.md) | Personal brand (individual creator) | Follower-to-engaged-reply ratio and owned-audience growth |
| [strategy-instagram.md](strategies/strategy-instagram.md) | Instagram organic and Reels | Reach, saves, and profile link clicks |
| [strategy-tiktok.md](strategies/strategy-tiktok.md) | TikTok organic and TikTok Ads | Watch-through rate, follower growth, and ROAS |
| [strategy-threads.md](strategies/strategy-threads.md) | Threads (Meta) | Replies and reshares per post |
| [strategy-community-building.md](strategies/strategy-community-building.md) | Community-led growth | Active member retention and community-sourced revenue |
| [strategy-referral.md](strategies/strategy-referral.md) | Referral programs | Referral conversion rate and viral coefficient |
| [strategy-product-launch.md](strategies/strategy-product-launch.md) | Product launch campaigns | Launch-week revenue and activation rate |
| [strategy-paid-social.md](strategies/strategy-paid-social.md) | Paid social (Meta + TikTok) | ROAS, CPL, and thumb-stop rate |
| [strategy-substack.md](strategies/strategy-substack.md) | Substack newsletter | Paid subscriber conversion and open rate |
| [strategy-twitter.md](strategies/strategy-twitter.md) | X / Twitter organic | Impressions, bookmarks, and follower growth |
| [strategy-google-ads.md](strategies/strategy-google-ads.md) | Google Ads paid search | ROAS and Quality Score |
| [strategy-linkedin-ads.md](strategies/strategy-linkedin-ads.md) | LinkedIn paid advertising | CPL and Lead Gen Form conversion rate |
| [strategy-lifecycle-crm.md](strategies/strategy-lifecycle-crm.md) | Lifecycle email and CRM | Activation rate, retention rate, and expansion revenue |
| [strategy-sales-enablement.md](strategies/strategy-sales-enablement.md) | Sales content enablement | Content utilization rate and pipeline influence |
| [strategy-editorial-seo.md](strategies/strategy-editorial-seo.md) | Editorial pillar and topic cluster SEO | Organic traffic to cluster pages and ranking positions |
| [strategy-cro.md](strategies/strategy-cro.md) | Conversion rate optimization | Conversion rate lift per test and statistical significance |
| [strategy-product-marketing.md](strategies/strategy-product-marketing.md) | Product marketing and launches | Launch-week activation rate and win rate |
| [strategy-reddit.md](strategies/strategy-reddit.md) | Reddit organic | Upvote rate and referral traffic from target subreddits |
| [strategy-pinterest.md](strategies/strategy-pinterest.md) | Pinterest | Monthly impressions and outbound link clicks |
| [strategy-events-webinar.md](strategies/strategy-events-webinar.md) | Events and webinars | Attendance rate and post-event pipeline |
| [strategy-crisis-comms.md](strategies/strategy-crisis-comms.md) | Crisis communications | Time to first response and sentiment recovery |
| [strategy-employer-branding.md](strategies/strategy-employer-branding.md) | Employer branding | Application conversion rate and offer acceptance rate |
| [strategy-link-building.md](strategies/strategy-link-building.md) | Link acquisition | Referring domains growth and average DR of new links |
| [strategy-gated-content.md](strategies/strategy-gated-content.md) | Gated content and lead magnets | Landing page conversion rate and post-download MQL rate |
| [strategy-mobile-messaging.md](strategies/strategy-mobile-messaging.md) | SMS, push, and in-app messaging | Click-through rate and opt-out rate |
| [strategy-discord.md](strategies/strategy-discord.md) | Discord community | Weekly active members and message volume |
| [strategy-competitive-analysis.md](strategies/strategy-competitive-analysis.md) | Competitive content intelligence | Content gap coverage and battlecard usage by sales |
| [strategy-technical-seo.md](strategies/strategy-technical-seo.md) | Technical SEO | Core Web Vitals scores and crawl coverage |
| [strategy-pr.md](strategies/strategy-pr.md) | PR and media relations | Media placements per month and domain authority of placements |
| [strategy-investor-comms.md](strategies/strategy-investor-comms.md) | Investor relations | Update open rate and investor response rate |

---

## Prompt Files (`prompts/`)

All prompts reference `_Brand_Detection_Rules.txt` for brand auto-detection. Brands are
defined in `config.json`'s `brands` map (keyed by domain); `edstellar.com` and
`invensislearning.com` ship as examples, and you can add your own brand's domain there.

### Core Content Prompts (upgraded with strategy frameworks)

| File | What It Produces | Key Framework |
|------|-----------------|---------------|
| [HARO_Prompts.txt](prompts/HARO_Prompts.txt) | HARO pitch emails | 5-block pitch structure + CARE framework |
| [LinkedIn_Post_Prompt.txt](prompts/LinkedIn_Post_Prompt.txt) | LinkedIn posts (3 formats) | Hook-Tension-Peak-CTC + 2026 algorithm rules |
| [Medium_Prompt.txt](prompts/Medium_Prompt.txt) | Medium articles (HTML output) | Shiny Dime + Rate of Revelation + 6-section skeleton |
| [Blog_Writing_Prompt.txt](prompts/Blog_Writing_Prompt.txt) | Blog posts (3 types: Pillar/Spoke/Decision) | Topic cluster + EEAT + intent mapping |
| [Newsletter_Prompt.txt](prompts/Newsletter_Prompt.txt) | Newsletter emails (2 modes) | 8-block structure + 6 subject line patterns |
| [Case_Study_Prompt.txt](prompts/Case_Study_Prompt.txt) | Case studies (web + PDF) | BAB-Plus framework + metrics enforcement |
| [Video_Script_Prompt.txt](prompts/Video_Script_Prompt.txt) | Video scripts (3 types) | YouTube retention structure + 30-sec hook rule |
| [GEO_Prompt.txt](prompts/GEO_Prompt.txt) | GEO optimization (3 modes) | 4-layer chunk format + FAQPage schema |
| [Repurpose_Prompt.txt](prompts/Repurpose_Prompt.txt) | Content repurposing map (4 source types) | Full derivative map + production sequence |
| [Podcast_Prompt.txt](prompts/Podcast_Prompt.txt) | Show notes / scripts / guest pitch (3 modes) | Primary takeaway framework + 11-derivative loop |
| [Guest_Article_Pitch_Prompt.txt](prompts/Guest_Article_Pitch_Prompt.txt) | Guest article pitches + full articles | 4-block pitch formula + trade publication structure |

### Additional Prompt Files

| File | What It Produces |
|------|-----------------|
| [GMB_Prompt.txt](prompts/GMB_Prompt.txt) | Google My Business posts |
| [LinkedIn_Carousel_Prompt.txt](prompts/LinkedIn_Carousel_Prompt.txt) | LinkedIn carousel slides (5 carousel types + caption) |
| [LinkedIn_Article_Prompt.txt](prompts/LinkedIn_Article_Prompt.txt) | LinkedIn long-form articles |
| [Twitter_Thread_Prompt.txt](prompts/Twitter_Thread_Prompt.txt) | Twitter/X threads (5 thread types + hook patterns) |
| [YouTube_Description_Prompt.txt](prompts/YouTube_Description_Prompt.txt) | YouTube descriptions + chapters + pinned comment (2 modes) |
| [Meta_SEO_Prompt.txt](prompts/Meta_SEO_Prompt.txt) | Meta titles and descriptions |
| [FAQ_Prompt.txt](prompts/FAQ_Prompt.txt) | FAQ sections |
| [Schema_Markup_Prompt.txt](prompts/Schema_Markup_Prompt.txt) | Schema markup code |
| [Content_Calendar_Prompt.txt](prompts/Content_Calendar_Prompt.txt) | Monthly content calendars |
| [Topic_Cluster_Prompt.txt](prompts/Topic_Cluster_Prompt.txt) | SEO topic cluster mapping |
| [Content_Brief_Prompt.txt](prompts/Content_Brief_Prompt.txt) | Article briefs for writers |
| [Press_Release_Prompt.txt](prompts/Press_Release_Prompt.txt) | Press releases |
| [Whitepaper_eBook_Prompt.txt](prompts/Whitepaper_eBook_Prompt.txt) | Whitepapers and eBooks |
| [Original_Research_Report_Prompt.txt](prompts/Original_Research_Report_Prompt.txt) | Original research reports |
| [Email_Drip_Sequence_Prompt.txt](prompts/Email_Drip_Sequence_Prompt.txt) | Email drip sequences |
| [Google_Ads_Prompt.txt](prompts/Google_Ads_Prompt.txt) | Google Ads copy |
| [LinkedIn_Ads_Prompt.txt](prompts/LinkedIn_Ads_Prompt.txt) | LinkedIn Ads copy |
| [Meta_Facebook_Ads_Prompt.txt](prompts/Meta_Facebook_Ads_Prompt.txt) | Meta/Facebook Ads copy |
| [Instagram_Prompt.txt](prompts/Instagram_Prompt.txt) | Instagram captions |
| [Pinterest_Prompt.txt](prompts/Pinterest_Prompt.txt) | Pinterest posts |
| [Webinar_Promo_Prompt.txt](prompts/Webinar_Promo_Prompt.txt) | Webinar promotional content |
| [Course_Training_Description_Prompt.txt](prompts/Course_Training_Description_Prompt.txt) | Course and training descriptions |
| [Buyer_Persona_Prompt.txt](prompts/Buyer_Persona_Prompt.txt) | Buyer persona documents |
| [Competitor_Content_Gap_Prompt.txt](prompts/Competitor_Content_Gap_Prompt.txt) | Competitor gap analysis |
| [Blog_Suggestion_Prompt.txt](prompts/Blog_Suggestion_Prompt.txt) | Blog topic suggestions |
| [Thought_Leadership_OpEd_Prompt.txt](prompts/Thought_Leadership_OpEd_Prompt.txt) | Op-eds and thought leadership |
| [Internal_Linking_Prompt.txt](prompts/Internal_Linking_Prompt.txt) | Internal linking recommendations |
| [Backlink_Outreach_Email_Prompt.txt](prompts/Backlink_Outreach_Email_Prompt.txt) | Link building outreach emails |
| [Testimonial_Review_Request_Prompt.txt](prompts/Testimonial_Review_Request_Prompt.txt) | Client testimonial requests |
| [Quora_Prompt.txt](prompts/Quora_Prompt.txt) | Quora answers |
| [Reddit_Post_Prompt.txt](prompts/Reddit_Post_Prompt.txt) | Reddit posts |
| [DevTo_Hashnode_Prompt.txt](prompts/DevTo_Hashnode_Prompt.txt) | Dev.to and Hashnode posts |
| [SlideShare_Presentation_Prompt.txt](prompts/SlideShare_Presentation_Prompt.txt) | SlideShare presentations |
| [Image_Alt_Text_Prompt.txt](prompts/Image_Alt_Text_Prompt.txt) | Image alt text |
| [Interactive_Content_Prompt.txt](prompts/Interactive_Content_Prompt.txt) | Interactive content (quizzes, assessments) |
| [Skills_Gap_Analysis_Prompt.txt](prompts/Skills_Gap_Analysis_Prompt.txt) | Skills gap analysis documents |
| [Trainer_Speaker_Bio_Prompt.txt](prompts/Trainer_Speaker_Bio_Prompt.txt) | Trainer and speaker bios |
| [TikTok_Ads_Prompt.txt](prompts/TikTok_Ads_Prompt.txt) | TikTok Ads copy (Spark Ads, TopView, In-Feed) |
| [Instagram_Content_Prompt.txt](prompts/Instagram_Content_Prompt.txt) | Instagram captions, Reels hooks, and Stories (3 formats) |
| [TikTok_Content_Prompt.txt](prompts/TikTok_Content_Prompt.txt) | TikTok organic scripts with hook + CTA structure |
| [Threads_Post_Prompt.txt](prompts/Threads_Post_Prompt.txt) | Threads posts optimised for replies and reshares |
| [Landing_Page_Copy_Prompt.txt](prompts/Landing_Page_Copy_Prompt.txt) | Landing page copy (lead-gen and sales variants) |
| [Product_Launch_Prompt.txt](prompts/Product_Launch_Prompt.txt) | Product launch copy across pre-launch, launch, and post-launch |
| [UGC_Brief_Prompt.txt](prompts/UGC_Brief_Prompt.txt) | UGC video and photo briefs for creators |
| [Substack_Post_Prompt.txt](prompts/Substack_Post_Prompt.txt) | Substack essays, Notes, and restacks |
| [Referral_Program_Copy_Prompt.txt](prompts/Referral_Program_Copy_Prompt.txt) | Referral program invite and incentive copy |
| [Sales_Email_Prompt.txt](prompts/Sales_Email_Prompt.txt) | Cold outreach and follow-up sales email sequences |
| [Facebook_Organic_Post_Prompt.txt](prompts/Facebook_Organic_Post_Prompt.txt) | Facebook organic page and group posts (3 formats) |
| [Twitter_Ads_Prompt.txt](prompts/Twitter_Ads_Prompt.txt) | X / Twitter paid ads (Promoted Post, Image, Video, Carousel, Follower) |
| [LinkedIn_Newsletter_Prompt.txt](prompts/LinkedIn_Newsletter_Prompt.txt) | LinkedIn native newsletters with subscriber growth guidance |
| [YouTube_Shorts_Prompt.txt](prompts/YouTube_Shorts_Prompt.txt) | YouTube Shorts scripts (distinct from TikTok/Reels structure) |
| [ASO_Copy_Prompt.txt](prompts/ASO_Copy_Prompt.txt) | App Store Optimization copy for iOS and Google Play |
| [Competitive_Battlecard_Prompt.txt](prompts/Competitive_Battlecard_Prompt.txt) | Internal sales competitive battlecards (verified claims only) |
| [Customer_Success_Email_Prompt.txt](prompts/Customer_Success_Email_Prompt.txt) | Customer success and renewal emails (6 types with trigger signals) |
| [Chatbot_Flow_Prompt.txt](prompts/Chatbot_Flow_Prompt.txt) | Chatbot and live chat conversation flows |
| [ABM_Content_Prompt.txt](prompts/ABM_Content_Prompt.txt) | Account-based marketing personalized content (3 ABM tiers) |
| [Brand_Voice_Style_Guide_Prompt.txt](prompts/Brand_Voice_Style_Guide_Prompt.txt) | Brand voice and style guide generator |
| [Partnership_Comarketing_Prompt.txt](prompts/Partnership_Comarketing_Prompt.txt) | Co-branded content and partner marketing copy |
| [Annual_Report_Prompt.txt](prompts/Annual_Report_Prompt.txt) | Corporate annual reports and nonprofit impact reports |
| [Podcast_Ad_Read_Prompt.txt](prompts/Podcast_Ad_Read_Prompt.txt) | Podcast sponsorship scripts (pre-roll / mid-roll / host-endorsed) |
| [Survey_Feedback_Copy_Prompt.txt](prompts/Survey_Feedback_Copy_Prompt.txt) | NPS surveys, post-purchase surveys, and interview invitation emails |
| [Newsletter_Sponsorship_Pitch_Prompt.txt](prompts/Newsletter_Sponsorship_Pitch_Prompt.txt) | Newsletter ad slot sales: media kit, cold email, follow-up sequence |
| [Community_Welcome_Prompt.txt](prompts/Community_Welcome_Prompt.txt) | Community onboarding and moderation copy (Slack, Discord, Circle) |
| [Bing_Ads_Prompt.txt](prompts/Bing_Ads_Prompt.txt) | Microsoft Advertising / Bing Ads copy with LinkedIn audience targeting |

---

## Resources (`RESOURCES.md`)

[RESOURCES.md](RESOURCES.md) is a curated directory of 90+ high-signal marketing resources across 10 disciplines: SEO & GEO, Paid Media, Social Media, Content Marketing, Email & Lifecycle, Analytics & Attribution, Copywriting & CRO, Brand Strategy, AI Marketing Tools, and Learning & Communities. Each entry includes the resource name, type (tool / course / community / newsletter), and a one-line description.

---

## Glossary (`GLOSSARY.md`)

[GLOSSARY.md](GLOSSARY.md) contains 146 marketing terms across 13 disciplines — Analytics, Brand, Business Metrics, Content, Copywriting, CRO, Email, Growth, Paid Ads, Psychology, SEO, Social Media, and Strategy — each with a plain-English definition and related terms. Cross-reference with `prompts/` files when generating content (e.g. check CRO terms before using `Landing_Page_Copy_Prompt.txt`). Sourced from [Marketing Academy](https://marketing-academy-roan.vercel.app/glossary).

---

## CLI Coverage (`generate.py`)

The generator automates a subset of the prompt library. The rest are **manual**:
copy the prompt file into your AI tool by hand. This table is the source of truth
for what `generate.py` can produce.

### Automated (routed in `PLATFORM_MAP`)

| Template key | CLI aliases (`--platform`) | Output subfolder |
|--------------|----------------------------|------------------|
| `gmb` | `gmb`, `google` | GMB *(print-only)* |
| `pinterest` | `pinterest` | Pinterest *(print-only)* |
| `medium` | `medium` | Medium |
| `blog_suggestion` | `suggestion`, `suggestions`, `ideas` | Blog_Suggestions |
| `blog_writing` | `linkedin`, `wordpress`, `blog` | Blog |
| `blog_writing_md` | `devto`, `dev.to`, `hashnode` | DevTo_Hashnode |
| `linkedin_post` | `linkedin_post`, `linkedin-post`, `linkedinpost` | LinkedIn |
| `twitter_thread` | `twitter`, `twitter_thread`, `x`, `thread` | Twitter |
| `youtube_desc` | `youtube`, `youtube_desc`, `yt` | YouTube |
| `newsletter` | `newsletter`, `email` | Newsletter |
| `quora` | `quora` | Quora |
| `instagram` | `instagram`, `ig` | Instagram |
| `content_brief` | `content_brief`, `brief` | Content_Brief |
| `faq` | `faq` | FAQ |
| `meta` | `meta` | Meta |
| `case_study` | `case_study`, `casestudy` | Case_Study |
| `press_release` | `press_release`, `pressrelease`, `pr` | Press_Release |
| `repurpose` | `repurpose` (or `--repurpose FILE`) | DataBank |
| `content_calendar` | `calendar`, `content_calendar` | Content_Calendar |
| `haro` | `haro`, `connectively`, `featured` | HARO |
| `linkedin_carousel` | `linkedin_carousel`, `carousel` | LinkedIn_Carousel |
| `video_script` | `video_script`, `video`, `script` | Video_Scripts |
| `geo` | `geo`, `aeo`, `ai_search` | GEO |
| `podcast` | `podcast`, `show_notes` | Podcast |
| `guest_article` | `guest_article`, `guest`, `byline` | Guest_Articles |
| `livejournal_post` | `livejournal`, `lj` | LiveJournal |
| `tumblr_post` | `tumblr` | Tumblr |
| `short_form_video` | `short_form_video`, `shorts`, `reels`, `tiktok` | Short_Form_Video |
| `landing_page` | `landing_page`, `landing`, `lp` | Landing_Pages |
| `comparison_page` | `comparison_page`, `comparison`, `vs`, `alternative` | Comparison_Pages |
| `business_case_one_pager` | `business_case_one_pager`, `business_case`, `one_pager`, `internal_pitch` | Business_Case |
| `influencer_outreach` | `influencer_outreach`, `outreach`, `influencer` | Influencer_Outreach |
| `ugc_brief` | `ugc_brief`, `ugc`, `creator_brief` | UGC_Briefs |
| `personal_brand_post` | `personal_brand_post`, `personal_brand`, `personal_post` | Personal_Brand |
| `creator_media_kit` | `creator_media_kit`, `media_kit`, `mediakit` | Media_Kit |
| `profile_bio` | `profile_bio`, `profile`, `social_bio` | Profile_Bio |
| `review_response` | `review_response`, `review`, `reviews` | Review_Response |
| `substack_post` | `substack_post`, `substack` | Substack |
| `glossary_page` | `glossary_page`, `glossary`, `definition_page` | Glossary_Pages |
| `discord_announcement` | `discord_announcement`, `discord` | Discord |
| `onboarding_sequence` | `onboarding_sequence`, `onboarding` | Lifecycle_Email |
| `win_back_sequence` | `win_back_sequence`, `win_back`, `winback` | Lifecycle_Email |
| `churn_prevention` | `churn_prevention`, `churn` | Lifecycle_Email |
| `upsell_cross_sell` | `upsell_cross_sell`, `upsell`, `cross_sell` | Lifecycle_Email |
| `pitch_deck_narrative` | `pitch_deck_narrative`, `pitch_deck` | Sales_Enablement |
| `cold_call_script` | `cold_call_script`, `cold_call` | Sales_Enablement |
| `inmail_template` | `inmail_template`, `inmail` | Sales_Enablement |
| `proposal_copy` | `proposal_copy`, `proposal` | Sales_Enablement |
| `crisis_statement` | `crisis_statement`, `crisis` | Crisis_Comms |
| `internal_announcement` | `internal_announcement`, `internal_comms` | Internal_Comms |
| `investor_update` | `investor_update`, `investor` | Investor_Updates |
| `press_kit` | `press_kit`, `media_kit_company` | Press_Kit |
| `display_banner_copy` | `display_banner_copy`, `display_ads`, `banner_ads` | Paid_Ads |
| `native_ad_copy` | `native_ad_copy`, `native_ads` | Paid_Ads |
| `retargeting_sequence` | `retargeting_sequence`, `retargeting` | Paid_Ads |
| `ctv_script` | `ctv_script`, `ctv`, `streaming_ad` | Paid_Ads |
| `job_posting` | `job_posting`, `job`, `recruitment` | Recruitment |
| `employee_spotlight` | `employee_spotlight`, `spotlight` | Recruitment |
| `webinar_registration_page` | `webinar_registration_page`, `webinar_registration`, `event_registration` | Events |
| `event_followup_sequence` | `event_followup_sequence`, `event_followup` | Events |
| `booth_followup` | `booth_followup`, `booth` | Events |
| `sms_blast` | `sms_blast`, `sms` | Mobile_Messaging |
| `push_notification` | `push_notification`, `push` | Mobile_Messaging |
| `in_app_message` | `in_app_message`, `in_app` | Mobile_Messaging |

> **Alias gotcha:** `--platform linkedin`, `wordpress`, and `blog` all resolve to
> `blog_writing` (long-form blog). For a LinkedIn *post*, use `--platform linkedin_post`.

### Text prompts (flat prompt files, wired via `textprompts.py`)

These load their `prompts/*.txt` file directly, substitute topic/audience/CTA/URL,
and leave brand tokens for the LLM to resolve. Run them exactly like the rich
templates: `python generate.py --platform <alias> --topic "..."`.

| Prompt file | Aliases | Output subfolder |
|-------------|---------|------------------|
| Backlink_Outreach_Email | `backlink`, `backlink_outreach` | Backlink_Outreach |
| Buyer_Persona | `buyer_persona`, `persona` | Buyer_Personas |
| Competitor_Content_Gap | `competitor_gap`, `competitor` | Competitor_Gap_Analysis |
| Course_Training_Description | `course`, `course_description` | Course_Descriptions |
| Email_Drip_Sequence | `email_drip`, `drip` | Email_Drip |
| Google_Ads | `google_ads` | Google_Ads |
| Image_Alt_Text | `alt_text`, `image_alt` | Image_Alt_Text |
| Interactive_Content | `interactive`, `quiz` | Interactive_Content |
| Internal_Linking | `internal_linking`, `linking` | Internal_Linking |
| LinkedIn_Ads | `linkedin_ads` | LinkedIn_Ads |
| LinkedIn_Article | `linkedin_article` | LinkedIn_Article |
| Meta_Facebook_Ads | `meta_ads`, `facebook_ads` | Meta_Facebook_Ads |
| Original_Research_Report | `research_report`, `research` | Research_Reports |
| Reddit_Post | `reddit` | Reddit |
| Schema_Markup | `schema`, `schema_markup` | Schema_Markup |
| Skills_Gap_Analysis | `skills_gap` | Skills_Gap_Analysis |
| SlideShare_Presentation | `slideshare`, `presentation` | SlideShare |
| Testimonial_Review_Request | `testimonial`, `review_request` | Testimonial_Request |
| Thought_Leadership_OpEd | `thought_leadership`, `oped` | Thought_Leadership |
| Topic_Cluster | `topic_cluster`, `cluster` | Topic_Cluster |
| Trainer_Speaker_Bio | `trainer_bio`, `bio` | Trainer_Bios |
| Webinar_Promo | `webinar`, `webinar_promo` | Webinar_Promo |
| Whitepaper_eBook | `whitepaper`, `ebook` | Whitepaper_eBook |

Run `python generate.py --list` for the live, authoritative list of every alias.

---

## CLI Flags

| Flag | Purpose |
|------|---------|
| `--platform`, `--topic` | Required for a single run (or use `--bulk`). |
| `--wordcount`, `--audience`, `--cta`, `--url` | Optional generation parameters. |
| `--title` | Medium step 2: the chosen article title. |
| `--repurpose FILE` | Repurpose an existing file into `--platform`. |
| `--bulk CSV` | Batch mode: writes a ZIP + run-log CSV. |
| `--list` | Print all platforms/aliases and exit. |
| `--dry-run` | Print the assembled prompt without writing a file. |
| `--generate` | Call an LLM and save finished content instead of just the prompt (needs that provider's API key + SDK - see "LLM Providers" below). |
| `--provider` | Which LLM to use for `--generate`: `anthropic` (default), `gemini`, or `openai`. |
| `--model` | Override the LLM model id for `--generate` (defaults to the selected provider's entry in `config.json`). |

## LLM Providers (`--generate`)

`--generate` is provider-agnostic: the same prompt and the same house-style rules
are sent to whichever model actually writes it. This does not mean equal output
quality: providers differ in instruction-following fidelity, reasoning depth, and
hallucination rate on long, structured prompts like this repo's templates. Give
closer editorial review to output from a non-default provider until you have
validated it against your own templates and audience. Pick a provider with
`--provider`, install only that provider's SDK, and export only that provider's
key:

| `--provider` | SDK to install | API key env var |
|---|---|---|
| `anthropic` (default) | `pip install .[llm-anthropic]` (or `pip install anthropic`) | `ANTHROPIC_API_KEY` |
| `gemini` | `pip install .[llm-gemini]` (or `pip install google-genai`) | `GEMINI_API_KEY` (or `GOOGLE_API_KEY`) |
| `openai` | `pip install .[llm-openai]` (or `pip install openai`) | `OPENAI_API_KEY` |

```bash
export ANTHROPIC_API_KEY=sk-ant-...
python generate.py --platform blog --topic "..." --generate                     # anthropic, default

export GEMINI_API_KEY=...
python generate.py --platform blog --topic "..." --generate --provider gemini

export OPENAI_API_KEY=sk-...
python generate.py --platform blog --topic "..." --generate --provider openai --model gpt-5
```

Change the default provider for every run in `config.json`'s `defaults.llm_provider`
(see below) instead of passing `--provider` every time.

### Cost reference (added 2026-07-13, check before scaling volume)

This repo does not hardcode per-token prices for any provider; they change too
often to keep accurate in source control. Before running `--generate` at any
real volume, check each provider's own current pricing page rather than
relying on a number from this file or from memory:

| Provider | Pricing page |
|---|---|
| Anthropic (Claude) | https://www.anthropic.com/pricing |
| Google (Gemini) | https://ai.google.dev/gemini-api/docs/pricing |
| OpenAI (GPT) | https://openai.com/api/pricing/ |

This note is undated-content-agnostic advice, not a one-time check: re-check
the relevant pricing page before any batch large enough that a per-token rate
change would matter to your budget. For a rough back-of-envelope estimate of
a single generated post's cost, a platform's `--wordcount` target (or its
template default in `config.json`) is a reasonable proxy for output tokens
(roughly 1.3-1.5 tokens per word in English), plus the prompt's own length
(typically a few hundred to low thousands of tokens depending on template)
for input tokens. Multiply each by the provider's current per-token rate from
the pricing page above to estimate cost per post.

## Configuration (`config.json`)

Brands, default audience, default word count, and the LLM provider/model/token
defaults live in `config.json` - edit there, not in code. `defaults.llm_provider`
sets which provider `--generate` uses when `--provider` isn't passed;
`defaults.llm_models` maps each provider name to its default model id, used when
`--model` isn't passed. `config.py` loads it with a safe fallback if the file is
missing.

Each brand entry can also declare:

- **`market`** - `"b2b"` (default), `"b2c"`, or `"creator"`. Selects the voice
  register (`MARKET_VOICE_RULES` in `templates/_shared.py`) that flows into
  templates: professional business language, consumer language, or a
  first-person personal-brand voice. Brands with no `market` field behave
  exactly as before (B2B).
- **`platform_audience_overrides`** - an optional map of platform alias →
  audience string, so e.g. a LiveJournal post can target a community audience
  while the brand's default stays B2B decision-makers.

## Development

```bash
python -m unittest test_generate -v   # tests
python lint_content.py                # content-rule lint (no em-dashes, etc.)
ruff check .                          # style lint
git config core.hooksPath hooks       # enable the pre-commit hook (once per clone)
```

CI runs all three on every push/PR (`.github/workflows/ci.yml`).

---

## Data (`data/`)

| File | Contents |
|------|----------|
| [HARO_DataBank.csv](data/HARO_DataBank.csv) | Pitch-ready, verified statistics and findings for HARO responses, guest articles, and podcast appearances |
| [HARO_DataBank_PENDING.csv](data/HARO_DataBank_PENDING.csv) | Unfilled `[PLACEHOLDER]` claims quarantined out of the main bank so they can never be cited by accident |

**DataBank CSV columns:** Claim | Source | URL | Year | Context | Quotable Version | Topic Tags

Add a new row to HARO_DataBank.csv every time a new first-party statistic, client outcome metric, or citable finding is available and verified. If the figure isn't confirmed yet, add the row to HARO_DataBank_PENDING.csv instead, fill it in from real internal data, then move it into HARO_DataBank.csv and delete it from the pending file. Never cite a row directly from the pending file.

---

## Global Content Rules

All content produced in this system follows these rules (defined in [prompts/_Brand_Detection_Rules.txt](prompts/_Brand_Detection_Rules.txt)):

1. No em dashes anywhere
2. No passive voice
3. Match the brand's configured market register (`market` field in `config.json`: `b2b` default, `b2c`, or `creator`) - B2B professional language unless the brand is explicitly configured otherwise
4. Every statistic names its source, organization, and year
5. Output saves to the appropriate `output/` subfolder
6. Bulk content types (GMB, Pinterest, multi-post batches) output as CSV
7. No promotional brand tone in content body
8. Every statistic is verified against a real, live source before publish (see below)
9. Source-diversity: within any content cluster (multiple posts published close
   together on related topics), never reuse the exact same single source as the
   sole statistical anchor across more than one post in that cluster. A vague
   reference like "Harvard Business Review has written extensively about..."
   with no article title or year is never an acceptable citation, name a
   specific report/article and year every time
10. Third-party research is characterized accurately and never implied to
    endorse, sponsor, or partner with the brand (see `RESEARCH_RULES` in
    `templates/_shared.py`)
11. Any first-party/proprietary-sounding statistic traces to a row in
    `data/HARO_DataBank.csv`, not the model's general knowledge (external
    academic/industry stats are exempt, see Citation Verification below)
12. Any stat-bearing post, or any post using first-person/confessional voice,
    requires a human reviewer's sign-off (name + date) before its `Status`
    can move to "Published" on the content calendar tracker (use
    `publish_tracker_template.csv`, copied to a dated working file per
    cycle, see Governance note below), this is a process discipline today,
    not code-enforced

Rule 4 is enforced by the prompt instructions at generation time; it does not by
itself guarantee the citation is accurate; a model can name a real organization
and year while still misstating the finding. Rule 8 is the separate verification
step that closes that gap.

### Citation Verification (pre-publish step, not yet automated)

Before any generated post carrying a statistic is marked ready to publish, run a
research pass that checks every cited claim against a live source:

1. Read the finished file(s) and list every sentence that names a source,
   organization, or study.
2. For each one, search for the real source and confirm the claim matches what
   it actually says (right figure, right year, right report edition).
3. If verified: tighten the sentence to name the specific report/edition if it
   was vague (e.g. "Gallup's research" → "Gallup's 2023 State of the Global
   Workplace report").
4. If wrong, outdated, or unverifiable after a real search effort: correct the
   figure/source, replace it with a verifiable alternative, or soften the claim
   to a qualitative statement with no fabricated precision. Never invent a
   fake-precise fix.
5. Do not touch anything else in the file, this is a citation-only pass.

This applies per content batch, not per platform template, since the same
underlying claim (e.g. "44% of core job skills will be disrupted within 5
years") can recur across multiple posts and should be verified once and then
kept consistent. `data/HARO_DataBank.csv` rows marked `[PLACEHOLDER]` are a
brand's own first-party program data, not web-researchable, they need to be
filled from that brand's internal metrics instead.

This step is currently manual (or agent-assisted on request), it is not wired
into `generate.py` or `lint_content.py`, so nothing blocks a citation-unverified
file from landing in `output/`. Treat it as a required gate before publish, not
an optional polish pass.

### Cluster Citation Diversity Pass

A named, repeatable process for the specific failure mode where a batch or
cluster over-relies on the same stat(s)/source(s) across multiple posts. Run
it whenever a batch is flagged for this (referenceable by name: "run a
Cluster Citation Diversity Pass on X"). Two variants:

**(a) Repeated generic promotional stats within one batch** (e.g. a GMB batch
where multiple rows carry the same kind of unsourced headline number, "$438
billion annually"):
1. List every stat-bearing sentence in the batch.
2. WebSearch for the real source behind each one.
3. If found: cite it inline with exact organization + year + figure.
4. If not confirmable after a real search effort: remove the stat, or replace
   it with a qualitative claim. Never fabricate a precise-sounding number to
   fill the gap.

**(b) One cluster leaning on a single repeated source** (e.g. four LiveJournal
posts all anchored on "Gallup's State of the Global Workplace"):
1. Identify which posts in the cluster share a source.
2. WebSearch for distinct, verifiable alternative reports covering the same
   underlying claim, for all but one of the posts in the cluster.
3. Confirm each alternative source actually supports the specific claim being
   made, not just the general topic area.
4. Replace and re-run `lint_content.py` to confirm no em-dash/passive-voice
   violations were introduced by the edit.

### Governance note

No content in this pipeline has an enforced human sign-off gate before it
lands in `output/`. The only automated enforcement anywhere in this pipeline
is `lint_content.py`'s em-dash/passive-voice check, it does not check citation
accuracy, brand-safety, or claim validity. Standing rule: any stat-bearing
post, or any post written in first-person/confessional voice, requires a
human reviewer's sign-off (name + date, tracked on the content calendar
tracker) before its `Status` can move to "Published." This is a process
discipline today, not something the code blocks on.

Use [publish_tracker_template.csv](publish_tracker_template.csv) as the
actual tracker artifact: it already has the `Reviewed By`/`Review Date`
columns this rule requires, plus `Status`, `Clicks`, `Leads/Conversions`,
and `Last Checked` for lightweight post-publish follow-up. Copy it to a
dated working file at the start of each publishing cycle (e.g.
`jul2026_publish_tracker.csv`) rather than editing the template in place,
so the template stays reusable across cycles.

---

## Example Brands (`config.json`)

These ship as working examples in `config.json`'s `brands` map. Edit their fields,
delete them, or add a new domain entry with your own brand's name, description,
audience, hashtag, and market register.

| Domain | Brand | Market | Description |
|--------|-------|--------|-------------|
| edstellar.com | Edstellar | b2b | Global corporate training company delivering high-impact training solutions for enterprise teams |
| invensislearning.com | Invensis Learning | b2b | Global professional training and certification provider across project management, IT service management, agile, and cybersecurity |
| example-creator.com | `[YOUR NAME]` placeholder | creator | A deliberately unusable placeholder entry showing the creator/personal-brand register - replace every `[BRACKETED]` field with a real creator's details (or delete) before publishing anything generated from it |
