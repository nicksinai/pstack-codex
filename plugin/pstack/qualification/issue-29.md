# Issue #29 qualification: investigation, writing and principle review

Implements issue #29 under specification #20. Reviewed official pstack 0.15.23 at `dbf49813a39c1a5389c5e28cb8e4c1c2379e2454` against 0.15.15 at `d0ef80d86795816da932a153458c5dbe192d294e`. Both immutable archives and manifests are unchanged. Scope is exactly the 31 primary source files below, plus preservation review of #25's root-cause addition. Engineering workflow sources owned by #28 are untouched.

## Evidence and capability boundary

These are established instruction/source properties, not observed workflow runs. The [capability record](capabilities.md), [compatibility](../references/compatibility.md), [delegation](../references/delegation.md), [history](../references/history.md), and [source access](../skills/pstack-why/references/source-access.md) remain the actual portable bindings. Native subagent tools are exposed in this implementation host, but recipient controls, isolation, model/effort validity, capacity and connector availability must be inspected at invocation. No custom registered agent, Cursor Task tool, provider-diverse review or Cursor readonly-mode behavior is claimed. GPT-only local workers replace provider/cloud choices. Read-only instructions do not establish enforced sandbox isolation.

C7 worker and C8 history contracts are conditional: unavailable spawn/results block a required panel; unavailable exact transcript uses the scoped labeled digest fallback. C9 file/Git/forge/profiler access and source connector authentication/pagination/retention remain recipient premises; no documentation reference supplies an executable tool. Missing or partial source records remain evidence gaps, never successful searches. Exact active-chat/workspace identity and current artifacts govern scoped history and recovery; no unrelated transcript searches, recipient-global memory edits or private records are added. Explicit/sticky mode policy remains unchanged. No continuity through shutdown/sleep is claimed.

## Source and deletion accounting

Each section names the exact source and delivered counterpart. Ranges are zero-context source edit spans `old-start:count → new-start:count` from the two immutable archives, including metadata, additions and deleted lines. Wording edits are accepted only with the requirement correspondence below; retained spans keep useful substantive obligations or an already equivalent Codex binding. “Retained” does not mean upstream requirements were silently discarded. Where a combined hunk includes both shortening and a provider/path substitution, the paragraph states that distinction. The immutable archives plus these ranges permit reconstruction without embedding full upstream files in the package.

### `skills/how/SKILL.md`

Counterpart: [skills/pstack-how/SKILL.md](../skills/pstack-how/SKILL.md). Transition: **retained**.

Existing sections 1–4 already implement the revised simple/complex split, 2–4 angles, complete explorer-to-explainer handoff and light presentation edits. Retain that equivalent sequence rather than reintroducing Task/generalPurpose, readonly flags or Grok/Claude defaults. Compatibility, delegation and models links bind native read-only workers, capacity, missing slices and fresh synthesis. The removed per-step spawn listings are consolidated in those shared contracts; no worker or prerequisite disappears.

Source edit spans: `11:1 → 11:1`; `13:1 → 13:1`; `17:2 → 17:2`; `22:1 → 22:1`; `24:1 → 24:1`; `26:3 → 26:1`; `30:1 → 28:1`; `32:1 → 30:1`; `34:1 → 32:1`; `36:21 → 34:1`.

### `skills/how/references/explorer-prompt.md`

Counterpart: [skills/pstack-how/references/explorer-prompt.md](../skills/pstack-how/references/explorer-prompt.md). Transition: **retained**.

Retain all three deletions. The opening assigns factual exploration rather than human-facing prose. Exploration Instructions retain finding the entry point, reading the full call chain and data transformations, reading types/abstractions, tracing subsystem inputs/outputs and finding non-obvious behavior. The cannot-trace gap instruction and precise paths/functions/types/line output remain. Components/Flow/Boundaries/Open Questions headings alone would not require that traversal. Native file/symbol reads replace Glob/Grep/Read names.

Source edit spans: `6:2 → 6:0`; `19:13 → 17:0`; `33:2 → 18:0`.

### `skills/principle-build-the-lever/SKILL.md`

