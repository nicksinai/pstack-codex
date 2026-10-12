---
name: pstack-how
description: Explain how code works, subsystem architecture, placement, ownership and layering through a source-backed walkthrough. Use why for motivation.
---

# How

Read [compatibility](../../references/compatibility.md), [delegation](../../references/delegation.md) and [models](../../references/models.md). This workflow explicitly requests bounded local read-only delegates. Use its specialized explorer/explainer prompts, not the full poteto-mode wrapper.

## 1. Assess complexity

State an interpretation and explore when scope is ambiguous. A single module, small utility or narrow function question uses the simple path; default to simple when unsure. A cross-file/service subsystem or architectural overview uses the complex path.

## 2. Explore or directly explain

For complex questions, divide into 2–4 distinct angles. Dispatch the explorer batch as concurrently as the established capacity permits, resolving `how explorer`. Build each brief from [explorer prompt](references/explorer-prompt.md), filling question and angle. Assign read-only scope and exact workspace, and require the prompt's context reads and findings. Reading workers need no writing worktrees. Drain all results, explicitly retaining dropouts and coverage gaps.

For simple questions, dispatch one `how explainer` that both explores and explains. Build its brief from [explainer prompt](references/explainer-prompt.md), omitting the explorer-findings section and changing the opening to direct exploration. Proceed to presentation after receiving its result.

## 3. Synthesize complex findings

After all explorer results arrive, dispatch one fresh `how explainer` with the question, every finding and explicit missing slices. Use the explainer prompt. It reconciles overlap, checks contradictions against source and fills gaps when possible. Remaining uncertainty stays visible; missing explorers cannot become inferred evidence.

## 4. Present

Present the explainer's result with light clarity/context edits; preserve its substance. Include applicable Overview, Key Concepts, How It Works, Where Things Live and Gotchas sections. Source paths/functions ground the mental model. Include helpful diagrams for actual multi-component flows and acknowledge gaps. This read-only workflow completes with an explanation, not code changes or a PR.
