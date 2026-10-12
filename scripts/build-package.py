#!/usr/bin/env python3
"""Assemble a deterministic offline marketplace archive without installing it."""
import argparse
import hashlib
import json
from pathlib import Path
import stat
import subprocess
import zipfile

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir', type=Path, required=True)
args = parser.parse_args()
if args.output_dir.resolve().is_relative_to((root / 'plugin/pstack').resolve()):
    raise SystemExit('Artifact directory must be outside the installed package tree.')
subprocess.run(['python3', str(root / 'scripts/validate-provenance.py')], check=True)
package = root / 'plugin/pstack'
version = json.loads((package / 'plugin.json').read_text())['version']
entries = {}
for path in sorted(package.rglob('*')):
    if path.is_symlink():
        raise SystemExit(f'Symlink forbidden: {path}')
    if path.is_file():
        entries[path.relative_to(root).as_posix()] = (path.read_bytes(), bool(path.stat().st_mode & stat.S_IXUSR))
entries['.agents/plugins/marketplace.json'] = ((package / 'marketplace.example.json').read_bytes(), False)
entries['THIRD_PARTY_NOTICES.md'] = ((root / 'THIRD_PARTY_NOTICES.md').read_bytes(), False)
manifest = {'format': 1, 'plugin': 'pstack-codex', 'version': version, 'files': [
    {'path': name, 'sha256': hashlib.sha256(data).hexdigest(), 'size': len(data), 'executable': executable}
    for name, (data, executable) in sorted(entries.items())]}
entries['MANIFEST.json'] = ((json.dumps(manifest, indent=2, sort_keys=True) + '\n').encode(), False)
args.output_dir.mkdir(parents=True, exist_ok=True)
target = args.output_dir / f'pstack-codex-{version}.zip'
with zipfile.ZipFile(target, 'w', compression=zipfile.ZIP_STORED) as archive:
    for name, (data, executable) in sorted(entries.items()):
        entry = zipfile.ZipInfo(name, date_time=(2026, 10, 12, 0, 0, 0))
        entry.create_system = 3
        entry.external_attr = (stat.S_IFREG | (0o755 if executable else 0o644)) << 16
        archive.writestr(entry, data)
digest = hashlib.sha256(target.read_bytes()).hexdigest()
target.with_suffix('.zip.sha256').write_text(f'{digest}  {target.name}\n')
print(f'{target}\nSHA-256 {digest}\n{len(entries)} archive entries; no installation performed.')
