#!/usr/bin/env python3
"""Check baseline integrity, complete ownership, mapped paths, and package links."""
from pathlib import Path
import hashlib
import json
import re
from urllib.parse import unquote

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "provenance/ownership.json").read_text())
baseline = root / manifest["baseline"]
items = manifest["items"]
paths = [item["source"] for item in items]
assert len(paths) == len(set(paths)), "Duplicate source owners"
actual = {str(p.relative_to(baseline)) for p in baseline.rglob("*") if p.is_file()}
assert set(paths) == actual, "Inventory does not match baseline"
recon = json.loads((root / "recon/upstream-manifest.json").read_text())
assert manifest["commit"] == recon["commit"]
assert {x["source"]: x["sha256"] for x in items} == recon["files_sha256"]
for item in items:
    assert 2 <= item["owner_issue"] <= 15, item
    assert item["disposition"] in {"pending", "adapted", "preserved", "deferred", "blocked"}, item
    assert hashlib.sha256((baseline / item["source"]).read_bytes()).hexdigest() == item["sha256"], item["source"]
    if item["target"]:
        target = (root / item["target"]).resolve()
        assert target.is_relative_to(root), item["target"]
        assert target.is_file(), item["target"]
package = root / "plugin/pstack"
meta = json.loads((package / "plugin.json").read_text())
assert meta["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
assert re.fullmatch(r"[a-z][a-z0-9-]*", meta["name"])
assert re.fullmatch(r"\d+\.\d+\.\d+(?:-[a-zA-Z0-9.-]+)?", meta["version"])
assert meta["description"]
for md in package.rglob("*.md"):
    text = md.read_text()
    assert not re.search(r"/Users/[^/]+|/home/[^/]+|/tmp/pstack", text), md
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        href = match.group(1).strip("<>")
        if "://" in href or href.startswith("#"):
            continue
        target = (md.parent / unquote(href.split("#")[0])).resolve()
        assert target.is_relative_to(package.resolve()), (md, href, "outside package")
        assert target.exists(), (md, href, "missing")
skills = list((package / "skills").glob("*/SKILL.md"))
for skill in skills:
    assert skill.parent.name.startswith("pstack-")
    assert f"name: {skill.parent.name}\n" in skill.read_text(), skill
    assert "allow_implicit_invocation: false" in (skill.parent / "agents/openai.yaml").read_text(), skill
print(f"Validated {len(items)} baseline files with unique owners and hashes; {len(skills)} skill metadata/policies; package-local Markdown links.")
