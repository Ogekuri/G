import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class CmdDiffAliasesTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_command_aliases_include_dc_and_dw(self):
        self.assertIn("dwc", core.COMMANDS)
        self.assertIn("dwcc", core.COMMANDS)
        self.assertIn("dcc", core.COMMANDS)
        self.assertIn("dccc", core.COMMANDS)
        self.assertIn("dcd", core.COMMANDS)
        self.assertIn("dcm", core.COMMANDS)
        self.assertIn("ddm", core.COMMANDS)
        self.assertIn("dc", core.COMMANDS)
        self.assertIn("dw", core.COMMANDS)
        self.assertNotIn("dwd", core.COMMANDS)
        self.assertIn("dwc", core.HELP_TEXTS)
        self.assertIn("dwcc", core.HELP_TEXTS)
        self.assertIn("dcc", core.HELP_TEXTS)
        self.assertIn("dccc", core.HELP_TEXTS)
        self.assertIn("dcd", core.HELP_TEXTS)
        self.assertIn("dcm", core.HELP_TEXTS)
        self.assertIn("ddm", core.HELP_TEXTS)
        self.assertIn("dc", core.HELP_TEXTS)
        self.assertIn("dw", core.HELP_TEXTS)
        self.assertNotIn("dwd", core.HELP_TEXTS)
        self.assertNotIn("dr", core.COMMANDS)
        self.assertNotIn("dr", core.HELP_TEXTS)

    def test_cmd_dwc_runs_plain_git_difftool_when_unconfigured(self):
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dwc([])
            run_command.assert_called_once_with(["git", "difftool", "-d", "HEAD"])

    def test_cmd_dcc_runs_plain_git_difftool_when_unconfigured(self):
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dcc([])
            run_command.assert_called_once_with(
                ["git", "difftool", "-d", "HEAD~1", "HEAD"]
            )

    def test_cmd_dccc_runs_plain_git_difftool_when_unconfigured(self):
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dccc([])
            run_command.assert_called_once_with(
                ["git", "difftool", "-d", "HEAD~2", "HEAD"]
            )

    def test_cmd_dwcc_runs_plain_git_difftool_when_unconfigured(self):
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dwcc([])
            run_command.assert_called_once_with(["git", "difftool", "-d", "HEAD~1"])

    def test_cmd_dc_rejects_zero_refs(self):
        with mock.patch.object(core, "run_command") as run_command:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_dc([])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertIn("<ref>", err.getvalue())
            run_command.assert_not_called()

    def test_cmd_dc_rejects_more_than_two_refs(self):
        with mock.patch.object(core, "run_command") as run_command:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_dc(["HEAD", "HEAD~1", "HEAD~2"])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertIn("<ref>", err.getvalue())
            run_command.assert_not_called()

    def test_cmd_dc_defaults_ref_prev_to_commit_preceding_ref(self):
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dc(["v1.2.3"])
            run_command.assert_called_once_with(
                ["git", "difftool", "-d", "v1.2.3~1", "v1.2.3"]
            )

    def test_cmd_dc_runs_plain_git_difftool_from_ref_prev_to_ref(self):
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dc(["v1.0.0", "HEAD"])
            run_command.assert_called_once_with(
                ["git", "difftool", "-d", "HEAD", "v1.0.0"]
            )

    def test_cmd_dw_requires_exactly_one_ref(self):
        with mock.patch.object(core, "run_command") as run_command:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_dw([])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertIn("requires exactly one ref", err.getvalue())
            run_command.assert_not_called()

    def test_cmd_dw_runs_plain_git_difftool_with_ref(self):
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dw(["v1.0.0"])
            run_command.assert_called_once_with(["git", "difftool", "-d", "v1.0.0"])

    def test_cmd_dcd_runs_plain_git_difftool_between_develop_and_work(self):
        with (
            mock.patch.object(
                core, "get_branch", side_effect=["integration/develop", "feature/work"]
            ) as get_branch,
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dcd([])
            get_branch.assert_has_calls([mock.call("develop"), mock.call("work")])
            run_command.assert_called_once_with(
                ["git", "difftool", "-d", "integration/develop", "feature/work"]
            )

    def test_cmd_dcm_runs_plain_git_difftool_between_master_and_work(self):
        with (
            mock.patch.object(
                core, "get_branch", side_effect=["release/master", "feature/work"]
            ) as get_branch,
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dcm([])
            get_branch.assert_has_calls([mock.call("master"), mock.call("work")])
            run_command.assert_called_once_with(
                ["git", "difftool", "-d", "release/master", "feature/work"]
            )

    def test_cmd_ddm_runs_plain_git_difftool_between_master_and_develop(self):
        with (
            mock.patch.object(
                core, "get_branch", side_effect=["release/master", "integration/develop"]
            ) as get_branch,
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_ddm([])
            get_branch.assert_has_calls([mock.call("master"), mock.call("develop")])
            run_command.assert_called_once_with(
                ["git", "difftool", "-d", "release/master", "integration/develop"]
            )

    def test_diff_aliases_inject_terminal_diff_command_as_extcmd(self):
        core.CONFIG["diff_command"] = "icdiff --line-numbers"
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core.shutil, "which", return_value="/usr/bin/icdiff"),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dcc([])
            run_command.assert_called_once_with(
                [
                    "git",
                    "difftool",
                    "-d",
                    "--extcmd=icdiff --line-numbers",
                    "HEAD~1",
                    "HEAD",
                ]
            )

    def test_diff_aliases_inject_gfx_diff_command_as_extcmd(self):
        core.CONFIG["diff_command"] = "icdiff"
        core.CONFIG["diff_command_gfx"] = "/opt/sublime_merge/sublime_merge difftool"
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=True),
            mock.patch.object(
                core.shutil, "which", return_value="/opt/sublime_merge/sublime_merge"
            ),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dwc([])
            run_command.assert_called_once_with(
                [
                    "git",
                    "difftool",
                    "-d",
                    "--extcmd=/opt/sublime_merge/sublime_merge difftool",
                    "HEAD",
                ]
            )
