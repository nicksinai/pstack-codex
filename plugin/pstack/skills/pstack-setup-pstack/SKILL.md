---
name: pstack-setup-pstack
description: "Configure which models pstack uses per role and at what reasoning budget."
---

# Setup pstack

Read [compatibility](../../references/compatibility.md), [models](../../references/models.md) and [delegation](../../references/delegation.md). Configure recipient settings, preserving role distinctions and validating the actual runtime.

1. Detect exposed spawn operations, entitled native models, per-model efforts and override constraints. Record evidence and missing capabilities. Request choices when enumeration is unavailable; a user-supplied name alone does not establish host support.
2. Ask the recipient to use the project-local `.pstack/models.json` default or name another owned settings location. Read existing state. Show the recorded budget and choices; without a file start with inherited models, two-entry panels, and `large` target reasoning. List retired/unknown roles to be dropped on confirmation.
3. Ask budget using a supported question UI or ordinary chat. Offer the four exact budget labels in models.md. Preserve previously chosen model families, arrays and aliases on rerun; change supported real-model efforts according to that budget. Show all 17 roles, including defaults, panel counts, actual effort values and entries needing choice. Aliases keep parent reasoning; disclose that the budget cannot override those entries.
4. Let the user accept or change roles using detected native identities or inheritance aliases. Validate models and efforts independently, scalar/panel shapes and host override authority. Stop at unresolved selections; never write invalid model IDs. Explain absence of provider diversity and local-for-cloud execution. The `arena cross-judge pool` is an ordered candidate list for one judge. Only validated entries from a model family other than the parent qualify, tried in list order. `auto` and `inherit-parent` never judge. A GPT-only pool does not establish cross-family diversity; if no eligible family exists, Arena skips cross-judging and discloses that gap under its own contract.
5. After confirmation, write the schema in models.md to the selected file. Replace only pstack's configuration with the complete confirmed table for idempotence; preserve unrelated files/configuration. Report the path, budget, actual role values and that pstack reads it on each new workflow/dispatch rather than through a global always-applied rule. Keep personal settings out of shared package and commits.
6. Check for a project `verify-*` skill or real-app harness. If absent, offer once to generate a project-local verification skill with the bundled pstack-create-verification-skill entry, reading its instructions if accepted and present. If unavailable, report the missing entry; do not invent a Skill tool. On decline, continue without pushing.
7. Check whether the project has a formal verification skill that runs a model checker, a proof, or another verifier against its code. If absent, offer once to generate a project-local skill that proves a key property in every case in scope, beyond the cases tests reach. On acceptance read and invoke [create-formal-verification-skill](../pstack-create-formal-verification-skill/SKILL.md); on decline move on without pushing. An unavailable entry remains an explicit missing dependency.

Completion requires a confirmed valid configuration or an exact unresolved capability/choice report. Setup does not install the plugin, change account settings or authorize subsequent engineering work.
