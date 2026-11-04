# pstack upstream investigation, November 4, 2026

Investigation only. No port implementation, installation, release, upstream script execution, or changed baseline is part of this report. The recommendation is to prepare a reviewed update to **0.15.36**, with explicit adaptation decisions for orchestration and review, rather than treating it as a metadata bump.

## Source snapshots and method

- Retained reviewed source: **0.15.23**, `dbf49813a39c1a5389c5e28cb8e4c1c2379e2454`, recorded in [`provenance/baselines.json`](../provenance/baselines.json), under [`provenance/upstream-0.15.23/pstack`](../provenance/upstream-0.15.23/pstack). All **168 retained files** byte-match that official revision's Git blobs. The initial 0.15.15 baseline remains separate.
- Current official repository HEAD observed: **`bb68f2365eceafa0cb2d253112f675acf5f144cc`**, committed November 4 at 07:20:06 UTC. Its [pstack manifest][manifest] declares **0.15.36**. The last commit changing `pstack/` is [`c742dd6`, October 27, “make Orchestrate agentic and delete the orch scripts”][last-change]. HEAD also contains later changes to other plugins.
- Temporary official clone: `/tmp/pstack-upstream-investigation-20261104.nAozme/plugins`, cloned from `https://github.com/cursor/plugins.git` with blob filtering and sparse checkout of `pstack`. The clone is separate from the repository's retained baseline. Its checkout was clean after inspection.
- Current pstack Git tree: **`4719e1c4b4c43bac85d4206a8b41dd2899769c1c`**. It is identical at current HEAD and monitor revision `0f77cd5`. The monitor's older observed repository revision therefore does **not** mean its pstack finding is stale. The coordinator separately inspected issue #19 and the successful November 4 monitor run; this report independently checked content identity and counts.
- Comparison used Git history/diffs plus byte comparison of every retained/current file. Read the changed contracts and new skill entrypoints, selected helper changes, the statechart launcher/bootstrap, and the upstream Claude adapter. This is a semantic inventory, not an exhaustive correctness audit of every compiler implementation line.
The applicable local contract remains the [agreed specification](../docs/specs/pstack-for-codex.md) and [ADR](../docs/adr/0001-preserve-workflows-with-native-execution.md): official source, preserved workflow obligations, Codex-native models and local isolated workers, explicit substitutions, and source-backed qualification. An upstream implementation for another host does not establish Codex support.

## Complete inventory counts

Counts cover files physically under upstream `pstack/`, including excluded Benny/Grok Bot source, documentation, tests, fixtures, and assets. They are not distributable-package counts.

| Measure | Reviewed 0.15.23 | Current 0.15.36 |
| --- | ---: | ---: |
| Files | 168 | 573 |
| Bytes, file contents | 3,478,258 | 6,295,660 |
| Top-level skill directories with `SKILL.md` | 53 | 58 |
| Of those, principle skills | 24 | 24 |
| Of those, other skills | 29 | 34 |
| Poteto-mode playbooks | 23 | 23 |
| Agent definitions | 2 | 2 |
| Files executable in Git | 5 | 6 |

**412 added, 68 modified, 7 removed, 93 unchanged.** There are no removed skills or added/removed playbooks. Both agent definitions are byte-unchanged. The monitor's 487 differing paths are 412 + 68 + 7.
**407 of 412 added files belong to statechart.** That includes its skill and render instructions plus 405 script/config/test files. Of the 405, **376 are under `scripts/test/`**, including recorded TLC output, TLA+ examples, expected charts/reports, and test code; 29 are runtime/config files outside that test directory. Statechart contributes 2,878,251 bytes. The large count is primarily a new compiler and its test corpus, not hundreds of new workflows or image assets.
The other additions are four skill entrypoints and the Claude adapter. Removed: four Interrogate reference files (`code-quality-review`, `lead-judgment`, `reviewer-prompt`, `rubric`) and three orch files (`orch.test.ts`, `orch.ts`, `store.ts`).

## Five new skills

