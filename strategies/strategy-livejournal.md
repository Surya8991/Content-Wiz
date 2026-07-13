# LiveJournal Personal-Voice Blog Strategy

_Last updated: 2026-07-13_


## Goal and Metric

Build a small, loyal readership on a nostalgia/personal-blogging platform by publishing genuinely reflective, first-person workplace essays that a brand-voice post could not credibly produce. Target: readable-to-completion rate over raw impressions - LiveJournal's audience rewards depth over reach, so track comment quality and return-reader signals over follower counts.

---

## Core Principles

**1. First-person voice on this platform is a disclosed brand persona, not an anonymous individual.** LiveJournal's culture is built on personal, confessional writing, which creates real disclosure risk if a corporate byline writes "I" without any signal that this is branded content. This tool's `livejournal_post` template (`templates/community.py`) intentionally uses first-person as a **disclosed** brand-voice choice - the byline and any closing course link identify the brand, so the "I" is never presented as an anonymous private individual. Do not remove the brand identification in pursuit of a "more authentic" feel; that is what makes the voice acceptable rather than deceptive.

**2. The angle must be genuinely uncommon, not a repackaged industry stat.** LiveJournal readers disengage immediately from posts that read as a blog-format ad. The best posts here start from a specific, slightly uncomfortable observation ("the strange loneliness of being the person everyone reports to but no one reports for") rather than a framework or a statistic.

**3. One source per post, never the same source twice in a cluster.** A cluster of posts published close together must not all lean on the same statistical anchor (e.g. citing the same Gallup report as the sole evidence in three different posts) - this is the single most-flagged defect in this channel's audit history. See README's "Cluster Citation Diversity Pass" for the exact research process to run before publishing more than one post in a cluster.

**4. Vague attribution is not attribution.** "Harvard Business Review has written extensively about..." with no article title, author, or year is functionally unverifiable and reads as fabricated to a skeptical reader, even when the underlying claim is true. Every citation needs a specific report or article name and a year.

---

## Repeatable Post Structure

**Opening (2-4 sentences):** A specific, personal-sounding observation or scene. No industry jargon in the first paragraph.

**Body (400-600 words):** Develop the observation with one or two illustrative (composite, non-identifying) scenarios. Weave in at most one verified statistic or named source, with a specific report/article title and year.

**Closing:** A reflective turn, not a hard pitch. Where a course/CTA link is included, it should read as an earned continuation of the thought, not a sales pivot - see the audience-tested pattern already working in this template: "...which is exactly what [course] teaches."

---

## Cadence

- 1 post per week per topic cluster is sustainable without exhausting a single source pool. Clusters of more than 3-4 posts in a short window should span multiple distinct source bases per the diversity rule above.

---

## Failure Modes

1. **Undisclosed personal-narrative voice.** A first-person post with no brand identification at all, read in isolation, can look like impersonation. Always confirm the byline/closing identifies the brand.
2. **Repeated single-source citation across a cluster.** Run the Cluster Citation Diversity Pass (README.md) before publishing the second post in a cluster that would otherwise share a source with the first.
3. **Vague named-but-unlinked references** ("HBR has found...", "research shows..."): always name the specific report and year, or drop the reference.
4. **Formulaic closing pattern repeated across every post** (same rhetorical question, same `<hr>` structure): vary the close, since a reader who reads 3-4 posts back to back will notice a repeated template faster than a repeated fact.

---

## Adaptation for Your Brand

If a brand decides its first-person voice should instead be attributed to a named individual (a real employee, a course facilitator) rather than the organization itself, that individual's name should appear on every post using that voice, and this file's disclosure rule still applies unchanged - the requirement is disclosure of who is actually speaking, not any particular byline format.
