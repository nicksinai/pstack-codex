---
name: pstack-ketchup
description: Catch up on this conversation with checked states, real visuals, and pending user decisions.
---

# Ketchup

Read the [compatibility contract](../../references/compatibility.md) and [catch-up capability binding](../../references/ketchup-capabilities.md) before gathering evidence. This explicit invocation produces a catch-up reply, then stops; it does not resume the underlying task.

Catch the user up since the last message they wrote before this invocation. Notifications, tool messages and delegate results do not move that boundary. Assume the user remembers their message and nothing after it. Use the plain voice of [bro](../pstack-bro/SKILL.md), skipping its restating step. Call each PR, branch and agent by a recognizable name, rather than an invented internal label.

## Gather

Keep the turn read-only, except for reply visuals made from available facts. Do not change code, start apps or jobs, post externally, or continue task work to improve the report. Stay within this conversation and artifacts it touched. Collect your work, delegate reports and other messages since the boundary; include earlier unresolved user actions. Check the current state of every touched PR, CI run and agent with an available read operation. Verify every displayed number against its underlying facts, and disclose corrections. Mark unavailable state “unknown” or “not checked,” never inferred success.

An action item is a decision or step only the user can take: a product choice, approval, irreversible action or missing access. Agent-owned work is not a user action item.

## Reply

Keep text under 250 words, including Markdown tables; visuals do not count. Each visual replaces the facts it shows: avoid repeating them in text. Omit work that changed nothing for the user.

Open with one sentence giving the action-item count, or saying there are none. If nothing happened and nothing waits on the user, say so and stop.

Show progress in one visual containing each touched PR, run and agent with its state: done, running, failed or not checked. Give at most three one-line results that change what the user knows or must do. Keep a key number in its result line unless already visualized. Name remaining agent-owned work in one line.

For each user action, give three lines: the decision; your recommendation and reason; the consequence of no answer. Write “unknown” for anything unknown and link existing detail. Show before/after side by side in a visual; for choices show the current state beside each option, or options alone when there is no current state. Put options and costs in the visual rather than repeating them in text. Only access requests may omit their action visual.

## Real visuals

Use real screenshots or video for visible changes. When none exists, mark that change “No screenshot yet” in the progress visual. Never draw or generate an uncaptured screen. For other changes use fact-grounded Mermaid state/flow/structure diagrams or charts of verified numbers through an available visualization capability. Screenshots, video, diagrams and charts qualify; Markdown tables do not. Link only existing artifacts. Missing required history or visualization capabilities remain explicit limitations or blockers under the capability binding; text or tables do not silently substitute for a required visual.
