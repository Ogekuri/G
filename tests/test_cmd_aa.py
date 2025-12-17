import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class CmdAaTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_cmd_aa_requires_unstaged_changes(self):
        with mock.patch.object(core, "_git_status_lines", return_value=[]), mock.patch.object(
            core, "run_git_cmd"
        ) as run_git:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_aa([])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertIn("Nessuna modifica", err.getvalue())
            run_git.assert_not_called()

    def test_cmd_aa_runs_git_add_when_needed(self):
        with mock.patch.object(core, "_git_status_lines", return_value=["?? file.txt"]), mock.patch.object(
            core, "run_git_cmd", return_value=None
        ) as run_git:
            core.cmd_aa([])
            run_git.assert_called_once_with(["add", "--all"], [])
