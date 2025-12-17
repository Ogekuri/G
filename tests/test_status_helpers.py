import unittest

from git_alias import core


class StatusHelpersTest(unittest.TestCase):
    def test_has_unstaged_changes_detects_worktree_modifications(self):
        lines = [" M file.txt", "?? new.txt"]
        self.assertTrue(core.has_unstaged_changes(lines))
        self.assertFalse(core.has_staged_changes(lines))

    def test_has_staged_changes_detects_index_entries(self):
        lines = ["M  file.txt", "A  another.txt"]
        self.assertFalse(core.has_unstaged_changes(lines))
        self.assertTrue(core.has_staged_changes(lines))

    def test_mixed_status_is_detected_correctly(self):
        lines = ["MM file.txt"]
        self.assertTrue(core.has_unstaged_changes(lines))
        self.assertTrue(core.has_staged_changes(lines))