| Skill | Actual contract | Codex adaptation implication |
| --- | --- | --- |
| [sharpen][sharpen] | Deepen the task using professional methods, raw evidence, and an external correctness check, then rewrite the prompt while leaving the user's choices open. | Small instruction-only addition. Preserve upstream description wording and explicit invocation. |
| [create-formal-verification-skill][create-formal] | Pick a high-value property from code; choose the appropriate verifier; prove the check can fail; generate a project-local verify skill with coverage and sync commit. TLA+ is the default for event-order modeling. If no code verifier fits the language, use generated inputs against real code instead of a hand model of the function. Do not change product code without a request. | Add project-local skill authoring/routing and tool prerequisites. Preserve bounded claims, broken-variant evidence, and the boundary between verification edits and product fixes. This is a new available workflow, not a new mandatory port-release test suite. |
| [maintain-formal-verification-skill][maintain-formal] | Read changes since the sync commit, distinguish model drift from a product bug, update verification only, rerun and demonstrate sensitivity to a broken variant. Outcomes are in sync, updated, bug, or blocked; updated and bug can coexist. | Preserve coverage/sync metadata and scope. Blocked checks must not move their sync commit. |
| [statechart][statechart] | Run TLC against TLA+ specs; build Mermaid charts and shortest bug paths, with explicit bounds and unchecked-rule reporting. Replay modeled bugs against real code when modeling code. | New executable dependency surface requiring review. The launcher supports sufficiently recent Node, Bun, or Deno. First use can install pinned TLC 1.7.4 and Java Temurin 25 via mise; `TLA2TOOLS`/`JAVA` can supply alternatives. Image rendering specifies Pele 1.9.0. Confirm dependency bootstrap, writable scratch paths, subprocess/process-group cleanup, time/resource limits, and output behavior before claiming portability. |
| [ketchup-video][ketchup-video] | Follow ketchup's reporting scope, but render a short silent subtitled video outside the repository from actual work artifacts; inspect one frame per slide and measure readable holds. Fall back to calls when rendering fails. | Needs a reproducible video renderer and usable inline delivery in the recipient host. No specific renderer implementation is bundled. Availability in this research session is not proof for a friend's plugin. |

`setup-pstack` now offers formal verification separately and optionally. The create-formal skill routes every TLA+ result to statechart by skill name rather than copying release-dependent commands into generated skills. That dependency must be preserved in namespaced Codex routing. [Sources: setup][setup], [create formal][create-formal].
The statechart implementation's bounded follow-up checks and 500-state chart threshold are output constraints, not a claim to prove an entire real system. Its source documents cases where rules remain unchecked, state projection merges information, and a model bug may not reproduce in code. Retain these caveats. [Sources: statechart][statechart], [runtime/bootstrap][statechart-run], [renderer][statechart-render].

## Material changes to existing workflows

### Orchestration is a different implementation

Upstream replaced the large `orch` state-store/runtime protocol with a short [agentic orchestration contract][orchestrate]. The coordinator never writes code; one owner alone writes and carries each PR through merge. Fresh workers receive complete kickoffs. Sub-coordinators are reserved for an area with many parallel workers, with at most three levels and about ten in-flight workers per coordinator. Each PR needs an independent verifier on another model family. Start with one end-to-end unit before fan-out, inspect artifacts directly, track every child to a terminal disposition, and retry by failure cause at most twice.
The new text says to use the Project tracker/store, PR/CI event subscriptions where supported, and no scripts, polling loops, or status/message relaying. It assumes new cloud VMs by default and can fork workers when built state must survive. These are explicit host dependencies, not portable instruction syntax. In the Codex port, map each to verified current capabilities, preserve local worktree isolation, and record unsupported semantics. Do not silently retain the old orch runtime and call the result identical to 0.15.36. Conversely, do not delete the runtime until its current callers, recovery obligations, and compatibility ledger have a replacement.

### Interrogate now requires executable counterexamples

[Interrogate][interrogate] now reuses Arena's worktree fan-out rather than its former readonly review templates. Each adversary must run a failing test, repro, or real-tree probe; keep repros in its own worktree; and report command, actual output, and required output. For design review it must prototype or probe the tree. The parent reruns each command, retains only failures that violate intent, and merges shared root causes. It skips Arena's judging/selection phases and retains all verified findings. It still must not apply fixes.
This replaces broad Act-on/Consider/Noted/Dismissed judgments with Intent/Findings/Dropped and excludes unrun style, naming, structural, and hypothetical future risks. Four reference files disappear. Porting only the short new entrypoint without Arena's isolation and uncommitted-change copying would lose the new mechanism. It also changes the cost and scope of a review request, especially in read-only investigations: scratch repro work is part of the skill, product fixes are not.
[Arena][arena] now strictly requires a cross-judge from another model family; aliases to the parent cannot judge. When no other-family entry runs, it skips the judge and discloses that fact. Runner fallback also explicitly repairs a dropped panel to its intended minimum. The accepted GPT-only port cannot honestly satisfy cross-provider diversity. Decide and document whether the adapted Arena retains an independent same-provider judge as a substitution or follows the new skip rule; neither can be labeled equivalent provider diversity. The same limitation applies to Orchestrate's different-family verifier.

### Autopilot and shipping reduce repeated work while tightening evidence scope

