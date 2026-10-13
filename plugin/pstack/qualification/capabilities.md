# Capability evidence

Retrieved October 12, 2026 from official OpenAI documentation. Product contracts can change; recheck these sources when updating the port or adopting it in another client.

| ID | Supported contract | Authoritative source | Limit |
| --- | --- | --- | --- |
| C1 | Portable root `plugin.json` declares Agent Plugins schema; root `skills/` is discovered without a `skills` field. | [Package your plugin, Create a plugin manually](https://developers.openai.com/plugins/build/plugins#create-a-plugin-manually) | Not an observed installation in this repository. |
| C2 | Repo marketplace file is `.agents/plugins/marketplace.json`; local `source.path` is relative to the marketplace root, begins `./`, and stays inside that root. Entries include installation/authentication policies and category. | [Package your plugin, Marketplace metadata](https://developers.openai.com/plugins/build/plugins#marketplace-metadata) | Directory availability varies by surface and account policy. |
| C3 | `agents/openai.yaml` supports `policy.allow_implicit_invocation: false`; explicit selection remains available. | [Build skills, Optional metadata](https://developers.openai.com/codex/skills#optional-metadata) | Instruction compliance remains probabilistic. |
| C4 | Skill instructions require name and description; full instructions load on selection. Explicit invocation uses the skill picker; documented Codex CLI/IDE syntax includes `$` mentions. | [Build skills, How ChatGPT and Codex use skills](https://developers.openai.com/codex/skills#how-codex-uses-skills) | Confirm the installed identity and mention syntax in the recipient's desktop version. |
| C5 | The documented repo install sequence copies the package, adds/updates a marketplace entry, restarts desktop, and selects the plugin. Trusted project config can enable or disable it by `plugin-name@marketplace-name`. | [Package your plugin, Install a local plugin manually](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually), [Enable or disable a plugin for a repo](https://developers.openai.com/plugins/build/plugins#enable-or-disable-a-plugin-for-a-repo) | Trust, installation, and enablement remain recipient choices. No files outside this checkout were changed. |
| C6 | Plugins bundle instructions, optional MCP connections, assets, and supported hooks; arbitrary Cursor `Task` tools and Markdown agent files are not granted by packaging. | [Package your plugin](https://developers.openai.com/plugins/build/plugins), [Claude plugin conversion](https://developers.openai.com/plugins/guides/submit-claude-plugin#review-what-openai-supports) | Each workflow binds actual recipient capabilities. |

The issue #2 prose workflows need selected text or conversation context, ordinary response generation, and optional authorized document editing. They require no connector, external model, delegate, script, credential, hook, or executable dependency. A text-only response is sufficient when no file edit was requested. Missing context must be requested or stated; it cannot be inferred from inaccessible files.

No sticky-mode field, cloud worker, durable scheduler, history parser, or additional tool surface is established by C1–C6. Their complete conditional contracts are indexed below and linked in the final qualification. Operating through app closure or sleep is outside the release scope.

## Whole-package host capability evidence

The complete candidate closes the later source targets; these host premises remain conditional at runtime. Per-ticket source/control-flow arguments and the [final update qualification](issue-30.md) distinguish content from actual operation.

| ID | Supported contract | Authoritative source | Limit |
| --- | --- | --- | --- |
| C7 | Native Codex subagents, separate model and reasoning-effort configuration, delegated scopes; actual controls/schema must be checked. | [Codex subagents](https://developers.openai.com/codex/subagents) | Plugin Markdown does not register custom agents or guarantee this chat's tools, available capacity/nesting, enforceable read-only sandbox or no-inherited-history mode. Blind workflows require demonstrated context isolation. |
| C8 | App-server thread read/list operations and generated schemas describe full-turn history access where a supported client is available. | [App-server reference](https://learn.chatgpt.com/docs/app-server) | Documentation is not a plugin tool. Bind the actual authorized reader or metadata-verified local transcript format; summaries do not establish successful file/tool reads. Workspace/topic/time scope governs reads. |
| C9 | Plugins distribute instructions/resources and optional supported integrations, not arbitrary browser/terminal/GitHub control. Skills can read bundled resources when selected. | [Plugin packaging](https://developers.openai.com/plugins/build/plugins), [Codex skills](https://developers.openai.com/codex/skills) | UI/CLI controls, Git/GitHub authentication and profiler access are recipient capabilities, checked before use. The pinned Cursor team-kit instructions provide the adapted companion contract, with included MIT notice. |
| C10 | Requested local automation can perform scheduled follow-up while the desktop environment is available. | [Scheduled tasks](https://learn.chatgpt.com/docs/automations) | Host/account schedule schemas remain conditional. Active waits do not survive lost execution. No operation through app closure, computer sleep or offline services is claimed. |

[C3/C4](https://developers.openai.com/codex/skills) establish explicit skill invocation and instruction loading. There is no claimed native enforced Cursor-style sticky mode: the [continuation contract](../references/continuation.md) uses explicit scoped entry/exit plus recipient-private checkpoint and recovery. The documented initial catalog cap is context-dependent with an 8,000-character maximum; the repository validator computes the current name/description total from the delivered skills and checks that ceiling. That total does not guarantee every entry appears. The mode's internal lookup remains the complete route.

Helpers rely on their actual declared runtimes, locked dependency graph and inspected control flow, as qualified in [issue 11](issue-11.md), [issue 12](issue-12.md) and [issue 14](issue-14.md). A source/helper invariant is established only under its filesystem/process/auth premises. No official host page guarantees recipient helper dependencies are already installed.

## Reviewed 0.15.23 update

Port 0.1.3 closes all 65 fixed source differences; [issue #30](issue-30.md) accounts for all 168 source items and the 53 delivered explicit skills. Goal playback adds no tool dependency; ketchup requires authorized conversation/history and current-state reads plus real screenshots or fact-grounded reply visuals as specified in its [capability contract](../references/ketchup-capabilities.md). The update grants no additional runtime capabilities. The existing verified `--trunk` interface and portable root manifest satisfy the reviewed upstream intent under their stated premises. Recipient installation and desktop behavior remain unobserved.

## Explicit recipient updating

[Update qualification](update.md) records current official marketplace, workspace-sync, directory-publication and restart evidence, plus inspected local CLI help. It distinguishes refresh side effects from installation, catalog availability from installed contents, and source-backed instructions from conditional recipient execution. No experimental app-server API is assumed available to recipients.
