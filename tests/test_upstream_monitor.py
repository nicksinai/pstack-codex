"""Verify detection and issue lifecycle without creating test issues."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('monitor', Path(__file__).resolve().parents[1] / 'scripts/check-upstream.py')
monitor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(monitor)


class MonitorTests(unittest.TestCase):
    def setUp(self):
        self.manifest = {'version': '1', 'commit': 'a' * 40, 'items': [
            {'source': 'skills/a/SKILL.md', 'sha256': 'old', 'target': 'plugin/pstack/skills/pstack-a/SKILL.md'},
            {'source': 'removed', 'sha256': 'gone', 'target': None, 'disposition': 'deferred', 'reason': 'Excluded'},
        ]}
        self.hashes = {'skills/a/SKILL.md': 'new', 'added': 'new'}

    def test_complete_inventory_including_unmapped_and_deferred(self):
        delta = monitor.changes(self.manifest, self.hashes)
        self.assertEqual(delta, [('added', 'added'), ('removed', 'removed'), ('skills/a/SKILL.md', 'changed')])
        state, body = monitor.report(self.manifest, 'b' * 40, self.hashes, delta, 'owner/port')
        self.assertIn('Unmapped addition', body)
        self.assertIn('deferred', body)
        self.assertIn('plugin/pstack/skills/pstack-a/SKILL.md', body)
        self.assertIn('/blob/' + 'a' * 40 + '/pstack/removed', body)
        other_state, _ = monitor.report(self.manifest, 'c' * 40, self.hashes, delta, 'owner/port')
        self.assertEqual(state, other_state)
        self.assertEqual(monitor.changes(self.manifest, {x['source']: x['sha256'] for x in self.manifest['items']}), [])

    def test_create_one_issue_with_triage_label(self):
        with patch.object(monitor, 'run', side_effect=['[[]]', 'issue-url']) as run:
            monitor.sync_issue('owner/port', 'state', 'body', True)
        self.assertEqual(run.call_count, 2)
        self.assertIn('needs-triage', run.call_args.args)
        self.assertIn('--body-file', run.call_args.args)

    def test_unchanged_issue_stays_quiet_even_when_closed(self):
        for status in ('open', 'closed'):
            issue = {'number': 9, 'state': status, 'body': monitor.MARKER + '\nstate'}
            with patch.object(monitor, 'run', return_value=json.dumps([[issue]])) as run:
                monitor.sync_issue('owner/port', 'state', 'body', True)
            self.assertEqual(run.call_count, 1)

    def test_new_content_updates_and_reopens_existing_issue(self):
        issue = {'number': 9, 'state': 'closed', 'body': monitor.MARKER + '\nold-state'}
        with patch.object(monitor, 'run', side_effect=[json.dumps([[issue]]), 'edited', 'reopened']) as run:
            monitor.sync_issue('owner/port', 'new-state', 'body', True)
        self.assertEqual(run.call_count, 3)
        self.assertEqual(run.call_args.args[:4], ('gh', 'issue', 'reopen', '9'))

    def test_baseline_catches_up_and_closes_issue(self):
        issue = {'number': 9, 'state': 'open', 'body': monitor.MARKER}
        with patch.object(monitor, 'run', side_effect=[json.dumps([[issue]]), 'closed']) as run:
            monitor.sync_issue('owner/port', 'state', 'body', False)
        self.assertEqual(run.call_args.args[:4], ('gh', 'issue', 'close', '9'))

    def test_snapshot_ignores_untracked_files_and_does_not_follow_symlinks(self):
        with tempfile.TemporaryDirectory() as temp:
            repo = Path(temp)
            monitor.run('git', 'init', str(repo))
            path = repo / 'pstack/.cursor-plugin/plugin.json'
            path.parent.mkdir(parents=True)
            path.write_text('{}')
            (repo / 'pstack/link').symlink_to('/does-not-exist')
            monitor.run('git', '-C', str(repo), 'add', '.')
            monitor.run('git', '-C', str(repo), '-c', 'user.name=Test', '-c', 'user.email=test@example.com', 'commit', '-m', 'Fixture')
            (repo / 'pstack/untracked').write_text('ignore')
            _, hashes = monitor.snapshot(repo)
            self.assertEqual(set(hashes), {'.cursor-plugin/plugin.json', 'link'})
            path.unlink()
            with self.assertRaises(FileNotFoundError):
                monitor.snapshot(repo)


if __name__ == '__main__':
    unittest.main()
