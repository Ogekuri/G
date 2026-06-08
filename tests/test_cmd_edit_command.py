import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class CmdEditCommandTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_cmd_ed_runs_validated_editor_command_for_each_path(self):
        core.CONFIG["edit_command"] = "code --wait"
        with mock.patch.object(core.shutil, "which", return_value="/usr/bin/code"), \
             mock.patch.object(core, "run_command", return_value=None) as run_command:
            core.cmd_ed(["~/one.txt", "two.txt"])
        run_command.assert_has_calls(
            [
                mock.call(["code", "--wait", core.os.path.expanduser("~/one.txt")]),
                mock.call(["code", "--wait", "two.txt"]),
            ]
        )

    def test_cmd_ed_raises_when_configured_executable_is_unavailable(self):
        core.CONFIG["edit_command"] = "missing-editor --wait"
        with mock.patch.object(core.shutil, "which", return_value=None), \
             mock.patch.object(core, "run_command", return_value=None) as run_command:
            with self.assertRaisesRegex(
                RuntimeError,
                "Configured edit_command executable 'missing-editor' is not available on this system.",
            ):
                core.cmd_ed(["README.md"])
        run_command.assert_not_called()

    def test_main_prints_error_and_exits_when_edit_command_is_unavailable(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)
        core.CONFIG["edit_command"] = "missing-editor --wait"
        stderr = io.StringIO()
        with mock.patch.object(core, "get_git_root", return_value=core.Path.cwd()), \
             mock.patch.object(core, "load_cli_config", return_value=None), \
             mock.patch.object(core.shutil, "which", return_value=None), \
             mock.patch.object(core, "run_command", return_value=None) as run_command, \
             contextlib.redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as exc:
                core.main(["ed", "README.md"], check_updates=False)
        self.assertEqual(exc.exception.code, 1)
        self.assertIn(
            "Configured edit_command executable 'missing-editor' is not available on this system.",
            stderr.getvalue(),
        )
        run_command.assert_not_called()
