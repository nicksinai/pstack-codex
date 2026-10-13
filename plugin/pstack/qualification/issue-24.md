# Issue 24: Markdown fences in plan checks

Part of specification #20. This qualification covers the existing checker CLI and its packaged regression coverage.

## Source and adaptation

Reviewed official Cursor plugins revision `dbf49813a39c1a5389c5e28cb8e4c1c2379e2454`, pstack 0.15.23. Exact source locators under `pstack/skills/poteto-mode/scripts/` are `check-plan.mjs` lines 47–76 (opening/closing fence parser), added `check-plan.test.ts` lines 1–96 (temporary-plan CLI cases), and `package.json` line 7 (test command).

The parser adopts the reviewed fence hunk exactly. Openers allow zero to three spaces and at least three backticks or tildes; backtick info strings cannot contain backticks. Closers require the opening character, at least its length and only whitespace afterward. Code example headings are ignored; validation resumes after a valid close. All checker code outside this hunk is unchanged, including the existing Codex-specific `Reviewed instruction source.` and `Audit cadence. 1h` markers.

The added CLI test file retains the upstream temporary-directory, real Node subprocess, cleanup, status and diagnostic assertions. Its valid plan replaces Cursor `git show`/loop markers with the existing Codex markers. The suffixed-closer example uses a full-length fence so suffix rejection is tested independently of the shorter-fence rule. The helper package retains its existing name, dependencies and typecheck command, adding the regression file to `bun test orch watch-pr`.

## Evidence and limits

The preconfirmed seam invokes the adapted checker command against temporary Markdown plans. Red then green was observed for indented fences, nested fences, full-length suffixed closers and invalid backtick info strings. Five tests cover ordinary/indented/longer fences, nested backticks, tilde info strings, mismatched/shorter/suffixed closers, heading and prose diagnostics after close, and invalid backtick info strings. Final targeted result: five pass, zero fail, 18 assertions. The complete helper command passes 43 tests with 142 assertions in an external copy using frozen dependencies and disabled install scripts; no dependency files were installed into the package. `bun run --bun typecheck` also passes. Plain `bun run typecheck` fails under the available Node 18 executable because the locked TypeScript 7 package exposes an extensionless ESM entry point; running the unchanged command with Bun avoids that environment limitation.

The checker depends on Node filesystem/process support; its tests additionally need Bun and a `node` executable. These are deterministic command observations, not a new Codex tool binding or a claim of universal workflow compliance or observed installation. Original upstream helpers were read, never executed; both immutable source baselines remain intact. Complete package provenance and repository checks validate the source mappings and reviewed additions separately.
