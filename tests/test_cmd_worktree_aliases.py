import unittest
from unittest import mock

from git_alias import core


class CmdWorktreeAliasesTest(unittest.TestCase):
    def test_worktree_aliases_are_registered_with_help(self):
        for alias in ("wt", "wtl", "wtp", "wtr"):
            self.assertIn(alias, core.COMMANDS)
            self.assertIn(alias, core.HELP_TEXTS)

    def test_cmd_wt_runs_worktree_list(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_wt([])
            run_git.assert_called_once_with(["worktree", "list"], [])

    def test_cmd_wtl_forwards_list_arguments(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_wtl(["--porcelain", "-z"])
            run_git.assert_called_once_with(["worktree", "list"], ["--porcelain", "-z"])

    def test_cmd_wtp_forwards_prune_arguments(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_wtp(["--expire", "now", "-n", "-v"])
            run_git.assert_called_once_with(["worktree", "prune"], ["--expire", "now", "-n", "-v"])

    def test_cmd_wtr_forwards_remove_arguments(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_wtr(["-f", "../feature-tree"])
            run_git.assert_called_once_with(["worktree", "remove"], ["-f", "../feature-tree"])