Counterpart: [skills/pstack-principle-build-the-lever/SKILL.md](../skills/pstack-principle-build-the-lever/SKILL.md). Transition: **adapted**.

Remove Why/Pattern/Balance labels, retaining their complete throughput/reviewability rationale, triviality threshold and smallest-script constraint. First hand unit, rerun-and-diff proof, safe reruns, produced artifact and commit requirement remain unchanged. Namespaced Laziness/Structure/Prove It links survive.

Source edit spans: `10:1 → 10:1`; `12:1 → 12:1`; `21:1 → 21:1`.

### `skills/principle-encode-lessons-in-structure/SKILL.md`

Counterpart: [skills/pstack-principle-encode-lessons-in-structure/SKILL.md](../skills/pstack-principle-encode-lessons-in-structure/SKILL.md). Transition: **retained**.

Retain the deleted recurring-fix obligation and rationale: mechanisms enforce without reader cooperation. Preserve repeat-instruction detection, encode-and-delete-prose branch, judgment fallback with failure example, and strongest-mechanism ordering: unrepresentable compile-time state → CI lint/banned API → canonical helper → runtime check. Keep structural-only corollary. Capture every correction, classify one-off/pattern, route note/skill-or-lint/principle, and apply now or create concrete todo. Keep anti-patterns acknowledging without recording, recording without routing and isolated fixes without generalization. The approved reflect gate and recipient-global-memory/configuration limits remain; learning signal grants no write authority.

Source edit spans: `9:11 → 9:1`; `22:10 → 12:0`.

### `skills/principle-exhaust-the-design-space/SKILL.md`

Counterpart: [skills/pstack-principle-exhaust-the-design-space/SKILL.md](../skills/pstack-principle-exhaust-the-design-space/SKILL.md). Transition: **retained**.

Retain deleted novel-interaction/architecture trigger, cost rationale, 2–3 genuinely different prototypes/sketches, side-by-side comparison before commitment and all applicability branches. Product feel remains one branch alongside novel UI and architecture; mechanical established patterns, clear bug/refactor targets and single viable constraints remain exceptions. The new isolated “also applies” sentence cannot replace the rule it presupposes.

Source edit spans: `9:13 → 9:1`.

### `skills/principle-explain-the-number/SKILL.md`

Counterpart: [skills/pstack-principle-explain-the-number/SKILL.md](../skills/pstack-principle-explain-the-number/SKILL.md). Transition: **adapted**.

Condense rationale into the three actionable checks: independently profile/counter-observe the limiter and map it to source; reject errors, skipped/cached/unexecuted work, untuned defaults, noise and insignificant pieces; retain run count/spread/limiter beside the result. Deleted introductory claim and plausible-number examples are covered by those checks. “Reader can check” is realized by keeping the linked evidence, not a removed evidence gate. Benchmark and eval linkage and the no-count/spread/limiter failure condition remain. Prove It distinction loses only a repeated definition.

Source edit spans: `9:9 → 9:3`; `23:1 → 17:1`.

### `skills/principle-guard-the-context-window/SKILL.md`

Counterpart: [skills/pstack-principle-guard-the-context-window/SKILL.md](../skills/pstack-principle-guard-the-context-window/SKILL.md). Transition: **retained**.

Retain finite-context warning and both deleted mechanisms: isolate large payloads in workers with coordinator summaries, and keep every-invocation templates/references inline. These prescribe allocation and placement rather than merely explain context. Phase sizing, file limits, turn budgets and mechanism costs remain. Delegation capacity and authority are still governed by the shared header.

Source edit spans: `9:2 → 9:0`; `14:2 → 12:0`.

### `skills/principle-laziness-protocol/SKILL.md`

Counterpart: [skills/pstack-principle-laziness-protocol/SKILL.md](../skills/pstack-principle-laziness-protocol/SKILL.md). Transition: **retained**.

Retain least-code/complexity objective, deletion-first preference, flat hierarchy with rich-interface exception and >3-file/layer diagnostic, questioning cross-layer signal threading, removing tiny pass-throughs/leaks/duplicated choices and human maintainability test. Consolidated decisions and minimum diff remain. The two surviving upstream bullets do not cover these deleted decision rules.

