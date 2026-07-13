from ._shared import (
    BANNED_CTA_PHRASES,
    HUMAN_WRITING_RULES,
    market_voice,
)

_BANNED_CTA_LIST = ", ".join(f'"{p}"' for p in BANNED_CTA_PHRASES)

# Scoped citation rule for short creator documents (outreach messages, creator
# briefs). The full RESEARCH_RULES block mandates 2-3 statistics per 500 words
# and a Sources/Further Reading note, which is wrong for these formats: a
# ~125-word outreach email or a hand-off brief needs zero stats by default.
# Only the parts of the sourcing policy that still apply are kept here.
_INLINE_CITATION_RULE = """
CITATION RULE (scoped for this short-format document):
- This format needs zero statistics by default; include one only if it genuinely strengthens the message.
- Any statistic that does appear must name its source organization and year inline; never state a bare number and never fabricate one.
- Any first-party or proprietary-sounding statistic (e.g. "our customers saw X%") must trace to a real row in data/HARO_DataBank.csv, never be generated from general knowledge.
- No Sources or Further Reading section; this format does not carry one.
""".strip()


def influencer_outreach(topic, audience, wordcount=None, market=None, **_):
    # Real outreach that gets replies is short. Current-norm benchmarks (2026):
    # personalized pitches that reference a creator's actual recent content
    # outperform generic mail-merge pitches several times over, and creators
    # stop reading long pitches - so the default body target is 125 words and
    # every block scales proportionally with a caller override (no fixed
    # absolute floors, the bug class this repo's audit already fixed).
    wc = wordcount or 125
    open_lo, open_hi = round(wc * 0.22), round(wc * 0.28)
    offer_lo, offer_hi = round(wc * 0.34), round(wc * 0.42)
    ask_lo, ask_hi = round(wc * 0.20), round(wc * 0.26)
    sign_lo, sign_hi = round(wc * 0.06), round(wc * 0.10)
    total_lo = open_lo + offer_lo + ask_lo + sign_lo
    total_hi = open_hi + offer_hi + ask_hi + sign_hi
    return f"""You are a brand-side influencer partnerships manager who has personally sent and iterated hundreds of creator outreach messages, and you know exactly why most get ignored: they are long, generic, and all about the brand. Your pitches get replies because they are short, specific to the one creator reading them, and lead with what the creator gets.

TASK:
Write a personalized outreach message from a brand to a specific creator, proposing a collaboration related to: "{topic}"

TARGET CREATOR PROFILE: {audience}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. WHO is this creator, specifically? What have they posted recently, what formats do they favor, what does their audience respond to? If the real answer is unknown, the message must contain a clearly marked research slot ("[INSERT: reference to a specific recent post - name the post, what it covered, and what specifically worked about it]"), never a fake-specific compliment.
2. WHY this creator and not any creator? What is the genuine audience/content fit between their work and {topic}? If you cannot articulate the fit in one sentence, the pitch is not ready.
3. WHAT is the offer? Which compensation model do the inputs specify: flat fee, affiliate/commission, or product-plus-fee hybrid? Present the model the inputs specify. If the inputs do not specify one, present the offer with a placeholder and name the model options for the sender to choose.
4. WHAT is the single ask? One collaboration, one next step. Not a menu.

RESEARCH-THE-CREATOR-FIRST RULE (non-negotiable):
The opening lines must prove the sender actually looked at this creator's work. Reference a specific recent post, video, or series: what it was about and one concrete observation about it (an angle they took, a format choice, an audience reaction). A mail-merge opener that could be pasted to 50 creators is an automatic rewrite. Personalized outreach that names the creator's actual content is what earns replies; generic blasts get ignored.

BANNED OPENERS (never use these or close variants):
- "I love your content!"
- "I'm a big fan of your work"
- "I came across your profile"
- "I've been following you for a while" (unless followed immediately by a specific, checkable reference)
- Any compliment that names nothing specific the creator actually made

OUTREACH MESSAGE STRUCTURE ({total_lo} to {total_hi} words total body, target around {wc} - short messages get replies, long ones get archived):

SUBJECT LINE / DM FIRST LINE (not counted in body total):
- Email: 4 to 8 words, names the collaboration or the creator's content niche, zero clickbait (e.g. "Paid partnership idea for your [niche] series")
- DM variant: the first line does this job instead - get to the point in sentence one

BLOCK 1 - PERSONALIZED OPENER ({open_lo} to {open_hi} words):
- Reference the specific recent content identified in the diagnostic, with one concrete observation
- Then bridge in one sentence to why the brand is reaching out: the fit between their content/audience and {topic}
- No brand self-introduction paragraph. One clause of who is writing is enough ("I run partnerships at [INSERT: brand name]")

BLOCK 2 - THE OFFER, CREATOR-FIRST ({offer_lo} to {offer_hi} words):
What's in it for THEM, stated before any brand requirements:
- Name the compensation model the inputs specify: flat fee, affiliate/commission, or product-plus-fee hybrid
- NEVER invent specific dollar amounts, commission percentages, or product values - use placeholders: "[INSERT: offer details - fee range / commission rate / product + fee terms]"
- One line on scope: what kind of content, roughly how much, and that they keep creative control of how they say it
- One line on why their audience benefits (the offer has to make sense for their followers, not just the brand)

BLOCK 3 - THE SINGLE ASK ({ask_lo} to {ask_hi} words):
- One specific, low-friction next step: a yes/no reply, a 15-minute call slot, or "reply and I'll send the one-page brief"
- Never multiple asks, never "let me know your thoughts on all of this"
- Make the no easy too: one clause acknowledging they can pass and the door stays open

BLOCK 4 - SIGN-OFF ({sign_lo} to {sign_hi} words):
- Real name, role, brand, and one contact placeholder ("[INSERT: sender name, role, brand, contact]")
- No postscript sales pressure, no "limited spots" fake scarcity

DM VARIANT:
After the email version, provide a compressed DM variant of the same pitch (roughly 40 to 60 percent of the email body length): same personalized opener logic, same single ask, no subject line, even more conversational. Email is the norm for business-level collaboration outreach; the DM variant is for creators who are clearly more responsive on-platform.

FOLLOW-UP NOTE:
Below both variants, add one suggested follow-up line the sender can use if there is no reply after 3 to 7 days - one sentence, references the original message, adds one new piece of value or context, no guilt-tripping ("just bumping this" is banned).

CTA RULES:
- Exactly one ask across the whole message
- Banned phrases (do not use anywhere in the message): {_BANNED_CTA_LIST}
- No manufactured urgency, no fake deadlines

{HUMAN_WRITING_RULES}

{_INLINE_CITATION_RULE}

NO EM DASHES anywhere - use hyphens, commas, or restructure the sentence.

SELF-CHECK BEFORE OUTPUT:
- Could the opener be pasted to any other creator unchanged? If yes, rewrite it.
- Is every compensation figure a marked [INSERT: ...] placeholder, with zero invented dollar amounts or percentages?
- Is there exactly one ask, and is the next step genuinely low-friction?
- Is the email body within {total_lo} to {total_hi} words?
- Does the message lead with what the creator gets, before what the brand wants?
- Are there any banned openers, banned CTA phrases, or em dashes?

OUTPUT FORMAT:
Return, in order:
1. SUBJECT: [subject line]
2. EMAIL VERSION: the full email body, plain paragraphs
3. DM VERSION: the compressed on-platform variant
4. FOLLOW-UP LINE: the single suggested follow-up sentence
Below the email version, add a single line: WORD COUNT: [N words]
"""


