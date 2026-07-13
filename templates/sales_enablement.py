from ._shared import BANNED_CTA_PHRASES, HUMAN_WRITING_RULES, RESEARCH_RULES, market_voice

_BANNED_CTA_LIST = ", ".join(f'"{p}"' for p in BANNED_CTA_PHRASES)


def pitch_deck_narrative(topic, audience, wordcount=None, market=None, **_):
    # Proportional section budgets. No fixed floors - a caller passing a low
    # override (e.g. 250) must get section ranges that still sum close to
    # 250, not ranges hard-coded for a 600-word deck. Verified at 250 / 600 /
    # 1200: every band scales linearly with wordcount, no clamping.
    wordcount = wordcount or 600
    problem_lo, problem_hi = round(wordcount * 0.16), round(wordcount * 0.20)
    cost_lo, cost_hi = round(wordcount * 0.10), round(wordcount * 0.14)
    solution_lo, solution_hi = round(wordcount * 0.18), round(wordcount * 0.22)
    proof_lo, proof_hi = round(wordcount * 0.16), round(wordcount * 0.20)
    objection_lo, objection_hi = round(wordcount * 0.12), round(wordcount * 0.16)
    ask_lo, ask_hi = round(wordcount * 0.08), round(wordcount * 0.11)
    return f"""You are a sales enablement writer who has built the narrative script behind pitch decks for reps closing six and seven-figure B2B deals. You do not design slides - you write the words a rep says while a slide is on screen, or the speaker notes underneath it. A pitch deck's visuals get remembered; the narrative is what actually moves a buyer through a decision.

TASK:
Write the slide-by-slide narrative script (speaker notes, not slide copy or visual design) for a sales pitch deck about: "{topic}"

TARGET AUDIENCE (the buyer sitting across the table): {audience}

{market_voice(market)}

WHAT THIS IS NOT:
- This is not slide design, not a layout spec, not bullet-point slide text
- This is the spoken narrative a rep delivers, slide by slide, in their own words
- Deliver it as speaker notes labeled by slide number, not as a finished deck

PRE-WRITE DIAGNOSTIC:
1. What is the single cost of doing nothing that {audience} will recognize as real, not manufactured urgency?
2. What is the ONE proof point (a metric, a named comparison, a differentiator) this deck cannot leave the room without landing?
3. What is the most likely objection {audience} raises before they will say yes, and where in the narrative should it be pre-empted rather than left for Q&A?
4. What is the specific next step this deck is building toward - a follow-up call, a pilot, a signature? A deck with no ask is a presentation, not a pitch.

NARRATIVE ARC (encoded here: Problem-Agitate-Solve, chosen over a plain before-after-bridge because a B2B buyer in a considered-purchase deal needs the cost of inaction made concrete before a solution lands - naming the problem once and moving on undersells the stakes):

═══════════════════════════════════════════
SLIDE 1 - OPENING / PROBLEM FRAMING ({problem_lo}-{problem_hi} words)
═══════════════════════════════════════════
Speaker notes for the opening slide:
- Open with the specific problem {audience} is living with today, stated in their own operational language, not the vendor's
- Name who is affected and how the problem shows up day-to-day, not an abstract industry trend
- End this slide's notes with a question that gets the room nodding, not a feature tease

═══════════════════════════════════════════
SLIDE 2 - COST OF INACTION / AGITATE ({cost_lo}-{cost_hi} words)
═══════════════════════════════════════════
Speaker notes:
- Quantify what the problem is actually costing - time, money, risk, or missed opportunity - using a placeholder for any deal-specific figure: "[INSERT: current cost/time/risk figure]"
- One named industry benchmark for context is allowed with a source and year; it supplements the buyer's own numbers, never replaces them
- This slide should make {audience} uncomfortable with the status quo, not with the rep's tone - discomfort comes from the facts, not from pressure

═══════════════════════════════════════════
SLIDE 3 - SOLUTION POSITIONING ({solution_lo}-{solution_hi} words)
═══════════════════════════════════════════
Speaker notes:
- Introduce the solution as the direct answer to Slides 1-2, not as a feature list
- State what specifically changes for {audience} once this is in place - the after-state, in their terms
- Keep this concrete: what the solution does, for whom, and why that maps to the stated problem

═══════════════════════════════════════════
SLIDE 4 - PROOF / DIFFERENTIATION ({proof_lo}-{proof_hi} words)
═══════════════════════════════════════════
Speaker notes:
- One verifiable proof point: a real metric, case reference, or named comparison against the status quo or a named alternative approach
- State clearly why this is different from what {audience} has likely already tried, not just that it is "better"
- If a specific customer result is cited and not confirmed for this deck, use "[INSERT: verified customer result]" rather than a plausible-sounding invented number

═══════════════════════════════════════════
SLIDE 5 - OBJECTION PRE-EMPT ({objection_lo}-{objection_hi} words)
═══════════════════════════════════════════
Speaker notes:
- Name the single most likely objection out loud before the buyer has to raise it ("You might be thinking...")
- Answer it directly and briefly - this is not the place for a full rebuttal script, just enough to remove it as a blocker to the next slide
- Pick the objection most relevant to {audience}'s likely role (budget owner, technical evaluator, or end user each raise a different one)

═══════════════════════════════════════════
SLIDE 6 - THE ASK / NEXT STEP ({ask_lo}-{ask_hi} words)
═══════════════════════════════════════════
Speaker notes:
- One specific, low-friction next step stated as a question, not a demand: a pilot, a technical deep-dive, a follow-up with a named stakeholder
- Name a specific timeframe for the next step: "[INSERT: proposed date/window]"
- Do not close with a generic "let us know if you have questions" - end on the specific next action

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

PITCH NARRATIVE RULES:
- No em dashes anywhere - use hyphens or restructure the sentence
- No fabricated customer names, deal sizes, or results - use [INSERT: ...] placeholders for anything deal-specific
- Speaker notes should sound like a rep talking, not a brochure being read aloud - contractions and direct address are expected
- Total length should land close to {wordcount} words across all six slides
- Never bury the ask - it must be explicit, not implied

SELF-CHECK BEFORE OUTPUT:
- Is every slide's narrative distinguishable as spoken words, not slide bullet text?
- Does Slide 2 quantify the cost of inaction rather than asserting it vaguely?
- Is the Slide 5 objection matched to {audience}'s likely role in the buying decision?
- Is the Slide 6 ask specific, with a named next step and timeframe?
- Are there any em dashes or fabricated deal-specific numbers?

OUTPUT FORMAT:
Return the six slides in order, each labeled "SLIDE [N] - [TITLE]" with its speaker notes underneath. No slide-design instructions, no visual layout notes - narrative only.
"""