Source edit spans: `9:4 → 9:0`; `15:4 → 11:0`.

### `skills/principle-minimize-reader-load/SKILL.md`

Counterpart: [skills/pstack-principle-minimize-reader-load/SKILL.md](../skills/pstack-principle-minimize-reader-load/SKILL.md). Transition: **adapted**.

Merge the two independent axes and rationale into the introduction: layers to trace, state to hold, metric proxies, 50 globals versus 6-layer stack and finite reader memory all survive. Remove only Pattern label and repeat explanation. Layer compression, abstraction change, meaningful interfaces, scoped/pure state, boundary invariants, balancing added load and the 30-second reader check remain in the body; namespaced context link survives.

Source edit spans: `9:3 → 9:1`; `13:3 → 11:0`; `21:1 → 16:1`; `23:1 → 18:1`.

### `skills/principle-model-the-domain/SKILL.md`

Counterpart: [skills/pstack-principle-model-the-domain/SKILL.md](../skills/pstack-principle-model-the-domain/SKILL.md). Transition: **adapted**.

Keep portable principle description rather than upstream explicit-only metadata changes. Merge invalid-state/branch reduction and write-time rationale into opening; “scattered booleans/repeated shape assumptions” is retained by state-machine/typed-model/map bullets. Typed object/model becomes typed model, graph/tree becomes graph, tree with unchanged choices. Module ownership, data-access shape, invariant discovery and no-forced-abstraction boundaries survive.

Source edit spans: `3:1 → 3:1`; `9:1 → 9:1`; `11:3 → 11:1`; `16:1 → 14:1`; `21:1 → 19:1`.

### `skills/principle-never-block-on-the-human/SKILL.md`

Counterpart: [skills/pstack-principle-never-block-on-the-human/SKILL.md](../skills/pstack-principle-never-block-on-the-human/SKILL.md). Transition: **adapted**.

Keep portable description. Merge reversible/reviewable cost rationale into opening and remove labels; retain all five bullets: proceed/present, log/self-heal, confirmation for irreversible actions including external messages, reversible work, and human product direction. Deleted bottleneck sentence explains the retained proceed rule. The compatibility/current-authority header still scopes reversible actions; this principle cannot override reflect approval or a user restriction.

Source edit spans: `3:1 → 3:1`; `9:1 → 9:1`; `11:10 → 11:5`.

### `skills/principle-redesign-from-first-principles/SKILL.md`

Counterpart: [skills/pstack-principle-redesign-from-first-principles/SKILL.md](../skills/pstack-principle-redesign-from-first-principles/SKILL.md). Transition: **adapted**.

Keep portable description; replace “there from the start” with “foundational assumption from the start”. Affected-file reads, greenfield redesign question and broader existing steps remain. Description shortening cannot remove discovery because mode lookup and existing invocation policy remain.

Source edit spans: `3:1 → 3:1`; `9:1 → 9:1`.

### `skills/principle-subtract-before-you-add/SKILL.md`

Counterpart: [skills/pstack-principle-subtract-before-you-add/SKILL.md](../skills/pstack-principle-subtract-before-you-add/SKILL.md). Transition: **adapted**.

Merge opening and default-to-subtraction; remove causal exposition about complexity compounding and Pattern label. Removal-before-construction, minimum-before-polish, observed-usage constraint and continually simpler same/smaller interface remain explicit, so sequence and scope survive.

Source edit spans: `9:3 → 9:1`; `15:1 → 13:0`.

### `skills/principle-test-behavior-not-implementation/SKILL.md`

Counterpart: [skills/pstack-principle-test-behavior-not-implementation/SKILL.md](../skills/pstack-principle-test-behavior-not-implementation/SKILL.md). Transition: **adapted**.

Keep portable description and strengthen the subject-result check to reject undefined OR a wrong value. Condense five anti-pattern classes while retaining omitted diagnostics toBeInstanceOf, toHaveLength(0), not.toBe(wrongValue), self-referential expectation, constant/config/table/prompt pins and fixture-only assertions. Retain literal observable output/effect, mock payload OR resulting state, presence on other input in the same test, mechanism-over-constant check and deletion when no observable assertion exists. The slugify worked example is omitted because the explicit concrete-input/literal-output rule remains; CI-cost rationale is explanatory. Relation checks and compile-time test-d.ts exceptions remain.

