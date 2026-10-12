# Published pstack implementation tickets

Status: approved and published October 12, 2026. Implementation has not started.

Parent specification: https://github.com/nicksinai/pstack-codex/issues/1

Section numbers below retain the approved draft identifiers. The table maps them to published GitHub issues. All 14 issues are labeled `ready-for-agent`, linked as native sub-issues of the specification, and connected by native blocking dependencies. The parent specification body, state, and labels remain unchanged.

## Published issue map

| Plan ticket | GitHub issue | Blocked by |
| --- | --- | --- |
| 1 | [#2](https://github.com/nicksinai/pstack-codex/issues/2) — Deliver a portable plugin with explicit prose workflows | None |
| 2 | [#3](https://github.com/nicksinai/pstack-codex/issues/3) — Deliver model-configured local delegation, how, and swarm | #2 |
| 3 | [#4](https://github.com/nicksinai/pstack-codex/issues/4) — Deliver competing designs and independent adversarial review | #3 |
| 4 | [#5](https://github.com/nicksinai/pstack-codex/issues/5) — Deliver scoped rationale, recall, teaching, and session pickup | #3 |
| 5 | [#6](https://github.com/nicksinai/pstack-codex/issues/6) — Deliver PR preparation, babysitting, and requested shipping | #4 |
| 6 | [#7](https://github.com/nicksinai/pstack-codex/issues/7) — Deliver faithful investigation and code-change routing | #5, #6 |
| 7 | [#8](https://github.com/nicksinai/pstack-codex/issues/8) — Deliver approved reflection and guided personal skill authoring | #5, #6 |
| 8 | [#9](https://github.com/nicksinai/pstack-codex/issues/9) — Deliver measured performance and forensic workflows | #7 |
| 9 | [#10](https://github.com/nicksinai/pstack-codex/issues/10) — Deliver prototype, visual parity, and project verification workflows | #7, #8 |
| 10 | [#11](https://github.com/nicksinai/pstack-codex/issues/11) — Deliver sticky mode, unattended continuation, and interruption recovery | #5 |
| 11 | [#12](https://github.com/nicksinai/pstack-codex/issues/12) — Deliver local program orchestration with durable ownership and verdicts | #7, #11 |
| 12 | [#13](https://github.com/nicksinai/pstack-codex/issues/13) — Deliver independent-PR and stacked-change autopilot | #12 |
| 13 | [#14](https://github.com/nicksinai/pstack-codex/issues/14) — Deliver evidence-based worktree cleanup | #5 |
| 14 | [#15](https://github.com/nicksinai/pstack-codex/issues/15) — Deliver a friend-shareable package with complete fidelity accounting | #9, #10, #13, #14 |

## Shared acceptance contract

Each ticket delivers a complete narrow user workflow, including instructions, relevant references, required execution adaptation, user-facing setup/help, and its source-backed qualification argument. Reuse the existing capability contract and proof ledger rather than creating separate adapter frameworks per ticket.

For each owned upstream requirement, record its pinned locator, adapted counterpart, Codex capability evidence, preservation argument, deviations/assumptions, and evidence status (established, conditional, unresolved). Complete reference closure for the slice. Source inspection is not proof of agent compliance or observed execution. No mandatory behavioral test suite is introduced; upstream testing and verification requirements remain part of the workflows themselves.

Native model selection remains GPT-only and provider diversity is explicitly absent. Local execution replaces cloud workers. Every ticket respects host authority, personal-data boundaries, existing skills/configuration, and the agreed deferred scope. If a required capability cannot be established, document the exact blocker and request a scope decision instead of silently dropping it or declaring completion.

Every upstream item has exactly one primary ticket owner in the baseline inventory. Cross-ticket callers link to the same authoritative contract; they do not maintain conflicting copies. A ticket's acceptance covers its owned slice. Final whole-package closure belongs to ticket 14.

## 1. Deliver a portable plugin with explicit prose workflows

**What to build:** A recipient can obtain a namespaced local plugin candidate, configure the supported environment, and explicitly invoke the upstream bro, unslop, and technical-writing workflows. Installation makes skills available without starting work. This is the first complete path through packaging, activation, instructions, output, and qualification; it is not a claim that the full mode is complete.

**Blocked by:** None.

- [ ] Establish current authoritative Codex desktop plugin, tool, explicit-invocation, and distribution contracts; record recipient-facing requirements and unknowns.
- [ ] Preserve pinned upstream provenance, attribution, license notices, and an explicit adaptation diff; initialize the complete baseline ownership inventory, including deferred items and all principle references.
- [ ] Package the three prose workflows with preserved upstream requirements and namespaced reference closure. Preserve existing recipient skills/configuration and use recipient-owned setup values.
- [ ] Provide installation/removal and explicit invocation instructions for this limited candidate without globally installing it as part of implementation.
- [ ] Complete the shared source-backed qualification contract for this slice and identify the contract future workflow tickets consume.

## 2. Deliver model-configured local delegation, how, and swarm

**What to build:** A user can configure native model roles, request a code walkthrough or partitioned investigation, and receive consolidated results from bounded local delegates with explicit ownership.

**Blocked by:** 1.

- [ ] Preserve setup-pstack role distinctions while validating model identity and reasoning effort separately against the supported target environment.
- [ ] Adapt how and swarm end to end, including briefs, required context reads, outputs, coverage gaps, and aggregation.
- [ ] Preserve poteto-agent initialization, fresh/resumed delegate rules, supported parent/child lifecycle operations, cancellation, and bounded concurrency.
- [ ] Allocate one explicit worktree/branch/location per writer; account for shared ports, sessions, artifacts, and available nesting depth. Reading workers need not receive unnecessary writing isolation.
- [ ] Establish the exact local-for-cloud substitution, disclose absent provider diversity, and complete the shared qualification contract.

## 3. Deliver competing designs and independent adversarial review

**What to build:** A user can request architect, arena, interrogate, or blinded evaluation and receive independently produced alternatives or findings plus a reasoned synthesis.

**Blocked by:** 2.

- [ ] Preserve architect's caller/data-shape exploration, arena's independent attempts and selection/grafting rules, and interrogate's shared rubric and lead judgment.
- [ ] Preserve scope, intent, candidate isolation, independent prompts, review outputs, and absence of automatic application of review suggestions.
- [ ] Adapt the eval playbook with sanitized candidate labels, blinded judging, and source/trace-based chain accounting where available; it remains a user-facing workflow, not a required port qualification suite.
- [ ] Explain precisely which upstream cross-family assumptions change with GPT-only models and which independence properties remain.
- [ ] Resolve all references owned by the slice and complete its qualification argument.

## 4. Deliver scoped rationale, recall, teaching, and session pickup

**What to build:** A user can ask why something exists, reconstruct recent work, understand it through teach, or resume a specific interrupted session without crossing unrelated history boundaries.

**Blocked by:** 2.

- [ ] Preserve why's source categories, investigators, synthesis, epistemic distinctions, missing-source handling, and citations; adapt teach's how-plus-why composition.
- [ ] Preserve recall's topic/workspace/time scope, seven-day default for recent, supplied-capsule shortcut, shared-source sweep, live-artifact checks, and brief format.
- [ ] Establish accurate Codex history/trace access, distinguishing summaries from full execution records and excluding inappropriate current, child, eval, and unrelated-workspace material.
- [ ] Preserve session-pickup's reconstruction of branches, worktrees, decisions, unfinished work, and current artifacts rather than replaying work from scratch.
- [ ] Complete the shared qualification contract for source permissions, schema assumptions, privacy boundaries, and unavailable connectors.

## 5. Deliver PR preparation, babysitting, and requested shipping

**What to build:** A developer can turn an upstream-style code change into a ready PR, request babysitting, and explicitly request verified shipping without those activities silently authorizing one another.

**Blocked by:** 3.

- [ ] Preserve opening-a-pr, ready-not-draft status, narrow commits/stacks, writing/cleanup requirements, supported forge selection, and available built-in PR-tool requirements.
- [ ] Inspect original cleanup companion requirements and establish licensed adaptation or verified equivalence for deslop, no-comments, and Comment Sicko, preserving their scope and output contracts.
- [ ] Preserve babysit modes, frontier ownership, conflict escalation, untrusted review-text handling, CI classification, and stopping at merge-ready.
- [ ] Preserve Shipping's independent per-PR verdict, current patch/head/base accounting, contiguous verified run, one-at-a-time merge, and post-merge recomputation.
- [ ] Adapt PR watcher helpers and dependency/bootstrap behavior with their callers; keep watcher wakeups distinct from durable scheduling.
- [ ] Establish merge/request and always-pause boundaries under host instructions and existing authorization. Provide a shared PR-delivery contract usable by learning workflows.
- [ ] Complete the shared qualification contract; never invent CI, review, or merge evidence.

## 6. Deliver faithful investigation and code-change routing

**What to build:** Explicit poteto mode routes investigation, feature, bug-fix, refactoring, and bespoke tasks through upstream engineering steps, producing source-backed answers or verified changes delivered as ready PRs.

**Blocked by:** 4, 5.

- [ ] Preserve mode routing, principle reads, verbatim playbook steps, explicit skipped-step accounting, data-shape requirements, throughput checkpoints, and evidence gates for the owned routes.
- [ ] Adapt investigation, feature, bug-fix, refactoring, and figure-it-out, including blast-radius, TDD, TypeScript guidance, correct, and mode help, using established rationale and delivery contracts.
- [ ] Integrate the cleanup/review requirements owned by ticket 5, preserving their required positions within code-change workflows.
- [ ] Preserve reproduction before fixes and real-artifact verification through PR delivery. Read-only investigation remains read-only.
- [ ] Account for all 24 principles and their cross-references, with one authoritative interpretation, and complete the shared qualification contract for owned routes.

## 7. Deliver approved reflection and guided personal skill authoring

**What to build:** A user can request reflect or automate-me and obtain durable skill improvements through the same review, approval, and drafting process upstream prescribes.

**Blocked by:** 4, 5.

- [ ] Preserve reflect's explicit trigger, reviewer lenses, synthesis, structural-enforcement check, Accepted/Rejected/Backlog output, and approval before Accepted edits.
- [ ] Preserve backlog filing subject to configured tracker and authority; route approved edits by their substantive or trivial scope.
- [ ] Preserve automate-me's existing-skill detection, scoped mining, preference gathering, iterative draft feedback, and PR delivery through the established delivery contract.
- [ ] Inspect the original skill-authoring companion, map its requirements to supported Codex authoring, and adapt the authoring-a-skill playbook with validation where available.
- [ ] Preserve existing skills and personal-data boundaries; complete the shared qualification contract for the learning/authoring route.

## 8. Deliver measured performance and forensic workflows

**What to build:** A user can request performance work, metric hillclimbing, runtime diagnosis, or captured-trace analysis and receive evidence tied to the actual metric or artifact.

**Blocked by:** 6.

- [ ] Preserve perf-issue, hillclimb, runtime-forensics, trace-forensics, benchmark-checklist, and explain-the-number requirements through their complete routes.
- [ ] Retain baseline, probe, unit, comparison, acceptance/rejection, and reporting rules; keep measured results distinct from assertions.
- [ ] Retain appropriate live verification and competing hypotheses rather than treating successful compilation as performance evidence.
- [ ] Tie unavailable profiling/control capabilities to explicit environment requirements or unresolved obligations.
- [ ] Complete the shared qualification contract and reference closure for the slice.

## 9. Deliver prototype, visual parity, and project verification workflows

**What to build:** A user can explore competing UI designs, pursue visual parity, and create or maintain a project-specific real-app verification workflow using supported Codex controls.

**Blocked by:** 6, 7.

- [ ] Inspect original UI/terminal control companions, provenance, licensing, and required behavior; map to supported controls and adapt missing instructions rather than relying on name similarity.
- [ ] Preserve prototype and visual-parity steps, artifact comparisons, environment requirements, and user-facing evidence standards.
- [ ] Adapt create-verification-skill and maintain-verification-skill, including feature maps, live passes, drift handling, intended storage, and scope limits.
- [ ] Document shared browser/terminal/runtime ownership and do not confuse independent worktrees with isolated running applications.
- [ ] Complete the shared qualification contract for controls, routes, generated references, and unavailable capabilities.

## 10. Deliver sticky mode, unattended continuation, and interruption recovery

**What to build:** A user can explicitly enter or leave sticky mode, let a task progress unattended while the environment is available, pause safely, and recover from interruption using actual artifacts.

**Blocked by:** 4.

- [ ] Establish supported persistence for explicitly entered sticky mode, task intent, and exit across turns; keep ordinary single-request use separate.
- [ ] Adapt autonomous-run, pause-safely, multi-phase-plan, and show-me-your-work with durable state, decision logs, continuation briefs, and explicit predicates.
- [ ] Distinguish active-session waits from supported recurring follow-ups, creating scheduled work only when requested and available.
- [ ] Recover from current branches/diffs, task records, and service state; do not assume worker survival, timestamp-based liveness, or applicability of an old verdict to a new patch.
- [ ] Adapt plan-checker/logging assumptions with their callers, including removal of Cursor-only wake syntax where replaced.
- [ ] Complete the shared qualification contract and disclose interruption/runtime availability limits.

## 11. Deliver local program orchestration with durable ownership and verdicts

**What to build:** A user can hand a multi-track engineering program to a local coordinator that assigns bounded work, collects results, maintains explicit ownership, and recovers its program state.

**Blocked by:** 6, 10.

- [ ] Adapt orchestrate's coordinator/worker/verifier responsibilities, supported nesting, briefs, frontier calculation, drain protocol, and one-writer rules.
- [ ] Preserve orchestration ledger/inbox/lock/state contracts and verdict identity; the ledger CLI remains state tooling rather than a second agent spawning runtime.
- [ ] Adapt orchestration helpers, dependency bootstrap, filesystem writes, and supported Git/forge assumptions together with instructions.
- [ ] Preserve verifier independence, changed-patch invalidation, blocked/failed verdict semantics, and exact reporting of current program state.
- [ ] Complete the shared qualification contract for ownership, scheduling boundaries, recovery, and local resource limits.

## 12. Deliver independent-PR and stacked-change autopilot

**What to build:** A user can explicitly request an autonomous queue of independent PRs to merge or a reviewed linear stack to land personally, retaining each mode's distinct ownership and delivery authority.

**Blocked by:** 11.

- [ ] Adapt autopilot-full and autopilot-stack end to end using established program, PR, review, and continuation contracts.
- [ ] Preserve one owner per unit, build/review/babysit sequencing, merge-ready or STACK-READY reports, and root verification duties.
- [ ] Keep stack topology changes serialized and distinguish independent PRs from dependent chains.
- [ ] Preserve the difference between authorized autonomous merging and building a stack for the operator to land; adapt local execution without silently changing delivery semantics.
- [ ] Complete the shared qualification contract for both routes, including interruption and failure paths.

## 13. Deliver evidence-based worktree cleanup

**What to build:** A user can obtain an accurate worktree cleanup assessment and carry out authorized cleanup with upstream safeguards and Codex-aware history/context.

**Blocked by:** 4.

- [ ] Adapt worktree-cleanup and its auditor together, preserving merge/PR/dirty/recent-work classification and intended human gates.
- [ ] Account accurately for paths with spaces, supported platform utilities, current trunk, ignored/untracked work, and managed-worktree lifecycle constraints.
- [ ] Replace Cursor transcript assumptions with the scoped history contract; distinguish an audit from ref-fetches, temporary writes, and deletion operations.
- [ ] Preserve work that is active, uncommitted, unpushed, or not established as disposable; describe limitations rather than classifying unknowns as safe.
- [ ] Complete the shared qualification contract for data preservation and authorized mutation boundaries.

## 14. Deliver a friend-shareable package with complete fidelity accounting

**What to build:** A friend can receive the complete namespaced plugin candidate, follow self-contained setup instructions, understand its capabilities and limits, and remove it without overwriting existing skills.

**Blocked by:** 8, 9, 12, 13.

- [ ] Account for all baseline skills, agents, playbooks, references, and helpers through their primary ticket ownership; include original companion adaptations and explicitly deferred Grok Bot UI/Benny.
- [ ] Integrate the exact supported distribution mechanism, installation/setup/removal instructions, role configuration, single-request/sticky activation, capability requirements, and troubleshooting.
- [ ] Close internal references, metadata/configuration, dependency/bootstrap/cache assumptions, namespace/agent collisions, license/provenance obligations, and portable setup requirements across the full package.
- [ ] Establish that the package excludes personal paths, histories, credentials, account-specific connector identifiers, and model choices.
- [ ] Consolidate the source-backed fidelity argument, adaptation diff, supported capabilities, assumptions, and unresolved claims. Resolve core-contract blockers or bring them back for an explicit scope decision before declaring the package complete.
- [ ] Present the exact package for review; do not globally install, publicly publish, or message a friend as an automatic consequence of completing this ticket.

## Dependency summary

1 → 2 → 3 → 5

2 → 4; 4 + 5 → 6, 7; 6 → 8; 6 + 7 → 9

4 → 10, 13; 6 + 10 → 11 → 12

8 + 9 + 12 + 13 → 14

Transitive blockers are deliberately omitted. During parallel implementation, shared capability contracts, manifests, and namespace edits need one integration owner; independently owned workflow content can proceed at the frontier. Ticket 14 checks cross-ticket caller closure.
