from ._shared import (
    BANNED_CTA_PHRASES,
    HUMAN_WRITING_RULES,
    RESEARCH_RULES,
    market_voice,
)

_BANNED_CTA_LIST = ", ".join(f'"{p}"' for p in BANNED_CTA_PHRASES)


def positioning_statement(brand, product, category, differentiator, audience, market=None, **_):
    return f"""You are a product marketing strategist who has built positioning for B2B SaaS, professional services, and consumer products, and who knows that a positioning statement is an internal alignment tool - not marketing copy - that makes every downstream asset faster and more consistent to produce.

TASK:
Write a complete positioning statement and messaging foundation for:

BRAND: {brand}
PRODUCT: {product}
CATEGORY: {category}
PRIMARY DIFFERENTIATOR: {differentiator}
TARGET AUDIENCE: {audience}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. What does {audience} currently use or do instead of {product}? That alternative is the real competitive frame, not the named competitors.
2. Does "{differentiator}" describe what {product} does differently, or just what it claims to be? If it sounds like something two competitors could both claim, it needs to be more specific.
3. What is the one thing {audience} believes about {category} right now that {product}'s positioning needs to change or reinforce?

2025 PRODUCT POSITIONING CONTEXT:
- 95% of newly launched products fail commercially - most because positioning is vague, not because the product is bad (Harvard Business School study cited in SHNO 2024)
- Positioning before tactics is the highest-leverage step: every downstream asset - the landing page headline, the email subject line, the sales pitch - is easier when the positioning is locked first
- A positioning statement is not a tagline: it is a structured logical argument for why {audience} should choose {product} over the alternative
- The "frame of reference" (the category) is the single most powerful positioning lever: it determines what {product} is compared to

POSITIONING STATEMENT (write all five components):

COMPONENT 1 - FRAME OF REFERENCE:
- The category {product} belongs to, stated from {audience}'s perspective - not the internal category {brand} wishes it occupied
- One sentence: "For {audience}, {product} is a [category {audience} already understands]"
- If {product} is creating a new category, name the old category it replaces and the reason the new frame is necessary

COMPONENT 2 - TARGET CUSTOMER DEFINITION:
- Who specifically within {audience} benefits most from {product}
- Named by role, situation, or behavior - not demographic
- One sentence: "[Role/persona] who [specific situation or behavior that makes them the ideal buyer]"
- If there are two buyer personas (e.g. economic buyer and end user), define both and note where their motivations differ

COMPONENT 3 - POINT OF DIFFERENCE:
- The one thing {product} does that the current alternative cannot - anchored to "{differentiator}"
- Must pass the "could a competitor claim this too?" test: if yes, it is not a point of difference, it is table stakes
- One sentence naming the capability or outcome, not just the feature: "[Product] is the only [category] that [specific capability or outcome that is genuinely unique]"

COMPONENT 4 - REASON TO BELIEVE:
- The evidence that makes the point of difference credible rather than a claim
- Choose from: a named case study metric, a proprietary mechanism, a third-party validation, or a customer outcome data point
- One to two sentences: specific enough that a skeptical buyer could verify it

COMPONENT 5 - FULL POSITIONING STATEMENT (assembled):
Write the complete statement in the classic Geoffrey Moore format, then rewrite it in plain language for internal team use:

MOORE FORMAT: "For [target customer], [product name] is the [frame of reference] that [point of difference], because [reason to believe]."

PLAIN LANGUAGE VERSION (2-3 sentences): The same argument, written as a product marketer would explain it to a new sales hire on their first day - no jargon, no marketing speak, just the honest case for why {audience} should pick {product}.

BONUS - 3 THINGS THIS POSITIONING RULES OUT:
Name three things {product} is NOT - adjacent claims or audiences that the positioning explicitly excludes. This sharpens the positioning and prevents internal scope creep.

TECHNICAL REQUIREMENTS:
- No em dashes - hyphens only
- The point of difference must be specific enough to fail if the differentiator changes - if it still works after removing "{differentiator}", it is not anchored to the actual differentiator
- Banned phrases: {_BANNED_CTA_LIST}

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the frame of reference name the category {audience} would use, not the category {brand} aspires to?
- Does the point of difference pass the "could a competitor claim this too?" test - if yes, rewrite it?
- Is the reason to believe specific enough to be verifiable by a skeptical buyer?
- Does the plain language version of the statement sound like a person speaking, not a committee document?
- Are there zero em dashes anywhere in the output?

OUTPUT FORMAT:
Write each component under its label. Deliver the Moore-format statement and the plain language version clearly separated. Then the 3 exclusions block.

Save to: output/Product/Positioning/
"""