Source edit spans: `3:1 → 3:1`; `9:1 → 9:1`; `11:1 → 11:1`; `13:1 → 13:5`; `15:1 → 19:1`; `17:9 → 21:1`.

### `skills/principle-type-system-discipline/SKILL.md`

Counterpart: [skills/pstack-principle-type-system-discipline/SKILL.md](../skills/pstack-principle-type-system-discipline/SKILL.md). Transition: **adapted**.

Retain all eight patterns and fold each removed diagnostic into its corresponding bullet: optional-field validity → sum types; equal primitives/different meanings → branding; any/as/assertNotNull → boundary validation; new variant → exhaustive compiler failure; duplicate shape → derive authoritative schema; no partial operation → keep plain type. Construction examples nonempty list and time range remain; remove even-length pairs illustration and redundant refinement explanation, covered by choose-a-shape-that-cannot-build-illegal-value. Keep payload variants, total-function sum/head examples, validated semantic primitives, external boundary parsing, casts-as-hazards and language exhaustiveness idioms. Removed language-specific branding examples are replaced by own semantic type/newtype; no type-system capability is claimed for an untyped language.

Source edit spans: `9:1 → 9:1`; `11:21 → 11:8`.

### `skills/reflect/SKILL.md`

Counterpart: [skills/pstack-reflect/SKILL.md](../skills/pstack-reflect/SKILL.md). Transition: **retained**.

Retain existing equivalent six-step scoped Codex implementation: exact current-chat identity/export or labeled digest, three independent lens reviewers, fresh complete synthesis, structural check, full Accepted/Rejected/Backlog presentation and explicit approval before edits, routing and accurate reply. Deleted headings/explanations are already compressed here. Cursor transcript layout/search command and readonly:false/Task/model defaults are deliberately substituted by history/context/delegation/models contracts. Automatic Backlog filing stays conditional on configured tracker, authority and access, with unfiled drafts/blockers otherwise; no invented tracker or write authority. Approved substantive/new/description edits use the authoring companion rather than Cursor create-skill. Available validator or disclosed direct checks remain. Global cache and private-data boundaries remain stronger than source.

Source edit spans: `11:2 → 11:0`; `15:1 → 13:1`; `17:3 → 15:1`; `25:1 → 21:1`; `27:1 → 23:1`; `29:3 → 25:1`; `43:1 → 37:1`; `45:1 → 39:1`; `47:1 → 41:1`; `49:1 → 43:1`; `51:1 → 45:1`; `53:1 → 47:1`; `55:1 → 49:1`; `57:1 → 51:1`; `59:1 → 53:1`; `64:1 → 58:1`; `66:1 → 60:1`.

### `skills/reflect/references/divergent-reviewer.md`

Counterpart: [skills/pstack-reflect/references/divergent-reviewer.md](../skills/pstack-reflect/references/divergent-reviewer.md). Transition: **adapted**.

Retain the opening read-only lookup restriction and context adapter. Consolidate used-skill evidence into native file reads, explicit delegation path or matching documented tool calls, replacing Cursor paths/Task/Read names. Preserve both valid routes (used skill body gap; catalog-visible missed trigger → tune description), reject neither-used-nor-missed candidates, exact transcript evidence, contrarian principle, routing and drift/trivial/already-covered filters. The removed canonical-missed-trigger explanation is carried by the explicit second route. No lookup scope widens.

Source edit spans: `5:1 → 5:1`; `21:1 → 21:1`; `23:3 → 23:3`; `27:1 → 27:1`; `29:6 → 29:1`; `37:1 → 32:1`; `39:1 → 34:1`.

### `skills/reflect/references/judgment-reviewer.md`

Counterpart: [skills/pstack-reflect/references/judgment-reviewer.md](../skills/pstack-reflect/references/judgment-reviewer.md). Transition: **adapted**.

