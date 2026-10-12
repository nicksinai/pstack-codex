# pstack for Codex

Language for deciding which pstack capabilities the Codex port preserves.

## Language

**pstack port**:
An adaptation of Lauren Tan / poteto's official pstack for use in Codex, preserving its engineering workflows subject to explicitly agreed differences.
_Avoid_: Community port, copied skill collection

**Provider diversity**:
Independent attempts or reviews performed by models from different providers. Multiple GPT reviewers provide independent reviews but do not provide provider diversity.
_Avoid_: Multiple personas, independent review as a synonym

**Workflow fidelity**:
Preservation of pstack's workflow steps, review standards, and evidence requirements despite explicitly agreed changes in execution capabilities.
_Avoid_: Skills loading successfully, identical infrastructure

**Unattended execution**:
Task progress without ongoing human input while the execution environment remains available. It does not imply continued operation through shutdown or sleep.
_Avoid_: Always-on execution

**Recovery**:
Reconstruction and continuation of interrupted pstack work from recorded state and verified current artifacts.
_Avoid_: Continuous execution, restart from scratch
