# pstack reconnaissance for Codex

Investigated October 7, 2026. Recommendation: adapt Lauren Tan's official upstream directly, with a small, explicit Codex compatibility layer and a repo-scoped pilot before global installation. An unchanged copy would load some useful prose but would not execute the complete workflow correctly.

## Source and evidence

- Official source: https://github.com/cursor/plugins/tree/d0ef80d86795816da932a153458c5dbe192d294e/pstack
- Repository commit: `d0ef80d86795816da932a153458c5dbe192d294e`. This pins the whole Cursor plugins repository, not a dedicated pstack release commit.
- Manifest: `pstack/.cursor-plugin/plugin.json`, version `0.15.15`, author `Lauren Tan`, MIT license. The README identifies the author as poteto. This confirms Lauren/poteto authorship; the user's Grokbot employment description was not independently verified.
- Inspection copy: `../upstream/cursor-plugins/pstack`, sparse checkout of the official repository. No third-party port was installed or used as implementation input.
- Current inventory: 51 top-level skills, including 24 principle skills; two Markdown agent definitions; 23 playbook files, including opening-a-pr. The dormant Benny pack additionally contains three skills outside the registered top-level skills directory.
- Exa: 10 search results across upstream/provenance and Codex compatibility searches, then fetched upstream README and official Codex skills/subagents documentation. Search results were discovery inputs; the cloned, pinned source controls version-specific findings. Exa's README content had older model defaults and counts than the clone, so those were not used for the inventory.
- Verification level: static source reconnaissance. No pstack skill, upstream helper, package installation, cloud agent, automation, or ported runtime was executed.

## What the plugin actually is

pstack is primarily an instruction and workflow library. Its Cursor coupling is largely in Markdown instructions, metadata, paths, model slugs, and tool schemas, rather than imports of a Cursor JavaScript SDK.

The front door is `skills/poteto-mode/SKILL.md`: read the principle index, match a playbook, copy the steps into a task list, invoke other skills as needed, delegate work, verify the real outcome, and write concise reports. Most engineering principles and review rubrics are portable. The orchestration surrounding them is platform-specific.

It also includes executable tooling: a decision logger, plan checker, worktree auditor, a Bun orchestration ledger/inbox CLI, and a PR watcher. These require separate review; preserving the Markdown alone does not account for their behavior.

## Compatibility map

| Upstream surface | Source locator | Codex adaptation | Cost / limitation |
| --- | --- | --- | --- |
| Cursor packaging | `.cursor-plugin/plugin.json`; `agents/*.md` | Author repo-scoped skills first; package a Codex plugin after behavior is proven. Convert agent definitions to the target's supported configuration format. | Low packaging effort; agent loading needs target-specific validation. |
| `/poteto-mode` and Cursor mode metadata | `skills/poteto-mode/SKILL.md:1-10` | Use explicit `$poteto-mode`; translate explicit-only invocation to `agents/openai.yaml` policy. Persist mode intent in supported instructions/state if desired. | A Cursor sticky custom mode has no established equivalent merely by copying `mode: true` or `reminder`. |
| `Task`, `subagent_type`, `run_in_background`, `readonly` | `skills/poteto-mode/SKILL.md:93-95`; `skills/interrogate/SKILL.md`, step 3 | Map to the actual target spawn/message/wait interfaces and agent instructions. Preserve freshness/resume rules, bounded scopes, and evidence requirements. | No mechanical parameter rename is sufficient. This desktop exposes collaboration tools; CLI documentation uses a different surface. |
| Per-role models and budget | `skills/setup-pstack/SKILL.md` | Store explicit model and reasoning-effort fields separately, validate against available models, and avoid rewriting Cursor slugs by suffix. Read configuration explicitly instead of assuming an always-applied `.mdc` rule. | Current session exposes GPT models, not native Claude/Grok delegates. No external-provider bridge is included in this recommendation. |
| Cross-family reviewers and blinded judges | `skills/interrogate/SKILL.md`; `skills/arena/SKILL.md`; `playbooks/eval.md:20-22` | Preserve independent candidates and blinded evaluation; disclose the loss of provider diversity when using GPT-only reviewers. | Faithful Claude/Grok behavior would require a separately designed and authorized provider integration. Personas alone do not reproduce model diversity. |
| Cloud workers, pushed bases, nesting | `skills/swarm/SKILL.md:30-32`; `playbooks/orchestrate.md:15-17` | Start with local agents. Allocate one worktree per writer; bound concurrency/depth; use explicit paths because current child agents share the workspace by default. | Codex worktree creation does not automatically place a child there. Current spawn tools have no Cursor `environment: cloud` or `cloud_base_branch` equivalent. |
| Team-kit dependencies | `skills/poteto-mode/SKILL.md:26-30`; README “not shipped here” | Replace `create-skill` with the Codex skill-creator workflow. Define concrete equivalents for deslop, browser/UI control, and CLI/TUI control. | Existing CUA/shell capabilities are useful building blocks, but not proof of parity with those companion skills. |
| Transcript discovery | `skills/recall/SKILL.md:15-21`; `skills/automate-me/SKILL.md:29-31`; `playbooks/session-pickup.md`; `playbooks/eval.md` | Prefer scoped Codex thread-reading tools; where exact execution trace matters, use a verified local session parser. Filter by workspace and exclude current/eval/child noise. | Replacing `.cursor` with `.codex` is insufficient: storage hierarchy, record schema, and available summary fidelity differ. |
| `/loop` and durable programs | `playbooks/autonomous-run.md:6`; `playbooks/orchestrate.md:95-101` | Keep active-session work separate from recurring heartbeats. Use the app's automation mechanism only for explicitly requested follow-up work. Reconstruct from durable artifacts after restart. | An in-session wait is not a durable scheduler; local child agents should not be assumed to survive restart. |
| Generated skills and config | `skills/automate-me/SKILL.md:67-77`; `skills/create-verification-skill/SKILL.md`; `skills/reflect/SKILL.md` | Map placement to repo `.agents/skills`, preserve existing user skills, and make skill writes explicit and reviewable. | Several existing skills have the same names, including `tdd`, `unslop`-adjacent writing workflows, and TypeScript/design standards. Avoid bulk flattening and silent collisions. |
| Grok Bot UI | `skills/make-bot-ui/SKILL.md` | Treat as a separate integration: it targets Grok Bot webhooks, sender keys, and Tailscale. | Not a generic Codex frontend workflow. Exclude from the first port. |
| Benny | `automations/benny/FOR_AGENTS.md`; `templates/*`; three nested skills | Defer. It involves Slack issue reports, scheduled triage/reproduction, repository setup, and runtime verification. | A separate product/integration effort, not needed for core pstack. |

