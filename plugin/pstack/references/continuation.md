# Invocation, continuation and recovery

This is the shared contract for sticky mode, autonomous runs, program audits and interruption recovery. Read [delegation](delegation.md) for child lifecycle and resource ownership, [history](history.md) for scoped execution records, and [session pickup](session-pickup.md) for cold-start reconstruction. The package supplies instructions and deterministic helpers, not an always-running service or a native Cursor mode. Host instructions and the user's task limits govern every transition.

## Explicit invocation state

Keep one invocation record scoped to the current conversation ID and canonical workspace, never a repository-wide default. Record the user's actual entry/exit instruction and its turn locator. Use host task context immediately; also checkpoint in recipient-owned private task storage when available. Do not create or change global/repository AGENTS, hooks or settings to force activation. Installation makes workflows available; it does not activate them.

| Current state | User instruction/event | Next state and action |
| --- | --- | --- |
| Inactive | Explicit pstack invocation for a request | Single request. Read the main mode and route that request. Completion returns to inactive. |
| Inactive or single request | Explicit instruction to enter sticky pstack mode | Sticky active for this conversation/workspace. Record entry, read main mode and relevant leaf instructions, acknowledge scope. |
| Sticky active | Next task in the same conversation/workspace | Apply mode routing, required leaves and existing task limits. Casual turns need no engineering playbook. Carry record through handoff. |
| Sticky active | Explicit opt-out or exit | Inactive immediately. Record exit and stop applying mode to future work. Preserve work/evidence and report any independently running requested work. |
| Any | Explicit pause | Keep invocation scope but set task execution paused. Follow [pause safely](../playbooks/pause-safely.md); exit and pause are distinct. |
| Paused | Explicit resume/keep going | Reconstruct current artifacts and route pending authorized work. Preserve the recorded invocation state. |
| Any | Compaction, replacement or interrupted environment | Checkpoint if possible, then recover from the latest scoped record. No entry record means no assumed sticky activation. |
| Any | Different conversation or canonical workspace | Inactive unless the user explicitly carries activation into that scope. A supplied recovery brief may carry the user's recorded activation only for the same identified conversation/workspace. |

An exit is not an implicit cancellation of separately requested schedules or already authorized workers. Inspect and report their state; obey an explicit stop/cancel request using actual controls. A checkpoint is evidence of intent, not proof that the host automatically reloads it. When private storage is unavailable, retain entry/exit and task state in host context and state that restart persistence is conditional on that context remaining available or a supplied continuation capsule. Never claim a lost record survived. On recovery, the latest actual user exit/limit supersedes stale checkpoint text.

The record contains conversation/workspace identity, state (inactive/single-request/sticky), user entry and latest exit locators, task/run ID, execution state (active/paused/blocked/completed), predicate, authority limits, reviewed instruction identity and checkpoint location. A single request never silently becomes sticky. Invoking a specialized leaf skill does not itself request sticky mode.

## Durable task checkpoint

Choose a recipient-owned private task directory outside the plugin and record its actual location in chat/host task context. Reuse an existing task store where available; do not assume a universal environment variable or fixed home path. Keep private trails outside shared source by default. If a reviewer needs a committed decision trail, sanitize it before committing and preserve the user's disclosure limits. Do not store secrets in checkpoints.

Before an iteration yields, before a planned interruption and after each material transition, checkpoint:

- The goal and checkable exit predicate, task/run identity, invocation record and last user limits.
- Current branch/worktree locations, base SHA and head SHA, dirty work, commits, PR URLs, dependency ordering, done/pending checklist and first next action.
- Decisions and assumptions with pointers into the canonical [decision trail](../skills/pstack-show-me-your-work/SKILL.md); state what was attempted, retained and discarded.
- Exact verification identities and receipts. Record the head/patch/base each verdict covers, applicable patch-ID rules from the selected shipping playbook, open findings and invalidated evidence.
- Owners, actual child IDs, checkout/resource reservations, pending result receipts, processes/services and how to inspect them. Record unknown state explicitly.
- Current wait mechanism, event/cadence, actual requested schedule ID if any, last observed event identity, stop condition and cancellation owner.
- Capability gaps, unresolved product decisions, blockers and the continuation brief's paths/locators. A private transcript pointer is not material to publish.

