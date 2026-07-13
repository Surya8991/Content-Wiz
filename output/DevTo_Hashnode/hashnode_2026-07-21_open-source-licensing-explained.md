---
title: Open Source Licensing Explained for Developers
published: true
description: Open source licenses carry legal weight most engineering teams never read closely. Here is what permissive and copyleft terms actually mean for your product.
tags: opensource, licensing, legal, softwaredevelopment
canonical_url: https://hashnode.com
---

Every commercial codebase ships with dozens of open source dependencies, and almost none of those dependencies get a license review before someone runs `npm install` or `pip install`. Synopsys publishes an annual Open Source Security and Risk Analysis report, and its 2024 edition found license conflicts in the majority of scanned commercial codebases. Engineering teams treat licensing as a legal afterthought, but license terms determine what a company can build, sell, and keep proprietary.

This is a practical breakdown of what license categories mean for engineering decisions, where teams get into trouble, and what a working audit process looks like.

## Permissive vs Copyleft: The Core Distinction

Open source licenses split into two functional categories, and the difference between them changes what you owe downstream.

**Permissive licenses** (MIT, Apache 2.0, BSD) let you use, modify, and redistribute code with minimal obligations. You keep the original copyright notice and license text in your distribution. Beyond that, you can embed the code in a closed-source commercial product, modify it privately, and never publish your changes. Apache 2.0 adds an explicit patent grant: contributors license their patents covering the code to users, closing a legal gap that MIT and BSD leave open. Most companies building commercial software default to permissive dependencies specifically because they impose no reciprocal obligation.

**Copyleft licenses** (GPL, AGPL, LGPL) require derivative works to carry the same license. The GNU General Public License mandates that if you distribute a modified version of GPL-licensed code, or a work that links against it in ways the license treats as derivative, you must release your source code under the GPL too. The Affero GPL (AGPL) closes the loophole that let companies run modified GPL code as a network service without distributing anything: it triggers the same source-disclosure obligation the moment users interact with the software over a network, not just when you ship a binary. The Lesser GPL (LGPL) sits in between: it permits linking from proprietary code without forcing that code to inherit the GPL, but modifications to the LGPL component itself still require release.

The practical takeaway: permissive licenses ask you to give credit, copyleft licenses ask you to give code back, and AGPL asks you to give code back even for software you never physically ship.

## What This Means for Commercial Products

A company embedding OSS in a commercial product faces a direct decision tree. Permissive dependencies are safe defaults for proprietary products because they impose no disclosure requirement.

GPL dependencies are workable if you treat them as intentionally isolated components, not casually imported utilities. Static linking or direct code inclusion of GPL code generally pulls your surrounding code into GPL obligations. Calling a GPL-licensed tool as a separate process, or interacting with it over a well-defined interface without linking, keeps more legal separation, though the exact boundary is a genuinely contested area of software law and depends on how courts interpret "derivative work" in a given jurisdiction.

AGPL dependencies are the highest-risk category for any company running software as a service. If your product is a SaaS platform and it incorporates AGPL code anywhere in its serving path, you may owe your users the complete source of your modifications, including proprietary business logic layered on top. Legal teams at SaaS companies frequently ban AGPL outright rather than litigate the boundary case by case.

None of this is optional once you distribute or operate the software commercially. A startup that builds a core feature on an AGPL library and only discovers the obligation during due diligence for a funding round or acquisition faces a real, expensive problem: rewriting the component, negotiating a commercial license from the copyright holder, or disclosing source code they never intended to release.

## License Compatibility Conflicts

Dependencies do not exist in isolation. Your application likely imports dozens of packages, each carrying its own license, and those licenses have to coexist. Compatibility conflicts happen when two licenses in the same dependency tree impose contradictory obligations.

The most common conflict: a GPL-licensed library and an Apache 2.0-licensed library used together in ways that create a combined work. GPLv2 and Apache 2.0 are considered incompatible by the Free Software Foundation because Apache 2.0's patent termination clause conflicts with GPLv2's terms. GPLv3 resolved this specific conflict and is compatible with Apache 2.0. This means the GPL version in your dependency tree matters, not just the fact that something is "GPL licensed."

A second common conflict arises from license proliferation within a single project: one contributor pulls in an AGPL utility, another pulls in a BSD-licensed one, and nobody checks whether the combination is legally coherent. Compatibility is not symmetric or transitive in the way developers often assume. Two licenses that are each individually permissive can still create a problematic combination depending on how the code is integrated.

Resolving a conflict usually means replacing one of the conflicting dependencies, isolating the conflicting component behind a clean interface boundary, or in rare cases negotiating a dual-license or commercial license directly with the maintainer.

## Dependency Auditing and SBOM Practices

Manual license review does not scale past a handful of dependencies, and modern applications routinely carry hundreds of transitive dependencies through package managers. Automated auditing is the only workable approach at scale.

A Software Bill of Materials (SBOM) is a structured inventory of every component in your software, including transitive dependencies, versions, and license identifiers. The SPDX and CycloneDX formats are the two dominant SBOM standards, and both are now referenced in procurement requirements from large enterprise buyers and government contracts, following the U.S. Executive Order on cybersecurity that pushed SBOM adoption starting in 2021.

Tools like FOSSA, Snyk, and the OSS Review Toolkit scan a dependency tree, resolve each package's declared license, flag known conflicts, and generate an SBOM automatically as part of a CI pipeline. Running this scan on every pull request, not just at release time, catches license problems when a single dependency change is easy to revert, rather than months later when the offending library is load-bearing.

A working audit process defines an allowed license list (typically MIT, Apache 2.0, BSD variants, and a small number of explicitly reviewed exceptions), fails CI automatically when a new dependency falls outside that list, and requires a documented legal sign-off for any exception. Without automation, license drift accumulates the same way technical debt does: silently, until an acquisition, audit, or customer security questionnaire forces a reckoning.

## Common Mistakes Engineering Teams Make

**Shipping AGPL code without realizing it.** Package managers do not surface license terms prominently, and a transitive dependency three levels deep can carry an AGPL license that nobody on the team ever sees directly. This is the single most expensive licensing mistake because it is invisible until legal, a customer, or an acquirer asks about it.

**Ignoring license changes on upgrade.** A dependency's license can change between versions. Several notable projects (Redis, Elasticsearch, Terraform's underlying tooling) moved away from permissive or fully open licenses to source-available licenses like the Business Source License or the Server Side Public License in recent years. A team that pins a dependency version and upgrades blindly during routine maintenance can inherit new legal terms without any code change triggering a review.

**Treating "open source" as a single legal category.** Developers frequently assume all open source licenses are functionally interchangeable because the code is publicly visible. The legal obligations attached to MIT and AGPL are entirely different despite both being labeled open source, and conflating them is the root cause of most licensing incidents.

**Skipping license review for internal tools.** Internal-only software still triggers obligations under AGPL and, in some interpretations, GPL if the tool is later exposed as a service or spun out as a product. License decisions made for internal convenience have a way of becoming production liabilities once a prototype ships.

Licensing is not a one-time checkbox. It is an ongoing constraint that shifts every time a dependency updates, a new package gets added, or a product's deployment model changes from on-premise to SaaS. Treating it with the same rigor as security scanning, rather than as a legal formality handled once at project kickoff, is what keeps a growing dependency tree from becoming a growing liability.
