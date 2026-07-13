from ._shared import (
    BANNED_CTA_PHRASES,
    HUMAN_WRITING_RULES,
    RESEARCH_RULES,
    market_voice,
)

_BANNED_CTA_LIST = ", ".join(f'"{p}"' for p in BANNED_CTA_PHRASES)


def _resolve_wordcount(wordcount, default):
    if not wordcount:
        return default
    try:
        wc = int(wordcount)
    except (TypeError, ValueError):
        return default
    return wc if wc > 0 else default


# ─────────────────────────────────────────────
# ONBOARDING SEQUENCE
# ─────────────────────────────────────────────


def onboarding_sequence(topic, audience, wordcount=None, market=None, **_):
    # Five emails, each with a distinct job. Per-email word budgets scale
    # proportionally with {wordcount} using the same floor-then-rescale
    # pattern as landing_page() in growth.py: floors keep tiny wordcounts
    # workable, and if the floors would overshoot the target the first four
    # emails rescale down together while the fifth (check-in) absorbs the
    # remainder, so the recount in SELF-CHECK is always the exact achievable
    # sum - verified by hand at wordcount 150, 400, and 900.
    wc = _resolve_wordcount(wordcount, 400)
    e1_words = max(round(wc * 0.24), 45)  # welcome + quick win
    e2_words = max(round(wc * 0.20), 40)  # feature discovery
    e3_words = max(round(wc * 0.18), 35)  # social proof
    e4_words = max(round(wc * 0.19), 35)  # habit-forming nudge
    min_e5_words = 35  # check-in, absorbs the remainder
    fixed_total = e1_words + e2_words + e3_words + e4_words
    if fixed_total + min_e5_words > wc:
        scale = max(wc - min_e5_words, 1) / fixed_total
        e1_words = max(round(e1_words * scale), 1)
        e2_words = max(round(e2_words * scale), 1)
        e3_words = max(round(e3_words * scale), 1)
        e4_words = max(round(e4_words * scale), 1)
        fixed_total = e1_words + e2_words + e3_words + e4_words
    e5_words = max(wc - fixed_total, min_e5_words)
    total_words = fixed_total + e5_words

    return f"""You are a lifecycle email marketer who has built onboarding drips for SaaS and subscription products, working from one hard number: users who do not engage within their first 72 hours face roughly a 90% chance of never activating. Every email in this sequence exists to move a new signup toward one specific first "aha moment," not to describe the product in general.

TASK:
Write a complete {"" if not topic else f'{topic}-focused '}onboarding email drip for a brand new signup or customer.

TARGET AUDIENCE: {audience}
TOTAL WORD BUDGET ACROSS ALL 5 EMAIL BODIES: {total_words} words (hit this target, do not pad any single email to fill space)

{market_voice(market)}

PRE-WRITE DIAGNOSTIC (answer before writing a single email):
1. What is the ONE action that proves this product's value to a brand-new {audience} user - the single "aha moment" this whole sequence is built to reach? Name it as [INSERT: product-specific first-value action].
2. What happens if the user does nothing in the first 72 hours? (Default assumption: activation odds drop sharply - the sequence's send timing exists to beat that window, not to pad out a marketing calendar.)
3. What is the single most common reason a new user stalls before reaching that first action (confusion, no clear next step, competing priorities)? Each email should chip away at that specific blocker, not repeat the same pitch five times.
4. Unsubscribe-compliance check: does this sequence give every recipient an unmistakable, working unsubscribe path in every send, and does it stop immediately once a user unsubscribes or fully activates? (State yes and confirm before proceeding - this is a compliance requirement, not a style note.)

SEND-TIMING WINDOW (encode this cadence, do not invent a different one):
- Email 1: within 5-10 minutes of signup (same session, while intent is highest)
- Email 2: Day 2-3 (inside the 72-hour activation window)
- Email 3: Day 5-7 (end of week one)
- Email 4: Day 10-14 (building the habit into week two)
- Email 5: Day 21-28 (the one-month check-in)
Adjust by a day or two for the product's actual usage cadence, but do not compress all five into the first week - the sequence needs the full arc to build habit, not just initial activation.

THE 5 EMAILS (each has a distinct job - do not repeat "welcome" five times):

═══════════════════════════════════════════
EMAIL 1 - WELCOME + QUICK WIN ({e1_words} words)
═══════════════════════════════════════════
- Subject line: names the outcome, not the brand ("You're in - here's your first [INSERT: product-specific quick win]" beats "Welcome to [Brand]!")
- Opens by confirming the signup succeeded in one line, then immediately points at [INSERT: product-specific first-value action] - no company history, no feature tour
- One single, specific next step the user can complete in under 5 minutes - this is the only ask in this email
- Include a visible, working unsubscribe link and a one-line note on how often this sequence will email them

═══════════════════════════════════════════
EMAIL 2 - FEATURE DISCOVERY ({e2_words} words)
═══════════════════════════════════════════
- Sent once the user has (or has not) completed Email 1's action - branch the framing: "Nice work on [action]" vs. "Still time to [action] - here's a shortcut"
- Introduces ONE additional capability tied directly to a problem the user likely already has, using [INSERT: product-specific feature name and what it does] rather than a fabricated feature claim
- Format as a short walkthrough (3-4 numbered steps), not a feature-list dump

═══════════════════════════════════════════
EMAIL 3 - SOCIAL PROOF ({e3_words} words)
═══════════════════════════════════════════
- Shows the user they are not alone in figuring this out: one specific, real customer story or outcome, using `[INSERT: real customer name/company and outcome - never fabricate a testimonial or result]`
- Frame the proof around the SAME first-value action from Email 1, reinforcing it rather than introducing a new pitch
- If citing an industry benchmark stat (e.g. typical activation or time-to-value figures), it must name the source and year per the research rules below, or be flagged for verification

═══════════════════════════════════════════
EMAIL 4 - HABIT-FORMING NUDGE ({e4_words} words)
═══════════════════════════════════════════
- Targets the user who activated but has not yet made the product part of a routine
- Suggest one small, repeatable behavior (e.g. a weekly check, a recurring use case) using `[INSERT: product-specific recurring-use pattern]`
- Tone: a helpful nudge from a peer who wants them to get the full value, not a re-pitch of the product

═══════════════════════════════════════════
EMAIL 5 - CHECK-IN ({e5_words} words)
═══════════════════════════════════════════
- A genuine, low-pressure check-in at the one-month mark: how is it going, what is unclear, what would help next
- Offers a specific, named resource or contact for help (`[INSERT: support resource/contact]`), not a generic "let us know if you have questions"
- Closes the onboarding sequence explicitly - state that this is the last scheduled onboarding email so the recipient knows what to expect next (regular lifecycle emails, not silence)
- Include a specific, genuine question that invites a real reply

CTA DISCIPLINE (applies across all 5 emails):
- Banned CTA phrases (never use these): {_BANNED_CTA_LIST}
- Every CTA names the specific next action ("Finish your first [INSERT: action]" beats "Get started")
- Every email includes a working unsubscribe path - this is non-negotiable, not just Email 1's job

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the email body word count add up to {total_words} total? (Recount: Email 1 {e1_words} + Email 2 {e2_words} + Email 3 {e3_words} + Email 4 {e4_words} + Email 5 {e5_words}.)
- Does each of the 5 emails have a genuinely distinct job, or does any of them just repeat "welcome"?
- Is every product-specific claim marked with an `[INSERT: ...]` placeholder instead of an invented feature or number?
- Does every email include a visible unsubscribe path?
- Is there zero em dash anywhere in the output?
- Does the send-timing note for each email match the 72-hour-to-one-month arc above?

OUTPUT FORMAT:
Return all 5 emails in order, each labeled with its send timing, subject line, and full body, using the "═══" section dividers above. No preamble, no meta-commentary about what was written.
"""


