#!/usr/bin/env python3
"""Check baseline integrity, complete ownership, mapped paths, and package links."""
import argparse
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
from urllib.parse import unquote

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--require-complete", action="store_true", help="Reject incomplete reviewed-transition qualification before distribution")
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "provenance/ownership.json").read_text())
registry = json.loads((root / "provenance/baselines.json").read_text())
assert registry["schema_version"] == 1
assert registry["original_revision"] == "d0ef80d86795816da932a153458c5dbe192d294e"
assert registry["reviewed_revision"] == "dbf49813a39c1a5389c5e28cb8e4c1c2379e2454"
baselines = {}
for entry in registry["baselines"]:
    revision = entry["revision"]
    assert revision not in baselines, "Duplicate baseline revision"
    baseline = root / entry["baseline"]
    assert baseline.resolve().is_relative_to(root), entry["baseline"]
    assert (root / entry["manifest"]).resolve().is_relative_to(root), entry["manifest"]
    source_manifest = json.loads((root / entry["manifest"]).read_text())
    assert source_manifest["commit"] == revision
    assert source_manifest["repository"] == manifest["repository"]
    assert source_manifest["plugin_version"] == entry["version"]
    hashes = source_manifest["files_sha256"]
    actual = {str(p.relative_to(baseline)) for p in baseline.rglob("*") if p.is_file()}
    assert actual == set(hashes), (revision, "Baseline inventory mismatch")
    for path, digest in hashes.items():
        source = baseline / path
        assert not source.is_symlink() and source.resolve().is_relative_to(baseline.resolve()), path
        assert hashlib.sha256(source.read_bytes()).hexdigest() == digest, (revision, path)
    baselines[revision] = (baseline, hashes)
assert set(baselines) == {registry["original_revision"], registry["reviewed_revision"]}
reviewed = next(x for x in registry["baselines"] if x["revision"] == registry["reviewed_revision"])
assert reviewed["predecessor_revision"] == registry["original_revision"]
assert manifest["commit"] == registry["original_revision"]
transition = json.loads((root / "provenance/upstream-transition.json").read_text())
assert transition["schema_version"] == 1 and transition["spec_issue"] == 20
assert transition["from_revision"] == registry["original_revision"]
assert transition["to_revision"] == registry["reviewed_revision"]
old_hashes = baselines[transition["from_revision"]][1]
new_hashes = baselines[transition["to_revision"]][1]
expected_delta = {path for path in old_hashes.keys() | new_hashes.keys()
                  if old_hashes.get(path) != new_hashes.get(path)}
rows = transition["items"]
assert len(rows) == len({x["source"] for x in rows}) == 65
assert {x["source"] for x in rows} == expected_delta
assert sum(x["change"] == "added" for x in rows) == 4
assert sum(x["change"] == "changed" for x in rows) == 61
for row in rows:
    path = row["source"]
    assert row["previous_sha256"] == old_hashes.get(path) and row["sha256"] == new_hashes.get(path), path
    assert row["change"] == ("added" if path not in old_hashes else "removed" if path not in new_hashes else "changed"), path
    assert 21 <= row["owner_issue"] <= 30 and row["reason"], path
    assert row["disposition"] in {"pending", "blocked", "adapted", "equivalent", "retained", "deferred"}, path
    if row["disposition"] not in {"pending", "blocked"}:
        evidence = root / row["qualification"]
        assert evidence.resolve().is_relative_to(root) and evidence.is_file(), path
    if row["target"]:
        target = root / row["target"]
        assert target.resolve().is_relative_to(root), path
        # A pending addition can declare its intended target before it exists.
        assert row["disposition"] == "pending" or target.is_file(), path
items = manifest["items"]
paths = [item["source"] for item in items]
assert len(paths) == len(set(paths)), "Duplicate source owners"
assert set(old_hashes) <= set(paths) <= set(old_hashes) | set(new_hashes), "Active inventory lost original source or added unknown source"
for item in items:
    baseline, hashes = baselines[item["source_revision"]]
    assert item["sha256"] == hashes[item["source"]], item["source"]
    assert 2 <= item["owner_issue"] <= 30, item
    assert item["disposition"] in {"pending", "adapted", "preserved", "deferred", "blocked"}, item
    if item["target"]:
        target = (root / item["target"]).resolve()
        assert target.is_relative_to(root), item["target"]
        assert target.is_file(), item["target"]
active_by_source = {item["source"]: item for item in items}
for row in rows:
    if row["disposition"] in {"adapted", "equivalent", "retained"}:
        active = active_by_source[row["source"]]
        assert row["target"] and row["target"] == active["target"], row["source"]
        if row["disposition"] == "adapted":
            assert active["source_revision"] == transition["to_revision"], row["source"]
