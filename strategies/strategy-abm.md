# Account-Based Marketing Strategy

_Last updated: 2026-07-14_

## Goal and Metric

Convert a defined set of named high-value accounts through personalized, account-specific content and coordinated outreach, rather than broad-reach campaigns. Target: 20%+ of named target accounts showing measurable engagement (content opens, meeting acceptance) within 90 days, and a sales cycle at least 20% shorter for ABM-sourced opportunities compared to inbound-sourced opportunities in the same segment.

---

## Core Principles

**1. Real personalization requires four inputs.** Before generating or sending any ABM content, the account's name, a specific business context (a recent funding round, a leadership change, a public initiative), the named contact's role and seniority, and the specific value proposition relevant to that account's situation must all be known. Content missing any of these four reads as templated personalization, which is worse than no personalization: it signals the sender did not actually research the account.

**2. Tier the account list and match effort to tier.** Not every named account deserves 1:1 hand-built content. Split accounts into three tiers: 1:1 (a handful of the highest-value named accounts, fully custom content per account), 1:Few (a small cluster of similar accounts, semi-custom content per cluster), and 1:Many (a broader named-account segment, templated content with light personalization tokens). Applying 1:1 effort across a 200-account list is not ABM, it is unsustainable; applying 1:Many templating to a top-10 strategic account under-invests in the highest-value opportunity.

**3. Sales and marketing alignment is a precondition, not a nice-to-have.** ABM fails when marketing generates account-specific content that sales never uses, or when sales requests personalization marketing cannot support at scale. Before launching, agree on the account list jointly, agree on who owns outreach timing, and agree on what "engaged" means for each account so both teams work from the same signal.

**4. Multi-threading beats single-contact outreach.** A deal that depends on one champion inside the account is fragile if that person leaves or loses influence. ABM content should be built to reach multiple roles inside the same account (economic buyer, technical evaluator, end user) with role-appropriate framing of the same underlying value proposition, not identical content sent to every contact.

**5. Measure account engagement, not just contact engagement.** A single contact opening every email looks like strong engagement but may represent one person's interest, not organizational buy-in. Track engagement across the full buying committee within an account (how many distinct contacts engaged, from how many departments) as the leading indicator of real account-level traction.

---

## Strategy Architecture

**Step 1: Build and tier the target account list jointly with sales.** Use firmographic fit (industry, company size, tech stack) combined with intent signals (recent funding, hiring surges in a relevant department, public statements about a relevant initiative) to build the list, then tier per Principle 2.

**Step 2: Research each account before generating content.** For 1:1 and 1:Few tiers, research the specific business context and named contacts before writing anything. For 1:Many, define the shared context that applies across the segment (a common trigger event type, a common role).

**Step 3: Build content per the tier using `ABM_Content_Prompt.txt`'s three formats.** 1:1 Enterprise content references the account by name and its specific context. 1:Few content references the shared cluster trait. 1:Many content uses personalization tokens (company name, industry) inserted into a structured template.

**Step 4: Coordinate multi-channel, multi-contact delivery.** Sequence outreach across email, LinkedIn, and sales-direct touches to reach multiple roles inside the account within the same engagement window, rather than a single channel to a single contact.

**Step 5: Track account-level engagement and hand off to sales at the defined threshold.** Agree in advance what engagement level (e.g. 2+ distinct contacts engaging within 30 days) triggers a sales-led follow-up, so marketing and sales do not compete for the same account moment with conflicting messages.

---

## Cadence

- Target account list review: quarterly, refreshed with new intent signals
- 1:1 account research and content: built per active opportunity, not on a fixed schedule
- 1:Few and 1:Many content: refreshed monthly or per campaign
- Sales-marketing alignment sync: bi-weekly during active ABM campaigns
- Account engagement reporting: weekly during active campaigns

---

## Failure Modes

1. **Fake personalization.** Swapping only the company name into an otherwise generic template is detectable to the recipient and damages credibility more than generic outreach would have.
2. **1:1 effort applied at 1:Many scale.** This burns out the team producing the content and cannot sustain a large account list.
3. **Marketing and sales working from different account lists or different definitions of "engaged."** This produces duplicate, conflicting, or contradictory outreach to the same account.
4. **Single-contact dependency.** A deal that collapses when one champion leaves the account was never a multi-threaded ABM motion, regardless of how personalized the content was.
5. **Measuring campaign volume instead of account-level engagement depth.** A high send volume with low distinct-contact engagement inside target accounts is not a working ABM program.

---

## Recommended Tools

- **6sense or Demandbase:** account-level intent data and firmographic fit scoring to build and prioritize the target account list.
- **LinkedIn Sales Navigator:** identify and research named contacts across roles within a target account.
- **Clay or Apollo:** enrich account and contact data to support the four personalization inputs required per Principle 1.
- **Salesforce or HubSpot (account-based views):** track engagement at the account level, not just the contact level, across marketing and sales touches.
