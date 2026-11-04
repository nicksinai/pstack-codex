# Existing workflow qualification for upstream 0.15.36

Source is the official `cursor/plugins` revision `bb68f2365eceafa0cb2d253112f675acf5f144cc`, compared with the retained 0.15.23 baseline. This argument covers existing workflows and helpers. New-skill qualification and the release inventory account for the other source files. Historical issue qualification remains historical where this update removes an entry point.

## Review and execution changes

| Source | Preserved behavior | Codex adaptation and evidence limit |
| --- | --- | --- |
| `skills/arena/SKILL.md` | Runner replacement restores the intended minimum; generation seats may repeat; judges start only after terminal candidates; unavailable other-family judge explicitly skips to parent selection; synthesis discloses dropouts and skipped judgment. | Native role validation replaces Cursor slugs. Different GPT variants are not other-family evidence. The GPT-only package explicitly skips Phase C rather than falsely claiming cross-family review. Candidate worktrees, fresh-context briefs and private rubric isolation remain required. |
| `skills/interrogate/SKILL.md` | Exact named scope or merge-base through working tree; restated intent; writable independent repro worktrees; executable failures only; coordinator reruns commands, merges roots, reports Intent/Findings/Dropped without applying fixes; skips Arena C/D/E. | Native general-purpose child operation replaces `generalPurpose`. Tracked and untracked scope inputs are copied deliberately. Command inspection, isolated reruns and host authority apply. Unavailable runtime is a disclosed verification limit, never a proven finding. |
| Removed `skills/interrogate/references/{code-quality-review,lead-judgment,reviewer-prompt,rubric}.md` | Upstream replaced rubric/lens review with executable adversarial evidence. | Removed packaged templates and active callers. Historical qualification links become historical path text. |
| `skills/poteto-mode/SKILL.md` | Changed principle triggers, task-dependent reasoning/speed and dependency-only Autopilot stacking. | Keeps explicit single-request/sticky scope, receiving-chat ownership, complete namespaced lookup, actual wrapper initialization and user/host authority. Adds five new skill routes. |
| `skills/principle-attack-the-premise/SKILL.md` | Test a falsifiable premise rather than requiring an actor-imbalance census. | Current upstream body with namespaced links and shared authority preamble. |
| `skills/principle-explain-the-number/SKILL.md` | Apply before measurement as well as before reporting or acting on it. | Current upstream body; measurable-work and evidence requirements retained. |
| `skills/principle-fix-root-causes/SKILL.md` | Locate the first wrong state; guards are fixes only for legitimate states. | Current upstream body and namespaced principle links. |
| `skills/principle-test-behavior-not-implementation/SKILL.md` | Assert user-observable behavior, tolerate internal redesign and omit low-value regressions. | Current upstream body and original examples; no artificial assertion requirement retained. |
| `skills/principle-type-system-discipline/SKILL.md` | Avoid type assertions through predicates and boundary parsing. | Current upstream body and links. |
| `skills/principle-make-operations-idempotent/SKILL.md` | Distinguishes unavoidable effect repetition and replay-safe convergence. | Three-way source merge preserves Codex preamble. |
| `skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md` | Updated small migration principle without the removed machinery. | Three-way source merge preserves namespace and authority. |
| `skills/correct/SKILL.md`, `skills/figure-it-out/SKILL.md` | Current upstream wording and workflow delta. | Three-way merge retains scoped invocation and bound shared references. |
| `skills/typescript-best-practices/{SKILL.md,references/patterns.md}` | Predicate-based branded primitive validation replaces the assertion example. | Source merge preserves the full examples and native links. |

## Executable helpers

| Source | Result and evidence |
| --- | --- |
| `skills/poteto-mode/scripts/check-plan.{mjs,test.ts}` | Upstream matching multi-backtick inline spans and regression cases merged. Existing fenced-block checks retained. |
| `skills/poteto-mode/scripts/watch-pr/{github.ts,github.test.ts,types.ts}` | Upstream fork identity prevents same-named fork heads entering repository stacks; owner-approval ACTION_REQUIRED gate is classified consistently on both read paths. Existing fail-closed pagination regressions retained. |
| `skills/poteto-mode/scripts/watch-pr/{policy.ts,policy.test.ts}` | Upstream timeout clamps each poll/retry sleep to remaining deadline; disabled deadlines preserve interval. Retained port pagination checks plus new deadline cases. |
| `skills/poteto-mode/scripts/package.json` | Removed obsolete orch test route. Retained locked dependency cache bootstrap. Explicit Bun compiler launcher avoids accidentally routing the locked TypeScript executable through an incompatible system Node. |
| Removed `skills/poteto-mode/scripts/orch/{orch.ts,store.ts,orch.test.ts}` | Removed packaged runtime; test was already source-only. Native orchestration contracts replace its callers. No new orchestration runtime added. |
| `skills/poteto-mode/scripts/worktree-audit.sh` | Retained reviewed Python read-only adapter and shell entrypoint. Python datetime/stat avoids upstream GNU/BSD flag differences by construction. Explicit authenticated GitHub reads remain the supported PR provider; this port does not claim upstream Origin CLI fallback. Unknown PR/activity state holds for review, no guessed integration or direct Cursor transcript scan, no deletion/ref mutation. |

