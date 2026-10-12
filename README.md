# pstack for Codex

A source-preserving port of Lauren Tan / poteto's pstack engineering workflows to Codex, intended to be shareable with a friend.

**Status:** source-qualified port, prepared for public repository distribution. Recipient installation and runtime capabilities still require verification. The [self-contained package guide](plugin/pstack/README.md) describes setup, invocation and limits; [whole-package qualification](plugin/pstack/qualification/issue-15.md) records the source-backed argument.

## Install

Use Codex desktop with local marketplace support and a policy allowing local plugins. If the Codex CLI is available, add this repository as a marketplace source:

```sh
codex plugin marketplace add nicksinai/pstack-codex --ref main
```

Clients with `codex plugin add` can also install from the terminal:

```sh
codex plugin add pstack-codex@pstack-codex-marketplace
```

Restart the desktop app, open the Plugins Directory, choose **PStack for Codex**, and install **pstack-codex**. In a new chat, explicitly select **pstack-setup-pstack**, then **pstack-poteto-mode** with your request. Installation does not activate PStack or authorize a task. Availability varies by client version and account policy; see the [official marketplace guidance](https://developers.openai.com/plugins/build/plugins#add-a-marketplace-from-the-cli).

Without the CLI, clone or download this repository, open its directory as a project in Codex, and restart the desktop app. The committed `.agents/plugins/marketplace.json` exposes the same package through the project's marketplace. For use in another project or from an offline archive, follow the [complete setup/removal guide](plugin/pstack/README.md).

Select an individual skill for one request, or explicitly say “Enter sticky PStack mode for this conversation.” Exit with “Exit PStack mode.” Required tools, authentication, model choices and local helper dependencies are checked during setup; the plugin cannot grant them.

## Source and qualification

Build an offline friend artifact with `python3 scripts/build-package.py --output-dir <recipient-artifact-directory>`. This assembles a reproducible archive and companion digest; it does not install or share it. Run `python3 scripts/validate-provenance.py` first.

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

The ignored reconnaissance checkout is excluded. The immutable baseline is retained under `provenance/upstream/pstack`; [the source manifest](recon/upstream-manifest.json) records its hashes and [ownership inventory](provenance/ownership.json) accounts for every adaptation. [Third-party notices](THIRD_PARTY_NOTICES.md) and companion licenses accompany redistributed content.

## Project workflow

Specs and tickets live in GitHub Issues. Repository conventions are in [issue-tracker](docs/agents/issue-tracker.md), [triage labels](docs/agents/triage-labels.md), and [domain documentation](docs/agents/domain.md).
