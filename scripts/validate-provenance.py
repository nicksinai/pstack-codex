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
# Final closure is structural proof, not a behavioral product-use claim.
assert len(items) == 164
assert sum(x['disposition'] == 'deferred' for x in items) == 13
assert all(x['disposition'] in {'adapted', 'preserved', 'deferred'} for x in items)
assert all(x.get('reason') for x in items)
for item in items:
    if item['disposition'] == 'deferred':
        assert item['target'] is None
        assert item['source'].startswith('automations/benny/') or item['source'] == 'skills/make-bot-ui/SKILL.md'
    else:
        assert item['target']
        if item['disposition'] == 'preserved':
            assert (baseline / item['source']).read_bytes() == (root / item['target']).read_bytes()
assert json.loads((package / 'qualification/source-inventory.json').read_text()) == manifest
assert len(skills) == 51
assert len(list((package / 'skills').glob('pstack-principle-*/SKILL.md'))) == 24
source_playbooks = [x for x in items if '/playbooks/' in x['source']]
assert len(source_playbooks) == 23
assert len({x['target'] for x in source_playbooks}) == 23
assert len([x for x in items if x['source'].startswith('agents/')]) == 2
catalog_chars = 0
for skill in skills:
    description = re.search(r'^description: (.+)$', skill.read_text(), re.M)
    assert description
    catalog_chars += len(skill.parent.name) + len(description.group(1))
assert catalog_chars <= 8000, f'Catalog name/description total exceeds documented absolute cap: {catalog_chars}'
for file in package.rglob('*'):
    assert not file.is_symlink(), file
    assert not any(part in {'node_modules', '__pycache__', '.git', '.cache', '.env'} for part in file.relative_to(package).parts), file
    if not file.is_file():
        continue
    assert file.suffix in {'.md', '.json', '.yaml', '.ts', '.mjs', '.py', '.sh', '.lock', '.tsv'} or file.name in {'LICENSE', 'cursor-team-kit-LICENSE', 'watch-pr'}, file
    text = file.read_text()
    assert not re.search(r'/Users/[^/]+|/home/[^/]+|/tmp/pstack|gh[pousr]_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9]{24,}|app-[a-f0-9]{32}', text), file
    if file.suffix == '.md' and 'qualification' not in file.relative_to(package).parts:
        assert not re.search(r'\bstaged\b', text), file
        # Explicit relative inline paths are executable instruction dependencies.
        for href in re.findall(r'`((?:\.\.?/)[^`\n]+\.(?:md|ts|py|sh|mjs|json))`', text):
            target = (file.parent / href).resolve()
            assert target.is_relative_to(package.resolve()) and target.is_file(), (file, href)
    if file.suffix in {'.ts', '.mjs'}:
        for href in re.findall(r'(?:from\s*|import\s*\()?[\"\'](\.[^\"\']+)[\"\']', text):
            if not href.startswith(('./', '../')):
                continue
            target = file.parent / href
            assert target.exists() or target.with_suffix('.ts').exists() or target.with_suffix('.js').exists(), (file, href)
print(f'Final closure: 164 accounted source items, 13 agreed deferred; 51 skills, 24 principles, 23 playbook targets, 2 wrappers; {catalog_chars} catalog characters; dependency/privacy/symlink checks.')

expected_files = json.loads((root / "provenance/package-files.json").read_text())
actual_files = sorted(str(f.relative_to(package)) for f in package.rglob("*") if f.is_file())
assert expected_files == actual_files, "Unexpected or missing packaged files; review and update package-files.json explicitly"
marketplace = json.loads((package / "marketplace.example.json").read_text())
entry = marketplace["plugins"][0]
assert entry["name"] == meta["name"]
assert entry["source"] == {"source": "local", "path": "./plugin/pstack"}
assert entry["policy"]["installation"] == "AVAILABLE"
assert (root / entry["source"]["path"]).resolve() == package.resolve()
print(f"Reviewed file allowlist matches {len(actual_files)} package files; local catalog resolves package root.")
