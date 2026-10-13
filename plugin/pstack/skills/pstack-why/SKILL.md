---
name: pstack-why
description: Investigate design rationale, regressions, postmortems and data-backed thresholds across available historical sources, with cited confidence distinctions.
---

# Why

Investigate the motivation and intent behind code. The companion `how` skill answers what the code does and how it works. `why` answers what forces led to its shape.

Read [compatibility](../../references/compatibility.md), [delegation](../../references/delegation.md), [models](../../references/models.md), and [source access](references/source-access.md). This workflow explicitly requests bounded local read-only investigators and a fresh synthesizer. Resolve the `why investigators` and `why synthesizer` roles through the shared contract. All workers retain their specialized prompts, not the full mode wrapper. GPT-only investigation replaces upstream provider choices; independent workers do not supply provider diversity.

## Operating Posture

Operate as a **careful, cautious, and precise investigator**. Be honest about what you know vs what you're inferring. Read [references/epistemics.md](references/epistemics.md) for the full confidence framework and phrasing guide. The synthesizer must follow it.

## Step 1. Understand the Target and the Question

The **target** is usually a chunk of code, a pattern, a feature, or a named design decision. The **question** is usually a design rationale, a tradeoff, a motivating edge case, an external constraint, dead code, or a broad history sweep.

If the target is vague ("why do we do it this way?" with no clear referent), make your best guess from conversation context (open files, recent edits, cursor location, what was just discussed). State your interpretation briefly so the user can redirect if you're off, then proceed.

## Step 2. Establish the Code Anchor

Before spawning investigators, build the seed context inline: file paths and line ranges, key symbols (functions, classes, constants), the last few commits touching the target, PR numbers from merge commits (pattern `(#1234)` in the subject line), and any linked ticket IDs. Run `git blame -L <start>,<end> <file>` for last-touch commits, `git log --follow -p -- <file>` for full history with patches through renames, `git log --oneline -20 -- <file>` for recent commits with PR numbers visible, and `git log -1 --format=%B <commit>` to extract PR numbers. Then pull the PR bodies and discussion for any substantive commit: `gh pr view <number> --json title,body,author,createdAt,mergedAt,labels,closingIssuesReferences,comments,reviews`. This anchor goes to every investigator and to the synthesizer.

## Step 3. Spawn Parallel Investigators

**Default to the full parallel investigation.** The goal is a complete coverage map, not a minimal one. Document the null, don't skip the search.

### Discovery

Before spawning, discover the recipient’s exposed connector/tool catalog using its supported discovery operation. Inspect server instructions and actual schemas, including pagination and access scope. Do not inspect a Cursor `mcps/` directory or assume this package supplies connectors. Classify authenticated read access separately from names merely listed. Follow [source access](references/source-access.md).

Map each available MCP to one evidence category:

1. Source control history
2. Issue / ticket tracker
3. Long-form documents
4. Real-time team chat
5. Infrastructure observability
6. Error / exception tracking
7. Product analytics warehouse

Source control requires the repository and local Git; forge discussion additionally requires authenticated `gh` or a supported forge reader. Always assign the source-control investigator when its local repository is accessible; record missing Git/forge access as a gap rather than assuming success. For the other six, classify using the MCP name, server instructions, tool names, and resource descriptors. If an MCP could fit more than one category, choose the one matching its primary evidence. Record ambiguous cases in the coverage map.

Dispatch matching investigators as one parallel batch within the shared concurrency allocation. Queue excess workers. Each worker owns one source endpoint; when several endpoints match a category, dispatch separate workers and account for each under that category. Do not ask one worker to cover multiple connectors.

Worker configuration: native local child, role `why investigators`, exact read-only task scope, authenticated connector access where available. A read-only instruction is not a sandbox guarantee. Do not select a host execution mode that removes the required connector; inspect actual capabilities rather than copying Cursor's `readonly:false` convention. No worker may write files or mutate external sources.

Each investigator gets:
1. The base prompt from [references/investigator-prompt.md](references/investigator-prompt.md)
2. The category playbook `references/sources/<source>.md` for the selected MCP, adapted from the examples in [references/source-playbook.md](references/source-playbook.md)
3. The cross-cutting [references/sources/incident-postmortem.md](references/sources/incident-postmortem.md) **if the target code looks defensive** (null checks, retry logic, timeout handling, rate limiting, feature flags, egress guards, OOM handlers)
4. The code anchor from Step 2 (file paths, symbols, commit hashes, PR numbers, ticket IDs)
5. The user's original question

### Investigator roster. One per available source endpoint

Cover every available category, with one investigator per selected endpoint. Local Git and forge PR discussion form the source-control slice. Record endpoint ambiguity and duplicate-category coverage in the map.