The reviewed watcher launcher installed only locked dependencies with scripts disabled in a private temporary cache outside the package. Its `--help` completed. The cached current helper tests passed **76 tests, 194 assertions**, including deadline, fork identity, owner approval and retained pagination cases. `bun run typecheck` passed after using the explicit Bun compiler launcher. The first direct test attempt without a prepared dependency cache failed on missing Commander; the corrected cache execution is the successful qualification. These are deterministic helper checks, not a claim that live repository CI, merge operations or unattended deployment ran.

## Host capability boundary

The exposed collaboration schema provides spawn, terminal mailbox waiting, messaging, follow-up and interruption. `send_message` does not wake an idle child; `followup_task` does. `fork_turns` is parent-history inheritance, not cloning a running worker's state. Native GPT model identity and reasoning effort are separate fields; role configuration is validated against the invocation's schema, and no unsupported speed field or upstream slug is sent. Missing fields are disclosed rather than invented. A recipient may expose a different tool set; every operation is conditional on that actual binding.

The per-job model contract raises effort for difficult work, lowers it for judgment/routine work, preserves verification's configured worker settings, and reserves fast mode for urgency when the host actually exposes it. Native limitations do not weaken mandatory proof or owner boundaries. No tests here claim cross-provider diversity, cloud VM cloning, event subscriptions, durable unattended execution, or external-message authority.

## History and help source accounting

Source is cursor/plugins commit bb68f2365eceafa0cb2d253112f675acf5f144cc, pstack/skills. Compared complete assigned directories with retained provenance/upstream-0.15.23/pstack/skills. No added or deleted source files in these eleven directories. Twelve source files changed (eleven entrypoints plus poteto-help/references/recipes.md); all accounted below. Unchanged supporting prompts, history adapters and helpers retained.

| Source locator | Adapted destination / fidelity argument |
| --- | --- |
| automate-me/SKILL.md, Mine their history | pstack-automate-me adds per-job effort/speed choice through shared mode/models binding; bounded disjoint metadata-filtered history retained. |
| how/SKILL.md, opening spawn guidance | pstack-how retains specialized explorer/explainer read-only paths and adds native control binding. |
| ketchup/SKILL.md, full changed body and description | pstack-ketchup carries upstream wording for every waiting item, summary under 100 words, about 30 per item without dropping items, grouped decisions with per-item risk, every considered option, inline media, six-box/eight-word visuals, no status-only visuals, no invented calls, and no redundant facts. Added native current-chat/read-state/visual capability binding; retained no task resumption. Description is exact upstream excerpt. |
| no-comments/SKILL.md, step 1 | pstack-no-comments retains isolated Comment Sicko writer wrapper and adds per-job control binding. |
| poteto-help/SKILL.md, setup/router/playbooks | pstack-poteto-help adds formal-verification missing/stale checks, both optional setup offers, all five new routes, full-item ketchup promise, no-merge autopilot wording. Notes upstream Claude Code adapter separately without importing its unavailable-feature skipping policy. |
| poteto-help/references/recipes.md | Adds sharpen, formal verification/create-maintain prompt; Dropped terminology; pending-item ketchup; no-merge autopilot. Native active-session continuation wording retained. |
| recall/SKILL.md, mining step | pstack-recall adds effort/speed binding and keeps seven-day/workspace/topic/full-trace rules and shared-source sweep intact. |
| reflect/SKILL.md, spawn and approved rows | pstack-reflect adds controls; destination shown before approval; never edit plugins/cache, copy full folder to verified recipient-owned Codex skill root after approval, preserve existing contents/policy; no PR/push including authoring companion. Accepted/Rejected/Backlog and host-governed tracker authority retained. |
| setup-pstack/SKILL.md, roles and formal offer | pstack-setup-pstack adds ordered one-judge pool, different family only, aliases never judge, disclose no eligible family; optional formal verification offer once only when absent. Native validated separate role/effort config retained. |
| show-me-your-work/SKILL.md, audit delegate | Adds native controls; original execution-trace and append-only audit gates retained, independent same-GPT fallback still disclosed rather than claimed provider diversity. |
| swarm/SKILL.md, frame/report | Adds native controls; upstream removed redundant opening/total-worker/report prose. Existing total N versus bounded native capacity retained as required local-adapter invariant. Final consolidated result table, gaps and race rule retained. |
| why/SKILL.md, opening role guidance | Adds native controls; specialized seven-category source investigators and epistemic separation retained. |

