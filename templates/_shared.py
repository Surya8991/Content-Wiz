HUMAN_WRITING_RULES = """
HUMAN WRITING & GRAMMAR RULES (Non-negotiable - apply to every word):
- Write exactly as a senior human professional would - not a content bot
- Zero tolerance for: comma splices, subject-verb disagreement, dangling modifiers, run-on sentences, or tense shifts
- Use active voice in at least 85% of sentences
- Vary sentence length intentionally: mix short punchy sentences (6-10 words) with medium ones (15-20 words). Never three long sentences in a row
- Each paragraph: 2-4 sentences maximum. No walls of text
- Transitions must feel organic - not "Furthermore", "Moreover", "In addition", "It is worth noting"
- NEVER use these AI-signature phrases (2025 refresh - checked against current LLM output patterns):
  Classic tells: "In today's fast-paced world", "In conclusion", "It's important to note", "It's worth noting", "It goes without saying", "Needless to say", "At the end of the day", "Dive into", "Delve into", "Leverage", "Utilize", "Unlock the potential", "Game-changer", "Holistic approach", "Robust", "Paradigm shift", "Synergy", "Move the needle", "Take it to the next level", "Cutting-edge", "Transformative", "Groundbreaking", "Revolutionize", "Empower", "Seamlessly", "Streamline"
  Current-era LLM tells (Claude/GPT/Gemini 2024-2025 patterns): "Elevate", "Elevated", "Harness", "Navigate the", "The landscape of", "A tapestry of", "Pivotal", "Crucial", "Underscores", "Underscoring", "Meticulous", "Meticulously", "Rapidly evolving", "Ever-evolving", "Ever-changing", "Stands out", "Ensure that", "Not only... but also", "Whether you're a... or a...", "This isn't just... it's...", "It's more than just", "Testament to", "A journey", "Journey towards", "Embark on", "Embark upon", "In the realm of", "The world of", "At its core", "In essence", "Ultimately", "That being said", "With that said", "Bustling", "Vibrant", "Thriving", "Nestled", "Boasts", "Boasting", "A treasure trove", "Look no further", "Say goodbye to", "Say hello to", "Unleash", "Unleashing", "Foster", "Fostering", "Curate", "Curated", "Bespoke", "Cornerstone", "Beacon", "Testament", "Ecosystem" (when used as filler), "Best practices" (when unsupported), "Actionable insights", "Data-driven decisions" (when unsupported)
- Replace ALL em dashes with regular hyphens (-)
- Use contractions naturally where they fit (it's, you're, don't, we've)
- Write from direct experience - not "studies show" without naming the study
- If writing in first-person "I" voice, the output must be disclosed as a real configured persona's byline or attributed directly to the brand (e.g. "Posted on behalf of [Brand]") - never an undisclosed anonymous "I" voice with no attribution
""".strip()

RANKABILITY_RULES = """
SEO & RANKABILITY RULES:
- Match search intent precisely: if the topic implies a how-to, write a how-to. If it implies a comparison, structure accordingly
- Place the primary keyword naturally in: title/heading, first 100 words, at least one subheading, and the conclusion
- Use semantic/LSI keywords throughout - synonyms and related terms that a human expert would naturally use
- Answer the question a reader types into Google before they scroll - put the core answer early
- Use subheadings as mini-questions or benefit statements (not vague labels like "Introduction")
- Include one stat or data point per major section - cite the source inline (e.g. "according to Gallup's 2024 workplace report")
- Internal link opportunity: note where a related resource could be linked
- Aim for a Flesch Reading Ease score of 60+ - write at a grade 8-10 reading level
- Meta-description ready: the opening paragraph should double as a standalone 155-character summary
""".strip()