def ugc_brief(topic, audience, wordcount=None, market=None, **_):
    # Section budgets scale proportionally with the caller's wordcount override
    # instead of fixed absolute floors (the bug class this repo's audit already
    # fixed in blog_writing). Fractions sum to 1.0 of the target.
    wc = wordcount or 600
    snap_lo, snap_hi = round(wc * 0.10 * 0.85), round(wc * 0.10 * 1.15)
    prod_lo, prod_hi = round(wc * 0.14 * 0.85), round(wc * 0.14 * 1.15)
    msg_lo, msg_hi = round(wc * 0.14 * 0.85), round(wc * 0.14 * 1.15)
    free_lo, free_hi = round(wc * 0.08 * 0.85), round(wc * 0.08 * 1.15)
    deliv_lo, deliv_hi = round(wc * 0.12 * 0.85), round(wc * 0.12 * 1.15)
    hook_lo, hook_hi = round(wc * 0.12 * 0.85), round(wc * 0.12 * 1.15)
    dd_lo, dd_hi = round(wc * 0.10 * 0.85), round(wc * 0.10 * 1.15)
    disc_lo, disc_hi = round(wc * 0.12 * 0.85), round(wc * 0.12 * 1.15)
    rights_lo, rights_hi = round(wc * 0.08 * 0.85), round(wc * 0.08 * 1.15)
    return f"""You are a brand-side UGC and creator-content lead who has briefed hundreds of contracted creators, and you have learned the central lesson of creator briefs the hard way: the brief's job is to define WHAT to communicate, never to script HOW to say it. Over-scripted briefs produce content that sounds like an ad read by a hostage; the highest-performing creator content comes from a clear goal plus genuine creative freedom in the creator's own voice.

TASK:
Write a complete UGC / creator creative brief a brand hands to a contracted creator, for a campaign about: "{topic}"

CREATOR / AUDIENCE CONTEXT: {audience}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. What is the ONE campaign goal this content serves (awareness, consideration, conversion, retention)? A brief serving three goals serves none.
2. What are the 2 to 3 key messages the content must land - stated as ideas to communicate, not lines to read?
3. What does the creator need to know about the product to talk about it credibly (features, the problem it solves, what makes it different)?
4. Which platform and format is this for, and what does native content on that platform actually look like?

THE WHAT-NOT-HOW PRINCIPLE (this governs the entire brief):
- The brief defines WHAT to communicate: goal, key messages, product focus, mandatory compliance elements
- The brief NEVER scripts HOW to say it: no word-for-word scripts, no mandated phrasing for the creator's narration, no dictated jokes or personality
- The brief must SAY this to the creator explicitly, in plain language, e.g.: "These are the ideas to get across. Say them in your own voice, the way you'd naturally talk to your audience. We hired you for how you talk, not to read our lines."
- Clarity on what is non-negotiable versus where the creator has freedom is what makes a brief work - mark every mandatory element as MANDATORY and state that everything else is the creator's call

UGC CREATIVE BRIEF STRUCTURE (target {wc} words total):

═══════════════════════════════════════════
SECTION 1 - CAMPAIGN SNAPSHOT ({snap_lo} to {snap_hi} words)
═══════════════════════════════════════════
- Brand and product in one line ("[INSERT: brand name]" if not specified)
- The ONE campaign goal, stated plainly
- The audience this content should speak to, in one or two lines
- Timeline: draft due date and go-live window as placeholders ("[INSERT: draft due date]", "[INSERT: publish window]")

═══════════════════════════════════════════
SECTION 2 - PRODUCT FOCUS ({prod_lo} to {prod_hi} words)
═══════════════════════════════════════════
What the creator needs to know to talk about the product credibly:
- The problem it solves and for whom
- The 2 to 3 features or benefits that matter for THIS campaign (not the full feature list)
- What makes it different from the obvious alternatives, in one line
- Any true claims the creator may make, and a note that anything not listed here must not be claimed (no invented performance numbers, no medical/financial promises)

═══════════════════════════════════════════
SECTION 3 - KEY MESSAGES ({msg_lo} to {msg_hi} words)
═══════════════════════════════════════════
The 2 to 3 ideas the content must communicate, each stated as a concept, not a script line:
- Format each as: "MESSAGE: [the idea]. Why it matters to your audience: [one line]."
- Explicitly label these as ideas to convey in the creator's own words
- MANDATORY elements only if the inputs truly require them (e.g. product visibly in frame, brand name spoken once) - each marked MANDATORY and kept to the minimum

═══════════════════════════════════════════
SECTION 4 - YOUR VOICE, YOUR EXECUTION ({free_lo} to {free_hi} words)
═══════════════════════════════════════════
The explicit creative-freedom statement, addressed directly to the creator:
- Say plainly: the hook, structure, setting, styling, humor, and phrasing are the creator's call
- State why: their audience follows them for their voice; content that sounds like the brand wrote it underperforms content that sounds like the creator made it
- Invite them to flag anything in the brief that would not work for their audience

═══════════════════════════════════════════
SECTION 5 - DELIVERABLES SPEC ({deliv_lo} to {deliv_hi} words)
═══════════════════════════════════════════
Precise and boring on purpose - this is the one section where specificity helps the creator:
- Format: [e.g. 1 vertical video + 2 raw variations - adapt to the inputs]
- Platform: [the platform(s) the inputs specify, or "[INSERT: platform]"]
- Aspect ratio and resolution: 9:16 vertical, 1080x1920 for short-form video (adjust if the platform differs)
- Length: state the target runtime for the platform (e.g. 15 to 60 seconds for TikTok/Reels/Shorts)
- File delivery: raw footage vs edited, captions on/off, delivery method as a placeholder ("[INSERT: delivery method]")
- Rounds of revision included: "[INSERT: revision terms]"

═══════════════════════════════════════════
SECTION 6 - OPTIONAL HOOK AND CONCEPT STARTERS ({hook_lo} to {hook_hi} words)
═══════════════════════════════════════════
2 to 3 hook or concept directions the creator MAY use, adapt, or ignore entirely:
- Label the section explicitly: "Optional - use these, remix them, or pitch your own. Your call."
- Each is a one-line concept direction (an angle, a scenario, a question), never a scripted opening line
- Ground each in the campaign goal, not in brand vanity

═══════════════════════════════════════════
SECTION 7 - DOS AND DON'TS ({dd_lo} to {dd_hi} words)
═══════════════════════════════════════════
Kept deliberately SHORT - a brief with 20 don'ts kills the creator's voice, and a short don'ts list means everything outside it is fair game (state that explicitly):
- Maximum 3 dos and 4 don'ts, each one line
- Don'ts limited to genuine brand-safety and legal lines (e.g. no competitor disparagement, no unapproved claims, no profanity if the brand requires it)
- End the section with: "Anything not on this list is fair game."

═══════════════════════════════════════════
SECTION 8 - DISCLOSURE AND COMPLIANCE (MANDATORY) ({disc_lo} to {disc_hi} words)
═══════════════════════════════════════════
This section is a legal requirement, not a style preference. Encode current FTC (US) and ASA (UK) guidance:
- The material connection (payment, free product, or both - gifted product counts as payment) must be disclosed clearly and conspicuously WITH the content itself, not only on a profile page or behind a "more" tap
- Caption disclosure goes at the START of the caption, before the truncation point on platforms that cut captions (Instagram, TikTok, Facebook)
- Acceptable disclosure language: "Ad", "Sponsored", "Paid partnership with [brand]". NOT acceptable on their own: "collab", "sp", "spon", "partner", "thanks [brand]"
- For video: the disclosure must also be IN the video (spoken and/or clearly readable on-screen), not caption-only, since videos get reshared without captions
- Platform disclosure tools (e.g. paid-partnership labels) may be used IN ADDITION to, not instead of, the caption/in-content disclosure
- State that the brand requires this on every deliverable and will not publish or pay for undisclosed content - regulators can penalize both creator and brand
- UK/other markets: "#ad" upfront per ASA rules; adapt to "[INSERT: campaign markets]" if the inputs specify markets

═══════════════════════════════════════════
SECTION 9 - USAGE RIGHTS AND PAYMENT ({rights_lo} to {rights_hi} words)
═══════════════════════════════════════════
NEVER invent legal or commercial terms - every term in this section is a placeholder the brand fills in:
- Usage scope: "[INSERT: usage terms - organic only / paid amplification (Spark Ads, whitelisting) / website and email use]"
- Duration and exclusivity: "[INSERT: usage duration]", "[INSERT: exclusivity terms, if any]"
- Payment: "[INSERT: fee and payment schedule]" - never a fabricated amount
- One line noting that paid-usage and whitelisting rights are priced separately from organic posting, as a prompt for the brand to be explicit rather than assume

{HUMAN_WRITING_RULES}

{_INLINE_CITATION_RULE}

NO EM DASHES anywhere in the brief - use hyphens, commas, or restructure.
No fabricated statistics anywhere: any illustrative number that is not a genuine platform spec (like 9:16 or 1080x1920) must be a clearly marked [INSERT: ...] placeholder.

SELF-CHECK BEFORE OUTPUT:
- Does the brief define WHAT to communicate without scripting HOW to say it anywhere - zero word-for-word narration lines?
- Does it explicitly TELL the creator they have creative freedom, in Section 4 and in the hook section's "optional" label?
- Are dos and don'ts at or under 3 and 4 items, with the "everything else is fair game" line present?
- Is the disclosure section complete: start-of-caption placement, acceptable wording listed, in-video disclosure for video, gifted product counts as payment?
- Is every usage-rights, payment, and legal term a marked [INSERT: ...] placeholder with zero invented terms?
- Do the deliverables specify format, aspect ratio, length, and platform?
- Are there any em dashes or fabricated statistics?

OUTPUT FORMAT:
Return the complete brief with all nine numbered sections in order, with section dividers, written TO the creator in second person ("you", "your audience"). Paste-ready for a real brand-to-creator handoff document. No preamble, no meta-commentary.
"""
