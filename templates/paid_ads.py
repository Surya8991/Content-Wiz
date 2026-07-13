from ._shared import (
    BANNED_CTA_PHRASES,
    HUMAN_WRITING_RULES,
    RESEARCH_RULES,
    market_voice,
)

_BANNED_CTA_LIST = ", ".join(f'"{p}"' for p in BANNED_CTA_PHRASES)


def display_banner_copy(topic, audience, wordcount=None, market=None, **_):
    # Headline/body/CTA are character-capped by the ad network, not word-count
    # driven - these ceilings hold regardless of any wordcount override (same
    # rule as profile_bio's X/Instagram variants). wordcount only ever affects
    # how many visual-direction/rationale sentences surround the copy, never
    # the ad copy itself.
    wordcount_note = (
        f"CALLER OVERRIDE: a wordcount of {wordcount} was supplied. It has no effect on the headline, "
        "body, or CTA character budgets below - those are hard platform ceilings. Use the override only "
        "to decide how much supporting VISUAL DIRECTION detail to write per size."
        if wordcount
        else "No wordcount override supplied - write concise, standard-depth visual direction notes."
    )

    return f"""You are a programmatic display copywriter who has shipped IAB-standard banner creative across DV360, The Trade Desk, and Google Display Network, and who writes to the real character ceilings those networks truncate at rather than to an idealized headline length.

TASK:
Write a complete set of programmatic display banner ad copy for: "{topic}"

TARGET AUDIENCE: {audience}

{market_voice(market)}

{wordcount_note}

PRE-WRITE DIAGNOSTIC:
1. What is the single scannable claim this banner must land in under 2 seconds of peripheral attention - display is glanced at, not read?
2. What one visual (product shot, single stat, or before/after) does the headline need to sit next to for the claim to land without extra words?
3. What is the one action the click should trigger, stated as a 2-4 word button label?

2026 PROGRAMMATIC DISPLAY CONTEXT:
- Five IAB standard sizes carry over 70% of all display impressions: 300x250 (Medium Rectangle), 728x90 (Leaderboard), 160x600 (Wide Skyscraper), 300x600 (Half Page), and 320x50 (Mobile Banner)
- Google Ads-served display headlines cap at 30 characters (short headline) with a 90-character long headline field, and descriptions cap at 90 characters - copy that runs longer gets truncated with an ellipsis, not wrapped
- Every size shares the same ~150 KB creative file-weight ceiling most networks enforce, which is why the copy itself has to carry the message; there is no room for a second visual idea
- Smaller units (320x50, 728x90) have almost no vertical room - one line of headline, no room for a body line at all in the 320x50

AD SIZE SET (write copy for all five, since a real campaign trafficks all five together):

SIZE 1 - 300x250 (MEDIUM RECTANGLE):
- HEADLINE: 25-30 characters. The single scannable claim.
- BODY: 45-60 characters. One supporting detail or proof point, no source needed at this length - if a stat is used it must still be real and not fabricated.
- CTA BUTTON: 2-4 words, action-first ("See pricing", "Start free trial").
- VISUAL DIRECTION: What image/icon this headline needs beside it to read instantly (e.g. "product screenshot, left-aligned, headline right-aligned over solid background").

SIZE 2 - 728x90 (LEADERBOARD):
- HEADLINE: 30-35 characters. Wide and short - this unit reads left to right in one glance.
- BODY: omit or cap at 30-35 characters if included - the leaderboard has almost no vertical room.
- CTA BUTTON: 2-3 words, placed far right of the unit.
- VISUAL DIRECTION: Horizontal layout note (e.g. "logo left, headline center, button right, single accent color").

SIZE 3 - 160x600 (WIDE SKYSCRAPER):
- HEADLINE: 20-25 characters, stacked (this unit is tall and narrow - write for vertical stacking, not a horizontal sentence).
- BODY: 60-80 characters, can stack across 2-3 short lines.
- CTA BUTTON: 2-3 words, anchored at the bottom of the unit.
- VISUAL DIRECTION: Vertical stacking note (e.g. "logo top, headline mid, single supporting icon, button pinned bottom").

SIZE 4 - 300x600 (HALF PAGE):
- HEADLINE: 25-35 characters.
- BODY: 90-110 characters - this is the one size with room for a real supporting sentence.
- CTA BUTTON: 2-4 words.
- VISUAL DIRECTION: Note on how the extra vertical space gets used (e.g. "product shot top half, copy block bottom half, button beneath body").

SIZE 5 - 320x50 (MOBILE BANNER):
- HEADLINE ONLY: 20-25 characters, no body line fits at this size.
- CTA BUTTON: 2-3 words, or a single icon-plus-word if the network supports it.
- VISUAL DIRECTION: Note that this unit is thumb-adjacent on mobile - keep any tap target away from the very edge.

CTA RULES:
- Use the placeholder [INSERT CTA LINK] for the destination - never fabricate a URL
- Banned phrases across all sizes: {_BANNED_CTA_LIST}
- Do not repeat the identical CTA button label across all five sizes in the same set - vary the verb (e.g. "See pricing" / "Compare plans" / "Get started") so the set doesn't read as one copy-pasted ad resized five times

CITATION RULE:
If any body line states a stat or number, name the source organization and year in the accompanying VISUAL DIRECTION note as a reminder for whoever builds the creative (e.g. "footnote/legal line should cite [Org], [Year]") - never state a bare number in the ad copy with no attributable source available to the advertiser.

NO EM DASHES: hyphens only, in every headline, body line, and CTA.

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does every headline fit its stated character ceiling, counted exactly, not estimated?
- Is the 320x50 headline-only, with no body line squeezed in?
- Does the 300x600 body use its extra room for one real supporting sentence rather than repeating the headline?
- Do the five CTA button labels vary instead of repeating the same two or three words five times?
- Is any stat backed by a real, nameable source rather than invented?
- Are there zero em dashes anywhere in the output?

OUTPUT FORMAT:
For each of the 5 sizes, output: SIZE, HEADLINE (with character count shown), BODY (with character count shown, or "(none - size has no body room)"), CTA BUTTON, VISUAL DIRECTION.

Save to: output/Paid_Ads/Display/
"""


