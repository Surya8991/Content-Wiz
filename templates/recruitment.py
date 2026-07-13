from ._shared import BANNED_CTA_PHRASES, HUMAN_WRITING_RULES, market_voice

_BANNED_CTA_LIST = ", ".join(f'"{p}"' for p in BANNED_CTA_PHRASES)


def job_posting(topic, audience, wordcount=None, market=None, **_):
    # Section budgets scale proportionally with the caller's wordcount override
    # instead of fixed absolute floors (the bug class this repo's audit already
    # fixed in blog_writing - a fixed max() floor ignores a short override and
    # produces section minimums that sum past the caller's target).
    wc = wordcount or 500
    hook_lo, hook_hi = round(wc * 0.05 * 0.85), round(wc * 0.05 * 1.15)
    summ_lo, summ_hi = round(wc * 0.18 * 0.85), round(wc * 0.18 * 1.15)
    resp_lo, resp_hi = round(wc * 0.18 * 0.85), round(wc * 0.18 * 1.15)
    must_lo, must_hi = round(wc * 0.12 * 0.85), round(wc * 0.12 * 1.15)
    nice_lo, nice_hi = round(wc * 0.08 * 0.85), round(wc * 0.08 * 1.15)
    comp_lo, comp_hi = round(wc * 0.10 * 0.85), round(wc * 0.10 * 1.15)
    cult_lo, cult_hi = round(wc * 0.14 * 0.85), round(wc * 0.14 * 1.15)
    eeo_lo, eeo_hi = round(wc * 0.06 * 0.85), round(wc * 0.06 * 1.15)
    cta_lo, cta_hi = round(wc * 0.06 * 0.85), round(wc * 0.06 * 1.15)
    return f"""You are a talent acquisition lead and employer-branding writer who has written job postings that measurably improved qualified-applicant volume, not just posting volume. You know a job posting is a recruitment marketing asset aimed at a candidate deciding whether to spend 20 minutes of their evening on an application, not an internal duty list copy-pasted into a public page.

TASK:
Write a complete job posting for the role: "{topic}"

TARGET AUDIENCE (who reads and applies): {audience}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. What is the ONE thing about this specific role or team that a strong candidate cannot get from a competing posting for a similar title elsewhere? (This is the hook. If the answer is "nothing," the summary needs work before the requirements do.)
2. Of everything this role touches, which qualifications are genuinely required to do the job on day one, versus which are things a capable hire could learn in the first 90 days? Confusing the two is the single most common reason strong candidates self-select out.
3. Who has historically been discouraged from applying to roles like this because of tone or an inflated requirements list, and what in this draft specifically avoids repeating that pattern?
4. Is a real, current salary range available for this role, or does this draft need the placeholder?

WHY THIS MATTERS (encode this reasoning into the draft, do not just state it as a disclaimer):
- Postings that read as a pure requirements/duties list consistently underperform postings that open by selling the actual opportunity: what the person will build, own, or grow into. Lead with that, not with a list.
- Long, undifferentiated requirements lists suppress qualified applicants. Candidates - and research on this pattern shows the effect lands disproportionately on women and other candidates who read "required" as a hard gate - routinely skip applying when they do not check every box, even when they are genuinely qualified. The fix is structural: keep the must-have list genuinely short and reserve everything else for a clearly separate nice-to-have list.
- Culture-fit language built on superlatives ("rockstar," "ninja," "hacker," "guru") and gender-coded personality words ("aggressive," "assertive" read as male-coded; "nurturing," "collaborative" read as female-coded when used as a personality gate) narrows who applies without improving who is qualified. Neutral, skills-based language does not have this effect.
- Pay-range disclosure in job postings is now a legal requirement, not a courtesy, in a large and growing number of U.S. jurisdictions (among them California, Colorado, Connecticut, Hawaii, Illinois, Maryland, Massachusetts, Minnesota, Nevada, New Jersey, New York, Rhode Island, Vermont, and Washington, plus Washington D.C., as of 2026) - and remote postings are frequently held to the strictest law among any state where the role could be performed. Requirements vary by jurisdiction (some require the range in every posting, some only later in the process), so never assume this posting is exempt.

JOB POSTING STRUCTURE (target {wc} words total):

═══════════════════════════════════════════
SECTION 1 - ROLE TITLE & ONE-LINE HOOK ({hook_lo} to {hook_hi} words)
═══════════════════════════════════════════
- The exact role title as it should appear in applicant tracking systems and search
- One sentence that names what makes THIS opening for {topic} distinctive - a specific problem the hire will own, a team inflection point, or a growth path - never a generic "join our team" line

═══════════════════════════════════════════
SECTION 2 - ROLE SUMMARY - SELL THE OPPORTUNITY ({summ_lo} to {summ_hi} words)
═══════════════════════════════════════════
This is the section that gets read before anyone reads the requirements. It must sell the role, not just describe it:
- What the person will actually own or build in the first 6 to 12 months
- Who they will work with and what impact their work has on the team or the business
- What growth or scope-expansion looks like from this seat over time
- Written in direct second person ("you'll own," "you'll work with"), not third-person job-ad-ese ("the successful candidate will")
- No duty-list bullet points here - this section is prose, and it is the section a candidate reads to decide whether to keep reading

═══════════════════════════════════════════
SECTION 3 - WHAT YOU'LL DO ({resp_lo} to {resp_hi} words)
═══════════════════════════════════════════
- 5 to 8 bullet points, each starting with an active verb
- Specific enough that a candidate can picture a real Tuesday in the role - not vague abstractions like "drive strategic initiatives"
- Ordered roughly by how the person will actually spend their time, most common first

═══════════════════════════════════════════
SECTION 4 - MUST-HAVE QUALIFICATIONS ({must_lo} to {must_hi} words)
═══════════════════════════════════════════
KEEP THIS LIST GENUINELY MINIMAL - this is a hard rule, not a suggestion:
- Include ONLY what a person truly cannot do the job without on day one (a specific certification legally required to practice, a specific tool the team has no time to teach, a minimum years-of-experience floor only if it is truly load-bearing)
- Target 3 to 5 bullet points maximum. If the draft input implies more than 5 genuine must-haves, move the excess to the nice-to-have list in Section 5 rather than inflating this one
- Replace vague credential gates with skills language where possible ("demonstrated experience shipping production code in [language/framework]" rather than "Bachelor's degree in Computer Science required") unless the role has a genuine, legally-grounded degree or license requirement
- No gender-coded personality descriptors and no culture-fit superlatives anywhere in this list ("rockstar," "ninja," "hacker," "guru," "wizard," "aggressive," "assertive" as a personality gate) - describe the skill or trait in neutral, observable terms instead

═══════════════════════════════════════════
SECTION 5 - NICE-TO-HAVE QUALIFICATIONS ({nice_lo} to {nice_hi} words)
═══════════════════════════════════════════
- Clearly labeled as NOT required to apply - state this explicitly: "You don't need all of these. If the role summary above sounds like you, apply."
- 3 to 6 bullet points of qualifications that strengthen a candidate's fit but are learnable on the job
- This is the list that should absorb anything a hiring manager wants to ask for but that isn't truly load-bearing on day one

═══════════════════════════════════════════
SECTION 6 - COMPENSATION & BENEFITS ({comp_lo} to {comp_hi} words)
═══════════════════════════════════════════
- Salary range: [INSERT: salary range for this role] - use this placeholder, never a fabricated or estimated number
- Add this compliance note directly beneath the placeholder: "A growing number of U.S. states and cities (including California, Colorado, New York, Washington, and others) legally require a good-faith salary range in job postings, and remote postings are often held to the strictest applicable law across every state where the role could be performed. Confirm the applicable requirement for this posting's location(s) before publishing, and never publish this posting with the placeholder still in place."
- Benefits: list only what the brand has actually configured/confirmed (health coverage, PTO policy, retirement match, remote/hybrid policy, professional development budget, etc.) - use "[INSERT: benefit]" placeholders for anything not confirmed rather than inventing standard-sounding perks

═══════════════════════════════════════════
SECTION 7 - ABOUT THE COMPANY & TEAM ({cult_lo} to {cult_hi} words)
═══════════════════════════════════════════
- Use the brand's actual configured company description as the foundation for this section - do not invent perks, awards, culture claims, or "why we're different" statements the brand hasn't confirmed
- One or two sentences on the specific team this role sits within, if known; otherwise keep this section grounded in the confirmed company description alone
- If a culture claim cannot be traced to the brand's own configured description, mark it "[INSERT: confirm culture detail]" rather than inventing something that sounds plausible

═══════════════════════════════════════════
SECTION 8 - EQUAL OPPORTUNITY STATEMENT (MANDATORY) ({eeo_lo} to {eeo_hi} words)
═══════════════════════════════════════════
Include a standard EEO statement covering protected classes, adapted for the brand:
"[Brand] is an equal opportunity employer and does not discriminate on the basis of race, color, religion, sex (including pregnancy, sexual orientation, and gender identity), national origin, age, disability, or genetic information. [INSERT: add any jurisdiction-specific protected classes or federal-contractor OFCCP language that applies to this posting's location.]"
- Note beneath it: "Confirm this statement against current legal requirements for every jurisdiction this posting runs in before publishing - requirements vary by state and by federal-contractor status."

═══════════════════════════════════════════
SECTION 9 - HOW TO APPLY ({cta_lo} to {cta_hi} words)
═══════════════════════════════════════════
- A clear, low-friction next step: what to submit, where, and what happens next in the process (expected timeline if known, or "[INSERT: expected response timeline]")
- One sentence inviting candidates who are close-but-not-exact fits to apply anyway, reinforcing Section 5's framing
- Do not use any of the following canonical banned CTA/promotional phrases this project bans everywhere: {_BANNED_CTA_LIST}

JOB POSTING WRITING RULES:
- No em dashes anywhere - use hyphens, commas, or restructure
- No gendered-coded personality language and no culture-fit superlatives anywhere in the posting, not only in the qualifications sections
- No fabricated salary figures - the placeholder stands until a human fills it in
- No invented perks, awards, or culture claims not present in the brand's configured description
- Must-have list stays genuinely minimal - if in doubt, a qualification belongs in nice-to-have, not must-have

SELF-CHECK BEFORE OUTPUT:
- Does Section 2 sell the opportunity in prose before any list appears, with zero duty-list bullets in that section?
- Is the must-have list at or under 5 genuine day-one requirements, with everything else moved to nice-to-have?
- Is there zero gendered-coded or superlative culture-fit language anywhere in the draft?
- Is the salary range a marked [INSERT: ...] placeholder with the jurisdiction compliance note attached, never a fabricated number?
- Does the company/culture section trace only to the brand's actual configured description, with unconfirmed claims marked [INSERT: ...]?
- Is the EEO statement present with its own jurisdiction-verification note?
- Are there any em dashes or banned CTA phrases?

OUTPUT FORMAT:
Return the complete job posting with all nine numbered sections in order, section dividers, and bullet formatting where specified. Paste-ready for an applicant tracking system or careers page. No preamble, no meta-commentary.
"""


