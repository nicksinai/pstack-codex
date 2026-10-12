# Codex compatibility contract

Read this contract when a pstack skill requests it. Apply the workflow within the user's request and the host's governing instructions. Installation exposes instructions; it does not authorize execution, persistent mode, external messaging, merging, or deployment.

## Package and invocation

The portable package uses root `plugin.json` and root `skills/`. Names use the `pstack-` prefix as well as the host's plugin namespace. Resolve links relative to the file containing the link, never a developer's checkout. Read linked workflow instructions when a caller requires their behavior. Directly reading bundled instructions does not require a second user selection.

Each user-facing entry sets `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. Select the installed skill explicitly in the desktop skill picker. Where the Codex host supports `$` mentions, use `$pstack-<name>`. A recipient must confirm the actual picker identity; presentation and namespacing can differ across clients. One invocation covers the current request. Sticky mode requires its separate entry/exit contract; plugin metadata alone does not establish persistence.

## Capabilities and authority

A plugin distributes instructions and declared integrations. It cannot grant arbitrary tools. Before a workflow depends on a capability, inspect the current tool schema and permissions. Use only exposed operations. Report missing operations and the affected workflow step. Never fabricate tools, successful actions, service access, observations, or delegate results.

Use native GPT models for this release. Model identity and reasoning effort are separate choices validated against the recipient's environment. Independent GPT workers do not provide upstream Claude/Grok provider diversity. Local workers replace cloud execution. Bound concurrency and give every writing worker an explicit isolated checkout; worktree creation alone does not move a worker. Shared ports, sessions, and artifacts need separate ownership.

Keep investigation, code changes, PR preparation, babysitting, merge, and deployment authority distinct. Upstream broad team-chat permission does not override the host requirement for explicit authorization to send messages. Preserve existing skills and configuration. Write personal settings only to recipient-owned locations established by the relevant setup workflow.

## Qualification

The authoritative per-ticket arguments are in [qualification](../qualification/README.md). Their statuses describe source/configuration properties under stated premises, not guaranteed agent compliance. A tool observed in an implementation chat is not evidence that a friend's installed plugin receives that tool. UI outcomes, runtime availability, and successful installation remain conditional until observed in the recipient's environment.

Current official evidence is recorded in [capabilities](../qualification/capabilities.md). Additional workflow-specific capability contracts must link here and record their authoritative evidence rather than invent a parallel runtime.
