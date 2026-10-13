# Explicit PStack recipient updates

Approved October 13, 2026. Tracked in [issue #31](https://github.com/nicksinai/pstack-codex/issues/31). This is a Codex-specific addition, separate from maintainer review of new upstream source.

## Problem

Recipients should be able to explicitly request “update pstack” without remembering Codex CLI commands. Add a Codex-specific `pstack: update` skill. The design was approved through a decision interview before implementation.

## Agreed contract

- “Update pstack” authorizes inspection and update within the existing source and revision constraints. “Check for updates” remains read-only, including no marketplace refresh.
- Execute only for configured local Git marketplaces with supported commands. Provide supported handoff guidance for workspace-managed, public-directory, copied and unsupported installations. Do not install a missing plugin.
- Identify the actual installation and marketplace. Ask if ambiguous. Preserve source, branch, tags and commit selectors. A fixed tag or commit does not advance without an explicit request to change the pin.
- Track the configured branch. Compare package contents and revisions as well as version metadata. Refresh only the selected marketplace; identical distributable contents do not require reinstalling.
- Show publisher notes when available. Otherwise summarize verified repository changes with source links and identify the summary as generated. Missing notes do not block updating.
- Detect actual CLI support. Do not install/upgrade Codex or require one version. Apply the historical command-scoped workaround only for its exact configuration parsing error.
- Preserve recipient enablement, configuration, model roles, generated skills, task records and external caches. Do not rerun setup/migrate settings or edit installed cache files directly. Stop for conflicting package customizations.
- Verify installed identity, version, revision/content identity and relevant pre/post configuration independently. Marketplace rows and exit codes alone do not establish installed state. Separate on-disk installation from current-chat activation.
- Self-update does not establish hot reload. Explain documented restart requirements. Never restart automatically.
- Stop and inspect failed/partial updates. Report actual state and supported recovery options with the prior revision retained as recovery information. No automatic uninstall, source switching, unpinning or undocumented rollback.
- Start with an agent skill using supported Codex commands. Add a narrow helper only when reliable comparison requires it.

## Qualification and delivery

Preserve both immutable upstream baselines and the reviewed 0.15.23 active and transition inventories. Record the addition separately from upstream-derived workflows. Update explicit UI metadata, catalog/help, package allowlist and structural checks. Use the agreed source-backed verification standard; distinguish conditional recipient execution from deterministic structural proof. No installation, publication, merge or restart is authorized by this implementation task.

## Capability evidence

- https://developers.openai.com/plugins/build/plugins#add-a-marketplace-from-the-cli
- https://learn.chatgpt.com/docs/enterprise/plugin-management#configure-a-marketplace-sync
- https://developers.openai.com/plugins/deploy/app-review#submitting-new-versions-for-review

Local CLI 0.133.0 help exposes marketplace upgrade and plugin add. Those help contracts do not establish rollback, atomicity or settings-preservation guarantees.

## Refresh side effects

Official documentation states that marketplace refresh can install or refresh configured plugin files, even for disabled plugins. Treat refresh as the first installation mutation. Run preservation and customization gates before it, inspect resulting installation state afterward, and skip redundant plugin add when refresh already delivered the exact target. Stop when refreshing the selected marketplace could mutate unrelated configured plugins beyond the request's authority. See [enable or disable a plugin](https://developers.openai.com/plugins/build/plugins#enable-or-disable-a-plugin-for-a-repo).
