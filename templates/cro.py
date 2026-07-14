from ._shared import (
    BANNED_CTA_PHRASES,
    HUMAN_WRITING_RULES,
    RESEARCH_RULES,
    market_voice,
)

_BANNED_CTA_LIST = ", ".join(f'"{p}"' for p in BANNED_CTA_PHRASES)


def landing_page_lead_gen(brand, offer, audience, cta_text, social_proof, market=None, **_):
    return f"""You are a conversion copywriter who has written landing pages that generate leads at 15-30% opt-in rates for B2B and professional brands. You understand that a lead-gen page has one job: exchange the offer for the visitor's contact information, and every element either drives that exchange or gets cut.

TASK:
Write a complete lead-gen landing page for: "{brand}"

OFFER: {offer}
TARGET AUDIENCE: {audience}
PRIMARY CTA TEXT: {cta_text}
SOCIAL PROOF ANCHOR: {social_proof}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. What is the single outcome {audience} gets from {offer} - stated as a result they can describe to a colleague in one sentence?
2. What is the most likely objection that stops {audience} from filling out the form at the moment they hover over the CTA button?
3. What is the minimum information needed to deliver {offer} - that is the maximum number of form fields.

2025 LEAD-GEN PAGE CONTEXT:
- Pages with 4 form fields convert 120% better than the industry average of 11 fields (SEO Sherpa, 2026)
- Personalized CTAs outperform generic ones by 202% - the CTA label must name what happens after the click, not just "Submit"
- 83% of landing page traffic is mobile - every copy block must be readable in 3 seconds on a phone screen
- Social proof placed directly above the CTA removes last-moment hesitation for visitors who have already scrolled to the bottom

PAGE SECTIONS (write each section in full, in this order):

SECTION 1 - HEADLINE:
- One sentence naming the outcome {audience} gets from {offer}
- Not the product name, not "{brand}", not a tagline - the direct answer to "what will I get?"
- Good: "Get 3 Hours Back Every Week" / Weak: "Introducing {brand}'s New Tool"
- 8 words maximum, present tense

SECTION 2 - SUBHEADLINE (1-2 sentences):
- Who this is for and how it works at a high level
- Bridge between the headline promise and the explanation below
- Name {audience} explicitly so they self-identify

SECTION 3 - HERO STATEMENT (2-3 sentences):
- Expand the headline without repeating it
- Describe the situation {audience} is in right now, then the situation they will be in after {offer}
- Concrete, specific language - no "holistic" or "comprehensive"

SECTION 4 - BENEFITS LIST (3-5 bullets):
- Outcomes, not features - each bullet answers "so what?" for {audience}
- Format: "[Specific result] - [one-sentence explanation of how]"
- Include one quantified outcome if a real number is available for this offer

SECTION 5 - SOCIAL PROOF BLOCK:
- Anchor: {social_proof}
- Format: direct quote, full name, title/company, and one specific result the person achieved
- If quoting a metric ("saved 5 hours a week"), that metric must be real and attributable - do not fabricate proof
- Placement note: this block appears immediately above the CTA, not at the bottom of the page

SECTION 6 - LEAD CAPTURE FORM:
- Headline above form: one action-oriented line naming exactly what {audience} is getting (e.g. "Get Your Free [Offer Name]")
- Field list: name only the fields required to deliver {offer} - maximum 4
- CTA button label: "{cta_text}" - verify this matches the headline promise
- Microcopy directly below the button: one friction-reducing line (e.g. "No credit card required.", "Unsubscribe anytime.", "Delivered to your inbox in 2 minutes.")
- Note: this microcopy is the objection handler - it must remove the single most common hesitation for {audience}

SECTION 7 - OBJECTION HANDLER (below the form, optional but high-leverage):
- One FAQ-style question phrased as the real objection {audience} has
- One direct 1-2 sentence answer that removes it
- Example: "Will I get spammed?" / "One email with your [offer]. No weekly newsletters unless you opt in."

TECHNICAL REQUIREMENTS:
- No navigation menu anywhere on the page - every link that is not the CTA reduces conversion
- No em dashes - hyphens only
- No passive voice in the headline or CTA
- Page sections appear in the exact order listed above
- Banned CTA phrases (do not use in the button label or microcopy): {_BANNED_CTA_LIST}

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the headline name an outcome, not a product or brand name?
- Is the CTA button label "{cta_text}" - and does it describe what happens after the click?
- Is social proof placed above the CTA button, not at the page bottom?
- Does the form have 4 or fewer fields?
- Does the microcopy below the button address the single most likely hesitation for {audience}?
- Are there zero em dashes anywhere in the copy?

OUTPUT FORMAT:
Write each section under its label (HEADLINE, SUBHEADLINE, HERO STATEMENT, BENEFITS LIST, SOCIAL PROOF BLOCK, LEAD CAPTURE FORM, OBJECTION HANDLER). Deliver the final page copy exactly as it would appear on the page - no bracketed placeholders except [INSERT CTA LINK] for the form destination URL.

Save to: output/CRO/LeadGen/
"""


