#!/usr/bin/env python3
"""Print deterministic unified diffs for every mapped upstream adaptation."""
from pathlib import Path
import difflib
import json
import sys

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "provenance/ownership.json").read_text())
for item in manifest["items"]:
    if not item["target"]:
        continue
    source = root / manifest["baseline"] / item["source"]
    target = root / item["target"]
    if not target.is_file():
        raise SystemExit(f"Missing mapped target: {item['target']}")
    if source.read_bytes() == target.read_bytes():
        continue
    try:
        before = source.read_text().splitlines(keepends=True)
        after = target.read_text().splitlines(keepends=True)
    except UnicodeDecodeError:
        print(f"Binary files differ: {item['source']} -> {item['target']}")
        continue
    sys.stdout.writelines(difflib.unified_diff(
        before, after, fromfile="upstream/pstack/" + item["source"],
        tofile=item["target"],
    ))
