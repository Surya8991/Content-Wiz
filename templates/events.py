from ._shared import (
    BANNED_CTA_PHRASES,
    HUMAN_WRITING_RULES,
    RESEARCH_RULES,
    market_voice,
)

_BANNED_CTA_LIST = ", ".join(f'"{p}"' for p in BANNED_CTA_PHRASES)


def _split_words(wordcount, weights):
    """Split `wordcount` across `weights` (must sum to 1.0) proportionally.

    No fixed floor per section - every section scales with the requested
    wordcount. The last section absorbs the rounding remainder so the parts
    always sum to exactly `wordcount` (never negative, never silently off).
    A trivial max(..., 1) only prevents an actual zero-word section; it never
    overrides the caller's wordcount the way a large fixed floor would.
    """
    words = [max(round(wordcount * w), 1) for w in weights[:-1]]
    words.append(max(wordcount - sum(words), 1))
    return words


def webinar_registration_page(topic, audience, wordcount=None, market=None, **_):
    wordcount = wordcount or 450
    hero_w, learn_w, speaker_w, who_w, cta_w = _split_words(
        wordcount, [0.15, 0.30, 0.15, 0.20, 0.20]
    )
    total_words = hero_w + learn_w + speaker_w + who_w + cta_w

    return f"""You are a senior conversion copywriter who builds webinar registration pages, distinct from the promotional posts and emails that drive traffic TO the page. Your pages have been tested against form-field count, headline framing, and objection placement, and you write for the moment a visitor decides whether registering is worth 5 seconds of thought.

TASK:
Write a complete, publish-ready webinar registration page for: "{topic}"

TARGET AUDIENCE: {audience}
TARGET LENGTH: {total_words} words total (a scannable registration page, not an article - hit this target, do not pad)

{market_voice(market)}

PRE-WRITE DIAGNOSTIC (do this mentally before writing):
1. What is the single outcome a registrant walks away with, stated as a result, not a topic label? ("How to close 20% more deals with live demos" beats "Sales Webinar")
2. Who should self-qualify as "yes, this is for me" within the first 5 seconds, and who should self-disqualify just as fast?
3. What is the #1 reason a qualified visitor hesitates to register (time cost, "will this actually apply to me", skepticism about the speaker), and where does this get resolved before the CTA?

REGISTRATION PAGE CONVERSION CONTEXT:
- This is a distinct page from the promotional social posts and emails that drive traffic here - those sell the click, this page sells the registration decision itself
- Registration pages that lead with the specific outcome outperform pages that lead with a generic session title or format description
- Registration forms convert best when they ask for the minimum viable fields - do not invent extra form fields beyond what a typical registration needs (name, email, and only what the CTA discipline below calls for)
- A visible, real speaker credibility line lifts registration more than a polished but faceless page - people register for a person they trust, not an abstract agenda
- Mobile visitors are a meaningful share of registration traffic - keep the hero and CTA legible without assuming a desktop-only reader

PAGE STRUCTURE (follow this order - it is the page's scan path):

═══════════════════════════════════════════
1. HERO: OUTCOME HEADLINE + FORMAT DETAILS ({hero_w} words)
═══════════════════════════════════════════
- HEADLINE (8-12 words): States the concrete outcome or transformation tied to "{topic}", never the session's internal name or a vague topic label
- SUBHEADLINE (1 sentence, 15-25 words): Names who it's for ({audience}) and what format this is (live, on-demand replay available, panel, workshop)
- FORMAT/DATE/TIME LINE: exact date, time with timezone, duration, and delivery mode - use "[INSERT: date and time]" and "[INSERT: timezone]" placeholders if not supplied, never invent a specific date
- No fabricated live-registrant counter or attendee count here - if a real registration count is available, mark it "[INSERT: live registration count]" rather than inventing a number

═══════════════════════════════════════════
2. WHAT YOU WILL LEARN ({learn_w} words)
═══════════════════════════════════════════
- Exactly 3 concrete takeaways, each a specific skill, framework, or answer the attendee leaves with - never a vague benefit like "gain insights" or "learn best practices"
- Each takeaway bolds the specific result in the first few words
- Frame every takeaway as something the attendee can act on within a week of attending, not an abstract topic area

═══════════════════════════════════════════
3. SPEAKER CREDIBILITY BLOCK ({speaker_w} words)
═══════════════════════════════════════════
- Name and title: use "[INSERT: speaker name and title]" if not supplied - never invent a name, employer, or credential
- One sentence of relevant, specific credibility (what they have actually done that qualifies them on "{topic}") - use "[INSERT: speaker's relevant credential or experience]" if not supplied
- Do not fabricate a headshot description, a past employer, a certification, or a number of people the speaker has trained

═══════════════════════════════════════════
4. WHO THIS IS FOR ({who_w} words)
═══════════════════════════════════════════
- One qualifying sentence: "This session is built for {audience} who [specific situation]."
- A short bullet list (3-4 items) of specific roles or situations that should self-select in
- One counter-qualification line: who this is NOT for, or what they should look at instead - this is what makes the qualifying line credible rather than a page chasing everyone

═══════════════════════════════════════════
5. REGISTRATION CTA BLOCK ({cta_w} words)
═══════════════════════════════════════════
- One short closing line naming what happens immediately after registering (calendar invite, confirmation email, replay access if they cannot attend live)
- REGISTRATION CTA BUTTON: specific and benefit-framed (e.g. "Save My Seat for the Live Session", "Reserve My Spot") linking to [INSERT: registration URL] - never a banned generic phrase (see banned list below)
- If real social proof exists (a past attendee quote, a client logo), use an explicit placeholder - "[INSERT: attendee testimonial - name, title, company]" or "[INSERT: client logo]" - never invent a name, quote, or company

CTA DISCIPLINE:
- Banned CTA phrases (never use these, on this page or anywhere else in this project): {_BANNED_CTA_LIST}
- The registration CTA must name the specific action and benefit, not a vague command
- Only one primary registration action on the page - do not compete it against a second unrelated ask

{RESEARCH_RULES}

{HUMAN_WRITING_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the section word count add up to {total_words} total? (Recount: hero {hero_w} + takeaways {learn_w} + speaker {speaker_w} + who {who_w} + CTA {cta_w}.)
- Are there exactly 3 concrete takeaways, none of them a vague benefit statement?
- Does every speaker credential, testimonial, logo, or attendee count use an explicit [INSERT: ...] placeholder instead of an invented detail?
- Is the registration CTA specific, benefit-framed, and free of any banned phrase?
- Is there zero em dash anywhere in the output?

OUTPUT FORMAT:
Return the complete registration page copy in the exact section order above, with the "═══" section dividers and heading labels included. Use Markdown bold (**phrase**) for key phrases and bullet lists (-) for the takeaways and qualifying lists. No preamble, no meta-commentary about what was written.
"""


