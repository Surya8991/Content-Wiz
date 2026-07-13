HUMAN_WRITING_RULES = """
HUMAN WRITING & GRAMMAR RULES (Non-negotiable - apply to every word):
- Write exactly as a senior human professional would - not a content bot
- Zero tolerance for: comma splices, subject-verb disagreement, dangling modifiers, run-on sentences, or tense shifts
- Use active voice in at least 85% of sentences
- Vary sentence length intentionally: mix short punchy sentences (6-10 words) with medium ones (15-20 words). Never three long sentences in a row
- Each paragraph: 2-4 sentences maximum. No walls of text
- Transitions must feel organic - not "Furthermore", "Moreover", "In addition", "It is worth noting"
- NEVER use these AI-signature phrases: "In today's fast-paced world", "In conclusion", "It's important to note", "Dive into", "Delve into", "Leverage", "Utilize", "Unlock the potential", "Game-changer", "Holistic approach", "Robust", "Paradigm shift", "Synergy", "It goes without saying", "Needless to say", "At the end of the day", "Move the needle", "Take it to the next level", "Cutting-edge", "Transformative", "Groundbreaking", "Revolutionize", "Empower", "Seamlessly", "Streamline"
- Replace ALL em dashes (-) with regular hyphens (-)
- Use contractions naturally where they fit (it's, you're, don't, we've)
- Write from direct experience - not "studies show" without naming the study
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
- Prioritize sources: peer-reviewed journals > industry reports (McKinsey, Deloitte, Gallup, SHRM, LinkedIn) > reputable news (HBR, Forbes, WSJ)
- Include at least 2-3 real statistics with proper attribution per 500 words
- Reference real companies, real case studies, or real named experts where relevant
- If quoting a stat you are not 100% certain of, flag it with a note to verify before publishing
- Add a "Sources" or "Further Reading" note at the end listing key references used
- Third-party research disclaimer: when characterizing a named third party's research, report, or data (e.g. OWASP, Verizon, Gallup, Gartner, HBR), describe only what that source actually found, in neutral reporting language ("Gallup's 2024 report found..." not "Gallup agrees with us that..."). Never imply the third party endorses, partners with, sponsors, or recommends the brand or its product. If a specific report/edition/year cannot be confirmed, soften to a qualitative statement rather than naming a source you cannot pin down
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


# ─────────────────────────────────────────────
# EXISTING TEMPLATES
# ─────────────────────────────────────────────