def launch_announcement(product, key_benefit, cta, channel, market=None, **_):
    return f"""You are a product marketing writer who has crafted launch announcements across email, social, and press for B2B SaaS and consumer products, and who knows that the launch announcement is the highest-stakes copy in the entire launch campaign because it sets the frame for all coverage and conversation that follows.

TASK:
Write a launch announcement for: "{product}"

KEY BENEFIT: {key_benefit}
CALL TO ACTION: {cta}
CHANNEL: {channel}  (email / social / press)

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. Why does "{product}" matter RIGHT NOW - what has changed in the market, in the audience's situation, or in the competitive landscape that makes this the right moment to launch?
2. What is the one sentence a journalist, a prospect, or a colleague would use to describe this launch to someone else? That sentence is the headline.
3. What does {cta} ask the reader to do, and what do they get in the next 60 seconds after clicking?

2025 LAUNCH ANNOUNCEMENT CONTEXT:
- 26% of total product sales occur within the first 90 days of launch - the announcement window is the highest-leverage moment (SHNO 2024 benchmark report)
- The channels require genuinely different copy: a press release is written for a journalist who will rewrite it; an email is written for an existing customer or subscriber who trusts the sender; a social post is written for a stranger who scrolls past in 2 seconds
- Message match between the announcement and any ad or email that preceded it is a primary conversion driver - use the same headline language across the funnel so readers feel continuity, not confusion

CHANNEL-SPECIFIC ANNOUNCEMENT:

--- EMAIL ANNOUNCEMENT ---
(Write this section only if channel is "email" or all channels are requested)

SUBJECT LINE (3 variants - each using a different pattern):
- VARIANT A: Outcome-led - names what the reader gets, not what the product is
- VARIANT B: Curiosity gap - states a specific contrast or before/after without giving away the full answer
- VARIANT C: Direct announcement - names the product and its primary use case plainly ("Introducing [product]: [one-line use case]")
- Each subject line: 40-55 characters, no ALL CAPS, no exclamation point in A or C

PREVIEW TEXT (1 line, 80-100 characters): Complements the subject line without repeating it - adds the specific detail the subject line withheld

EMAIL BODY:
- OPENING (1-2 sentences): Lead with the problem this solves or the change it enables - NOT "We're excited to announce"
- WHAT IT IS (2-3 sentences): Name {product}, explain the mechanism, name {key_benefit} in outcome language
- WHO IT'S FOR (1-2 sentences): Self-selection line - who gets the most value, stated by situation not demographic
- PROOF (1-2 sentences): One early-access customer result, a beta metric, or a named use case - real and specific
- CTA: "{cta}" - one button, one destination - [INSERT CTA LINK]
- MICROCOPY below CTA: one friction-reducing line (e.g. "No setup required." / "Free 14-day trial." / "Invite your team instantly.")

--- SOCIAL ANNOUNCEMENT ---
(Write this section only if channel is "social" or all channels are requested)

Adapt the announcement for each of these two platforms (write both):

LINKEDIN POST:
- LINE 1 (hook, visible before "see more"): A specific claim or contrarian statement - not "I'm excited to share" or "We're thrilled to announce"
- BODY (80-120 words): What it is, who it's for, the one result that proves it works - no feature list
- CTA: "{cta}" - with the destination URL noted as "Link in comments" (LinkedIn suppresses posts with outbound links in the body)
- HASHTAGS: 3-5, last line, lowercase

X / TWITTER POST (single tweet, not a thread):
- 240 characters maximum
- Lead with the outcome or proof, name the product, end with {cta} or a thread signal if space requires a thread
- No more than 1 emoji

--- PRESS RELEASE ---
(Write this section only if channel is "press" or all channels are requested)

HEADLINE: One declarative sentence naming {product} and its primary outcome - written for a journalist who will rewrite it, so factual and specific beats clever
DATELINE: [CITY, DATE] -
LEAD PARAGRAPH (1-2 sentences): The who, what, and why this matters now - the complete story in two sentences
BODY (2-3 paragraphs): Expands the lead with the problem context, how {product} addresses it, and one supporting data point or quote from a named internal spokesperson
BOILERPLATE: One paragraph describing {product}'s company (placeholder if not provided)
MEDIA CONTACT: [INSERT: media contact name, email, phone]

TECHNICAL REQUIREMENTS:
- No em dashes - hyphens only
- No passive voice in headlines or subject lines
- Banned CTA phrases: {_BANNED_CTA_LIST}
- CTA destination: [INSERT CTA LINK] placeholder - never fabricate a URL

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the email opening avoid "We're excited/thrilled/proud to announce"?
- Are the 3 subject line variants structurally different - not the same pattern reworded?
- Does the LinkedIn hook work as a standalone line before the "see more" cut?
- Is the press release lead paragraph a complete story in 1-2 sentences that a journalist could use directly?
- Are there zero em dashes anywhere?

OUTPUT FORMAT:
Write only the sections for the requested channel. If channel is not specified, write all three. Label each section clearly (EMAIL ANNOUNCEMENT, SOCIAL ANNOUNCEMENT - LINKEDIN, SOCIAL ANNOUNCEMENT - X, PRESS RELEASE).

Save to: output/Product/LaunchAnnouncement/
"""


