import unittest
from unittest import mock

from git_alias import core


class RemoteStatusTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_has_remote_develop_updates_true_when_remote_ahead(self):
        with mock.patch.object(core, "run_git_text", return_value="0 2"):
            self.assertTrue(core.has_remote_develop_updates())

    def test_has_remote_master_updates_false_when_in_sync(self):
        with mock.patch.object(core, "run_git_text", return_value="1 0"):
            self.assertFalse(core.has_remote_master_updates())
