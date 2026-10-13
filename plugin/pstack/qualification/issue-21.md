# Issue 21: separately pinned 0.15.23 review baseline

Part of specification #20. This ledger establishes source retention and transition accounting, not completion of the 0.15.23 adaptation or observed installation.

## Exact source and retained relationship

Original: official Cursor plugins revision `d0ef80d86795816da932a153458c5dbe192d294e`, pstack `0.15.15`, 164 files. Reviewed: revision `dbf49813a39c1a5389c5e28cb8e4c1c2379e2454`, pstack `0.15.23`, 168 files. Repository evidence retains both complete source archives and SHA-256 manifests separately; the original archive and recon manifest remain unchanged. The reviewed revision declares the original as its predecessor. No later source is included.

Source locators: [original pstack](https://github.com/cursor/plugins/tree/d0ef80d86795816da932a153458c5dbe192d294e/pstack), [reviewed pstack](https://github.com/cursor/plugins/tree/dbf49813a39c1a5389c5e28cb8e4c1c2379e2454/pstack), and [comparison](https://github.com/cursor/plugins/compare/d0ef80d86795816da932a153458c5dbe192d294e...dbf49813a39c1a5389c5e28cb8e4c1c2379e2454). The comparison includes other plugins; the transition ledger covers only pstack bytes.

## Active adaptation and remaining work

[Source inventory](source-inventory.json) identifies the exact `source_revision` for each delivered mapping. Initially all 164 mappings retain their original source revision and hashes. [Transition inventory](upstream-transition.json) separately accounts for exactly 65 differences: four added and 61 changed files, each with a primary owner, prior/current hash, target if known, disposition and reason. Pending and blocked items are not qualified. Primary help ownership belongs to #26, with #27 as an explicit dependency. Downstream tickets must record their source-backed decisions and qualification before closing those obligations.

The repository validator checks both complete archives, independent hash manifests, predecessor relationship, exact delta completeness, active mapping source revisions, local targets, qualification references for completed dispositions, and the package's matching inventories. The adaptation diff labels each source with its actual revision. These are deterministic source/content properties; they do not prove agent compliance.

## Monitor contract

The monitor compares observed pstack content against the declared reviewed revision, independently of the active adaptation map. It also reports pending or blocked transition obligations and keeps the tracking issue open for them even when observed bytes equal the archived snapshot. Content fingerprints exclude unrelated monorepo revision changes; unchanged fingerprints remain quiet. Existing single-issue, manual-close, reopen-on-change and fail-on-error behavior remains in place. Only explicit `--publish` authorizes issue mutation; local comparison can use a supplied checkout without executing its helpers.

## Direct evidence and limits

The monitor regression first failed because pending adaptations disappeared from a zero-delta report, then passed after the transition contract was implemented. Existing detection and issue-lifecycle checks pass. A read-only comparison against the exact reviewed source reports zero new upstream differences and 65 pending adaptation obligations. Complete package validation and deterministic archive assembly pass after regeneration; original source retention is independently checked against Git. Negative integrity checks reject corrupt source bytes in either baseline. No workflow, installation, release, upstream helper or external issue mutation is performed by this qualification.

Codex capability bindings and runtime conditions remain those recorded by the original package. This infrastructure change makes no new claim of recipient compatibility. Final instruction/helper qualification, new skills, inventory adoption and release versioning remain owned by #22–#30.
