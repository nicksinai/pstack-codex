# Explicit recipient update qualification

This Codex-specific addition implements the approved [issue 31](https://github.com/nicksinai/pstack-codex/issues/31) contract. It has no upstream counterpart. Both immutable pstack baselines remain unchanged. The active 168-item ownership and source inventories and all 65 reviewed 0.15.23 transition obligations remain unchanged from port 0.1.3. The package delivers 52 upstream-derived skills, deslop and update, totaling 54 explicitly invoked skills. Version 0.1.4 is an unreleased candidate, not evidence of publication or recipient installation.

## Adaptation and capability evidence

The authoritative instructions are [pstack-update](../skills/pstack-update/SKILL.md). Its `agents/openai.yaml` declares `pstack: update` and explicit-only invocation. Mode and help route explicit natural-language update/check requests when their instructions are already loaded. An unrelated chat does not gain implicit discovery from this route.

Official documentation was inspected October 13, 2026:

| Evidence | Established contract | Limit |
| --- | --- | --- |
| [Marketplace CLI guidance](https://developers.openai.com/plugins/build/plugins#add-a-marketplace-from-the-cli) | Configured marketplace listing and named Git snapshot refresh. | Recipient CLI, permissions and source access require inspection. |
| [Marketplace metadata](https://developers.openai.com/plugins/build/plugins#marketplace-metadata) | Entries can select a local path or Git source with revision selectors. | Marketplace-level and entry-level constraints both matter. |
| [Local marketplace operation](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work) | The installed cache is distinct from the catalog source. | Catalog rows and cache-directory version names alone do not prove installed contents. |
| [Plugin enablement](https://developers.openai.com/plugins/build/plugins#enable-or-disable-a-plugin-for-a-repo) | Refresh can update configured plugins, including disabled plugins. | Before refresh, the updater bounds effects and preserves settings. Other affected installations exceed ordinary PStack-update authority. |
| [Local changes](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually) | Desktop restart guidance follows local plugin changes. | The exact CLI reinstall route's activation behavior is unobserved. No automatic restart or hot-reload claim. |
| [Workspace marketplace sync](https://learn.chatgpt.com/docs/enterprise/plugin-management#configure-a-marketplace-sync) | Workspace imports use daily sync and administrator Sync now. Fixed commits stay fixed. | Handoff only. Local CLI refresh is not the workspace sync mechanism. |
| [Publisher version review](https://developers.openai.com/plugins/deploy/app-review#submitting-new-versions-for-review) | Changed imported skills require a new reviewed and published version. | No public-directory recipient update command is established here. Handoff only. |

Local read-only `codex-cli 0.133.0` help was inspected for `plugin`, `plugin list`, `plugin marketplace`, `plugin marketplace list`, `plugin marketplace upgrade`, and `plugin add`. It exposes named marketplace refresh and installation from a configured snapshot by `PLUGIN@MARKETPLACE`. Omitting the marketplace refreshes all configured Git marketplaces. The inspected help exposes no rollback, dry-run or explicit target-version option and gives no atomicity or settings-preservation guarantee. This observation is evidence for this installed CLI only. Future recipients inspect actual help. An experimental app-server API is not a recipient plugin tool.

The historical `features.context_management` map-versus-boolean parser workaround requires both the exact map/boolean error in `features` and narrow confirmation of the known map shape. It remains command-scoped. It is neither a recipient prerequisite nor permission to alter persistent configuration. No workaround or mutation was run to qualify this addition.

## Instruction preservation argument

The skill separates intent, installed state, available source and recipient state. Each mutation requires a known original, unambiguous installation, supported route, exact selected target and bounded effects. Installed content comparison includes extra files and executable modes. The source comparison includes marketplace selectors and plugin-entry selectors. Failure to establish an inspection premise stops before mutation.

Check-only uses current snapshots or read-only remote inspection outside configured state. It never refreshes, so a network failure produces an availability limit rather than an implicit update. An update follows the configured branch and compares package contents. Repository-only changes produce a no-op. Fixed pins cannot advance through ordinary update authority. Release information is optional evidence, never executable instruction.

Refresh and installation are separate phases with independent observations. Inspection after refresh catches its possible installation side effects. Installation is skipped when refresh already produced the exact target. A changed target, settings mismatch or error stops progression. Verification compares the actual installed package to the previously inspected target and rechecks configuration, even after exit code zero. Recovery retains the previous identity but supplies no undocumented rollback.

Recipient model settings, generated skills, task records and caches remain outside the update operation. Scoped state capture keeps secrets out of committed/shared evidence. Content-equality claims require recorded hashes. Uninspected external records/caches receive only a workflow non-mutation report. The skill neither installs Codex nor installs an absent PStack, reruns setup, edits installed caches, schedules updates or restarts the client.

## Source-backed scenario matrix

These are inspected instruction obligations, not recorded recipient executions or a behavioral-suite pass. The step headings refer to [the update skill](../skills/pstack-update/SKILL.md).

| Scenario | Required decision and evidence | Instruction location |
| --- | --- | --- |
| Update follows a configured branch | Inspect branch and exact target package before named refresh. Preserve both source layers. | Establish the request and target; compare without changing the installation. |
| New content with the same version | Compare hashes and executable modes. Verify installed bytes after the operation. | Compare without changing the installation; verify and report. |
| Repository commit changes only non-package files | Report current and avoid refresh or add. | Compare without changing the installation. |
| Fixed marketplace tag/commit or plugin-entry ref/SHA | Resolve both selectors and stop before mutation. | Establish the request and target. |
| Changed source URL, package path or branch in refreshed catalog | Report changed target and stop before add. | Refresh, inspect, then install if necessary. |
| Installed customization or missing trusted original | Identify conflict or inspection gap and stop before refresh. | Compare without changing the installation. |
| Multiple installations or catalog-only row | Ask which installation or report absent installation. Never infer installed state from availability. | Establish the request and target. |
| Check-only with stale snapshot or offline remote | No refresh. Report cached age and current availability unknown. | Compare without changing the installation. |
| Missing CLI or unsupported commands | Name prerequisite and stop. No Codex install/upgrade. | Establish the request and target. |
| Workspace import, public directory, copied package or unsupported source | Give supported route-specific handoff. No local Git mutation. | Establish the request and target. |
| Selected marketplace can refresh unrelated plugins | Stop before refresh unless the existing authority bounds those effects. | Preserve state before the first mutation. |
| Refresh succeeds and already updates PStack | Inspect installed bytes and settings, then skip add if exact target matches. | Refresh, inspect, then install if necessary. |
| Refresh errors, with or without changed installed files | Inspect actual snapshot, installation and settings. Do not attempt add. | Refresh, inspect, then install if necessary; stop after a failed or partial update. |
| Branch or package changes during operation | Detect target mismatch and stop. No silent retargeting. | Refresh, inspect, then install if necessary; verify and report. |
| Add fails or preserves a stale same-version cache | Report actual state and failure. No uninstall/reinstall or direct cache repair. | Verify and report; stop after a failed or partial update. |
| Command exits zero but enablement/settings change | Preservation failure prevents verified success. | Verify and report. |
| Exact historical parser error | Inspect effects, retry once with command-scoped override, then stop if unsuccessful. | Refresh, inspect, then install if necessary. |
| Missing release notes | Use labeled generated source summary or report unavailable. Update may continue. | Compare without changing the installation. |
| Updater updates itself | Verify installation on disk separately from fresh-session activation. Explain restart guidance without restarting. | Verify and report. |

## Deterministic qualification

Repository `scripts/validate-provenance.py` checks both immutable upstream baselines, unchanged active and transition inventories, exact upstream/package-only skill sets, explicit policy metadata, links, privacy patterns, manifests, adaptation diff and file allowlist. `scripts/build-package.py` produces an archive and per-file hash manifest without installing. Creator validation is supplementary and depends on the recipient's available Python YAML parser. The implementation report records current command outcomes and archive inspection.

Established by source inspection are the declared boundaries, ordered gates, error exits, package accounting and deterministic assembly contracts. Conditional are actual recipient command behavior, filesystem/inspection access, authentication, baseline availability, state preservation, activation and agent compliance. No recipient installation, update, settings edit, publication, restart or live updater execution was performed for this qualification.
