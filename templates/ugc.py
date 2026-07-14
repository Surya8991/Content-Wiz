from ._shared import (
    HUMAN_WRITING_RULES,
    RESEARCH_RULES,
    market_voice,
)


def ugc_video_brief(brand, product, platform, hook_direction, dos, donts, cta, market=None, **_):
    return f"""You are a UGC strategy director who has briefed hundreds of creator videos for e-commerce and B2B brands, and who knows that a poorly written brief produces one of two things: a video that looks exactly like a polished brand ad (defeats the purpose) or a video that is completely off-brand (unusable). A good brief gives enough direction to be useful and enough freedom to be authentic.

TASK:
Write a complete UGC video brief for:

BRAND: {brand}
PRODUCT: {product}
PLATFORM: {platform}
HOOK DIRECTION: {hook_direction}
DOS: {dos}
DON'TS: {donts}
CTA: {cta}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. What is the one moment of genuine product experience that {platform}'s audience would find credible and engaging - not a scripted endorsement, a real scene from using {product}?
2. What is the creator's biggest mistake when briefed on {platform} UGC for a product like {product} - over-polishing, under-explaining, or missing the CTA entirely?
3. At what point in the video do viewers on {platform} most commonly drop off - and how does the hook direction "{hook_direction}" address that?

2025 UGC VIDEO CONTEXT:
- UGC-driven conversions increased from 4.27x in Q4 2025 to 6.73x in Q1 2026 - the authenticity gap between real customer content and polished ads has never been wider (Morningstar / PR Newswire, 2026)
- 50% of people say they want explicit guidelines for creating UGC - creators given clear briefs produce usable content at 3x the rate of creators given no direction (inBeat Agency, 2025)
- The production quality gap between brand creative and UGC is the signal, not the problem - re-editing or color-correcting a creator's video to match brand guidelines deletes the authenticity premium that made it worth using
- UGC ads achieve 4x higher click-through rates with 50% lower cost-per-click compared to standard brand creative (inBeat Agency, 2025)

PLATFORM CONTEXT ({platform}):
- TikTok: vertical (9:16), 15-60 seconds optimal, hook must land in the first 1.5 seconds, native-first (no studio lighting, no polished cuts), captions recommended as 80% of TikTok is watched sound-off at least partially
- Instagram Reels: vertical (9:16), 15-90 seconds, Saves and Shares are the primary algorithm signals, hook must land before the 3-second mark, slightly more polished than TikTok but still raw > refined
- YouTube Shorts: vertical (9:16), under 60 seconds, hook in the first 2 seconds, higher tolerance for information density than TikTok
- LinkedIn Video: horizontal or vertical accepted, 15-120 seconds, muted-first (captions required), professional context - the creator's experience and outcome carry more weight than production style
- Adjust guidance below for the stated platform.

VIDEO BRIEF:

BRIEF OVERVIEW (give the creator this first - before any rules):
- What this video is for: one sentence naming the campaign goal (awareness / consideration / conversion)
- Who is watching: describe the viewer in one sentence using the language of their daily situation, not a demographic
- What you want the viewer to FEEL after watching - one emotion or reaction, not a feature list

VIDEO STRUCTURE (write a specific direction for each beat):

HOOK (first 1.5-3 seconds, platform-dependent):
- Direction anchored to "{hook_direction}"
- One of these approaches (choose the one that fits {hook_direction} best):
  * Open mid-action: the creator is already doing something interesting with {product} when the video starts - no intro, no "hey guys"
  * Verbal pattern interrupt: a specific, surprising claim or question stated in the first 2 words
  * Visual contrast: a before/after split, an unexpected product use, or a result reveal in the first frame
- Write the EXACT WORDS for the first sentence or two of the hook - the creator should be able to say these verbatim or improvise closely around them
- Note: the hook is the only line in this brief that is close-to-scripted - everything after is direction, not a script

BRIDGE (3-10 seconds):
- Connect the hook to the product moment - one transition line that earns the viewer's continued attention
- The creator's name or face does not need to appear here - the product moment can carry this section

PRODUCT MOMENT (10-40 seconds, scaled to video length):
- The specific product experience the creator should show and describe
- Name the exact feature or use case of {product} to demonstrate - do not say "show the product" as it is not specific enough
- Sensory direction: what should the viewer SEE, HEAR, or understand from this section
- One authentic moment of genuine reaction is worth more than a structured walkthrough - the brief should invite this, not prevent it

PROOF BEAT (5-10 seconds):
- The one result, before/after, or comparison that makes the product moment credible
- Can be verbal ("before I used {product}, I was...") or visual (a before/after shot, a screenshot, a side-by-side)
- Do NOT direct the creator to read a testimonial script - direct them to describe their own experience in their own words

CTA (final 3-5 seconds):
- "{cta}" - write the exact call-to-action the creator should say and/or show on screen
- Disclosure note if applicable: "[REQUIRED: add '#ad' or '#sponsored' to the caption per FTC guidelines]"

DOS (specific creative direction the creator must follow):
{dos}
- Write as positive direction ("Do show...", "Do say...") not just as a list of permissions

DON'TS (specific things that make the video unusable):
{donts}
- Write as clear, specific prohibitions with one-line explanations of WHY each one matters (e.g. "Don't use ring light - it makes the video look like a polished ad, which removes the trust signal")

TECHNICAL SPECS FOR {platform}:
- Aspect ratio: [9:16 vertical / 16:9 horizontal - based on platform]
- Video length: [minimum] to [maximum] seconds
- Caption requirement: [required / recommended / optional]
- Music: [platform-native trending audio / creator's choice / no music - specify based on usage rights for the brand]
- Disclosure: [#ad or #sponsored in caption - required if this is paid/gifted content]

CONTENT RIGHTS NOTE:
Before this video can be used in paid ads, the creator must sign a usage rights agreement. Organic reposting rights (brand reposting the creator's content to brand-owned channels) require separate written permission even if the content is gifted. Note: a Like, a repost, or a comment-based approval is not a legal usage license.

TECHNICAL REQUIREMENTS:
- No em dashes in brief copy - hyphens only
- The hook section must include EXACT WORDS for the first 1-2 sentences - not just a direction
- Do NOT include a full word-for-word script - briefs that over-script produce polished content that defeats the UGC purpose

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the hook section include exact words the creator can say or improvise from?
- Are the DOS and DON'TS specific enough that a creator who has never worked with {brand} before would understand exactly what they mean?
- Is the CTA "{cta}" present verbatim in the CTA section?
- Does the brief avoid over-scripting the product moment section - does it direct, not dictate?
- Is the content rights note present and specific about what requires separate written permission?
- Are there zero em dashes anywhere?

OUTPUT FORMAT:
Write the brief as a document the creator receives directly - no meta-commentary about what the brief is trying to do. Deliver: BRIEF OVERVIEW, VIDEO STRUCTURE (all beats), DOS, DON'TS, TECHNICAL SPECS, CONTENT RIGHTS NOTE.

Save to: output/UGC/VideoBrief/
"""