def event_followup_sequence(topic, audience, wordcount=None, market=None, **_):
    wordcount = wordcount or 500
    attended_total, noshow_total = _split_words(wordcount, [0.5, 0.5])

    # Each branch splits internally the same way: subject/preview, opening,
    # core body, CTA + sign-off. Scales with whatever half of `wordcount`
    # that branch received above - no branch has a fixed word count.
    a_subject_w, a_open_w, a_body_w, a_cta_w = _split_words(
        attended_total, [0.10, 0.20, 0.45, 0.25]
    )
    n_subject_w, n_open_w, n_body_w, n_cta_w = _split_words(
        noshow_total, [0.10, 0.20, 0.45, 0.25]
    )
    total_words = attended_total + noshow_total

    return f"""You are a lifecycle email strategist who builds post-webinar follow-up sequences for B2B teams, and you know that a single shared template with a swapped variable is the single most common way these sequences underperform. Attendees and no-shows are at different starting points and need structurally different messages, not the same message with a name plugged in.

TASK:
Write a complete, SEGMENTED post-event follow-up for the webinar: "{topic}"

TARGET AUDIENCE: {audience}
TARGET LENGTH: {total_words} words total, split into two clearly labeled, structurally distinct branches (not counting subject-line character counts)

{market_voice(market)}

PRE-WRITE DIAGNOSTIC (do this mentally before writing):
1. Attended branch: what is the single next step tied specifically to what this session covered - the thing someone who just watched it should logically do next?
2. No-show branch: what is the one thing that gets a non-attendee to actually open the recording, without guilt-tripping them for missing it?
3. What did each segment NOT yet see - attendees saw the content live, no-shows have seen nothing - and does each branch's message reflect that difference in starting point?

SEGMENTATION CONTEXT (why this cannot be one shared template):
- Attendees already have the content; their message should reinforce it and move them to a concrete next step, not re-pitch the session
- No-shows have not seen anything yet; their message has to first close that gap (get them to the recording) before any next-step ask makes sense
- Sending the same generic "thanks for your interest" message to both groups measurably under-converts the attended segment (who are ready to act now) and under-serves the no-show segment (who need the recording surfaced, not a next step they haven't earned yet)
- First-touch speed matters for both segments: reaching attendees same-day while the session is fresh, and reaching no-shows within a day or two before intent decays, both outperform a delayed, generic single blast

Write BOTH branches below, clearly labeled and fully separated - do not write one email and note "similar for the other segment."

═══════════════════════════════════════════
BRANCH A - ATTENDED (send same day, while the session is fresh)
═══════════════════════════════════════════

A1. SUBJECT LINE + PREVIEW TEXT ({a_subject_w} words):
- Subject references something specific from the session, not "Thanks for attending"
- Preview text adds a second layer of value, does not repeat the subject

A2. OPENING ({a_open_w} words):
- Thanks them for attending specifically, naming the session by topic, not a generic pleasantry
- References one specific moment or question from the session to prove this isn't a mass template

A3. BODY ({a_body_w} words):
- Recording and resource links: "[INSERT: recording link]" and "[INSERT: slides/resource link]"
- One specific next-step CTA tied directly to what they just learned in "{topic}" (not a generic "book a demo") - name the exact action and why it follows from the session content
- If citing a session outcome or expected result, follow the sourcing rules below or mark it "[VERIFY: ...]" rather than inventing a figure

A4. CTA + SIGN-OFF ({a_cta_w} words):
- CTA button/link text names the specific next step, not a banned generic phrase (see banned list below)
- Sign-off names a real sender or "[INSERT: sender name]" - never an anonymous "The Team"

═══════════════════════════════════════════
BRANCH B - NO-SHOW (send within 24-48 hours, before intent decays)
═══════════════════════════════════════════

B1. SUBJECT LINE + PREVIEW TEXT ({n_subject_w} words):
- Subject acknowledges they missed it without guilt language ("You missed something good", never "You missed out" framing that shames)
- Preview text leads with the recording, not an apology on their behalf

B2. OPENING ({n_open_w} words):
- Acknowledges plainly that they registered but could not attend live - factual, not guilt-tripping, no "we missed you!" over-familiarity
- Immediately pivots to what they can still get: the full recording

B3. BODY ({n_body_w} words):
- Recording link: "[INSERT: recording link]", framed as the easiest way to catch up, not a consolation prize
- One specific reason to actually watch it now (the single most useful takeaway from the session), re-engaging interest without pressure
- Do not repeat Branch A's next-step CTA here - a no-show has not earned that step yet; the only ask is "watch the recording"

B4. CTA + SIGN-OFF ({n_cta_w} words):
- CTA button/link text is specific to watching the recording, not a banned generic phrase (see banned list below)
- Sign-off names a real sender or "[INSERT: sender name]"

CTA DISCIPLINE (both branches):
- Banned CTA phrases (never use these, in either branch): {_BANNED_CTA_LIST}
- The two branches' CTAs must differ from each other - Branch A moves someone forward, Branch B gets someone caught up. They are not interchangeable.

{RESEARCH_RULES}

{HUMAN_WRITING_RULES}

SELF-CHECK BEFORE OUTPUT:
- Are Branch A and Branch B structurally different messages, not the same template with "attended"/"missed it" swapped in?
- Does Branch A's CTA depend on session content actually covered in "{topic}", and does Branch B's CTA stop at "watch the recording"?
- Is Branch B's acknowledgment of the miss free of guilt-tripping language?
- Do the word counts for each branch sum to their stated totals (Branch A: {a_subject_w} + {a_open_w} + {a_body_w} + {a_cta_w} = {attended_total}; Branch B: {n_subject_w} + {n_open_w} + {n_body_w} + {n_cta_w} = {noshow_total})?
- Is there zero em dash anywhere in the output?

OUTPUT FORMAT:
Return both branches in full, clearly labeled "BRANCH A - ATTENDED" and "BRANCH B - NO-SHOW" with the subsections above included under each. No preamble, no meta-commentary about which branch is "more important."
"""


