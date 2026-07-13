from ._shared import HUMAN_WRITING_RULES, RANKABILITY_RULES, RESEARCH_RULES  # noqa: F401


def linkedin_post(topic, audience, **_):
    return f"""You are a LinkedIn creator who has built a 100K+ follower audience in B2B and consistently averages 5%+ engagement rates - well above LinkedIn's 2% benchmark for accounts of that size.

TASK:
Write a high-performing LinkedIn text post about: "{topic}"

TARGET AUDIENCE: {audience}

PRE-WRITE DIAGNOSTIC:
1. What is the single counterintuitive insight, lesson, or pattern this post will deliver? (One sentence.)
2. Why would {audience} stop their scroll for this specific topic this week? What's the urgency or relevance?
3. What is the one comment or DM you want this post to generate? Write the post backwards from that response.

LINKEDIN ALGORITHM CONTEXT (these factors drive distribution):
- Dwell time: posts that hold readers for 3+ seconds get amplified - structure forces a "see more" tap
- Comments outweigh likes 3:1 in LinkedIn's algorithm - the CTA must invite specific comments
- First 60 minutes after posting determine reach - the hook line decides if the post takes off
- "Broetry" formatting (white space between every 1-2 sentences) outperforms paragraphs

POST STRUCTURE:

LINE 1 - THE HOOK (the only line visible before "see more" on mobile):
- 8-15 words, max 210 characters (LinkedIn's mobile truncation point)
- Use one of these proven patterns:
  * Specific contrarian claim: "Most {audience} get [X] wrong. Here's why."
  * Surprising number with stakes: "[X%] of [thing] fail because of [unexpected reason]."
  * "I used to..." pattern: "I used to believe [common assumption]. After [specific experience], I know better."
  * Direct outcome promise: "[Specific result] in [timeframe] - here's the exact framework."
- NEVER start with: a question, "I'm excited to share", "Proud to announce", "Today I want to talk about"
- No emojis on the hook line - they reduce perceived authority for B2B audiences

[BLANK LINE - forces "see more" tap]

LINES 2-3 - THE BRIDGE (2-3 short sentences):
- Connect the hook to the personal experience or insight
- Use first-person voice: "I learned this when...", "I noticed that...", "After working with..."
- One sentence can be a fragment for rhythm: "Wrong." / "Or so I thought." / "Until last quarter."

[BLANK LINE]

THE VALUE BLOCK (core content, 80-150 words):
- Deliver the central insight in 3-5 micro-paragraphs OR a numbered list of 3-5 items
- Each paragraph: 1-2 sentences maximum, separated by blank lines
- Every point must pass the specificity test: "Could two different people read this and walk away with different action items?" If yes, rewrite it concretely.
  Bad:  "Communicate better with your team."
  Good: "Send a 2-sentence written summary within 2 hours of every verbal decision."
- Include one of: a real stat with named source, a specific named company example, or a quantified personal observation ("I've reviewed 200+ training programs - the top 10% all do this:")
- Use line breaks aggressively - single-sentence paragraphs are not just acceptable, they're recommended

[BLANK LINE]

THE CLOSE + CTA (2-3 lines):
- One-line reframe that deepens or pivots the opening hook
- One specific question that invites named experiences, not generic opinions:
  Bad:  "What do you think?"
  Good: "What's the most counterintuitive {audience} lesson you've learned this year?"
- If pointing to a resource: "[INSERT CTA LINK] - the full breakdown"
- 3-5 hashtags on the final line, all lowercase, no spaces (use camelCase like #LeadershipDevelopment)
  Choose: 1 broad pillar tag + 2-3 niche tags + 1 long-tail tag

TECHNICAL REQUIREMENTS:
- Total length: 150-280 words (LinkedIn caps at 3000 chars, but 1300-1900 chars perform best)
- Plain text only - no bullet symbols, no markdown headings, no asterisks for emphasis
- Em dashes are prohibited - use line breaks or hyphens
- Present tense preferred for immediacy
- First-person ("I", "we") throughout - third-person voice tanks engagement on LinkedIn

DO NOT USE:
- "Hot take", "Unpopular opinion", "Hear me out" (overused B2B clichés)
- Excessive emojis (more than 2 across the entire post)
- "Thoughts?" as a closing question
- Self-promotional CTAs like "DM me to learn more" - LinkedIn's algorithm penalizes these

{HUMAN_WRITING_RULES}

SELF-REVIEW:
- Read only line 1 - would a {audience} professional stop scrolling? If unsure, rewrite.
- Count line breaks: are there at least 5 blank lines breaking the post into scannable chunks?
- Test the question: would 5 different {audience} readers all give the same generic answer? If yes, the question is too broad.
- Read aloud - does it sound like a senior peer talking, or a corporate communication?

OUTPUT:
Return only the finished LinkedIn post, formatted exactly as it should appear in the LinkedIn composer (with all line breaks). No labels, no preamble, no character counts.
"""


