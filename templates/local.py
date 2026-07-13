from ._shared import BANNED_CTA_PHRASES, HUMAN_WRITING_RULES, RESEARCH_RULES, market_voice

_BANNED_CTA_LIST = ", ".join(f'"{p}"' for p in BANNED_CTA_PHRASES)


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
- Sentence 1 (14-17 words): State the value the reader gets, lead with an action verb, embed the primary keyword naturally
- Sentence 2 (17-21 words): Specify what the resource delivers - frameworks, data, examples, checklists
- Sentence 3 (14-17 words): Close with a soft CTA tied to the reader's role. Vary the exact phrasing post to post, do not reuse the same closing sentence across a batch. Examples of the pattern (write a new one each time, do not copy these verbatim): "Use it to tighten next quarter's rollout plan.", "Apply this before your next team review.", "Reference this the next time budget gets questioned.", "Bring this into your next planning conversation."

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
- Salesy phrases (the canonical banned-CTA list this project enforces everywhere, not just here): {_BANNED_CTA_LIST}, and "Don't miss out on this essential read"
- The identical closing sentence reused across multiple posts in the same batch - if you are generating more than one GMB post in a session, no two may share a closing sentence
- Em dashes - use hyphens only

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-REVIEW (before output):
- Word count exactly between 45 and 55? (Count again.)
- Could a stranger in the role of {audience} restate the value in one sentence after reading this?
- Is the primary keyword in the first 10 words?
- Does it sound like a senior peer wrote it, or a marketing intern?
- If generating multiple posts, does this closing sentence differ from every other post's closing sentence so far?

OUTPUT:
Return only the final 45-55 word description. No labels, no preamble, no explanations, no word count notation.
"""


def review_response(topic, audience, wordcount=None, market=None, **_):
    _default_cap = 150
    if wordcount:
        try:
            _target = int(wordcount)
        except (TypeError, ValueError):
            _target = _default_cap
        _word_budget = min(_target, _default_cap)
    else:
        _word_budget = 100

    return f"""You are a reputation-management specialist who has written review responses for local businesses, B2B software vendors, and consumer brands across Google, Yelp, Trustpilot, G2, and Capterra.

TASK:
Write a single reply to this review input: "{topic}"

TARGET AUDIENCE (who else reads this reply): {audience}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC (do this mentally before writing):
1. Classify the review first: is it POSITIVE (praise) or NEGATIVE (complaint), and what is the ONE specific thing praised or the ONE specific issue raised? Do not respond generically to "feedback" - respond to the actual content in "{topic}"
2. Who is the real reader? Every review reply is read far more by future prospects browsing the platform than by the original reviewer - write for that silent audience
3. What is the single next step (thanks + invite, or apology + offline contact) that fits this specific case?

STRUCTURE - choose the branch that matches your diagnostic:

IF POSITIVE:
- Open with specific, non-generic thanks that names the exact thing praised in "{topic}" - never open with "Thank you for your feedback!" as the whole response
- Reinforce the real value delivered, tied to that same specific detail, not a generic brand claim
- Where it fits naturally, invite further engagement (a repeat visit, a referral, a case study conversation) without sounding salesy - do not use any phrase from this banned-CTA list: {_BANNED_CTA_LIST}
- Sign off appropriately for the platform (owner/team name, or "The [Brand] Team")

IF NEGATIVE:
- Open by acknowledging the specific issue raised in "{topic}" - never open defensive or dismissive, and never dispute or argue with the reviewer's account of what happened inside the response itself
- Do not admit legal liability or use language that could be read as a legal admission ("we were negligent," "this is our fault legally") - acknowledge the experience and impact, not liability
- Offer one concrete next step: a named contact channel (support email, phone line, "please reach out to us directly at...") to move the conversation offline
- If a specific resolution or compensation has not been authorized in the input, do not invent one - use a placeholder like "[INSERT: specific resolution offered]" rather than fabricating a discount, refund amount, or promise
- Hard rule: never argue, never re-litigate the facts, never say the reviewer is wrong, anywhere in the reply

BOTH MODES:
- Brief: target about {_word_budget} words for this reply (a review reply is not an essay). Even if a longer word count is requested, treat roughly {_default_cap} words as the realistic ceiling for a single review reply - a 500-word reply reads as corporate overkill and hurts trust more than it helps, so use extra budget for specificity, not padding
- No corporate-sounding template language ("We take this very seriously," "Your feedback is important to us" as a standalone line)
- Sign off in a way that fits the platform implied by "{topic}" (Google/Yelp: owner or team name; G2/Capterra: product/company name; Trustpilot: brand name)

DO NOT USE:
- "Thank you for your feedback" as a complete opening line
- "We take this very seriously" / "Your feedback is important to us" as filler
- Salesy phrases (canonical banned-CTA list): {_BANNED_CTA_LIST}
- Any admission of legal fault or liability
- A fabricated specific resolution, refund amount, or compensation not present in "{topic}" - use an [INSERT: ...] placeholder instead
- Arguing with, correcting, or disputing the reviewer's account within the response
- Em dashes - use hyphens only

{HUMAN_WRITING_RULES}

SELF-CHECK (before output):
- Did you correctly classify positive vs. negative from "{topic}" before writing?
- Does the reply reference the specific thing praised or complained about, not a generic restatement?
- Negative only: is there zero language disputing the reviewer's account or admitting legal liability?
- Negative only: is any resolution detail either real (from the input) or clearly flagged as [INSERT: ...]?
- Is the reply close to {_word_budget} words, well under the {_default_cap}-word realistic ceiling?
- Any em dashes? Replace with hyphens.

OUTPUT FORMAT:
Return only the final reply text, ready to paste into the review platform. No labels, no preamble, no explanation of which branch (positive/negative) was chosen.
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
