import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class CmdDiffAliasesTest(unittest.TestCase):
    def test_command_aliases_are_renamed_to_dwc_and_dcc(self):
        self.assertIn("dwc", core.COMMANDS)
        self.assertIn("dwcc", core.COMMANDS)
        self.assertIn("dcc", core.COMMANDS)
        self.assertIn("dccc", core.COMMANDS)
        self.assertIn("dwc", core.HELP_TEXTS)
        self.assertIn("dwcc", core.HELP_TEXTS)
        self.assertIn("dcc", core.HELP_TEXTS)
        self.assertIn("dccc", core.HELP_TEXTS)
        self.assertNotIn("dw", core.COMMANDS)
        self.assertNotIn("dc", core.COMMANDS)

    def test_cmd_dw_runs_difftool_against_head(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_dw([])
            run_git.assert_called_once_with(["difftool", "-d", "HEAD"], [])

    def test_cmd_dc_runs_difftool_between_latest_commits(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_dc([])
            run_git.assert_called_once_with(["difftool", "-d", "HEAD~1", "HEAD"], [])

    def test_cmd_dccc_runs_difftool_between_third_last_and_latest_commit(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_dccc([])
            run_git.assert_called_once_with(["difftool", "-d", "HEAD~2", "HEAD"], [])

    def test_cmd_dwcc_runs_difftool_against_penultimate_commit(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_dwcc([])
            run_git.assert_called_once_with(["difftool", "-d", "HEAD~1"], [])

    def test_cmd_d_requires_exactly_two_refs(self):
        with mock.patch.object(core, "run_git_cmd") as run_git:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_d(["HEAD"])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertIn("requires exactly two refs", err.getvalue())
            run_git.assert_not_called()

    def test_cmd_d_runs_difftool_with_two_refs(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_d(["v1.0.0", "HEAD"])
            run_git.assert_called_once_with(["difftool", "-d", "v1.0.0", "HEAD"])