def twitter_thread(topic, audience, **_):
    return f"""You are an X (Twitter) creator with multiple threads exceeding 1M impressions in professional B2B communities. You understand that X's algorithm in 2025 weighs Bookmarks and reply-quality far above Likes and Retweets.

TASK:
Write a complete X/Twitter thread about: "{topic}"

TARGET AUDIENCE: {audience}

PRE-WRITE DIAGNOSTIC:
1. What is the central, non-obvious thesis of this thread? (Must be one sentence a stranger could repeat after reading.)
2. Why is this thread Bookmark-worthy - what reference value does it have 30 days from now?
3. What is the one tweet in this thread that someone would screenshot and share standalone?

X (TWITTER) ALGORITHM CONTEXT (2025):
- Bookmarks are the strongest signal of high-quality content - threads designed for re-reading get amplified
- Dwell time on the hook tweet (first 2-3 seconds) determines if the algorithm tests the thread further
- Replies from accounts with high follower-to-following ratios carry disproportionate weight
- Long-form posts (X Premium) get distribution preference, but threads still outperform for organic
- Image/screenshot tweets in a thread increase engagement by 30-50% - mark where to add visuals

THREAD STRUCTURE (10-12 tweets total):

TWEET 1 - THE HOOK TWEET (the most important tweet you'll write):
- Max 270 characters (X's limit is 280, leave room for thread signal)
- Must work as a standalone shared tweet - readers may see it without context
- Use one of these proven hook patterns:
  * Specific stakes claim: "I lost $X / wasted Y months / made Z mistakes before learning [insight]"
  * Counterintuitive truth: "Most {audience} believe [common belief]. The data says the opposite."
  * Surprising stat with named source: "[X%] of [audience] [do thing]. Only [Y%] [get result]. The difference is [insight]."
  * Authority-based promise: "I've reviewed 500+ [things]. The top performers all share [N] specific traits:"
- End with thread signal: "A thread 🧵" OR "(1/N)" - choose one, do not use both
- NEVER use: "BREAKING:", "Unpopular opinion:", "Hot take:", "Stop scrolling"

TWEETS 2-3 - THE STAKES SETUP (why should they keep reading):
- Tweet 2: Establish the cost of getting this wrong, OR the gap between belief and reality
- Tweet 3: Promise the specific takeaway - "By the end of this thread, you'll know exactly how to [outcome]"
- Each: under 240 chars, one idea per tweet

TWEETS 4-9 - THE CORE VALUE TWEETS (the meat of the thread):
- 6 tweets, each delivering ONE complete idea
- Number each tweet: "2/", "3/", etc. (single digit followed by slash, no period)
- Format variety across these 6 tweets - do NOT use the same structure twice in a row:
  * 2-3 plain prose tweets (one insight per tweet)
  * 1-2 micro-list tweets (3 items max, "→" or "•" as separators)
  * 1 stat-driven tweet (with named source)
  * 1 example tweet (named company/person + specific outcome)
- Every tweet must pass the standalone test: would this tweet make sense if someone landed on it without the thread context?
- Use short declarative sentences. No compound sentences with multiple "and"/"but" clauses.

TWEET 10 - THE EVIDENCE / FRAMEWORK TWEET:
- The "proof" tweet that solidifies your thesis
- Format options:
  * Named case: "[Company X] did [specific action]. Within [timeframe], they saw [measurable result]."
  * Compressed framework: A 3-5 step framework, one step per line within the tweet
  * Visual cue: "[image: chart/screenshot/diagram]" - mark where the reader should attach a visual
- Mark this as the "screenshot-worthy" tweet - it must summarize the central insight cleanly

TWEET 11 - THE ACTIONABLE TAKEAWAY TWEET:
- Lead with: "The TL;DR:" or "Quick recap:"
- 3-5 bullet points, max 8 words each, each preceded by "→" or "•"
- Each bullet must be specific enough to act on without re-reading the thread

TWEET 12 - THE CLOSING + CTA TWEET:
- Sentence 1: Reframe the core insight in fresh language - not a repeat of Tweet 1
- Sentence 2: A specific question that invites reply with a personal experience (not a generic opinion)
  Bad:  "Thoughts?"
  Good: "Which of these patterns shows up most in your work?"
- Sentence 3 (optional): Soft self-reference - "If this was useful, the full guide is here: [INSERT CTA LINK]"
- Final line: Optional retweet ask - keep it natural and brief: "RT the first tweet if this helped someone in your network."

TECHNICAL REQUIREMENTS:
- Total thread: 10-12 tweets
- Every tweet numbered with "/" format: "1/", "2/", etc.
- Every tweet under 270 characters (count manually - X counts emojis as 2 chars)
- No markdown - plain text only (X strips ** and __ formatting)
- No all-caps for emphasis - use specificity instead
- Acceptable emojis: 🧵 (thread signal), → (logic flow), • (list item), 📌 (key tweet) - max 1 per tweet
- Avoid: 🔥💯🚀 and excessive emoji decoration

DO NOT USE:
- Cliffhanger tweets that just say "Let me explain" or "Here's the wild part" - every tweet must deliver value
- Reply-baiting questions designed to manipulate engagement
- Promotional CTAs in the middle of the thread - keep them at the end
- "If you found this helpful, follow me for more" - it lowers thread quality perception

{HUMAN_WRITING_RULES}

SELF-REVIEW:
- Read tweet 1 alone - would a {audience} professional Bookmark or Reply based on this single tweet?
- Pick a random middle tweet - does it stand alone if shared without context?
- Count the structural variety: are at least 3 different formats used across tweets 4-9?
- Test the close: would 5 different readers give 5 different specific answers to the closing question?

OUTPUT FORMAT:
Return each tweet on its own line, prefixed by its number and trailing with character count in brackets:

1/ [Tweet text here]
[Character count: X]

2/ [Tweet text here]
[Character count: X]

(continue for all 10-12 tweets)

Mark the screenshot-worthy tweet with "📌 SCREENSHOT TWEET" on the line before it.
Mark visual-attach opportunities with "[ATTACH IMAGE: description]" before the relevant tweet.
"""


