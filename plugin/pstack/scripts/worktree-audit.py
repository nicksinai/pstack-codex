#!/usr/bin/env python3
"""Read-only Git worktree audit. Suggestions never authorize deletion."""
import argparse
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys


def git(repo, *args):
    result = subprocess.run(['git', '-C', str(repo), *args], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE, env={**os.environ, 'GIT_OPTIONAL_LOCKS': '0'})
    if result.returncode:
        raise ValueError(result.stderr.decode(errors='replace').strip() or 'Git command failed')
    return result.stdout


def canonical(path):
    return str(Path(path).resolve())


def worktrees(raw):
    rows, current = [], {}
    for item in raw.split(b'\0'):
        if not item:
            if current:
                rows.append(current)
                current = {}
            continue
        key, _, value = item.partition(b' ')
        current[key.decode()] = os.fsdecode(value)
    if current:
        rows.append(current)
    return rows


def status_counts(raw):
    items, index = raw.split(b'\0'), 0
    result = {'tracked': [], 'untracked': [], 'ignored': []}
    while index < len(items):
        entry = items[index]
        index += 1
        if not entry:
            continue
        code, name = entry[:2], os.fsdecode(entry[3:])
        category = 'untracked' if code == b'??' else 'ignored' if code == b'!!' else 'tracked'
        result[category].append(name)
        # Porcelain v1 -z rename/copy records have a second path field.
        if b'R' in code or b'C' in code:
            if index < len(items):
                result[category].append(os.fsdecode(items[index]))
                index += 1
    return result


def disk_size(path):
    total = 0
    def fail(error):
        raise error
    for directory, dirs, files in os.walk(path, followlinks=False, onerror=fail):
        for name in files:
            total += os.lstat(os.path.join(directory, name)).st_size
    return total


def activity_for(path, evidence, now):
    mapping = evidence.get('worktrees', {})
    entry = mapping.get(path) if isinstance(mapping, dict) else None
    if not isinstance(entry, dict):
        return {'state': 'unknown'}
    # The producer is responsible for metadata-scoped history and current host liveness.
    if not isinstance(entry.get('sources'), list) or not entry['sources']:
        return {'state': 'unknown'}
    if type(entry.get('active')) is not bool or type(entry.get('pinned')) is not bool:
        return {'state': 'unknown'}
    if entry['active'] or entry['pinned']:
        return {**entry, 'state': 'in-use'}
    try:
        timestamp = dt.datetime.fromisoformat(entry['last_activity'].replace('Z', '+00:00'))
        if timestamp.tzinfo is None or timestamp > now:
            raise ValueError('ambiguous activity timestamp')
    except (KeyError, TypeError, AttributeError, ValueError):
        return {**entry, 'state': 'unknown'}
    return {**entry, 'state': 'recent' if (now - timestamp).total_seconds() <= 4 * 86400 else 'inactive'}


