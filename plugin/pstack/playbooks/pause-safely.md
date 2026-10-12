### Pause safely

Read [continuation](../references/continuation.md) for private durable checkpoints and actual worker/process state. Explicit pause stops execution; imminent compaction requires a checkpoint and continuation, not an unsolicited pause.

**You own a clean stop. Leave a checkpoint a cold-start agent can resume from.** This is explicit only. On "keep going", "going to bed, keep going", or "don't stop", do not pause.

1. Stop at a safe boundary. Finish the current atomic step or back out of it. Start nothing new, and cancel any nested subagents through supported host controls. Confirm their terminal state and owned processes independently; a cancelled chat does not establish process cleanup.
2. Take no irreversible action to pause. No PR and no push unless you already had one out.
3. Make the work durable. Commit uncommitted edits as one clear `wip:` commit on the current branch so nothing is lost. If the tree is broken, say so in the commit body in one line.
4. Write the resume note off-context. Capture intent, what you were doing, progress and what's verified, current state, next steps, key files, and gotchas. Write it in recipient-owned durable private task storage identified under continuation, outside the distributed plugin. A temporary file may supplement an imminent-compaction handoff but cannot be the sole restart record. Include invocation entry/exit state and the checkable task predicate. If writing a private checkpoint is unavailable, retain these in host task context and disclose that persistence across context loss is conditional. If a show-me-your-work trail exists, point at it instead of duplicating it.

**Reply:** where you are in the loop, what's on disk versus still in your head (paths, no diff dumps), the commits you made and whether the tree is clean, and the first action on resume. This is a pause, not a final report.
