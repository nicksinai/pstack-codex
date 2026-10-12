#!/usr/bin/env bash
# Compatibility entrypoint; Git/Python audit performs no deletion or ref writes.
set -eu
exec python3 "$(dirname "$0")/worktree-audit.py" "$@"