def pre_launch_teaser(product, launch_date, hook, cta, market=None, **_):
    return f"""You are a product marketing writer who builds pre-launch teaser campaigns, and who knows that the pre-launch window is the highest-leverage moment to build demand signal, shape expectations, and earn media attention before a single feature is shipped.

TASK:
Write a complete pre-launch teaser campaign for: "{product}"

LAUNCH DATE: {launch_date}
HOOK (the tension or problem the product resolves): {hook}
CTA: {cta}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. What is the one thing the target audience currently believes about {hook} that {product} is going to challenge, contradict, or resolve? That belief is the center of gravity for the teaser campaign.
2. What is the minimum amount of information needed to get the right audience to take {cta} action - and what information must be withheld to preserve launch-day impact?
3. Why does {launch_date} matter as a specific date - is there a market event, a seasonal moment, or a competitive trigger that makes the timing meaningful? If yes, name it. If not, create internal urgency around the waitlist or early access instead.

2025 PRE-LAUNCH CONTEXT:
- Notion AI generated 1 million waitlist signups before general availability by anchoring their pre-launch on a single, clear positioning message ("AI that works inside your existing workspace, not beside it") repeated consistently across every teaser touchpoint
- The pre-launch period is for positioning, not feature revelation - revealing features pre-launch cannibalizes launch-day coverage and gives competitors time to respond
- A waitlist or early-access CTA converts better than a generic "coming soon" page because it gives the audience a specific action that creates commitment and self-selection

PRE-LAUNCH CAMPAIGN DELIVERABLES (write all four):

DELIVERABLE 1 - TEASER HEADLINE + SUBHEADLINE (for a holding page or social card):
- HEADLINE: Names the problem {hook} represents or the outcome {product} produces - not the product name
- Approach: "The [specific problem] ends on [launch_date]." OR "[Outcome] - finally." OR "[Specific result] without [the thing they hate about current alternatives]."
- Do NOT name {product} in the teaser headline if naming it reduces curiosity
- SUBHEADLINE (1-2 sentences): Adds just enough context to earn the {cta} action without giving away the full product story

DELIVERABLE 2 - WAITLIST / EARLY ACCESS PAGE COPY:
- ABOVE THE FOLD: Teaser headline + subheadline (from Deliverable 1) + CTA form
- FORM FIELDS: Name and email only - maximum 2 fields
- CTA BUTTON LABEL: Names what early access participants get, not just "Sign Up" (e.g. "Get Early Access" / "Join the Waitlist" / "Reserve My Spot")
- BELOW FORM: One proof line establishing credibility without naming the full product (e.g. number of beta users, a named early-access partner, a specific result from beta testing)
- MICROCOPY below the button: one line explaining what happens after they sign up and when (e.g. "You'll get an invitation on [launch_date]. No spam before then.")

DELIVERABLE 3 - TEASER SOCIAL POSTS (write one for each platform):

LINKEDIN TEASER POST:
- Open with the problem or tension from {hook} - no product name in the first paragraph
- Reveal that something is changing on {launch_date} without naming what
- End with a specific question that invites comments from the exact audience who has this problem
- CTA line: "{cta}" - with "Link in comments"
- 100-150 words, plain text, no em dashes

X / TWITTER TEASER (single tweet):
- 240 characters maximum
- State the tension from {hook} and the date - tease without revealing
- One emoji maximum

DELIVERABLE 4 - PRE-LAUNCH EMAIL (to existing subscribers or a relevant list):
- SUBJECT LINE: Creates urgency around the problem {hook} names, not around the product
- PREVIEW TEXT: Adds the date or a specific tease that rewards opening
- OPENING (1-2 sentences): Names the problem {hook} represents - in the words of someone who has lived it, not a brand describing it from the outside
- BRIDGE (2-3 sentences): Something is changing. On {launch_date}, the way [audience] handles [hook problem] changes. No further detail yet.
- CTA: "{cta}" - [INSERT CTA LINK]
- SIGN-OFF: First-name sign-off from a named person at the brand, not "The [Brand] Team"

TECHNICAL REQUIREMENTS:
- No em dashes - hyphens only
- {product} name may be withheld in teasers if naming it reduces curiosity - use "[PRODUCT NAME]" as a placeholder in that case
- No feature reveals in the teaser campaign - save those for launch day
- Banned phrases: {_BANNED_CTA_LIST}

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the teaser headline name the problem or outcome without naming the product?
- Does the early-access form have 2 fields maximum?
- Do the social posts build tension without revealing what the product actually does?
- Does the pre-launch email close without a "We're excited to announce" opener?
- Is the {launch_date} used as a specific anchor in at least two of the four deliverables?
- Are there zero em dashes anywhere?

OUTPUT FORMAT:
Write each deliverable under its label. Include all sub-elements (headline, copy, button labels, microcopy) exactly as they would appear in production. Use [INSERT CTA LINK] for all destination URLs.

Save to: output/Product/PreLaunchTeaser/
"""