# ─────────────────────────────────────────────
# WIN-BACK / RE-ENGAGEMENT SEQUENCE
# ─────────────────────────────────────────────


def win_back_sequence(topic, audience, wordcount=None, market=None, **_):
    # Three emails. Word budgets scale proportionally with {wordcount} using
    # the same floor-then-rescale pattern used elsewhere in this project
    # (see landing_page() in growth.py): floors keep small wordcounts
    # workable, and if the floors would overshoot the target the first two
    # emails rescale down together while the third (last call) absorbs the
    # remainder - verified by hand at wordcount 150, 400, and 900.
    wc = _resolve_wordcount(wordcount, 400)
    e1_words = max(round(wc * 0.36), 50)  # reconnect / reason to return
    e2_words = max(round(wc * 0.32), 45)  # value reminder + soft incentive
    min_e3_words = 45  # last call, absorbs the remainder
    fixed_total = e1_words + e2_words
    if fixed_total + min_e3_words > wc:
        scale = max(wc - min_e3_words, 1) / fixed_total
        e1_words = max(round(e1_words * scale), 1)
        e2_words = max(round(e2_words * scale), 1)
        fixed_total = e1_words + e2_words
    e3_words = max(wc - fixed_total, min_e3_words)
    total_words = fixed_total + e3_words

    return f"""You are a lifecycle/retention email marketer who runs win-back sequences that recover roughly 10-30% of a lapsed segment when the trigger window and cadence are set correctly, and who never leans on a fabricated discount to do a subject line's job.

TASK:
Write a complete 3-email win-back / re-engagement sequence for: "{topic}"

TARGET AUDIENCE: {audience}
TOTAL WORD BUDGET ACROSS ALL 3 EMAIL BODIES: {total_words} words (hit this target, do not pad any single email to fill space)

{market_voice(market)}

PRE-WRITE DIAGNOSTIC (answer before writing, and STATE the answer to #1 at the top of the output as the diagnostic label):
1. WHICH TRIGGER APPLIES - pick exactly one and label it explicitly:
   - TIME-LAPSED INACTIVITY: a previously active user/customer has gone quiet for a defined window (see timing below)
   - ABANDONED CART: a shopper added items or started checkout and left without completing purchase
   - ABANDONED SIGNUP: a prospect started creating an account or a trial and never finished or never activated
2. What is the single most likely reason this specific segment went quiet (forgot, hit friction, priorities shifted, price hesitation)? The sequence should address that reason, not a generic "we miss you."
3. Is there a real, approved incentive available for this send (percentage off, free trial extension, bonus credit)? If none is confirmed, every incentive reference in the output must use `[INSERT: incentive if applicable]` rather than inventing a number - this project has a hard rule against fabricating business terms.

TRIGGER-SPECIFIC TIMING (use the window that matches the diagnosed trigger from #1):
- TIME-LAPSED INACTIVITY: anchor the window to the product's natural usage or repurchase cycle rather than a fixed calendar date - a reasonable default absent other data is 60-90 days of inactivity before Email 1 fires, with Emails 2 and 3 spaced 10-14 days apart
- ABANDONED CART: Email 1 at 30-60 minutes after abandonment (45 minutes is a solid default), Email 2 at 18-24 hours, Email 3 at 48-72 hours - waiting past roughly 2 hours for Email 1 measurably drops recovery
- ABANDONED SIGNUP: compress the whole sequence into the first 48-72 hours (Email 1 within a few hours, Email 2 at 24 hours, Email 3 at 48-72 hours) since incomplete-signup intent decays faster than a lapsed customer's does

THE 3 EMAILS:

═══════════════════════════════════════════
EMAIL 1 - RECONNECT / REASON TO RETURN ({e1_words} words)
═══════════════════════════════════════════
- Subject line: curiosity or specific-value framing, never a bare discount headline ("Still thinking about [INSERT: cart item / product]?" beats "20% OFF INSIDE")
- Leads with social proof, a genuine reason to come back, or what changed since they left - not a discount pitch as the opening move
- No fabricated urgency ("today only") unless a real deadline exists - if one does, state it plainly; if not, omit urgency language entirely
- If an incentive is planned for later emails, do not reveal it here - Email 1 earns attention on value, not price

═══════════════════════════════════════════
EMAIL 2 - VALUE REMINDER + SOFT INCENTIVE ({e2_words} words)
═══════════════════════════════════════════
- Restates the specific value the person is missing (named cart item, named product benefit, or named account capability - not a generic "come back")
- This is where an incentive can appear if one exists: `[INSERT: incentive if applicable]` - never a specific percentage or dollar figure the model does not actually have
- One clear, single CTA back to the exact point they left off (checkout, signup completion, or account login)

═══════════════════════════════════════════
EMAIL 3 - LAST CALL ({e3_words} words)
═══════════════════════════════════════════
- Final touch in the sequence - state plainly that this is the last scheduled message on this specific trigger (builds honest urgency without manufacturing a fake deadline)
- Strongest incentive placement if one exists: `[INSERT: incentive if applicable]`, otherwise lead with the single strongest value reason from Emails 1-2, restated fresh
- Close with an honest note on what happens next: if the trigger is TIME-LAPSED INACTIVITY, mention that continued non-engagement may reduce future email frequency or move them to a lower-frequency list (list-hygiene transparency, not a threat)

CTA DISCIPLINE (applies across all 3 emails):
- Banned CTA phrases (never use these): {_BANNED_CTA_LIST}
- Every incentive reference in every email uses the exact placeholder `[INSERT: incentive if applicable]` unless the caller has supplied a real, confirmed figure
- No fabricated scarcity or countdown claims not grounded in a real deadline

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Is the diagnosed trigger (time-lapsed inactivity / abandoned cart / abandoned signup) stated explicitly at the top of the output?
- Does the email body word count add up to {total_words} total? (Recount: Email 1 {e1_words} + Email 2 {e2_words} + Email 3 {e3_words}.)
- Does the send-timing note for each email match the window for the diagnosed trigger, not a generic guess?
- Is every incentive reference a placeholder rather than an invented number?
- Is there zero em dash anywhere in the output?

OUTPUT FORMAT:
Start with one line stating the diagnosed trigger. Then return all 3 emails in order, each labeled with its send timing, subject line, and full body, using the "═══" section dividers above. No preamble beyond the trigger line, no meta-commentary about what was written.
"""