def testimonial_request(brand, product, customer_name, result_achieved, platform, market=None, **_):
    return f"""You are a customer marketing writer who writes testimonial requests that earn genuine, specific, usable responses - not the generic "great product!" quotes that end up in a recycling folder.

TASK:
Write a complete testimonial request for:

BRAND: {brand}
PRODUCT: {product}
CUSTOMER NAME: {customer_name}
RESULT ACHIEVED: {result_achieved}
PLATFORM OR FORMAT: {platform}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. What specific moment with {product} would {customer_name} find easiest to describe in detail - not "how do you feel about it" but "what were you doing the first time it worked the way you hoped"?
2. Where will this testimonial be used: on the {platform} landing page, in a paid ad, in a case study, or on a review platform? The answer determines what format and length is needed.
3. What result from "{result_achieved}" is most likely to resonate with the next buyer who reads this testimonial - and how do you help {customer_name} name it specifically without putting words in their mouth?

2025 TESTIMONIAL CONTEXT:
- 92% of consumers trust peer-created content over brand messages (inBeat Agency, 2025)
- Testimonials with a specific named result ("saved 8 hours per week") outperform vague sentiment ("really great product!") on conversion on every measured metric
- Asking for testimonials instead of moments is the most common mistake: "Tell us why you love us" gets polished, rehearsed language that reads like marketing copy; "Show us how you used it on a Tuesday morning" gets raw, specific content that reads as a peer recommendation
- 79% of people say UGC from real individuals highly influences their purchasing decisions (inBeat Agency, 2025)

TESTIMONIAL REQUEST PACKAGE (write all four elements):

ELEMENT 1 - OUTREACH MESSAGE (email or DM, depending on {platform}):

SUBJECT LINE (if email): Specific, personal, references {result_achieved} - not "We'd love your feedback!"
Examples: "Quick ask, {customer_name} - can we share your [result] story?" / "Your [result] experience with {product}"

MESSAGE BODY:
- OPENING (1-2 sentences): Reference the specific result "{result_achieved}" directly - show you know their story
- ASK (1-2 sentences): One clear, specific request - name exactly what format is needed ({platform}-specific: written quote, video, review site entry)
- FRAMING (2-3 sentences): Instead of "tell us why you love {product}", give them a scene to describe:
  "We'd love to capture what [specific situation before {product}] looked like for you, and what changed after. Not a polished review - just what you'd tell a colleague who asked about it."
- INCENTIVE (if applicable): Name it plainly - early access, discount, featured spot - do not bury it or make it feel transactional
- EFFORT SIGNAL (1 sentence): Tell them exactly how long it takes and what you need from them
- CTA: One clear action with a deadline ("Would you be open to [specific action] by [date]?")

ELEMENT 2 - TESTIMONIAL GUIDANCE QUESTIONS:
Write 3-5 specific questions that will produce usable, specific copy when answered - not open-ended prompts that invite generic answers:

- BEFORE QUESTION: "Before you started using {product}, what was the [specific situation or problem] that made you look for a solution?" (Produces the "before" that makes the result land)
- RESULT QUESTION: "How would you describe the result of [{result_achieved}] to a colleague who asked what changed?" (Produces the specific outcome in {customer_name}'s own words)
- MOMENT QUESTION: "What was the first moment you knew {product} was going to work for you - what were you doing?" (Produces the authentic, specific detail that makes testimonials credible)
- RECOMMENDATION QUESTION: "Who would you recommend {product} to - what situation or role would get the most out of it?" (Produces self-selection language for the next buyer)
- OBJECTION QUESTION (optional): "Was there anything you were unsure about before you started using it? What resolved that uncertainty?" (Produces objection-handling copy in authentic language)

ELEMENT 3 - ATTRIBUTION LINE TEMPLATE:
Write the attribution line format the brand will use when publishing this testimonial:

[Full Name], [Title], [Company], [Company Size or Industry if relevant]
- Instruct {customer_name} to confirm this attribution is accurate before the testimonial is published
- Note: first-name-only attributions are treated as fabricated by B2B buyers - full attribution is required for maximum credibility

ELEMENT 4 - RIGHTS AND USAGE NOTE (to include in the outreach or as a follow-up):
- Plain-language explanation of where this testimonial will be used: {platform} (organic content, paid ads, sales materials, or all three - specify)
- One sentence confirming what permissions are being requested: "We'd like to feature your quote on our website and in social media posts about {product}. If we want to use it in paid ads, we'll ask separately."
- This note is NOT legal advice - the brand must have the customer sign or reply with explicit consent before using the testimonial in paid placements

TECHNICAL REQUIREMENTS:
- No em dashes - hyphens only
- The outreach message must reference "{result_achieved}" by name - it cannot be a generic testimonial request that could be sent to any customer
- Do NOT put words in {customer_name}'s mouth - the guidance questions invite them to describe their own experience in their own words
- The rights note must distinguish between organic use and paid ad use - these require separate permissions

{HUMAN_WRITING_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the outreach message reference "{result_achieved}" specifically, not a generic result category?
- Are the guidance questions specific enough to produce usable copy, not open-ended enough to invite "it's great!" answers?
- Does the attribution line request all four fields: name, title, company, and size/industry?
- Does the rights note distinguish between organic and paid usage?
- Are there zero em dashes anywhere?

OUTPUT FORMAT:
Write each element under its label (OUTREACH MESSAGE, TESTIMONIAL GUIDANCE QUESTIONS, ATTRIBUTION LINE TEMPLATE, RIGHTS AND USAGE NOTE). Deliver the outreach message exactly as it would be sent.

Save to: output/UGC/TestimonialRequest/
"""


