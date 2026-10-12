# pstack for Codex

A Codex adaptation of Lauren Tan / poteto's pstack. This candidate currently provides explicit `pstack-bro`, `pstack-unslop`, and `pstack-technical-writing` workflows. Other workflows remain under implementation; see the source repository's ownership inventory. The source-backed argument is in [qualification](qualification/README.md).

## Install this candidate in a project

Use a Codex desktop version with local/repo marketplace support. Your organization's policy must allow local plugins. These prose workflows require no credentials, extra tools, or chosen model. Review the [compatibility contract](references/compatibility.md) and [capability evidence](qualification/capabilities.md).

1. Obtain this repository or a copy of this package from its maintainer. Access to a private repository requires an invitation. Copy the entire package directory to `plugin/pstack` inside your own project. Preserve its relative layout. If that path exists, choose a distinct path and adjust the catalog entry.
2. Review `marketplace.example.json` in this directory. Merge its plugin entry into your project's `.agents/plugins/marketplace.json`. If you create a catalog, copy the example's full content. If a catalog exists, keep its name and existing entries. Set `source.path` to your package's location relative to the project root, beginning with `./`. Keep the path inside the project.
3. Restart desktop. In the Plugins Directory, choose the project's marketplace and install `pstack-codex`. Confirm its displayed skills. If your client does not expose that local source, stop and check the linked official guidance and account policy.
4. In a new chat, explicitly select a skill in the skill picker. Where `$` mentions are supported, use `$pstack-bro`, `$pstack-unslop`, or `$pstack-technical-writing`. Use the selector's actual identity if the host adds a plugin prefix.

Example requests:

- Select `pstack-bro` after an assistant response to restate that response plainly.
- Select `pstack-unslop` and provide text to edit, preserving meaning and tone.
- Select `pstack-technical-writing` and provide a document or authorized file path. The workflow also reads the bundled unslop instructions.

Installation makes skills available. It does not activate a continuing mode or authorize file edits. The sample marketplace is deliberately outside automatic discovery paths. This repository does not enable the plugin in `.codex/config.toml` or install anything globally.

## Remove this candidate

1. Uninstall or disable `pstack-codex` in the Plugins Directory. If you explicitly added a project enablement entry, remove only that entry, preserving unrelated settings.
2. Remove only this plugin's entry from the project marketplace. Preserve the catalog and other entries.
3. Remove the package copy you created, then restart desktop. Keep documents you created with the workflows unless you want to delete them separately.

Project config can disable a local plugin using `[plugins."pstack-codex@YOUR-MARKETPLACE-NAME"]` and `enabled = false`. Use your catalog's actual name. Disabling is not deletion, and refresh may still refresh files. See [official package guidance](https://developers.openai.com/plugins/build/plugins#enable-or-disable-a-plugin-for-a-repo).

## Source and limits

Derived from [Lauren Tan's official pstack](https://github.com/cursor/plugins/tree/d0ef80d86795816da932a153458c5dbe192d294e/pstack), version `0.15.15`. The port's version is independent. The [MIT license](LICENSE) covers original source; see [NOTICE](NOTICE.md). This is an independent adaptation, not an official Cursor or OpenAI plugin.

The source repository retains the unmodified baseline, SHA-256 inventory, ownership, and generated adaptation diffs outside the installable package. Updates are reviewed and pinned. No automatic upstream sync occurs. Source/configuration checks do not prove agent compliance or successful installation. No runtime or UI installation was observed during creation.