RESEARCH_RULES = """
RESEARCH & AUTHORITY RULES:
- Every major claim needs a real source: name the organization, report title, and year (e.g. "LinkedIn's 2024 Workplace Learning Report found that...")
- Prioritize sources by tier, then by regional fit for the target audience:
  Tier 1 (peer-reviewed journals) > Tier 2 (industry reports) > Tier 3 (reputable news)
  Tier 2 examples by region - use the source list appropriate to the audience:
    - US / global default: McKinsey, Deloitte, Gallup, SHRM, LinkedIn, Pew, Bureau of Labor Statistics
    - UK / EU: Eurostat, INSEE (France), Destatis (Germany), CIPD (UK HR), Statista Europe, EU-OSHA, EIB
    - APAC: NSO country stats agencies, ADB, MOM (Singapore), NASSCOM (India), Nikkei/Nikkei Asia research
    - LATAM: CEPAL, INEGI (Mexico), IBGE (Brazil), Statista LATAM
  Tier 3 examples by region: HBR/Forbes/WSJ (US), FT/Economist/Reuters (UK/global), Nikkei (Japan), Handelsblatt (Germany), Les Echos (France), Folha/Estadao (Brazil), Economic Times (India)
  Rule: if the audience is regional or non-US, lead with regional sources rather than US-only ones; US-only sources on a European or APAC piece read as sloppy localization
- Include at least 2-3 real statistics with proper attribution per 500 words
- Reference real companies, real case studies, or real named experts where relevant
- If quoting a stat you are not 100% certain of, flag it with a note to verify before publishing
- Add a "Sources" or "Further Reading" note at the end listing key references used
- Third-party research disclaimer: when characterizing a named third party's research, report, or data (e.g. OWASP, Verizon, Gallup, Gartner, HBR), describe only what that source actually found, in neutral reporting language ("Gallup's 2024 report found..." not "Gallup agrees with us that..."). Never imply the third party endorses, partners with, sponsors, or recommends the brand or its product. If a specific report/edition/year cannot be confirmed, soften to a qualitative statement rather than naming a source you cannot pin down
- Source-diversity: within a content cluster (multiple posts published close together on related topics), never anchor more than one post in that cluster on the exact same single source as its sole statistical evidence; name a specific report/article and year every time, never a vague reference with no title or year
- DataBank-only sourcing: any first-party or proprietary-sounding statistic (e.g. internal program data, "our customers saw X%") must trace to a real row in data/HARO_DataBank.csv, not be generated from general knowledge. External academic/industry stats (Gartner, Verizon DBIR, Gallup, etc.) are exempt and follow the sourcing rules above instead
- Publish gate: any stat-bearing post, or any post written in first-person/confessional voice, requires a human reviewer's sign-off (name + date, tracked on the content calendar) before it can move to "Published" - flag this requirement rather than treating the draft as publish-ready on its own
""".strip()

# Canonical list of banned CTA/promotional phrases. Any template with a
# call-to-action should ban these explicitly rather than re-deriving its own
# list, so a phrase banned in one template (e.g. blog_writing's "click here"
# ban) doesn't silently miss a sibling template (e.g. gmb()). lint_content.py
# also scans template source against this same list to catch a banned phrase
# regressing into a template's own example/scaffold text.
BANNED_CTA_PHRASES = [
    "Don't miss out",
    "Take advantage of",
    "Click here",
    "Click on learn more",
    "Learn more",
    "Discover",
]


# Per-market voice registers. A brand's `market` field in config.json selects
# one of these ("b2b" is the default and matches this repo's original voice).
# Templates receive `market` as a kwarg from generate.build_prompt and can
# interpolate `market_voice(market)`; templates that ignore it stay B2B-toned.
MARKET_VOICE_RULES = {
    "b2b": """
MARKET REGISTER - B2B:
- Write for a professional evaluating a business decision, not a casual browser
- Frame outcomes in business terms: productivity, retention, risk, cost, revenue
- Credible-expert tone: confident, specific, zero hype
- Role-aware: a CFO, a CTO, and an HR lead care about different proof - match the stated audience's actual concerns
- No consumer-style urgency or emotional selling
""".strip(),
    "b2c": """
MARKET REGISTER - B2C / CONSUMER:
- Write for an individual spending their own money and time - lead with what changes in THEIR life, not organizational outcomes
- Everyday language over industry vocabulary: say "get better at" not "upskill", "figure out" not "assess"
- Emotional resonance is legitimate here: relief, confidence, pride, curiosity - but earned through specifics, never manufactured urgency
- Short sentences, direct address ("you"), concrete before abstract
- Price/effort transparency builds trust: acknowledge what it costs (time or money) instead of hiding it
""".strip(),
    "creator": """
MARKET REGISTER - CREATOR / PERSONAL BRAND:
- Write as one identifiable human with a point of view, not an organization - first person, personality-forward, opinions allowed and expected
- Platform-native informality: contractions, fragments, asides - the register of someone talking, not publishing
- The reader follows a PERSON: consistency of voice across posts matters more than polish within any single post
- Share process and specifics from lived experience ("here's what I actually did") over general advice ("here's what one should do")
- Never voice-of-god corporate neutrality: hedged, committee-approved language reads as fake on a personal account
""".strip(),
}


