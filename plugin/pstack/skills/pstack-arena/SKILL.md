---
name: pstack-arena
description: Produce independent competing artifacts, cross-judge them, select a base, graft strengths and verify the synthesis.
---

# Arena

Fan out N parallel attempts at the same task. Read every candidate end to end. Pick the strongest as the base. Graft the best ideas from the others into it. Verify the synthesized result.

## Entry and execution

Invoke `$pstack-arena` with the artifact task. Read [delegation](../../references/delegation.md) and [models](../../references/models.md). This workflow explicitly requests local parallel delegation. Bind to actual host operations and capacity before dispatch. Give every code writer its own declared worktree/branch and runtime resources; output-only writers get unique directories. Supply identical tasks and grounding, keep candidates unaware of each other's output, and let each finish before cross-judging. Independent GPT contexts retain attempt isolation; they do not reproduce Claude/Grok provider diversity.

## Start

Open a todolist, or a visible local checklist if unavailable, with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Cross-judge
4. Pick
5. Graft
6. Verify

## Phase A: Frame

The N candidates will receive the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric. State what success looks like for *this* task, then turn it into 3-6 concrete gradeable criteria. The rubric is the picker's tool in Phase D. Candidates only see the task.
3. Pick the runners. Resolve every seat in `arena runners` through models.md, unless architect supplies its own panel. Defaults are two inherited native GPT seats. Preserve alias and repeated-entry count. Spawn more when the arena covers multiple design directions. The same model N times remains suitable for generation-bound work. Validate real models and separate efforts against the current host; report rejected selections and obtain supported replacements. No external provider or guessed slug fallback.
4. Assign separate output locations under delegation.md. Record exact base commit, output/worktree location, branch and runtime resource ownership before launch. A candidate must inspect its assigned cwd and branch before writing.

## Phase B: Fan out

Dispatch all N subagents asynchronously in bounded concurrent batches through the actual host spawn operation, each with the same task, the path to shared grounding, its own output path, and instructions to produce both artifact and short rationale. Keep the private picker rubric out of the candidate brief. Queue seats beyond current capacity; concurrency is not the total candidate count. Missing parallel spawn/result support blocks this workflow rather than turning it into a fabricated single-agent panel.

Each rationale names the alternatives the candidate considered and what it rejected.

If a candidate fails to produce output, proceed with N-1 and note the dropout in the synthesis record.

## Phase C: Cross-judge

After all Phase B candidates reach terminal state, choose one validated model from `arena cross-judge pool` through models.md. Defaults are inherited native GPT choices. Prefer a different available model family from the parent's within the native GPT selection, while disclosing that provider diversity remains absent. Spawn one fresh read-only judge. It sees the rubric and complete artifacts by path label, scores each criterion, and recommends a base with rationale. Withhold other judges' views and model identities; shared prompts, not assigned personas, are the comparison basis. Run judging in parallel with the parent's reading in Phase D, never while candidates are still writing. Read-only is an instruction unless the host enforces a sandbox. If no candidate survives, report BLOCKED; with one survivor, note lost comparison and dropout rather than claiming competing-design evidence. Architect's two-distinct-design requirement still applies.

## Phase D: Pick a base

Read every candidate end to end before picking.

Score each candidate against the rubric criterion by criterion, not on holistic feel. Compare against the cross-judge. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base on which candidate a future maintainer can extend most easily without breaking invariants. Prefer the cleaner boundary or smaller API when two feel tied, per the Laziness Protocol.

Record the pick and the reason in a short synthesis note alongside the base artifact, including the cross-judge's verdict.

## Phase E: Graft

Walk each losing candidate once more and identify what is worth porting into the base. The signal is usually one or two things per candidate, not most of it.

Fold each graft in by hand, per the **redesign-from-first-principles** principle skill. Don't paste mechanically. The result has to remain coherent under one mental model.

Record what was grafted, from which candidate, and what was rejected and why.

When N candidates converge on the same shape, that is a strong agreement signal. Note the convergence in the record and ship the consensus shape. No graft is needed. When N candidates wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

The synthesized artifact has to hold up under the same scrutiny as any other output, per the **prove-it-works** principle skill.

If verification surfaces a problem the arena did not catch, either Phase A was wrong (re-frame and re-run) or one candidate caught it and you missed the graft (go back to Phase E). Don't paper over.

## Outputs

One synthesized artifact. One short synthesis note alongside, naming the base, the grafts (with source candidate), the rejections, the dropouts if any, and the verification result.
