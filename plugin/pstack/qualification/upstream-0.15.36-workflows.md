# Existing workflow qualification for upstream 0.15.36

Source is the official `cursor/plugins` revision `bb68f2365eceafa0cb2d253112f675acf5f144cc`, compared with the retained 0.15.23 baseline. This argument covers existing workflows and helpers. New-skill qualification and the release inventory account for the other source files. Historical issue qualification remains historical where this update removes an entry point.

## Review and execution changes

| Source | Preserved behavior | Codex adaptation and evidence limit |
| --- | --- | --- |
| `skills/arena/SKILL.md` | Runner replacement restores the intended minimum; generation seats may repeat; judges start only after terminal candidates; unavailable other-family judge explicitly skips to parent selection; synthesis discloses dropouts and skipped judgment. | Native role validation replaces Cursor slugs. Different GPT variants are not other-family evidence. The GPT-only package explicitly skips Phase C rather than falsely claiming cross-family review. Candidate worktrees, fresh-context briefs and private rubric isolation remain required. |
| `skills/interrogate/SKILL.md` | Exact named scope or merge-base through working tree; restated intent; writable independent repro worktrees; executable failures only; coordinator reruns commands, merges roots, reports Intent/Findings/Dropped without applying fixes; skips Arena C/D/E. | Native general-purpose child operation replaces `generalPurpose`. Tracked and untracked scope inputs are copied deliberately. Command inspection, isolated reruns and host authority apply. Unavailable runtime is a disclosed verification limit, never a proven finding. |
| Removed `skills/interrogate/references/{code-quality-review,lead-judgment,reviewer-prompt,rubric}.md` | Upstream replaced rubric/lens review with executable adversarial evidence. | Removed packaged templates and active callers. Historical qualification links become historical path text. |
| `skills/poteto-mode/SKILL.md` | Changed principle triggers, task-dependent reasoning/speed and dependency-only Autopilot stacking. | Keeps explicit single-request/sticky scope, receiving-chat ownership, complete namespaced lookup, actual wrapper initialization and user/host authority. Adds five new skill routes. |
| `skills/principle-attack-the-premise/SKILL.md` | Test a falsifiable premise rather than requiring an actor-imbalance census. | Current upstream body with namespaced links and shared authority preamble. |
| `skills/principle-explain-the-number/SKILL.md` | Apply before measurement as well as before reporting or acting on it. | Current upstream body; measurable-work and evidence requirements retained. |
| `skills/principle-fix-root-causes/SKILL.md` | Locate the first wrong state; guards are fixes only for legitimate states. | Current upstream body and namespaced principle links. |
| `skills/principle-test-behavior-not-implementation/SKILL.md` | Assert user-observable behavior, tolerate internal redesign and omit low-value regressions. | Current upstream body and original examples; no artificial assertion requirement retained. |
| `skills/principle-type-system-discipline/SKILL.md` | Avoid type assertions through predicates and boundary parsing. | Current upstream body and links. |
| `skills/principle-make-operations-idempotent/SKILL.md` | Distinguishes unavoidable effect repetition and replay-safe convergence. | Three-way source merge preserves Codex preamble. |
| `skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md` | Updated small migration principle without the removed machinery. | Three-way source merge preserves namespace and authority. |
| `skills/correct/SKILL.md`, `skills/figure-it-out/SKILL.md` | Current upstream wording and workflow delta. | Three-way merge retains scoped invocation and bound shared references. |
| `skills/typescript-best-practices/{SKILL.md,references/patterns.md}` | Predicate-based branded primitive validation replaces the assertion example. | Source merge preserves the full examples and native links. |

## Executable helpers

| Source | Result and evidence |
| --- | --- |
| `skills/poteto-mode/scripts/check-plan.{mjs,test.ts}` | Upstream matching multi-backtick inline spans and regression cases merged. Existing fenced-block checks retained. |
| `skills/poteto-mode/scripts/watch-pr/{github.ts,github.test.ts,types.ts}` | Upstream fork identity prevents same-named fork heads entering repository stacks; owner-approval ACTION_REQUIRED gate is classified consistently on both read paths. Existing fail-closed pagination regressions retained. |
| `skills/poteto-mode/scripts/watch-pr/{policy.ts,policy.test.ts}` | Upstream timeout clamps each poll/retry sleep to remaining deadline; disabled deadlines preserve interval. Retained port pagination checks plus new deadline cases. |
| `skills/poteto-mode/scripts/package.json` | Removed obsolete orch test route. Retained locked dependency cache bootstrap. Explicit Bun compiler launcher avoids accidentally routing the locked TypeScript executable through an incompatible system Node. |
| Removed `skills/poteto-mode/scripts/orch/{orch.ts,store.ts,orch.test.ts}` | Removed packaged runtime; test was already source-only. Native orchestration contracts replace its callers. No new orchestration runtime added. |
| `skills/poteto-mode/scripts/worktree-audit.sh` | Retained reviewed Python read-only adapter and shell entrypoint. Python datetime/stat avoids upstream GNU/BSD flag differences by construction. Explicit authenticated GitHub reads remain the supported PR provider; this port does not claim upstream Origin CLI fallback. Unknown PR/activity state holds for review, no guessed integration or direct Cursor transcript scan, no deletion/ref mutation. |

The reviewed watcher launcher installed only locked dependencies with scripts disabled in a private temporary cache outside the package. Its `--help` completed. The cached current helper tests passed **76 tests, 194 assertions**, including deadline, fork identity, owner approval and retained pagination cases. `bun run typecheck` passed after using the explicit Bun compiler launcher. The first direct test attempt without a prepared dependency cache failed on missing Commander; the corrected cache execution is the successful qualification. These are deterministic helper checks, not a claim that live repository CI, merge operations or unattended deployment ran.

## Host capability boundary

The exposed collaboration schema provides spawn, terminal mailbox waiting, messaging, follow-up and interruption. `send_message` does not wake an idle child; `followup_task` does. `fork_turns` is parent-history inheritance, not cloning a running worker's state. Native GPT model identity and reasoning effort are separate fields; role configuration is validated against the invocation's schema, and no unsupported speed field or upstream slug is sent. Missing fields are disclosed rather than invented. A recipient may expose a different tool set; every operation is conditional on that actual binding.

The per-job model contract raises effort for difficult work, lowers it for judgment/routine work, preserves verification's configured worker settings, and reserves fast mode for urgency when the host actually exposes it. Native limitations do not weaken mandatory proof or owner boundaries. No tests here claim cross-provider diversity, cloud VM cloning, event subscriptions, durable unattended execution, or external-message authority.
