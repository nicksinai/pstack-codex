### Autonomous run

Read [continuation](../references/continuation.md) before the run. It owns persistence, scheduling, authority and recovery. Read [decision trail](../skills/pstack-show-me-your-work/SKILL.md) for logging and its independent audit gate.

**You own the exit condition. Define done, then drive to it without stopping.**

1. State the exit condition as a checkable predicate before the first iteration (tests green, repro fixed, all N PRs merged, pixel-diff zero).
2. Bind the actual wake mechanism under continuation. An event to watch (CI, a merge, a ref advancing) gets a local watcher delegate under [delegation](../references/delegation.md), using an exposed event/result wait with a long time-based fallback while the session remains active. No event gets bounded fixed-interval waits sized to when the result is worth re-checking. Active waits are not durable schedules. Create a recurring follow-up only on an explicit scheduling/watch/check-back request and an available supported host scheduler. Record its actual ID, next check and stopping condition. If the requested unattended mechanism is unavailable, report that exact capability gap; never invent a Cursor loop or promise wakeups after shutdown.
3. Each iteration makes the smallest change the evidence justifies, verifies it against the predicate, commits if it advanced, discards changes that didn't help. Belt-and-suspenders that "might help" gets reverted, not left to ride.
   Sequence the work via the **sequence-verifiable-units** principle skill, verifying each unit before the next instead of batching checks at the end.
4. Mid-run discoveries are yours. Address broken skills, related bugs, flaky verifiers, review noise, tooling failures, orphaned follow-ups, and fixable drift yourself via poteto-mode. Put out-of-band fixes in their own PR. Do not park reversible work for the human or ask for confirmation on already authorized reversible work. Respect existing user limits and host authority. Surface irreversible actions, genuine product or preference calls no experiment can settle, or a real dead end. External messages require explicit human authorization. The broad upstream autonomy wording cannot supply that authorization. Keep the predicate as the main drive, and return to it after each side fix.
5. Checkpoint every iteration via the **show-me-your-work** skill, a row for what changed and whether the predicate moved.
6. Stop when the predicate is met. A plateau is not a stop, so keep going and pivot your approach to push past it. Surface a genuine dead end rather than spinning, and never relax the predicate to declare victory.

**Reply:** the exit condition, iterations run, what landed, what was discarded, final predicate state.
