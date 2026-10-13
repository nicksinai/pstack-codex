---
name: pstack-interrogate
description: Review code through independent adversarial panels and return an evidence-based lead verdict without applying changes.
---

# Interrogate

Invoke `$pstack-interrogate` with a diff, files, or recent-work scope. Read [delegation](../../references/delegation.md) and [models](../../references/models.md). This workflow explicitly requests independent local reviewers. Spawn one reviewer per configured seat with the same prompt, intent, code, rubric and code-quality lens. Independent contexts and separately validated GPT selections preserve independent attempts; the upstream cross-provider adversarial signal from Claude/Grok is absent. Repeated inherited GPT seats are allowed and are disclosed, never described as provider diversity. Use no assigned personas.

The deliverable is a synthesized verdict. Do NOT auto-apply changes.

## Step 1, Scope

Identify what to review from context:

- If the user points at specific files or a diff, use that.
- If on a feature branch, run `git diff main...HEAD` (or the appropriate base branch) for the full changeset.
- If the user's message references recent work, gather the relevant files.

Package the diff or file contents with any surrounding context files the reviewers need to understand the code.

## Step 2, Intent

Before spawning reviewers, state the intent in one clear paragraph from the user's message, commit messages, the PR description if one exists, and the code. If you're unsure about the intent, ask the user before proceeding.

## Step 3, Spawn Reviewers

Resolve the `interrogate reviewers` panel through models.md, one fresh reviewer per entry, extending or shrinking Reviewer A/B labels to the seat count. Defaults are two inherited native GPT seats. Record actual model/effort where observable; otherwise identify inheritance honestly. Validate identities and efforts separately against the host; obtain a valid replacement for rejected entries, retaining aliases as inheritance. Do not guess model slugs, install providers, or open an unrelated configuration PR.

Launch the reviewers asynchronously in bounded concurrent batches using supported spawn/result operations. Every reviewer is read-only and receives its own fresh context; read-only scope is an instruction unless the host enforces it. They may share immutable source, but see neither other findings nor the lead's preferred verdict. Freeze review scope at an exact base/head SHA or file snapshot, include enough surrounding code to trace real callers, and identify dirty changes explicitly. Missing reviewers are recorded as coverage gaps; a dropout is not consensus. The lead waits for every launched reviewer's terminal state before the final verdict. Missing required delegation support is BLOCKED, never a simulated panel.

Read [reviewer prompt](references/reviewer-prompt.md) and fill in the template with:

1. The stated intent
2. The diff or file contents
3. The review rubric from [review rubric](references/rubric.md)
4. The code-quality lens from [code-quality lens](references/code-quality-review.md)

The same filled template goes to all reviewers, so every model applies the code-quality lens.

## Step 4, Synthesize

As results come back, parse every reviewer's findings. Merge findings about the same issue and note which models raised each. Agreement by two or more independent reviewers is a high-signal input. Identify repeated-model seats; agreement is not independent provider confirmation and never substitutes for tracing the evidence. Read lone-model findings and weight them accordingly. Record disagreements, including a reviewer explicitly contradicting another finding.

## Step 5, Lead Judgment

You are the lead reviewer, a pragmatic senior engineer, not a neutral aggregator. Read [lead judgment](references/lead-judgment.md) for the full framework. Put every finding in one of four buckets, with the model(s) that raised it and a one-line rationale.

- **Act on**. Real issues affecting correctness, security, or maintainability given the actual goals. These would block a real PR.
- **Consider**. Legitimate, but you're not sure they outweigh the cost of addressing them now. Worth the user's attention.
- **Noted**. Technically valid but not actionable. Context-dependent, premature optimization, or low-impact given the current stage.
- **Dismissed**. Wrong, nitpicky, or missing context. Brief explanation why.

## Output Format

### Intent
> [The stated intent paragraph from Step 2]

### Reviewers
- Reviewer [label]: [observed model/effort or inherited selection], [N findings], [complete/dropout/blocked] (one bullet per reviewer; disclose repeated models and absent provider diversity)

### Act On
[Each: description, which models raised it, why it matters.]

### Consider
[Each: description, which models raised it, the tradeoff.]

### Noted
[Brief list.]

### Dismissed
[Each with a brief rationale.]

### Agreement Map
[Where models agreed and diverged, and what that pattern tells us.]
