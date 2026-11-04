# pstack for Codex

A shareable adaptation of Lauren Tan / poteto's pstack, updated to reviewed source 0.15.36 at Cursor plugins commit `bb68f2365eceafa0cb2d253112f675acf5f144cc`. Port version 0.2.0 includes 59 skills: 57 upstream workflows and principles, deslop, and the Codex-specific updater. It includes all 24 principles, all 23 playbooks and both original agent roles as instruction wrappers. The five new workflows are sharpen, statechart, create-formal-verification-skill, maintain-formal-verification-skill and ketchup-video. See [update qualification](qualification/upstream-0.15.36.md), [source inventory](qualification/source-inventory.json), [capabilities](qualification/capabilities.md) and [notices](NOTICE.md). It is not an official Cursor or OpenAI plugin.

The chat receiving PStack mode owns the playbook, ordered checklist and delegation. Comment Sicko remains a portable [review wrapper](references/comment-sicko.md), normally reached through `pstack-no-comments`, rather than a registered Cursor agent. The poteto-agent instruction wrapper initializes code-writing and helper delegates within that run. See the [coordinator and instruction-access qualification](qualification/issue-25.md) for the reviewed 0.15.23 slice and its limits.

## Recipient setup

Use Codex desktop with local marketplace support and an account/organization policy allowing local plugins. A plugin supplies instructions and helpers; it cannot grant tools. Read [compatibility](references/compatibility.md) before use. Installation and task authorization are separate.

### Install from the repository

If the Codex CLI is available, run:

```sh
codex plugin marketplace add nicksinai/pstack-codex --ref main
```

Clients with `codex plugin add` can also install from the terminal:

```sh
codex plugin add pstack-codex@pstack-codex-marketplace
```

