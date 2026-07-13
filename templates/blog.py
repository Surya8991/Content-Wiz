from ._shared import (
    BANNED_CTA_PHRASES,
    HUMAN_WRITING_RULES,
    RANKABILITY_RULES,
    RESEARCH_RULES,
    market_voice,
)

_BANNED_CTA_LIST = ", ".join(f'"{p}"' for p in BANNED_CTA_PHRASES)


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
    # Section-length guidance scales proportionally with the requested wordcount
    # instead of using fixed absolute floors, so a shorter request (e.g. 800
    # words) isn't silently forced past its target by section minimums that
    # summed to 1,290+ words regardless of what was asked for.
    opening_lo, opening_hi = max(round(wordcount * 0.13), 60), max(round(wordcount * 0.18), 90)
    context_lo, context_hi = max(round(wordcount * 0.10), 50), max(round(wordcount * 0.14), 80)
    body_target = max(round(wordcount * 0.40), 300)
    case_lo, case_hi = max(round(wordcount * 0.09), 50), max(round(wordcount * 0.13), 80)
    takeaways_lo, takeaways_hi = max(round(wordcount * 0.09), 50), max(round(wordcount * 0.13), 80)
    faq_lo, faq_hi = max(round(wordcount * 0.08), 50), max(round(wordcount * 0.12), 80)
    conclusion_lo, conclusion_hi = max(round(wordcount * 0.06), 40), max(round(wordcount * 0.09), 60)
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
- 150-158 characters (with spaces) - the tighter bound protects against search-result truncation
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
SECTION 2 - OPENING HOOK ({opening_lo}-{opening_hi} words)
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
SECTION 3 - WHY THIS MATTERS / CONTEXT ({context_lo}-{context_hi} words)
═══════════════════════════════════════════
- Establish the current landscape or problem with 1-2 real data points
- Format: "According to [Named Organization]'s [Specific Report Name] (Year), [specific finding]."
- Cite at least one source from the priority research tier (peer-reviewed > industry reports > reputable journalism)
- Briefly frame the gap between common practice and what actually works
- This section earns the trust of the reader - no fluff, every sentence must add information

═══════════════════════════════════════════
SECTION 4 - MAIN BODY (target {body_target}+ words)
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
SECTION 5 - REAL-WORLD EXAMPLE / CASE STUDY ({case_lo}-{case_hi} words)
═══════════════════════════════════════════
- Use a real, publicly known company, team, or individual where possible
- Format:
  * The situation (what they faced)
  * What they did (specific actions)
  * The outcome (specific, quantified result with timeframe)
- If a real case is unavailable, present a clearly labeled "Illustrative scenario" that reflects real-world patterns - never fabricate a fake case study
- This section adds Experience and Trust signals to the article's E-E-A-T profile

═══════════════════════════════════════════
SECTION 6 - ACTIONABLE TAKEAWAYS ({takeaways_lo}-{takeaways_hi} words)
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
SECTION 7 - FAQ SECTION (optional but recommended for SEO, {faq_lo}-{faq_hi} words)
═══════════════════════════════════════════
If the topic supports it, add an FAQ section addressing 3-5 of the "People Also Ask" questions identified earlier.
- Each Q-A pair: question on its own line (H3), answer in 40-60 words
- Format answers for featured snippet capture: direct response in the first sentence, supporting context after
- Note: this section can be wrapped in FAQPage schema for rich snippets

═══════════════════════════════════════════
SECTION 8 - CONCLUSION + CTA ({conclusion_lo}-{conclusion_hi} words)
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

RELATED ARTICLES (in-body companion links):
- Wherever the article body references a companion piece by name (e.g. "a companion piece on...", "we covered this in..."), do not leave it as plain text - mark it as `[LINK: <exact companion piece title>]` immediately after the reference
- Do not fabricate a URL. Real published URLs don't exist until publish time, so the bracketed placeholder is the deliverable - a human or tracker-driven pass finds and replaces `[LINK: ...]` with the live URL once the companion piece is published
- If no companion piece exists yet for this topic, skip this instruction entirely rather than inventing one

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
- description: required, never leave this field blank. Write a single-sentence meta description that is 150-158 characters including spaces, includes the primary keyword naturally, and reads as a standalone summary of the article's value.

