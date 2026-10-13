# Issue 26: explicit goal playback

Part of specification #20. This ledger qualifies the goal-playback addition by source and configuration inspection. It does not claim observed desktop selection or universal agent compliance.

## Source and preservation argument

Reviewed source: official Cursor plugins revision `dbf49813a39c1a5389c5e28cb8e4c1c2379e2454`, pstack `0.15.23`. The original `0.15.15` archive remains intact. The complete added [upstream skill](https://github.com/cursor/plugins/blob/dbf49813a39c1a5389c5e28cb8e4c1c2379e2454/pstack/skills/in-your-own-words/SKILL.md#L1-L7) has one task: restate the user's goals and problem in the agent's own words. Its frontmatter disables model invocation and describes explicit slash entry.

| Requirement | Adapted counterpart and argument | Status |
| --- | --- | --- |
| Restate both goals and problem in the agent's own words; upstream body line 7 | [Skill](../skills/pstack-in-your-own-words/SKILL.md) preserves the upstream instruction verbatim. The only added body text ends the invocation at a restatement for the user to check and implements specification #20's explicit boundary against implementation or a discovery interview. No plan, question sequence or tool workflow is introduced. | Established instruction content; agent compliance conditional. |
| Explicit-only entry; upstream frontmatter lines 2–4 | Namespaced folder/frontmatter `pstack-in-your-own-words`; [metadata](../skills/pstack-in-your-own-words/agents/openai.yaml) uses the existing `pstack: <name>` display convention and `policy.allow_implicit_invocation: false`. Cursor's slash syntax and `disable-model-invocation` field are replaced by the documented Codex policy and `$pstack-in-your-own-words` entry. Existing skill identities and settings remain intact. | Established configuration; recipient discovery conditional. |
| Find goal playback before work; reviewed help table addition at line 66 | [Help](../skills/pstack-poteto-help/SKILL.md) routes the user's understanding check to in-your-own-words; the authoritative [mode lookup](../skills/pstack-poteto-mode/SKILL.md) resolves the namespaced sibling directly. This is discovery of an explicit leaf, not an automatic mode trigger. | Established package links and routing text. |
| Copyable explicit prompt; reviewed recipes addition at line 8 | [Recipes](../skills/pstack-poteto-help/references/recipes.md) carries `$pstack-in-your-own-words <long or messy ask>`, preserving the upstream example with Codex mention syntax. | Established source-backed recipe. |

The shared reviewed [help source](https://github.com/cursor/plugins/blob/dbf49813a39c1a5389c5e28cb8e4c1c2379e2454/pstack/skills/poteto-help/SKILL.md) also adds ketchup at line 71 and the recall/ketchup distinction at line 103. Those requirements belong to dependency #27. Both shared help transition rows retain primary owner #26 and `dependency_issues: [27]`, with pending disposition until both tickets integrate and the combined targets are reviewed. This ticket qualifies its portion only; it does not adopt the full reviewed help source prematurely or add ketchup itself. The recipes row also stays pending with the shared dependency despite its single goal-playback hunk being delivered.

## Codex capability dependencies

Official OpenAI [Build skills: Optional metadata](https://learn.chatgpt.com/docs/build-skills#optional-metadata), fetched October 13, 2026, establishes `agents/openai.yaml` UI metadata and the explicit-only policy: disabling implicit invocation retains explicit `$skill` invocation. [C3/C4](capabilities.md) record instruction loading and recipient-client limits. This leaf needs only the user's available request/conversation and ordinary response generation. It requires no scripts, credentials, connectors, delegates, history reader or external mutations. The authoring guidance's Cursor-style invocation field is not copied into Codex metadata.

Namespacing, explicit policy and resolvable local instructions are established by inspection and deterministic package checks. Actual picker presentation, installation, enabled-plugin state and probabilistic adherence remain conditional on the recipient environment and were not observed. No installation or plugin workflow was executed.

## Package accounting and verification

The independent #26 snapshot adds one delivered upstream skill mapping: 164 original source items plus one addition equals 165 active mappings; 51 original packaged skills plus goal playback equals 52, with 24 principles, 23 playbooks, two wrappers and 13 agreed exclusions retained. The computed name/description catalog is 6,031 characters at this snapshot; later tickets recompute from their actual delivered inventory. Final README totals and release qualification belong to #30.

The reviewed allowlist adds only this ledger and the new leaf's `SKILL.md` and `agents/openai.yaml`. Active source and transition inventories are synchronized into the package, and the source-revision-labelled adaptation diff is regenerated. The new source row selects the reviewed hash; immutable archives and original source mappings are retained. Shared help mappings remain on their original revision until combined qualification.

Verification uses the agreed complete-package/source-backed boundary: repository provenance, inventory, namespace, metadata, internal-reference, dependency and privacy validation; existing deterministic tests; skill-authoring validation; and archive assembly. No prompt-string assertions or broad agent-behavior tests are added. Exact validation results are reported with the implementation commit.

Independent #26 validation passed with 224 reviewed package files and 64 still-pending transition obligations. All seven existing monitor unit tests passed; their issue mutations use fakes, not GitHub. The skill-authoring validator passed using isolated PyYAML 6.0.3 after the system Python reported that dependency missing. Two deterministic offline builds were byte-identical: 227 archive entries, SHA-256 `2d8fb80184d8254fa81b5bd92cd270944e8abe3c103d51a6e01651343ab60d3c` before this results paragraph was added. This is a pre-release intermediate package, not final #30 release evidence. Neither retained source archive nor either hash manifest was changed.