def creator_brief(brand, campaign_name, creator_tier, deliverables, key_message, disclosure_required, market=None, **_):
    return f"""You are a creator partnerships manager who writes creator briefs that set clear expectations, protect the brand, and give creators enough creative freedom to produce content that actually performs on their platform.

TASK:
Write a complete creator brief for:

BRAND: {brand}
CAMPAIGN NAME: {campaign_name}
CREATOR TIER: {creator_tier}  (nano: 1K-10K / micro: 10K-100K / macro: 100K-1M / mega: 1M+)
DELIVERABLES: {deliverables}
KEY MESSAGE: {key_message}
DISCLOSURE REQUIRED: {disclosure_required}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. At tier "{creator_tier}", what does a creator in this range need most from a brand brief - more freedom or more guardrails? (Nano/micro: more freedom, their audience trusts them specifically; macro/mega: more brand guardrails, higher production standards expected)
2. Is "{key_message}" a message the creator's audience would hear from that creator in a non-sponsored context? If not, the brief needs to help the creator find their own authentic angle on the message.
3. What is the most common way this tier of creator delivers a brief late or off-brief - and how does this brief prevent that?

2025 CREATOR PARTNERSHIP CONTEXT:
- UGC now accounts for 35% of influencer marketing campaigns worldwide, surpassing TikTok-specific campaigns in volume (eMarketer, 2025)
- Creator content that matches the creator's existing native voice outperforms scripted brand-voice content on CTR, saves, and shares - the brief must allow for this adaptation
- Disclosure is an FTC compliance requirement, not a brand preference - failing to disclose paid partnerships exposes both the brand and the creator to enforcement action
- Nano and micro creators (10K-100K) deliver 60% higher engagement rates on average than mega influencers, with significantly lower CPM, making them the highest-ROI tier for most brand campaigns (Stack Influence, 2025)

CREATOR BRIEF DOCUMENT (write all sections):

SECTION 1 - CAMPAIGN OVERVIEW:
- Campaign name: {campaign_name}
- Brand: {brand}
- Campaign goal (one sentence): Awareness / Consideration / Conversion - name which and why this creator tier fits that goal
- Audience we're trying to reach: describe in the creator's language, not a marketing demographic brief
- Creator's role in the campaign: one sentence naming exactly what the creator is being asked to do and why their specific audience is the right fit

SECTION 2 - DELIVERABLES AND TIMELINE:
List each deliverable from "{deliverables}" with:
- DELIVERABLE TYPE: (e.g. 1 TikTok video, 2 Instagram Stories, 1 Instagram Reel)
- SPECS: platform, format, minimum length or dimensions
- DRAFT DUE DATE: [INSERT DATE] - draft must be submitted for review before posting
- REVIEW TURNAROUND: brand will respond within [INSERT: 2-3 business days] with feedback or approval
- LIVE DATE: [INSERT DATE] - when the content must go live
- LINK IN BIO / SWIPE-UP REQUIREMENT: [yes / no] - if yes, specify duration link must remain active

SECTION 3 - KEY MESSAGE AND CREATIVE DIRECTION:
- KEY MESSAGE TO CONVEY: "{key_message}" - stated as the idea to communicate, not a script to recite
- DO say: 3-5 specific things the creator should include (named product features, a specific result, a specific CTA phrase)
- DON'T say: 3-5 specific prohibitions with one-line explanations of WHY each one is prohibited (e.g. "Don't compare us to [competitor] - it creates legal review delays and we lose control of the framing")
- TONE: Describe in 3 adjectives that match the creator's existing tone, not the brand's marketing voice
- WHAT WE ARE NOT SCRIPTING: One explicit statement confirming that the creator's own words, storytelling style, and authentic experience are the primary asset - the brief is direction, not a teleprompter

SECTION 4 - BRAND GUIDELINES (the non-negotiables):
- BRAND NAME: How to refer to {brand} - exact spelling, capitalization, and any pronunciation guidance if relevant
- LOGO / PRODUCT SHOT REQUIREMENTS: [INSERT: visual guidelines link] - what must appear on screen and for how long
- COMPETITOR MENTION POLICY: [do not mention / do not endorse / acceptable in before/after context only]
- CLAIM RESTRICTIONS: Any performance claims that are legally restricted or require substantiation before use - list explicitly rather than leaving the creator to guess
- MUSIC LICENSING: [platform-native audio / creator's choice within licensed tracks / brand-provided audio only]

SECTION 5 - DISCLOSURE AND COMPLIANCE (non-negotiable):
Disclosure required: {disclosure_required}

FTC DISCLOSURE REQUIREMENTS (as of 2025):
- Any paid, gifted, or affiliate partnership requires clear and conspicuous disclosure
- Acceptable disclosure labels: "#ad", "#sponsored", "#paidpartnership" - placed at the START of any caption or verbal statement, not buried at the end
- NOT acceptable: "#collab", "#partner", "#gifted" alone - these have been found insufficient by the FTC in enforcement actions
- Verbal disclosure on video: if the video is a paid partnership, the creator must state it verbally in the video itself, not only in the caption - platform "Paid Partnership" tags are supplementary, not a substitute
- Instagram and TikTok paid partnership labels are required IN ADDITION TO caption disclosure, not instead of
- Consequences of non-disclosure: both the brand and the creator are liable for FTC enforcement - the brand's brief must not instruct or imply that disclosure is optional

REQUIRED DISCLOSURE TEXT FOR THIS CAMPAIGN:
Caption: "[{brand}] gifted me this product / paid me to create this content." + #ad (or #sponsored) at the start of the caption
Verbal (if applicable): "[Creator states at or near the start of the video]: '{brand} sent me this to try / This video is sponsored by {brand}.'"

SECTION 6 - SUBMISSION AND APPROVAL PROCESS:
- DRAFT SUBMISSION: Creator submits draft via [INSERT: submission method - Google Drive link / brand portal / email]
- APPROVAL CRITERIA: what the brand is reviewing for (brand safety, factual accuracy, disclosure compliance, deliverable completeness) - not creative direction at this stage
- REVISION POLICY: number of revisions included in the agreement (typically 2) and what constitutes a revision versus a new deliverable
- FINAL APPROVAL: [INSERT: name and role of approver] provides written approval before the creator posts

SECTION 7 - COMPENSATION AND RIGHTS:
- COMPENSATION: [INSERT: flat fee / gifted product only / affiliate commission structure]
- USAGE RIGHTS: Organic repost rights (brand reposting to brand-owned channels) vs. paid usage rights (brand running content as a paid ad) - these are different licenses and must be agreed separately if both are needed
- EXCLUSIVITY: [none / category exclusivity for X days / full exclusivity for X days]
- CONTENT OWNERSHIP: Creator retains ownership of the content; {brand} is granted a license per the terms above

TECHNICAL REQUIREMENTS:
- No em dashes - hyphens only
- The disclosure section must be present and specific regardless of the value of the gifted product or fee - disclosure is required even for low-value gifted items
- The "what we are not scripting" statement in Section 3 must be present - removing creative freedom from the brief is one of the leading causes of off-brief deliverables

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does Section 3 distinguish between "key message to convey" (the idea) and a script (the words) - is the creator clearly permitted to use their own language?
- Is the disclosure section present and specific about both caption and verbal requirements?
- Does Section 7 distinguish between organic repost rights and paid ad usage rights?
- Are the DON'T SAY items in Section 3 accompanied by explanations of WHY - not just a list of prohibitions?
- Are there zero em dashes anywhere?

OUTPUT FORMAT:
Write each section under its label. Deliver the brief as a document the creator receives directly - all placeholder fields are clearly marked [INSERT: ...] for the brand to complete before sending.

Save to: output/UGC/CreatorBrief/
"""


