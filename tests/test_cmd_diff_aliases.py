import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class CmdDiffAliasesTest(unittest.TestCase):
    def test_cmd_dw_runs_difftool_against_head(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_dw([])
            run_git.assert_called_once_with(["difftool", "-d", "HEAD"], [])

    def test_cmd_dc_runs_difftool_between_latest_commits(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_dc([])
            run_git.assert_called_once_with(["difftool", "-d", "HEAD~1", "HEAD"], [])

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
