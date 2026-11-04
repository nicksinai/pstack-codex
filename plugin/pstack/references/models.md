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

Panel roles (`arena runners`, `architect runners`, `interrogate reviewers`) default to two entries; each entry, including repeated aliases, counts toward fan-out. `arena cross-judge pool` is a candidate list, not a fan-out count. A cross-judge must be from another model family than the parent; GPT variants do not satisfy that requirement. In this GPT-only port the pool cannot supply such a judge, so Arena explicitly skips Phase C and discloses parent-only selection. Inherited aliases never qualify for cross-judging. Scalar roles default to `{ "model": "inherit-parent" }`, panel/pool roles to two copies. This portable default intentionally replaces unvalidated Claude/Grok slugs. Different roles remain independently configurable even if initially inherited.

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

## Per-job reasoning and speed

Before every spawn start from the configured role and its budget effort. Raise effort one supported step, up to the host maximum, for the hardest or subtlest work. Lower it one supported step for judgment and two or more for routine work. Keep the role's actual model identity; do not infer family diversity from an effort change. Verification retains the configured `swarm workers` model and speed. Use fast speed only when CI or trunk is red, or a person is blocked on the result right now; otherwise use standard speed.

These preferences apply only through fields actually exposed and permitted by the current host schema. For example, a host may expose `reasoning_effort` independently of `model`, and may not expose a speed/service-tier spawn field at all. Do not append upstream `-fast` or effort suffixes to GPT identities, pass unknown arguments, or claim an unavailable speed setting took effect. Inherited aliases omit both overrides. Record the effective fields and any unsupported adjustment.

If the host rejects an adjusted selection, record it and try the validated configured role once, without repeating a rejected selection. Follow the calling workflow's explicit fallback next (Arena restores its runner count but skips an unavailable other-family judge). Where it has no fallback, use supported parent inheritance and disclose the substitution unless that loses a required independence or execution capability, in which case the required step remains blocked. An account's schema and task authority take precedence over illustrative settings here.
