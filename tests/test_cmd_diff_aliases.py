import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class CmdDiffAliasesTest(unittest.TestCase):
    def test_command_aliases_include_dc_and_dw(self):
        self.assertIn("dwc", core.COMMANDS)
        self.assertIn("dwcc", core.COMMANDS)
        self.assertIn("dcc", core.COMMANDS)
        self.assertIn("dccc", core.COMMANDS)
        self.assertIn("dc", core.COMMANDS)
        self.assertIn("dw", core.COMMANDS)
        self.assertIn("dwd", core.COMMANDS)
        self.assertIn("dwc", core.HELP_TEXTS)
        self.assertIn("dwcc", core.HELP_TEXTS)
        self.assertIn("dcc", core.HELP_TEXTS)
        self.assertIn("dccc", core.HELP_TEXTS)
        self.assertIn("dc", core.HELP_TEXTS)
        self.assertIn("dw", core.HELP_TEXTS)
        self.assertIn("dwd", core.HELP_TEXTS)
        self.assertNotIn("dr", core.COMMANDS)
        self.assertNotIn("dr", core.HELP_TEXTS)

    def test_cmd_dwc_runs_difftool_against_head(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_dwc([])
            run_git.assert_called_once_with(["difftool", "-d", "HEAD"], [])

    def test_cmd_dcc_runs_difftool_between_latest_commits(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_dcc([])
            run_git.assert_called_once_with(["difftool", "-d", "HEAD~1", "HEAD"], [])

    def test_cmd_dccc_runs_difftool_between_third_last_and_latest_commit(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_dccc([])
            run_git.assert_called_once_with(["difftool", "-d", "HEAD~2", "HEAD"], [])

    def test_cmd_dwcc_runs_difftool_against_penultimate_commit(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_dwcc([])
            run_git.assert_called_once_with(["difftool", "-d", "HEAD~1"], [])

    def test_cmd_dc_requires_exactly_two_refs(self):
        with mock.patch.object(core, "run_git_cmd") as run_git:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_dc(["HEAD"])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertIn("requires exactly two refs", err.getvalue())
            run_git.assert_not_called()

    def test_cmd_dc_runs_difftool_with_two_refs(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_dc(["v1.0.0", "HEAD"])
            run_git.assert_called_once_with(["difftool", "-d", "v1.0.0", "HEAD"])

    def test_cmd_dw_requires_exactly_one_ref(self):
        with mock.patch.object(core, "run_git_cmd") as run_git:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_dw([])
            self.assertNotEqual(ctx.exception.code, 0)
            self.assertIn("requires exactly one ref", err.getvalue())
            run_git.assert_not_called()

    def test_cmd_dw_runs_difftool_with_ref(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_dw(["v1.0.0"])
            run_git.assert_called_once_with(["difftool", "-d", "v1.0.0"])

    def test_cmd_dwd_runs_difftool_between_configured_work_and_develop(self):
        with (
            mock.patch.object(
                core, "get_branch", side_effect=["feature/work", "integration/develop"]
            ) as get_branch,
            mock.patch.object(core, "run_git_cmd", return_value=None) as run_git,
        ):
            core.cmd_dwd([])
            get_branch.assert_has_calls([mock.call("work"), mock.call("develop")])
            run_git.assert_called_once_with(
                ["difftool", "-d", "feature/work", "integration/develop"], []
            )

    def test_command_handlers_match_cmd_plus_command_name(self):
        for command, handler in core.COMMANDS.items():
            self.assertEqual(handler.__name__, f"cmd_{command}")