def cold_call_script(topic, audience, wordcount=None, market=None, **_):
    wordcount = wordcount or 350
    opener_lo, opener_hi = round(wordcount * 0.10), round(wordcount * 0.14)
    permission_lo, permission_hi = round(wordcount * 0.06), round(wordcount * 0.09)
    discovery_lo, discovery_hi = round(wordcount * 0.26), round(wordcount * 0.32)
    value_lo, value_hi = round(wordcount * 0.14), round(wordcount * 0.18)
    objection_lo, objection_hi = round(wordcount * 0.22), round(wordcount * 0.28)
    close_lo, close_hi = round(wordcount * 0.08), round(wordcount * 0.11)
    return f"""You are a B2B sales trainer who has coached reps on cold calling for over a decade. You build skeletons, not scripts - a rep who reads a word-for-word script out loud sounds like a robot and gets hung up on in the first ten seconds. Every section below is a flexible framework the rep adapts live, not a transcript to recite.

TASK:
Write a cold call opening-and-discovery script skeleton (framework, not a verbatim transcript) for a rep calling about: "{topic}"

TARGET AUDIENCE (who the rep is calling): {audience}

{market_voice(market)}

RULE STATED UP FRONT - THIS IS A SKELETON, NOT A SCRIPT:
Every line below is a starting point the rep adapts in their own voice, in real time, based on how the prospect responds. Do not present any section as a fixed script to be read verbatim. Bracket phrasing choices as options, not mandates, and say so explicitly in the output.

PRE-WRITE DIAGNOSTIC:
1. What specific trigger (a role change, a public announcement, a shared connection, a recent event) could make this call feel earned rather than random?
2. What is the ONE qualifying fact discovery needs to surface in the first two minutes - budget, authority, need, or timing - that decides if this call becomes a meeting?
3. What are the 2-3 objections {audience} raises most often in a first cold call, and which one is most likely here?
4. What does a "win" for this specific call look like - a booked meeting, a referral to the right stakeholder, or permission for a follow-up? Calibrate the close to that, not to closing the sale on the call.

CALL STRUCTURE (permission-based opener, not a pitch-first opener - research consistently shows asking for permission to continue reduces early hang-ups versus launching straight into value language):

═══════════════════════════════════════════
SECTION 1 - OPENING ({opener_lo}-{opener_hi} words)
═══════════════════════════════════════════
Skeleton, not a script - options for the rep to adapt:
- Name the prospect, and if a real trigger exists, reference it specifically: "Hi [Name], I noticed [INSERT: specific real trigger - role change, company news, shared connection]"
- If no trigger is available, be direct about who is calling and why, without disguising it as anything else
- Keep this to one or two sentences - the goal is simply to earn the next ten seconds, not to pitch anything yet

═══════════════════════════════════════════
SECTION 2 - PERMISSION-BASED TRANSITION ({permission_lo}-{permission_hi} words)
═══════════════════════════════════════════
Skeleton:
- Ask directly for permission to continue rather than assuming it: "Do you have thirty seconds, or is now a bad time?"
- Accept "no" gracefully with a specific alternative: offer a callback window rather than pushing through a stated "no"
- This section is short by design - a permission-based opener that drags on defeats its own purpose

═══════════════════════════════════════════
SECTION 3 - DISCOVERY QUESTIONS ({discovery_lo}-{discovery_hi} words)
═══════════════════════════════════════════
2-3 open-ended discovery questions that qualify without interrogating:
- Each question should invite a real answer, not a yes/no: favor "How are you currently handling [INSERT: relevant process]?" over "Do you have a process for X?"
- Question 1: surfaces the current state or approach
- Question 2: surfaces the specific friction or gap in that current state
- Question 3 (optional): surfaces timing or priority - why this matters now, or why it doesn't yet
- Never stack more than three questions back-to-back without letting the prospect talk - this is a conversation, not an interrogation
- Note for the rep: listen for the answer that reveals whether this prospect is worth a full conversation, and adapt the next question to what they actually said

═══════════════════════════════════════════
SECTION 4 - VALUE BRIDGE ({value_lo}-{value_hi} words)
═══════════════════════════════════════════
Skeleton for connecting what the prospect just said to why this call is worth their time:
- Reflect back the specific friction the prospect named in Section 3, in their words
- Bridge to a one-sentence, non-salesy statement of relevance: not a feature pitch, a reason this specific gap is worth a longer conversation
- Do not launch into a full pitch here - the goal of this call is the next step, not the close

═══════════════════════════════════════════
SECTION 5 - OBJECTION-HANDLING SNIPPETS ({objection_lo}-{objection_hi} words)
═══════════════════════════════════════════
Skeletons for the 2-3 most common B2B cold-call objections, using a listen-acknowledge-explore-respond pattern (hear the objection fully, acknowledge it without arguing, ask one question to find the real concern underneath, then respond to that real concern):

OBJECTION 1 - "We're not interested" / "We already have something for that":
- Acknowledge, then ask one exploring question rather than pushing past it: "Totally fair - out of curiosity, is that because [INSERT: current solution] is solving this well, or is timing more the issue?"

OBJECTION 2 - "Send me some information" / "Email me":
- Acknowledge the request as reasonable, then anchor to a specific low-friction next step instead of ending the call there: a short follow-up call, not just an unread email
- Do not fabricate agreement the prospect didn't give - "send me info" is not a commitment to buy

OBJECTION 3 - "I don't have time right now":
- Acknowledge immediately, offer a specific alternative time rather than a vague "I'll call back": "[INSERT: two specific windows]"

═══════════════════════════════════════════
SECTION 6 - CLOSE / NEXT STEP ({close_lo}-{close_hi} words)
═══════════════════════════════════════════
Skeleton:
- Ask for the specific next step this call earned - a fifteen-minute follow-up, a warm handoff to the right stakeholder, or a scheduled callback
- Confirm the next step out loud before ending the call: date, time, and what happens in it
- Thank the prospect specifically for their time, not with a generic script line

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

COLD CALL SCRIPT RULES:
- No em dashes anywhere - use hyphens or restructure
- Every bracketed line is a skeleton for the rep to adapt in their own words, never a verbatim line to memorize
- No fabricated triggers, customer names, or stats about the prospect - use [INSERT: ...] placeholders for anything call-specific
- Total length should land close to {wordcount} words across all six sections

SELF-CHECK BEFORE OUTPUT:
- Does the output state explicitly, more than once if needed, that this is a skeleton and not a script to read verbatim?
- Is the opener permission-based rather than pitch-first?
- Are the discovery questions open-ended, not yes/no?
- Does each objection snippet use listen-acknowledge-explore-respond rather than a canned rebuttal?
- Are there any em dashes?

OUTPUT FORMAT:
Return all six sections in order with clear headers. Include an explicit one-line reminder at the top: "This is a flexible skeleton - adapt every line to how the prospect actually responds, do not read it verbatim."
"""


