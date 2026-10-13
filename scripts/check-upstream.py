#!/usr/bin/env python3
"""Compare official pstack bytes with the reviewed pin; optionally maintain one issue."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import tempfile
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = 'https://github.com/cursor/plugins'
MARKER = '<!-- pstack-upstream-monitor -->'
TITLE = 'Review upstream pstack changes'


def run(*args, **kwargs):
    return subprocess.check_output(args, text=True, **kwargs).strip()


def snapshot(checkout):
    revision = run('git', '-C', str(checkout), 'rev-parse', 'HEAD')
    # ls-tree avoids untracked files; hash symlink text without following targets.
    entries = subprocess.check_output(
        ['git', '-C', str(checkout), 'ls-tree', '-rz', 'HEAD', '--', 'pstack/']
    ).split(b'\0')
    hashes = {}
    for entry in filter(None, entries):
        metadata, filename = entry.split(b'\t', 1)
        mode, kind, _ = metadata.split()
        if kind != b'blob':
            raise ValueError('Unsupported upstream entry: ' + os.fsdecode(filename))
        path = checkout / os.fsdecode(filename)
        content = os.fsencode(os.readlink(path)) if mode == b'120000' else path.read_bytes()
        hashes[os.fsdecode(filename).removeprefix('pstack/')] = hashlib.sha256(content).hexdigest()
    if '.cursor-plugin/plugin.json' not in hashes:
        raise ValueError('Official pstack manifest missing; refusing to report a mass removal')
    return revision, hashes


def changes(manifest, hashes):
    old = {item['source']: item['sha256'] for item in manifest['items']}
    return [(path, 'added' if path not in old else 'removed' if path not in hashes else 'changed')
            for path in sorted(old.keys() | hashes.keys()) if old.get(path) != hashes.get(path)]


def pending_adaptations(manifest):
    return [item for item in manifest.get('transition', {}).get('items', [])
            if item['disposition'] in {'pending', 'blocked'}]


def needs_review(manifest, delta):
    return bool(delta or pending_adaptations(manifest))


def report(manifest, revision, hashes, delta, repository):
    # Content fingerprint prevents unrelated commits in Cursor's monorepo causing updates.
    fingerprint = hashlib.sha256(json.dumps(
        [manifest['commit'], hashes, manifest.get('transition')], sort_keys=True
    ).encode()).hexdigest()
    state = f'<!-- pstack-upstream-state:{fingerprint} -->'
    owners = {item['source']: item for item in manifest['items']}
    counts = {kind: sum(status == kind for _, status in delta)
              for kind in ('added', 'changed', 'removed')}
    lines = [MARKER, state, '',
             'Upstream source changes require adaptation review before release.', '',
             f"Reviewed baseline: [{manifest['version']} / {manifest['commit'][:12]}]"
             f"({UPSTREAM}/tree/{manifest['commit']}/pstack).",
             f'Observed upstream: [{revision[:12]}]({UPSTREAM}/tree/{revision}/pstack).',
             f"[Compare revisions]({UPSTREAM}/compare/{manifest['commit']}...{revision}) "
             '(comparison includes other plugins; the inventory below is pstack-only).', '',
             f"{counts['added']} added, {counts['changed']} changed, {counts['removed']} removed files.", '',
             '| Change | Upstream file | Codex counterpart / review status |',
             '| --- | --- | --- |']
    for path, status in delta:
        item = owners.get(path)
        if item and item['target']:
            target = item['target']
            counterpart = f'[{target}](https://github.com/{repository}/blob/{quote(os.environ.get("GITHUB_SHA", "main"), safe="")}/{quote(target)})'
        elif item:
            counterpart = f"{item['disposition']} — {item['reason']}"
        else:
            counterpart = 'Unmapped addition — evaluate scope and Codex adaptation'
        ref = manifest['commit'] if status == 'removed' else revision
        # Escape table delimiters and HTML in paths supplied by upstream.
        label = path.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '&#124;').replace('`', '&#96;').replace('\n', ' ')
        lines.append(f'| {status} | [{label}]({UPSTREAM}/blob/{ref}/pstack/{quote(path)}) | {counterpart} |')
    pending = pending_adaptations(manifest)
    if manifest.get('transition'):
        lines += ['', f'{len(pending)} pending adaptation obligations for the reviewed transition.', '',
                  'Archiving reviewed source does not qualify these adaptations.']
        for item in pending:
            lines.append(f"- `{item['source']}` — #{item['owner_issue']}: {item['reason']}")
    lines += ['', 'Review steps:', '',
              '- Review changed requirements and all callers/dependencies; additions need an explicit scope decision.',
              '- Preserve the original baseline; pin the new revision separately and account for each adaptation or omission.',
              '- Update the inventory, qualification records and adaptation diff; validate and release a new Codex plugin version.', '',
              'This monitor updates this issue only. It does not import code, execute upstream helpers, or release/install the plugin.',
              'The issue body is managed by the monitor; record maintainer decisions in comments.']
    return state, '\n'.join(lines) + '\n'


def sync_issue(repository, state, body, has_changes):
    pages = json.loads(run('gh', 'api', '--paginate', '--slurp',
                          f'repos/{repository}/issues?state=all&per_page=100'))
    matches = [issue for page in pages for issue in page
               if 'pull_request' not in issue and MARKER in (issue.get('body') or '')]
    if len(matches) > 1:
        raise ValueError('Multiple monitor issues found; reconcile before updating')
    issue = matches[0] if matches else None
    if not has_changes:
        if issue and issue['state'] == 'open':
            run('gh', 'issue', 'close', str(issue['number']), '--repo', repository,
                '--reason', 'completed')
            print('Closed monitor issue: reviewed baseline matches upstream.')
        else:
            print('No upstream differences; no issue mutation.')
        return
    if issue and state in (issue.get('body') or ''):
        print('Upstream content unchanged; no issue mutation.')
        return
    # Stay below GitHub's issue body limit; full report remains a workflow artifact.
    if len(body) > 60000:
        body = body[:55000].rsplit('\n', 1)[0] + '\n\nReport truncated; download the complete upstream-report workflow artifact.\n'
    with tempfile.TemporaryDirectory() as temp:
        file = Path(temp) / 'body.md'
        file.write_text(body)
        if issue:
            print(run('gh', 'issue', 'edit', str(issue['number']), '--repo', repository,
                      '--body-file', str(file)))
            if issue['state'] == 'closed':
                run('gh', 'issue', 'reopen', str(issue['number']), '--repo', repository)
        else:
            print(run('gh', 'issue', 'create', '--repo', repository, '--title', TITLE,
                      '--label', 'needs-triage', '--body-file', str(file)))


def reviewed_manifest(root):
    registry = json.loads((root / 'provenance/baselines.json').read_text())
    reviewed = next(item for item in registry['baselines']
                    if item['revision'] == registry['reviewed_revision'])
    source = json.loads((root / reviewed['manifest']).read_text())
    if source['commit'] != reviewed['revision']:
        raise ValueError('Reviewed baseline revision does not match source manifest')
    active = json.loads((root / 'provenance/ownership.json').read_text())
    transition = json.loads((root / 'provenance/upstream-transition.json').read_text())
    if transition['to_revision'] != source['commit']:
        raise ValueError('Transition does not match reviewed baseline')
    owners = {item['source']: item for item in active['items']}
    owners.update({item['source']: item for item in transition['items']})
    return {'repository': source['repository'], 'version': source['plugin_version'],
            'commit': source['commit'], 'transition': transition,
            'items': [dict(owners.get(path, {}), source=path, sha256=digest)
                      for path, digest in source['files_sha256'].items()]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--publish', action='store_true', help='Create/update the tracking issue')
    parser.add_argument('--repository', default='nicksinai/pstack-codex')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--source-checkout', type=Path, help='Read an existing official-repository checkout instead of fetching upstream')
    args = parser.parse_args()
    manifest = reviewed_manifest(ROOT)
    if manifest['repository'] != UPSTREAM:
        raise ValueError('Unexpected upstream repository')
    if args.source_checkout:
        revision, hashes = snapshot(args.source_checkout)
    else:
        with tempfile.TemporaryDirectory(prefix='pstack-upstream-') as temp:
            checkout = Path(temp) / 'source'
            subprocess.run(['git', 'clone', '--depth=1', '--filter=blob:none', '--sparse',
                            UPSTREAM + '.git', str(checkout)], check=True)
            subprocess.run(['git', '-C', str(checkout), 'sparse-checkout', 'set', 'pstack'], check=True)
            revision, hashes = snapshot(checkout)
    delta = changes(manifest, hashes)
    state, body = report(manifest, revision, hashes, delta, args.repository)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(body)
    print(f'{len(delta)} upstream file differences; report: {args.output}')
    if args.publish:
        sync_issue(args.repository, state, body, needs_review(manifest, delta))


if __name__ == '__main__':
    main()