The direct top-level skill scan found `Task`/delegation syntax in 10 skill files, Cursor paths/config references in 15, and Cursor invocation/mode metadata in 50. Categories overlap and omit references/playbooks; these counts indicate breadth, not total edit counts. See the dependency index for full matches.

## Helper tooling findings

- `skills/show-me-your-work/scripts/log.sh`: shell decision logging, a plausible carry-over after checking its caller/path assumptions.
- `skills/poteto-mode/scripts/orch/{orch,store}.ts`: local files, atomic writes/locks, ledgers, inboxes, plus Git/Graphite queries. The orchestration playbook explicitly says the CLI never spawns, waits, or wakes agents. Preserve that boundary rather than inventing a second agent runtime.
- `scripts/watch-pr/*`: GitHub PR polling/policy/rendering tooling. Likely reusable independently of Cursor, subject to dependency and real-repository verification.
- `scripts/bootstrap.ts:35-61`: may run `bun install --frozen-lockfile` and restart the helper. The package depends on Commander 14.0.0 and has Bun/TypeScript development dependencies. A future pilot must account for installation and writable cache location; none was run here.
- `scripts/worktree-audit.sh`: assumes `.cursor` transcript paths, macOS `stat -f` / `date -r`, and extracts worktree paths with `awk '{print $2}'`, which truncates paths containing spaces. This workspace has a space in its name. Its “read-only” header means no deletion; it still fetches Git refs and writes temporary files. Adapt before use.
- `scripts/check-plan.mjs`: validates a prescribed plan format and explicitly requires `/loop 1h` among program markers. Porting only the autonomous-run prose leaves the validator enforcing Cursor syntax.

## Recommended scope

1. **Create a reviewable local adaptation.** Keep the pinned upstream intact. Put adapted files outside skill discovery paths until approval to activate the pilot. Record a source manifest and file-level adaptation diff.
2. **Port the core route.** Poteto mode, principles, investigation/bug-fix/feature/refactoring routes, TDD, architect, how/why, review, prose, and real-artifact verification. Centralize the Codex tool/model/path conventions in one short reference read by callers. Preserve upstream intent rather than redesigning all playbooks.
3. **Prove delegation and review.** Validate fresh child setup, correct source reads, independent review, cancellation/resume, workspace ownership, model/effort mapping, and honest handling of unavailable capabilities. Label GPT-only review accurately.
4. **Add history and durability later.** Scoped recall/session pickup and explicit recurring work, followed by program orchestration if needed. Keep Grok Bot UI and Benny out of the first pilot.
5. **Package after acceptance.** Show the exact installation layout and collision inventory, then activate repo-scoped use; consider global use only after the pilot demonstrates behavior.

Proposed review layout (not created):

```text
upstream/cursor-plugins/pstack/      # unmodified, pinned official source
port/pstack/                        # adapted, inactive files
recon/                              # source manifest, dependency map, findings
evals/                              # representative tasks and observed evidence
```

Pilot acceptance requires more than skills appearing in the selector:

- An investigation selects the intended route, reads the principles/rubrics, and produces source-backed findings.
- A bug fix reproduces behavior before editing and verifies the exact changed artifact.
- A delegate receives the full style wrapper, stays within its assigned files/worktree, and returns usable evidence.
- An adversarial review remains independent, synthesizes supported findings, and does not auto-apply fixes.
- Unavailable Cursor/Grok/cloud features fail clearly or follow an explicitly approved alternative; no fabricated successful execution.
- History reads stay within the authorized workspace/time scope, and recurring work is created only when requested.
- Existing global skills/configuration remain intact.

## Decision

Unchanged install: unsuitable for complete Codex use.

Minimal source-preserving port: recommended for the core workflow; meaningful but bounded adaptation effort.

Full feature parity: substantially larger because cloud execution, cross-provider model review, durable automation, and Grok Bot/Benny integrations are not just instruction substitutions.

This reconnaissance downloaded the official source and wrote research artifacts only. It did not activate skills or change global configuration. Runtime compatibility and port behavior remain unverified.

## Official Codex references

- Skills, locations, metadata, explicit invocation, and plugin distribution: https://developers.openai.com/codex/skills
- Custom subagents, configuration, inheritance, concurrency/depth, and sandbox controls: https://developers.openai.com/codex/subagents

These pages describe the documented product surface. Any implementation must also validate the tools actually exposed by the chosen Codex app/CLI version; documentation alone does not prove identical runtime schemas here.