def native_ad_copy(topic, audience, wordcount=None, market=None, **_):
    reference_words = 150
    scale = (wordcount / reference_words) if wordcount else 1.0
    variant_count = 3 if not wordcount else max(2, min(5, round(3 * scale)))

    return f"""You are a native advertising copywriter who has written in-feed placements for Outbrain, Taboola, and social in-feed native units, and who writes headlines that earn the click on their own merit rather than through curiosity-gap clickbait that native networks and platform algorithms now actively suppress.

TASK:
Write a set of {variant_count} in-feed native ad headline-and-body variants for: "{topic}"

TARGET AUDIENCE: {audience}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. What is the specific, concrete outcome or fact this native unit promises - stated plainly enough that the headline is still true after the click, not just enticing before it?
2. Where will this unit run (news-content recommendation widget, social feed, or content-discovery sidebar), since that changes how much the copy needs to visually match surrounding editorial content?
3. What does {audience} actually read next to this unit - what editorial tone would make this headline feel native rather than foreign to the feed?

2026 NATIVE ADVERTISING CONTEXT:
- Native networks (Outbrain, Taboola) and platform feed algorithms now actively down-rank engagement-bait patterns ("You won't believe...", "Number 7 will shock you", ellipses-as-hook, ALL CAPS urgency) - these patterns trigger clickbait-detection penalties that reduce delivery, not just reader trust
- Headline field limits run up to 200 characters on most native ad platforms, but headlines that convert best sit far shorter - roughly 25-40 characters performs best for scannability, with the full field reserved for edge cases, not the target
- Description/caption fields cap around 200 characters with roughly 100 characters recommended as the practical read-through length
- The winning pattern for 2026 clickbait-resistant headlines: state the specific, concrete outcome or finding directly (a real number, a named method, a plain claim) rather than withholding it to force a click

MANDATORY DISCLOSURE (this is an FTC compliance requirement, not a style choice):
- Every native unit must carry a visible disclosure placed close enough to the unit that a reader sees it before engaging, not buried behind a tap or only on the landing page
- Acceptable disclosure labels per FTC guidance: "Ad", "Advertisement", "Paid Advertisement", "Sponsored Content"
- NOT acceptable on their own, because the FTC has found them ambiguous or misleading: "Promoted", "Promoted Story", "Suggested for you" with no other marker
- If this unit could be mistaken for the surrounding editorial content in look or topic (the more it resembles the feed, the more disclosure it needs), state that explicitly and require the stronger label ("Sponsored Content" or "Advertisement") rather than the bare minimum
- Disclosure applies to both the in-feed teaser AND the landing page it clicks through to - note this as a requirement for whoever builds the landing page, not just the ad unit

VARIANT STRUCTURE (write all {variant_count} variants, each distinct):

For each variant:
- HEADLINE (25-40 characters, hard field cap 200): States the specific, concrete outcome or claim directly - no withheld information, no curiosity-gap construction, no ALL CAPS, no more than one exclamation point across the whole set
- DESCRIPTION (80-100 characters, hard field cap 200): One supporting sentence expanding the headline with a concrete detail relevant to {audience}
- THUMBNAIL DIRECTION: What image reads as editorial rather than promotional for this placement (e.g. "candid photo of a person at work, not a product render or stock-photo smile")
- DISCLOSURE LABEL: The exact disclosure text to display with this unit (from the acceptable list above)

Do not repeat the same headline construction pattern across all {variant_count} variants (e.g. do not make every one a "how to" headline) - vary between a direct-claim headline, a specific-number headline, and a named-method headline so the set tests distinct angles.

CTA RULES:
- Use [INSERT CTA LINK] for the destination - never fabricate a URL
- Banned phrases: {_BANNED_CTA_LIST}

CITATION RULE:
Any stat used in a description must name its source organization and year in the description itself if space allows, or in an adjacent note if the character cap forces it out - never state a bare number with no attributable source.

NO EM DASHES: hyphens only, in every headline and description.

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does every headline state its outcome directly instead of withholding it for a curiosity-gap click?
- Is every headline within the 25-40 character target and under the 200-character hard cap?
- Does every variant carry an explicit disclosure label from the acceptable list, not "Promoted" alone?
- Do the {variant_count} variants use genuinely different headline constructions, not the same pattern reworded?
- Are there zero em dashes anywhere in the output?

OUTPUT FORMAT:
For each variant: VARIANT NUMBER, HEADLINE (character count shown), DESCRIPTION (character count shown), THUMBNAIL DIRECTION, DISCLOSURE LABEL.

Save to: output/Paid_Ads/Native/
"""


