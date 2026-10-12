---
name: pstack-setup-pstack
description: Configure pstack native GPT model roles and separate reasoning budgets. Explicit setup or model-budget changes.
---

# Setup pstack

Read [compatibility](../../references/compatibility.md), [models](../../references/models.md) and [delegation](../../references/delegation.md). Configure recipient settings, preserving role distinctions and validating the actual runtime.

1. Detect exposed spawn operations, entitled native models, per-model efforts and override constraints. Record evidence and missing capabilities. Request choices when enumeration is unavailable; a user-supplied name alone does not establish host support.
2. Ask the recipient to use the project-local `.pstack/models.json` default or name another owned settings location. Read existing state. Show the recorded budget and choices; without a file start with inherited models, two-entry panels, and `large` target reasoning. List retired/unknown roles to be dropped on confirmation.
3. Ask budget using a supported question UI or ordinary chat. Offer the four exact budget labels in models.md. Preserve previously chosen model families, arrays and aliases on rerun; change supported real-model efforts according to that budget. Show all 17 roles, including defaults, panel counts, actual effort values and entries needing choice. Aliases keep parent reasoning; disclose that the budget cannot override those entries.
4. Let the user accept or change roles using detected native identities or inheritance aliases. Validate models and efforts independently, scalar/panel shapes and host override authority. Stop at unresolved selections; never write invalid model IDs. Explain absence of provider diversity and local-for-cloud execution.
5. After confirmation, write the schema in models.md to the selected file. Replace only pstack's configuration with the complete confirmed table for idempotence; preserve unrelated files/configuration. Report the path, budget, actual role values and that pstack reads it on each new workflow/dispatch rather than through a global always-applied rule. Keep personal settings out of shared package and commits.
6. Check for a project `verify-*` skill or real-app harness. If absent, offer once to generate a project-local verification skill with the bundled pstack-create-verification-skill entry, reading its instructions if accepted and present. If unavailable, report the missing entry; do not invent a Skill tool. On decline, continue without pushing.

Completion requires a confirmed valid configuration or an exact unresolved capability/choice report. Setup does not install the plugin, change account settings or authorize subsequent engineering work.
