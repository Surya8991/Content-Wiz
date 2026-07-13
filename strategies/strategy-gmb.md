# Google Business Profile (GMB) Post Strategy

_Last updated: 2026-07-13_


## Goal and Metric

Keep a local/enterprise Google Business Profile active enough to influence local pack ranking and give a prospect who lands on the profile a reason to trust the brand. Target: at least 1 post per week, with a "Learn more" click-through rate above 2% of profile views. GMB posts are a trust signal and a minor ranking factor, not a primary lead-generation channel - do not overinvest relative to their actual reach.

---

## Core Principles

**1. GMB posts are read by people who already found you, not people you are trying to convert cold.** Anyone seeing a GMB post has already searched for the brand or a related local term. The job of the post is to confirm credibility and give a next step, not to sell from zero.

**2. Every post must sound like a different person wrote it.** GMB posts sit in a public feed where a prospect can scroll through the last 10-20 posts in under a minute. Identical or near-identical closing lines across posts are the single fastest way to signal "this account is automated" - which undercuts the exact trust signal the channel exists to build. See `templates/local.py`'s `gmb()` function for the enforced rule: no repeated closing sentence within the same batch, and no phrase from the banned-CTA list in `templates/_shared.py`.

**3. Specificity beats promotion.** A post naming a real training format, a real skill area, or a real outcome metric reads as informational. A post using generic urgency language ("don't miss out," "act now") reads as an ad and gets skipped, per Rule 5 in README's Global Content Rules (no promotional brand tone in content body).

**4. Any statistic in a GMB post must be source-attributable.** Precise-sounding numbers with no named source or year are the highest-risk pattern for this channel - a 300-character post has no room for a footnote, so either name the source inline in one clause or drop the exact figure in favor of a qualitative claim. See README's "Citation Verification" section.

**5. GMB is a stat-bearing channel and is subject to the governance sign-off rule.** Because GMB posts routinely carry a statistic (see Failure Mode #2 below), every GMB post requires a human reviewer's sign-off (name + date) before its `Status` can move to "Published," tracked on `publish_tracker_template.csv` (copy to a dated file per cycle). See `agents.md`'s Governance / review gate note for the full rule.

---

## Repeatable Post Structure

**Line 1: The specific hook (10-15 words)**
Name a real skill, format, or outcome. No generic openers like "We are excited to share."

**Body (2-4 short sentences, 40-80 words)**
One concrete idea: a training format, a common workplace problem it solves, or a result. No stacked claims.

**Closing line (1 sentence, varied per post)**
A specific, non-generic invitation to learn more, phrased differently from every other post in the same batch. Never use a phrase from the banned-CTA list (`templates/_shared.py`'s `BANNED_CTA_PHRASES`): "Don't miss out," "Take advantage of," "Click here," "Click on learn more," "Learn more," "Discover." The ban on "Discover" is unqualified in `templates/_shared.py`, not scoped to bare-imperative use, treat any use of the word as a phrase, not just its imperative form.

**Optimal length:** 150-300 characters total. GMB truncates longer posts in the default view.

---

## Cadence

- 1-2 posts per week is the sustainable range for a single-location or single-brand profile. Google's own guidance treats GMB posts as expiring content (roughly 7 days of prominent visibility), so consistency matters more than volume.
- Never publish more than one post per day; it reads as spam in the profile feed.

---

## Failure Modes

1. **Identical closing line across the batch.** This is the exact defect a real batch shipped with (24/24 rows ending in the same sentence) - flagged independently across four review personas as the single biggest credibility problem in the channel. Vary every closer.
2. **Precise unsourced statistics.** A number like "$438 billion annually" with no named source reads as fabricated in a promotional post; either cite it properly or state the claim qualitatively.
3. **Named third-party companies with unverifiable claims.** Citing a real company's internal practice ("Organizations like [Company] redeployed 8,000+ employees") with no public source is both a credibility risk and a misattribution risk to that company - remove the name or link the specific public source.
4. **Treating this as a sales channel.** GMB posts with a hard sell in every sentence undercut the "helpful local business" framing the channel depends on.

---

## Adaptation for Your Brand

GMB is print-only in single-run mode (see `agents.md`) and only writes a file inside a `--bulk` run - confirm the bulk log actually produced a row before assuming a week's post was captured. Treat this channel as low-effort, low-risk: a good post takes two minutes to review before it goes into the batch queue, so there is no excuse for skipping the human read-through this channel's short format makes easy.
