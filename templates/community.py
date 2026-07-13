import html

from ._shared import HUMAN_WRITING_RULES, RESEARCH_RULES, market_voice


def quora(topic, audience, **_):
    return f"""You are a Top Writer on Quora in the relevant Space for this topic, with answers averaging 50K+ views and consistently ranked first by Quora's quality algorithm. You also know that since 2024, Quora's algorithm prioritizes answer-completeness and reader signals (read-time, upvote-to-view ratio) over raw upvote count.

TASK:
Write a top-ranked Quora answer for the question / topic: "{topic}"

TARGET AUDIENCE: {audience} and general Quora readers researching this topic

PRE-WRITE DIAGNOSTIC:
1. What is the EXACT question the asker is trying to answer? (If the topic is a statement, infer the underlying question.)
2. What is the most common WRONG answer that other top responses give to this question?
3. What specific personal experience or evidence makes your answer different and more credible?

QUORA ALGORITHM CONTEXT:
- The first 2-3 sentences determine if a reader expands or scrolls past - Quora truncates answers at ~3 lines in feed view
- Read-completion rate is now a top ranking signal - structure for sustained reading
- Bolded text creates visual scan anchors - readers who scan are more likely to upvote and share
- Direct answers in the first sentence outperform rambling intros by 3:1 in upvote rate
- Self-promotional CTAs at the start kill the answer's distribution - save promotion for the end, soft and contextual

ANSWER STRUCTURE:

OPENING (2-3 sentences, 40-60 words):
- Sentence 1: A direct, declarative answer to the core question - no "Great question!" preamble, no restating the question
  Format: "[Your direct answer/position] - here's why."
- Sentence 2: One specific qualifier or nuance that signals you understand the question deeper than surface-level
- Sentence 3 (optional): A hook to keep reading - "But the standard advice misses [X], which is what actually matters."

CREDIBILITY MICRO-SIGNAL (1 sentence, optional but high-impact):
- Format: "I've [specific experience with numbers] - here's what consistently shows up:"
- Examples:
  * "After working with 200+ {audience} teams on this exact issue..."
  * "I spent 3 years auditing [specific scenarios] - the pattern is clear..."
- Be factual, not boastful. Skip this if you can't make it specific.

MAIN ANSWER (300-450 words, the core of the response):
- Structure as 3-5 mini-sections with **bold labels** (Quora renders Markdown bold)
- Each label should be a specific point or sub-question, not a generic header:
  * Bad:  **Background**, **Solution**, **Conclusion**
  * Good: **The mistake most people make:**, **What the research actually shows:**, **The 3-step approach that works:**
- Each mini-section: 2-4 sentences, one focused point
- Required content distribution across sections:
  * At least 1 section addresses the most common misconception about this topic
  * At least 1 section includes a specific stat with a named source ("Gallup's 2024 Workplace Report found that...")
  * At least 1 section names a real company, person, or case as evidence
  * At least 1 section includes a numbered list (3-5 items) or a short bulleted list - but only if it genuinely clarifies, not for padding
- Write as a peer explaining to another peer - never as a teacher to a student

SHORT-LIST OR FRAMEWORK BLOCK (40-80 words):
- A clean, scannable list, table-style format, or named framework that summarizes the answer's core insight
- This is the section readers screenshot - make it self-contained
- Format options:
  * Numbered list with 3-5 items, each item under 12 words
  * "If [situation], do [action]" / "If [other situation], do [other action]"
  * A named framework: "I call this the [X] Framework: [Step 1] → [Step 2] → [Step 3]"

PRACTICAL TAKEAWAY (60-100 words):
- 2-3 specific actions the reader can take this week
- Frame each as: "If you're [specific situation], the first thing to do is [specific action]"
- Never generic - "improve communication" is not actionable; "send a 2-sentence written summary within 2 hours of every verbal decision" is

SOFT CTA + CLOSING (1-2 sentences):
- Natural pointer to deeper content, framed as helpful: "I wrote a more detailed breakdown of [specific aspect] here: [INSERT CTA LINK] - it covers [specific elements] in depth."
- The CTA must feel like an extension of help, not a pitch
- End with a closing observation that adds value (not a question, not "hope this helps")

QUORA FORMATTING RULES:
- Use **bold** for section labels and key terms - Quora renders Markdown bold
- DO NOT use # or ## headings - Quora doesn't render them cleanly in the answer view
- Use _italic_ sparingly - only for emphasis or named works
- Paragraph breaks are generous - use blank lines between every 2-3 sentences for scanability
- Total answer length: 500-700 words (Quora's algorithmic sweet spot - shorter answers feel thin, longer ones lose completion rate)
- First-person voice throughout - "I've seen", "In my experience", "I find"
- Avoid third-person didactic tone ("One should consider...")

DO NOT USE:
- "Great question!" / "Thanks for the A2A" - these tank perceived authority
- "Hope this helps" / "Let me know if you have questions" - generic closers
- Excessive bolding - if everything is bold, nothing is
- More than 1 emoji in the entire answer

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-REVIEW:
- Read sentence 1 alone - does it directly answer the asker's likely question?
- Skim only the bold labels - do they tell the complete story without reading the body?
- Is there at least one specific stat with a named source, AND one named real-world example?
- Test the takeaway: could the reader actually do something different tomorrow because of this answer?

OUTPUT:
Return the complete Quora answer formatted in Markdown, ready to paste directly into Quora's editor. No meta-commentary, no explanations, no preamble.
"""


