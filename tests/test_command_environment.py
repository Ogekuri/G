import ast
import unittest
from pathlib import Path
from unittest import mock

from git_alias import core


class GraphicalEnvironmentDetectionTest(unittest.TestCase):
    """REQ-187 environment classification contract."""

    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_posix_without_display_returns_terminal(self):
        with (
            mock.patch.object(core.os, "name", "posix"),
            mock.patch.dict(core.os.environ, {"DISPLAY": "", "WAYLAND_DISPLAY": ""}),
        ):
            self.assertFalse(core._is_graphical_environment())

    def test_posix_with_display_returns_graphical(self):
        with (
            mock.patch.object(core.os, "name", "posix"),
            mock.patch.dict(core.os.environ, {"DISPLAY": ":0", "WAYLAND_DISPLAY": ""}),
        ):
            self.assertTrue(core._is_graphical_environment())

    def test_posix_with_wayland_display_returns_graphical(self):
        with (
            mock.patch.object(core.os, "name", "posix"),
            mock.patch.dict(
                core.os.environ, {"DISPLAY": "", "WAYLAND_DISPLAY": "wayland-0"}
            ),
        ):
            self.assertTrue(core._is_graphical_environment())

    def test_non_posix_returns_graphical(self):
        with (
            mock.patch.object(core.os, "name", "nt"),
            mock.patch.dict(core.os.environ, {"DISPLAY": "", "WAYLAND_DISPLAY": ""}),
        ):
            self.assertTrue(core._is_graphical_environment())


class EnvironmentCommandSelectionTest(unittest.TestCase):
    """REQ-186/REQ-187/REQ-188 dual-command selection contract."""

    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def _resolve(self):
        return core._environment_config_command_parts(
            "gp_command", core.DEFAULT_GP_COMMAND
        )

    def test_graphical_environment_selects_gfx_command(self):
        core.CONFIG["gp_command"] = "term-viewer"
        core.CONFIG["gp_command_gfx"] = "gfx-viewer --all"
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=True),
            mock.patch.object(core.shutil, "which", return_value="/usr/bin/gfx-viewer"),
        ):
            self.assertEqual(self._resolve(), ["gfx-viewer", "--all"])

    def test_graphical_environment_falls_back_when_gfx_empty(self):
        core.CONFIG["gp_command"] = "term-viewer"
        core.CONFIG["gp_command_gfx"] = ""
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=True),
            mock.patch.object(core.shutil, "which", return_value="/usr/bin/term-viewer"),
        ):
            self.assertEqual(self._resolve(), ["term-viewer"])

    def test_terminal_environment_ignores_gfx_command(self):
        core.CONFIG["gp_command"] = "term-viewer"
        core.CONFIG["gp_command_gfx"] = "gfx-viewer"
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core.shutil, "which", return_value="/usr/bin/term-viewer"),
        ):
            self.assertEqual(self._resolve(), ["term-viewer"])

    def test_graphical_environment_selects_editor_gfx_command(self):
        core.CONFIG["edit_command"] = "edit"
        core.CONFIG["edit_command_gfx"] = "gedit"
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=True),
            mock.patch.object(core.shutil, "which", return_value="/usr/bin/gedit"),
        ):
            self.assertEqual(
                core._environment_config_command_parts(
                    "edit_command", core.DEFAULT_CONFIG["edit_command"]
                ),
                ["gedit"],
            )


class ConfiguredDiffDefaultCommandTest(unittest.TestCase):
    """REQ-189 default diff command fallback contract."""

    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_diff_defaults_to_git_difftool_in_terminal_environment(self):
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=False),
            mock.patch.object(core.shutil, "which", return_value="/usr/bin/git"),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dcc([])
            run_command.assert_called_once_with(
                ["git", "difftool", "-d", "HEAD~1", "HEAD"]
            )

    def test_diff_uses_gfx_command_in_graphical_environment(self):
        core.CONFIG["diff_command"] = "icdiff"
        core.CONFIG["diff_command_gfx"] = "meld"
        with (
            mock.patch.object(core, "_is_graphical_environment", return_value=True),
            mock.patch.object(core.shutil, "which", return_value="/usr/bin/meld"),
            mock.patch.object(core, "run_command", return_value=None) as run_command,
        ):
            core.cmd_dc(["v1.0.0", "HEAD"])
            run_command.assert_called_once_with(["meld", "HEAD", "v1.0.0"])


class SubprocessWrapperIsolationTest(unittest.TestCase):
    """REQ-185 single subprocess interception point contract."""

    def test_subprocess_calls_exist_only_inside_run_checked(self):
        source = Path("src/git_alias/core.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        offenders = []
        for node in ast.walk(tree):
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            if node.name == "_run_checked":
                continue
            for sub in ast.walk(node):
                if (
                    isinstance(sub, ast.Call)
                    and isinstance(sub.func, ast.Attribute)
                    and isinstance(sub.func.value, ast.Name)
                    and sub.func.value.id == "subprocess"
                    and sub.func.attr
                    in ("run", "Popen", "call", "check_call", "check_output")
                ):
                    offenders.append(f"{node.name}: subprocess.{sub.func.attr}")
        self.assertEqual(offenders, [])

    def test_global_config_keys_define_paired_command_ids(self):
        self.assertEqual(
            core.GLOBAL_CONFIG_KEYS,
            (
                "edit_command",
                "gp_command",
                "gr_command",
                "diff_command",
                "edit_command_gfx",
                "gp_command_gfx",
                "gr_command_gfx",
                "diff_command_gfx",
            ),
        )
        self.assertEqual(core.DEFAULT_CONFIG["diff_command"], "git difftool -d")
        self.assertEqual(core.DEFAULT_CONFIG["edit_command_gfx"], "")
        self.assertEqual(core.DEFAULT_CONFIG["gp_command_gfx"], "")
        self.assertEqual(core.DEFAULT_CONFIG["gr_command_gfx"], "")
        self.assertEqual(core.DEFAULT_CONFIG["diff_command_gfx"], "")
