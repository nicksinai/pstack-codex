# Agent instructions

Read `docs/specs/pstack-for-codex.md` before implementing the port. Preserve the agreed scope and source-backed verification standard. Confirm actual Codex capabilities before claiming compatibility. Keep the pinned upstream source intact and account for adaptations explicitly.

## Agent skills

### Issue tracker

Use GitHub Issues in `nicksinai/pstack-codex` for specs and tickets. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the five canonical triage labels. See `docs/agents/triage-labels.md`.

### Domain docs

Use the root `GLOSSARY.md` and relevant decisions in `docs/adr/`. See `docs/agents/domain.md`.

## Source and distribution

`upstream/` is an ignored reconnaissance checkout, not a submodule or part of the distributable. Keep personal paths, transcripts, credentials, and account-specific configuration out of the plugin package. Repository creation and tracker setup do not authorize plugin installation or implementation.