## Evidence and limits

Read actual wrapper, mode, repository spec, delegation, compatibility, models, authoring companion and writing-for-agents/skill-creator instructions. Actual collaboration spawn schema in this task exposes model and reasoning_effort with inheritance restrictions; it has no speed parameter. Added prose explicitly leaves unavailable controls inherited/unset and records that fact. Recipients must inspect their own schemas, not inherit this chat's entitlement assumptions. No new tool or successful model/speed execution is claimed.

Direct checks passed for all eleven: name/directory correspondence, valid quoted description scalars, exact upstream substring descriptions and picker short descriptions, preserved explicit-only policy, and all local Markdown links except the intentional forthcoming pstack-create-formal-verification-skill integration target. Git diff --check passed. Optional skill-creator quick_validate.py could not start because system Python lacks PyYAML; no dependency installed. Direct checks replace only its structural checks, not behavior evidence. No probabilistic execution or external service success claimed.

Integrated companion changes update ketchup-capabilities, shared model controls and Arena cross-family behavior. Five new targets, provenance ledgers and full package checks are qualified by the release coordinator.

## Playbook source accounting

Source: official Cursor plugins commit `bb68f2365eceafa0cb2d253112f675acf5f144cc`, `plugins/pstack/skills/poteto-mode/playbooks/`; comparison baseline is pinned 0.15.23. Destination is `plugin/pstack/playbooks/` except session-pickup, which remains in `references/session-pickup.md`.

## Source accounting

| Changed source | Preserved change and Codex adaptation |
| --- | --- |
| autonomous-run | Per-worker effort/speed guidance retained through validated models contract; event/heartbeat uses actual bounded host wait, separately requested schedule, no Cursor loop API. Existing goal/predicate/iteration/evidence preserved. |
| autopilot-full | Complete seven-step current source retained. Full swarm initial/major; one verifier rebase/conflict/minor; none wording-only. Live lane and receipts remain mandatory at initial code-ready review. Demonstrable head defects or wrong shipped docs block; base defect only if copied/newly reached. Lockfile frozen-install exception, caller/dependency merge-result tests and third-rebase escalation retained. One PR owner, current CI, pinned lease, recoverable trails, fresh countersign and enforced forge approvals retained. Local worktrees replace VMs. Replacement may inspect while cancellation runs but cannot become concurrent PR writer. Hourly active waits are not durable schedules; changed audits notify, quiet audits stay quiet. |
| autopilot-stack | Entire new two-step source retained: run Full without merging; current-head verified+green handoff; no push after handoff without operator go; every tick names no-merge playbook. Only real dependencies stack; each owner rebases on its own parent; unchanged patch-id preserves verdict. Removed obsolete root stacker/STACK-READY protocol. |
| babysit | Both Full and Stack owners babysit/rebase their own PR. Removed obsolete root-as-stack-owner exception. All mode/frontier/queued stop/triage boundaries retained. |
| bug-fix | New effort/speed instruction added through models; source workflow and existing Codex authority binding preserved. |
| eval | Only new effort/speed instruction added; prior detailed sanitized environments, fresh context, trace-source scopes, true successful reads, unknown-record handling and GPT-only disclosure preserved. |
| feature | New effort/speed instruction added; mandatory writer/review separation and arena branch retained. |
| hillclimb | New effort/speed instruction added; existing measured loop/hypothesis isolation retained. |
| multi-phase-plan | Full vs Stack chosen by merge authority. New same-file trunk-change rebase trigger. Initial/major swarm, single later verifier, wording exception and source blocking rules retained in skeleton; merge/handoff wording replaces append. Ten initial live lanes, perf and review gates remain. Installed package paths and local resources retained. |
| opening-a-pr | Child follows merged parent to trunk via Shipping step 4; automatic interrogate removed from subagent opening gate as upstream removed it. Deslop/no-comments remain, and contested-design routing remains elsewhere. Merge-ready replaces STACK-READY. |
| orchestrate | Full new topology/supervision source retained. Coordinator never codes; one PR writer, complete brief, fresh tasks, max three levels, rolling about ten constrained by capacity, pilot end-to-end, fresh current-head verifier, inspect evidence and child briefs, scope discipline, live PR state, two retries by cause and replan. Native controls replace Task; private notes/store substitute explicitly declared because no universal native project-store operation exposed. Optional PR/CI subscription absence disclosed; no coordinator polling scripts or status-message relay. Local worktrees/GPT independence replace cloud/provider diversity. |
| perf-issue | New effort/speed instruction added through models; source measurement/reproduction gates retained. |
| refactoring | New effort/speed instruction added through models; source behavior pin/caller migration preserved. |
| runtime-forensics | New effort/speed instruction added through models; all artifact/evidence workflow retained. |
| session-pickup | New effort/speed instruction added; existing detailed scoped-history/recovery/authority/real-artifact checks preserved. |
| shipping | Complete six-step source retained. Independent local verifier with real parent/head operation; verdict post gated on host messaging authority. Contiguous run and independent transplant fresh-verdict rule. Exact base/head stable patch-id and docs/tests/lint build-noise exception; no build output reruns lane. Origin plain merge vs gh squash, merged-and-trunk readback, queued is not merged, auto only current verdict. Next owner retargets/rebases/pinned-lease pushes only after preceding merge. Frozen queued watcher with active bounded waits, no second poller, complete readback, stop ceiling. |
| trace-forensics | New effort/speed instruction added through models; artifact reduction/evidence retained. |
| worktree-cleanup | New effort/speed instruction added. Preserved audited Codex helper’s --trunk counterpart to upstream -b and all managed-worktree, history-scope and valuable-data holds; no raw Cursor cache deletion commands introduced. |