[Autopilot-full][autopilot-full] runs a full verification swarm at code-ready, and again for new behavior, redesign, or a large new diff. Minor fixes, rebases, and conflict resolutions get one verifier at the new head; wording-only changes get none. The initial live behavior lane remains necessary. A blocking finding must be demonstrable at the head or a shipped documentation error. A pre-existing base defect does not block unless the change copies or newly reaches it. These are changed upstream gates, not discretionary simplifications by the port.
Owners report every later head, preserve recoverable state in the root store, and pin force-with-lease to the last owned SHA. Merge preparation reasons about affected files, callers, dependencies, and checks; some lockfile overlap can be resolved with a frozen install on the merge result. A third rebase beyond merge prep escalates colliding work to the coordinator. Countersigns do not bypass forge-enforced approvals. Hourly audit ticks report through ketchup only when something changed, and remain quiet otherwise. Preserve the user's existing grant and Codex's scheduling limits.
[Autopilot-stack][autopilot-stack] is now Autopilot-full without merge. Independent work branches from trunk; only real dependencies form a stack. Each PR stops verified and green, and nobody pushes after handoff without the operator's go. The previous requirement for one artificial linear stack is gone. [Multi-phase plan][multi-phase] reflects these new verification and delivery rules.
[Shipping][shipping] retains independent verification, a contiguous verified run, patch-equivalence checks, and bottom-up landing. It explicitly reads back merged state and trunk base because queue acceptance or auto-merge requests are not a completed merge. The stack is left alone while landing except for moving the next PR onto the merge result. The rewrite is shorter but still requires careful adaptation of forge semantics and verdict validity.

### Model effort, updates, reporting, and principles

- [Poteto-mode][mode] introduces task-sensitive reasoning and speed selection, preserves the configured model family, uses fast only when urgent except verification's role default, and prohibits retrying already-rejected slugs. Steers/resumes are background too. For Codex, keep model identity and reasoning effort separate and bind to the actual exposed schema; a Cursor `-fast` slug is not a Codex parameter. The new goal/problem/smallest-change restatement propagates into briefs, PRs, and final reports.
- [Reflect][reflect] explicitly forbids edits under `plugins/cache/`; show the intended local/user skill destination before approval, copy there after approval, and never PR/push the change. Adapt those destinations to Codex namespacing and skill precedence, and preserve Accepted approval and backlog authority boundaries.
- [Ketchup][ketchup] spends words on decisions, lists every waiting item without truncating to a word cap, names each item's user impact/evidence/risk, embeds real screenshots/video, and draws diagrams only when useful. It still distinguishes operator-only actions from work the agent can do.
- Seven principles change. Attack-the-premise, root-causes, testing, and idempotence become general reasoning instead of narrow rules. Testing explicitly distinguishes externally observable effects from private helper calls and permits valid empty/absence assertions. Explain-the-number now requires the decision threshold and noise floor before measuring. Type-system-discipline and migrate-callers lose several prescriptive sections. The TypeScript example uses a type guard instead of a cast. Treat these as upstream semantic edits, not mere formatting. [Principle sources][principles], [TypeScript example][typescript].

## Helper fixes and descriptions

The remaining helper changes are small but operationally material:

- [watch-pr GitHub adapter][watch-github]: distinguish fork heads during stack discovery; do not interpret an owner-approval gate's ACTION_REQUIRED as an ordinary failed check.
- [watch-pr polling policy][watch-policy]: cap ordinary and retry sleeps to the remaining timeout.
- [worktree audit][worktree-audit]: GNU/BSD stat/date support and Origin-first PR reads with GitHub fallback. This still contains Cursor transcript assumptions and upstream worktree parsing; preserve existing Codex path-with-spaces and transcript adaptations rather than replacing the ported helper wholesale.
- [check-plan][check-plan]: match inline code spans with equal backtick delimiters. Its caller/template changes must move together.
- Removed orch runtime, package script adjustment, and new statechart executable need explicit provenance dispositions, including tests/fixtures rather than silently dropping them.
Seven existing frontmatter descriptions changed: `interrogate`, `ketchup`, `principle-attack-the-premise`, `principle-explain-the-number`, `principle-fix-root-causes`, `principle-test-behavior-not-implementation`, and `principle-type-system-discipline`. Add source mappings for the five new descriptions and refresh those seven without inventing generic picker summaries. Preserve the port's source-derived description policy and separate Codex-only update and pinned companion descriptions.

## New official Claude Code distribution

Upstream now documents a generated Claude Code distribution, but it is not an official Codex distribution. The [adapter][claude-adapter] maps tools, worktrees, models, paths, history, and setup. Its blanket instruction to skip unsupported Cursor-only steps and leave placeholders differs from this port's source-backed, explicit-gap standard; do not import that behavior as a Codex compatibility proof.
Relevant source extends outside `pstack/`: [`scripts/generate-pstack-harness-trees.mjs`][generator], [`scripts/check-pstack-docs.mjs`][docs-check], and [`harness/pstack/`][harness]. The generator declares `pstack/` as source, generates a separate Claude tree, and excludes automations/assets. Its presence supports inspecting a thin adapter/generator approach, not replacing the retained original source with the generated tree. A future source monitor should account for these relevant outside-tree paths separately from the pstack content fingerprint. This investigation read the adapter and generator declarations but did not execute generation or qualify the Claude package.