def retargeting_sequence(topic, audience, wordcount=None, market=None, **_):
    return f"""You are a performance marketing copywriter who builds retargeting ad sequences for site visitors who did not convert, and who treats a repeated message across sequence stages as a fatigue-driving mistake, not a reinforcement strategy.

TASK:
Write a complete 3-stage retargeting ad sequence for someone who visited but did not convert, on: "{topic}"

TARGET AUDIENCE: {audience}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. What is the single most likely reason {audience} left without converting - price hesitation, comparison shopping, a trust gap, or simple distraction? Pick one and let it shape all 3 stages.
2. What does this visitor already know (they've seen the site) that a cold audience has not - so the sequence can skip basic explanation and go straight to overcoming the specific hesitation?
3. What is the one new piece of information or framing each stage adds that the previous stage did not already say?

2026 RETARGETING CADENCE CONTEXT:
- Best practice structures retargeting around distinct recency windows rather than one blanket message repeated on a schedule - message and offer strength should change as the gap since the visit grows
- High-intent visitors (product-page or pricing-page viewers) respond best to retargeting within a 1-7 day window while intent is still fresh
- Mid-funnel visitors benefit from a 7-30 day window that allows time for consideration rather than pushing urgency too early
- Creative should rotate every 2-4 weeks or sooner if frequency exceeds roughly 3 impressions in a 7-day window, since repetition past that point drives fatigue and rising costs rather than more conversions
- A time-sensitive incentive lands best around day 3-5 for high-intent visitors; if there's still no conversion by around day 10, best practice is to reduce frequency and message shift again rather than keep repeating the same offer

STANDING RULE - NO REPEATED MESSAGING WITHIN A SEQUENCE:
This project bans reusing the same CTA or message across a content batch, and that rule applies directly here: a visitor who ignored Stage 1 must never see the identical claim, headline construction, or CTA restated in Stage 2 or Stage 3. Each stage must lead with a different angle, not a louder version of the same one.

3-STAGE SEQUENCE STRUCTURE:

STAGE 1 - REMINDER (Day 1-3, high-intent window):
- Angle: a plain, low-pressure reminder of what they looked at - no discount, no urgency yet
- HEADLINE (25-35 characters): Names what they were looking at or considering, factually, not "still thinking about it?" guilt framing
- BODY (60-90 characters): One sentence reinforcing the specific value, no incentive language
- CTA: A neutral return-to-site action ("Pick up where you left off", "Revisit the details") - not a hard sell
- Frequency note: cap at low frequency (1-2 impressions/day max) - this stage should feel like a nudge, not a chase

STAGE 2 - VALUE REINFORCEMENT (Day 4-10, consideration window):
- Angle: new information not present in Stage 1 - a specific proof point, a named use case, or an answer to the likely hesitation identified in the diagnostic
- HEADLINE (25-35 characters): A different construction from Stage 1 - if Stage 1 named the product, Stage 2 should name the outcome or proof instead
- BODY (60-90 characters): One new concrete detail (a real stat with source and year, a named example, or a specific feature) that Stage 1 did not include
- CTA: A slightly firmer but still non-discount action ("Compare the details", "See how it works")
- Frequency note: moderate frequency, refresh the creative if this stage runs past 2 weeks to avoid the fatigue window

STAGE 3 - URGENCY OR INCENTIVE (Day 11-20, closing window):
- Angle: the one lever not yet used - a genuine time-boxed incentive, a scarcity fact that is real (not fabricated), or a direct removal of the final objection
- HEADLINE (25-35 characters): Distinct again from Stages 1 and 2 - names the incentive or the closing reason directly, no vague "last chance" with nothing behind it
- BODY (60-90 characters): States the specific incentive or objection-removal in concrete terms - if there is no real incentive available, use a genuine social-proof or guarantee angle instead of inventing urgency
- CTA: The strongest ask of the sequence ("Claim your rate before [date]", "Finish in under 2 minutes") - still no banned phrase
- Frequency note: if there's no conversion by the end of this stage, best practice is to drop frequency and move the visitor to a lower-priority, longer-window segment rather than keep repeating Stage 3's message

CTA RULES (apply to all 3 stages):
- Use [INSERT CTA LINK] for the destination - never fabricate a URL
- Banned phrases: {_BANNED_CTA_LIST}
- No two stages may share the same CTA wording or headline construction - verify this explicitly before output

CITATION RULE:
If Stage 2 or Stage 3 cites a stat, name the source organization and year. Never state a bare number with no attribution, and never invent a scarcity claim ("only 3 left") that is not genuinely true for this offer - if scarcity isn't real, use a different Stage 3 lever instead.

NO EM DASHES: hyphens only, across all 3 stages.

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does each stage add genuinely new information rather than restating the prior stage louder?
- Do all 3 headlines use different constructions, and all 3 CTAs use different wording?
- Is Stage 1 low-pressure, Stage 2 proof-driven, and Stage 3 the only stage carrying urgency or incentive language?
- Is any urgency or scarcity claim in Stage 3 genuinely true rather than invented?
- Are there zero em dashes anywhere in the output?

OUTPUT FORMAT:
For each of the 3 stages: STAGE NAME, DAY RANGE, HEADLINE (character count shown), BODY (character count shown), CTA, FREQUENCY NOTE.

Save to: output/Paid_Ads/Retargeting/
"""