# ─────────────────────────────────────────────
# CHURN PREVENTION
# ─────────────────────────────────────────────


def churn_prevention(topic, audience, wordcount=None, market=None, **_):
    # One proactive email, structured in four blocks whose word budgets
    # scale proportionally with {wordcount} using the same floor-then-
    # rescale pattern as the other functions in this file - verified by
    # hand at wordcount 150, 400, and 900.
    wc = _resolve_wordcount(wordcount, 400)
    s1_words = max(round(wc * 0.16), 35)  # opening signal acknowledgment
    s2_words = max(round(wc * 0.34), 70)  # the specific at-risk signal, named
    s3_words = max(round(wc * 0.28), 55)  # genuine help / no-pressure options
    min_s4_words = 35  # closing ask, absorbs the remainder
    fixed_total = s1_words + s2_words + s3_words
    if fixed_total + min_s4_words > wc:
        scale = max(wc - min_s4_words, 1) / fixed_total
        s1_words = max(round(s1_words * scale), 1)
        s2_words = max(round(s2_words * scale), 1)
        s3_words = max(round(s3_words * scale), 1)
        fixed_total = s1_words + s2_words + s3_words
    s4_words = max(wc - fixed_total, min_s4_words)
    total_words = fixed_total + s4_words

    return f"""You are a customer success writer who sends proactive save-the-account emails to at-risk B2B accounts before renewal conversations happen, not after. Your emails read as genuinely diagnostic - "what's not working for you" - never as defensive, discount-desperate, or scripted retention theater.

TASK:
Write a proactive churn-prevention email for an account showing at-risk signals related to: "{topic}"

TARGET AUDIENCE: {audience}
TOTAL WORD BUDGET: {total_words} words (this is one focused email, not a multi-touch drip - hit this target, do not pad)

{market_voice(market)}

PRE-WRITE DIAGNOSTIC (answer before writing):
1. WHICH AT-RISK SIGNAL triggered this email - name it explicitly: declining usage/login frequency, recent support friction (tickets, escalations, unresolved issues), or an approaching contract renewal with no recent engagement. Use `[INSERT: specific at-risk signal and data point]` for the exact metric or event (never fabricate a usage number or ticket count).
2. What does this account's OWN usage history suggest they were originally trying to accomplish? The email should reference that original goal, not restate generic product value.
3. Context check: B2B SaaS retention benchmarks put median annual retention around 88-90%, with top performers holding monthly churn under 2% (Recurly's 2025 Churn Report) - this email exists to keep a specific account on the right side of that median, not to hit a company-wide statistic. Do not cite this figure to the customer; it is context for the writer only.
4. What is the single most likely reason this account is at risk - onboarding gap, team turnover, budget scrutiny, a feature gap, or a support experience that went wrong? Frame the email around this specific hypothesis, stated as a genuine question, not an assumption presented as fact.

TONE MANDATE (the single hardest requirement in this template):
- Genuinely helpful and diagnostic - the email should read like a person who noticed something and wants to understand it, not a company defending its product or panicking about a lost deal
- NEVER defensive ("we've actually improved a lot since then"), NEVER desperate ("please don't go"), NEVER a hidden pitch disguised as concern
- Ask real questions and mean them - the email should work even if the honest answer is "this isn't the right fit anymore"
- No fabricated retention offer, discount, or concession - if one exists, use `[INSERT: retention offer if applicable]`; if none exists, do not invent one

THE EMAIL - 4 BLOCKS:

═══════════════════════════════════════════
1. OPENING SIGNAL ACKNOWLEDGMENT ({s1_words} words)
═══════════════════════════════════════════
- Subject line: specific and human, never alarmist ("Noticed a shift in [INSERT: specific area]" beats "We need to talk" or "Don't lose access")
- Names the specific observed signal from the diagnostic plainly, without judgment: "I noticed [INSERT: specific at-risk signal and data point]."
- No apology-first opening, no assumption of blame on either side

═══════════════════════════════════════════
2. THE SPECIFIC SIGNAL, NAMED ({s2_words} words)
═══════════════════════════════════════════
- Connects the signal to the account's own original goal (from diagnostic #2): "when you first set this up, it looked like the priority was [INSERT: original stated goal] - wanted to check whether that's still the case."
- Ask a direct, specific, genuinely open question about what changed: is it the product, the team, priorities, or something else entirely
- No feature pitch here - this section diagnoses, it does not sell

═══════════════════════════════════════════
3. GENUINE HELP / NO-PRESSURE OPTIONS ({s3_words} words)
═══════════════════════════════════════════
- Offer 2-3 concrete, low-friction options tied to plausible root causes: a working session with `[INSERT: specific support/success contact]`, a configuration review, or a direct answer to a specific blocker if one is known
- If a genuine retention offer or concession exists, place it here as `[INSERT: retention offer if applicable]` - never invent a discount, credit, or extension
- Explicitly acknowledge that "this isn't the right fit anymore" is a valid, acceptable answer - this is what separates genuine diagnosis from a disguised save-pitch

═══════════════════════════════════════════
4. CLOSING ASK ({s4_words} words)
═══════════════════════════════════════════
- One specific, low-effort next step: reply to this email, pick a time with `[INSERT: specific contact/scheduling link]`, or answer one direct question inline
- Sign off from a named human (`[INSERT: CSM/account owner name]`), not a team alias or "The [Brand] Team"
- No countdown, no renewal-deadline pressure language unless the renewal date is genuinely imminent and stating it plainly is itself useful information for the customer

CTA DISCIPLINE:
- Banned CTA phrases (never use these): {_BANNED_CTA_LIST}
- The single ask in this email is a reply or a scheduled conversation, not a link to a sales page

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the word count add up to {total_words} total? (Recount: Block 1 {s1_words} + Block 2 {s2_words} + Block 3 {s3_words} + Block 4 {s4_words}.)
- Does the email read as genuinely diagnostic, or does any sentence sound defensive or desperate?
- Is the at-risk signal named as an `[INSERT: ...]` placeholder rather than a fabricated number?
- Does the email explicitly leave room for "this isn't the right fit anymore" as an acceptable outcome?
- Is there zero em dash anywhere in the output?

OUTPUT FORMAT:
Return the complete email with subject line and all 4 blocks in order, using the "═══" section dividers above. No preamble, no meta-commentary about what was written.
"""