Retain opening read-only lookup restriction and context adapter. Consolidate three usage signals into native reads/delegation/documented calls, preserving two valid finding routes and explicit tune-description exception, reject-neither condition, principle/evidence/routing fields and drift/trivial/already-covered filters. Cursor path and tool syntax are substituted, not runtime claims. Deleted list setup and repetition are fully represented in the consolidated scope paragraph and two route bullets.

Source edit spans: `3:1 → 3:1`; `20:1 → 20:1`; `22:3 → 22:3`; `26:1 → 26:1`; `28:6 → 28:1`; `36:1 → 31:1`; `38:1 → 33:1`.

### `skills/reflect/references/synthesizer.md`

Counterpart: [skills/pstack-reflect/references/synthesizer.md](../skills/pstack-reflect/references/synthesizer.md). Transition: **adapted**.

Shorten only skill-was-used and already-covered criteria: invoked or genuine missed trigger remains required, otherwise skill-not-used rejection. Target read precedes body acceptance; clear existing guidance yields already-covered; buried/weak guidance permits wording/placement repair rather than duplication. The removed “so it triggers next time” repeats tune-description purpose. All other criteria and exact Accepted/Rejected/Backlog output remain.

Source edit spans: `21:2 → 21:2`.

### `skills/reflect/references/tooling-reviewer.md`

Counterpart: [skills/pstack-reflect/references/tooling-reviewer.md](../skills/pstack-reflect/references/tooling-reviewer.md). Transition: **adapted**.

Retain read-only restriction and context adapter. Merge self-sufficiency introduction and per-moment lead-in without losing every manually supplied fetchable context check or principle/evidence/routing fields. Consolidate usage signals using native file-read/delegation calls; retain used-body and missed-trigger routes, reject neither, all concrete technical/evidence/routing fields and trivial/drift filters. “Convention generalizes, pinned details do not” remains. Cursor paths/Task syntax are deliberately replaced.

Source edit spans: `3:1 → 3:1`; `9:3 → 9:1`; `33:1 → 31:1`; `35:3 → 33:3`; `39:1 → 37:1`; `41:6 → 39:1`; `49:1 → 42:1`; `51:1 → 44:1`.

### `skills/technical-writing/SKILL.md`

Counterpart: [skills/pstack-technical-writing/SKILL.md](../skills/pstack-technical-writing/SKILL.md). Transition: **adapted**.

All four layers remain as headings and full rules: document compass, reader address, sentence load and ambiguity. Remove introductory preview and repeated teacher/persona, teaching-pause, reference-generation-reliability, condition-skip, ing-ambiguity and plain-language-reader rationales; their learner-visible steps, one-clause/link limit, generate-from-code, condition-first, ing avoidance and no-idiom rules remain. Keep rhythm, one thought, tone, rule exception, concrete symbols, clarity over word count, one name and no churn. Removed final “real symbols” duplicates the earlier authoritative-symbol rule. Counts still require regeneration commands; product strings use product guidelines.

Source edit spans: `9:1 → 9:1`; `15:1 → 15:1`; `23:1 → 23:1`; `25:1 → 25:1`; `41:1 → 41:1`; `43:1 → 43:1`; `45:1 → 45:1`; `56:1 → 56:1`; `74:1 → 74:1`; `82:1 → 82:1`; `88:2 → 88:2`; `96:1 → 96:1`.

### `skills/unslop/SKILL.md`

Counterpart: [skills/pstack-unslop/SKILL.md](../skills/pstack-unslop/SKILL.md). Transition: **adapted**.

Keep portable description/invocation metadata. Merge scan→rewrite steps into opening while retaining meaning and intended tone. Adopt plain imperative rewrites for is/has, natural group count, colons, quotes, filler and adverbs. Parenthetical jargon replacements preserve every listed term and concrete substitution; final plain-word mapping retains utilize/leverage/facilitate/numerous/in-the-event-that. All 33 pattern rules and exceptions remain; “Must always apply” metadata removal does not silently change this port's discovery policy.

Source edit spans: `3:1 → 3:1`; `9:6 → 9:1`; `28:1 → 23:1`; `30:1 → 25:1`; `37:1 → 32:1`; `42:1 → 37:1`; `51:1 → 46:1`; `57:1 → 52:1`; `64:2 → 59:2`.

