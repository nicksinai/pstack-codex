# pstack for Codex

A source-preserving port of Lauren Tan / poteto's pstack engineering workflows to Codex, intended to be shareable with a friend.

**Status:** specification and reconnaissance. No runnable port or installable plugin has been built yet.

- [Implementation specification](docs/specs/pstack-for-codex.md)
- [Published specification issue](https://github.com/nicksinai/pstack-codex/issues/1)
- [Implementation tickets and dependencies](docs/plans/pstack-ticket-breakdown.md)
- [Design decisions](docs/pstack-port-design.md)
- [Architectural decision](docs/adr/0001-preserve-workflows-with-native-execution.md)
- [Glossary](GLOSSARY.md)
- [Source reconnaissance](recon/pstack-codex-recon-2026-10-07.md)
- [GitHub Issues](https://github.com/nicksinai/pstack-codex/issues)

The first release targets Codex desktop with native GPT models and isolated local workers. It preserves upstream workflow contracts, explicit activation, history/learning, PR workflows, and unattended work with recovery. Cloud execution, external model providers, Grok Bot UI, and Benny are deferred.

Port qualification uses a source-backed fidelity and compatibility argument rather than a mandatory behavioral test suite. Pstack's own testing and real-artifact verification requirements remain part of the workflows.

## Upstream

The official source is [cursor/plugins/pstack](https://github.com/cursor/plugins/tree/d0ef80d86795816da932a153458c5dbe192d294e/pstack), authored by Lauren Tan and distributed under MIT. The initial baseline is version 0.15.15 at repository commit `d0ef80d86795816da932a153458c5dbe192d294e`. This is an independent adaptation project, not an official Cursor or OpenAI plugin.

The local upstream checkout is excluded from this repository. [The source manifest](recon/upstream-manifest.json) records its file hashes. [Third-party notices](THIRD_PARTY_NOTICES.md) include the upstream license for quoted source material. Applicable notices must accompany future redistributed upstream content.

## Project workflow

Specs and tickets live in GitHub Issues. Repository conventions are in [issue-tracker](docs/agents/issue-tracker.md), [triage labels](docs/agents/triage-labels.md), and [domain documentation](docs/agents/domain.md).
