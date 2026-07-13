# Content Wiz - Multi-Brand Content Distribution Prompt Generator

Content Wiz assembles fully-specified, channel-ready content prompts for any brand.
It is not tied to one company: `config.json` holds a `brands` map keyed by domain,
where each entry defines a brand's name, description, audience, and hashtag. Pass
`--url yourdomain.com` when generating and the audience auto-fills from the matching
brand entry; without a matching entry (or without `--url`), it falls back to a
neutral default audience. `--audience` always overrides both. Edstellar and Invensis
Learning ship as two working example brands in `config.json` - edit them, delete
them, or add your own.

## Directory Structure

```
Content Wiz/
├── README.md                         ← This file
├── strategies/                       ← Channel strategy documents (one per channel)
├── prompts/                          ← AI prompt files (one per content type)
├── output/                           ← Generated prompts, auto-routed into per-type subfolders
│                                        (may contain real generated content for whichever
│                                        brand you configured)
├── data/                             ← Persistent pitch-ready data bank (HARO_DataBank.csv)
├── bulk_template.csv
├── config.json                       ← Brands + defaults (edit here, not in code)
├── config.py                         ← Loads config.json with a safe fallback
├── generate.py                       ← CLI prompt generator (single + bulk + --generate)
├── templates/                        ← 27 rich, parameterized prompt builders, split by domain
│   ├── __init__.py                   ← Re-exports every function at package level
│   ├── _shared.py                    ← HUMAN_WRITING_RULES, RANKABILITY_RULES, RESEARCH_RULES
│   ├── local.py, blog.py, social.py, community.py, video.py, growth.py, pr.py
├── textprompts.py                    ← Loader wiring the flat prompts/*.txt into the CLI
├── llm.py                            ← Optional Anthropic generation (--generate)
├── lint_content.py                   ← Content-rule linter (no em-dashes, etc.)
├── pyproject.toml                    ← Packaging + ruff config (content-wiz entry point)
├── hooks/pre-commit                  ← Lint + tests before every commit
├── .github/workflows/ci.yml          ← CI: content lint + ruff + tests
└── test_generate.py                  ← Smoke tests (python -m unittest test_generate)
```

`generate.py` creates each `output/` subfolder on demand from `SUBFOLDER_MAP`.
The subfolders it can produce are:

```
Blog/                Blog_Suggestions/    Case_Study/          Content_Brief/
Content_Calendar/    DataBank/            DevTo_Hashnode/      FAQ/
GEO/                 GMB/                 Guest_Articles/      HARO/
Instagram/           LinkedIn/            LinkedIn_Carousel/   LiveJournal/
Medium/              Meta/                Newsletter/          Pinterest/
Podcast/             Press_Release/       Quora/               Tumblr/
Twitter/             Video_Scripts/       YouTube/
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
| `--generate` | Call the LLM and save finished content (needs `ANTHROPIC_API_KEY` + `pip install anthropic`). |
| `--model` | Override the LLM model id for `--generate`. |

## Configuration (`config.json`)

Brands, default audience, default word count, and the LLM model/token defaults live
in `config.json` - edit there, not in code. `config.py` loads it with a safe
fallback if the file is missing.

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
8. Every statistic is verified against a real, live source before publish (see below)

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

---

## Example Brands (`config.json`)

These ship as working examples in `config.json`'s `brands` map. Edit their fields,
delete them, or add a new domain entry with your own brand's name, description,
audience, and hashtag.

| Domain | Brand | Description |
|--------|-------|-------------|
| edstellar.com | Edstellar | Global corporate training company delivering high-impact training solutions for enterprise teams |
| invensislearning.com | Invensis Learning | Global professional training and certification provider across project management, IT service management, agile, and cybersecurity |