## Recommended dependency order for a future update

1. **Pin and inventory.** Retain a new untouched 0.15.36 baseline and manifest alongside 0.15.23; enumerate all additions/deletions and outside-tree upstream references. No automatic synchronization.
2. **Resolve execution contracts.** Review current Codex tools against new model-effort selection, Arena cross-family judge, Interrogate writable repro workers, and Orchestrate tracker/store/events/forking. Decide the GPT-only review substitutions and the old orch runtime's disposition before porting callers.
3. **Move coupled existing workflows.** Adapt Arena/Interrogate, Orchestrate, Autopilot-full/stack, Shipping, and multi-phase templates together, then helper fixes, reflect, reporting, and principle changes. Preserve head-specific evidence and authority boundaries.
4. **Add new workflows.** Sharpen is smallest. Formal create/maintain and statechart form one dependency group; qualify statechart bootstrap and renderer prerequisites before release claims. Ketchup-video separately needs a concrete artifact/rendering contract.
5. **Refresh distribution evidence.** Update source-derived descriptions, namespaced links, package/catalog metadata, adaptation diff, dependency inventory, and per-contract qualification. Keep excluded Benny/Grok Bot disposition explicit. The coordinator found that current validation hardcodes two baselines/168 files and permits a limited extension set; review statechart fixtures and extensions deliberately rather than bypassing those checks. Use existing deterministic provenance/package checks; targeted helper or real-artifact checks should substantiate changed behavior without inventing a mandatory broad agent benchmark.
6. **Review before release/install.** Present the exact proposed package and unresolved assumptions. Installation, on-disk version, app activation, and observed workflow behavior remain separate gates. This investigation authorizes none of them.

## Evidence limits

Established here: official source revision/version, retained-baseline byte identity, complete tree counts/diff status, monitor content identity, source-level workflow changes and dependency assumptions. Not tested here: any upstream script, statechart/TLC/Java/Pele installation or run, video rendering, model selection, agent review behavior, local worker isolation/recovery, forge mutation, generated Claude distribution, Codex installation, picker activation, or recipient runtime compatibility. The coordinator verifies the port's own release/installed state separately; upstream freshness alone says nothing about installation.

[manifest]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/.cursor-plugin/plugin.json
[last-change]: https://github.com/cursor/plugins/commit/c742dd6
[sharpen]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/sharpen/SKILL.md
[create-formal]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/create-formal-verification-skill/SKILL.md
[maintain-formal]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/maintain-formal-verification-skill/SKILL.md
[statechart]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/statechart/SKILL.md
[statechart-run]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/statechart/scripts/run.ts
[statechart-render]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/statechart/references/render.md
[ketchup-video]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/ketchup-video/SKILL.md
[setup]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/setup-pstack/SKILL.md
[orchestrate]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/poteto-mode/playbooks/orchestrate.md
[mode]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/poteto-mode/SKILL.md
[interrogate]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/interrogate/SKILL.md
[arena]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/arena/SKILL.md
[autopilot-full]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/poteto-mode/playbooks/autopilot-full.md
[autopilot-stack]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/poteto-mode/playbooks/autopilot-stack.md
[multi-phase]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md
[shipping]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/poteto-mode/playbooks/shipping.md
[reflect]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/reflect/SKILL.md
[ketchup]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/ketchup/SKILL.md
[principles]: https://github.com/cursor/plugins/compare/dbf49813a39c1a5389c5e28cb8e4c1c2379e2454...bb68f2365eceafa0cb2d253112f675acf5f144cc
[typescript]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/typescript-best-practices/references/patterns.md
[watch-github]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/poteto-mode/scripts/watch-pr/github.ts
[watch-policy]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/poteto-mode/scripts/watch-pr/policy.ts
[worktree-audit]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/poteto-mode/scripts/worktree-audit.sh
[check-plan]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/skills/poteto-mode/scripts/check-plan.mjs
[claude-adapter]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack/docs/harness/claude-code.md
[generator]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/scripts/generate-pstack-harness-trees.mjs
[docs-check]: https://github.com/cursor/plugins/blob/bb68f2365eceafa0cb2d253112f675acf5f144cc/scripts/check-pstack-docs.mjs
[harness]: https://github.com/cursor/plugins/tree/bb68f2365eceafa0cb2d253112f675acf5f144cc/harness/pstack