# ─────────────────────────────────────────────
# UPSELL / CROSS-SELL
# ─────────────────────────────────────────────


def upsell_cross_sell(topic, audience, wordcount=None, market=None, **_):
    # One value-led email, structured in four blocks whose word budgets
    # scale proportionally with {wordcount} using the same floor-then-
    # rescale pattern as the other functions in this file - verified by
    # hand at wordcount 150, 400, and 900.
    wc = _resolve_wordcount(wordcount, 400)
    hook_words = max(round(wc * 0.22), 40)  # success recap hook
    link_words = max(round(wc * 0.30), 60)  # the natural next step, tied to success
    frame_words = max(round(wc * 0.28), 55)  # specific value framing
    min_cta_words = 30  # low-pressure ask, absorbs the remainder
    fixed_total = hook_words + link_words + frame_words
    if fixed_total + min_cta_words > wc:
        scale = max(wc - min_cta_words, 1) / fixed_total
        hook_words = max(round(hook_words * scale), 1)
        link_words = max(round(link_words * scale), 1)
        frame_words = max(round(frame_words * scale), 1)
        fixed_total = hook_words + link_words + frame_words
    cta_words = max(wc - fixed_total, min_cta_words)
    total_words = fixed_total + cta_words

    return f"""You are a customer-marketing writer who builds expansion emails for accounts that have already demonstrated success - not cold upsell blasts. Expansion revenue from existing accounts now accounts for roughly 40% of new ARR at B2B SaaS companies, up from a median of about 25% a few years ago, precisely because the strongest upgrade path is the one triggered by a customer's own results, not a generic "check out our other plans" email.

TASK:
Write a value-led upsell/cross-sell email triggered by a customer's own demonstrated usage or success, related to: "{topic}"

TARGET AUDIENCE: {audience}
TOTAL WORD BUDGET: {total_words} words (one focused email - hit this target, do not pad)

{market_voice(market)}

PRE-WRITE DIAGNOSTIC (answer before writing):
1. WHAT SUCCESS SIGNAL triggered this email - a specific usage milestone, a result the customer achieved, or a pattern showing they've outgrown their current plan/tier? Name it as `[INSERT: specific usage milestone or achieved result]` - never fabricate a number or outcome the account did not actually reach.
2. What is the NATURAL next step this specific success points toward - not a generic "upgrade now," but the specific capability or tier that extends what they already proved works for them?
3. Who owns this signal - is it a product-usage trigger (self-serve expansion) or a customer-success-identified signal (a CSM should be the named sender)? State which, since this determines both the sender and the tone.

CORE PRINCIPLE (the single hardest requirement in this template):
- The customer's own success IS the reason for the next step - not a list of additional features they don't have yet
- Never open with a bundle/plan comparison. Open with what they already accomplished, and let that accomplishment be the argument
- If the email cannot honestly point to a specific thing this account already did or achieved, it should not be sent as an upsell trigger - flag this rather than manufacturing a generic pitch

THE EMAIL - 4 BLOCKS:

═══════════════════════════════════════════
1. SUCCESS RECAP HOOK ({hook_words} words)
═══════════════════════════════════════════
- Subject line: names the customer's own result, not the product's feature ("You've [INSERT: specific milestone] - here's what's next" beats "Unlock more with [Plan Name]")
- Opens by naming the specific, real success signal from the diagnostic: `[INSERT: specific usage milestone or achieved result]`
- No feature pitch yet - this block exists purely to make the customer feel seen for something they actually did

═══════════════════════════════════════════
2. THE NATURAL NEXT STEP, TIED TO SUCCESS ({link_words} words)
═══════════════════════════════════════════
- Draws a direct line from the named success to the specific next capability or tier: "because you've already [INSERT: milestone], the next thing most accounts like yours do is [INSERT: specific next step]"
- This is a logical extension of proven behavior, not a separate sales pitch bolted onto the top
- Reference the account's own context specifically enough that this email could not be sent to an account that hadn't hit the same milestone

═══════════════════════════════════════════
3. SPECIFIC VALUE FRAMING ({frame_words} words)
═══════════════════════════════════════════
- Describe what changes for this account specifically if they take the next step - outcome language, not a feature list
- If citing an expected result or benchmark (e.g. typical expansion outcomes for similar accounts), name the source and year per the research rules below, or mark it for verification
- Any pricing, discount, or bundling detail uses `[INSERT: pricing/offer detail]` - never a fabricated number

═══════════════════════════════════════════
4. LOW-PRESSURE ASK ({cta_words} words)
═══════════════════════════════════════════
- One clear, specific next action: a short call with `[INSERT: CSM/account owner name]`, a self-serve upgrade link, or a direct reply to ask questions
- No artificial urgency or countdown - this is an earned recommendation, not a limited-time push
- Signed by a named human matching whichever owner was identified in diagnostic #3

CTA DISCIPLINE:
- Banned CTA phrases (never use these): {_BANNED_CTA_LIST}
- The CTA names the specific next step tied to the account's own success, never a generic "upgrade now" or "see plans"

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the word count add up to {total_words} total? (Recount: Block 1 {hook_words} + Block 2 {link_words} + Block 3 {frame_words} + Block 4 {cta_words}.)
- Does the email's argument rest on the customer's own demonstrated success, or does it read as a generic feature pitch?
- Is every specific milestone, result, or pricing detail an `[INSERT: ...]` placeholder rather than an invented figure?
- Is there zero em dash anywhere in the output?

OUTPUT FORMAT:
Return the complete email with subject line and all 4 blocks in order, using the "═══" section dividers above. No preamble, no meta-commentary about what was written.
"""