def audit(args):
    repo = canonical(os.fsdecode(git(args.repo, 'rev-parse', '--show-toplevel')).strip())
    rows = worktrees(git(repo, 'worktree', 'list', '--porcelain', '-z'))
    evidence = {}
    if args.activity:
        with open(args.activity, encoding='utf-8') as stream:
            evidence = json.load(stream)
        if not isinstance(evidence, dict):
            raise ValueError('Activity evidence must be an object')
        if evidence.get('version') != 1 or canonical(evidence.get('repository', '')) != canonical(rows[0]['worktree']):
            raise ValueError('Activity evidence repository/version does not match main worktree')
        observed = dt.datetime.fromisoformat(evidence['observed_at'].replace('Z', '+00:00'))
        age = (dt.datetime.now(dt.timezone.utc) - observed).total_seconds() if observed.tzinfo else -1
        if not 0 <= age <= 3600:
            raise ValueError('Activity evidence must have a timezone and be observed within one hour')
    trunk = args.trunk
    if not trunk:
        try:
            trunk = git(repo, 'symbolic-ref', '--quiet', 'refs/remotes/origin/HEAD').decode().strip()
        except ValueError:
            trunk = None
    trunk_head = None
    if trunk:
        trunk_head = git(repo, 'rev-parse', '--verify', trunk + '^{commit}').decode().strip()
    now = dt.datetime.now(dt.timezone.utc)
    output = []
    for offset, entry in enumerate(rows):
        path = canonical(entry['worktree'])
        row = {'path': path, 'registration': entry, 'trunk': trunk, 'trunk_head': trunk_head,
               'bucket': 'review', 'reasons': [], 'pr': 'unknown', 'remote': 'unknown'}
        try:
            row['bytes'] = disk_size(path)
        except OSError:
            row['bytes'] = None
            row['reasons'].append('size-inspection-incomplete')
        try:
            head = git(path, 'rev-parse', 'HEAD').decode().strip()
            row['head'] = head
            row['head_age_days'] = (int(now.timestamp()) - int(git(path, 'log', '-1', '--format=%ct'))) // 86400
            row['dirty'] = status_counts(git(path, 'status', '--porcelain=v1', '-z', '--untracked-files=all', '--ignored'))
            row['branch'] = entry.get('branch', '').removeprefix('refs/heads/')
            if trunk_head:
                check = subprocess.run(['git', '-C', path, 'merge-base', '--is-ancestor', head, trunk_head], capture_output=True)
                row['merged'] = 'yes' if check.returncode == 0 else 'no' if check.returncode == 1 else 'unknown'
            else:
                row['merged'] = 'unknown'
            try:
                upstream = git(path, 'rev-parse', '--symbolic-full-name', '@{upstream}').decode().strip()
                if not upstream.startswith('refs/remotes/'):
                    raise ValueError('Upstream is not a remote-tracking ref')
                ahead, behind = map(int, git(path, 'rev-list', '--left-right', '--count', 'HEAD...' + upstream).split())
                row['remote'] = {'ref': upstream, 'ahead': ahead, 'behind': behind, 'cached': True}
            except ValueError:
                row['remote'] = 'detached-or-no-upstream'
            if args.github and row['branch']:
                command = ['gh', 'pr', 'list', '--head', row['branch'], '--state', 'all', '--limit', '1000',
                           '--json', 'number,state,headRefOid,url']
                query = subprocess.run(command, cwd=path, capture_output=True)
                if query.returncode == 0:
                    parsed = json.loads(query.stdout)
                    if isinstance(parsed, list) and len(parsed) < 1000:
                        row['pr'] = parsed
            row['activity'] = activity_for(path, evidence, now)
            reasons = row['reasons']
            if offset == 0 or path == repo:
                reasons.append('primary-or-invoking-worktree')
            if 'locked' in entry or 'prunable' in entry:
                reasons.append('locked-or-prunable-registration-needs-review')
            if row['dirty']['tracked']:
                reasons.append('tracked-uncommitted-work')
            if row['dirty']['untracked'] or row['dirty']['ignored']:
                reasons.append('untracked-or-ignored-data-needs-disposition')
            if row['activity']['state'] != 'inactive':
                reasons.append('activity-' + row['activity']['state'])
            if not isinstance(row['remote'], dict) or row['remote']['ahead']:
                reasons.append('unpushed-or-unknown-remote-state')
            if row['pr'] == 'unknown':
                reasons.append('pr-state-unknown')
            elif any(pr['state'] == 'OPEN' for pr in row['pr']):
                reasons.append('open-pr')
            exact_merged_pr = isinstance(row['pr'], list) and any(
                pr['state'] == 'MERGED' and pr['headRefOid'] == head for pr in row['pr'])
            if row['merged'] != 'yes' and not exact_merged_pr:
                reasons.append('head-not-proven-integrated')
            row['bucket'] = ('hold-review' if 'size-inspection-incomplete' in reasons else
                             'candidate-needs-confirmation' if not reasons else
                             'hold-wip' if row['dirty']['tracked'] else
                             'hold-open-pr' if 'open-pr' in reasons else
                             'verify-recent-chat' if row['activity']['state'] == 'recent' else 'hold-review')
        except (ValueError, OSError, KeyError, TypeError, json.JSONDecodeError) as error:
            row['bucket'] = 'hold-review'
            row['reasons'].append('audit-incomplete: ' + str(error))
        output.append(row)
    return {'version': 1, 'observed_at': now.isoformat(), 'repository': canonical(rows[0]['worktree']),
            'ref_freshness': 'cached; no fetch performed',
            'worktrees': sorted(output, key=lambda row: row['bytes'] or 0, reverse=True)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('repo', nargs='?', default='.')
    parser.add_argument('--trunk', help='Verified current trunk ref, e.g. refs/remotes/origin/main')
    parser.add_argument('--github', action='store_true', help='Query PR metadata with recipient-authenticated gh; no fetch or writes')
    parser.add_argument('--activity', help='Private scoped activity evidence JSON; see cleanup playbook')
    args = parser.parse_args()
    try:
        print(json.dumps(audit(args), indent=2, ensure_ascii=True))
    except (ValueError, OSError, KeyError, TypeError, IndexError) as error:
        print('Audit unavailable: ' + str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