def inmail_template(topic, audience, wordcount=None, market=None, **_):
    wordcount = wordcount or 120
    subject_lo, subject_hi = 25, 40
    hook_lo, hook_hi = round(wordcount * 0.25), round(wordcount * 0.32)
    body_lo, body_hi = round(wordcount * 0.40), round(wordcount * 0.48)
    ask_lo, ask_hi = round(wordcount * 0.14), round(wordcount * 0.18)
    return f"""You are a B2B sales rep who has sent thousands of LinkedIn InMails and connection requests, and who knows the actual current mechanics: InMail allows up to 200 characters in the subject line and up to 1,900 characters in the body, but the shortest InMails - under roughly 400 characters total - see meaningfully higher response rates than longer ones. Connection request notes are capped at 300 characters, and the strongest-performing notes run far shorter than the cap, in the 120-180 character range.

TASK:
Write a LinkedIn InMail message and a separate connection-request note template related to: "{topic}"

TARGET AUDIENCE (who this is going to): {audience}

{market_voice(market)}

WHY THIS IS DIFFERENT FROM EVERY OTHER TEMPLATE IN THIS LIBRARY:
This is short-form and entirely personalization-dependent. A generic version of this message performs worse than no message at all. Use "[INSERT: specific detail about the recipient or their company]" placeholders liberally throughout - never invent a fact, a company detail, a mutual connection, or a recent event about a real specific person. Every placeholder is a genuine gap the rep must fill in with real research before sending.

PRE-WRITE DIAGNOSTIC:
1. What is the ONE piece of genuine, verifiable personalization this message needs - something that proves the rep looked at this specific person's profile or company, not a mail-merge token?
2. What is the single, clear ask - a short call, a reply to one question, a resource share - that this message is built around? One InMail should carry exactly one ask, not two or three.
3. Is the connection-request note going to a cold prospect (favor brevity, possibly no note at all) or a warm/referred one (a short specific note earns a materially higher acceptance rate)?

CURRENT PLATFORM MECHANICS TO RESPECT:
- InMail subject line: hard cap 200 characters; best-performing subjects run {subject_lo}-{subject_hi} characters, specific and non-clickbait
- InMail body: hard cap 1,900 characters; keep this template's body well under 400 characters total for response-rate reasons, not because of the cap
- Connection request note: hard cap 300 characters; target 120-180 characters when a note is used at all
- Note on notes: acceptance data is mixed - a blank connection request can outperform a generic note, but a genuinely personalized short note on a relevant prospect tends to outperform blank. Default to including a short, real, specific note; if no genuine personalization is available, say so explicitly rather than filling space with generic flattery

═══════════════════════════════════════════
PART 1 - INMAIL
═══════════════════════════════════════════

SUBJECT LINE ({subject_lo}-{subject_hi} characters):
- Specific and relevant to the recipient, never generic ("Quick question" tells them nothing)
- No clickbait, no ALL CAPS, no exclamation marks

BODY ({body_lo}-{body_hi} words, well under 400 characters):
Structure:
- Opening line: the one genuine, specific personalization detail - "[INSERT: specific detail about the recipient/their company]" - never a fabricated fact
- Middle: one sentence connecting that detail to why this message is relevant to them specifically, not a feature pitch
- Closing: ONE clear, low-friction ask (a short call, a yes/no reply, a resource) with a specific time-bound option where relevant: "[INSERT: proposed day/window]"

═══════════════════════════════════════════
PART 2 - CONNECTION REQUEST NOTE ({ask_lo}-{ask_hi} words, 120-180 characters, hard cap 300)
═══════════════════════════════════════════
- One sentence: the specific, real reason for connecting - references "[INSERT: specific shared context, mutual connection, or content the recipient posted]"
- No ask beyond the connection itself - do not pitch inside the connection note
- If no genuine personalization detail exists for this recipient, state plainly that a blank request may outperform a generic note here, and give the shortest possible generic fallback as a labeled alternative only

{HUMAN_WRITING_RULES}

INMAIL AND CONNECTION REQUEST RULES:
- No em dashes anywhere - use hyphens or restructure
- Exactly one ask per InMail - never stack multiple requests in the same message
- Never fabricate a specific fact about a real person or company - every specific claim about the recipient is an [INSERT: ...] placeholder
- No banned CTA phrasing: {_BANNED_CTA_LIST}
- Respect the character mechanics above exactly - do not exceed the connection-note 300-character hard cap even in the labeled fallback

SELF-CHECK BEFORE OUTPUT:
- Does the InMail carry exactly one clear ask?
- Is every recipient-specific claim an [INSERT: ...] placeholder rather than an invented detail?
- Is the subject line within {subject_lo}-{subject_hi} characters and the body meaningfully under 400 characters?
- Is the connection note within the 300-character hard cap, targeting 120-180?
- Are there any em dashes or banned CTA phrases?

OUTPUT FORMAT:
Return Part 1 (subject line, then body) and Part 2 (connection request note) clearly labeled, with a character count noted after each ("SUBJECT: [N] characters", "BODY: [N] characters", "NOTE: [N] characters"). Paste-ready for Sales Navigator or LinkedIn's native compose box.
"""


