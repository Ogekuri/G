import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class CmdRaTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_cmd_ra_requires_work_branch(self):
        with mock.patch.object(core, "_current_branch_name", return_value="feature"), mock.patch.object(
            core, "get_branch", return_value="work"
        ):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_ra([])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertIn("git ra must be executed from the work branch", err.getvalue())

    def test_cmd_ra_fails_with_unstaged_changes(self):
        with mock.patch.object(core, "_current_branch_name", return_value="work"), mock.patch.object(
            core, "_git_status_lines", return_value=[" M file.txt"]
        ):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_ra([])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertIn("unstaged changes are still present", err.getvalue())

    def test_cmd_ra_fails_with_empty_staging(self):
        with mock.patch.object(core, "_current_branch_name", return_value="work"), mock.patch.object(
            core, "_git_status_lines", return_value=[]
        ):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_ra([])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertIn("the staging area is empty", err.getvalue())

    def test_cmd_ra_runs_reset_when_ready(self):
        with mock.patch.object(core, "_current_branch_name", return_value="work"), mock.patch.object(
            core, "_git_status_lines", return_value=["M  file.txt"]
        ), mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_ra([])
            run_git.assert_called_once_with(["reset", "--mixed"], [])