Restart the desktop app, choose **PStack for Codex** in the Plugins Directory, and install **pstack-codex**. Then follow step 5 below. To pin a reviewed revision, replace `main` with its commit or release tag. The CLI command adds a marketplace source; installation happens in the desktop app. See the [official repository marketplace guidance](https://developers.openai.com/plugins/build/plugins#add-a-marketplace-from-the-cli).

Without the CLI, clone/download the repository and open it as a Codex project. Its committed `.agents/plugins/marketplace.json` points at `./plugin/pstack`; restart desktop and install from **PStack for Codex**, then follow step 5. Local marketplace availability depends on the recipient client and account policy and has not been observed on the recipient's machine.

### Copy into another project or use an offline archive

1. Obtain the public [source repository](https://github.com/nicksinai/pstack-codex) or an offline archive. For an archive, extract it and verify its companion SHA-256 digest and included `MANIFEST.json` before trusting its contents. The archive includes `plugin/pstack`, notices, source accounting and a local marketplace catalog.
2. Copy the complete `plugin/pstack` directory into your own project's `plugin/pstack`. Preserve the relative layout. If the destination already exists, choose a new path rather than overwriting it.
3. Merge the entry from this package's `marketplace.example.json` into your project's `.agents/plugins/marketplace.json`. For a new catalog, copy its complete content. Preserve existing catalog names and entries. The entry's `source.path` must begin `./` and resolve from the project/marketplace root to the copied package. Adjust it if you chose another location. Merely copying or adding a catalog does not install or enable anything.
4. Restart Codex desktop. In the Plugins Directory, select your project's marketplace and install `pstack-codex`. Confirm its displayed skills in a new chat. If the catalog is unavailable, check the [official local installation guidance](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually) and account policy; this package does not bypass either. No automatic installation or configuration edit is supplied.
5. Explicitly select `pstack-setup-pstack` to configure recipient-owned roles, budgets and capability checks. Existing user settings/skills remain under your control. Model identity and effort are separate, validated choices; inheritance aliases avoid hardcoded account model IDs. Read [models](references/models.md). No global custom-agent installation is required: [delegation](references/delegation.md) injects instruction wrappers into supported local children.

Use the actual picker identity if the host adds a plugin prefix. Documented `$` syntax depends on the recipient surface. The catalog may omit entries due to its size/context cap; select the main mode and use its complete bundled lookup rather than assuming every leaf appears in the picker.

## Activation and examples

Select `pstack-poteto-mode` in the picker before entering your request for the full workflow router, or select an individual leaf. A leaf or normal mode invocation applies to that request. Enter sticky mode explicitly with “Enter sticky PStack mode for this conversation.” End it with “Exit PStack mode.” Read [continuation](references/continuation.md) for scope, private checkpoint, interruption and recovery. Persistence requires available context or a valid scoped entry record; this is not a native enforced mode.

- `pstack-sharpen`: rewrite a prompt with expert methods, source material and an outside check; it does not perform the underlying task.
- `pstack-create-formal-verification-skill` / `pstack-maintain-formal-verification-skill`: check one important property with the appropriate verifier, state its bounded scope and preserve a project-local recheck path. Distinguish verification drift from code defects.
- `pstack-statechart`: check a TLA+ model, render the behavior as a statechart and show shortest paths to violated rules; a graph alone is not model-checking evidence.
- `pstack-ketchup-video`: render the checked catch-up as a subtitled slide video and keep every pending user decision in text beneath it. Missing rendering capability requires a disclosed fallback.
- `pstack-in-your-own-words`: play back your goals and problem before work begins; explicit selection does not start implementation or an interview.
- `pstack-ketchup`: checked visual catch-up on this conversation, including earlier pending user decisions; read-only except for reply visuals. History, state readers and a real visual channel remain [recipient prerequisites](references/ketchup-capabilities.md); see [qualification](qualification/issue-27.md).
- `pstack-how`: explain a named subsystem from source; `pstack-why`: reconstruct its rationale; `pstack-recall`: recover scoped recent work; `pstack-teach`: explain it interactively.
- `pstack-architect` or `pstack-arena`: compare independent designs/artifacts; `pstack-interrogate`: adversarial review that keeps only independently rerun failures; `pstack-swarm`: partition investigation or implementation coverage.
- `pstack-poteto-mode`: investigate, fix a bug, build a feature, refactor, prototype, assess visual parity, diagnose performance or measure a benchmark. The mode routes to its playbook, principles, cleanup and verification gates.
- “Prepare a PR,” “Babysit this PR” and “Ship this PR” are distinct requests under [PR delivery](references/pr-delivery.md). Installation/activation does not authorize merging or deployment.
- `pstack-reflect`: propose Accepted/Rejected/Backlog lessons and wait for approval before durable Accepted edits. `pstack-automate-me`: draft your own preferences and review them with you.
- “Plan a multi-phase change,” “orchestrate this program,” or “autopilot stack/full” routes through the corresponding playbook. [Program state](references/orchestration.md) and [continuation](references/continuation.md) retain ownership, evidence, recovery and stop boundaries.
- `pstack-poteto-help` provides recipes and the workflow map; `pstack-bro`, `pstack-unslop` and `pstack-technical-writing` cover prose.

## Verification and longer runs

Setup offers a project verification skill and, separately, a formal verification skill when the project lacks one. Accept either offer when useful; it does not silently start generation. An app verification skill drives real features and preserves evidence after cleanup. A formal verification skill picks a consequential property, chooses a tool appropriate to the question, checks it within explicit bounds and demonstrates failure on a broken variant. It records the covered code and last checked revision. After merges or refactors, maintenance distinguishes a stale model from a product bug; it does not weaken the property to obtain a pass or edit product code without a request.

Arena compares independent artifacts in separate writer locations. When another model family is unavailable, its upstream fallback skips that judge and the parent selects the base with the limitation disclosed. Interrogate retains only failures the parent independently reruns; dropped findings retain their reasons and no fixes are applied by the review itself.

Autopilot-full assigns one writer per PR and requires a fresh verification verdict on the patch that merges. The first code-ready head and large behavioral changes receive a full verification swarm; small fixes or rebases receive an appropriate fresh verifier. Autopilot-stack follows the same preparation and verification without merging: independent work branches from trunk, and stacking is reserved for actual dependencies. Orchestrate manages longer programs with owned workers and private checkpoints under the explicit Codex adapter. It does not claim a cloud Project API or durable execution across app closure. Use ketchup or ketchup-video for a read-only catch-up with every unresolved user decision retained.

## Capability and dependency requirements

Text editing/explanation needs selected text or authorized file reads. Parallel/design/review/program workflows require actual spawn/result/control operations, available capacity and isolated writer locations. Blind/private-rubric workflows additionally require a verified fresh-context/no-inherited-history operation. Read-only instructions are not sandbox enforcement. Native GPT independence preserves separate attempts but lacks upstream Claude/Grok provider diversity. Missing required capabilities block the affected gate, never become successful evidence.

History requires an actual scoped host reader or metadata-verified supported local transcript format; see [history](references/history.md). Shared sources require recipient connectors and authorization. Browser/terminal verification requires available controls and the target app: [verification controls](references/verification-controls.md), [UI](references/control-ui.md), [CLI](references/control-cli.md). Missing tools remain explicit blockers. The bundled [authoring adapter](references/skill-authoring.md) preserves visible pstack obligations; fidelity to the unavailable full Cursor built-in creator source remains unresolved.

Git delivery/cleanup requires Git and relevant authenticated forge tools. PR-watch helpers require Bun, Git, authenticated `gh` for GitHub, and a private writable dependency cache selected by the recipient. Program coordination uses supported host workers and private checkpoints; the retired orchestration scripts are not shipped. Explicit dependency setup may fetch pinned dependencies; no bundled `node_modules` or credentials are included. Follow [program setup](references/orchestration.md) and [PR delivery](references/pr-delivery.md), quote actual paths, and keep cache/store outside the installed plugin. Plan checking uses Node; worktree audit uses Python 3 and Git. Unix local filesystem/PID semantics qualify helper locking; Windows/network-shared stores are not qualified. Existing Graphite is optional; other forges lack the GitHub-specific helper adapter.

Unattended work runs while the computer/app/project/services remain available. Requested schedules require actual host automation support. Active waits are not durable schedulers. Operation through sleep, app closure, lost workers or offline services is excluded. Grok Bot UI and Benny are excluded (13 source files total). Cloud workers and external-provider bridges are deferred. Host rules and user limits govern authority, including explicit authorization for external messages.

## Update on request

Select **pstack: update** or invoke `$pstack-update` with "update pstack". When the main mode or help is already loaded, that request also routes to update. Use "check for pstack updates" for a read-only comparison. Explicit-only discovery means an ordinary message in an unrelated chat may need the skill selection first.

The updater uses supported commands for an existing configured local Git marketplace. It preserves source selection, fixed pins and recipient settings, stops for uncertain baselines or conflicting customizations, and verifies installed contents independently. Other routes receive supported next-step guidance. It never installs Codex, restarts the app or edits installed cache files. See the [update skill](skills/pstack-update/SKILL.md) and [qualification](qualification/update.md).

## Remove

Disable or uninstall `pstack-codex` through Plugins Directory. Remove only its marketplace entry, preserving other entries and configuration. If you explicitly enabled it in project config, remove only that enablement; the documented key is `pstack-codex@YOUR-MARKETPLACE-NAME`. Remove only the package copy you created, then restart desktop. Stop owned processes before removing a recipient-selected dependency cache. Keep or separately remove your own task records, generated skills and artifacts; uninstalling does not erase them. See [official enable/disable guidance](https://developers.openai.com/plugins/build/plugins#enable-or-disable-a-plugin-for-a-repo).

## Maintenance and evidence

The immutable 0.15.15, 0.15.23 and 0.15.36 archives remain separately pinned in the source repository. The [transition ledger](qualification/upstream-transition.json) accounts for 487 changed, added or removed files; the active inventory accounts for all 573 current source items. The 13 prior exclusions remain. Another 377 files are retained only as upstream reference evidence: 376 statechart test files and the Claude-specific harness adapter. [Update qualification](qualification/upstream-0.15.36.md) records requirement evidence, integrated checks and conditional runtime limits. Earlier qualification records describe their historical delivery states.

Maintainer updates to the pinned upstream baseline require a new source review; no automatic upstream synchronization occurs. Recipient updates use the explicit update skill to obtain an already adapted Codex package within their configured source constraints. Immutable original sources remain in the source repository, outside this package. The inventory records every original item, unique owner, adaptation/deferment and target. Per-ticket ledgers preserve the source-to-target argument. Deterministic checks establish content, hashes, reference closure and reproducible assembly; they do not establish observed recipient installation, service access, full agent compliance or real-app outcomes. The port requires no new behavioral qualification suite; pstack's own TDD/reproduction/live-verification requirements remain product behavior.