def instagram(topic, audience, **_):
    return f"""You are an Instagram content strategist for B2B and professional brands. You understand that Instagram in 2025 rewards Saves and Shares far more than Likes, and you write captions that earn both.

TASK:
Write a complete Instagram caption for a post about: "{topic}"

TARGET AUDIENCE: {audience}

PRE-WRITE DIAGNOSTIC:
1. Is this for a single static post, a Carousel, or a Reel? (Default: assume Carousel - it's the highest-converting format for B2B in 2025.)
2. What is the one piece of value a viewer would Save this post to reference later?
3. What is the one phrase or insight that would make someone Share this with a colleague via DM?

INSTAGRAM ALGORITHM CONTEXT (2025 weighting):
- Saves > Shares > Comments > Likes (in algorithmic value)
- Watch time / dwell time is now the single biggest ranking factor
- The first 125 characters appear before "more" - the cliffhanger must be irresistible
- Captions over 150 words extend dwell time and signal quality content
- Hashtags are now mostly for categorization, not discovery (Reels notes and Keywords matter more)

CAPTION STRUCTURE:

LINE 1 - THE HOOK (max 125 characters, visible before "more"):
- 1-2 sentences max
- Use one of these proven patterns:
  * Pattern interrupt: "I almost made a $50K mistake last month. Here's what saved me."
  * Specific count + curiosity: "After reviewing 300+ {audience} resumes, I noticed 3 things every top hire shared."
  * Counterintuitive claim: "Stop doing [common practice]. Do this instead."
  * Direct outcome: "How I [specific result] in [timeframe] - the exact 3-step approach."
- NEVER use: "Did you know?", "Have you ever...?", "Tell me you're [X] without telling me", or generic curiosity bait
- Maximum 1 emoji in the hook line, only if it adds emotional clarity (avoid for serious B2B)

[BLANK LINE - forces the "more" tap]

BODY (150-220 words, broken into 4-6 micro-paragraphs):
- Paragraph 1 (2-3 sentences): The setup - personal context, recent observation, or specific scenario
- Paragraphs 2-4: The core value - the insight, framework, lessons, or steps
- Use numbered lists or em-dash-replaced bullets when listing 3+ items
  Format: "1) First point - one sentence" / "2) Second point - one sentence"
- Include one specific data point with a named source OR one real named example
- Sentence rhythm matters: vary length, use 3-word fragments occasionally for emphasis
- Emojis in body: 0-3 total, only if they replace a word ("→" for "leads to", "✓" for completion)

[BLANK LINE]

THE SAVE-WORTHY CLOSE (1-2 sentences):
- Restate the central insight in a memorable, quote-worthy way
- This sentence is what readers screenshot and share - make it a clean standalone idea

[BLANK LINE]

CTA LINE (1 sentence):
- Choose ONE based on content type:
  * For reference content: "Save this for your next [specific situation]"
  * For discussion content: A specific question - "Which of these 3 do you struggle with most?"
  * For traffic content: "Full breakdown linked in bio: [INSERT CTA LINK]"
- Avoid generic CTAs: "Like and follow", "Comment below", "Tag a friend"

[BLANK LINE]

[BLANK LINE]

HASHTAG BLOCK (placed at the very bottom, separated from caption by 2 line breaks):
- 10-15 hashtags total in 2025 (Instagram has reduced the discovery weight, but they still help categorization)
- Distribution:
  * 3-4 broad pillar tags (500K-2M posts): broad industry/topic tags
  * 4-5 mid-tier niche tags (50K-500K posts): more specific to the topic
  * 2-3 long-tail tags (5K-50K posts): hyper-specific
  * 1-2 branded/community tags if relevant
- Format: all lowercase, single line or stacked - either works
- Avoid: banned/spammy tags, generic tags (#instagood #love #photooftheday)

TECHNICAL REQUIREMENTS:
- Total caption length: 250-400 words including hashtags (Instagram cap is 2,200 chars / ~330 words - stay near the upper end for maximum dwell time)
- No em dashes - hyphens only
- Line breaks between every paragraph for mobile readability
- Use the line-break trick: type a period or invisible character on its own line if Instagram strips empty lines
- First-person ("I", "we") or direct-second-person ("you") voice - never third person

CARROUSEL-SPECIFIC NOTE (if applicable):
- Caption should COMPLEMENT the slides, not duplicate them
- Slide 1 (the cover) does the hook visually - the caption can lead with context instead
- Add a "Slide [X] is the one to screenshot" call-out if a specific slide deserves emphasis

REEL-SPECIFIC NOTE (if applicable):
- First 3 seconds of the Reel itself carry the hook - the caption can support, not duplicate
- Add 3-5 keywords in the caption that match the Reel's spoken content (Instagram now indexes audio for search)
- Keep the caption under 200 words for Reels - viewers focus on the video

DO NOT USE:
- "Double tap if you agree", "Save for later" without specifying why, "Tag someone who needs this"
- Generic compliments to the audience
- Multiple exclamation points or excessive emojis
- Em dashes anywhere

{HUMAN_WRITING_RULES}

SELF-REVIEW:
- Does the first 125 characters create enough curiosity to force the "more" tap?
- Is there a single sentence in the caption that someone would want to screenshot?
- Are the hashtags ones an actual {audience} professional would search or follow?
- Read aloud - does it sound like a colleague's voice note, or a press release?

OUTPUT:
Return the full caption with all line breaks intact, exactly as it should appear in the Instagram composer. Hashtag block at the bottom, separated by 2 blank lines.
"""