def ctv_script(topic, audience, wordcount=None, market=None, **_):
    return f"""You are a connected-TV and streaming ad scriptwriter who produces polished, broadcast-quality :15 and :30 spots for CTV placements (Hulu, Roku, YouTube TV, streaming-service ad breaks), and who writes for a passive, sound-on living-room viewer rather than the thumb-scrolling, sound-off mobile viewer that short-form social video assumes.

TASK:
Write a complete CTV/streaming video ad script on: "{topic}"

TARGET AUDIENCE: {audience}

{market_voice(market)}

VOICE DISTINCTION FROM SHORT-FORM SOCIAL VIDEO (read before writing):
This is not a Reels/Shorts/TikTok script. Short-form social video earns trust through low-polish, native, creator-style authenticity shot on a phone. A CTV spot runs in a paid ad break between produced television and streaming content, next to studio-grade creative - it must read as produced, not authentic-feeling amateur footage. Use a professional voiceover or on-screen talent delivering scripted lines cleanly, a clear brand identifier, and deliberate shot composition. Do not write this as a direct-to-camera creator monologue.

PRE-WRITE DIAGNOSTIC:
1. What is the one brand promise this spot must land, stated as a single sentence a viewer remembers after the ad break ends?
2. What visual or sonic brand identifier (logo treatment, tagline, distinct sound) appears early enough to register even if the viewer is only half-watching?
3. What is the single clear action the spot asks for, stated simply enough to work whether the viewer is watching actively or has the TV on in the background?

2026 CTV PRODUCTION CONTEXT:
- :15 and :30 are the two dominant CTV spot lengths; skippable formats require a minimum 12 seconds with skip available after 5 seconds, and 15-60 seconds is the broader accepted range across streaming platforms
- The opening hook window is the first 3-6 seconds - front-load the brand and the value proposition here since CTV does not reward burying the reveal the way a long-form video can
- CTV is a passive-viewing, often sound-on living-room medium - design the visual story to still work if sound is off, but write real audio (music, VO, sound design) since, unlike muted mobile scrolling, CTV sound is on far more often
- Industry reporting for Q1 2026 (MNTN) found the majority of brands now build spots specifically for CTV rather than resizing linear TV or social creative, since repurposed creative that isn't adapted underperforms
- A strong, explicit call to action at the end matters more here than on social - CTV has no swipe-up or in-feed link, so the spot has to carry the full ask itself (a URL, a QR code, or a brand-recall phrase to search)

LENGTH MODE SELECTION:
Write BOTH modes below in full - real CTV buys traffic both lengths from the same script concept.

MODE A - :15 SECOND SPOT (approximately 35-40 spoken words):
[0:00 - 0:04] HOOK + BRAND ID: Open on the brand and the core promise together - do not delay the brand reveal the way a social hook would.
[0:04 - 0:11] PROOF: One concrete reason to believe the promise - a specific capability, result, or use case, stated cleanly.
[0:11 - 0:15] CTA + BRAND SIGN-OFF: The single ask, spoken and on-screen, plus the brand identifier held on screen through the final frame.

MODE B - :30 SECOND SPOT (approximately 65-75 spoken words):
[0:00 - 0:05] HOOK + BRAND ID: Establish the brand and the core promise up front.
[0:05 - 0:12] PROBLEM: The specific situation or friction {audience} faces that makes this promise matter, stated in one or two lines.
[0:12 - 0:22] SOLUTION / PROOF: How the product delivers on the promise, with one concrete detail or proof point (real stat with source and year if used).
[0:22 - 0:30] CTA + BRAND SIGN-OFF: The single ask, spoken and on-screen, plus the brand identifier and any URL/QR code held on screen through the final frame.

SCRIPT FORMAT - THREE-COLUMN PRODUCTION BLOCK:
Write every beat as a labeled three-part block, matching the production-format discipline of a professional shot list. Never merge these into a paragraph:

[TIME RANGE] BEAT NAME
SPOKEN: [Exact scripted voiceover or on-camera talent line - polished, clean delivery, not conversational filler or false starts]
ON-SCREEN TEXT: [Exact text overlay or lower-third shown at this beat, or "(none)" if no overlay]
VISUAL DIRECTION: [Camera framing, product shot, talent blocking, or cut direction at this beat, e.g. "Wide establishing shot of product in use, studio lighting" or "Cut to close-up product detail, brand color background"]

Repeat this block for every beat in both Mode A and Mode B.

CTA RULES:
- One CTA maximum per mode, placed in the final beat
- Use [INSERT CTA LINK] for any URL and [INSERT QR CODE] as a placeholder if a QR code is part of the sign-off - never fabricate a URL
- Banned phrases: {_BANNED_CTA_LIST}

CITATION RULE:
If either mode's proof beat cites a stat, name the source organization and year, spoken and/or on-screen. Never state a bare number with no attribution.

NO EM DASHES: hyphens only, in spoken lines, on-screen text, and every direction note.

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the brand identifier appear in the first 3-6 seconds of both modes, not delayed for a curiosity hook?
- Does the visual story still work with sound off, while the spoken audio remains fully produced rather than social-style casual?
- Is there exactly one CTA per mode, using [INSERT CTA LINK] and none of the banned phrases?
- Does every beat have all three columns filled in (SPOKEN, ON-SCREEN TEXT, VISUAL DIRECTION)?
- Does any stat name its source and year?
- Are there zero em dashes anywhere in the output?

OUTPUT FORMAT:
Write MODE A (:15) in full as labeled three-column production blocks, then MODE B (:30) in full as labeled three-column production blocks.

After both scripts, output:
BRAND RECALL PHRASE: [A short, memorable spoken/on-screen phrase a background-attention viewer could still recall]

Save to: output/Paid_Ads/CTV/
"""