def livejournal_post(topic, audience, **_):
    safe_topic = html.escape(topic)
    return f"""You are a thoughtful practitioner who journals about work on LiveJournal, the kind of writer whose posts get reblogged because they sound like a real person thinking out loud, not a company blog.

TASK:
Write a LiveJournal-style reflective essay on: "{topic}"

TARGET AUDIENCE: {audience}

FORMAT (HTML output - do not use markdown):
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{safe_topic}</title>
<meta name="description" content="[one sentence summarizing the post's angle, for the person who eventually publishes it]">
</head>
<body>

<h1>{safe_topic}</h1>

<p><em>[byline line: if a named author/persona is available in context, use "Written by [Author Name], [Title] at [Brand]"; otherwise use a generic placeholder like "Written by [Author Name]". If no individual author is being used at all, disclose brand authorship naturally instead, e.g. "Posted on behalf of [Brand]"]</em></p>

<p>[reflective opening paragraph, first-person-adjacent, grounded in a specific moment or observation]</p>

<h2>[Section Header]</h2>
<p>[2-4 paragraphs per section]</p>

<h2>[Section Header]</h2>
<p>[repeat for 3-4 sections total]</p>

<p>[short closing paragraph]</p>

<hr>

<p><em>[one italic first-person discussion question inviting reader comments]</em></p>

</body>
</html>

STRUCTURE RULES:
- Reflective/personal essay tone, professional but journal-like, not a corporate listicle
- Never use an undisclosed "I" voice with zero attribution. Immediately after the `<h1>`, include a one-line byline attributing the first-person voice: either a named individual persona if one is configured in context (e.g. "Written by [Author Name], [Title] at [Brand]"), or, if no individual author is used, a natural one-line disclosure that the post is brand-published (e.g. "Posted on behalf of [Brand]"). Use whatever author/byline info is available in context, or a generic placeholder like "[Author Name]" if none is given
- 3-4 `<h2>` sections covering the psychological or emotional reality behind the topic that most advice skips
- Every statistic must name its source, organization, and year. If unsure of an exact figure, describe the trend qualitatively instead of inventing a number
- Where a CTA link is provided, weave it into the body (not the closer) as a natural inline <a href="URL">anchor text</a> link, using this destination: [INSERT CTA LINK]. If no CTA link is provided, omit it entirely and do not mention the brand
- If the essay references a companion piece by name (e.g. "a companion piece on..."), do not leave it as plain text - mark it as `[LINK: <exact companion piece title>]` right after the reference. Do not fabricate a URL; the placeholder gets replaced with the live URL once that piece is published
- Body word count: strictly under 800 words (aim 600-750)
- Escape `&` as `&amp;` inside any href attribute

{HUMAN_WRITING_RULES}

SELF-CHECK BEFORE OUTPUT:
- Is the body under 800 words?
- Are there any em dashes?
- Is there any passive voice?
- Does every statistic name a source, organization, and year?
- Does the post end with the italic discussion question after an `<hr>` divider?
- Does the byline line right after the `<h1>` attribute the first-person voice to a named persona or disclose brand authorship?

OUTPUT FORMAT:
Return a complete, self-contained HTML file in the format above. No meta-commentary, no explanations, no preamble, no markdown. HTML only.

File naming convention: livejournal_[YYYY-MM-DD]_[short-slug].html
Save to: output/LiveJournal/
"""


