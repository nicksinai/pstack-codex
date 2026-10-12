# Faithful pstack port for Codex

Created October 12, 2026. Status: synthesized design specification, published as [GitHub issue #1](https://github.com/nicksinai/pstack-codex/issues/1); implementation and installation have not begun. This document records the agreed scope and the proposed interpretation of proof-oriented verification. It is not a claim of implemented compatibility.

## Problem Statement

Nick wants Lauren Tan / poteto's pstack engineering workflows in Codex, with enough fidelity to retain their value: deliberate design, independent parallel work, adversarial review, concise communication, and evidence before declaring completion. The official plugin assumes Cursor tools, configuration, models, companion skills, transcripts, custom modes, and cloud execution. Copying its instructions into Codex leaves those assumptions unresolved.

Nick also wants to share the result with a friend. A personal configuration tied to his machine or a collection of globally installed skills is insufficient. The result must be portable, attributable to its upstream source, understandable to another user, and safe to install alongside their existing skills.

## Solution

Produce a namespaced, shareable Codex plugin derived directly from the pinned official pstack source. Preserve upstream workflow steps, principles, review standards, and evidence requirements. Adapt execution to Codex desktop, native GPT models, and isolated local workers. Record each substitution and deliberate omission rather than silently simplifying the workflows.

Support explicit invocation for one request and explicitly entered sticky mode. Preserve history reconstruction, guided personalization, reflection approval, PR preparation, requested shipping, unattended execution while the environment remains available, and interruption recovery.

Qualify the port through a source-backed fidelity and compatibility argument. A mandatory behavioral test suite is not part of the release gate. Source review must distinguish established properties from assumptions and runtime-dependent claims.

## User Stories

1. As a developer, I want to install one identifiable plugin, so that I can use pstack without manually copying dozens of skills.
2. As a friend receiving the plugin, I want self-contained setup instructions, so that I can install it without access to Nick's machine or this conversation.
3. As an installer, I want existing skills and settings preserved, so that adoption does not overwrite my working environment.
4. As a user, I want explicit single-request invocation, so that pstack runs when I choose it.
5. As a user, I want explicitly entered sticky mode and a clear way to exit, so that pstack can guide a continuing conversation.
6. As a user, I want installation to make workflows available without executing them, so that installation and task authorization remain distinct.
7. As a developer, I want upstream playbook routing preserved, so that an investigation, feature, bug fix, or refactor receives the intended process.
8. As a developer, I want the engineering principles preserved and reachable, so that adapted workflows retain Lauren's standards.
9. As a developer, I want how, why, recall, and teach to retain their distinct purposes, so that source understanding, rationale, working context, and explanation are not collapsed into one generic summary.
10. As a developer, I want architect and arena to preserve competing design or implementation attempts, so that I can compare alternatives before committing to one.
11. As a developer, I want swarm to divide coverage into explicit slices, so that parallel work produces a consolidated result with gaps accounted for.
12. As a developer, I want each writing worker isolated from other writers, so that concurrent edits do not corrupt shared work.
13. As a coordinator, I want bounded concurrency and explicit ownership, so that local parallelism remains manageable.
14. As a coordinator, I want fresh and resumed delegates to receive the correct workflow instructions and state, so that continuation preserves the intended process.
15. As a reviewer, I want independent adversarial review and evidence-based synthesis, so that the result identifies supported findings rather than merely counting opinions.
16. As a user, I want the absence of Claude/Grok provider diversity disclosed, so that I understand the difference between independent GPT reviewers and upstream review panels.
17. As a user, I want configurable roles mapped to available models and reasoning effort, so that setup does not emit invalid Cursor model identifiers.
18. As a developer fixing a defect, I want reproduction, root-cause analysis, and real-artifact verification retained, so that the port does not weaken upstream engineering requirements.
19. As a developer, I want performance, benchmark, runtime-forensics, trace-forensics, and hillclimb workflows preserved, so that measured work retains its evidence discipline.
20. As a developer, I want prototype and visual-parity workflows preserved, so that design questions and visual changes receive the intended inspection.
21. As a developer, I want cleanup, comment review, TypeScript guidance, and technical writing preserved, so that code and prose receive upstream quality checks.
22. As a developer, I want project verification-skill creation and maintenance preserved, so that pstack can help establish and maintain a real-app verification path.
23. As a user recalling work, I want topic, time-window, and workspace boundaries preserved, so that unrelated private conversations stay outside the search.
24. As a user recalling a named subsystem, I want available shared sources and live artifacts consulted, so that my own chat history does not become the sole account of current state.
25. As a user requesting reflection, I want proposed edits shown before application, so that durable skill changes retain upstream's explicit approval gate.
26. As a user requesting personalization, I want a guided draft and feedback flow, so that my mode reflects my working conventions rather than invented preferences.
27. As a user, I want unavailable connectors reported accurately, so that missing evidence is not disguised as successful investigation.
28. As a developer, I want code-change workflows to prepare ready PRs as upstream prescribes, so that reviewable delivery is part of the workflow.
29. As a user, I want opening a PR, babysitting it, and merging it treated as distinct activities, so that each follows upstream triggers and authority.
30. As a user requesting shipping, I want independent verification and stack ordering preserved, so that only the eligible verified run lands.
31. As a user, I want my explicit delivery limits and Codex's governing instructions respected, so that plugin activation does not expand authority beyond the request.
32. As a user leaving a task unattended, I want progress while the execution environment is available, so that work can continue without continual prompting.
33. As a user returning after interruption, I want recovery from durable records and verified artifacts, so that the agent resumes from actual state.
34. As a coordinator, I want multi-phase, orchestration, and autopilot workflows adapted to local execution, so that complex programs retain their ownership and evidence rules.
35. As a user, I want decision trails and worktree cleanup retained, so that long-running work is reviewable and resources can be reclaimed under the intended safeguards.
36. As a maintainer, I want pinned upstream provenance and an explicit adaptation diff, so that updates remain reviewable.
37. As a maintainer, I want every included workflow's compatibility argument recorded, so that completion is based on accounted-for requirements.
38. As a recipient, I want known omissions and unsupported capabilities stated clearly, so that I can judge whether the plugin fits my environment.

## Implementation Decisions

### Source and scope

- Derive the port directly from Lauren Tan's official pstack, not a third-party port. The initial baseline is pstack version 0.15.15 at Cursor plugins repository commit `d0ef80d86795816da932a153458c5dbe192d294e`.
- Preserve the upstream baseline separately from adapted content and retain a reviewable file-level diff and source manifest.
- Account for all 51 registered top-level skills, both agent definitions, 23 playbooks, references, and executable helpers in the baseline. Exclude the Grok Bot UI skill from the first release; classify every other item as preserved, adapted, or explicitly blocked with a reason. The dormant Benny pack is excluded.
- Include the engineering, history, learning, verification, PR, orchestration, and unattended-work capabilities discussed in the interview. Complexity alone does not authorize silently dropping another workflow.
- Inspect the original companion instructions for cleanup, skill authoring, and UI/terminal control. Reuse Codex capabilities where their contracts match, and adapt missing instructions. Availability, provenance, licensing, and distribution requirements for companions must be resolved before bundling them.

### Codex execution boundary

- Target Codex desktop first. Keep reusable instructions and helpers separable from desktop-specific integration so CLI adaptation remains possible, without requiring CLI parity now.
- Use one shared compatibility contract for tool capabilities, delegation, role configuration, history access, invocation state, and continuation. Keep it small; avoid a separate agent execution runtime unless a concrete requirement establishes the need.
- Bind instructions to the actual supported target tool schemas. Documentation or a tool available in this research chat does not by itself establish availability for a friend's installed plugin.
- Preserve fresh-agent initialization and upstream resume semantics. The designated style wrapper must read the required mode/principle material; an agent name alone is not evidence of initialization.
- Use local workers rather than a cloud-worker service. Assign each writer its own worktree/branch and explicit location; creating a worktree alone does not move a worker into it.
- Account separately for shared runtime resources such as ports, browser sessions, and generated artifacts. Filesystem isolation does not isolate these automatically.
- Preserve concurrency limits, parent/child ownership, aggregation, cancellation, and recovery semantics. Unsupported nesting or control capabilities are explicit compatibility gaps.
- Use Codex-native models in the first release. Configure model identity and reasoning effort separately, validate supported choices, and retain upstream role distinctions. Independent GPT reviewers do not provide Claude/Grok provider diversity.

### Invocation and workflow behavior

- Keep entry explicit. Support a single-request invocation and explicitly entered sticky mode, with a clear exit. Establish how mode instructions persist across turns and recovery in the supported desktop environment; do not assume Cursor metadata implements this in Codex.
- Preserve upstream routing and workflow steps, including required review and evidence gates. Changes to execution syntax must not accidentally remove a gate.
- Preserve distinctions among read-only investigation, implementation, PR preparation, babysitting, shipping, and the two autopilot delivery modes. Resolve upstream ambiguities against the specific playbook and the user's scope; a generic PR-ending instruction does not turn a read-only investigation into a code change.
- Preserve upstream TDD, reproduction, behavioral verification, benchmark, and independent-review requirements when those workflows are used. The port's proof-oriented qualification is a separate concern.
- Adapt helper behavior together with its callers. Account for dependency bootstrap/install behavior, writable cache requirements, plan validation, GitHub/forge support, and platform/path assumptions, including paths with spaces.

### History, learning, and authority

- Preserve recall's active-workspace default, topic scope, and seven-day default for “recent.” Use a supplied state capsule when upstream says mining can be skipped.
- Preserve shared-source investigation and live-state checking. Scope transcript reads accurately and distinguish full execution records from summaries.
- Preserve explicit reflect invocation, Accepted/Rejected/Backlog presentation, approval before Accepted edits, and upstream routing of approved edits. Backlog filing requires a configured tracker and sufficient authority.
- Preserve automate-me's guided preference gathering, draft feedback, existing-skill update behavior, and PR delivery. Adapt storage without embedding one user's identity or machine layout.
- Code-change workflows normally commit and open ready PRs. PR creation does not automatically begin babysitting, and babysitting does not authorize merge. Explicit merge/land/ship/merge-when-ready requests route to Shipping.
- Preserve the upstream pause boundaries for deployment, data deletion, shared-branch force pushes, and customer messages, subject to the user's existing authorization and the host's governing instructions. Explicit user limits always govern the current task.
- Document the unavoidable host difference: upstream's broad permission for team-chat messaging cannot override Codex's explicit-authorization requirement. The plugin must not claim identical authority where the host forbids it.

### Unattended work and recovery

- Support unattended progress while the app/computer and required services remain available. Continuous operation through app closure, sleep, or offline periods is outside first-release scope.
- Distinguish an active-session wait from a durable scheduling mechanism. Create recurring follow-up work only when requested and supported; do not present a wait loop as persistent scheduling.
- Preserve decision trails, ownership records, verification ledgers, and continuation briefs sufficient to reconstruct interrupted work.
- Recover by inspecting current branches, diffs, PRs, recorded verdicts, and task state. Do not assume local workers survive restart, transcript timestamps prove liveness, or old verdicts apply to changed patches.

### Sharing and maintenance

- Deliver a namespaced plugin that can be given to a friend. Include installation/setup/removal guidance, required capabilities and dependencies, model setup, activation/exit instructions, limitations, source provenance, and applicable license notices.
- Keep personal paths, conversations, credentials, connector identifiers, and account-specific model choices out of the distributable. Recipients configure their own environment.
- Preserve existing skills and user configuration. Namespacing must also account for internal references and specialized agent identities, not just directory names.
- Select a supported distribution mechanism during implementation from current official plugin guidance. Shareability does not imply public marketplace publication or a guaranteed distribution format already established by this spec.
- Pin reviewed upstream versions. Updates require a new adaptation review and updated compatibility argument; no automatic upstream synchronization.

## Testing Decisions

The user explicitly chose proof-like verification instead of a required testing program. This section records that decision; it does not prescribe a mandatory end-to-end suite or probabilistic task benchmark.

Use one qualification boundary: the complete packaged plugin and its declared workflow contracts. Establish a requirement-by-requirement fidelity argument rather than creating new test seams throughout the implementation.

For each included workflow or helper, record:

1. The upstream requirement and exact source locator at the pinned revision.
2. The corresponding adapted instruction, configuration, or helper behavior.
3. The Codex capability on which it relies, with authoritative evidence for its supported contract.
4. The argument that prerequisites, ordering, ownership, approvals, evidence gates, and outputs are preserved.
5. Every deliberate substitution, omitted capability, and environmental assumption.
6. Its evidence status: established by source/configuration inspection, conditional on stated assumptions, or unresolved.

Review the package for complete internal references, valid declared metadata/configuration, dependency closure, source attribution, collision avoidance, portable setup, and exclusion of private material. Review helper control flow where it affects isolation, state, mutation, bootstrap, or continuation. Direct deterministic validation may support these arguments; building a dedicated test suite is not required.

The qualification record must include the lost provider diversity, local-versus-cloud execution substitution, invocation persistence, runtime tool availability for recipients, and interruption recovery assumptions. An unresolved obligation cannot be labeled established. Any blocker preventing an included core contract must be resolved or explicitly brought back for scope adjustment before calling that contract complete.

Source inspection can establish properties of instructions and deterministic implementation under stated premises. It cannot prove that a probabilistic agent will always comply, that an unobserved UI interaction succeeded, or that an unavailable service works. Report those limits without converting them into invented runtime evidence or silently weakening upstream requirements.

Existing reconnaissance, the dependency index, and the source hash manifest provide prior art for the evidence inventory. No implemented port or behavioral test harness currently exists in this checkout.

## Out of Scope

- Grok Bot UI and the dormant Benny Slack automation pack.
- A Cursor-equivalent cloud execution service.
- Claude/Grok provider integrations in the first release.
- Continuous execution while the app/computer cannot run the work.
- Equal first-release support for Codex CLI and desktop.
- Automatic upstream updates.
- A mandatory end-to-end test suite or benchmark program for qualifying the port.
- Global installation, public publication, or sending the plugin to a friend during specification work.

## Further Notes

### Source documents

- [Design interview](../pstack-port-design.md)
- [Architectural decision](../adr/0001-preserve-workflows-with-native-execution.md)
- [Domain glossary](../../GLOSSARY.md)
- [Reconnaissance](../../recon/pstack-codex-recon-2026-10-07.md)
- [Dependency index](../../recon/pstack-dependency-index.json)
- [Pinned source manifest](../../recon/upstream-manifest.json)
- [Official upstream baseline](https://github.com/cursor/plugins/tree/d0ef80d86795816da932a153458c5dbe192d294e/pstack)

### Delivery sequence

1. Establish supported Codex plugin, tool, invocation, and distribution contracts; inspect the original companion sources.
2. Build the source manifest, inventory, and compatibility/requirement ledger covering the complete baseline.
3. Adapt the core mode, references, agents, configuration, and local delegation; then adapt history, learning, helpers, PR operations, and continuation against the same contracts.
4. Assemble the distributable and friend-facing setup material; complete the source-backed qualification argument and expose remaining assumptions.
5. Present the exact package, adaptation diff, limitations, and qualification record for review before installation or publication.

These are dependency-ordered delivery milestones, not generated tracker tickets or a grant to implement them now.

### Publication status

The project repository is `nicksinai/pstack-codex`, with GitHub Issues configured as its tracker. This specification is published as [issue #1](https://github.com/nicksinai/pstack-codex/issues/1) with the `ready-for-agent` label. Project tracker, triage, and domain conventions are recorded in the repository. Readiness does not independently authorize implementation or installation.