"""
    return frontmatter + blog_writing(topic, wordcount, platform, audience)


# ─────────────────────────────────────────────
# NEW PLATFORM TEMPLATES
# ─────────────────────────────────────────────


def comparison_page(topic, wordcount, platform, audience, market=None, **_):
    # topic is expected in the form "X vs Y" (or "best alternatives to X") -
    # a competitor-comparison SEO page. Section-length guidance scales
    # proportionally with the requested wordcount (default sensible range:
    # 800-1500 words), with small max() floors per section so very low
    # wordcounts still get workable sections. The floors can push the section
    # ranges past a very small requested wordcount, which is acceptable here
    # because the page brief states {wordcount}+ as a minimum, not an exact
    # target.
    intro_lo, intro_hi = max(round(wordcount * 0.10), 40), max(round(wordcount * 0.14), 60)
    criteria_lo, criteria_hi = max(round(wordcount * 0.24), 120), max(round(wordcount * 0.30), 160)
    when_x_lo, when_x_hi = max(round(wordcount * 0.13), 50), max(round(wordcount * 0.17), 70)
    when_y_lo, when_y_hi = max(round(wordcount * 0.13), 50), max(round(wordcount * 0.17), 70)
    decision_lo, decision_hi = max(round(wordcount * 0.10), 40), max(round(wordcount * 0.14), 60)
    faq_lo, faq_hi = max(round(wordcount * 0.08), 40), max(round(wordcount * 0.12), 60)

    frontmatter = f"""---
title: {topic}
tags: []
canonical_url:
cover_image:
description:
---