### `skills/why/SKILL.md`

Counterpart: [skills/pstack-why/SKILL.md](../skills/pstack-why/SKILL.md). Transition: **adapted**.

Merge companion opening and code-anchor recipe while retaining all exact git blame/log/follow/message and gh body/comment/review commands, file/line/symbol/commit/PR/ticket context and handoff to every investigator/synthesizer. Preserve all seven categories, endpoint ownership, capacity/queueing and full coverage. Repeated upstream model/spawn paragraphs are replaced by native delegation/models/source-access; no Grok/Claude slug or readonly:false promise is imported. Skips remain written unavailable/provably irrelevant only; trivial-inline still requires seven-category redundancy. Preserve defensive incident prompt, complete findings/nulls, fresh synthesis, confidence-language protection, exact output/coverage and Preserve/Change/Avoid/Risk. Reference index is retained to keep explicit links reachable.

Source edit spans: `9:3 → 9:1`; `14:0 → 12:2`; `21:1 → 21:1`; `27:1 → 27:1`; `29:4 → 29:1`; `34:27 → 31:1`; `78:1 → 49:1`; `80:1 → 51:4`; `82:4 → 56:1`; `87:6 → 58:1`; `94:19 → 60:7`; `116:1 → 70:1`; `118:2 → 72:2`; `125:7 → 79:1`; `133:1 → 81:1`; `140:1 → 88:1`; `144:1 → 92:1`; `146:1 → 94:1`; `151:8 → 99:0`.

### `skills/why/references/epistemics.md`

Counterpart: [skills/pstack-why/references/epistemics.md](../skills/pstack-why/references/epistemics.md). Transition: **adapted**.

Retain initial code-versus-intent warning. Merge examples into all five tiers with original meaning and phrasing: Direct textual author statement, Supported convergent indirect cited items, Inferred hedged interpretation/chain, Speculative marked thin-evidence alternatives, Unknown actual searched gap. Preserve immediately adjacent citations for confidence words, inference hedges and words-to-avoid. Rationalization, copy-paste versus intention, absence≠absence-of-concern, user hypothesis challenge, contradiction-with-both-citations, and concrete question/sources/queries/results gaps all remain. Calibration checklist becomes a paragraph requiring citation-or-reclassify, correct tier, no code-as-own-intent and gaps section. Removed missing-evidence benefit bullets become the opening sentence of that section.

Source edit spans: `3:3 → 3:1`; `9:1 → 7:1`; `13:1 → 11:1`; `15:8 → 13:1`; `26:1 → 17:1`; `28:6 → 19:1`; `37:1 → 23:1`; `39:5 → 25:1`; `47:1 → 29:1`; `49:5 → 31:1`; `57:1 → 35:1`; `59:1 → 37:1`; `63:1 → 41:1`; `65:1 → 43:1`; `67:23 → 45:1`; `97:1 → 53:1`; `99:6 → 55:1`; `108:3 → 59:1`; `114:6 → 63:1`; `123:1 → 67:1`; `125:3 → 69:1`; `129:16 → 71:1`.

### `skills/why/references/investigator-prompt.md`

Counterpart: [skills/pstack-why/references/investigator-prompt.md](../skills/pstack-why/references/investigator-prompt.md). Transition: **adapted**.

Move broad-first, verbatim/location, exact queries, contradictions, counterfactual and partial-finding rules into Investigation Loop while preserving one-source scope, whole records, cross-source Additional Leads routing and raw-evidence-only role. “What You're Not Doing” is folded into Gather-don't-conclude and no-intent-from-behavior/style bullets: no final narrative, no picking contradiction sides, no unsupported hunch and no code-as-intent. All Source/Searched/Direct/Indirect/Contradictions/Gaps/Leads fields remain, including author/date, relevance, alternative readings and inference chain. Category and defensive incident prompt prerequisites remain.

