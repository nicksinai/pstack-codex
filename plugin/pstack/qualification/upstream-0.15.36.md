# Port 0.2.0: upstream 0.15.36 qualification

Issue [#35](https://github.com/nicksinai/pstack-codex/issues/35) owns this update. The exact source is [cursor/plugins at bb68f2365eceafa0cb2d253112f675acf5f144cc](https://github.com/cursor/plugins/tree/bb68f2365eceafa0cb2d253112f675acf5f144cc/pstack), pstack 0.15.36. All 573 upstream files are retained unchanged in the repository's separately pinned archive; original 0.15.15 and predecessor 0.15.23 archives and prior ledgers remain intact. The transition has 412 additions, 68 changes and seven removals.

## Source disposition

The [active inventory](source-inventory.json) accounts for every current source file and the [transition](upstream-transition.json) accounts for every changed, added or removed path. All active source mappings use the current pin after byte comparison and requirement review; unchanged source requirements retain their established adaptations. The original qualification records remain historical evidence, not claims that removed targets are shipped.

The 13 established exclusions remain: Benny and make-bot-ui. The 376 files under statechart's upstream test directory remain review and test evidence in the raw archive, outside the installed runtime. The official Claude harness adapter is retained as reference evidence, since its tool names, installation commands, settings paths and permissive skip behavior are not Codex contracts. These 377 reference-only files have explicit null targets; none is silently dropped or counted as a delivered workflow. All 31 non-test statechart source files have installed counterparts.

The seven removed source files are four obsolete Interrogate review templates and three orchestration runtime files. The six formerly installed runtime/template targets are removed and their callers migrate to the new workflows. The orchestration test was already archive-only; its historical qualification target remains and is marked superseded. Removal validation checks the source transition, six target absences and the explicit historical test exception.

## Requirement and adaptation evidence

[Existing workflow qualification](upstream-0.15.36-workflows.md) covers executable-only Interrogate, Arena's explicit no-other-family fallback, native coordinator state and worker events, per-job model decisions, PR/autopilot verification policy, watcher behavior and revised principles. [New skill qualification](upstream-0.15.36-new-skills.md) covers sharpen, statechart, both formal verification generators and ketchup-video, including real runtime examples.

Upstream README and guide changes are represented in the package guide and linked workflow contracts: explicit one-request or sticky mode, expert prompt preparation without executing it, complete pending-decision catch-up, formal verification with bounded claims and negative controls, rendered statecharts, artifact-first verification, independently rerun review findings, independent PR branching and fresh verification after changes. Setup retains separate optional offers for app verification and formal verification. Model-checking results do not prove the entire implementation; generated workflows retain code reproduction and drift checks.

The two upstream manifests map to portable and Codex package metadata. Port version 0.2.0 is independent of upstream 0.15.36. Installation, namespace and host bindings are adapted; required workflow outcomes are preserved or their unavailable gates explicitly identified. Official Claude installation and auto-update instructions are not imported into Codex. Package guides retain recipient-specific installation and update checks.

Descriptions are exact upstream wording or contiguous excerpts. The validator checks both skill frontmatter and picker descriptions against each pinned source, with the historical source-backed deslop companion and Codex-specific updater accounted separately. Every skill requires explicit invocation through its metadata.

## Host limits

[Capability evidence](capabilities.md) records the official Codex skills/plugin documentation and inspected native collaboration schema. Local owned workers, actual control operations and private checkpoints substitute for Cursor-specific calls. No cloud clone, live-worker fork, provider diversity, durable scheduler, browser control or installed renderer is fabricated. GPT variants are one family. Arena uses upstream's documented judge-skip fallback when another family cannot run; other mandatory unavailable gates remain open. External messages require explicit user authorization.

The package is self-contained for instructions and bundled helper code. Java, TLC, JavaScript runtimes, renderer dependencies, Git/forge authentication, recipient app controls and actual local state remain runtime prerequisites. Dependency setup must respect the host's authority and keep caches/output outside the installed package. Local checks establish their named sample cases and content integrity, not universal future skill compliance or recipient installation.

## Integration checks

Integration passed the complete provenance validator: three immutable source archives, 573 accounted current files, all 487 transition outcomes resolved, 59 skill policies, 58 source-backed description pairs plus the Codex-specific updater, 7,834 catalog characters, 277 allowed package files and package-local dependency/link/privacy checks. The seven monitor lifecycle tests pass. A comparison with the exact official checkout reports zero upstream differences and no pending adaptation obligations.

Existing helper checks passed 76 tests with 194 assertions and strict typechecking. The integrated package's statechart launcher was rerun with the pinned TLC artifact: the valid case passed and the broken invariant failed with the expected two-step counterexample. The encoded video timing check was rerun against the final sample and passed both slide hold requirements. The new-skill ledger records test prerequisites, initial setup failures and corrected checks without presenting them as product failures or universal guarantees.

Two independently assembled offline archives compared byte-identically (280 entries). The build invokes the complete validator before assembly. `git diff --check` is applied to authored changes excluding the generated unified adaptation patch and immutable source archives, whose original whitespace is intentionally preserved. Installation and the actual desktop picker are separate shipping checks owned by the release coordinator.