FRONTMATTER INSTRUCTIONS:
- canonical_url: REQUIRED and must be populated (unlike a syndicated blog post, a comparison/alternatives page is a bottom-funnel SEO asset that lives at one canonical location on the brand's own site). Set this to the page's own intended URL (e.g. "https://[brand-domain]/compare/[slug]" or "https://[brand-domain]/alternatives/[slug]"), using a slug derived from "{topic}". Do not leave this field empty and do not point it at a competitor's domain.
- description: required, never leave this field blank. Write a single-sentence meta description that is 150-158 characters including spaces, states the comparison plainly, and includes the primary keyword naturally.

"""

    body = f"""You are a senior B2B content strategist and competitive-analysis writer who builds comparison and alternatives pages that rank on Google page 1 for high-intent "vs" and "alternatives to" queries, without ever crossing into misleading or legally risky claims about a named competitor.

ASSIGNMENT:
Write a complete, publish-ready comparison page that helps {audience} readers make a confident, well-informed decision between the options named in "{topic}".

---
PAGE BRIEF:
- Title/Topic: {topic}
- Target Word Count: {wordcount}+ words (hit this minimum, do not pad with filler)
- Target Audience: {audience}
- Publishing Platform: {platform}
- Primary Goal: Rank for high-intent comparison/alternatives search queries and help {audience} readers self-select the right option with a credible, non-biased breakdown
---

{market_voice(market)}

HARD FABRICATION GUARDRAIL (read this before writing a single word - this is the single highest legal and reputational risk section in this entire content system):
- This page names a real competitor. Never invent specific pricing figures, specific feature claims, specific customer/user counts, specific integrations, or specific certifications for that competitor unless the topic or supplied inputs explicitly state them.
- A plausible-sounding guess is not an acceptable substitute for a fact you do not have. Guessing a competitor's price tier, feature list, or customer base is competitor disparagement and false-advertising exposure, not a style choice - treat it as a hard constraint, not a preference.
- Whenever a concrete fact about the named competitor is not known with certainty, write a clearly-marked placeholder instead of a guess, in this exact format: `[VERIFY: <specific fact needed, e.g. competitor's current published pricing tier>]`. Do this every time, not just once.
- This guardrail applies to the comparison table, the prose sections, and the schema markup equally - a placeholder in the prose but a fabricated number in the JSON-LD is still a fabrication.
- It is acceptable and expected to describe the competitor's category-level positioning (e.g. "typically positioned for enterprise-scale deployments") when that is genuinely known or reasonably inferable from public category norms - the guardrail is about specific, checkable facts, not about refusing to describe the competitor at all.

FAIRNESS & CREDIBILITY MANDATE (a comparison page that only trashes the competitor reads as biased and gets ignored or reported):
- No disparaging adjectives about the competitor ("clunky", "outdated", "overpriced", "inferior") unless directly and neutrally sourced to a specific, cited fact.
- No absolute claims: never write "the only real choice", "no real alternative", "objectively better", or similar. A reader who senses a thumb on the scale stops trusting the whole page.
- Give the competitor genuine credit where it is due - a fair page names real scenarios where the competitor is the better fit. This is what makes the "when the competitor makes sense" section credible rather than a token gesture.
- Frame differences as fit-for-purpose tradeoffs (team size, budget stage, deployment complexity, support model) rather than as universal superiority claims.
- The brand can and should state its own genuine differentiators plainly - fairness means accurate and balanced, not neutral-to-the-point-of-uselessness.

PRE-WRITE DIAGNOSTIC (do this mentally before writing):
1. DECISION BEING MADE: What is the reader actually trying to decide - which tool to buy, whether to switch, which fits their team size/budget/maturity stage?
2. SEARCH INTENT: Is this a "vs" comparison (two named options, reader is choosing between them) or an "alternatives to X" page (reader is already unhappy with or has outgrown X, browsing options)? Write to match which one "{topic}" actually is.
3. REAL DECISION CRITERIA: What 4-6 criteria do buyers in this category actually weigh (features, pricing model, company-size fit, support/format, implementation effort, integrations)? Do not invent a criterion just to fill a row.
4. KNOWN VS UNKNOWN FACTS: Before writing the table, list mentally which competitor facts are actually supplied or verifiably known, versus which require a `[VERIFY: ...]` placeholder.
5. CONVERSION PATH: After reading, what should a reader who is a genuine fit for the brand's product do next? The CTA must feel earned by the honest comparison, not forced.

PAGE STRUCTURE (follow this exactly, section by section):

═══════════════════════════════════════════
SECTION 1 - METADATA PACKAGE (write before the page body)
═══════════════════════════════════════════

H1 TITLE:
- 55-65 characters, states the comparison plainly (e.g. "[Option A] vs [Option B]: Which Fits Your Team")
- Primary comparison keyword in the first 60% of the title
- No clickbait, no absolute-winner framing in the title itself

META DESCRIPTION:
- 150-158 characters (with spaces)
- States the comparison plainly and includes an implicit CTA verb ("Compare", "See", "Find out")

KEYWORD MAP:
- Primary keyword: [the exact "X vs Y" or "alternatives to X" phrase from "{topic}"]
- Secondary keywords (3-5): [semantic variations, e.g. "X alternative", "X vs Y pricing", "X vs Y for [audience]"]
- People Also Ask questions to address: [3-4 PAA-style questions a buyer comparing these options would ask]

SUGGESTED SLUG: [short URL-friendly version, e.g. "x-vs-y" or "x-alternatives"]

═══════════════════════════════════════════
SECTION 2 - INTRO: FRAMING THE DECISION ({intro_lo}-{intro_hi} words)
═══════════════════════════════════════════
- Open by naming the exact decision the reader is trying to make - not a generic category overview
- State plainly, in the first 2-3 sentences, who this page is for and what it will help them decide
- Set expectations: this page gives an honest, criteria-based breakdown, not a one-sided pitch
- Call out {audience} directly so the reader immediately recognizes themselves
- NEVER open with "In today's fast-paced world" or a dictionary definition of either product's category

═══════════════════════════════════════════
SECTION 3 - COMPARISON TABLE & DECISION CRITERIA ({criteria_lo}-{criteria_hi} words)
═══════════════════════════════════════════
Render an actual Markdown comparison table (not a description of one) with a row for each of the following criteria, one column per option named in "{topic}":
- Core features / what it's built to do
- Pricing model (category-level only - e.g. "per-seat subscription" or "usage-based tiering" - never a fabricated specific dollar figure for the competitor unless supplied; use `[VERIFY: ...]` for anything not known)
- Best-fit company size / team maturity stage
- Primary use case / who reaches for this option first
- Support model and format (e.g. self-serve docs, dedicated onboarding, community support)
- Implementation effort / time-to-value

After the table, add 2-4 short paragraphs unpacking the criteria that most affect the decision for {audience} specifically - do not just repeat the table in prose.

═══════════════════════════════════════════
SECTION 4 - WHEN [OPTION A] MAKES SENSE ({when_x_lo}-{when_x_hi} words)
═══════════════════════════════════════════
- Describe the specific team profile, use case, or constraint where the first option named in "{topic}" is genuinely the better fit
- Be concrete: team size range, budget stage, technical maturity, or specific workflow need
- This section must read as a fair, standalone recommendation - not a setup for a "but actually" pivot

═══════════════════════════════════════════
SECTION 5 - WHEN [OPTION B] MAKES SENSE ({when_y_lo}-{when_y_hi} words)
═══════════════════════════════════════════
- Same treatment, mirrored, for the second option named in "{topic}"
- If "{topic}" is an "alternatives to X" page rather than a two-way "vs", treat this section as "when to look at alternatives at all" and name the specific signals that a team has outgrown or is a poor fit for the original option
- Give equal editorial weight and specificity to this section as Section 4 - an unequal word count or unequal level of detail between the two sides is itself a bias signal

═══════════════════════════════════════════
SECTION 6 - DECISION GUIDANCE ({decision_lo}-{decision_hi} words)
═══════════════════════════════════════════
- Do not declare a universal winner. Instead, give the reader a short decision framework: 3-4 concrete questions they can ask themselves ("Do you need X?", "Is your team under/over [size]?") that map to one option or the other
- Close with a specific next step for the reader who is a genuine fit for the brand's product, using [INSERT CTA LINK] with anchor text that is a relevant keyword from "{topic}" - never any phrase from this project's canonical banned-CTA list: {_BANNED_CTA_LIST}
- End with one specific question that invites a substantive comment, not generic feedback
  Bad:  "What do you think?"
  Good: "Which of these criteria matters most for your team right now?"

═══════════════════════════════════════════
SECTION 7 - FAQ SECTION ({faq_lo}-{faq_hi} words)
═══════════════════════════════════════════
Address 3-5 of the People Also Ask questions identified earlier, framed around the comparison itself (e.g. "Is [Option A] more expensive than [Option B]?", "Can I migrate from [Option A] to [Option B]?").
- Each Q-A pair: question on its own line (H3), answer in 40-60 words
- Any competitor-specific fact in an FAQ answer follows the same fabrication guardrail as the table - use `[VERIFY: ...]` rather than guessing
- Format answers for featured snippet capture: direct response in the first sentence, supporting context after

═══════════════════════════════════════════
SECTION 8 - INTERNAL LINKING MAP
═══════════════════════════════════════════
After the page body, list 2-4 internal linking opportunities:
- Format: "Anchor text: [phrase]" → Suggested target: [topic of related page]"

RELATED ARTICLES (in-body companion links):
- Wherever the page references a companion piece by name (e.g. "we cover pricing in more depth in..."), mark it as `[LINK: <exact companion piece title>]` immediately after the reference, matching this system's standard internal-linking placeholder convention
- Do not fabricate a URL. The bracketed placeholder is the deliverable - a human or tracker-driven pass finds and replaces `[LINK: ...]` with the live URL once the companion piece is published
- If no companion piece exists yet for this topic, skip this instruction entirely rather than inventing one

═══════════════════════════════════════════
SECTION 9 - SOURCES & FURTHER READING
═══════════════════════════════════════════
- List every named source cited for category-level stats or trend claims (never for the competitor's own specific facts - those follow the fabrication guardrail instead)
- Format: "[Source/Report Name] ([Year]) - [Publishing Organization]"

═══════════════════════════════════════════
SECTION 10 - SCHEMA MARKUP (JSON-LD)
═══════════════════════════════════════════
Generate the actual JSON-LD schema markup for this page, ready to paste into the page. Include:
- Product schema (or two Product blocks if directly comparing two named products) - populated with each product's real name and a neutral, factual description; leave any unknown `offers`/`aggregateRating` field out entirely rather than fabricating a price or rating
- FAQPage schema - mainEntity list matching the real FAQ questions/answers from Section 7

Output real, populated `<script type="application/ld+json">...</script>` code block(s), not a prose recommendation - the code block itself is the deliverable. Any field you do not have a real value for must be omitted from the JSON entirely (never filled with a placeholder number or a guess).

---
WRITING STANDARDS:
{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

Comparison-specific tone addendum (on top of the rules above):
- No em dashes anywhere in the output - use hyphens or restructure the sentence instead
- No disparaging adjectives about the named competitor and no absolute-winner language (see Fairness & Credibility Mandate above)
- Any category-level industry stat or trend used to frame the comparison (e.g. "the project management category grew X% in 2024") must follow the research/citation rules above - name the source and year

---
PLATFORM-SPECIFIC NOTES FOR {platform.upper()}:
- LinkedIn Article: professional, insight-driven, bold key differentiators, business-formal voice
- Medium: narrative framing of the decision, still criteria-driven, italics for emphasis
- WordPress / Company Blog: brand-authoritative, SEO-heavy formatting, internal links, this is the default home for a comparison/alternatives page
- Dev.to / Hashnode: technical precision on implementation/integration criteria, Markdown formatting
- General Blog: balanced, scannable, expert-but-approachable

Format the page in the appropriate markup for {platform} (Markdown for Dev.to/Hashnode/Medium, standard HTML-friendly headings for WordPress/LinkedIn).

---
SELF-CHECK (verify every item before outputting):
- [ ] Word count meets or exceeds {wordcount}
- [ ] canonical_url in the frontmatter is populated, not left empty
- [ ] Comparison table is an actual rendered table, not a description of one
- [ ] "When [Option A] makes sense" and "When [Option B] makes sense" sections are roughly equal in length and specificity
- [ ] No fabricated competitor facts were introduced anywhere (table, prose, or FAQ) - every specific competitor pricing, feature, or customer-count claim not supplied in the inputs is marked `[VERIFY: ...]`, not guessed
- [ ] No disparaging adjectives or absolute-winner language about the named competitor
- [ ] No em dashes anywhere in the output
- [ ] JSON-LD schema block(s) are real populated code, with any unknown competitor field omitted rather than fabricated
- [ ] [INSERT CTA LINK] placeholder is present in the Decision Guidance section
- [ ] Internal Linking Map and Sources sections are included

OUTPUT:
Return the complete, publish-ready comparison page in this exact order:
1. Metadata Package (title, meta description, keyword map, slug)
2. Full page body with all sections (Intro through FAQ)
3. Internal Linking Map
4. Sources & Further Reading
5. Schema Markup JSON-LD code block(s)

No commentary, no explanations, no "here is your page" preamble.
"""
    return frontmatter + body


def substack_post(topic, audience, wordcount=None, market=None, **_):
    # Substack is not a generic newsletter platform (growth.py's newsletter()
    # already covers that): its discovery mechanic runs through the Notes
    # feed and restacks rather than opens/clicks, and its monetization model
    # is a native free/paid-tier split inside a single post rather than a
    # separate paid product. Section-length guidance scales proportionally
    # with the requested wordcount, no fixed floors that ignore {wordcount}.
    # Default of 900 reflects a typical single-topic Substack post length
    # when the caller doesn't supply one.
    wc = wordcount or 900
    hook_lo, hook_hi = max(round(wc * 0.07), 40), max(round(wc * 0.10), 60)
    context_lo, context_hi = max(round(wc * 0.08), 50), max(round(wc * 0.12), 70)
    body_target = max(round(wc * 0.45), 250)
    paid_lo, paid_hi = max(round(wc * 0.10), 50), max(round(wc * 0.14), 70)
    closing_lo, closing_hi = max(round(wc * 0.10), 60), max(round(wc * 0.15), 90)

    return f"""You are a senior Substack writer who has grown multiple newsletters into thousands of paid subscribers by treating the Notes feed, restacks, and the free/paid split as distinct growth levers, not just a newsletter delivered by email.

TASK:
Write a complete, publish-ready Substack post on: "{topic}"

POST BRIEF:
- Topic: {topic}
- Target Word Count: {wc}+ words (hit this minimum, do not pad with filler)
- Target Audience/Readers: {audience}
- Primary Goal: earn opens from the email preview, earn restacks and replies in the Notes feed, and (if the topic supports it) convert free readers into paid subscribers at a natural split point
---

{market_voice(market)}

SUBSTACK PLATFORM MECHANICS (bake these into the structure, not just the prose):
- DISCOVERY IS TWO SURFACES, NOT ONE: readers find this post either in their email inbox (where the subject line and preview text decide the open) or in the Notes feed (Substack's 2026 Notes algorithm surfaces posts mainly through restacks and replies, not just from accounts a reader already follows). Write the hook so it works standing alone in both places.
- RESTACKS ARE THE GROWTH SIGNAL: a restack is Substack's native repost/share-with-commentary mechanic. A post that earns restacks reaches readers who have never subscribed. The closing must make restacking feel like an obvious, low-friction next action, not an afterthought.
- PAID TIER IS A SPLIT INSIDE ONE POST, NOT A SEPARATE PRODUCT: if this topic and the supplied inputs indicate the brand runs (or should run) a paid tier, the post can carry a free section followed by a "subscribe to read the rest" teaser above a paywall. Never assume monetization applies by default - only include the paid-tier split if the topic or audience signals paid content is part of this brand's model (e.g. topic mentions a paid offering, premium analysis, or the audience is described as existing subscribers/paying members). If there's no signal either way, write the post as fully free and skip the paid-tier section entirely rather than inventing a paywall.
- COMMENTS ARE THE ENGAGEMENT SIGNAL SUBSTACK'S ALGORITHM WEIGHTS: a specific, answerable closing question drives replies, and replies (like restacks) feed the same discovery loop.

PRE-WRITE DIAGNOSTIC (do this mentally before writing):
1. PREVIEW TEST: What is the exact line of text a reader sees in their email inbox preview and in the Notes feed before they click? Does it work with zero other context?
2. MONETIZATION SIGNAL: Does the topic or audience actually indicate a paid tier exists for this brand? If not, do not build a paywall into this post.
3. RESTACK HOOK: What single line or idea in this post is quotable enough that someone would restack it with their own one-line reaction attached?
4. REPLY BAIT: What specific, personal question can this post's readers actually answer from their own experience (not a generic "thoughts?")?

POST STRUCTURE (follow this exactly, section by section):

═══════════════════════════════════════════
SECTION 1 - METADATA PACKAGE (write before the post body)
═══════════════════════════════════════════
POST TITLE: specific, benefit-driven, no clickbait, works as a standalone line in an inbox
PREVIEW TEXT (the inbox preview snippet, 40-55 characters): a second hook that adds new information beyond the title, not a repeat of it
SEO TITLE / DESCRIPTION: a short title tag and a 150-158 character meta description for the post's own page and for search/AI-search surfaces
SUGGESTED TAGS (3-5): topical tags for Substack's own discovery surfaces

═══════════════════════════════════════════
SECTION 2 - HOOK: THE LINE READERS SEE FIRST ({hook_lo}-{hook_hi} words)
═══════════════════════════════════════════
- This is what a reader sees in the email preview AND what could be pulled into a Notes post promoting this piece - write it to survive being read completely out of context
- Open with a specific scenario, a named stat, or a sharp contrarian line - never "In today's fast-paced world" or a dictionary definition
- By the end of this section, the reader knows what the post covers and why it's worth their next 3 minutes

═══════════════════════════════════════════
SECTION 3 - WHY THIS MATTERS RIGHT NOW ({context_lo}-{context_hi} words)
═══════════════════════════════════════════
- One real data point or named observation that frames the stakes for {audience}
- If a stat is used, name the source and year per the research rules below
- Connect the frame directly to {audience}'s actual situation, not a generic industry statement

═══════════════════════════════════════════
SECTION 4 - FREE-TIER BODY (target {body_target}+ words)
═══════════════════════════════════════════
- Deliver the core substance: the argument, framework, or story the hook promised
- Use 2-4 subsections with clear subheadings
- Include at least one specific, named example or first-hand anecdote
- Include at least one line written to be highlighted or quoted on its own - this is the line most likely to get restacked
- This section must stand alone as valuable even for a reader who never sees a paid tier

═══════════════════════════════════════════
SECTION 5 - PAID-TIER SPLIT POINT (conditional, {paid_lo}-{paid_hi} words)
═══════════════════════════════════════════
Only include this section if Section "MONETIZATION SIGNAL" above concluded this brand runs a paid tier. If so:
- Write the free-to-paid transition as a genuine continuation of the argument, not an abrupt cutoff - the last free sentence should create real curiosity about what follows, not just announce a paywall
- Immediately before the paywall marker, insert this exact placeholder on its own line: [INSERT: paywall placement rationale - explain why this specific point in the argument is where free value ends and paid depth begins]
- Mark the actual split point with a `---` divider followed by "This next section is for paid subscribers." (or the brand's own equivalent phrasing) rather than fabricating Substack's literal paywall UI
- Describe the paid section's content by topic and value (e.g. "the full framework," "the specific numbers," "the step-by-step version") rather than writing the paid content itself if the assignment is for the free-tier teaser only
If there is no monetization signal, skip this section entirely and continue the free-tier body straight into the conclusion.

═══════════════════════════════════════════
SECTION 6 - CLOSING: RESTACK PROMPT + COMMENT QUESTION ({closing_lo}-{closing_hi} words)
═══════════════════════════════════════════
- One sentence that distills the whole post into a single line worth restacking
- A direct, low-friction ask for readers to restack this post if it was useful to someone in their own network - name the action ("restack this") rather than a vague "share if you liked it," and never use any phrase from this project's canonical banned-CTA list: {_BANNED_CTA_LIST}
- Close with one specific question that invites a substantive reply, not generic feedback
  Bad:  "What do you think?"
  Good: "What's the version of this you've actually run into at work?"

---
WRITING STANDARDS:
{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

Substack-specific tone addendum:
- No em dashes anywhere in the output - use hyphens or restructure the sentence instead
- Write like one identifiable writer talking to their readers, not a brand broadcasting - even a B2B-market post should read as authored by a person
- Subheadings inside the free-tier body should read like benefits or specific questions, never "Introduction" or "Body"

---
SELF-CHECK (verify every item before outputting):
- [ ] Word count meets or exceeds {wc}
- [ ] Hook works standalone as both an email preview line and a Notes-feed line
- [ ] Paid-tier section is present ONLY if the topic/audience genuinely signaled a paid tier - otherwise it is skipped entirely, not invented
- [ ] If included, the paid-tier section contains the exact `[INSERT: paywall placement rationale ...]` placeholder immediately before the split
- [ ] At least one line in the free-tier body is written to be quotable/restackable on its own
- [ ] Closing explicitly asks for a restack (not a generic "share this") and ends with a specific, answerable question
- [ ] No em dashes anywhere in the output
- [ ] No phrase from the banned-CTA list appears anywhere in the post

OUTPUT FORMAT:
Return the complete, publish-ready post in this exact order:
1. Metadata Package (post title, preview text, SEO title/description, tags)
2. Full post body (Hook through Closing, including the paid-tier split section only if applicable)

No commentary, no explanations, no "here is your post" preamble.
"""


def glossary_page(topic, audience, wordcount=None, market=None, **_):
    # A single SEO glossary/definition page for one term ({topic} is the
    # term itself), the programmatic-SEO play referenced in
    # strategies/strategy-seo-programmatic.md but not previously built as a
    # template. This is inherently short-form - a glossary entry, not an
    # article - so the default wordcount is modest (250) with proportional
    # scaling and no fixed floors that ignore {wordcount}. The max() floors
    # below can push the section total slightly past a very small requested
    # wordcount (e.g. under ~180 words), matching comparison_page's
    # documented, accepted tradeoff for keeping every section workable.
    wc = wordcount or 250
    definition_lo, definition_hi = max(round(wc * 0.08), 15), max(round(wc * 0.14), 25)
    practice_lo, practice_hi = max(round(wc * 0.35), 70), max(round(wc * 0.45), 100)
    why_lo, why_hi = max(round(wc * 0.30), 60), max(round(wc * 0.40), 90)

    frontmatter = f"""---
title: {topic}
tags: []
canonical_url:
cover_image:
description:
---

FRONTMATTER INSTRUCTIONS:
- canonical_url: REQUIRED and must be populated. A glossary/definition page is a permanent programmatic-SEO asset that lives at one canonical location on the brand's own site (e.g. a `/glossary/[slug]` path), not a syndicated piece. Set this to the page's own intended URL using a slug derived from "{topic}". Do not leave this field empty.
- description: required, never leave this field blank. Write a single-sentence meta description that is 150-158 characters including spaces, states the term's definition plainly, and includes the term itself naturally.

"""

    body = f"""You are a senior SEO content strategist who has built programmatic glossary pages that rank for definition-intent queries, get pulled into featured snippets, and get cited by other sites and by AI search systems as the reference definition for a term.

TASK:
Write a complete, publish-ready glossary/definition page for the single term: "{topic}"

PAGE BRIEF:
- Term: {topic}
- Target Word Count: {wc}+ words (this is a short-form definition page, not an article - hit this target without padding it into a full blog post)
- Target Audience: {audience}
- Primary Goal: answer the definition query directly before the reader scrolls, build topical authority for this term within the brand's glossary, and qualify for a DefinedTerm rich result
---

{market_voice(market)}

PRE-WRITE DIAGNOSTIC (do this mentally before writing):
1. EXACT QUERY: What is the precise search query this page answers (e.g. "what is {topic}", "{topic} definition", "{topic} meaning")?
2. ONE-SENTENCE TEST: Can this term be defined correctly in a single sentence that a reader could screenshot and trust on its own?
3. RELATED-TERM MAP: What 2-4 adjacent or parent/child terms does a reader researching "{topic}" also need to understand, and does this brand's glossary or content already cover any of them?
4. INTENT DEPTH: Is a reader looking this up purely to understand the word, or are they evaluating whether it applies to their own situation? Write the "in practice" section to match.

PAGE STRUCTURE (follow this exactly, section by section):

═══════════════════════════════════════════
SECTION 1 - DIRECT DEFINITION ({definition_lo}-{definition_hi} words)
═══════════════════════════════════════════
- One sentence, placed as the very first line of body content, that answers the query before the reader scrolls
- Format: "{topic} is [precise, plain-language definition]."
- No throat-clearing, no "In this article we'll explore" - the definition itself is the opening line
- This sentence must be able to stand alone as a featured-snippet answer and as the DefinedTerm schema's description value

═══════════════════════════════════════════
SECTION 2 - IN PRACTICE ({practice_lo}-{practice_hi} words)
═══════════════════════════════════════════
- Expand on the one-sentence definition: what this actually looks like when applied, who uses the term and in what context, and one concrete example
- Format as 1-2 short paragraphs, plain language over jargon
- If a specific stat, named framework, or named source is genuinely relevant, include it with attribution per the research rules below - do not force a stat in if none is genuinely relevant to a short definition page

═══════════════════════════════════════════
SECTION 3 - WHY IT MATTERS / RELATED CONCEPTS ({why_lo}-{why_hi} words)
═══════════════════════════════════════════
- One short paragraph on why this term matters to {audience} specifically (a decision it affects, a mistake it prevents, a process it's part of)
- Followed by 2-4 related or adjacent terms the reader likely needs next, each introduced with its own short phrase of context (not just a bare list of links)
- Wherever a related term is mentioned, mark it with this project's standard internal-linking placeholder convention: `[LINK: <exact related term or article title>]` immediately after the reference
- Do not fabricate a URL - the bracketed placeholder is the deliverable; a human or tracker-driven pass finds and replaces `[LINK: ...]` with the live URL once the related page is published
- If no related glossary entry or article exists yet for a given related term, still name the term but skip the `[LINK: ...]` marker for that one rather than inventing a target

═══════════════════════════════════════════
SECTION 4 - SCHEMA MARKUP (JSON-LD)
═══════════════════════════════════════════
Generate the actual JSON-LD schema markup for this page, ready to paste into the page. Required:
- A `DefinedTerm` block populated with this term's real name, the Section 1 one-sentence definition as `description`, and (if the page belongs to a broader glossary) an `inDefinedTermSet` reference to the glossary's own DefinedTermSet URL
- If this term is explicitly part of a named glossary collection the brand maintains, also output a minimal `DefinedTermSet` block for that collection (name + url); if no such collection is indicated, omit the DefinedTermSet block rather than inventing one

Output a real, populated `<script type="application/ld+json">...</script>` code block, not a prose description of the schema - the code block itself is the deliverable. Omit any field you do not have a real value for rather than filling it with a placeholder or a guess.

---
WRITING STANDARDS:
{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

Glossary-specific tone addendum:
- No em dashes anywhere in the output - use hyphens or restructure the sentence instead
- This is a reference page, not a narrative piece - keep sentences declarative and skimmable
- Never pad the "in practice" or "why it matters" sections with filler to hit the word count; if the term is genuinely simple, a shorter page that stays accurate outranks a padded one

---
SELF-CHECK (verify every item before outputting):
- [ ] The very first line of body content is a single, direct, screenshot-able definition sentence
- [ ] Word count is close to {wc} without visible padding
- [ ] canonical_url in the frontmatter is populated, not left empty
- [ ] At least 2 related concepts are named in Section 3, each with a `[LINK: ...]` placeholder where a target page is indicated
- [ ] No fabricated URLs anywhere - every internal reference uses the `[LINK: ...]` placeholder convention instead
- [ ] DefinedTerm JSON-LD block is real, populated code, not a prose recommendation
- [ ] No em dashes anywhere in the output

OUTPUT FORMAT:
Return the complete, publish-ready glossary page in this exact order:
1. Frontmatter block (title, tags, canonical_url, cover_image, description)
2. Direct Definition
3. In Practice
4. Why It Matters / Related Concepts
5. Schema Markup JSON-LD code block

No commentary, no explanations, no "here is your glossary page" preamble.
"""
    return frontmatter + body
