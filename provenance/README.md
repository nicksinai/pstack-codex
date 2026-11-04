# Pinned source and ownership

`upstream/pstack/` is an unmodified, tracked reconstruction baseline. It is distinct from the ignored reconnaissance checkout at repository-root `upstream/`. Baseline files are inert review evidence outside the installable plugin. Do not install this directory or run its original helpers as adapted workflows.

The baseline is Cursor plugins revision `d0ef80d86795816da932a153458c5dbe192d294e`, pstack version `0.15.15`, authored by Lauren Tan. `ownership.json` preserves every source path and SHA-256 from the recon manifest. Each file has one primary GitHub issue owner and an explicit `source_revision` for its active adaptation. `pending` means its owner has not delivered an adapted target; `deferred` means the agreed first-release exclusion. Neither means qualified. Both agent definitions, all skills, playbooks, principles, helpers, original tests, docs and dormant Benny source are inventoried. Historical delivery counts belong to their retained qualification records.

Maintainers update each delivered item's `target` and `disposition` at integration. One shared inventory owner avoids concurrent edits. Per-ticket qualification remains in `plugin/pstack/qualification/issue-N.md`. Shared bootstrap/library files have a single primary owner even when several callers consume them; callers record their dependency.

Run from the repository root:

```sh
python3 scripts/validate-provenance.py
python3 scripts/adaptation-diff.py > provenance/adaptations.patch
```

The diff reports mapped targets against their exact originals. A pending mapping is not an assertion that the source is unchanged or excluded. New package-only instructions are maintained in ordinary Git history; initial additions are summarized in each issue's proof ledger. Source bytes, source hashes, and target contents remain independently inspectable. Preserve this baseline when reviewing upstream updates; introduce a separately pinned baseline and account for each changed requirement.

The `plugin/pstack` directory is the friend-shareable unit. This provenance directory and repository implementation records can accompany it as review material but are not runtime dependencies.

## Upstream change monitor

[Check upstream pstack](../.github/workflows/check-upstream.yml) runs daily at 13:23 UTC and supports manual dispatch. It compares the official repository's default-branch `pstack/` file contents against the separately declared reviewed pin in `baselines.json`, including new files and agreed exclusions. Active adaptations remain mapped independently in `ownership.json`. Changes to other plugins do not cause issue updates. It uses Git and Python's standard library to read upstream source without executing upstream helpers.

The monitor creates one **Review upstream pstack changes** issue with `needs-triage`, or updates that issue when the pstack content or reviewed pin changes. The report links exact upstream revisions and mapped Codex counterparts, marks unmapped additions and deferred files, and provides a complete report artifact retained for 30 days. No source differences and no pending/blocked transition obligations means no new issue; an open monitor issue closes only when both conditions are met. Archiving new source alone does not complete adaptation. A manually closed issue stays closed for the same content and reopens on new content. Maintainer decisions belong in comments because the monitor owns the issue body. Failures surface as failed Actions runs rather than a false no-change result.

Run a read-only comparison locally:

```sh
python3 scripts/check-upstream.py --output /tmp/pstack-upstream-report.md
```

`--publish` additionally maintains the GitHub issue using authenticated `gh`. The workflow uses its repository-scoped token with `contents: read` and `issues: write`, serializes runs to avoid duplicate issue creation, and never imports, ports, publishes or installs upstream changes. Review and release remain the process described above. GitHub schedules can be delayed and can be disabled after 60 days of inactivity in public repositories; check Actions if the monitor stops running. See [scheduled workflow behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule) and [token permissions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#permissions).

## Separately pinned review transitions

`baselines.json` retains the original 0.15.15 revision, predecessor 0.15.23 revision, and current reviewed 0.15.36 revision `bb68f2365eceafa0cb2d253112f675acf5f144cc`. Each immutable archive has its own complete SHA-256 manifest. The newest manifest also records Git executable modes. Prior ownership and transition ledgers are retained as `ownership-0.15.23.json` and `upstream-transition-0.15.23.json`; the validator pins their content hashes.

`upstream-transition.json` records the exact 487-file change from 0.15.23: 412 additions, 68 changes and seven removals. Each row names its source hashes, issue owner, target, disposition, reason and qualification evidence. `pending` and `blocked` remain incomplete and prevent distribution. `adapted`, `equivalent`, `retained`, `deferred`, `reference` and `removed` are accounted outcomes, not claims of observed recipient runtime behavior.

`ownership.json` accounts for every one of the 573 current files against the current source revision. Unchanged source bytes still receive current-revision mappings after comparison; historical mappings remain inspectable in the retained ledger. The 13 agreed first-release exclusions remain `deferred`. The 376 statechart upstream test files and official Claude-specific harness adapter are `reference`: retained intact in the archive for review, not installed as runtime dependencies. The 31 statechart non-test source files are delivered. Removed orchestration helpers and Interrogate templates are absent from the package and explicitly accounted in the transition.

Synchronize the two package qualification JSON mirrors with the authoritative ledgers. Review new runtime files in `package-files.json`, then regenerate `adaptations.patch`. The validator checks all three archives, historical ledgers, current inventory, exact source delta, removed targets, mapped preservation, description provenance, metadata, executable import closure, links, privacy, file allowlist and pending qualification. The build calls the complete validator before assembling a deterministic archive.

A read-only comparison using an inspected official checkout is supported with `--source-checkout CHECKOUT`. It does not fetch, import, execute helpers or mutate issues. The monitor tracks pending obligations even when the current reviewed source matches upstream; archiving source alone cannot close a review. Changes to files retained only as references and exclusions are still monitored.
