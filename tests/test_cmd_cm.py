import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class CmdCmTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_cmd_cm_fails_when_unstaged_changes_exist(self):
        with mock.patch.object(core, "_git_status_lines", return_value=[" M file.txt"]), mock.patch.object(
            core, "run_git_cmd"
        ) as run_git:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_cm(["message"])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertIn("modifiche non ancora aggiunte", err.getvalue())
            run_git.assert_not_called()

    def test_cmd_cm_fails_when_stage_is_empty(self):
        with mock.patch.object(core, "_git_status_lines", return_value=[]), mock.patch.object(
            core, "run_git_cmd"
        ) as run_git:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_cm(["message"])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertIn("staging è vuota", err.getvalue())
            run_git.assert_not_called()

    def test_cmd_cm_invokes_git_commit_when_checks_pass(self):
        lines = ["A  file.txt"]
        with mock.patch.object(core, "_git_status_lines", return_value=lines), mock.patch.object(
            core, "run_git_cmd", return_value=None
        ) as run_git:
            core.cmd_cm(["message"])
            run_git.assert_called_once_with(["commit", "-m"], ["message"])