def messaging_hierarchy(product, primary_message, supporting_points, proof_point, market=None, **_):
    return f"""You are a product marketing strategist who builds messaging hierarchies for product teams, and who knows that a messaging hierarchy is the master document that aligns sales, marketing, and product on a single version of why {product} exists and what it does for buyers.

TASK:
Build a complete messaging hierarchy for: "{product}"

PRIMARY MESSAGE: {primary_message}
SUPPORTING POINTS: {supporting_points}
PROOF POINT: {proof_point}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. Does "{primary_message}" describe what {product} does, or what it means for the buyer? Reframe as buyer outcome if needed.
2. Are the supporting points in "{supporting_points}" reasons-to-believe or product features? Convert any features to buyer outcomes before building the hierarchy.
3. Does "{proof_point}" pass the specificity test - would a skeptical buyer accept it as evidence, or would they dismiss it as a marketing claim?

2025 MESSAGING HIERARCHY CONTEXT:
- Companies with a structured launch process see 10% higher success rates and 3x greater revenue growth versus ad-hoc approaches (PDMA Global Best Practices Research, 2021)
- The messaging hierarchy is upstream of every asset - the landing page headline, the sales deck, the email subject line all derive from it, so vague primary messages produce inconsistent downstream copy
- Positioning before tactics: the messaging hierarchy is the translation layer between the positioning statement (internal strategic logic) and the copywriter's brief (channel-specific execution)

MESSAGING HIERARCHY (write all five levels in full):

LEVEL 1 - PRIMARY MESSAGE (the elevator pitch):
- The single sentence that wins the 30-second version of the sales conversation
- Anchored to "{primary_message}" - rewritten in outcome language if the input is feature-oriented
- Must work spoken aloud by a sales rep, written in a tweet, and placed as a landing page headline without any other context
- Format: "[Product] [does specific thing] for [audience], so [specific outcome]."

LEVEL 2 - VALUE PILLARS (3 pillars derived from "{supporting_points}"):
Write each pillar as a named, self-contained value argument:
- PILLAR NAME: 2-4 words, the outcome category (e.g. "Time to First Result", "Predictable Pipeline", "Zero Configuration")
- PILLAR STATEMENT: 1 sentence - the buyer outcome this pillar delivers
- SUPPORTING EVIDENCE: 1-2 sentences - the mechanism, feature, or data that makes the pillar credible
- TALK TRACK SEED: 1 sentence - how a sales rep would introduce this pillar in a discovery call

LEVEL 3 - PROOF POINTS (3 proof points, anchored to "{proof_point}"):
For each proof point:
- TYPE: case study / stat / guarantee / named outcome
- STATEMENT: the proof, stated with specificity (named company or attributed source, specific number, specific timeframe)
- PLACEMENT: where in the funnel this proof point lands hardest (e.g. "place in landing page above CTA", "use in sales deck objection slide", "use in retention email")
- Note: if "{proof_point}" is a single input, expand it into 3 distinct proof expressions (e.g. a customer quote, a usage metric, and a third-party validation) rather than repeating the same evidence three times

LEVEL 4 - OBJECTION RESPONSES (3 common objections with scripted responses):
For each objection:
- OBJECTION: The actual words a buyer would use when raising it
- RESPONSE (2-3 sentences): Direct, honest, specific - not defensive
- BRIDGE: one sentence that transitions from the objection response back to a pillar or proof point

LEVEL 5 - CHANNEL TRANSLATIONS (how the primary message adapts to each surface):
- SALES CALL OPENER (1 sentence): How a rep states the primary message as an opening question or statement in discovery
- LANDING PAGE HEADLINE (8-10 words): Outcome-first, audience-specific
- EMAIL SUBJECT LINE (40-55 characters): Named result or specific tension - not the product name
- LINKEDIN ONE-LINER (under 210 characters): The hook line, plain text, no emoji
- AD HEADLINE (25-30 characters): Scannable in 2 seconds

TECHNICAL REQUIREMENTS:
- No em dashes - hyphens only
- Every pillar statement and proof point must be specific enough that removing the product name leaves the statement meaningless - vague claims that could belong to any product are not acceptable
- Banned phrases: {_BANNED_CTA_LIST}

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the Level 1 primary message work as a landing page headline without any other context?
- Do the 3 value pillars each name a distinct buyer outcome - not three versions of the same benefit?
- Is every Level 3 proof point specific enough to be verifiable - named source, number, timeframe?
- Do the Level 4 objection responses sound like a senior rep speaking, not a marketing FAQ?
- Does the Level 5 email subject line avoid the product name and lead with outcome or tension instead?
- Are there zero em dashes anywhere?

OUTPUT FORMAT:
Write each level under its label with all sub-elements. The Level 5 channel translations should each be on their own clearly labeled line with character counts shown.

Save to: output/Product/MessagingHierarchy/
"""


