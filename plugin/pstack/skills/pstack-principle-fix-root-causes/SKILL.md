---
name: pstack-principle-fix-root-causes
description: Apply fix root causes when PStack selects this principle.
---


Resolve named skills through the [mode lookup](../pstack-poteto-mode/SKILL.md). The [compatibility contract](../../references/compatibility.md) and current user/host authority govern any delegated, durable or external action.

# Fix Root Causes

When debugging, do not fix symptoms. Trace every problem to its root cause and fix it there.

**Why:** Symptom fixes accumulate. Each workaround makes the system harder to reason about, and the real bug remains. Root-cause fixes are slower upfront but reduce total debugging time.

**Pattern:**
- Reproduce first
- Ask "why" until you hit the root cause
- Do not add guards (adding a nil check to silence a crash is a symptom fix)
- If a workaround needs a paragraph-long comment to justify it, the code is wrong (fix the code, not the comment)
- Check for the pattern, not just the instance (grep for the same pattern, fix all instances)
- When stuck, instrument. Don't guess (add logging, read the actual error)
- If the deciding fact took a deep dig to find, propose a cheap ongoing signal that would have exposed it at first look. Name the fact, where to observe it and the expected cost. Keep the signal a proposal; installation of monitoring, recurring work and external messages requires applicable user/host authorization.

**Restart bugs: suspect state before code**

When something "fails after restart," suspect stale persistent state first: config files, caches, lock files, serialized state. If clearing a state file restores behavior, prioritize state validation as the fix.