Use one named checkpoint owner. Serialize replacement writes and keep the prior valid checkpoint until the new complete record is persisted. Workers own their own logs/artifacts and return pointers. Evidence files must actually resolve. A timestamp alone proves neither activity nor liveness. Do not copy a stale clean verdict into a new patch's passing state.

## Active waits and requested scheduling

For [autonomous runs](../playbooks/autonomous-run.md), define the predicate before the first iteration and choose an event/result wait or bounded timed waits exposed by the host. Checkpoint before yielding. Choose cadence according to meaningful expected changes, use bounded waits so user steering remains responsive, and log each iteration. An in-session watcher and its fallback timer stop being reliable when the session or computer stops running.

Only create scheduled follow-ups when the user explicitly asks for recurring work, monitoring, checking back or a later wakeup and the host exposes a supported scheduler. Discover its current schema and bind an actual create/update/read/cancel operation. Record the returned ID and observed scheduling state; do not claim creation from a proposed prompt or a failed call. Reuse a matching existing schedule rather than duplicating after interruption. Preserve notification intent and task limits. A request to keep working now alone does not authorize a new recurring schedule.

A schedule's replay prompt names the conversation/workspace, checkpoint, predicate, reviewed instructions, authority limits, recovery-first behavior, cadence and stop condition. Do not copy credentials, unrelated history or personal account configuration into the package. Use a same-conversation follow-up where supported; if only standalone jobs are available, disclose the handoff difference and preserve the explicit user scope. Missing required scheduler operations block durable follow-up claims, though authorized active-session work can proceed. Stop or update a schedule when its authorized stopping condition is reached through the supported host operation; preserve receipts rather than assuming a final chat reply cancels it.

Official [scheduled tasks documentation](https://learn.chatgpt.com/docs/automations) describes chat schedules and local desktop execution requiring an available app/computer/project. Exact account capabilities are conditional. This contract promises no progress through app closure, sleep, offline services or lost workers, and no cloud-worker service.

## Recover from artifacts

Start with [session pickup](session-pickup.md). Verify the checkpoint's conversation/workspace scope and latest user instructions before following it. Inspect current Git status/diffs, branches and SHAs, PR/check state, task records, evidence files, service/process health and actual child-control results. Do not replay a merge, push, schedule creation or other mutation solely because the previous record ended before its receipt; first inspect whether it already happened. Reconcile state and log the recovery decision.

A recorded child ID is not proof that it survives restart. Confirm current terminal/liveness state using actual controls and inspect its worktree and owned processes. For dead or unknown workers, preserve artifacts, cancel/contain any surviving owned processes safely, and dispatch a fresh worker with consolidated scope and the verified resume point. Never delete a worktree to stop a worker. Escalate missing control capabilities rather than falsely claiming cancellation.

Compare inherited verdicts with current artifact identity. Invalidate results for changed patches unless the selected shipping playbook's explicit patch-ID rule applies. Repeat only affected checks, retain valid evidence and never redo completed work merely to rebuild confidence. If the checkpoint or history is unavailable, state what is established by current artifacts, what is unknown and which exact scoped record is needed. Missing activation evidence defaults to inactive; missing execution evidence never defaults to passing.

## Integration directions

The main pstack mode must read this contract on entry, exit, unattended routing and recovery. Its autonomous/pause/multi-phase routes read the matching playbook here; its long-run trigger reads pstack-show-me-your-work. Program/orchestration ledgers add their domain state to this shared checkpoint and use this scheduling contract instead of introducing another mode state or loop API. Preserve the selected workflow's existing engineering gates and merge/deployment authority. Planning alone never starts execution.

Official [Codex skills](https://developers.openai.com/codex/skills) establishes explicit invocation and `allow_implicit_invocation:false`, not native sticky-mode persistence. The state transitions above are established instruction structure; future instruction compliance, reload after context loss, recipient history/delegation/scheduling availability and observed execution remain conditional. Report those limits as such.
