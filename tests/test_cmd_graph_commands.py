import unittest
from unittest import mock

from git_alias import core


class CmdGraphCommandsTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_cmd_gp_runs_default_command_template(self):
        with mock.patch.object(core.shutil, "which", return_value="/usr/bin/gitk"), \
             mock.patch.object(core, "run_command", return_value=None) as run_command:
            core.cmd_gp(["--date-order"])
        run_command.assert_called_once_with(["gitk", "--all", "--date-order"])

    def test_cmd_gr_runs_default_command_template(self):
        with mock.patch.object(core.shutil, "which", return_value="/usr/bin/gitk"), \
             mock.patch.object(core, "run_command", return_value=None) as run_command:
            core.cmd_gr(["--branches"])
        run_command.assert_called_once_with(["gitk", "--simplify-by-decoration", "--all", "--branches"])

    def test_cmd_gp_uses_configured_command_when_executable_is_available(self):
        core.CONFIG["gp_command"] = "python3 -m git_alias.viewer"
        with mock.patch.object(core.shutil, "which", return_value="/usr/bin/python3"), \
             mock.patch.object(core, "run_command", return_value=None) as run_command:
            core.cmd_gp(["--all"])
        run_command.assert_called_once_with(["python3", "-m", "git_alias.viewer", "--all"])

    def test_cmd_gr_raises_when_configured_executable_is_unavailable(self):
        core.CONFIG["gr_command"] = "missing-viewer --all"
        with mock.patch.object(core.shutil, "which", return_value=None), \
             mock.patch.object(core, "run_command", return_value=None) as run_command:
            with self.assertRaisesRegex(
                RuntimeError,
                "Configured gr_command executable 'missing-viewer' is not available on this system.",
            ):
                core.cmd_gr(["--tags"])
        run_command.assert_not_called()

    def test_cmd_gr_raises_when_configured_command_is_invalid(self):
        core.CONFIG["gr_command"] = 'gitk "unterminated'
        with mock.patch.object(core, "run_command", return_value=None) as run_command:
            with self.assertRaisesRegex(
                RuntimeError,
                "Configured gr_command command is invalid:",
            ):
                core.cmd_gr(["--tags"])
        run_command.assert_not_called()
