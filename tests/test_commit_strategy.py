import unittest
from unittest import mock

from git_alias import core


class CommitStrategyTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_should_amend_returns_false_when_message_is_not_wip(self):
        with mock.patch.object(core, "_head_commit_message", return_value="fix bug"):
            result = core._should_amend_existing_commit()
            self.assertIsInstance(result, tuple)
            self.assertFalse(result[0])
            self.assertIn("not a WIP commit", result[1])

    def test_should_amend_returns_false_when_commit_already_in_develop(self):
        with mock.patch.object(core, "_head_commit_message", return_value="wip: work in progress."), mock.patch.object(
            core, "_head_commit_hash", return_value="abc123"
        ), mock.patch.object(core, "get_branch", return_value="develop"), mock.patch.object(
            core, "_commit_exists_in_branch", return_value=True
        ):
            result = core._should_amend_existing_commit()
            self.assertIsInstance(result, tuple)
            self.assertFalse(result[0])
            self.assertIn("already contained", result[1])

    def test_should_amend_returns_true_for_pending_wip(self):
        with mock.patch.object(core, "_head_commit_message", return_value="wip: work in progress."), mock.patch.object(
            core, "_head_commit_hash", return_value="abc123"
        ), mock.patch.object(core, "get_branch", return_value="develop"), mock.patch.object(
            core, "_commit_exists_in_branch", return_value=False
        ):
            result = core._should_amend_existing_commit()
            self.assertIsInstance(result, tuple)
            self.assertTrue(result[0])
            self.assertIn("pending locally", result[1])