def landing_page_sales(brand, product, key_benefit, price_point, cta_text, market=None, **_):
    return f"""You are a direct-response copywriter who builds sales landing pages for high-ticket and mid-market products, and who knows that a sales page is a written sales conversation that has to earn trust before it earns the purchase.

TASK:
Write a complete sales landing page for: "{brand}" - "{product}"

KEY BENEFIT: {key_benefit}
PRICE POINT: {price_point}
PRIMARY CTA TEXT: {cta_text}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. At {price_point}, what is the single biggest purchase hesitation for a buyer who has already read the product description and is on this page?
2. What is the one proof point - a named result, a case study metric, a guarantee term - that removes that hesitation better than any other argument?
3. What is the cost of NOT buying? Name the specific situation {brand}'s buyers remain stuck in without {product}.

2025 SALES PAGE CONTEXT:
- Pages with a single offer convert 266% better than pages with multiple offers (SEO Sherpa, 2026)
- Adding video to a landing page increases conversions by up to 86% - flag where a product demo or testimonial video would go
- Social proof nearest to the CTA removes last-click hesitation - place proof at every stage where doubt spikes
- The objection handler immediately below the CTA is one of the highest-leverage improvements on any sales page

PAGE SECTIONS (write each in full, in this order):

SECTION 1 - HERO BLOCK:
- HEADLINE (one sentence): The specific outcome the buyer gets from {product}. Not "{brand}", not "{product}" - the result.
- SUBHEADLINE (1-2 sentences): Who this is for and the mechanism at a high level
- VIDEO PLACEHOLDER: "[INSERT: 60-90 second product walkthrough or customer testimonial video]"
- CTA BUTTON (above the fold): "{cta_text}" - with microcopy naming the price or the first commitment step so there is no price-shock later

SECTION 2 - PROBLEM SECTION (2-3 short paragraphs):
- Name the specific, painful situation a buyer is in before {product}
- Use second-person ("you"), present tense - describe their current state concretely
- One sentence naming the cost of the status quo: what it costs in time, money, or outcome

SECTION 3 - SOLUTION INTRODUCTION (2-3 sentences):
- Introduce {product} by the result it produces, not by its feature list
- Name the mechanism: how it solves the problem at a high level
- One sentence connecting the problem to the product without a hard sell

SECTION 4 - BENEFITS AND FEATURES (3-5 items):
- Lead with the outcome, then explain the feature that produces it
- Format: "OUTCOME. The [feature/mechanism] that makes it possible."
- Include one quantified benefit where a real number is available

SECTION 5 - SOCIAL PROOF BLOCK (place this before the price reveal):
- 2-3 direct customer quotes with full name, title, company, and one specific result
- If {price_point} is above typical impulse territory, include at least one quote that speaks to ROI or value relative to cost
- Logos of recognizable brands using {product} if available - placeholder: "[INSERT: 3-6 customer logos]"

SECTION 6 - PRICING AND OFFER BLOCK:
- Price: {price_point} - stated clearly, not buried
- What is included at this price - bullet list of deliverables or access rights
- Risk-reversal: the guarantee or return policy, stated in plain language (e.g. "30-day money-back guarantee, no questions asked")
- Urgency or scarcity if genuine - do NOT invent a deadline or "limited spots" claim that is not real

SECTION 7 - FINAL CTA BLOCK:
- CTA button: "{cta_text}"
- Objection handler below the button: one 1-2 sentence line removing the single most common purchase hesitation at {price_point}
- Secondary proof: one additional customer quote or a stat placed here, not used in Section 5

TECHNICAL REQUIREMENTS:
- No navigation menu - every exit link reduces the conversion probability
- No em dashes - hyphens only
- CTA button "{cta_text}" appears at least 3 times: above the fold (Section 1), after Section 5, and in Section 7
- Price is stated plainly in Section 6, not hidden behind a "contact us for pricing" deflection
- Banned phrases: {_BANNED_CTA_LIST}

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the hero headline name an outcome, not a product name or brand?
- Does social proof appear before the price is revealed?
- Is the price stated plainly with the full cost of the offer bundled together, not deconstructed into confusing tiers?
- Is the guarantee stated clearly enough that a skeptical buyer reading it once would trust it?
- Does the CTA button label "{cta_text}" describe what happens immediately after the click?
- Are there zero em dashes anywhere in the copy?

OUTPUT FORMAT:
Write each section under its label. Deliver the full page copy exactly as it would appear on the page. Use [INSERT CTA LINK] as the button destination placeholder and [INSERT: ...] for visual placeholders.

Save to: output/CRO/Sales/
"""


