---
name: pstack-poteto-help
description: Explain PStack setup, workflows, and recovery without starting a run.
---

# Poteto help

Answer the question, give at most one usable prompt, and link the file you actually read. A help question does not start a token-consuming run. A message asking for work, such as “use pstack to fix this bug,” routes to [mode](../pstack-poteto-mode/SKILL.md) and executes within the user's scope. Mention explicit sticky entry once when relevant.

The [mode lookup](../pstack-poteto-mode/SKILL.md#bundled-skill-lookup) holds the namespaced path for every included upstream skill, even when the discovery menu omits entries. Read the target before recommending or quoting it. Link the actual installed local file or a verified adapted repository revision. Do not present the upstream main branch as the installed Codex instructions. Source provenance is pinned in the package qualification records.

## Find out what they need

Infer the need from the message and conversation. A specific situation goes directly to its answer. If unclear, ask one multiple-choice question, then answer only that branch:

- Get set up.
- Start a task with `$pstack-poteto-mode`.
- Pick a skill for a situation.
- Fix a run that went wrong.
- Make pstack my own.

Check state only when it changes the answer. Read [models](../../references/models.md) for the recipient's configured role file; its absence means inherited validated host defaults, not missing Cursor configuration. If the project has no verify-* skill or app harness, explain that scripted real-artifact verification is missing and route creation through the mode lookup.

If setup/model cost matters, ask at most once per chat whether they want setup now or later. Combine this with an unclear-need question. “Now” gives `$pstack-setup-pstack` and still answers the question; “Later” explains that missing roles inherit the parent until configured. Setup is explicit and never loads merely from installation or inferred preferences.

## Get set up

1. Follow the package [setup/removal instructions](../../README.md); use only a supported recipient install mechanism.
2. Read [setup-pstack](../pstack-setup-pstack/SKILL.md). Choose reasoning budget and available native GPT role identities in recipient-owned settings. It changes no global rules and roles are read at entry and dispatch.
3. Start with `$pstack-poteto-mode`, a goal, and a check that can pass or fail.

Installation makes workflows available without running them. Offer to word the first prompt using [prompting](references/prompting.md). Extra tokens go to workers and review panels. Reduce budget, use cheaper validated models or inherited aliases, or shorten configured panel lists (one worker per entry) when the workflow allows; never silently drop required independent review. Budget labels are reasoning preferences rather than dollar caps. Reserve mode rigor for tasks that need it.

This port targets Codex desktop, native GPT models and isolated local workers. It loses upstream Claude/Grok provider diversity and cloud machines. Actual tool access, model overrides, live control and continued execution depend on the recipient environment. No progress through app closure or sleep is promised. Grok Bot UI and Benny are excluded.

## Start a task

The mode chooses the playbook and copies its adapted steps verbatim into the todo/checklist before task-specific items. A genuinely inapplicable step stays with `skip: <reason>`; mandatory evidence gates retain their explicit exceptions. State the goal and done check instead of supplying an accidental reordered list of skills. Read [prompting](references/prompting.md).

A normal `$pstack-poteto-mode <request>` is one request. Explicitly say “enter sticky PStack mode for this conversation” to keep it active within the same conversation/workspace, and “exit PStack mode” to leave. Read [continuation](../../references/continuation.md) for scope, pause, exit and recovery; no native Cursor keyboard shortcut or automatic context persistence is claimed. Casual turns need no engineering playbook. “New task” selects a fresh route. Playbook workers receive [poteto-agent initialization](../../references/poteto-agent.md); specialized routed skills keep their own prompts.

## Pick a skill

Default to mode for a nontrivial engineering request; recommend a leaf when the user wants its narrower output. Resolve every name below through the authoritative mode lookup and read it before giving an example.

| User need | Upstream skill name (invoke as `$pstack-<name>`) |
| --- | --- |
| Check the agent understood your goals and problem before work begins | in-your-own-words |
| Current mechanics and where code belongs | how |
| Reasons, regression history or a number's origin | why |
| Plain explanation and tradeoffs | teach |
| Recent scoped working context | recall |
| Checked catch-up on this conversation and pending decisions | ketchup |
| Breakage outside the diff and a proven safety fact | blast-radius |
| Parallel design before crossing a function boundary | architect |
| Competing attempts with base selection and grafting | arena |
| Partitioned coverage, races or gauntlets using local workers | swarm |
| Independent adversarial GPT review | interrogate |
| Cheap failing-first bug regression | tdd |
| TypeScript rules for .ts/.tsx | typescript-best-practices |
| Fresh reviewer comment cleanup | no-comments |
| Clean prose | unslop |
| Docs, RFCs, README, PR descriptions and commits | technical-writing |
| Restate the last reply plainly | bro |
| Build or maintain project verification and feature map | create-verification-skill / maintain-verification-skill |
| Qualify measured performance numbers | benchmark-checklist |
| Bespoke rigorous large or cross-cutting run | figure-it-out |
| Auditable decision log and later review | show-me-your-work |
| Native roles and reasoning budget | setup-pstack |
| Guided personal mode draft | automate-me |
| Approved post-task skill learning | reflect |
| Enforceable fixes for recurring mistakes | correct |
| Help without starting work | poteto-help |

A new sibling not in this table is discoverable by its frontmatter. Principles live in the mode index; read their leaves before applying/citing them. They also support explicit `$pstack-principle-<name>` entry.

Close calls preserve upstream distinctions. How explains mechanics; why explains reasons; teach explains their result. Arena gives the same brief to competing workers; swarm partitions or races. Architect implements after design unless the user asks for a checkpoint. Interrogate reviews the diff; blast-radius proves safety beyond it. Ketchup reports this conversation since the last user message, retaining earlier pending user actions, without resuming work. Recall spans scoped recent work; [session pickup](../../references/session-pickup.md) resumes a specific run. Figure-it-out designs one bespoke run; Orchestrate manages a standing program; Autonomous run drives one task to a predicate.

## Playbooks

Playbooks are mode routes, without independent slash commands. Describe the task or name the route. “Check on PR X” runs Babysit in its prescribed status mode; “babysit this PR” drives to merge-ready. Neither merges without a merge/land/ship instruction. “Land the stack” runs Shipping with independent verification. “Take over this branch” runs session pickup. “Pause safely” preserves resumable state. “Full autopilot on this queue” requests the independent-PR mode; “stack them, don't ship” retains operator landing. “Run the eval playbook” requests blinded evaluation.

The mode lists all routes. Multi-phase planning produces a plan and does not authorize implementation. Prototype or architect settles design from evidence. [PR delivery](../../references/pr-delivery.md) distinguishes opening, babysitting and shipping. Bundled deslop and control adapters replace cursor-team-kit runtime dependencies; continuation replaces `/loop`, and the authoring playbook replaces the unavailable Cursor built-in authoring instructions. There is no independent bundled orchestrate skill.

## Fix a run that went wrong

| Symptom | Response |
| --- | --- |
| Mode faded | Verify explicit sticky entry; recover the scoped record or invoke one request again. |
| A question continued the prior task | Say “new task” or opt out for that turn. |
| Model change had no effect | Inspect recipient role path and actual dispatch/model validation, not an assumed global rule. |
| Cost grew | Revisit budget, validated model choices and allowed panel size. |
| Skill absent from menu | Use the mode's direct bundled path lookup; installation does not activate skills. |
| Workers overwrote work | Distinct worktrees/branches and explicit locations/resources are required. |
| Overnight work never finished | Supply a falsifiable predicate and decision log; active waits require the running app/computer. |
| A green build was called success | Ask for real flow/output/stored value/profile against the intended artifact. |

Read [prompting](references/prompting.md) for steers and [recipes](references/recipes.md) for examples. Never claim a missing control, history, scheduler or worker succeeded.

## Make it personal

Automate-me drafts from scoped authorized history and feedback. Reflect proposes Accepted/Rejected/Backlog changes and waits for approval before accepted edits. Authoring and eval routes support new skills and blind qualification. A broken skill gets its own PR without silently bypassing it or blocking independent task work. Follow the host's authority for durable edits and external tracker writes; installation alone grants none.

## Reply

Lead with the answer, give at most one adapted prompt from recipes, then the actual file link. Stay short unless the user asks for the whole map.
