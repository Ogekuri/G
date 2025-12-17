import contextlib
import io
import subprocess
import unittest
from unittest import mock

from git_alias import core


class CmdWipTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_cmd_wip_creates_new_commit_when_not_amending(self):
        with mock.patch.object(core, "_git_status_lines", return_value=["A  file"]), mock.patch.object(
            core, "_should_amend_existing_commit", return_value=False
        ), mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                core.cmd_wip([])
            run_git.assert_called_once_with(["commit", "-m", "wip: work in progress."])
            self.assertIn("nuova commit", buffer.getvalue())

    def test_cmd_wip_uses_amend_when_requested(self):
        with mock.patch.object(core, "_git_status_lines", return_value=["A  file"]), mock.patch.object(
            core, "_should_amend_existing_commit", return_value=True
        ), mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                core.cmd_wip([])
            run_git.assert_called_once_with(["commit", "--amend", "-m", "wip: work in progress."])
            self.assertIn("--amend", buffer.getvalue())

    def test_cmd_wip_reports_error_when_git_commit_fails(self):
        status_side_effect = [
            ["A  file"],
            [" M file"],
        ]
        with mock.patch.object(core, "_git_status_lines", side_effect=status_side_effect), mock.patch.object(
            core, "_should_amend_existing_commit", return_value=False
        ), mock.patch.object(
            core, "run_git_cmd", side_effect=subprocess.CalledProcessError(1, ["git", "commit"])
        ):
            stdout = io.StringIO()
            stderr = io.StringIO()
            with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                with self.assertRaises(SystemExit):
                    core.cmd_wip([])
            self.assertIn("Impossibile eseguire git wip", stderr.getvalue())
