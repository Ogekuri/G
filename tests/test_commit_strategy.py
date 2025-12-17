import unittest
from unittest import mock

from git_alias import core


class CommitStrategyTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_should_amend_returns_false_when_message_is_not_wip(self):
        with mock.patch.object(core, "_head_commit_message", return_value="fix bug"):
            self.assertFalse(core._should_amend_existing_commit())

    def test_should_amend_returns_false_when_commit_already_in_develop(self):
        with mock.patch.object(core, "_head_commit_message", return_value="wip: work in progress."), mock.patch.object(
            core, "_head_commit_hash", return_value="abc123"
        ), mock.patch.object(core, "get_branch", return_value="develop"), mock.patch.object(
            core, "_commit_exists_in_branch", return_value=True
        ):
            self.assertFalse(core._should_amend_existing_commit())

    def test_should_amend_returns_true_for_pending_wip(self):
        with mock.patch.object(core, "_head_commit_message", return_value="wip: work in progress."), mock.patch.object(
            core, "_head_commit_hash", return_value="abc123"
        ), mock.patch.object(core, "get_branch", return_value="develop"), mock.patch.object(
            core, "_commit_exists_in_branch", return_value=False
        ):
            self.assertTrue(core._should_amend_existing_commit())