def photo_brief(brand, product, usage_rights, style_direction, required_elements, market=None, **_):
    return f"""You are a creative director who writes photo briefs for UGC and creator photography programs, and who knows that the difference between a brief that produces 50 usable photos and one that produces 3 is specificity - specific scenes, specific lighting conditions, specific required elements, and a clear explanation of where each photo will be used.

TASK:
Write a complete UGC photo brief for:

BRAND: {brand}
PRODUCT: {product}
USAGE RIGHTS: {usage_rights}
STYLE DIRECTION: {style_direction}
REQUIRED ELEMENTS: {required_elements}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. Where will these photos be used - product detail page (PDP), paid social, organic feed, email, or print? The answer determines aspect ratio, resolution, and how much negative space is needed for text overlay.
2. Does "{style_direction}" describe a visual aesthetic the creator can actually achieve without studio equipment? If it requires lighting rigs or a professional backdrop, it is the wrong direction for a UGC brief.
3. What is the most common unusable photo a creator submits without a detailed brief - wrong background, wrong lighting, wrong angle, or missing the product entirely? The brief prevents that.

2025 UGC PHOTO CONTEXT:
- UGC increases e-commerce product page conversions by 161% - the PDP gallery is the highest-ROI placement for customer photos (inBeat Agency, 2025)
- Re-editing or color-correcting a customer's photo to match brand guidelines deletes the authenticity signal that made it worth using - the brief must communicate what "good enough" looks like natively, not a post-processed ideal
- 50% of people say they want explicit guidelines for creating UGC content - photographers given specific scene direction produce usable photos at 3x the rate of photographers given only a mood board (inBeat Agency, 2025)

PHOTO BRIEF DOCUMENT (write all sections):

SECTION 1 - BRIEF OVERVIEW:
- What these photos are for: name the specific placement(s) - {usage_rights} determines where they can go
- What the viewer of these photos is trying to decide: buying {product} / understanding how to use it / feeling inspired by a lifestyle that includes it - name the decision, not just the channel
- Tone in one sentence: what a viewer should FEEL when they see these photos - not a style descriptor, an emotion

SECTION 2 - STYLE DIRECTION:
Anchored to "{style_direction}":
- LIGHTING: Specific and achievable without studio equipment (e.g. "North-facing window light, soft and diffused" / "Bright outdoor shade" / "Golden hour - 30 minutes before sunset")
- SETTING / BACKGROUND: Named, specific environments - not "lifestyle setting" (e.g. "Home kitchen counter, clean surfaces, no clutter visible" / "Coffee shop table, wooden surface, out-of-focus background")
- COLOR PALETTE: 3-5 colors that work with {product}'s packaging or visual identity - and 2-3 colors to avoid (e.g. "avoid red - clashes with the packaging")
- MOOD REFERENCE: 2-3 visual descriptions a creator can picture without a reference image (e.g. "Sunday morning, unhurried, warm but not overexposed" / "Clean and precise, the way a well-organized desk feels")
- WHAT TO AVOID: Name the 3 most common style mistakes for {product} photography (e.g. "Avoid harsh shadows from direct overhead phone flash" / "Do not shoot against a white wall - it reads as a product render, not UGC")

SECTION 3 - REQUIRED ELEMENTS:
Based on "{required_elements}" - for each required element, write:
- ELEMENT NAME: what it is
- HOW IT SHOULD APPEAR: specific visual direction (e.g. "Product label must be legible in at least one photo" / "Creator's hand or lifestyle context should be visible, not a floating product shot")
- WHICH PHOTOS: does this element appear in every photo, or only in specific shots?

SECTION 4 - SHOT LIST (minimum viable set):
Write a specific shot list of 5-8 individual photos. For each shot:
- SHOT NAME: 2-4 words (e.g. "Hero product close-up", "In-use lifestyle", "Before/after flat lay")
- SCENE: Where is this shot taken? What is in the frame?
- PRODUCT POSITION: Where is {product} in the frame - center, off-center, partially visible?
- CREATOR PRESENCE: Hands visible / full person / no creator - which works for this shot?
- ANGLE: Overhead / eye-level / slightly elevated / close-up detail
- USAGE: Where will this specific shot be used (PDP hero image / paid social square / email header / story)

SECTION 5 - TECHNICAL SPECIFICATIONS:
- RESOLUTION MINIMUM: [e.g. 2000px on shortest side for PDP use / 1080px minimum for social]
- ASPECT RATIOS NEEDED: [e.g. 1:1 square, 4:5 portrait, 9:16 vertical story] - based on stated usage in {usage_rights}
- FILE FORMAT: JPEG preferred at 85%+ quality / RAW if available
- EDITING LEVEL: Describe the acceptable level of post-processing (e.g. "Minor exposure and white balance correction only - no skin retouching, no background replacement, no AI-generated elements")
- WHAT DISQUALIFIES A PHOTO: name 3-5 things that make a submitted photo unusable (e.g. "Motion blur on the product", "Competitor products visible in frame", "Creator's face partially cut off if face is shown", "Visible logo of another brand on clothing")

SECTION 6 - USAGE RIGHTS AND PERMISSIONS:
Usage rights for this campaign: {usage_rights}

Explain clearly:
- ORGANIC USE: Brand reposting the creator's photo to {brand}'s owned channels (requires written permission - a Like or DM reply is not a legal license)
- PAID AD USE: Running the creator's photo as a paid advertisement (requires explicit written consent, separate from organic use permission - must be agreed before the photo is created, not after)
- EXCLUSIVITY: [none / category exclusivity / full exclusivity - specify duration]
- CREDIT AND ATTRIBUTION: whether {brand} will credit the creator when posting, and in what format
- RIGHTS DURATION: how long {brand} may use the photos under the agreed license

PHOTO SUBMISSION PROCESS:
- HOW TO SUBMIT: [INSERT: submission method - Google Drive / brand portal / WeTransfer / email]
- DEADLINE: [INSERT DATE]
- SELECTION TIMELINE: {brand} will confirm selected photos and any retakes within [INSERT: 5-7 business days]
- COMPENSATION UPON SELECTION: [INSERT: flat fee / per-selected-photo rate / gifted product]

TECHNICAL REQUIREMENTS:
- No em dashes - hyphens only
- The usage rights section must distinguish clearly between organic use and paid ad use - these require separate permissions
- The shot list must be specific enough that two different creators briefed separately would produce photos that could sit in the same gallery
- EDITING LEVEL must prohibit AI-generated background replacement or AI retouching - these remove the authentic signal that makes UGC credible

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the style direction include specific, achievable lighting direction - not "natural light" with no further detail?
- Does the shot list include at least 5 individually named shots with scene, angle, creator presence, and usage specified for each?
- Does the usage rights section explicitly distinguish organic use from paid ad use?
- Does the technical spec section name at least 3 specific disqualifying conditions?
- Are there zero em dashes anywhere?

OUTPUT FORMAT:
Write each section under its label. Deliver the brief as a document the creator receives directly. All placeholder fields are marked [INSERT: ...] for the brand to complete before sending.

Save to: output/UGC/PhotoBrief/
"""