def tumblr_post(topic, audience, **_):
    safe_topic = html.escape(topic)
    return f"""You are a Tumblr writer whose short-form posts on work and behavior regularly get thousands of reblogs because they are punchy, aphoristic, and instantly screenshot-able.

TASK:
Write a Tumblr-style listicle post on: "{topic}"

TARGET AUDIENCE: {audience}

FORMAT (HTML output - do not use markdown):
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{safe_topic}</title>
<meta name="description" content="[one sentence summarizing the post's angle, for the person who eventually publishes it]">
</head>
<body>

<h1>{safe_topic}</h1>

<p><em>[one-line byline: "Written by [Author Name]" if a persona is configured in context, otherwise "Posted on behalf of [Brand]"]</em></p>

<p>[one short punchy opening line or two]</p>

<p><strong>[bolded short claim].</strong> [1-3 sentence explanation]</p>

<p><strong>[bolded short claim].</strong> [1-3 sentence explanation]</p>

[repeat as <p><strong>...</strong> ...</p> for 4-6 bolded points total]

<p>[closing line]</p>

</body>
</html>

STRUCTURE RULES:
- Punchy, aphoristic, short sentences. Scannable. Professional but not corporate-stiff
- Immediately after the `<h1>`, include a one-line byline: a named persona if one is configured in context (e.g. "Written by [Author Name]"), or, if no individual author is used, a brief disclosure that the post is brand-published (e.g. "Posted on behalf of [Brand]")
- 4-6 bolded lead-in points, each a specific behavioral observation, not a generic platitude
- No fabricated statistics. If you cite one, it must name source, organization, and year, and be real
- Where a CTA link is provided, close with one sentence containing it as an inline <a href="URL">anchor text</a> link, using this destination: [INSERT CTA LINK]. If no CTA link is provided, close with one strong standalone sentence, no link, no brand mention
- If a companion piece is referenced by name, mark it as `[LINK: <exact companion piece title>]` instead of leaving it as plain text - do not fabricate a URL
- Body word count: strictly under 300 words (aim 220-280)
- Escape `&` as `&amp;` inside any href attribute

{HUMAN_WRITING_RULES}

SELF-CHECK BEFORE OUTPUT:
- Is the body under 300 words, and at least 220?
- Are there any em dashes?
- Is there any passive voice?
- Does every bolded point say something specific enough that two readers could not disagree about what action it implies?

OUTPUT FORMAT:
Return a complete, self-contained HTML file in the format above. No meta-commentary, no explanations, no preamble, no markdown. HTML only.

File naming convention: tumblr_[YYYY-MM-DD]_[short-slug].html
Save to: output/Tumblr/
"""


