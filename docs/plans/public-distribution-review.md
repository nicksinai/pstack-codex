# Public repository distribution review

Reviewed October 12, 2026, following explicit user authorization to prepare distribution, merge PR #16, and make `nicksinai/pstack-codex` public.

## Exposure review

- Scanned all 405 historical file blobs reachable from local refs after fetching the remote; inspected current repository-owned documents and public-source provenance. Credential patterns covered GitHub/OpenAI/AWS token forms, private-key headers, authenticated URLs, and quoted secret assignments. No credential matches were found. This is a bounded review, not a guarantee against every possible secret format.
- Personal-path matches were upstream `/Users/you/proj` examples and validator regular expressions. No private transcripts or account configuration files were tracked. Commit attribution uses the maintainer's GitHub noreply address. Design/spec records identify Nick and the public repository owner, consistent with this project's provenance.
- Reviewed all 16 issue/PR bodies and 15 issue comments; there were no PR review comments. Credential and personal-path scans returned no matches. Discussions, wiki and Pages were disabled. There were no Actions runs, Actions artifacts, or releases at review time.
- The ignored reconnaissance checkout, local archives and dependency directories remain excluded. Original upstream bytes and their MIT notices remain intact; no history rewriting or private-content deletion was required.

## Distribution changes and evidence

The committed `.agents/plugins/marketplace.json` exposes `plugin/pstack` under **PStack for Codex**, using the same qualified package entry as the offline example. Root and package guides document repository-source registration, desktop installation, manual project setup, explicit onboarding/activation, and removal. Official source: https://developers.openai.com/plugins/build/plugins (retrieved October 12, 2026).

`python3 scripts/validate-provenance.py` passes the original complete package checks plus catalog equality and path resolution. The adaptation diff was regenerated after updating the package guide. `python3 scripts/build-package.py --output-dir dist` passes and produces the updated reproducible archive. These changes add distribution metadata and instructions; they do not install a plugin or establish recipient runtime capabilities. Existing source-qualified workflow limits still apply.

Public repository access is separate from publication in OpenAI's universal plugin directory. No directory submission is part of this operation.
