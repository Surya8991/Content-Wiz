from ._shared import HUMAN_WRITING_RULES, RANKABILITY_RULES, RESEARCH_RULES  # noqa: F401


def medium_step1(topic, **_):
    return f"""You are a Medium content strategist who has built audiences from 0 to 100K+ followers across multiple Medium publications. You understand both Medium's curation algorithm and the platform's organic distribution mechanics through Boost, Featured, and topic pages.

TASK:
Generate 3 supporting article title ideas that form a content cluster around the main blog post: "{topic}"

PRE-WRITE DIAGNOSTIC:
1. What are the 3 distinct sub-topics or angles within "{topic}" that each deserve their own dedicated article?
2. What search query (Google or Medium) would a reader use to find each of these supporting articles?
3. Which sub-topic has the lowest competition but highest reader interest? (Mark this as the priority pick.)

MEDIUM CONTENT CLUSTER STRATEGY:
- A content cluster is 1 main pillar post + 3-5 supporting articles, all interlinked
- Each supporting article ranks for a distinct long-tail variation of the main topic's keywords
- Supporting articles drive internal traffic to the pillar via natural CTA links
- Together, they signal topical authority to Medium's algorithm AND to Google
- The best clusters cover the main topic from 3 different angles: a how-to angle, an insight/perspective angle, and a problem/mistake angle

TITLE REQUIREMENTS (apply to all 3):

STRUCTURE & FORMAT:
- 8-12 words per title (Medium's optimal range for both readability and SEO)
- Each of the 3 titles must use a DIFFERENT structural format from this list:
  * "How to [Specific Outcome] [Without/Despite Common Constraint]" - tactical how-to
  * "[Number] [Specific Things] That [Specific Audience] [Action]" - listicle
  * "Why [Common Belief] Is [Wrong/Misleading] (And What [Audience] Should Do Instead)" - contrarian insight
  * "The [Adjective] Mistake [Audience] Make When [Specific Activity]" - problem-focused
  * "What I Learned After [Specific Experience] About [Topic]" - narrative/personal
  * "[Outcome] in [Timeframe]: [Specific Method/Framework]" - case-study-style

SEO & SEARCH INTENT:
- Each title must reflect a real search query, ideally one that gets 100-1,000 monthly searches (the long-tail sweet spot for new Medium articles to rank)
- Include the primary keyword from "{topic}" naturally in the title where possible
- Avoid keyword stuffing - the title should read as something a human would write, not an SEO bot

SPECIFICITY:
- Every title must pass the "could a stranger picture the article?" test
- Include at least one specific element per title:
  * A number ("5 Ways", "3 Mistakes", "The 7-Step Framework")
  * A named concept ("The 80/20 Rule", "OKR Framework", "Manager Tax")
  * A specific outcome ("Reduce Turnover", "Double Engagement", "Cut Onboarding Time")
  * A specific timeframe ("in 90 Days", "Within Q1", "Before Your Next Review")

AUDIENCE FIT:
- Titles must immediately signal "this is for me" to professionals in the field of "{topic}"
- The reader should be able to predict whether the article is worth their time from the title alone

NO-GO LIST:
- No clickbait ("You Won't Believe...", "This One Trick...", "Shocking Truth...")
- No vague titles ("Thoughts on Leadership", "About Employee Engagement")
- No titles that could apply to any topic ("Why It Matters", "The Future of Work")
- No "ultimate guide" or "comprehensive" titles - Medium readers prefer specific, narrow promises

MEDIUM-SPECIFIC TITLE NOTES:
- Subtitle is the second deliverable - Medium gives almost as much weight to the subtitle as the title
- Titles starting with a number consistently outperform on Medium (3-7% higher CTR)
- "How I" / "What I learned" titles work well for narrative-driven Medium readers
- Avoid colons over-stuffing the title (one colon max, e.g. "The Hidden Cost: How [X] Affects [Y]")

OUTPUT FORMAT (return exactly this):

---
Supporting Article 1:
Title: [Full title - 8-12 words]
Subtitle: [Subtitle - 12-20 words, explains the specific value or angle]
Format: [How-To / Listicle / Contrarian / Problem-focused / Narrative / Case-study]
Distinct Angle: [One sentence - what specific sub-topic this covers and how it differs from the other 2]
Target Search Query: [The exact phrase a reader might Google or search on Medium]
Connection to Main Post: [One sentence - how this links back to "{topic}" and where the CTA fits naturally]
---

Supporting Article 2:
Title: [...]
Subtitle: [...]
Format: [...]
Distinct Angle: [...]
Target Search Query: [...]
Connection to Main Post: [...]
---

Supporting Article 3:
Title: [...]
Subtitle: [...]
Format: [...]
Distinct Angle: [...]
Target Search Query: [...]
Connection to Main Post: [...]
---

EDITOR'S RECOMMENDATION:
Pick the title with the strongest combination of low search competition + high audience relevance + clearest connection to the main post. Briefly explain in 2 lines why this is the priority pick.

(After reviewing, choose one title and run Step 2 with: --title "your chosen title")
"""


