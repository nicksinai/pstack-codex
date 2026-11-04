---
name: pstack-reflect
description: "Spawn three parallel review subagents over the active transcript, surface learnings, and route each to a concrete edit on an existing skill."
---

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits. Enter only when the user explicitly asks for reflect or /reflect. Skip trivial, off-topic, one-off sessions and lessons already covered by a skill the parent followed correctly.

Pick each subagent's reasoning level and fast or standard speed for the job through the [mode's Subagents contract](../pstack-poteto-mode/SKILL.md#subagents) and [native model binding](../../references/models.md). Use only controls exposed and permitted by the actual host; record inherited or unavailable controls rather than claiming they were set.

## 1. Locate the active transcript

Read [history](../../references/history.md) and the [review context adapter](references/context.md). Identify this chat from host metadata and the opening user prompt; read its actual execution items when available. Bind an exposed reader or a metadata-verified export in the active workspace. Never search unrelated workspaces. Current chat is deliberately the corpus for reflect; recall's duplicate exclusion applies to separate history mining. If no exact transcript resolves, write a tight session digest, identify its limits and pass that instead. Do not represent summary/digest assertions as original execution evidence.

## 2. Spawn three independent reviewers

Read [delegation](../../references/delegation.md) and [models](../../references/models.md). Dispatch three fresh native GPT reviewers in parallel within verified capacity; queue bounded batches if necessary, retain all three independent lenses. Missing spawn/result capability blocks the panel rather than replacing it with invented self-reviews. Read-only instructions preserve lookup access when available; a Cursor readonly flag is not portable and does not establish sandbox enforcement.

| Lens | Role | Complete prompt |
| --- | --- | --- |
| Judgment | `reflect judgment, divergent, synthesizer` | [judgment](references/judgment-reviewer.md) |
| Tooling | `reflect tooling` | [tooling](references/tooling-reviewer.md) |
| Divergent | `reflect judgment, divergent, synthesizer` | [divergent](references/divergent-reviewer.md) |

Resolve validated model and effort separately. Inheritance is the portable default; native GPT independence lacks upstream Claude/Grok provider diversity. Pass each template's complete body with the verified transcript path or digest substituted. Collect the full outputs, including missing evidence and failed lookups.

## 3. Synthesize

Spawn a fresh synthesizer using `reflect judgment, divergent, synthesizer`, the complete [synthesizer](references/synthesizer.md) prompt and all three full outputs. It may read referenced context to spot-verify citations; it makes no edits. Require its exact Accepted / Rejected / Backlog output and all criteria, including target-skill reads, skill-was-used, existing-skill-first, already-covered and structural-mechanism checks.

## 4. Structural enforcement check

Sanity-check every Accepted row. Move any rule more reliably enforced by a lint rule, script, metadata flag or runtime check into Backlog. Read the bundled [encode-lessons-in-structure principle](../pstack-principle-encode-lessons-in-structure/SKILL.md). Prose is for judgment that structure cannot enforce cheaply.

## 5. Apply approved rows

Present the full Accepted / Rejected / Backlog output before any Accepted edit. Wait for explicit approval; the user chooses a subset and may redirect routings. Reflection invocation itself authorizes proposals, not durable skill edits. Before approval, show the exact recipient-owned destination for each edit. Never edit a skill under `plugins/cache/`. For a cached skill, propose a project-local `.agents/skills/<skill>/` copy or a verified recipient-owned user skill root, preserving the folder and invocation policy. After approval, copy the complete folder there and edit the copy. Check for an existing destination before copying and preserve unrelated content. Never open a PR or push from this workflow.

File Backlog automatically to the configured team devex/backlog tracker when the current host and user authority permit it; only Accepted edits have the reflection approval gate. Resolve the tracker/repository from actual team configuration and existing issue conventions, check duplicates, sanitize private evidence, and record the resulting issue. If no tracker is configured or filing is unauthorized/unavailable, retain a concrete unfiled draft with the exact blocker; never invent a destination or report it filed. A skill cannot override a host's message/write restriction.

For each approved Accepted row, follow Routing exactly:

- Trivial existing-skill edit (one-line bullet, tightened sentence, stale fact): parent edits directly.
- Substantive existing-skill edit (new section/pattern table or more than about ten lines): use [authoring companion](../../references/skill-authoring.md), including draft / appropriate validation / iterate.
- `tune description: <skill path>`: use that companion's description-optimization loop; preserve existing invocation policy.
- `new skill via create-skill: <kebab-name>`: use the same companion to create the approved skill; do not invent its shape ad hoc.

Preserve unrelated existing content and configuration. Never publish personal lessons in this distributable. Run the available SKILL.md validator on every touched skill; if unavailable, perform direct frontmatter/path checks and disclose the validator limitation. This workflow delivers local edits only; its no-PR/no-push rule also applies when the authoring companion normally routes repository edits to PR delivery.

## 6. Reply

Short list, no preamble:

- Edits applied: skill path and one-line change.
- New skills created: skill path and one line (rare).
- Backlog filed: issue title, tags and link; separately identify unfiled drafts and blockers.
- Dropped: each rejected finding and its synthesizer reason.

Report proposed, approved, applied and delivered states accurately; user approval is never inferred from a timeout.
