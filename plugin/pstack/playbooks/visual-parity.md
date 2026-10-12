### Visual parity


Read [verification controls](../references/verification-controls.md) and the matching [UI](../references/control-ui.md) or [terminal](../references/control-cli.md) adapter before using a surface. Bind available tools and reserve runtime resources; a worktree does not isolate an application. Read [delegation](../references/delegation.md) for parallel owners. Missing capture/drive/image-diff capabilities block the affected evidence claim, not an invitation to infer success from source. 

**You own pixel-exact equivalence. The baseline is the spec. You do not touch it.** Equivalence is verified by image diff, not by eye.

1. Establish the baseline first, before any migration: a visual regression harness that screenshots the current component across its states, plus the target when matching two implementations. No baseline, no parity claim. A blocking prerequisite, not a follow-up.
2. Anti-shortcut clauses, stated and held: no harness modifications, no baseline tampering, no component restructuring to make a diff pass. If the baseline looks wrong, stop and ask, don't edit it.
3. Migrate one component at a time. Parallelize across worktrees, one owner per component (the **separate-before-serializing-shared-state** principle skill). Shared primitives migrate first as a blocking phase.
4. Verify each component against its baseline via image diff on the matching surface via the matching bundled control adapter. A nonzero diff is a fail. Investigate the pixel delta. Repeat the capture/diff/investigate loop per component until the diff is zero.
5. Run **Opening a PR** per component or per safe batch.

**Reply:** components migrated, the diff result for each, the baseline harness location, what's left.

Use [PR delivery](../references/pr-delivery.md) for Opening a PR, honoring delivery limits. Record baseline and treatment revisions, harness/configuration hash, viewport, device scale, fonts, theme, animation state, deterministic data and capture environment. Normalize nondeterminism before freezing the baseline; never change harness/tolerance after seeing a failing treatment. Zero means zero under the frozen image-diff comparison; perceptual similarity or an agent's eye is not pixel-exact parity. Reproduce flaky baseline captures before migration; if deterministic zero cannot be established, report the blocker and ask for a changed acceptance criterion. Component owners use separate branches and separate runtime reservations or serialized capture. Shared primitives must be completed and integrated before dependent owners begin. A user-approved design change is a new spec, not permission to tamper with the current parity baseline.