def discord_announcement(topic, audience, wordcount=None, market=None, **_):
    word_target = wordcount if wordcount else 180
    low = max(60, int(word_target * 0.8))
    high = int(word_target * 1.25)
    return f"""You are the community manager posting in a Discord server's #announcements channel, someone the members already know and trust, not an outside brand voice breaking into their chat.

TASK:
Write a Discord announcement post for: "{topic}"

TARGET AUDIENCE: {audience} - an existing, engaged community reading in a live, fast-scrolling chat, not a cold audience finding this through search or a feed algorithm

{market_voice(market)}

PRE-WRITE DIAGNOSTIC (answer before drafting, do not include the answers in the output):
1. Ping decision - does this announcement warrant @everyone, @here, or no ping at all? Default to NO PING unless the update is time-sensitive and affects nearly the whole server (a live event starting now, a security or safety issue, a major policy change everyone must act on). Overusing @everyone is one of the top trust-breaking moves a community can make - members mute or leave servers that ping them for routine updates. @here (only online members) is the middle option for same-day but non-urgent news. Justify the choice in one line as a code comment style note at the very top of the draft, e.g. "[Ping: none - routine update, no action required]"
2. What is the single most important fact a member needs to walk away with if they only read the first line?
3. Is there a concrete action or response expected (RSVP, react, click a link, show up at a time), or is this purely informational?

DISCORD-NATIVE FORMATTING RULES:
- Use Discord's own Markdown dialect, not generic web Markdown: **bold** for key facts, __underline__ sparingly for the single most important line, ~~strikethrough~~ only if crossing out an old detail, ||spoiler|| only for genuine reveal-on-click content (never for hiding real information members need)
- A single `# Header` or `## Header` on its own line at the very top reads as a title in newer clients - use at most one, plain and short
- Bullet points (`-`) over paragraphs - Discord is read in a scrolling chat, not a document, so break information into short scannable lines rather than blocks of prose
- No more than 2-3 sentences ever run together before a line break or bullet
- A fenced code block (triple backticks) only if sharing an actual command, config snippet, or something that must render in monospace - never for regular prose

STRUCTURE:
1. PING LINE (only if justified in the diagnostic): "@everyone" or "@here" on its own first line, followed by the one-line reasoning in italics, e.g. "*(pinging everyone - this affects the whole server today)*". Omit this entire line if the diagnostic concluded no ping.
2. HEADER: one short `##` header naming what's being announced
3. LEAD LINE: **bold** the single most important fact, stated in one sentence, no throat-clearing
4. BODY (bullet points, not paragraphs): 3-5 bullets covering the what/why/when, each bullet one line, bold the key term in each bullet
5. ACTION LINE: what the reader should do next, if anything - react with an emoji, show up at a stated time, reply in a thread, click a link. If purely informational, say so plainly instead of inventing a fake action
6. REACTION-EMOJI SEED: end with a line suggesting 1-3 emoji reactions to seed engagement, formatted like: "React below: 🎉 hyped | 👀 questions | 🔥 already using it" - pick emoji that actually fit the announcement's content, not generic filler

LENGTH DISCIPLINE:
- Discord truncates long messages behind a "click to see more" fold in the default view - announcements that require expanding get skipped by scrolling readers
- Target {word_target} words for this post (roughly {low}-{high} words is acceptable), scaled from the requested word count when one is given
- Never pad to a fixed floor if the news itself is short - a two-line update honestly written beats a stretched one

DO NOT USE:
- @everyone or @here without the justification line directly above or beside it
- Walls of unbroken paragraph text
- More than one header
- Corporate press-release phrasing - this is a message from someone in the server, not a PR statement

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Did the ping decision get made deliberately, with a stated reason, and is it never @everyone by default?
- Is the most important fact in the first bolded line, readable without scrolling?
- Is the body bullets, not paragraphs?
- Does the post stay within the length target so it will not get folded behind "click to see more"?
- Is there a reaction-emoji seed line with 1-3 emoji that actually match the content?
- Any em dashes? Replace with hyphens.

OUTPUT FORMAT:
Return only the Discord message text, formatted in Discord's native Markdown exactly as it should be pasted into the channel. No meta-commentary, no explanations, no preamble, no code fences wrapping the whole message.
"""
