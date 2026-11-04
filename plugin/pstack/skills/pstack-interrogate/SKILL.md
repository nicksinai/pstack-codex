---
name: pstack-interrogate
description: "Multiple LLM reviewers challenge changes from independent angles."
---

# Interrogate

Adversaries try to break a change or a design. A finding survives only when a run proves it. Report the findings. Do not apply fixes.

## Frame

The scope is what the user names. Otherwise it is the branch diff from its merge base with the base branch, through the working tree. State the intent with [in-your-own-words](../pstack-in-your-own-words/SKILL.md), from the user's message, the commits, and the PR description. Ask the user when the intent is unclear.

## Fan out

Read [arena](../pstack-arena/SKILL.md), [delegation](../../references/delegation.md) and [models](../../references/models.md). This workflow explicitly requests parallel adversaries. Run arena Phase A steps 3 and 4 and Phase B, with four changes. Resolve the `interrogate reviewers` role through models.md in place of `arena runners`. Copy the scope's uncommitted changes into each worktree. Spawn each adversary with the actual supported native general-purpose worker operation and a self-contained fresh-context brief. Use a writable isolated worktree so it can build executable repros; never permit writes to another owner's worktree. Preserve tracked and untracked scope inputs when copying uncommitted changes, without copying secrets or unrelated files. Record the exact reviewed base, head and working-tree delta. Match effort and speed through models.md. In place of the arena task and rationale, give each adversary the scope, the intent, and this brief:

> Break this change. Prove each finding with a run against the real code, such as a failing test, a repro script, or command output that shows the wrong behavior. For a design or plan, run a prototype or probe the current tree. Keep repros in your own worktree. Report each finding with a title, the exact command, the output it printed, and the output the intent requires. Leave out anything you did not run. That covers style, naming, structure, and risks that need a future change to matter. No findings is a valid result.

## Verify

Verify each finding per arena Phase F by rerunning its command against the exact reviewed scope in an isolated verification location. Inspect the command before execution and respect user/host authority. An unavailable runtime does not prove a finding; report the verification limitation and drop the unverified claim. Keep a finding when the output shows the failure and the failure breaks the intent. Drop the rest. Merge findings that share a root cause.

Skip arena Phases C, D, and E. Adversaries find different failures, so the verdict keeps every verified finding, not one adversary's list.

## Output

- **Intent**: the restatement.
- **Findings**: for each verified finding, the command, its output, how it breaks the intent, and the adversaries that found it. Say "no verified findings" when none survive.
- **Dropped**: for each adversary, the count of dropped findings and why.
