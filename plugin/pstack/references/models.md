# Native role configuration

Read [compatibility](compatibility.md). The recipient chooses a repository-local, untracked settings file `.pstack/models.json`, or explicitly supplies another recipient-owned file. Read it at workflow entry and before every dispatch. Resolve the configured path from the active repository root, record it in the task ledger and continuation brief, and keep it outside the distributable. Setup changes no global or always-applied rule. Preserve unrelated settings; propose an ignore entry only when authorized to edit repository configuration.

## Roles and defaults

Preserve these exact upstream role labels:

- `feature, refactoring`
- `bug-fix`
- `perf-issue`
- `hillclimb`
- `judgment and prose`
- `hardest tasks`
- `how explorer`
- `how explainer`
- `why investigators`
- `why synthesizer`
- `reflect tooling`
- `reflect judgment, divergent, synthesizer`
- `arena runners`
- `arena cross-judge pool`
- `swarm workers`
- `architect runners`
- `interrogate reviewers`

Panel roles (`arena runners`, `architect runners`, `interrogate reviewers`) default to two entries; each entry, including repeated aliases, counts toward fan-out. `arena cross-judge pool` is a candidate list, not a fan-out count. Prefer a distinct available model family from the parent when possible; GPT-only operation cannot reproduce cross-provider diversity. Scalar roles default to `{ "model": "inherit-parent" }`, panel/pool roles to two copies. This portable default intentionally replaces unvalidated Claude/Grok slugs. Different roles remain independently configurable even if initially inherited.

Use schema version 1. Example shape, showing overrides only:

```json
{
  "schema_version": 1,
  "budget": "large",
  "target_effort": "xhigh",
  "roles": {
    "how explorer": {"model": "inherit-parent"},
    "how explainer": {"model": "auto"},
    "arena runners": [{"model": "inherit-parent"}, {"model": "inherit-parent"}]
  }
}
```

For a real selection write `model` as the exact validated native GPT identity and `reasoning_effort` as a separate validated effort value. Examples are shape documentation, not account entitlements. Aliases `auto` and `inherit-parent` both mean inherit the parent; omit model and effort overrides. Panel arrays must be nonempty; scalar roles require one object. Unknown roles are retired/unknown entries to report and remove during confirmed setup, never silently execute.

## Detection and dispatch validation

Enumerate models and per-model efforts from exposed host schemas/configuration or an entitled-model listing when available. Model identity and reasoning effort are independent fields. Validate each real model and its supported effort, and whether this spawn operation allows explicit overrides at all. Do not infer entitlement from documentation examples, combine model and effort into Cursor slugs, or use external providers. If detection is unavailable, ask for available choices and retain conditional status until supported host evidence confirms them. Inheritance works only if the host supports spawning; `auto` does not grant a model override.

Budgets retain upstream labels: `unlimited — max reasoning`, `large — xhigh reasoning`, `medium — high reasoning`, `small — medium reasoning`. For real models, choose the supported effort at the target, else highest supported at or below target on `max > xhigh > high > medium > low`. If none is supported or the effort scale cannot be established, mark the role needing choice. Aliases stay unchanged. Budget names describe reasoning preferences, not money caps or account quotas.

Before dispatch resolve role, validate against the current environment again, and map model and effort to the actual spawn fields. If host policy permits overrides only in fresh-context children, use that supported fresh context and a complete brief. Never pass forbidden fields. If a role is missing use its inherited default. If a configured model/effort is rejected, report the rejection, re-enumerate and obtain a valid replacement; never silently use a guessed closest slug. If required independence/role selection cannot be met, report the step blocked and seek a scope decision. Record actual selections and any approved substitution in the ledger.
