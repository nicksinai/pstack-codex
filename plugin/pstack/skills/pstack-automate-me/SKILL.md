---
name: pstack-automate-me
description: Draft or update a personal working-style mode when explicitly asked to automate me.
---

# Automate me

A guided flow for turning the user's working conventions into a skill agents will follow. The output is one `-mode` skill tailored to them (e.g. `jay-mode`, `priya-mode`).

This skill orchestrates three others: an inline mining pass (see step 1), the bundled [authoring companion](../../references/skill-authoring.md) and an available Codex skill-creator (authoring), and the **unslop** skill (prose discipline). It sequences them. It doesn't replace them.

## Flow

### 0. Check for an existing skill

Read [history](../../references/history.md), [delegation](../../references/delegation.md), [models](../../references/models.md) and [authoring companion](../../references/skill-authoring.md). Check the active repository's discoverable skill roots and verified recipient-owned skill roots for a `*-mode/SKILL.md` matching the chosen handle, including personal category subdirectories. Inspect host configuration/catalog to establish those roots; do not recursively scan unrelated home directories or overwrite a namesake in another plugin. A normal repository root is `.agents/skills`; recipient global location follows actual CODEX_HOME configuration. Preserve the existing path/category and invocation policy.

If one exists, confirm update versus start-fresh intent unless the user already requested update. Default to updating. Ask why before replacing a skill. Use the host's actual question tool if suitable; otherwise present the choices in chat. Tool absence is not permission to choose a destructive replacement.

Update mode changes the rest of the flow:
- Step 1 mines only history since the skill was last edited (`git log -1 --format=%cI <path>`).
- Step 2 asks what's changed or missing, not what to capture from zero.
- Step 4 edits the existing file in place. Preserve sections the user hasn't contradicted. Revise ones with new evidence. Add new sections only for genuinely new rules.

### 1. Mine their history

Establish canonical workspace, timezone, window and eligible transcript identities through the history contract before body reads. Use only metadata-confirmed active-workspace conversations; ask before expanding. For this mining pass exclude the current chat's stored duplicate and child/eval/test records; use the supplied current conversation separately as direct user input. If history is unavailable, disclose the gap and obtain an explicitly narrower user-input draft scope rather than claim mining occurred. Update mode starts strictly after the skill's verified last edit time; use Git history where available, and disclose uncertain mtime/provenance instead of inventing the cutoff.

Survey recent agent conversations within that scope for recurring patterns. Use fresh native GPT mining delegates through the delegation contract, with disjoint metadata-filtered slices of history and bounded capacity (e.g. last 2-4 weeks, split into 3 slices so each has enough material). Each slice mining subagent reads transcripts from the workspace-scoped path the parent provides, looks for the signals below, and returns a short structured list of patterns it saw with evidence pointers. Default signals worth hunting:

- Response preferences (length, tone, format, "dumb it down" corrections)
- Delegation habits (subagents, models, specialized workflows, parallelism)
- Verification posture (what "done" means, unit tests vs live repro, reviewers)
- Code and prose discipline (style, principles cited, lint/format tools)
- Process conventions (worktrees, commits, PRs, review/merge tooling)
- Meta preferences (fixing skills mid-task, proposing new ones)

Cross-check across slices before elevating a signal. Patterns seen in 2+ slices are high-confidence. Lone signals are weak and usually get dropped.

### 2. Ask the user directly

Mining misses intent that hasn't come up yet. Use the actual host question schema when it supports structured choices. Otherwise show compact numbered choices in chat. Gather real answers; elapsed time is not consent or preference evidence.

Shape: one or two questions with 4–6 options each when the host supports that size and multiple selection; otherwise split into schema-valid compact rounds and let the user select multiple categories in chat. Start broad ("Which areas matter most?"), then follow up on selected areas with specific options. After the structured rounds, one free-form chat question catches anything the options missed.

Don't dump 20 questions.

### 3. Cluster findings

Group the combined signals into sections. Common ones (use only what applies):