def market_voice(market=None):
    """Return the voice-register block for `market`, defaulting to b2b."""
    return MARKET_VOICE_RULES.get((market or "b2b").lower(), MARKET_VOICE_RULES["b2b"])


# Common labels for interpolating `market` into an opening persona line so a
# template's role-play doesn't contradict the `market_voice()` rules appended
# below it. Pattern: f"You are a {market_persona_label(market)} writer …".
_MARKET_LABELS = {
    "b2b":     {"label": "B2B",     "brand_kind": "B2B brands",         "buyer": "professional buyers"},
    "b2c":     {"label": "consumer", "brand_kind": "consumer brands",   "buyer": "everyday shoppers"},
    "creator": {"label": "creator-economy", "brand_kind": "solo creators", "buyer": "creator-audience readers"},
}


def market_persona_label(market=None, key="label"):
    """Return a short adjective/noun describing the persona to interpolate into
    a template's opening role-play. `key` selects a facet:
    - "label"      -> "B2B" / "consumer" / "creator-economy"      (adjective)
    - "brand_kind" -> "B2B brands" / "consumer brands" / "solo creators"
    - "buyer"      -> "professional buyers" / "everyday shoppers" / "creator-audience readers"
    Default falls back to the b2b variant so callers that omit `market` behave
    exactly as before.
    """
    entry = _MARKET_LABELS.get((market or "b2b").lower(), _MARKET_LABELS["b2b"])
    return entry.get(key, entry["label"])


# Region-aware disclosure-regime language for prompts that discuss sponsored/UGC
# labels, cookie/consent, telemarketing consent, and equal-opportunity notices.
# Templates should prefer this over hardcoding a single jurisdiction's regime.
DISCLOSURE_REGIME_NOTE = """
DISCLOSURE / CONSENT REGIME - apply the framework of the recipient audience's
jurisdiction, not the US default:
- Sponsored / UGC labels: FTC (US), ASA/CAP (UK), Competition Bureau (Canada),
  ACCC (Australia), each EU member state's advertising regulator under the
  UCPD + DSA (EU/EEA), CONAR (Brazil), ASCI (India). Use the label form the
  recipient regulator requires (#ad/#sponsored/Werbung/publicidade/etc.).
- SMS/telemarketing consent: TCPA + state law (US), PECR (UK), CASL (Canada),
  GDPR + ePrivacy (EU/EEA), Spam Act (Australia), LGPD (Brazil).
- Data/privacy: CCPA/CPRA + state law (US), UK GDPR, EU GDPR, LGPD (Brazil),
  PIPEDA (Canada), APPI (Japan), DPDP Act (India).
- Employment / equal opportunity: EEO Act + state law (US), Equality Act (UK),
  EU Pay Transparency Directive + national equality laws (EU), Fair Work Act
  (Australia).
When the target audience or `market` is unclear, name the regime that applies
and add a "confirm the local equivalent" reviewer note - do not silently assume
the US framework governs.
""".strip()


TONE_RULES = {
    "formal": (
        "TONE OVERRIDE - FORMAL: Use precise vocabulary, complete sentences, and a "
        "professional register throughout. Avoid contractions, colloquialisms, and casual phrasing. "
        "Authoritative but not cold."
    ),
    "conversational": (
        "TONE OVERRIDE - CONVERSATIONAL: Write as if speaking directly to one person. "
        "Use contractions, short sentences, and plain everyday language. Avoid jargon. "
        "Approachable but still credible."
    ),
    "urgent": (
        "TONE OVERRIDE - URGENT: Every sentence drives momentum toward the action. "
        "Short punchy sentences. Active verbs. Loss-frame hooks. No filler language. "
        "The reader should feel that delay has a cost."
    ),
    "educational": (
        "TONE OVERRIDE - EDUCATIONAL: Prioritize clarity over cleverness. Define terms "
        "on first use. Use analogies to explain complex ideas. Structure content to build "
        "understanding step by step. Patient and thorough."
    ),
    "playful": (
        "TONE OVERRIDE - PLAYFUL: Use wordplay and light humor where appropriate. "
        "Enthusiasm shows in word choice and sentence rhythm. Keep it professional "
        "enough for the brand's context but let personality come through."
    ),
}


def tone_modifier(tone=None):
    """Return the tone-override block for `tone`, or empty string if unset."""
    if not tone:
        return ""
    return TONE_RULES.get(tone.lower().strip(), "")


# ─────────────────────────────────────────────
# EXISTING TEMPLATES
# ─────────────────────────────────────────────