def cta_variants(action, benefit, urgency_level, market=None, **_):
    return f"""You are a conversion copywriter who writes CTA button labels and surrounding microcopy, and who knows that a CTA is the most-read and most A/B-tested element on any landing page or email.

TASK:
Write 3 distinct CTA variants for the following parameters:

ACTION: {action}
BENEFIT: {benefit}
URGENCY LEVEL: {urgency_level}  (low / medium / high)

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. What does the visitor get in the next 60 seconds after clicking - what is the immediate, concrete next step?
2. What is the one word or phrase that most directly names that next step without being generic?
3. At urgency level "{urgency_level}", what is the honest reason this matters now - or is there no real urgency and the copy should not manufacture it?

2025 CTA CONTEXT:
- Personalized CTAs (matching the exact language of the traffic source) outperform generic ones by 202% (SEO Sherpa, 2026)
- The CTA label is the most A/B-tested element on any conversion page - three structurally different variants are needed, not the same label reworded
- Button labels that describe the post-click outcome ("Get My Free Guide") outperform labels that describe the click action ("Submit") by 14-25% in most split tests
- Urgency language increases conversions only when it reflects a genuine constraint - manufactured urgency ("Last chance!") that disappears on the next visit destroys trust and conversion long-term

THREE VARIANTS (each must use a structurally different pattern - do not reuse the same construction):

VARIANT 1 - OUTCOME-LED:
Pattern: "[Verb] My/Your [Specific Outcome]"
- The verb names what happens, the noun names what the visitor walks away with
- Examples: "Get My Free Audit" / "Start My Trial" / "Book My Strategy Call"
- Write this as a first-person label ("Get My...") if the audience is an individual, second-person ("Get Your...") if writing in a voice directly from the brand
- MICROCOPY (1 line below the button): removes the friction between "clicking" and "committing" - e.g. "No credit card required." / "Takes 2 minutes." / "Instant access."

VARIANT 2 - ACTION + TIMEFRAME:
Pattern: "[Action] in [Specific Timeframe]"
- Names what changes and how fast
- Timeframe must be honest - if the action is not genuinely completable in that window, do not use it
- Example: "Close the First Deal in 14 Days" / "Launch Your First Ad in 30 Minutes"
- MICROCOPY: addresses the most common hesitation about the timeframe claim being realistic

VARIANT 3 - URGENCY VARIANT (scaled to urgency level "{urgency_level}"):
- LOW: A soft call to relevance - "This is for [audience type] who [situation]" - no time pressure, just specificity
- MEDIUM: A forward-looking frame - "Where will [audience] be in 90 days?" - creates mild internal urgency without a deadline
- HIGH: A real, honest constraint - states the actual reason this window closes (a real date, a real seat limit, a real pricing change) - do NOT invent a constraint
- MICROCOPY: named reason the urgency is genuine (if high), or a comfort line removing procrastination friction (if low/medium)

TECHNICAL REQUIREMENTS:
- Button labels: 3-6 words maximum
- Microcopy: 1-2 sentences, under 15 words each
- No em dashes - hyphens only
- Banned phrases in all three variants and their microcopy: {_BANNED_CTA_LIST}
- Urgency level "{urgency_level}" determines whether time or scarcity language is appropriate - never use it at a higher level than the level specified

{HUMAN_WRITING_RULES}

SELF-CHECK BEFORE OUTPUT:
- Do all 3 variants use genuinely different structural patterns, not just different synonyms for the same construction?
- Does the Variant 3 urgency match the stated urgency level "{urgency_level}" - not stronger, not weaker?
- Is every button label 3-6 words?
- Does every microcopy line address a specific hesitation rather than restating the button label?
- Are there zero em dashes anywhere?

OUTPUT FORMAT:
For each variant: VARIANT NUMBER AND PATTERN NAME, BUTTON LABEL, MICROCOPY LINE.
Then a one-line A/B TEST NOTE for each variant: which situation or traffic source this variant is best suited to test against.

Save to: output/CRO/CTAVariants/
"""


