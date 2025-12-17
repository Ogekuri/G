import contextlib
import io
import subprocess
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
            core, "_should_amend_existing_commit", return_value=False
        ), mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                core.cmd_cm(["message"])
            run_git.assert_called_once_with(["commit", "-F", "-"], input="message", text=True)
            self.assertIn("nuova commit", buffer.getvalue())

    def test_cmd_cm_uses_amend_when_wip_not_on_develop(self):
        lines = ["A  file.txt"]
        with mock.patch.object(core, "_git_status_lines", return_value=lines), mock.patch.object(
            core, "_should_amend_existing_commit", return_value=True
        ), mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                core.cmd_cm(["message"])
            run_git.assert_called_once_with(["commit", "--amend", "-F", "-"], input="message", text=True)
            self.assertIn("--amend", buffer.getvalue())

    def test_cmd_cm_reports_error_when_git_commit_fails_due_to_unstaged(self):
        status_side_effect = [
            ["A  file.txt"],  # initial readiness check passes
            [" M file.txt"],  # re-check after git failure shows unstaged data
        ]
        with mock.patch.object(core, "_git_status_lines", side_effect=status_side_effect), mock.patch.object(
            core, "_should_amend_existing_commit", return_value=False
        ), mock.patch.object(
            core,
            "run_git_cmd",
            side_effect=subprocess.CalledProcessError(1, ["git", "commit"]),
        ):
            stdout = io.StringIO()
            stderr = io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                with self.assertRaises(SystemExit):
                    core.cmd_cm(["message"])
            self.assertIn("Impossibile eseguire git cm", stderr.getvalue())
