---
name: pstack-arena
description: Produce independent competing artifacts, cross-judge them, select a base, graft strengths and verify the synthesis.
---

# Arena

## Entry and execution

Invoke `$pstack-arena` with the artifact task. Read [delegation](../../references/delegation.md) and [models](../../references/models.md). This workflow explicitly requests local parallel delegation. Bind to actual host operations and capacity before dispatch. Give every code writer its own declared worktree/branch and runtime resources; output-only writers get unique directories. Supply identical tasks and grounding, keep candidates unaware of each other's output, and let each finish before cross-judging. Independent GPT contexts retain attempt isolation; they do not reproduce Claude/Grok provider diversity.

## Start

Open a todolist, or a visible local checklist if unavailable, with one entry per phase (Frame, Fan out, Cross-judge, Pick, Graft, Verify) before launching anything.

## Phase A: Frame

Every candidate gets the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric, 3-6 concrete gradeable criteria for what success looks like on *this* task. It is the picker's tool in Phase D. Candidates only see the task.
3. Pick the runners. Resolve every seat in `arena runners` through models.md, unless architect supplies its own panel. Defaults are two inherited native GPT seats. Preserve alias and repeated-entry count. Spawn more when the arena covers multiple design directions. The same model N times remains suitable for generation-bound work. Validate real models and separate efforts against the current host; report rejected selections and obtain supported replacements. No external provider or guessed slug fallback.
4. Assign separate output locations under delegation.md. Record exact base commit, output/worktree location, branch and runtime resource ownership before launch. A candidate must inspect its assigned cwd and branch before writing.

## Phase B: Fan out

Dispatch all N subagents asynchronously in bounded concurrent batches through the actual host spawn operation, each with the same task, the path to shared grounding, its own output path, and instructions to produce the artifact and a short rationale naming the alternatives considered and rejected. Use the fresh-context/no-inherited-history operation required by delegation.md and a self-contained sanitized candidate brief. Keep the private picker rubric out of all candidate-accessible grounding and context. An inherited parent conversation leaks the rubric even when the brief omits it; missing context isolation blocks the private-rubric fan-out. Queue seats beyond current capacity; concurrency is not the total candidate count. Missing parallel spawn/result support blocks this workflow rather than turning it into a fabricated single-agent panel.

If a candidate produces no output, proceed with N-1 and note the dropout in the synthesis record.

## Phase C: Cross-judge

After all Phase B candidates reach terminal state, choose one validated model from `arena cross-judge pool` through models.md. Defaults are inherited native GPT choices. Prefer a different available model family from the parent's within the native GPT selection, while disclosing that provider diversity remains absent. Spawn one fresh-context read-only judge using the actual no-inherited-history operation and a sanitized stand-alone brief. A new agent ID with inherited parent history does not meet this requirement; missing context isolation blocks blinded judging. It sees the rubric and complete artifacts by path label, scores each criterion, and recommends a base with rationale. Withhold other judges' views and model identities; shared prompts, not assigned personas, are the comparison basis. Run judging in parallel with the parent's reading in Phase D, never while candidates are still writing. Read-only is an instruction unless the host enforces a sandbox. If no candidate survives, report BLOCKED; with one survivor, note lost comparison and dropout rather than claiming competing-design evidence. Architect's two-distinct-design requirement still applies.

## Phase D: Pick a base

Read every candidate end to end before picking. Score each against the rubric criterion by criterion, not on holistic feel, and compare with the cross-judge. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base a future maintainer can extend most easily without breaking invariants. When two feel tied, prefer the cleaner boundary or smaller API, per the Laziness Protocol.

## Phase E: Graft

Walk each losing candidate once more for what is worth porting into the base, usually one or two things per candidate, not most of it. Fold each graft in by hand, per the **redesign-from-first-principles** principle skill, so the result stays coherent under one mental model. Don't paste mechanically.

If the candidates converge on one shape, that is strong agreement. Note it and ship the consensus shape. No graft is needed. If they wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

Verify the synthesized artifact like any other output, per the **prove-it-works** principle skill. If verification finds a problem the arena missed, either Phase A was wrong (re-frame and re-run) or a candidate caught it and you missed the graft (go back to Phase E). Don't paper over it.

## Outputs

One synthesized artifact, with a short synthesis note alongside naming the base and why, the cross-judge's verdict, each graft with its source candidate, what was rejected and why, any convergence or dropouts, and the verification result.
