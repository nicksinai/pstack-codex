### Authoring or modifying a skill

**You own the skill's voice.**

1. Read the [skill-authoring companion](../references/skill-authoring.md), then the recipient's available Codex skill-creator. The exact Cursor built-in source is unavailable; the companion states that fidelity limit and carries the known authoring requirements.
2. Validate the skill: required name/description frontmatter, valid scalar YAML, referenced files and cross-skill targets resolve. Run a shipped validator when usable and disclose its absence otherwise.
3. Check meaningful cases if structural, as the user's verification standard requires. Skip behavioral benchmarks if subjective; iterate with the human on the draft. Structural checks remain.
4. Run [Opening a PR](opening-a-pr.md) through [PR delivery](../references/pr-delivery.md), respecting the authorized target and delivery limits.

When in doubt, delete. Keep only prose that changes a decision. Tell it to do the thing and skip the reason. Explain only when the rule is confusing without one. Match tone to scope. Point at structural sources (types, READMEs, config) rather than restating them. Delegate to other skills by resolvable path. A workflow you keep hitting but isn't captured → propose a new skill. Read the bundled encode-lessons-in-structure principle through core mode's principle index when available; its mechanism-first rule is preserved in the companion and reflection check.

**Reply:** summary of the skill, key design decisions, validation notes and any incomplete delivery step.
