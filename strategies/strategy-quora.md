# Quora Answer Strategy

_Last updated: 2026-07-13_


## Goal and Metric

Earn upvotes and "most viewed writer" credibility in relevant topic spaces by answering real, high-traffic questions directly and completely. Target: an upvote-to-view ratio that beats the space average, tracked per answer rather than aggregated, since Quora's algorithm resurfaces individual answers independently of when they were posted.

---

## Core Principles

**1. Answer the actual question asked, in the first sentence.** Quora readers and the platform's own ranking both penalize answers that build up to the point. State the direct answer first, then support it.

**2. Length should match the question's complexity, not a fixed template.** A tactical how-to question deserves a tight, scannable answer; a "why does X happen" question can support more explanation. The `quora()` template (`templates/community.py`) targets a single flat word range rather than a section-by-section budget, specifically to avoid the arithmetic mismatch that a rigid multi-section structure previously produced (section budgets that summed outside the stated overall cap) - keep any future revision to this template as one coherent range, not stacked section minimums/maximums that have to be manually re-verified to sum correctly.

**3. Credibility comes from specificity, not credentials alone.** A named framework, a concrete number, or a specific example outperforms an answer that only asserts expertise ("As someone with 10 years of experience...").

**4. Every statistic still needs a source, organization, and year** - Quora's format is more forgiving of inline citation than GMB or Tumblr's short formats, so there is no excuse for a bare unsourced number here.

---

## Repeatable Answer Structure

**Line 1: The direct answer.** One sentence, no preamble.

**Body (2-4 short paragraphs):** Support the direct answer with reasoning, a named framework, or a specific example. Break up long answers with short paragraphs, not walls of text.

**Optional closing:** A single sentence pointing to further resources (a course, a guide) only if it is a genuinely relevant next step for someone who asked this specific question - never a generic pitch bolted onto an unrelated answer.

**Optimal length:** 150-250 words for most questions; longer only when the question genuinely requires it.

---

## Cadence

- Answer opportunistically as relevant, high-traffic questions appear rather than on a fixed schedule - Quora's value comes from answering the right question, not from a consistent publishing cadence.

---

## Failure Modes

1. **Burying the answer under a long setup.** Quora readers and rankers reward getting to the point immediately.
2. **Section word-budgets that do not sum to the stated total.** If this template is ever revised to use multiple sections again, re-verify the arithmetic before shipping - this is the exact defect that was previously found and fixed here.
3. **Generic self-promotion unrelated to the specific question.** An answer that pivots to a course pitch regardless of what was actually asked reads as spam and gets downvoted.
4. **Unsourced statistics.** Same rule as every other channel: name the source, organization, and year.

---

## Adaptation for Your Brand

Quora rewards genuine expertise more directly than almost any other channel in this system - prioritize answers in topic spaces where the brand's own program data or client outcomes give a real, specific answer over answers that only restate general industry knowledge available anywhere else.
