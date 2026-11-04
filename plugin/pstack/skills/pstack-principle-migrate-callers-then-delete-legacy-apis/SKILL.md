---
name: pstack-principle-migrate-callers-then-delete-legacy-apis
description: "Apply when introducing a new internal API while old callers still exist."
---


Resolve named skills through the [mode lookup](../pstack-poteto-mode/SKILL.md). The [compatibility contract](../../references/compatibility.md) and current user/host authority govern any delegated, durable or external action.

# Migrate Callers Then Delete Legacy APIs

- Update tests to assert the new contract, and delete tests that only protect pre-refactor implementation details

**When this applies:**
- No external users depend on backward compatibility
- The project can absorb coordinated breaking changes
- The new API is part of a simplification or refactor initiative
