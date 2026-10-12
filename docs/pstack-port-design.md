# pstack port design interview

Status: scope agreed; consolidated design and interpretation of proof-oriented verification await final confirmation. No implementation or installation authorized by this interview.

## User's objective

Use the full power of Lauren Tan / poteto's pstack in Codex through a faithful port. Preserve substantial engineering behavior rather than merely copying instructions. The user is willing to omit capabilities whose porting complexity is disproportionate to their value.

Input: [October 7 reconnaissance](../recon/pstack-codex-recon-2026-10-07.md), based on official upstream commit `d0ef80d86795816da932a153458c5dbe192d294e`, pstack version `0.15.15`. Findings are static source evidence, not runtime proof.

## Decision tree

First frontier, accepted by the user October 11, 2026:

1. Target environment: Codex desktop first, keeping reusable instructions/helpers suitable for a later CLI adaptation. CLI parity is not a first-release requirement.
2. Model diversity: Codex-native GPT models for the first release. Preserve role configuration for later external-provider support; explicitly acknowledge that independent GPT review does not preserve Claude/Grok provider diversity.
3. Integration scope: defer Grok Bot UI and Benny Slack automation. Parallel engineering, verification, PR workflows, history, and long-running work remain candidates for inclusion.

Second frontier, accepted by the user October 12, 2026:

4. Fidelity: preserve upstream workflow steps, review standards, and evidence gates. Change execution mechanisms as needed and record every substitution or omission. Loading skills alone does not establish parity.
5. Parallel work: preserve independent local attempts, isolated writers, bounded concurrency, and consolidated results. A cloud execution service is deferred.
6. Long-running work: require unattended execution while the app/computer remain available, plus reliable recovery after interruption. Continuous execution through app closure, sleep, or offline periods is not required.
7. Upstream maintenance: use reviewed, pinned revisions and an explicit adaptation diff; no automatic upstream tracking.

Third frontier, answered October 12, 2026:

8. Invocation: explicit activation. Preserve both one-request use and explicitly entered sticky chat mode, as accepted in round four.
9. History and learning: preserve upstream behavior, not a newly designed approval model. Recall defaults to the active workspace and seven days for “recent,” combines scoped transcripts with shared sources, and verifies live artifacts. Reflect is explicitly requested, presents Accepted/Rejected/Backlog findings, and waits for approval before Accepted skill edits; backlog filing is automatic subject to available authorization/tools. Automate-me is a guided authoring flow with draft feedback and a PR.
10. Companion skills: accepted recommendation to inspect original companions, preserve requirements, reuse verified Codex equivalents, and port missing instructions.
11. Delivery authority: preserve upstream behavior. Code-change workflows normally commit and open ready PRs; opening a PR does not start babysitting. Babysitting does not authorize merge; explicit merge/land/ship/merge-when-ready requests route to Shipping. Upstream's always-pause list covers deploys, data deletion, force-pushes to shared branches, and customer messages. No pstack operations are authorized merely by agreeing to the design.

Evidence for round three: pinned README line 91 (one-message versus custom mode); `skills/reflect/SKILL.md` step 5 (explicit edit approval and automatic backlog); `skills/recall/SKILL.md` steps 1–5; `skills/automate-me/SKILL.md` steps 2–6; `skills/poteto-mode/playbooks/opening-a-pr.md`; `playbooks/babysit.md` steps 6 and 9; `skills/poteto-mode/SKILL.md` Autonomy section.

Required host adaptation: upstream broadly permits external actions including team-chat messages without asking. This cannot override Codex's higher-priority requirement for explicit authorization to send messages. Record that limit in the compatibility diff rather than promising identical authority. Installation alone also does not execute any workflow.

Fourth frontier, answered October 12, 2026:

12. Explicit invocation persistence: preserve both one-request attachment and explicitly entered sticky chat mode.
13. Distribution: a shareable, namespaced Codex plugin that the user can give to a friend, developed locally first and preserving existing skills. Include source attribution/license, pinned provenance, setup instructions, capability requirements, and explicit limitations. Do not embed personal paths, history, credentials, or account-specific model choices. Sharing does not itself request public publication.
14. Release gate: the user rejects a required testing program for port qualification and prefers proof-like verification. Proposed interpretation: establish a source-backed argument for each included workflow, with upstream requirements linked to adapted instructions/helpers, supported Codex capabilities, and explicit assumptions/deviations. Review reference closure, metadata/configuration, dependency requirements, authority, and writer isolation directly. Record any runtime-dependent claim as unestablished by source review; do not claim formal proof of agent compliance or observed execution. No mandatory end-to-end task suite. This changes how the port is qualified, not pstack's own TDD, reproduction, or real-artifact verification requirements when used for engineering work.

## Consolidated proposed design

- Adapt the pinned official source directly, preserving workflow contracts and documenting necessary Codex substitutions.
- Include engineering principles/playbooks, independent attempts/reviews, local isolated delegation, history/learning, PR workflows, and unattended work with recovery. Inspect/adapt original companion requirements and helpers.
- Defer cloud execution, non-GPT providers, continuous execution while the environment is unavailable, Grok Bot UI, and Benny.
- Support explicit single-request and sticky-mode activation in Codex desktop; treat persistence and runtime-tool compatibility as obligations to substantiate rather than assume.
- Produce a portable, shareable namespaced plugin with friend-facing installation/setup documentation and upstream attribution; perform no global install or public publication as part of the design interview.
- Qualify by a source-backed fidelity/compatibility argument with honest limits, not a mandatory behavioral test suite.

Final confirmation of shared understanding remains before implementation, including the proposed interpretation of proof-oriented verification.

Recommendations remain proposals until the user answers. Create glossary terms when their meanings are settled. Create ADRs only for accepted consequential tradeoffs.