Source edit spans: `3:1 → 3:1`; `7:1 → 7:1`; `9:12 → 9:1`; `45:1 → 34:1`; `47:1 → 36:6`; `49:8 → 43:1`; `60:3 → 47:3`; `64:0 → 51:1`; `67:1 → 55:1`; `73:1 → 61:1`; `76:1 → 64:1`; `83:1 → 71:1`; `86:1 → 74:1`; `90:1 → 78:1`; `93:1 → 81:1`; `96:8 → 84:1`.

### `skills/why/references/sources/code-archaeology.md`

Counterpart: [skills/pstack-why/references/sources/code-archaeology.md](../skills/pstack-why/references/sources/code-archaeology.md). Transition: **retained**.

Retain deleted substantive-commit PR body/review/comment/linked-issue fetch and all return fields: exact quote, hash/PR/file:line, author/date and direct/circumstantial. Retain good-evidence examples and pitfalls squash-merge lost history, misleading messages, copied-pattern origin, bot/backport motivation and code≠intent. Other wording changes only rename existing tests/changelog/ticket and command comments; deliberately retain old descriptions because no search reduction is justified. Git commands, source-access adapter and scope remain.

Source edit spans: `9:1 → 9:1`; `11:2 → 11:2`; `21:1 → 21:1`; `33:1 → 33:1`; `38:12 → 38:0`; `61:1 → 49:1`; `64:25 → 52:0`.

### `skills/why/references/sources/datadog.md`

Counterpart: [skills/pstack-why/references/sources/datadog.md](../skills/pstack-why/references/sources/datadog.md). Transition: **adapted**.

Condense runtime-source descriptions and rationale without deleting metrics/monitors/dashboards/APM/logs/incidents/notebooks. Dashboards/monitors-first and bounded-log-query rule remain; volume/timeouts are explanation only. Preserve correlation-versus-causation and neighboring PR check, human dashboard framing, retention gaps, service/tag/time narrowing with aggregation, instrumented≠caused and commit/PR cross-reference. All query examples/return fields survive under actual-schema source-access binding.

Source edit spans: `7:1 → 7:1`; `9:3 → 9:3`; `13:3 → 13:1`; `28:1 → 26:1`; `54:1 → 52:1`; `85:2 → 83:2`; `88:2 → 86:2`.

### `skills/why/references/sources/incident-postmortem.md`

Counterpart: [skills/pstack-why/references/sources/incident-postmortem.md](../skills/pstack-why/references/sources/incident-postmortem.md). Transition: **retained**.

Retain both deletions in full. Cross-cutting defensive angle applies inside each assigned source. Preserve Notion file/feature/error postmortem search; Linear incident/sev/action-item labels; Slack incident channels/dates; Git defensive/revert/reapply messages; Datadog formal incidents/timelines plus action-item dashboards/monitors; Sentry windows and target stacks; Databricks/warehouse error/retry counts and before/after correlation. Fetch full linked postmortem including Action Items; corroborate IDs/links across sources rather than infer causality from count drops. Preserve defensive-trigger/irrelevance bound. source-access requires scoped authenticated reads, schema binding and concrete unavailable/partial/empty gaps; removed named-source coverage is not waived by a missing connector.

Source edit spans: `3:3 → 3:0`; `9:7 → 6:0`.

### `skills/why/references/sources/sentry.md`

Counterpart: [skills/pstack-why/references/sources/sentry.md](../skills/pstack-why/references/sources/sentry.md). Transition: **retained**.

Retain source introduction with issue/event/release/replay/profile/comment/assignment evidence and temporal correlation rationale. Retain query component wording and first/last/release/frequency checklist as equivalent older wording. Preserve good-evidence examples and every deleted pitfall: grouping/fingerprint drift, releases with many commits, silent upstream fixes, resolved marker≠code-fixed, Seer hallucinations and sampling. Seer remains hypothesis/inference only; actual event/stack/timestamp is primary. Keep return fields and source-access schema/auth/gap binding.

Source edit spans: `2:13 → 2:0`; `33:1 → 20:1`; `42:5 → 29:1`; `70:18 → 53:1`.

### `skills/why/references/sources/slack.md`

Counterpart: [skills/pstack-why/references/sources/slack.md](../skills/pstack-why/references/sources/slack.md). Transition: **retained**.

