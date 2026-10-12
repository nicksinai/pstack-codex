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
