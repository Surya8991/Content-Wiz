---
title: How to Structure Large Frontend Applications
published: true
description: Frontend codebases rot the same way every time, folders that mirror file types instead of features. Here's how experienced teams structure apps that stay maintainable past 100,000 lines.
tags: frontend, architecture, react, webdev
canonical_url: https://hashnode.com
---

A frontend codebase that started clean six months ago now takes new engineers two weeks to navigate. The components folder has 400 files. Nobody remembers which of three state management patterns in use is the "correct" one. Every pull request touches five unrelated directories because a single feature's logic is scattered across `components/`, `hooks/`, `utils/`, and `services/`. This is not a tooling problem, it is a structural one, and it happens to almost every growing frontend team that never made deliberate architecture decisions.

Structure does not fix itself as a codebase scales. Teams that avoid the two-week-onboarding problem made specific choices early about folder organization, module boundaries, and state ownership.

## Feature-Based Folders Beat Layer-Based Folders

Most frontend projects start with a layer-based structure: a `components/` folder, a `hooks/` folder, a `services/` folder, a `utils/` folder. This works fine at 20 components. At 200, it stops working, because every feature's code is spread across four or five top-level directories, and understanding one feature means opening files in all of them.

Feature-based structure inverts this. Each feature or domain gets its own folder containing its components, hooks, types, and API calls:

```
src/
  features/
    checkout/
      components/
      hooks/
      api.ts
      types.ts
    inventory/
      components/
      hooks/
      api.ts
      types.ts
  shared/
    components/
    hooks/
    utils/
```

The `shared/` folder holds only code genuinely used across multiple features, not code that might be reused someday. Teams that put everything in `shared/` "just in case" end up back at layer-based structure with extra steps.

The payoff shows up in code review and onboarding. A reviewer looking at a checkout bug only opens `features/checkout/`. A new hire assigned to inventory has one folder to read, not five. Deleting a feature means deleting one directory instead of hunting for orphaned files across the tree.

## Module Boundaries Need Enforcement, Not Just Convention

Folder structure alone does not prevent coupling. Nothing stops a developer from importing `features/checkout/components/CartSummary` directly into `features/inventory/`, and once that happens a few times, the features stop being independent and the folder structure becomes decorative.

Enforce boundaries with tooling, not documentation. ESLint's `import/no-restricted-paths` rule, or the more purpose-built `eslint-plugin-boundaries`, can fail a build when one feature imports another feature's internals directly. The rule of thumb: features expose a public API, usually an `index.ts` barrel file with a deliberately small surface, and everything else in that folder stays private. Cross-feature communication happens through shared state, events, or the `shared/` layer, never through direct file imports.

This is the same discipline backend teams apply to service boundaries, applied to frontend code. It costs a small amount of setup time and saves the larger cost of untangling circular dependencies later.

## State Management Has to Scale With the App, Not Precede It

A common mistake is picking a global state library on day one and routing everything through it, including state that only one component needs. The opposite mistake, avoiding any structured state management until the prop-drilling becomes unbearable, is just as costly to unwind.

The workable middle ground treats state ownership as a decision made per piece of state, not per application:

- **Local component state** for anything a single component or its direct children need. Most UI state (form inputs, toggle states, modal visibility) belongs here and never needs to leave.
- **Feature-scoped state** for data shared within one feature but not outside it. A context provider or a feature-level store handles this without polluting global state.
- **Global state** reserved for genuinely cross-cutting data: authenticated user, feature flags, theme, active locale. If a piece of state is only read by two features, it is not automatically "global."
- **Server cache state** handled separately from client state. Libraries like TanStack Query or SWR manage server data (fetching, caching, invalidation) and should not be forced into the same store as client-only UI state. Mixing the two is one of the most common sources of stale-data bugs in large React apps.

Teams that separate server cache from client state see fewer bugs tied to stale or duplicated data, because the two have different lifecycles: server state goes stale and needs revalidation, client state doesn't.

## Design Systems Prevent Component Sprawl

Without a shared component library, every feature team rebuilds its own button, its own modal, its own form input, each with slightly different padding and slightly different accessibility behavior. This is how a codebase ends up with fourteen button components and no team confident which one is safe to change.

A design system does not need to be a separate published package on day one. It can start as a `shared/components/` folder with a documented, deliberately small API: a `Button`, an `Input`, a `Modal`, a handful of layout primitives. What matters is that it is the single source of truth, enforced by code review and ideally by a visual regression tool like Storybook combined with Chromatic. Once the org runs multiple frontend applications, extracting the design system into a versioned package, published internally via a private npm registry, keeps teams from silently drifting.

One accessible, tested `Button` component beats fourteen ad hoc ones, and it turns a design change into a one-line update instead of a company-wide search-and-replace.

## Monorepos and Micro-Frontends Solve Different Problems

As frontend applications multiply within an organization, teams reach for either a monorepo or a micro-frontend architecture, and conflating the two leads to the wrong tool for the problem.

A monorepo, managed with Turborepo, Nx, or pnpm workspaces, solves a build and code-sharing problem. Multiple applications and packages live in one repository, share tooling configuration, and share code through workspace packages instead of a published npm package for every internal utility. This is the right choice when one team, or a small number of coordinated teams, needs to move fast across several related applications without duplicating configuration.

Micro-frontends solve a different problem: independent deployment. When separate teams own separate parts of a single product surface and need to ship on their own schedules without coordinating a shared release, splitting the frontend into independently deployable applications composed at runtime, via Module Federation, single-spa, or iframe-based isolation, removes the release-train bottleneck. The tradeoff is real complexity: shared dependency versioning, cross-application styling consistency, and runtime integration all get harder. Micro-frontends earn that cost when organizational boundaries, not code size alone, are the actual bottleneck. Reaching for them because a monolith feels big, without an organizational reason to split ownership, adds operational overhead without solving the underlying problem.

## Build Performance Degrades Predictably, So Plan For It

Every large frontend application eventually hits slow builds and slow hot-reload cycles. This is predictable, not surprising, and teams that plan for it avoid the point where a rebuild takes minutes and developers start avoiding small changes.

The main levers are the same regardless of framework: incremental and cached builds, since Turborepo and Nx both cache task output and skip unchanged work, code splitting at the route and feature level so the bundler does not process the entire app on every change, and a dependency graph shallow enough that a change in one shared file does not invalidate unrelated parts of the build cache. Google's Web Vitals data has repeatedly tied larger JavaScript bundle sizes to worse Largest Contentful Paint and Interaction to Next Paint scores, which makes build and bundle discipline a user-facing concern, not just a developer-experience one.

Feature-based folder structure and enforced module boundaries pay off here too. A build system parallelizes and caches effectively only when it can tell which parts of the app actually depend on each other, and a codebase where everything imports everything cannot be split efficiently no matter which bundler runs it.

Getting this right at 50,000 lines is a matter of a few deliberate decisions. Getting it right at 500,000 lines across a dozen teams needs a documented architecture, tooling that enforces it, and, for teams considering the leap to independently deployed frontends, a solid grounding in [micro-frontends architecture training](https://www.edstellar.com/course/micro-frontends-architecture-training) before committing to the runtime and organizational complexity that comes with it.
