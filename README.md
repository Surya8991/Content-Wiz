# Edstellar Content Creation - Master Index

## Directory Structure

```
Edstellar Content Creation/
├── README.md                         ← This file
├── strategies/                       ← Channel strategy documents (one per channel)
├── prompts/                          ← AI prompt files (one per content type)
├── output/                           ← Generated prompts, auto-routed into per-type subfolders
├── data/                             ← Persistent pitch-ready data bank (HARO_DataBank.csv)
├── bulk_template.csv
├── generate.py                       ← CLI prompt generator (single + bulk)
├── templates.py                      ← Prompt template functions
└── test_generate.py                  ← Smoke tests (python -m unittest test_generate)
```

`generate.py` creates each `output/` subfolder on demand from `SUBFOLDER_MAP`.
The subfolders it can produce are:

```
Blog/                Blog_Suggestions/    Case_Study/          Content_Brief/
Content_Calendar/    DataBank/            DevTo_Hashnode/      FAQ/
GEO/                 GMB/                 Guest_Articles/      HARO/
Instagram/           LinkedIn/            LinkedIn_Carousel/   Medium/
Meta/                Newsletter/          Pinterest/           Podcast/
Press_Release/       Quora/               Twitter/             Video_Scripts/
YouTube/             Misc/  (fallback for any unmapped key)
```

Anything routed to a subfolder not in this list (e.g. `LiveJournal/`, `Tumblr/`)
was placed there manually and is not produced by `generate.py`.

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

---

## Prompt Files (`prompts/`)

All prompts reference `_Brand_Detection_Rules.txt` for brand auto-detection. Known brands: `edstellar.com` and `invensislearning.com`.

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

> **Alias gotcha:** `--platform linkedin`, `wordpress`, and `blog` all resolve to
> `blog_writing` (long-form blog). For a LinkedIn *post*, use `--platform linkedin_post`.

### Manual only (no CLI route yet)

These have a `prompts/*.txt` file but **no** `templates.py` function or `PLATFORM_MAP`
entry - run them by hand until wired in:

`Backlink_Outreach_Email`, `Buyer_Persona`, `Competitor_Content_Gap`,
`Course_Training_Description`, `Email_Drip_Sequence`, `Google_Ads`, `Image_Alt_Text`,
`Interactive_Content`, `Internal_Linking`, `LinkedIn_Ads`, `LinkedIn_Article`,
`Meta_Facebook_Ads`, `Original_Research_Report`, `Reddit_Post`, `Schema_Markup`,
`Skills_Gap_Analysis`, `SlideShare_Presentation`, `Testimonial_Review_Request`,
`Thought_Leadership_OpEd`, `Topic_Cluster`, `Trainer_Speaker_Bio`, `Webinar_Promo`,
`Whitepaper_eBook`.

---

## Data (`data/`)

| File | Contents |
|------|----------|
| [HARO_DataBank.csv](data/HARO_DataBank.csv) | Pitch-ready statistics and findings for HARO responses, guest articles, and podcast appearances |

**DataBank CSV columns:** Claim | Source | URL | Year | Context | Quotable Version | Topic Tags

Add a new row to HARO_DataBank.csv every time a new first-party statistic, client outcome metric, or citable finding is available.

---

## Global Content Rules

All content produced in this system follows these rules (defined in [prompts/_Brand_Detection_Rules.txt](prompts/_Brand_Detection_Rules.txt)):

1. No em dashes anywhere
2. No passive voice
3. B2B language only
4. Every statistic names its source, organization, and year
5. No promotional brand tone in content body
6. Output saves to the appropriate `output/` subfolder
7. Brand auto-detection from URL before generating any content

---

## Known Brands

| Domain | Brand | Description |
|--------|-------|-------------|
| edstellar.com | Edstellar | Global corporate training company delivering high-impact training solutions for enterprise teams |
| invensislearning.com | Invensis Learning | Global professional training and certification provider across project management, IT service management, agile, and cybersecurity |