assert json.loads((root / "plugin/pstack/qualification/upstream-transition.json").read_text()) == transition
pending = sum(row["disposition"] in {"pending", "blocked"} for row in rows)
if args.require_complete:
    assert pending == 0, f"Final qualification requires zero pending/blocked obligations; found {pending}"
    assert {item["source"] for item in manifest["items"]} == set(new_hashes), "Final qualification requires all 168 reviewed source items"
print(f"Validated both retained source baselines; 65 transition differences, {pending} pending/blocked adaptation obligations.")
current_diff = subprocess.check_output(
    [sys.executable, str(root / "scripts/adaptation-diff.py")], cwd=root,
)
assert (root / "provenance/adaptations.patch").read_bytes() == current_diff, (
    "Stale adaptation diff; regenerate with "
    "python3 scripts/adaptation-diff.py > provenance/adaptations.patch"
)
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
skill_sources = {item['target']: baselines[item['source_revision']][0] / item['source']
                 for item in items if item['target'] and item['target'].endswith('/SKILL.md')}
companion_sources = json.loads((root / 'provenance/companion-descriptions.json').read_text())
assert len(companion_sources) == 1
for companion in companion_sources:
    assert companion['repository'] == manifest['repository']
    assert companion['revision'] == registry['original_revision']
    assert companion['source'] == 'cursor-team-kit/skills/deslop/SKILL.md'
    assert companion['target'] == 'plugin/pstack/skills/pstack-deslop/SKILL.md'
    baseline = root / companion['baseline']
    assert baseline.resolve().is_relative_to(root / 'provenance')
    assert hashlib.sha256(baseline.read_bytes()).hexdigest() == companion['sha256']
    skill_sources[companion['target']] = baseline
for skill in skills:
    if skill.parent.name == 'pstack-update':
        continue
    source_path = skill_sources.get(str(skill.relative_to(root)))
    assert source_path, ('Unaccounted description source', skill)
    source_text = source_path.read_text()
    source_raw = re.search(r'^description: (.+)$', source_text, re.M).group(1)
    source_description = json.loads(source_raw) if source_raw.startswith('"') else source_raw
    raw = re.search(r'^description: (.+)$', skill.read_text(), re.M).group(1)
    description = json.loads(raw) if raw.startswith('"') else raw
    assert description in source_description, ('Description differs from upstream', skill)
    ui = (skill.parent / 'agents/openai.yaml').read_text()
    short = json.loads(re.search(r'^  short_description: (.+)$', ui, re.M).group(1))
    assert 25 <= len(short) <= 64, ('Picker description length', skill)
    assert short in source_text or short in source_description, ('Picker wording differs from upstream', skill)
print(f'Validated upstream wording for {len(skill_sources)} skill and picker descriptions; Codex-specific update is excluded.')
# Final closure is structural proof, not a behavioral product-use claim.
assert len(old_hashes) == 164 and len(new_hashes) == 168
assert len(items) == len(old_hashes) + len(set(paths) - set(old_hashes))
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
            assert (baselines[item['source_revision']][0] / item['source']).read_bytes() == (root / item['target']).read_bytes()
assert json.loads((package / 'qualification/source-inventory.json').read_text()) == manifest
upstream_skill_paths = {
    item['target'] for item in items
    if item['source'].startswith('skills/') and item['source'].endswith('/SKILL.md') and item['target']
}
package_only_skill_paths = {
    'plugin/pstack/skills/pstack-deslop/SKILL.md',
    'plugin/pstack/skills/pstack-update/SKILL.md',
}
assert not upstream_skill_paths & package_only_skill_paths
assert {str(skill.relative_to(root)) for skill in skills} == upstream_skill_paths | package_only_skill_paths
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
print(f'Active adaptation closure: {len(items)} accounted source items, 13 agreed deferred; {len(skills)} skills, 24 principles, 23 playbook targets, 2 wrappers; {catalog_chars} catalog characters; dependency/privacy/symlink checks. Transition qualification tracked separately.')

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

repo_catalog = json.loads((root / ".agents/plugins/marketplace.json").read_text())
assert repo_catalog["name"] == "pstack-codex-marketplace"
assert repo_catalog["plugins"] == marketplace["plugins"]
assert repo_catalog["interface"]["displayName"] == "PStack for Codex"
print("Repository marketplace catalog matches the qualified plugin entry.")

compat_manifest = json.loads((package / ".codex-plugin/plugin.json").read_text())
for field in ("name", "version", "description"):
    assert compat_manifest[field] == meta[field], field
assert compat_manifest["skills"] == "./skills/"
print("Portable and Codex compatibility manifests agree; skills path resolves.")
