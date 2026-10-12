# Issue tracker: GitHub

Specs and tickets live in GitHub Issues for `nicksinai/pstack-codex`.

- Create an issue with `gh issue create --repo nicksinai/pstack-codex --title "..." --body-file <file>`.
- Read an issue and its comments with `gh issue view <number> --repo nicksinai/pstack-codex --comments`.
- List open issues with `gh issue list --repo nicksinai/pstack-codex --state open --json number,title,body,labels,assignees`.
- Apply a triage label with `gh issue edit <number> --repo nicksinai/pstack-codex --add-label <label>`.
- Publish a specification as a GitHub issue labeled `ready-for-agent`. This means the issue is specified; it does not independently authorize execution.
- Link implementation tickets to their specification. Use native sub-issues and dependency edges where supported; otherwise record `Part of #N` and `Blocked by: #N` explicitly.
- Keep repository source documents and the published specification consistent when requirements change.

Use temporary files for multiline issue/PR bodies; pass them via `--body-file`. Infer the repository from `origin` when appropriate.

PRs as a request surface: no.