def medium_step2(topic, title, **_):
    return f"""You are a Medium writer whose articles routinely earn Boost selection, Featured status in major Medium publications (Better Programming, The Startup, Better Marketing), and consistent 5-minute+ average read times. You write for the Medium reader: someone who chose to be on a long-form platform and wants substance, not skim-bait.

TASK:
Write a 500-word Medium article on this title:
"{title}"

PILLAR CONTEXT:
This article is a supporting piece in a content cluster anchored by the main pillar post: "{topic}"
The article must:
- Stand alone as a valuable read (someone who never reads the pillar post should still get full value)
- Naturally lead curious readers to the pillar via a contextual CTA at the end
- Rank for its own long-tail search query

PRE-WRITE DIAGNOSTIC:
1. What is the ONE specific insight or takeaway a reader will remember 24 hours after reading? (Write the article around delivering this.)
2. What personal angle, named source, or specific data point will you anchor this article in? (Medium readers reject generic content - specificity is non-negotiable.)
3. What is the natural bridge from this article's specific topic to the pillar post's broader topic? (The CTA must feel like a logical "and if you want to go deeper, here's where to look" rather than a hard pitch.)

MEDIUM PLATFORM CONTEXT:
- Medium's curation algorithm rewards: 5+ minute read times, high read-completion rates, clap-to-view ratios above 8%, and quality engagement (highlights, follows, comments)
- The first 3 paragraphs decide if a reader scrolls or bounces - Medium's "above the fold" matters
- Bolded text creates visual scan anchors - readers who scan are more likely to clap and follow
- Medium highlights (the yellow text-highlighting feature) are a strong engagement signal - write at least 2-3 sentences that beg to be highlighted (clean, quotable insights)
- Pull quotes, blockquotes, and short standalone lines extend dwell time

ARTICLE STRUCTURE (follow exactly):

TITLE & SUBTITLE (Medium-specific - both have algorithmic weight):
- TITLE (H1): "{title}"
- SUBTITLE: Write a 12-20 word subtitle that:
  * Adds specific value or angle not in the title
  * Includes a semantic keyword variation
  * Reads like a deck (newspaper-style sub-headline) - not a tagline

SECTION 1 - OPENING HOOK (70-90 words, 2-3 short paragraphs):
- Open with one of these patterns (NEVER start with "In today's world" or a dictionary definition):
  * Specific scenario: "It was [specific time/situation]. [Specific event happened]. That's when I realized..."
  * Surprising stat: "[Stat with named source] - and most {topic} professionals get it backwards."
  * Sharp observation: "The standard advice on [{title}'s topic] is wrong. Here's what works instead."
- Within the first 3 sentences, the reader must know:
  * What this article is about
  * Why it matters to them specifically
  * What they'll walk away knowing
- The opening must earn the scroll - if it sounds like every other Medium article, rewrite it

SECTION 2 - THE CONTEXT / WHY IT MATTERS (80-100 words):
- One key data point, industry finding, or named research that establishes the problem or opportunity
- Format: "According to [Named Organization]'s [Specific Report Name] (Year), [specific finding]."
- Briefly connect this context to why it matters specifically for "{title}"
- Avoid generic phrases like "studies show" or "research suggests" without naming the study

SECTION 3 - THE CORE INSIGHT (150-180 words, the substance):
- Deliver the central argument, framework, or practical advice the article's title promises
- Use 2-3 short paragraphs OR a tight numbered list (Medium renders both well)
- Required elements:
  * One specific named example, brief case study, or "I worked with..." anecdote
  * At least one bolded sentence that summarizes the article's core insight in a quotable way (highlight bait)
  * Concrete advice that passes the specificity test (not "communicate better" but "send a 2-sentence written summary within 2 hours of every verbal decision")
- Use a sub-heading (H2 in Medium) to label this section with a benefit-driven phrase, not "Main Body"

SECTION 4 - THE NUANCE OR COMMON MISTAKE (80-100 words):
- One reinforcing point, common pitfall, or deeper layer that strengthens the core insight
- Format options:
  * "But there's a catch..." pattern
  * "What most people get wrong about [insight]..." pattern
  * "The mistake I see most often..." pattern
- Connect back to the reader's professional context

SECTION 5 - CONCLUSION + PILLAR CTA (60-80 words):
- One sentence that distills the entire article into a single takeaway (the line readers will share)
- Natural transition to the pillar post:
  * "If you want the full breakdown on [main topic from {topic}], [INSERT CTA LINK] walks through [specific element of the pillar post] in detail."
  * The CTA anchor text must include a relevant keyword from the pillar topic
- Closing question that invites a specific comment, not generic feedback:
  * Bad:  "What do you think?"
  * Good: "Which of these patterns shows up most in your work?"

MEDIUM FORMATTING SPECIFICS (HTML output - do not use markdown):
- <h1> for the article title only; <h2> for 1-2 main section breaks; <h3> for sub-points if needed
- <strong> for important phrases sparingly - 3-5 instances max across the whole article
- <em> for emphasis on specific terms or named concepts
- <blockquote> for the central insight of the article (the "highlight-bait" line)
- <hr> before the conclusion if the article exceeds 600 words
- <a href="URL">anchor text</a> for all hyperlinks

WRITING STANDARDS:
{HUMAN_WRITING_RULES}

{RANKABILITY_RULES}

{RESEARCH_RULES}

GRAMMAR & VOICE CHECKLIST (review before output):
- Every sentence has a clear subject and verb
- No comma splices, run-on sentences, or tense shifts
- Consistent tense throughout (present tense preferred for Medium's narrative voice)
- Paragraph breaks feel natural - 1-3 sentences per paragraph max
- Read the full article aloud - rewrite anything that sounds like a corporate broadcast
- The voice should feel like a senior peer sharing a hard-won insight, not an article

MEDIUM TAGS RECOMMENDATION:
After the article, suggest 5 tags optimized for Medium discoverability:
- 1 broad tag (Leadership, Business, Productivity)
- 2-3 mid-tier tags (specific to {topic})
- 1 niche tag (hyper-specific to this article's angle)

SELF-REVIEW:
- Title + subtitle: do they earn the click without overpromising?
- First 3 sentences: would a Medium reader scroll past or commit to reading?
- Highlight test: are there at least 2-3 sentences that someone would highlight in yellow?
- CTA test: does the link to the pillar feel like a useful next step or a sales pitch?
- Read time check: at 500 words, the article should feel substantive without padding

OUTPUT:
Return a complete, self-contained HTML file ready to open in a browser and paste into Medium's editor. Structure:
1. <!DOCTYPE html> declaration with <html>, <head> (including <meta charset="UTF-8"> and <title>), and <body> tags
2. <h1> for the article headline
3. <p><em>Subtitle</em></p> directly below the headline
4. Full article body using <h2>, <p>, <strong>, <em>, <blockquote>, <hr>, and <a href> as appropriate
5. After <hr> at the end, output three lines:
   MEDIUM TAGS: [5 comma-separated tags]
   ESTIMATED READ TIME: [X min read, calculated at 200 wpm]
   SUGGESTED SUBTITLE: [under 120 characters]

File naming convention: Article_[Number]_[Short-Slug].html
Save to: output/Medium/
Do not output markdown. HTML only. No meta-commentary, no explanations, no preamble.
"""


