# New skills qualification — upstream 0.15.36

Source: `poteto/pstack`, revision `bb68f2365eceafa0cb2d253112f675acf5f144cc`. The five skill descriptions and picker descriptions are contiguous excerpts from upstream descriptions. The shortened catalog entries keep the plugin within its description budget; complete upstream descriptions remain in the immutable baseline. Names, local links, and body invocation references use the Codex `pstack-` namespace; `agents/openai.yaml` requires explicit invocation.

## Source accounting

| Source | Codex destination | Disposition |
| --- | --- | --- |
| `pstack/skills/sharpen/SKILL.md` | `skills/pstack-sharpen/SKILL.md` | Workflow preserved; host invocation preface |
| `pstack/skills/create-formal-verification-skill/SKILL.md` | `skills/pstack-create-formal-verification-skill/SKILL.md` | Workflow preserved; project skill discovery and disposable broken-code check binding |
| `pstack/skills/maintain-formal-verification-skill/SKILL.md` | `skills/pstack-maintain-formal-verification-skill/SKILL.md` | Workflow preserved; project skill discovery and disposable broken-code check binding |
| `pstack/skills/ketchup-video/SKILL.md` | `skills/pstack-ketchup-video/SKILL.md` | Workflow preserved; concrete renderer and host media binding in `references/codex-rendering.md` |
| `pstack/skills/statechart/SKILL.md` | `skills/pstack-statechart/SKILL.md` | Workflow preserved; dependency preflight and executable view-module trust boundary |
| `pstack/skills/statechart/references/render.md` | `skills/pstack-statechart/references/render.md` | Byte-identical Pele rendering reference |
| `pstack/skills/statechart/scripts/**`, except `scripts/test/**` | `skills/pstack-statechart/scripts/**` | All 29 runtime/config files byte-identical; executable modes retained |
| `pstack/skills/statechart/scripts/test/**` | Immutable upstream baseline | All 376 test/corpus files retained for source audit and qualification, outside installed skill resources |

These rows account for all 411 files associated with the five additions. The 376 test files do not supply runtime capability. Runtime imports remain intact, and no upstream algorithm or verification bound was changed. The Codex-only additions are five picker metadata files, one video rendering reference, and this qualification record.

## Observed runtime checks

On macOS arm64 with Node 22.23.1, privately provisioned Temurin JRE 21.0.13, and TLC 1.7.4:

- Verified the TLC JAR against upstream's SHA-256 `936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88` before execution. Supplied `TLA2TOOLS` and `JAVA`; did not invoke the mise bootstrap or change global Java settings.
- Ran the distributed launcher on a three-state counter with a terminal stutter action. `Safe == x <= 2` exited 0 and reported `Safe, NoDeadlock` holding.
- Ran the same counter with `Safe == x <= 1`. It exited 1 and reported the shortest two-step path from Empty through One item to Two items. Mermaid, report, and raw TLC output were produced for both cases.
- Rendered both emitted Mermaid files with Pele 1.9.0 and the upstream options; both produced SVG. This checks renderer execution, not every chart shape.
- Reviewed bootstrap, subprocess, output staging, cleanup, and view import paths before running the helper. Supplied view modules execute code. Missing tools, inaccessible dependencies, and unsupported runtimes remain explicit blockers rather than verification passes.

The passing model proves only its bounded three-state property. It is qualification data, not a claim about a user's product. The create/maintain workflows still require their own real-code mapping, intentional break, counterexample replay, and sync-commit evidence on each target repository.

## Video contract check

Rendered a silent 960×540 H.264 MP4 at 24 fps with Pillow 13.0.0 and a privately provisioned FFmpeg 9.0 binary from imageio-ffmpeg 0.8.1. The two slides were drawn from the actual valid and broken counter reports, with a shared connected state diagram and a changed failure mark. They are diagrams, not invented product screenshots. The video has a dedicated subtitle strip and a half-second transition.

Decoded the final MP4, inspected a frame from each slide at 640×360, and confirmed legible subtitles with no overlap. Compared decoded frames with their settled-slide midpoint using a strict per-channel difference threshold; measured contiguous holds of 5.875 seconds and 3.917 seconds. These exceed the conservative added-word requirements of 17/3 and 11/3 seconds. This verifies an available local renderer path, frame extraction, and actual encoded timing, not universal availability of FFmpeg or host media embedding.

Private dependency paths, scripts, reports, rendered media, and detailed command logs remain outside the distributable. The installed skill discovers available renderers and follows upstream's failure response when none can satisfy the rendering contract. Publishing or sending media requires the user's instruction.

## Upstream test corpus

Ran the upstream TypeScript test corpus from a scratch copy with dependencies installed using `npm install --ignore-scripts`. The non-TLC checks passed after preserving the source directory layout and using a canonical macOS temporary directory; a logical `/var` versus `/private/var` path caused the initial symlink fixture failure. The render suite separately passed all 74 checks with Pele 1.9.0, Mermaid 11.16.0, and jsdom 26.1.0 in a private cache. Live corpus checks require `TLA2TOOLS`; configuration fuzzing also launches a Java source file and therefore requires a JDK, not just the JRE sufficient for the distributed runtime. These are test-environment requirements, not changes to the shipped runner.

The live TLC corpus trial ran 294 checks: 291 passed and the three setup failures described above failed. Targeted reruns resolved all three: the canonical temporary-directory launcher/symlink check passed, the complete render suite passed 74/74, and the 4,000-configuration seed-1 fuzz check passed with Temurin JDK 21.0.13. No failed assertion remains unresolved; this is a combination of the full trial and the targeted corrections, not a claim that the original trial was entirely green.