Retain all four deletions. Source context distinguishes deliberation/incident/design/review/customer evidence and ephemeral/DM coverage. Search includes author/date, feature/symbol/misspellings/casual phrasing, PR URL, exact errors, engineering/project/incident/sev/team/design channels and whole relevant threads. Good-evidence examples prevent casual statements becoming decisions. Return channel, permalink/thread ID, participants, dates, attributed verbatim key quotes and thread/incident context. Keep retention/DM/auth/context-collapse pitfalls. source-access handles actual schema, pagination, compliant excerpts and scoped permissions; inaccessible full threads remain gaps.

Source edit spans: `2:11 → 2:0`; `19:1 → 8:0`; `22:15 → 10:0`; `45:10 → 18:0`.

### `skills/why/references/synthesizer-prompt.md`

Counterpart: [skills/pstack-why/references/synthesizer-prompt.md](../skills/pstack-why/references/synthesizer-prompt.md). Transition: **adapted**.

Condense prose while preserving full epistemics prerequisite, five tiers, adjacent Direct/Supported citations, inference/speculation language, code≠intent, independent hypothesis check and concrete gaps. Read all findings; merge overlap; surface both contradictions; calibrate every claim; spot-verify uncertain citations read-only. Exact output sections retain per-claim source, inference chain, competing hypotheses/for/against/confidence, unanswered questions, verbatim searched queries, unavailable sources/reasons and actual source coverage. Preserve confidence summary, seven-item revise-on-failure check and honest-useful final goal. source-access continues to override old “git/gh always expected” assumption with explicit access gap; no changed prose establishes connector access.

Source edit spans: `3:1 → 3:1`; `7:1 → 7:1`; `29:1 → 29:1`; `31:1 → 31:1`; `35:2 → 35:2`; `40:6 → 40:6`; `49:1 → 49:1`; `55:1 → 55:1`; `59:1 → 59:1`; `63:1 → 63:1`; `68:1 → 68:1`; `72:1 → 72:1`; `76:1 → 76:1`; `80:1 → 80:1`; `90:1 → 90:1`; `92:3 → 92:1`; `96:2 → 94:2`; `101:1 → 99:1`; `113:1 → 111:1`; `121:1 → 119:1`; `123:1 → 121:1`; `125:5 → 123:5`; `131:5 → 129:1`.

## Root-cause preservation and authority

Reviewed `skills/principle-fix-root-causes/SKILL.md` addition `20:0 → 20:1` delivered by #25 in [Fix Root Causes](../skills/pstack-principle-fix-root-causes/SKILL.md). Its deciding-fact deep-dig trigger still requires proposing a cheap ongoing signal with observation point and expected cost. Monitoring, recurring work and external messages still require applicable authorization. This slice does not change that file or reassign its primary source row from #25. Reproduction, why-chain, instrumentation, pattern search and restart-state rules remain. Structural learning continues to follow reflect approval and the current authority boundary.

## Validation record

Instruction changes use the user-confirmed complete packaged-plugin/source-backed review seam. No prompt-string tests or broad agent-behavior suite was added. Reviewed each old/new edit span above against its delivered counterpart for scope, prerequisites, ordering, evidence fields, skip/blocker behavior, approval and outputs. Updated only this ticket's transition rows and only adopted source ownership revisions; retained rows keep the original pinned source and existing ownership. Synchronized packaged inventories and regenerated adaptation evidence. Added this evidence file to the explicitly reviewed package allowlist.

Validation results are recorded after running existing provenance/package checks and monitor tests. No upstream helpers or plugin workflows were executed. No installation, publication, external messages, tracker mutation or personal configuration changes occurred. Whole-transition closure/versioning and reproducible final-release qualification remain #30's responsibility.

Checks passed: `python3 scripts/validate-provenance.py` (both immutable baselines, 31 owned transition rows completed; 226 reviewed package files at this pre-merge point); `python3 -B -m unittest discover -s tests -v` (7 existing fake-backed monitor tests); `python3 scripts/build-package.py --output-dir <external-build-directory>` (offline archive, 229 entries); authored-file `git diff --check`. The generated adaptation patch retains original upstream whitespace. No new runtime or probabilistic behavior evidence is claimed.
