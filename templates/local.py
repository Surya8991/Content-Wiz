from ._shared import HUMAN_WRITING_RULES, RANKABILITY_RULES, RESEARCH_RULES  # noqa: F401


def gmb(topic, audience, **_):
    return f"""You are a B2B content specialist who has written 500+ Google Business Profile posts that drive measurable click-through to client websites.

TASK:
Write a 50-word business description for the blog post titled: "{topic}"

TARGET AUDIENCE: {audience}

PRE-WRITE DIAGNOSTIC (do this mentally before writing):
1. What is the one specific pain point this blog post solves for {audience}?
2. What single phrase from the topic is the searchable keyword? (Use this verbatim in sentence 1.)
3. What concrete outcome will the reader gain after reading?

STRUCTURE (50 words, distributed as):
- Sentence 1 (12-15 words): State the value the reader gets, lead with an action verb, embed the primary keyword naturally
- Sentence 2 (15-20 words): Specify what the resource delivers - frameworks, data, examples, checklists
- Sentence 3 (12-18 words): Close with a soft CTA tied to the reader's role - "Use it to...", "Apply these to...", "Reference this when..."

STRICT REQUIREMENTS:
- Exactly 45-55 words (count every word, including articles)
- Total character count under 500 (Google's GMB description limit is 750, but shorter wins on mobile)
- Primary keyword from "{topic}" must appear in the first 10 words
- Must include: one specific benefit + one specific deliverable + one role-relevant CTA
- Active voice throughout - zero passive constructions
- Tone: authoritative peer giving practical advice, not marketing copy
- Reader must feel "this was written for someone in my exact role"

DO NOT USE:
- Openers like "This blog...", "In this post...", "Learn how..."
- Generic value words: "comprehensive", "ultimate", "complete", "everything you need"
- Salesy phrases: "Don't miss out", "Take advantage of", "Discover"
- Em dashes - use hyphens only

{HUMAN_WRITING_RULES}

SELF-REVIEW (before output):
- Word count exactly between 45 and 55? (Count again.)
- Could a stranger in the role of {audience} restate the value in one sentence after reading this?
- Is the primary keyword in the first 10 words?
- Does it sound like a senior peer wrote it, or a marketing intern?

OUTPUT:
Return only the final 45-55 word description. No labels, no preamble, no explanations, no word count notation.
"""


def pinterest(topic, audience="professionals and decision makers", **_):
    return f"""You are a Pinterest content strategist who manages B2B accounts averaging 500K+ monthly views, with deep knowledge of how Pinterest's algorithm ranks Pins in search and Smart Feed.

TASK:
Write a complete Pinterest Pin package for an image with the heading: "{topic}"

TARGET AUDIENCE: {audience}

PRE-WRITE DIAGNOSTIC:
1. What specific search query would {audience} type into Pinterest to find this Pin?
2. What action do you want them to take after seeing it - save, click through, or both?
3. What is the one piece of value the image alone communicates, and what does the description add on top?

DELIVERABLES (return all four):

1. PIN TITLE (100 characters max, displayed under the Pin in feeds):
   - Front-load the primary keyword from "{topic}" (Pinterest weighs the first 30 chars heavily for search)
   - Use Title Case for major words
   - Add one specificity hook: a number, a year, or a clearly defined audience
   - Format examples: "5 Factors That Affect Business Credit in 2025" / "How HR Leaders Evaluate Training ROI"

2. PIN DESCRIPTION (2 lines, 100-200 chars total - sweet spot for Pinterest SEO):
   - Line 1: A keyword-rich statement that sounds natural - include the primary keyword + 1-2 semantic variations
   - Line 2: A soft pivot toward action - "Save this for your next planning session", "Use this when reviewing...", "Reference this before..."
   - Total: 40-60 words across both lines
   - Tone: informative peer, not salesperson
   - The description is also indexed by Pinterest search - treat it as SEO real estate, not flair

3. ALT TEXT (for the image, accessibility + SEO):
   - 8-15 words describing what the image actually shows
   - Include the primary keyword naturally
   - Format: "[Visual description] showing [key concept] for [audience]"

4. HASHTAGS (4-5 tags, placed at the very end of the description):
   - Distribution: 1 broad industry tag (1M+ Pins) + 2-3 mid-tier niche tags (100K-1M) + 1 specific niche tag (<100K)
   - All lowercase, no spaces, no symbols
   - Must be Pinterest-active tags - not Twitter/Instagram conventions
   - Avoid: #success #motivation #tips #blog #pinterest

PINTEREST-SPECIFIC RULES:
- Pinterest is a visual search engine, not a social network - write for search intent, not engagement
- Pins have a long shelf life (months to years) - prioritize evergreen relevance over trending hooks
- Pinterest users are in planning/research mode, often saving for later action - the Pin must feel useful 6 months from now
- Avoid emojis in the title (they hurt Pinterest search ranking)
- Up to 2 emojis in the description are acceptable but not required

DO NOT USE:
- "Don't miss out", "Check this out", "Click here", "Read more"
- Buzzwords: comprehensive, ultimate, game-changer
- Em dashes (use hyphens only)
- Excessive punctuation or all-caps words

{HUMAN_WRITING_RULES}

SELF-REVIEW (before output):
- Would a {audience} professional searching Pinterest for this exact topic find this Pin via the title and description?
- Is the primary keyword in the title's first 30 chars?
- Does the description read naturally, or feel keyword-stuffed?
- Are the hashtags ones a Pinterest user would actually search for?

OUTPUT FORMAT:
Pin Title:
[Title text]

Pin Description:
[Line 1]
[Line 2]

Alt Text:
[Alt text]

Hashtags:
#tag1 #tag2 #tag3 #tag4 #tag5
"""