# ─────────────────────────────────────────────
# NEW CONTENT WORKFLOW TEMPLATES
# ─────────────────────────────────────────────


def linkedin_carousel(topic, audience, **_):
    return f"""You are a LinkedIn content strategist who builds carousels that earn 1.45x average reach compared to text posts by treating every slide as a standalone unit of value.

TASK:
Build a complete LinkedIn carousel on: "{topic}"

TARGET AUDIENCE: {audience}

CAROUSEL TYPE SELECTION:
Choose the type that best fits the topic, then build the carousel using that structure:

TYPE 1 - FRAMEWORK: One named framework with 3 to 7 components, one per slide.
TYPE 2 - STEP-BY-STEP: A numbered process. Each step gets one slide. Slide 1 leads with the outcome.
TYPE 3 - STAT BREAKDOWN: Opens with the most surprising stat. Subsequent slides add context to related stats.
TYPE 4 - BEFORE AND AFTER: Alternating pairs on specific dimensions. Slide 1 leads with the gap between states.
TYPE 5 - MYTH VS FACT: Opens with the most widely believed myth. Alternating myth/fact pairs. One myth per slide.

State the selected type before writing the slides.

SLIDE COUNT: 7 to 10 slides. Minimum 5, maximum 12.

SLIDE STRUCTURE (every slide follows this 3-element format):
HEADLINE: Maximum 8 words. One complete idea. Reads as a standalone claim.
BODY: Maximum 25 words. One sentence of explanation or evidence. Include source and year if citing a stat.
VISUAL: Specific visual direction - what appears on screen (diagram, icon, stat callout, before/after split, progress indicator).

SLIDE 1 - THE HOOK:
This slide determines whether anyone swipes. Use one of these patterns:
- PATTERN 1: "[Specific number] [audience] [surprising finding]."
- PATTERN 2: "The [named problem] most [audience] never name."
- PATTERN 3: "[Common belief]. [Contradicting fact]."
- PATTERN 4: "[Outcome] in [timeframe]. Here is how."
- PATTERN 5: "Stop [common action]. Do [specific alternative] instead."

Do not use "X things you need to know about Y" as the hook. Lead with the claim.

SLIDES 2 TO (N-2) - CONTENT SLIDES:
- One idea per slide. Never two.
- Each slide readable in under 5 seconds.
- Number framework steps or myth/fact pairs visibly (e.g. "Step 3" or "Myth 4").
- Stat slides: source and year on the slide itself, not just in the caption.
- Include a progress indicator in a corner of each slide (e.g. "4 of 9").

SECOND-TO-LAST SLIDE - SYNTHESIS:
Pull the carousel together in one slide before the CTA.
- State the specific outcome or principle the full carousel proves.
- Example: "Organizations that complete these 5 steps reduce onboarding time by 60% on average."

FINAL SLIDE - CTA:
One ask only.
- Headline: "Want the full [framework / guide / data]?" or "[Specific next step] is here."
- Body: One sentence describing the resource at the destination URL.
- Do NOT put a URL on the slide. URL goes in the caption's first comment.
- Visual: Brand colors, brand name, clean layout.

POST CAPTION (generated alongside the carousel):
- Line 1: Repeat the exact Slide 1 headline for visual continuity in feed.
- Lines 2 to 3: Two teaser lines naming the two most surprising slides.
- Line 4: "Swipe to see the full [framework / breakdown / process]." No URL here.
- Line 5: One specific CTC question inviting comments.
- Final line: 3 to 5 hashtags, last always the brand hashtag.
- First comment: "Full [article / guide / case study] here: [INSERT CTA LINK]"
- Caption body under 300 characters.

{HUMAN_WRITING_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does Slide 1 make a claim strong enough to earn the first swipe on its own?
- Does every content slide contain exactly one idea?
- Do all stat slides show source and year on the slide itself?
- Is the CTA slide free of any live URL?
- Does the synthesis slide connect the content into one memorable conclusion?

OUTPUT FORMAT:
CAROUSEL TYPE: [State the type chosen]

For each slide:
SLIDE [N] - [TYPE: Hook / Step X / Stat X / Myth X / Synthesis / CTA]
HEADLINE: [max 8 words]
BODY: [max 25 words]
VISUAL: [specific visual direction]

Then:
POST CAPTION:
CAPTION: [full caption text, under 300 characters]
FIRST COMMENT: [INSERT CTA LINK] + one-line CTA description

Save to: output/LinkedIn_Carousel/
"""


# ─────────────────────────────────────────────
# VIDEO SCRIPT TEMPLATE
# ─────────────────────────────────────────────