def blog_suggestion(topic, platform, **_):
    return f"""You are a senior content strategist who has built editorial calendars that drove 7-figure organic traffic at multiple B2B brands. You combine SEO research, audience signal mining, and SERP gap analysis to identify the topics that will actually rank and convert.

TASK:
Generate 10 high-potential blog topic ideas for the following brief:

Publishing Platform: {platform}
Target Niche / Audience: {topic}

PRE-RESEARCH DIAGNOSTIC (do this mentally before generating titles):
1. What is the primary search ecosystem for this niche - Google, YouTube, Medium, Reddit, LinkedIn? (This affects topic angle and structure.)
2. What are the 3-4 evergreen pain points that the target audience consistently faces in this niche?
3. What 2-3 trends or shifts have happened in this niche in the last 12-18 months that create timely opportunities?

RESEARCH METHODOLOGY (apply to each idea):

Layer 1 - SEARCH DEMAND:
- What specific search query does this title target?
- Estimated monthly search volume tier: low (<500), medium (500-5,000), high (5,000+)
- Keyword competition tier: low (under-served), medium (competitive but winnable), high (dominated)

Layer 2 - SERP GAP ANALYSIS:
- What does the current first-page Google result look like for this query?
- What's MISSING from the existing top results - depth, recency, format, audience-specific framing?
- Why would a new article on this topic have a chance to outrank or differentiate?

Layer 3 - AUDIENCE SIGNAL:
- Where is this topic being discussed organically - LinkedIn comments, Reddit threads, niche newsletters, podcasts?
- What specific question or frustration are people raising that current content doesn't answer well?

Layer 4 - PUBLISHING PLATFORM FIT:
- Does this topic fit {platform}'s tone and reader expectations?
- For Medium: narrative-friendly, opinion-driven, personal-experience-friendly
- For LinkedIn: professional, insight-driven, data-friendly
- For WordPress/Company Blog: SEO-heavy, solution-oriented, branded
- For Dev.to/Hashnode: technical depth, code/tool-driven, peer-to-peer
- For Newsletter: timely, conversational, useful

CONTENT TYPE DISTRIBUTION (across the 10 ideas):
Include at minimum:
- 2 LISTICLES ("X Ways to...", "X Best...")
- 2 HOW-TO GUIDES ("How to..." with specific outcomes)
- 1 THOUGHT LEADERSHIP / OPINION piece (a contrarian or perspective-driven take)
- 1 DATA-DRIVEN / RESEARCH-BACKED piece (built around stats or original analysis)
- 1 COMMON-MISTAKES piece ("X Mistakes...", "Why You're [Failing] At [X]")
- 1 COMPARISON / VS piece ("X vs. Y", "When to Use X Over Y")
- 1 CASE STUDY / NARRATIVE piece ("How [Company/Person] Did [Specific Outcome]")
- 1 of your strongest format choice

TITLE QUALITY REQUIREMENTS:
- Specificity test: a stranger should be able to picture the exact article from the title alone
- SEO-friendly without keyword stuffing - the title reads as something a human would write
- Each title 8-14 words (the optimal range for both readability and SERP display)
- Numbers, named concepts, or specific outcomes should appear in at least 7 of the 10 titles
- Avoid: "ultimate guide", "complete guide", "everything you need to know", "the future of"
- The title should immediately signal value to a {topic} professional

EVERGREEN VS TIMELY MIX:
- 6-7 ideas should be evergreen (long-term SEO traffic potential)
- 3-4 ideas should be timely (capitalize on current trends or recent shifts)
- Mark each idea clearly

OUTPUT FORMAT (return exactly this structure for each of the 10):

═══════════════════════════════════════════
IDEA #[Number]
═══════════════════════════════════════════
Title: [Full article title - 8-14 words, specific, SEO-friendly]
Subtitle / Deck: [Optional 1-line subtitle that adds context, 12-20 words]
Type: [Listicle / How-To / Thought Leadership / Data-Driven / Common-Mistakes / Comparison / Case Study]
Primary Search Query: [The exact phrase a reader would Google to find this]
Estimated Search Volume: [Low / Medium / High]
Keyword Difficulty: [Low / Medium / High]
Evergreen or Timely: [Evergreen / Timely / Both]

Distinct Angle (1 sentence):
[What makes this piece unique - what specific pain point, curiosity, or under-served insight it addresses]

SERP Gap (1 sentence):
[What's missing from current top-ranking content for this query, and why this article can win]

Why It Will Rank (1 sentence):
[The specific search intent, audience match, and content gap this title exploits]

Suggested Section Outline (3-5 H2-level subheadings):
- [Subheading 1]
- [Subheading 2]
- [Subheading 3]
- [Subheading 4]

Estimated Word Count: [recommended range - e.g. 1,200-1,500 words]
═══════════════════════════════════════════

[Repeat for all 10 ideas]

EDITOR'S TOP 3 PICKS:
After all 10 ideas, identify the 3 with the strongest combination of:
- Search demand
- Low-to-medium competition
- Clear audience-specific angle
- High conversion potential (relevant CTA opportunity)

Format:
1. [Title] - [One-sentence reason this is a top priority]
2. [Title] - [One-sentence reason]
3. [Title] - [One-sentence reason]

CONTENT CLUSTER OPPORTUNITIES:
After the Top 3, identify any 2-3 ideas from the list that could form a content cluster (one pillar + supporting articles) for stronger topical authority. List which would be the pillar and which would be supporting pieces.
"""


