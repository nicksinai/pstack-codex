---
name: pstack-recall
description: Reconstruct scoped recent working context from chat history, shared sources and live artifacts, returning a tight current-state brief before work resumes.
---

# Recall

Rebuild the user's working context, then hand back a tight capsule of where things stand and what to do next. Keep it on-topic. Read [history](../../references/history.md) before searching, and [delegation](../../references/delegation.md) plus [models](../../references/models.md) before dispatch. This workflow explicitly requests bounded local read-only history workers and source investigators when appropriate. Raw transcripts stay in workers; the main thread receives findings.

The user's chat trail holds what they did and decided. The shared record holds user reports, prior fixes, reversions and production incidents around the same code. Do not reconstruct a named feature solely from personal chats.

1. **Classify, then route.** A specific prior chat to resume uses [session pickup](../../references/session-pickup.md). Turning habits into a durable skill uses the automate-me workflow when installed; a human-readable activity summary is a different task. Recall loads working context across recent chats before action. If the user supplies a full capsule with paths, branch and change, use it and skip mining.
2. **Lock scope.** State the real date range and timezone, topic if named, and workspace before content reads. Recent defaults to the last seven days; all remains all. Default to the active workspace. Follow the shared history contract's metadata checks and exclusions before searching; never inspect unrelated projects' conversations.
3. **Mine chat history.** Enumerate eligible chats by actual modification time, not UUID. Search the topic first and read only matching chats and relevant regions. Exclude the current stored chat and child/subagent, eval and test noise through understood metadata. For one or two chats search directly; otherwise dispatch parallel disjoint slices, choosing a fast economical native model only if validated by the shared model contract, otherwise inheriting. Each returns one block per chat: topic, user's goal, decisions, open threads, struggles/corrections and artifacts (PRs, tickets, branches), each citing chat UUID and relevant item/line. Include fidelity and coverage gaps. Summaries cannot establish actual execution.
4. **Sweep the shared record for every named feature, file, subsystem, area or bug.** This includes “my work on X.” Read [why](../pstack-why/SKILL.md) and use its source investigators/playbooks, question changed to “what's the current state, what's been tried and didn't hold, and what are users still reporting?” Run this sweep concurrently with history mining within established capacity. Preserve seven-category coverage, one investigator per endpoint, null findings and unavailable-source gaps, source permissions and epistemic discipline. Skip only pure activity recall with no named target (“what did I do this week”), where own history and live state suffice. A supplied capsule skips transcript mining, not the named-target shared-source obligation.
5. **Check live artifacts.** Inspect surfaced PRs, branches, tickets and current diffs using the actual repository plus authenticated `gh` or supported forge readers. Preserve unavailable source gaps. When an answer hinges on what an agent did, read original execution items, including relevant tool calls/results and errors; a trimmed copy or summary is insufficient. Merged, deployed, verified and self-reported are separate claims.
6. **Write the brief.** Group by thread, stay on the named topic, and apply [unslop](../pstack-unslop/SKILL.md). Cite chat findings by UUID/item and shared findings by PR, ticket, chat permalink or error issue. Sanitize before public output. An adjacent feature stays out unless it blocks this one. If it outgrows a screen, cut detail before threads.

## Output contract

Lead with capsule, then threads, problems and next move. Deeper detail goes below or gets cut.

- **Capsule:** at most five bullets, stating what the work is and its current overall state.
- **Threads:** one line each, with exactly one status tag: `[merged #N]`, `[open PR #N]`, `[in flight <branch>]`, `[verified, uncommitted]`, `[reverted #N]`, or `[planned, not started]`. Every thread gets a tag supported by evidence. Use planned for confirmed plans, never to conceal unknown state; put unresolved status in the gaps/problems instead of inventing a tag verdict.
- **Problems:** at most five recurring problems, including user symptoms and shipped fixes that were reverted, so the next attempt starts where the last failed.
- **Next move:** the single most useful concrete next action.

Reply with the brief. Recall itself is read-only; continuing edits or delivery follows the user's separate authorized scope. If required history is unavailable, report the precise blocked access and partial evidence rather than pretending mining succeeded.