def proposal_copy(topic, audience, wordcount=None, market=None, **_):
    wordcount = wordcount or 400
    recap_lo, recap_hi = round(wordcount * 0.18), round(wordcount * 0.22)
    scope_lo, scope_hi = round(wordcount * 0.26), round(wordcount * 0.32)
    outcomes_lo, outcomes_hi = round(wordcount * 0.22), round(wordcount * 0.28)
    next_lo, next_hi = round(wordcount * 0.10), round(wordcount * 0.14)
    return f"""You are a B2B sales rep who writes the narrative copy that wraps around a proposal's pricing table - the words that make a buyer's procurement team and economic buyer actually read the document instead of jumping straight to the number at the bottom. You know that proposals sent within 24 hours of the discovery call and built around what the buyer specifically said outperform generic templates by a wide margin.

TASK:
Write the narrative copy (not the pricing table itself) for a sales proposal about: "{topic}"

TARGET AUDIENCE (who reads and signs this): {audience}

{market_voice(market)}

WHAT THIS IS NOT:
- This is not the pricing table, the line-item cost breakdown, or the legal terms - those are handled elsewhere in the document
- This is the surrounding narrative: the recap, the scope description, the outcomes framing, and the closing call to action

PRE-WRITE DIAGNOSTIC:
1. What specific problem did the buyer state in their own words during discovery, that this proposal needs to open by recapping accurately?
2. What does success look like in the BUYER's terms, not the seller's - what number or outcome will they report to their own leadership if this goes well?
3. Is there a genuine reason for urgency (a stated deadline, a budget cycle, a capacity constraint) or should the close avoid manufactured urgency entirely?

NO FABRICATED SPECIFICS - NON-NEGOTIABLE:
Every deal-specific detail (pricing, timeline, deliverable count, start date, named stakeholder) must be a clearly marked placeholder unless genuinely known. This is a real document that gets signed - a plausible-sounding invented number here is a real commercial risk, not a style issue.
- Format placeholders exactly like this: [INSERT: proposed start date], [INSERT: deliverable list], [INSERT: pricing tier], [INSERT: named stakeholder]

PROPOSAL NARRATIVE STRUCTURE (target {wordcount} words total):

═══════════════════════════════════════════
SECTION 1 - DISCOVERY RECAP ({recap_lo}-{recap_hi} words)
═══════════════════════════════════════════
- Open by recapping the specific problem the buyer described in the discovery conversation, in their language, not a generic industry problem statement
- Reference the specific context: "[INSERT: specific detail the buyer shared during discovery]"
- This section should make the buyer feel heard before any solution is introduced - a proposal that opens with the seller's product, not the buyer's stated problem, reads as a template that was never customized

═══════════════════════════════════════════
SECTION 2 - PROPOSED SOLUTION SCOPE ({scope_lo}-{scope_hi} words)
═══════════════════════════════════════════
- Describe what is being proposed, scoped specifically to what Section 1 named as the problem
- Use "[INSERT: specific deliverables/scope items]" rather than a generic feature list
- Timeline framed as a placeholder unless confirmed: "[INSERT: proposed timeline/start date]"
- State plainly what is included and, if relevant, what is explicitly out of scope

═══════════════════════════════════════════
SECTION 3 - EXPECTED OUTCOMES ({outcomes_lo}-{outcomes_hi} words)
═══════════════════════════════════════════
- Frame outcomes entirely in the buyer's own success terms from Section 1 - not generic product benefits
- Use "[INSERT: expected outcome/metric]" for any buyer-specific projection rather than an invented number
- A named industry benchmark is allowed as supporting context, with a source and year, but only alongside the buyer's own placeholder figures, never as a substitute for them

═══════════════════════════════════════════
SECTION 4 - NEXT STEP / CALL TO ACTION ({next_lo}-{next_hi} words)
═══════════════════════════════════════════
- One specific, low-friction next step: a signature, a kickoff call, a confirmation reply - not a vague "let us know your thoughts"
- Name a specific date or window if a genuine deadline exists: "[INSERT: decision/response date]"; do not invent urgency where none exists
- Offer to walk through the proposal together rather than assuming it will be read and acted on unassisted

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

PROPOSAL COPY RULES:
- No em dashes anywhere - use hyphens or restructure
- No fabricated pricing, timelines, deliverables, or buyer-specific outcomes - every deal-specific detail is a marked [INSERT: ...] placeholder
- No banned CTA phrasing: {_BANNED_CTA_LIST}
- Written to and about this specific buyer's stated problem, never a generic industry pitch that could apply to any prospect
- Total length should land close to {wordcount} words across the four sections, excluding the pricing table itself

SELF-CHECK BEFORE OUTPUT:
- Does Section 1 recap a specific stated problem rather than a generic industry pain point?
- Are outcomes framed in the buyer's own success terms, not generic product benefits?
- Is every deal-specific number, date, or deliverable a marked placeholder rather than an invented figure?
- Is there exactly one clear next step in Section 4?
- Are there any em dashes or banned CTA phrases?

OUTPUT FORMAT:
Return the four sections in order with clear headers. Do not include a pricing table - note "[PRICING TABLE INSERTED HERE]" where it belongs in the final document. Paste-ready to wrap around a proposal generated in PandaDoc, Proposify, or a similar tool.
"""