def trust_signals_block(testimonial_name, result_metric, company_size, market=None, **_):
    return f"""You are a conversion copywriter who writes social proof blocks, and who knows that trust signals placed near the CTA are the single highest-leverage location for proof on any landing page.

TASK:
Write a complete trust signals block using the following anchors:

TESTIMONIAL NAME: {testimonial_name}
RESULT METRIC: {result_metric}
COMPANY SIZE: {company_size}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. What is the one sentence from {testimonial_name} that a prospect who has NOT yet converted would find most credible - the statement that sounds like a peer, not a paid endorsement?
2. Does the result metric "{result_metric}" pass the specificity test - would two different readers interpret it exactly the same way? If not, add context until it does.
3. At company size "{company_size}", what is the specific fear or objection a prospect of similar size would have? The trust block should address it.

2025 SOCIAL PROOF CONTEXT:
- 92% of consumers trust peer-created content over branded messages (inBeat Agency, 2025)
- Social proof placed immediately above the CTA removes last-moment hesitation for visitors closest to converting
- Testimonials with a specific named result ("saved 8 hours per week") outperform vague sentiment ("really great product!") on every metric
- Including name, title, company, and company size in a testimonial attribution line increases perceived credibility - anonymized or first-name-only quotes are treated as fabricated by B2B buyers

TRUST SIGNALS BLOCK SECTIONS (write all four, in this order):

ELEMENT 1 - HEADLINE (above the proof block):
- One line that names what the proof proves - not "What Our Customers Say"
- Frame it as the outcome: "How [audience type] at [company_size] companies use this to [result category]"

ELEMENT 2 - FEATURED TESTIMONIAL:
- Name: {testimonial_name}
- Result metric: {result_metric} - worked into the quote naturally, not bolted on after
- Attribution line: full name, title, company, company size - all four fields
- Quote structure: opens with the situation before (1 sentence), names the result (1 sentence), closes with a recommendation or observation (1 sentence)
- Do NOT write a manufactured quote that sounds like marketing copy - write it as a real person would say it in a conversation, contractions and all
- Note: if the result metric requires rounding or approximation, use honest language ("roughly", "about") rather than false precision

ELEMENT 3 - SUPPORTING PROOF ITEMS (choose 2 from the following formats):
- FORMAT A - STAT CALLOUT: "[Number]% of [audience type] at [company_size] organizations report [result] after [timeframe]" - only use a stat you can attribute to a real source (name the source)
- FORMAT B - LOGO BAR: "[INSERT: logos of 4-6 recognizable companies of {company_size} size]" - with a one-line caption naming the company size range and the result category they share
- FORMAT C - REVIEW RATING: "[X.X out of 5 from N reviews on G2/Capterra/Trustpilot]" - use only if a real rating and review count exists; do not fabricate
- FORMAT D - NAMED CASE STUDY TEASER: One sentence naming a {company_size}-size company, what they did, and the outcome - with a link placeholder "[INSERT: case study link]"

ELEMENT 4 - OBJECTION NEUTRALIZER (1-2 sentences, placed below the proof block):
- Name the specific hesitation a {company_size}-size company prospect has at this stage
- Address it directly and concisely - not a marketing claim, an honest answer
- Example: "Already using [competitor]? Most of our customers switched from there - setup takes under an hour."

TECHNICAL REQUIREMENTS:
- No em dashes - hyphens only
- The featured testimonial must include all four attribution fields: name, title, company, company size
- No fabricated stats - flag any stat with [VERIFY: source] if it cannot be confirmed
- Banned phrases: {_BANNED_CTA_LIST}

{HUMAN_WRITING_RULES}

{RESEARCH_RULES}

SELF-CHECK BEFORE OUTPUT:
- Does the featured testimonial include all four attribution fields?
- Does the result metric "{result_metric}" appear inside the quote naturally, not as a bolted-on stat after the attribution?
- Is every supporting proof item using a format that can be verified - no invented ratings or fabricated case study metrics?
- Does the objection neutralizer address the specific hesitation a {company_size}-size buyer would have, not a generic one?
- Are there zero em dashes anywhere in the output?

OUTPUT FORMAT:
Write each element under its label (HEADLINE, FEATURED TESTIMONIAL, SUPPORTING PROOF ITEMS, OBJECTION NEUTRALIZER). Deliver the block exactly as it would appear on the page.

Save to: output/CRO/TrustSignals/
"""


