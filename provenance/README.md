# Pinned source and ownership

`upstream/pstack/` is an unmodified, tracked reconstruction baseline. It is distinct from the ignored reconnaissance checkout at repository-root `upstream/`. Baseline files are inert review evidence outside the installable plugin. Do not install this directory or run its original helpers as adapted workflows.

The baseline is Cursor plugins revision `d0ef80d86795816da932a153458c5dbe192d294e`, pstack version `0.15.15`, authored by Lauren Tan. `ownership.json` preserves every source path and SHA-256 from the recon manifest. Each file has one primary GitHub issue owner. `pending` means its owner has not delivered an adapted target; `deferred` means the agreed first-release exclusion. Neither means qualified. Both agent definitions, all 51 top-level skills, 23 playbooks, principle references, executable helpers, original tests, docs, and dormant Benny source are inventoried.

Maintainers update each delivered item's `target` and `disposition` at integration. One shared inventory owner avoids concurrent edits. Per-ticket qualification remains in `plugin/pstack/qualification/issue-N.md`. Shared bootstrap/library files have a single primary owner even when several callers consume them; callers record their dependency.

Run from the repository root:

```sh
python3 scripts/validate-provenance.py
python3 scripts/adaptation-diff.py > provenance/adaptations.patch
```

The diff reports mapped targets against their exact originals. A pending mapping is not an assertion that the source is unchanged or excluded. New package-only instructions are maintained in ordinary Git history; initial additions are summarized in each issue's proof ledger. Source bytes, source hashes, and target contents remain independently inspectable. Preserve this baseline when reviewing upstream updates; introduce a separately pinned baseline and account for each changed requirement.

The `plugin/pstack` directory is the friend-shareable unit. This provenance directory and repository implementation records can accompany it as review material but are not runtime dependencies.

## Upstream change monitor

[Check upstream pstack](../.github/workflows/check-upstream.yml) runs daily at 13:23 UTC and supports manual dispatch. It compares the official repository's default-branch `pstack/` file contents against the hashes in `ownership.json`, including new files and agreed exclusions. Changes to other plugins do not cause issue updates. It uses Git and Python's standard library to read upstream source without executing upstream helpers.

The monitor creates one **Review upstream pstack changes** issue with `needs-triage`, or updates that issue when the pstack content or reviewed pin changes. The report links exact upstream revisions and mapped Codex counterparts, marks unmapped additions and deferred files, and provides a complete report artifact retained for 30 days. No differences means no new issue; an open monitor issue closes when the reviewed baseline catches up. A manually closed issue stays closed for the same content and reopens on new content. Maintainer decisions belong in comments because the monitor owns the issue body. Failures surface as failed Actions runs rather than a false no-change result.

Run a read-only comparison locally:

```sh
python3 scripts/check-upstream.py --output /tmp/pstack-upstream-report.md
```

`--publish` additionally maintains the GitHub issue using authenticated `gh`. The workflow uses its repository-scoped token with `contents: read` and `issues: write`, serializes runs to avoid duplicate issue creation, and never imports, ports, publishes or installs upstream changes. Review and release remain the process described above. GitHub schedules can be delayed and can be disabled after 60 days of inactivity in public repositories; check Actions if the monitor stops running. See [scheduled workflow behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule) and [token permissions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax#permissions).