## Related adapter migration

`references/orchestration.md` now documents native capability discovery, explicit private notes/task-store fallback, no invented Project API, conditional PR/CI subscriptions, coordinator no-polling, per-owner branch ownership, fresh workers, current-head Orchestrate verdicts and restart reconciliation. Deleted custom orchestration CLI state/commands are no longer callable. `references/pr-delivery.md` retains the watcher bootstrap dependency/cache lifecycle formerly in orchestration.md; it preserves locked install, disabled lifecycle scripts, explicit setup, protected recipient cache, setup-lock recovery and no installed-plugin writes. `references/continuation.md` points to native/fallback records rather than old ledgers.

## Capability evidence and limits

Read actual exposed collaboration schemas on 2026-11-04: spawn accepts explicit model/reasoning effort and parent-history choice, no cloud environment or service-tier parameter; wait/list/results/message/interrupt exist. Model speed thus remains conditional, never an invented dispatch parameter. A forked conversation is not evidence of a forked filesystem/process. Actual available tool metadata showed project listing/organization, but no equivalent of upstream Project store or PR/CI event subscription. The private file substitution and subscription gap are explicitly described instead of claiming native equivalence.

Official documentation fetched 2026-11-04:
- https://learn.chatgpt.com/docs/glossary distinguishes subagents, Git worktrees and history-based thread forks. This is conceptual support, not recipient-specific schema proof.
- https://learn.chatgpt.com/docs/automations says desktop tasks using local files require the computer on and app running; standalone/chat schedules differ. No through-sleep or closed-app guarantee is claimed.

The direct guessed /docs/subagents fetch returned 404; it supplies no capability evidence. Runtime authority is the exposed schema, not guessed docs endpoints. No schedules, subscription registrations, external messages or PR mutations were performed in the playbook adaptation slice. No origin runtime compatibility was empirically exercised. Required forge/control/auth capabilities remain conditional and source-derived command spelling is subject to recipient preflight.

## Verification

- Read three-way differences for every changed source playbook; 18 changed source files accounted for above.
- `git diff --check` passes.
- Relative Markdown target scan across all playbooks plus the four owned references reports zero missing targets.
- Targeted executable-assumption scan finds no old orch helper paths, ORCH_STORE, frontier/ledger CLI calls, cloud dispatch flag, Grok default, Task tool, or operational /loop in owned active instructions.
- No helper code or package metadata changed. Integration validation and independent review remain parent-owned.

Principles read and applied: migrate-callers-then-delete-legacy-apis moved helper setup caller to PR delivery while eliminating old orchestration protocol; separate-before-serializing-shared-state preserved one writer per PR and private per-worker artifacts during replacement.
