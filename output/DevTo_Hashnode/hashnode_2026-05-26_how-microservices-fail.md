---
title: "How Microservices Fail (and When You Should Avoid Them)"
published: true
description: Microservices solve real scaling problems. They also create new ones that teams rarely anticipate. Here is the honest accounting of what goes wrong and when the architecture is the wrong choice.
tags: microservices, architecture, backend, distributedsystems
canonical_url: https://hashnode.com
---

Microservices architecture has become the default recommendation for serious backend systems. The pattern's proponents make compelling arguments: independent deployability, technology flexibility per service, fault isolation, and the ability for multiple teams to work on different services without stepping on each other.

All of those benefits are real. So are the failure modes, which tend to be underrepresented in the same conversations. This article covers both honestly: how microservices fail in practice and the circumstances where they are the wrong architecture for the problem at hand.

## The Failure Modes That Surprise Teams

**Distributed monolith:** The most common microservices failure is not technical in the narrow sense. It is architectural. Teams decompose their application into many small services without decomposing the domain model or the release process. The result is a distributed monolith: dozens of services that must be deployed simultaneously because they share a database, or services that cannot function independently because their APIs are tightly coupled to the internal behavior of other services. The surface area of a monolith remains; the operational simplicity is gone.

This failure typically emerges when microservices decomposition is driven by technical team structure rather than domain boundaries. Conway's Law predicts that systems mirror the communication structure of the teams building them. A microservices architecture built to match an org chart often produces service boundaries that reflect reporting lines rather than meaningful domain separations.

**Network failure becomes a design problem.** In a monolith, a function call between modules succeeds or fails in-process. In a microservices architecture, every inter-service call is a network call. Network calls fail, time out, and return partial responses. Every service must handle the failures of every other service it depends on, and those failures cascade in ways that are not obvious from the individual service's behavior.

Teams that migrate from a monolith without internalizing this shift produce distributed systems that are less reliable than the monolith they replaced. A service that calls three other services, each with a 99% uptime, has a compound availability of approximately 97% before adding its own failure probability. Reliability engineering in microservices requires explicit investment in circuit breakers, timeouts, retry logic with backoff, bulkhead patterns, and graceful degradation. None of this is required at the same depth in a monolith.

**Testing complexity scales non-linearly.** Unit testing individual services is straightforward. Integration testing the behavior of five services that interact with each other is significantly harder. End-to-end testing across fifteen services is genuinely difficult and slow. Teams that migrate to microservices without adjusting their testing strategy discover that their test coverage effectively decreases as the number of services increases, because the interaction surface grows faster than the team's ability to cover it.

**Operational overhead is a recurring cost, not a one-time investment.** Each service requires its own deployment pipeline, its own observability configuration, its own scaling policies, its own secret management, and its own on-call runbooks. A team running fifteen services does not pay the operational overhead of one monolith multiplied by fifteen. They pay more than that, because the services interact and the interactions generate their own operational events. Teams that underestimate this overhead end up with services that are deployed but not truly maintained: inconsistent logging, missing alerts, undocumented deployment dependencies, and runbooks that were written at launch and never updated.

**Data management becomes genuinely hard.** Each microservice that owns its own data store eliminates cross-service transactions. Operations that would be a single database transaction in a monolith become distributed transactions in a microservices architecture. Distributed transactions require either the saga pattern, two-phase commit, or accepting eventual consistency. Each of these approaches adds complexity and requires the team to make explicit choices about consistency guarantees that a monolith handles automatically.

## When Microservices Are the Wrong Architecture

The pattern is overused. Specific circumstances where a monolith is the correct architecture:

**Small teams.** The independent deployability benefit of microservices requires enough engineers that multiple teams can work on different services in parallel without coordination. A team of three or four engineers gets no meaningful autonomy benefit from microservices and pays the full operational overhead. Martin Fowler's "microservices premium" observation holds: microservices impose a complexity overhead that only pays off above a threshold of team size, traffic volume, and organizational maturity that most small teams do not reach.

**Early-stage products with unstable domain models.** Microservices work best when service boundaries are well-understood and stable. Early-stage products change their domain model rapidly as product-market fit is discovered. Decomposing into microservices before the domain is understood produces service boundaries that need to be redrawn repeatedly, each redrawing requiring coordinated changes across multiple services and their consumers. A monolith allows domain model changes to be made in one place.

**Systems without significant scaling differentials between components.** The canonical microservices scaling argument is that you can scale the checkout service independently of the product catalog service if they have different load profiles. If your system does not have meaningful differences in load or resource requirements between its components, independent scaling provides no benefit. You are paying the operational overhead without receiving the scaling reward.

**Teams without distributed systems operational maturity.** Running microservices well requires investment in service meshes or API gateways, distributed tracing, centralized logging with correlation IDs, container orchestration, and blue-green or canary deployment infrastructure. Teams that do not have this operational foundation will run their microservices poorly, with less reliability than a well-run monolith.

## The Migration Path That Works

For teams that have reached the scale and organizational complexity where microservices make sense, the migration pattern that produces the best outcomes is incremental extraction rather than big-bang decomposition.

Start with a strangler fig approach: keep the monolith running and extract one well-bounded domain into a service when there is a compelling operational reason to do so (independent scaling requirement, team ownership clarity, technology change). The monolith shrinks as services are extracted. No service is created speculatively. Each extraction pays for itself before the next begins.

This approach also lets teams build operational maturity incrementally: one service's deployment pipeline, one service's observability configuration, one service's failure handling. By the time the team is running ten services, they have built the operational habits and tooling on simpler cases.

## The Honest Summary

Microservices solve the specific problems of large organizations with multiple teams shipping software to different parts of a system at different rates. They create substantial new problems that require significant engineering investment to manage well.

The question is not whether microservices are good or bad. The question is whether your organization's scale, team structure, and operational maturity are the ones where the tradeoff is favorable. For many teams that have adopted the pattern because it seemed like the right architecture for serious engineering, the honest answer is that a well-structured monolith would have delivered better outcomes with less effort.

---

*What drove your team's decision to adopt microservices? The distributed monolith failure mode is the one I see most often in teams that decomposed too early or along the wrong boundaries. What has your experience looked like?*