def hero_headline_formula(outcome, audience, timeframe, market=None, **_):
    return f"""You are a headline copywriter who has written hero headlines for landing pages across SaaS, professional services, and e-commerce, and who knows that 90% of landing page visitors read the headline and then decide whether to stay within 3 seconds (SEO Sherpa, 2026).

TASK:
Write 3 distinct hero headline options using the following inputs:

DESIRED OUTCOME: {outcome}
TARGET AUDIENCE: {audience}
TIMEFRAME: {timeframe}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. Is "{outcome}" stated as something {audience} wants to achieve, or as something the product does? Reframe it as the visitor's desired state before writing.
2. Is "{timeframe}" a real, honest timeframe for achieving "{outcome}", or does it need a qualifier ("for most [audience]", "on average") to be accurate?
3. Which of these three concerns does {audience} most distrust in a headline: a claim that sounds too good, a claim that sounds too generic, or a claim that sounds like it requires too much effort? The three headline patterns below are designed to counter each one.

2025 HEADLINE CONTEXT:
- 90% of landing page visitors read the headline - it alone determines whether the page gets a fair read (SEO Sherpa, 2026)
- Headlines framed around the visitor's desired outcome outperform headlines framing the product's features in every major split test category
- Specificity is credibility: "Save 3 hours a week" outperforms "Save time" because vague claims are not believed
- The headline and CTA are the two elements that drive most of the conversion result - they must be read as a pair, not independently

THREE HEADLINE OPTIONS (each uses a structurally different formula - do not reuse the same construction):

OPTION 1 - OUTCOME + TIMEFRAME FORMULA:
Pattern: "[Specific Outcome] in [Specific Timeframe]"
- State the outcome {audience} wants, then the honest timeframe to get there
- Specificity is mandatory: "3 qualified leads" not "more leads", "14 days" not "quickly"
- If {timeframe} needs a qualifier to be honest, include it: "in [timeframe] on average"
- One-line SUPPORTING SUBHEADLINE: names who this is for and the mechanism at a high level

OPTION 2 - AUDIENCE IDENTITY FORMULA:
Pattern: "[Audience Identity or Role]: [Outcome Statement]"
- Opens by naming {audience} so they self-identify immediately
- The outcome statement after the colon is the direct payoff for staying on the page
- Avoids "Are you a [audience]?" - states it as a direct address instead
- One-line SUPPORTING SUBHEADLINE: addresses the single most common objection for {audience} before they raise it

OPTION 3 - CONTRAST FORMULA:
Pattern: "[What they have now] to [What they will have] - without [The common frustration they expect to endure]"
- Names the current state, the desired state, and removes the assumed cost
- "Without the [pain they expected]" is the highest-leverage line - it answers the objection inside the headline
- Example: "From scattered leads to a full pipeline - without cold calling or manual follow-up"
- One-line SUPPORTING SUBHEADLINE: adds the timeframe and one proof anchor (a stat or a named result)

TECHNICAL REQUIREMENTS:
- Each headline: 8-12 words maximum
- Each subheadline: 15-20 words maximum, one sentence
- No em dashes in headlines - hyphens only; em dashes are also banned in subheadlines
- No question marks in any of the three options - declarative statements only
- Banned phrases in headlines and subheadlines: {_BANNED_CTA_LIST}
- Do not use the words "revolutionary", "game-changing", "cutting-edge", or any superlative without a specific proof point attached

{HUMAN_WRITING_RULES}

SELF-CHECK BEFORE OUTPUT:
- Do all 3 options use genuinely different structural formulas, not just different wording of the same pattern?
- Is every headline under 12 words?
- Is the timeframe "{timeframe}" accurate in each headline that uses it - or qualified appropriately if needed?
- Does each subheadline add new information rather than restating the headline?
- Are there zero em dashes anywhere?

OUTPUT FORMAT:
For each of the 3 options: OPTION NUMBER AND FORMULA NAME, HEADLINE (word count shown), SUBHEADLINE, and a one-line A/B TEST NOTE naming which traffic source or page context this headline is best suited for.

Save to: output/CRO/HeroHeadlines/
"""