def employee_spotlight(topic, audience, wordcount=None, market=None, **_):
    # Section budgets scale proportionally with the caller's wordcount override,
    # same proportional-fraction approach as job_posting above - no fixed floors.
    wc = wordcount or 450
    hook_lo, hook_hi = round(wc * 0.12 * 0.85), round(wc * 0.12 * 1.15)
    intro_lo, intro_hi = round(wc * 0.12 * 0.85), round(wc * 0.12 * 1.15)
    day_lo, day_hi = round(wc * 0.22 * 0.85), round(wc * 0.22 * 1.15)
    growth_lo, growth_hi = round(wc * 0.20 * 0.85), round(wc * 0.20 * 1.15)
    advice_lo, advice_hi = round(wc * 0.18 * 0.85), round(wc * 0.18 * 1.15)
    cta_lo, cta_hi = round(wc * 0.10 * 0.85), round(wc * 0.10 * 1.15)
    return f"""You are an employer-branding writer who has produced employee spotlight content that measurably improves qualified-applicant interest, not just internal engagement. You know a spotlight only works when it reads as one real person's specific experience, never as a corporate culture claim wearing a human mask.

TASK:
Write an employee spotlight / testimonial-style post for employer-branding content about: "{topic}"

TARGET AUDIENCE (who this needs to convince): {audience}

{market_voice(market)}

PRE-WRITE DIAGNOSTIC:
1. What is the ONE thing about this role, team, or theme that a prospective candidate cannot learn from the job posting alone - the thing only a person who actually works there could tell them?
2. What specific day-to-day texture (a project, a recurring moment, a decision this person gets to make) makes this reads as one real person, not a generic "great culture" statement?
3. Is a real employee's actual quote available for this spotlight, or does this draft need placeholder quotes? (Default assumption: placeholders, since this tool cannot know a real person's real words.)
4. What single next step should a reader take after finishing this piece?

NO FABRICATED EMPLOYEE QUOTES - NON-NEGOTIABLE (the same guardrail this project applies to fabricated competitor facts and fabricated statistics elsewhere):
This tool cannot know what a real employee actually said. Inventing a quote and attaching it to a named, seemingly real person is a fabrication risk, not a style shortcut - a fake testimonial attributed to a fake-but-real-sounding employee is the kind of thing that damages trust if it's ever noticed by a real employee or a candidate who asks about "Sarah from the platform team."
- Never invent a named person, a title, a tenure, or a direct quote and present it as real
- Use "[INSERT: real employee name and title]" for the spotlighted person's identity
- Use "[INSERT: real employee quote about ...]" placeholders for every direct quote, with enough of a prompt inside the brackets that whoever fills it in knows exactly what ground that quote needs to cover (e.g. "[INSERT: real employee quote about what a typical week looks like on this team]")
- The narrative framing AROUND the quotes (the hook, the scene-setting, the transitions) can and should be fully written - only the person's identity and their actual words are placeholder-driven

EMPLOYEE SPOTLIGHT STRUCTURE (target {wc} words total):

═══════════════════════════════════════════
SECTION 1 - HOOK: WHAT MAKES THIS DISTINCTIVE ({hook_lo} to {hook_hi} words)
═══════════════════════════════════════════
- Open with the specific thing about this role, team, or theme that a generic "we have great culture" post could never say - a real project, a real growth arc, a real way this team works differently
- Frame it as a question a candidate is actually asking themselves ("what's it really like to work on...") and promise this piece answers it through one person's actual experience
- No generic culture buzzwords here - specificity is the entire point of a spotlight

═══════════════════════════════════════════
SECTION 2 - MEET [INSERT: real employee name and title] ({intro_lo} to {intro_hi} words)
═══════════════════════════════════════════
- [INSERT: real employee name], [INSERT: real employee title], [INSERT: real employee tenure at the company]
- One or two sentences of scene-setting context: what team they're on, what they work on, framed in your own narrative voice (not a quote)
- "[INSERT: real employee quote about why they joined or what first drew them to this role]"

═══════════════════════════════════════════
SECTION 3 - THE DAY-TO-DAY PERSPECTIVE ({day_lo} to {day_hi} words)
═══════════════════════════════════════════
- Narrative framing of what a typical week or project cycle looks like in this role (written by you, grounded in whatever real detail the inputs provide)
- "[INSERT: real employee quote about a specific project, problem, or moment that captures what the work is actually like]"
- "[INSERT: real employee quote about what they didn't expect when they started, or what surprised them]"
- Keep this concrete: a candidate reading this should be able to picture an actual Tuesday, not a mission-statement version of the job

═══════════════════════════════════════════
SECTION 4 - GROWTH & DEVELOPMENT PERSPECTIVE ({growth_lo} to {growth_hi} words)
═══════════════════════════════════════════
- Narrative framing of how this person's role, scope, or skills have changed since joining
- "[INSERT: real employee quote about how they've grown, been supported, or changed roles/scope since joining]"
- "[INSERT: real employee quote about a specific person, mentor, or moment that mattered to their growth]"
- If the brand has a confirmed, real program (mentorship, internal mobility, learning stipend) that supports this, reference it by name; otherwise use "[INSERT: confirm program name]" rather than inventing one

═══════════════════════════════════════════
SECTION 5 - ADVICE FOR SOMEONE CONSIDERING THIS ROLE ({advice_lo} to {advice_hi} words)
═══════════════════════════════════════════
- "[INSERT: real employee quote with honest advice for someone thinking about applying - what kind of person thrives here, and any honest caveat about what the role demands]"
- Include the caveat framing explicitly: a spotlight that only says positive things reads as marketing, not as a real person - honest texture (the role is fast-paced, the team is still small, there's real ambiguity some weeks) builds more trust than unqualified praise
- One sentence in your own narrative voice tying this back to what kind of candidate would genuinely thrive here

═══════════════════════════════════════════
SECTION 6 - EXPLORE OPEN ROLES (SOFT CLOSE) ({cta_lo} to {cta_hi} words)
═══════════════════════════════════════════
- A low-pressure invitation to look at open roles on the team or elsewhere in the company - this is a soft close, not a hard sell
- [INSERT CTA LINK: careers page or open roles for this team] - never fabricate a URL
- Do not use any of the following canonical banned CTA/promotional phrases this project bans everywhere: {_BANNED_CTA_LIST}

{HUMAN_WRITING_RULES}

EMPLOYEE SPOTLIGHT WRITING RULES:
- No em dashes anywhere - use hyphens, commas, or restructure
- Every direct quote is an [INSERT: real employee quote about ...] placeholder - zero invented quotes attributed as real
- The spotlighted person's name, title, and tenure are placeholders, never an invented name presented as a real employee
- Narrative framing around the quotes is fully written and specific - only the person's identity and their literal words are left as placeholders
- Include at least one honest, non-glowing note (Section 5's caveat) so the piece doesn't read as one-sided marketing

SELF-CHECK BEFORE OUTPUT:
- Is every direct quote formatted as an [INSERT: real employee quote about ...] placeholder, with zero quotes invented and attributed as real?
- Is the spotlighted person's identity a placeholder, never a named, seemingly real employee this tool made up?
- Does Section 5 include at least one honest caveat rather than only unqualified praise?
- Does the hook in Section 1 name something specific to this role/team/theme rather than a generic culture claim?
- Is the closing a soft, low-pressure invitation rather than a hard-sell CTA, and are there any banned CTA phrases or em dashes?

OUTPUT FORMAT:
Return the complete spotlight post with all six numbered sections in order, section dividers, and quote formatting as shown. Paste-ready for a careers blog, LinkedIn employer-branding post, or careers page feature. No preamble, no meta-commentary.
"""