- **Response style**: length, tone, format.
- **Autonomy**: how much to do without asking, MCP tool use.
- **Understand first**: which skills to reach for when scoping or investigating a change.
- **Subagents**: default, parallelism, model-to-task, specialized workflows.
- **Prose / code discipline**: principles, lint tools, style guides.
- **Review and verify**: repro posture, verification skills, live-testing tools.
- **Process**: git worktrees, commits, PRs, review/merge tooling.
- **Skills**: skill-authoring habits, fix-the-skill-first, proposing new skills.

The bundled core mode at `../pstack-poteto-mode/SKILL.md` shows the shape. Read it for granularity when present; its availability is a staged core-mode dependency, not permission to copy another user’s preferences. Don't copy its content. The user's rules are not the same as poteto-mode's.

### 4. Draft the skill

Use the [authoring companion](../../references/skill-authoring.md), reading the recipient's actual Codex skill-creator when available. Placement:

- Preserve an existing mode skill's path and personal category. For new repository modes use `.agents/skills/<handle>-mode/SKILL.md`, retaining an established discoverable personal category where the recipient supports it. A global skill requires the user's chosen recipient-owned skill root; do not infer global installation authority from a drafting request.
- Handle: the user's first name or chosen identifier.
- Description: trigger on their name, `/<handle>-mode` and “work in their style”; avoid generic “write code” or “review PR” triggers. Use one YAML scalar, quoted or folded when punctuation/wrapping needs it.
- New modes default to explicit-only `agents/openai.yaml` with `policy.allow_implicit_invocation: false`. Preserve an existing policy. If the user wants continuing application, agree the explicit sticky scope and exit using [continuation](../../references/continuation.md); change invocation policy only on their explicit request. Do not emit Cursor `disable-model-invocation` or `mode` metadata as a Codex compatibility claim.
- Draft in a reviewable recipient-owned checkout/output location. Do not package mined transcripts, credentials, account configuration or this user's rules into the shared pstack plugin. Referenced personal skills must resolve for that recipient; external paths are documented recipient dependencies, never shared private absolute paths.

### 5. Iterate on prose

Read [unslop](../pstack-unslop/SKILL.md) and apply it plus the authoring companion’s writing guidelines to every line.

Show the draft to the user and take feedback. Expect multiple iterations. Cut ruthlessly. A mode skill is not a manual.

### 6. Land it

For a repository-managed skill, work in an isolated worktree off the repository’s main branch, commit and open a PR through [PR delivery](../../references/pr-delivery.md). Respect existing local-only/draft-only limits. A personal skill without a repository gets a reviewable local draft/diff and an explicit apply location; do not invent a PR repository or install globally. Report that delivery difference. Never overwrite existing preferences merely to land the draft.

## Guardrails

- **Don't overfit to one conversation.** A preference stated once and contradicted another time is noise. Require multiple instances before codifying it.
- **Don't be clever.** Restating other skills' contents, inventing metaphors, or writing "poetic" prose for an agent reader is cost without benefit. Keep it operational.
- **Reference, don't inline.** Other skills the user relies on should appear as path references, not pasted excerpts. Same for any principle docs they maintain elsewhere.
- **Keep sections minimal.** Only add a section if the user has a specific, non-default rule there. "Communicate clearly" is not a section. "Short paragraphs. Tables when comparing options. Bullets only when items are genuinely parallel." is.
- **Name conventions generic.** Use "the user" or "the human" in imperatives, not the author's first name.
- **Don't force symmetry.** If a user has no process rules worth writing down, skip the Process section entirely.

## Evaluation

A `-mode` skill is subjective output. A behavioral test/iterate benchmark loop is not useful for subjective preference matching; direct structural/frontmatter/path validation still applies. Vibe-check with the user: does it read like them? Did it miss anything? Then ship.

Run a description-optimization loop only if the skill's trigger accuracy turns out to be a problem in practice.

## When not to use

- User wants a task-specific skill (not working conventions): the authoring companion alone, no mining required.
- User wants to capture one narrow workflow (e.g. "how I write commit messages"). That's a regular skill, not a mode skill.