def booth_followup(topic, audience, wordcount=None, market=None, **_):
    wordcount = wordcount or 130
    open_w, value_w, cta_w, sign_w = _split_words(wordcount, [0.30, 0.35, 0.25, 0.10])
    total_words = open_w + value_w + cta_w + sign_w

    return f"""You are a sales development writer who follows up on leads captured in a specific, real conversation at a conference or trade-show booth - not a passive form fill. You know booth-lead recall decays fast: the longer the gap between the conversation and the follow-up, the less the prospect remembers about your product or the conversation itself.

TASK:
Write a single follow-up message for a lead captured at a booth conversation about: "{topic}"

TARGET AUDIENCE: {audience}
TARGET LENGTH: {total_words} words total (a short, specific follow-up, not a sales email essay)

{market_voice(market)}

PRE-WRITE DIAGNOSTIC (do this mentally before writing):
1. What specific thing was discussed at the booth that this message must reference to prove it isn't a mass follow-up? (Use "[INSERT: what was discussed at the booth]" - never fabricate a conversation detail you were not given.)
2. Where did this person say they were in their buying or interest cycle - just looking, actively evaluating, ready for a next step? The next-step ask must match that, not overshoot it.
3. How many hours or days has it passed since the conversation? The faster this goes out, the more the prospect still remembers - treat send timing as part of the message's effectiveness, not a separate concern.

TIMING GUIDANCE (apply before sending, not counted in the word budget above):
- Booth-lead recall drops fast after the event ends - the tighter the gap between the conversation and this message, the higher it converts
- Send the same day if possible; treat anything past 24-48 hours as a lead that needs a lighter, more re-introductory touch rather than assuming full recall
- Do not send more than 2-3 total follow-ups to a booth lead who does not respond - repeated unanswered follow-ups hurt more than they help

MESSAGE STRUCTURE:

═══════════════════════════════════════════
1. OPENING - REFERENCE THE CONVERSATION ({open_w} words)
═══════════════════════════════════════════
- Opens by naming the event/booth context and "[INSERT: what was discussed at the booth]" specifically - never invent what was supposedly said or shown
- No generic opener like "It was great meeting you" as the entire opening - it must be paired with the specific detail placeholder above

═══════════════════════════════════════════
2. VALUE TIED TO THE CONVERSATION ({value_w} words)
═══════════════════════════════════════════
- Connects "{topic}" directly to the specific problem or interest the prospect raised at the booth (from the placeholder above), not a generic pitch
- One specific, relevant detail or resource that follows naturally from what they said they cared about - use "[INSERT: relevant resource/case study]" if a specific one is not supplied
- If citing any stat or result, follow the sourcing rules below or mark it "[VERIFY: ...]"

═══════════════════════════════════════════
3. NEXT STEP MATCHED TO THEIR STAGE ({cta_w} words)
═══════════════════════════════════════════
- One clear next step, sized to where they said they were in the buying/interest cycle - a "just looking" contact gets a light next step (a resource, a follow-up question), not a "book a 30-minute demo" ask reserved for someone ready to evaluate
- CTA names the specific action, never a banned generic phrase (see below)
- Only one next step - do not stack multiple competing asks in a short follow-up

═══════════════════════════════════════════
4. SIGN-OFF ({sign_w} words)
═══════════════════════════════════════════
- Real name and role, or "[INSERT: sender name and title]" if not supplied
- No corporate "The Team" sign-off - this follows up on a person-to-person conversation

CTA DISCIPLINE:
- Banned CTA phrases (never use these): {_BANNED_CTA_LIST}
- The next-step ask must match the stage signal from the conversation, not default to the biggest possible ask

{RESEARCH_RULES}

{HUMAN_WRITING_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the opening reference the "[INSERT: what was discussed at the booth]" placeholder rather than a fabricated conversation detail?
- Is the next step sized to the stage the prospect indicated, not automatically the most aggressive ask available?
- Does the word count add up to {total_words} total? (Recount: opening {open_w} + value {value_w} + CTA {cta_w} + sign-off {sign_w}.)
- Is there zero em dash anywhere in the output?

OUTPUT FORMAT:
Return only the final follow-up message, ready to send, with the sign-off included. No labels, no preamble, no explanation of which structure block produced which line.
"""