def blog_writing(topic, wordcount, platform, audience, **_):
    return f"""You are a senior B2B writer and SEO strategist whose articles regularly rank in Google's top 3 positions for high-intent commercial queries. You write content that satisfies both Google's E-E-A-T quality signals and the human reader's need for substance over fluff.

ASSIGNMENT:
Write a complete, publish-ready blog article that can rank on Google page 1 and convert {audience} readers into engaged followers.

---
ARTICLE BRIEF:
- Title/Topic: {topic}
- Target Word Count: {wordcount}+ words (hit this minimum, do not pad with filler)
- Target Audience: {audience}
- Publishing Platform: {platform}
- Primary Goal: Rank on Google page 1 + deliver genuine expert-level value to {audience}
---

PRE-WRITE DIAGNOSTIC (do this mentally before writing):
1. SEARCH INTENT: What is the user actually trying to accomplish when they search this topic? (Informational, navigational, commercial, transactional?)
2. SERP REALITY: What does Google currently rank on page 1 for this topic? What format dominates - listicles, ultimate guides, comparison posts, video?
3. CONTENT GAP: What is missing or under-served in the current top results? Where can this article be 10x better?
4. E-E-A-T SIGNALS: What experience, expertise, or authority can be demonstrated in this article? (Real cases, named experts, specific data, lived experience.)
5. CONVERSION PATH: After reading, what specific action should {audience} take? The CTA must align with the search intent.

E-E-A-T QUALITY SIGNALS (Google's 2025 ranking framework - bake these into the article):
- EXPERIENCE: First-hand, real-world examples - "I worked with...", "After auditing 50+...", "When we ran this experiment..."
- EXPERTISE: Demonstrated subject knowledge through specific, accurate, niche details
- AUTHORITATIVENESS: Citations to recognized industry sources, named experts, official reports
- TRUSTWORTHINESS: Transparent sourcing, balanced perspectives, accurate data, no vague claims

ARTICLE STRUCTURE (follow this exactly, section by section):

═══════════════════════════════════════════
SECTION 1 - METADATA PACKAGE (write before the article body)
═══════════════════════════════════════════

H1 TITLE (the article's main heading):
- 55-65 characters
- Primary keyword in the first 60% of the title
- Specific, benefit-driven, no clickbait
- Front-load the most important word or number

META DESCRIPTION:
- 150-158 characters (with spaces)
- Includes primary keyword naturally
- Contains one implicit or explicit CTA verb ("Learn", "See", "Get", "Find out")
- Reads as a standalone summary - someone seeing only this should understand the article's value

KEYWORD MAP:
- Primary keyword: [The single phrase to optimize for]
- Secondary keywords (4-6): [Semantic variations to use 2-3 times each]
- Long-tail variations (2-3): [Specific phrases that capture related search intent]
- People Also Ask questions to address: [3-4 PAA questions this article should answer]

SUGGESTED SLUG: [Short URL-friendly version, e.g. "factors-affecting-business-credit"]

═══════════════════════════════════════════
SECTION 2 - OPENING HOOK (150-200 words)
═══════════════════════════════════════════
Open with one of these proven patterns (NEVER open with a question or "In today's fast-paced world"):

Pattern A - Specific stat with stakes:
"[Stat with named source]. For [audience], that means [specific consequence]."

Pattern B - Vivid relatable scenario:
"[Specific scenario in 2-3 sentences]. If you've been there, you already know [insight]."

Pattern C - Counterintuitive claim:
"Most {audience} believe [common assumption]. The data and the experience of [specific group] tell a different story."

Within the first paragraph (3-4 sentences), explicitly state:
- What this article covers
- Who it's for (call out {audience} by name)
- What they'll know or be able to do after reading

This section must make a {audience} professional think: "This is exactly what I needed."

═══════════════════════════════════════════
SECTION 3 - WHY THIS MATTERS / CONTEXT (150-200 words)
═══════════════════════════════════════════
- Establish the current landscape or problem with 1-2 real data points
- Format: "According to [Named Organization]'s [Specific Report Name] (Year), [specific finding]."
- Cite at least one source from the priority research tier (peer-reviewed > industry reports > reputable journalism)
- Briefly frame the gap between common practice and what actually works
- This section earns the trust of the reader - no fluff, every sentence must add information

═══════════════════════════════════════════
SECTION 4 - MAIN BODY (target {max(wordcount - 700, 500)}+ words)
═══════════════════════════════════════════
The substance of the article. Break into 4-6 H2 subsections.

Subheading rules (these matter for SEO and skim-readability):
- Each H2 must be a benefit, a specific question (matches PAA queries), or a named concept
- Avoid vague headings: "Introduction", "Background", "Conclusion"
- Include the primary keyword in 1-2 H2s naturally (not all - looks spammy)
- Use H3s within long H2 sections for further breakdown

Required content distribution across the main body:
- At least one H2 section addresses a common misconception or mistake in this niche
- At least one H2 section provides a numbered framework, checklist, or step-by-step (this is the section readers screenshot)
- At least one H2 section includes a comparison, table, or "X vs Y" element where relevant
- At least one section has an actionable framework readers can implement immediately
- Use bullet points or numbered lists when listing 3+ items - format for skimming
- Bold key phrases sparingly (3-5 across the entire main body) - over-bolding signals AI writing

Featured snippet optimization:
- For at least one H2 that matches a question-style query, format the answer as a 40-60 word direct response immediately under the heading (Google's featured snippet sweet spot)
- Use ordered/unordered lists for "how to" or "best of" subsections - Google often pulls these into snippets

Each subsection should include at least ONE of:
- A real, attributable stat with named source and year
- A specific named example (real company, real person, real case)
- A step-by-step instruction with concrete details
- A direct quote from a credible expert with attribution

═══════════════════════════════════════════
SECTION 5 - REAL-WORLD EXAMPLE / CASE STUDY (120-180 words)
═══════════════════════════════════════════
- Use a real, publicly known company, team, or individual where possible
- Format:
  * The situation (what they faced)
  * What they did (specific actions)
  * The outcome (specific, quantified result with timeframe)
- If a real case is unavailable, present a clearly labeled "Illustrative scenario" that reflects real-world patterns - never fabricate a fake case study
- This section adds Experience and Trust signals to the article's E-E-A-T profile

═══════════════════════════════════════════
SECTION 6 - ACTIONABLE TAKEAWAYS (120-180 words)
═══════════════════════════════════════════
- 4-6 specific, concrete next steps the reader can take this week (not generic advice)
- Format as a numbered list
- Each takeaway must:
  * Be specific enough to act on without needing more info
  * Include a "do this" verb at the start
  * Reference a specific timeframe, tool, or measurable threshold where relevant

Example of a good takeaway:
"1. Within 7 days, audit your team's last 5 verbal decisions - did each have a written 2-sentence summary sent within 2 hours? If not, implement the rule starting tomorrow."

Example of a bad takeaway:
"1. Improve communication with your team."

═══════════════════════════════════════════
SECTION 7 - FAQ SECTION (optional but recommended for SEO, 150-250 words)
═══════════════════════════════════════════
If the topic supports it, add an FAQ section addressing 3-5 of the "People Also Ask" questions identified earlier.
- Each Q-A pair: question on its own line (H3), answer in 40-60 words
- Format answers for featured snippet capture: direct response in the first sentence, supporting context after
- Note: this section can be wrapped in FAQPage schema for rich snippets

═══════════════════════════════════════════
SECTION 8 - CONCLUSION + CTA (100-150 words)
═══════════════════════════════════════════
- Open with a one-paragraph summary that reinforces the single most important idea (not a recap of every section)
- NEVER open the conclusion with: "In conclusion", "To summarize", "Wrapping up", "In summary"
- Natural link to related content: weave [INSERT CTA LINK] into a sentence with anchor text that is a relevant keyword from the topic, NOT "click here" or "learn more"
- Close with one specific question that invites a substantive comment, not generic feedback
  Bad:  "What do you think?"
  Good: "Which of these mistakes shows up most often in your work?"

═══════════════════════════════════════════
SECTION 9 - INTERNAL LINKING MAP
═══════════════════════════════════════════
After the article body, list 3-5 internal linking opportunities:
- Suggested anchor text + the type of related article it should link to
- Format: "Anchor text: [phrase]" → Suggested target: [topic of related article]"
- These help Google understand topical clusters and pass authority

═══════════════════════════════════════════
SECTION 10 - SOURCES & FURTHER READING
═══════════════════════════════════════════
- List every named source cited in the article in proper format
- Format: "[Source/Report Name] ([Year]) - [Publishing Organization]"
- Group by type: Industry Reports, Academic Sources, Books, Articles
- Optional: 2-3 "Further Reading" recommendations the reader might explore

═══════════════════════════════════════════
SECTION 11 - SCHEMA MARKUP (JSON-LD)
═══════════════════════════════════════════
Generate the actual JSON-LD schema markup for this article, ready to paste into the page. Pick the schema type(s) that apply:
- Article schema (always required)
- FAQPage schema (if an FAQ section is included)
- HowTo schema (if the article includes step-by-step instructions)
- Review/Product schema (if comparing products/services)

Output a real, populated `<script type="application/ld+json">...</script>` code block (or one block per schema type if more than one applies), filled in with the article's actual title, description, author/publisher placeholders, and structure (e.g. FAQPage mainEntity list matching the real FAQ questions/answers, HowTo step list matching the real steps). Do not output a prose recommendation instead of code - the code block itself is the deliverable.

---
WRITING STANDARDS:
{HUMAN_WRITING_RULES}

{RANKABILITY_RULES}

{RESEARCH_RULES}

---
PLATFORM-SPECIFIC NOTES FOR {platform.upper()}:
- LinkedIn Article: professional, insight-driven, shorter paragraphs, bold key takeaways, business-formal voice
- Medium: literary voice, personal narrative woven in, strong story arc, italics for emphasis
- WordPress / Company Blog: brand-authoritative, solution-focused, SEO-heavy formatting, internal links
- Dev.to / Hashnode: technical precision, code blocks where relevant, peer-to-peer tone, Markdown formatting
- General Blog: balanced - readable, scannable, expert-but-approachable

Format the article in the appropriate markup for {platform} (Markdown for Dev.to/Hashnode/Medium, standard HTML-friendly headings for WordPress/LinkedIn).

---
FINAL QUALITY GATE (verify every item before outputting):
- [ ] Word count meets or exceeds {wordcount}
- [ ] Primary keyword appears in: H1 title, meta description, first 100 words, at least 2 H2 subheadings, the conclusion, and 3-5 times naturally throughout
- [ ] Total keyword density: 0.8% - 1.5% (never above 2%)
- [ ] At least 3 named sources cited (organization, report name, year)
- [ ] At least 1 real or clearly-labeled illustrative case study included
- [ ] At least 1 numbered framework or step-by-step that readers can act on
- [ ] No AI-signature phrases present (re-read the banned phrases list)
- [ ] Every paragraph passes the "so what?" test - if it doesn't add value, cut it
- [ ] Read aloud - rewrite any sentence that sounds robotic
- [ ] CTA placeholder [INSERT CTA LINK] is present
- [ ] Sources, internal linking map, and schema JSON-LD code block included
- [ ] Featured snippet formatting applied to at least one Q&A-style section

OUTPUT:
Return the complete, publish-ready article in this exact order:
1. Metadata Package (title, meta description, keyword map, slug)
2. Full article body with all H2 sections
3. Internal Linking Map
4. Sources & Further Reading
5. Schema Markup JSON-LD code block(s), populated with this article's actual title, description, and structure

No commentary, no explanations, no "here is your article" preamble.
"""


def blog_writing_md(topic, wordcount, platform, audience, **_):
    frontmatter = f"""---
title: {topic}
tags: []
canonical_url:
cover_image:
description:
---

FRONTMATTER INSTRUCTIONS:
- canonical_url: if this article is being cross-posted from another platform (e.g. it originally ran on the company blog, Medium, or another Dev.to/Hashnode account), set this field to that original article's URL. If this is the first and only publication of this piece, leave the field empty - do not fabricate or guess a URL.

"""
    return frontmatter + blog_writing(topic, wordcount, platform, audience)


# ─────────────────────────────────────────────
# NEW PLATFORM TEMPLATES
# ─────────────────────────────────────────────