Each entry names the category and the kind of "why" it uniquely surfaces. Use it to know what to expect back, how to name a gap when a category returns empty, and (only in the rare provably-irrelevant case) to justify a skip.

1. **Source control investigator**. Git history, `gh` for PRs, code comments, tests. Always spawn when repository access is established. Report a missing repository as an explicit blocker for code-anchored investigation. Best at surfacing *implementation-time rationale captured during review*.

2. **Issue / ticket tracker investigator** (e.g. Linear, Jira, GitHub Issues, Plane, Shortcut MCP). Best at surfacing *the product or business forcing function*. Strongest when the why is external to engineering.

3. **Long-form documents investigator** (e.g. Notion, Confluence, Google Docs, Coda MCP). Best at surfacing *long-form design rationale*. Where the why is written out before it becomes code.

4. **Real-time team chat investigator** (e.g. Slack, Discord, Microsoft Teams, Mattermost MCP). Best at surfacing *real-time deliberation that never reached a doc*. Especially important when the source control, ticket, and doc paper trail is thin.

5. **Infrastructure observability investigator** (e.g. Datadog, New Relic, Honeycomb, Grafana, Splunk MCP). Infra/runtime view. Best at surfacing *infrastructure and runtime reality that motivated the code*. Strongest when the target reacts to an infra signal (timeouts, retries, rate limits, circuit breakers).

6. **Error / exception tracking investigator** (e.g. Sentry, Rollbar, Bugsnag, Airbrake MCP). Best at surfacing *the specific exceptions and error trajectories that motivated defensive or corrective code*. Strongest for catch blocks, null guards, type checks, retries, and other defenses.

7. **Product analytics warehouse investigator** (e.g. Databricks, Snowflake, BigQuery, ClickHouse, dbt, Redshift MCP). Product/data view. Best at surfacing *product and data reality that shaped the code*. Strongest for flag-gated code, experiment-driven ships, data migrations, and "where did this number come from" questions.

### When to skip an investigator

Only with an **explicit, written justification** that goes in the final Sources Consulted. Two valid reasons:

- **No MCP is available for that category** in this environment. Flag it as a gap, not a choice: "Real-time team chat skipped. No matching MCP available, so the conversational record was not searchable."
- **The source is provably irrelevant**, not just "probably irrelevant." A high bar: "Error / exception tracking skipped. Target is a build-time script with no runtime code path."

If your scope assessment suggests a single-commit trivial target where the PR description already contains the complete answer, you may answer inline **only after** confirming all seven available category searches would be redundant. Say so explicitly. This should be rare.

## Step 4. Synthesize

Dispatch one fresh local synthesizer using `why synthesizer`. Give it read-only code and source access sufficient to spot-check citations. Missing citation access stays a documented verification gap; summaries or search snippets cannot stand in for original evidence.

The synthesizer gets:
1. The investigator findings, including any null results and any categories skipped with justification
2. The code anchor
3. The user's original question
4. The epistemics framework from [references/epistemics.md](references/epistemics.md)
5. The synthesizer prompt template from [references/synthesizer-prompt.md](references/synthesizer-prompt.md)

## Step 5. Present

Present the synthesizer's output to the user. You may lightly edit for clarity or add context from the conversation, but **do not rewrite the confidence language**.

## Output Format

The output structure is the one in [references/synthesizer-prompt.md](references/synthesizer-prompt.md): The Question, The Code in Question, What We Found, What We Can Reasonably Infer, Competing Hypotheses, What We Don't Know, Sources Consulted, Confidence Summary. Adapt as needed, but keep the confidence separation intact, and keep Sources Consulted as one line per investigator, including the ones that returned nothing or were skipped, with the reason.

After Sources Consulted, if the user's `why` question is a precursor to changing this code, convert the lineage findings into a Preserve / Change / Avoid / Risk constraint set for planning the change.

## Common Failure Modes to Avoid

- **Recency bias**. Assuming the most recent commit is authoritative. The current shape is often the accretion of many earlier decisions. Trace back.

## Reference Files

- [references/epistemics.md](references/epistemics.md). Confidence tiers and phrasing guide. The synthesizer must follow it.
- [references/investigator-prompt.md](references/investigator-prompt.md). Base prompt template for investigator subagents.
- [references/source-playbook.md](references/source-playbook.md). Index pointing at the category playbooks below.
- `references/sources/*.md`. One self-contained example playbook per category, plus cross-cutting `incident-postmortem.md`. Give an investigator the single file that matches its category and adapt it to the available MCP.
- [references/synthesizer-prompt.md](references/synthesizer-prompt.md). Prompt template for the synthesizer subagent, including the output format.