def launch_email_sequence(product, benefit, cta_url, market=None, **_):
    return f"""You are an email marketing strategist who writes product launch sequences that move a cold or warm subscriber from "curious" to "converted" across 3 emails without burning the list.

TASK:
Write a 3-email launch sequence for: "{product}"

PRIMARY BENEFIT: {benefit}
CTA URL: {cta_url}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. Who is this sequence going to - existing customers, warm leads, or a cold audience? Each requires a different opening tone. (Default to warm leads if not specified.)
2. What is the single most likely reason a subscriber who opens all 3 emails still does not convert - price, trust, timing, or relevance? That objection drives the structure of Email 3.
3. What does each email add that the previous email did not - if any email could be cut without reducing conversions, it should be cut.

2025 EMAIL LAUNCH SEQUENCE CONTEXT:
- 26% of total product sales occur within the first 90 days of launch (SHNO 2024) - the email sequence is the primary driver of that early revenue window
- Multi-email sequences outperform single announcement emails on conversion, but only if each email delivers new value - a sequence that repeats the same message in different words destroys trust faster than silence
- Subject line open rates determine whether the sequence works at all - each email needs a distinct subject line that earns the open on its own, without relying on the previous email to set it up

3-EMAIL SEQUENCE STRUCTURE:

EMAIL 1 - THE ANNOUNCEMENT (Launch Day or Day 1):
GOAL: Awareness + first-click intent from the highest-intent subscribers

SUBJECT LINE (3 variants, each structurally different):
- VARIANT A: Outcome-led (what the reader gains, not what the product is)
- VARIANT B: Named tension or problem ({benefit} framed as resolution to a specific frustration)
- VARIANT C: Direct and plain ("Introducing [product]: [one-line use case]")
- Each: 40-55 characters, no exclamation point in A or C, no ALL CAPS

PREVIEW TEXT: 80-100 characters, adds specific detail the subject line withheld

EMAIL BODY:
- OPENING: 1-2 sentences naming the problem {benefit} solves - not "We're excited to announce"
- WHAT IT IS: 2-3 sentences, {product} in plain language with {benefit} in outcome terms
- PROOF: 1 concrete early result from a beta user or an internal data point - specific, attributed, real
- CTA: One button: "{cta_url}" - label names what the reader gets when they click (e.g. "See [product] in action" / "Start your free trial")
- SEND TIMING: Launch day

EMAIL 2 - THE PROOF EMAIL (Day 3-5):
GOAL: Convert readers who opened Email 1 but did not click - add a new layer of evidence

SUBJECT LINE (1 final variant, different from all Email 1 options):
- Opens with a specific customer result or a specific use case, not a restatement of the product name
- Example frame: "How [customer type] used [product] to [specific result]"
- 40-55 characters

PREVIEW TEXT: 80-100 characters

EMAIL BODY:
- OPENING: Lead with the proof, not the product - "Here's what happened when [customer type] used {product} for the first time"
- CASE STUDY OR USE CASE (2-3 sentences): Specific scenario - who used it, what they did, what happened - named or described precisely enough to be credible
- FEATURE SPOTLIGHT (1 brief mention): The one feature of {product} that made the result in the case study possible - named and explained in 2 sentences
- SECONDARY CTA: Same destination as Email 1 ({cta_url}) but with a different label that matches the proof in this email
- SEND TIMING: Day 3-5 post-launch

EMAIL 3 - THE CLOSE (Day 7-10):
GOAL: Convert fence-sitters by removing the final objection - this email handles the single biggest hesitation for a reader who has opened Emails 1 and 2 but still has not converted

SUBJECT LINE (distinct from all prior options):
- Acknowledges the reader's inaction without guilt-tripping
- Frame: "Still deciding on [product]? Here's the one thing to know." OR names the specific objection directly: "Is [product] right for [audience type]?"
- 40-55 characters

PREVIEW TEXT: 80-100 characters

EMAIL BODY:
- OPENING: Acknowledge that the reader has seen the emails and may have a specific hesitation - address them directly, not as a broadcast
- OBJECTION RESPONSE (2-3 sentences): The most common hesitation for a reader at this stage, answered honestly and specifically
- SOCIAL PROOF ANCHOR: A second customer result, different from Email 2 - anchored to a different use case to cover a different buyer persona
- RISK REMOVAL: Guarantee, free trial terms, or cancellation policy - stated plainly
- FINAL CTA: Same {cta_url} - button label that closes with the risk-removal language (e.g. "Start free - cancel anytime" / "Get access, risk-free")
- SEND TIMING: Day 7-10 post-launch

SEQUENCE-LEVEL RULES:
- No two emails may share the same subject line pattern or CTA button label
- Each email must add genuinely new information - no email should be cuttable without reducing the conversion argument
- Unsubscribe link must be referenced in the footer of each email as "[INSERT: unsubscribe link]"
- Do NOT fabricate case study results - use "[INSERT: customer name and result]" as a placeholder if a real example is not available

TECHNICAL REQUIREMENTS:
- No em dashes - hyphens only
- All CTA destinations: {cta_url} (use this exact URL, do not fabricate variants)
- Email body length: 150-250 words per email - short enough to read in full, long enough to make the argument
- Banned phrases in subject lines, button labels, and body copy: {_BANNED_CTA_LIST}

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Do all 4 subject line options (across the 3 emails) use structurally different patterns?
- Does Email 2 add a new layer of proof not present in Email 1?
- Does Email 3 name and directly answer the most likely remaining objection for a non-converter?
- Are all CTA button labels different across the 3 emails?
- Is any case study or proof point a placeholder ([INSERT ...]) rather than a fabricated statistic?
- Are there zero em dashes anywhere?

OUTPUT FORMAT:
Return a structured dict with keys "email_1", "email_2", "email_3". Each value is a dict with keys: "subject_variants" (list), "preview_text", "body", "cta_label", "send_timing". Write the dict as clearly labeled Python-style output showing all fields.

Save to: output/Product/LaunchEmailSequence/
"""
