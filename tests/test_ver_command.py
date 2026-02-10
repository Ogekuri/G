import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from git_alias import core


class VerCommandTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)
        core.CONFIG["ver_rules"] = core.DEFAULT_CONFIG["ver_rules"]

    @staticmethod
    def _set_rules(rules):
        core.CONFIG["ver_rules"] = rules

    def test_cmd_ver_prints_shared_version(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "module.py").write_text('__version__ = "1.2.3"\n', encoding="utf-8")
            (root / "README.md").write_text('Current version "1.2.3"\n', encoding="utf-8")
            self._set_rules(
                [
                    {"pattern": "module.py", "regex": r'__version__\s*=\s*"(\d+\.\d+\.\d+)"'},
                    {"pattern": "README.md", "regex": r'"(\d+\.\d+\.\d+)"'},
                ]
            )
            with mock.patch.object(core, "get_git_root", return_value=root):
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    core.cmd_ver([])
                self.assertEqual(buffer.getvalue().strip(), "1.2.3")

    def test_cmd_ver_anchors_src_glob_at_root(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "src" / "git_alias").mkdir(parents=True)
            (root / "src" / "git_alias" / "__init__.py").write_text(
                '__version__ = "1.2.3"\n', encoding="utf-8"
            )
            (root / "prova" / "src").mkdir(parents=True)
            (root / "prova" / "src" / "__init__.py").write_text(
                '__version__ = "2.0.0"\n', encoding="utf-8"
            )
            self._set_rules(
                [
                    {"pattern": "src/**/*.py", "regex": r'__version__\s*=\s*["\']?(\d+\.\d+\.\d+)["\']?'},
                ]
            )
            with mock.patch.object(core, "get_git_root", return_value=root):
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    core.cmd_ver([])
                self.assertEqual(buffer.getvalue().strip(), "1.2.3")

    def test_cmd_ver_normalizes_git_ls_files_paths(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "src" / "debriddo").mkdir(parents=True)
            (root / "src" / "debriddo" / "main.py").write_text(
                '__version__ = "1.2.3"\n', encoding="utf-8"
            )
            self._set_rules(
                [
                    {"pattern": "src/**/*.py", "regex": r'__version__\s*=\s*["\']?(\d+\.\d+\.\d+)["\']?'},
                ]
            )
            proc = mock.Mock(stdout="src\\debriddo\\main.py\n", stderr="")
            with mock.patch.object(core, "get_git_root", return_value=root):
                with mock.patch("subprocess.run", return_value=proc):
                    buffer = io.StringIO()
                    with contextlib.redirect_stdout(buffer):
                        core.cmd_ver([])
                    self.assertEqual(buffer.getvalue().strip(), "1.2.3")

    def test_cmd_ver_detects_conflict(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "module.py").write_text("__version__ =  '1.2.3'\n", encoding="utf-8")
            (root / "second.py").write_text('__version__ = "2.0.0"\n', encoding="utf-8")
            self._set_rules(
                [
                    {"pattern": "*.py", "regex": r'__version__\s*=\s*["\']?(\d+\.\d+\.\d+)["\']?'},
                ]
            )
            with mock.patch.object(core, "get_git_root", return_value=root):
                err = io.StringIO()
                with contextlib.redirect_stderr(err):
                    with self.assertRaises(SystemExit) as ctx:
                        core.cmd_ver([])
                self.assertNotEqual(ctx.exception.code, 0)
                message = err.getvalue()
                self.assertIn("Version mismatch", message)
                self.assertIn("module.py", message)
                self.assertIn("second.py", message)

    def test_cmd_ver_errors_on_rule_without_matches(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "module.py").write_text('__version__ = "1.2.3"\n', encoding="utf-8")
            regex = r'version\s*=\s*"(\d+\.\d+\.\d+)"'
            self._set_rules(
                [
                    {"pattern": "module.py", "regex": regex},
                ]
            )
            with mock.patch.object(core, "get_git_root", return_value=root):
                err = io.StringIO()
                with contextlib.redirect_stderr(err):
                    with self.assertRaises(SystemExit) as ctx:
                        core.cmd_ver([])
                self.assertNotEqual(ctx.exception.code, 0)
                message = err.getvalue()
                self.assertIn("No version matches found", message)
                self.assertIn("module.py", message)
                self.assertIn(regex, message)

    def test_cmd_ver_ignores_cached_and_temp_paths(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "module.py").write_text('__version__ = "1.2.3"\n', encoding="utf-8")
            ignored_paths = [
                root / ".git" / "ignored.py",
                root / ".vscode" / "ignored.py",
                root / "tmp" / "ignored.py",
                root / "temp" / "ignored.py",
                root / ".cache" / "ignored.py",
                root / ".pytest_cache" / "ignored.py",
                root / "node_modules" / ".cache" / "ignored.py",
            ]
            for path in ignored_paths:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('__version__ = "9.9.9"\n', encoding="utf-8")
            self._set_rules(
                [
                    {"pattern": "**/*.py", "regex": r'__version__\s*=\s*["\']?(\d+\.\d+\.\d+)["\']?'},
                ]
            )
            with mock.patch.object(core, "get_git_root", return_value=root):
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    core.cmd_ver([])
                self.assertEqual(buffer.getvalue().strip(), "1.2.3")

    def test_cmd_ver_verbose_reports_regex_matches(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "module.py").write_text('__version__ = "1.2.3"\n', encoding="utf-8")
            (root / "notes.py").write_text("no version here\n", encoding="utf-8")
            self._set_rules(
                [
                    {"pattern": "*.py", "regex": r'__version__\s*=\s*["\']?(\d+\.\d+\.\d+)["\']?'},
                ]
            )
            with mock.patch.object(core, "get_git_root", return_value=root):
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    core.cmd_ver(["--verbose"])
                output = buffer.getvalue()
                self.assertIn("Regex match for module.py: yes.", output)
                self.assertIn("Regex match for notes.py: no.", output)
                self.assertEqual(output.strip().splitlines()[-1], "1.2.3")

    def test_cmd_ver_debug_reports_globbing_matches(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "module.py").write_text('__version__ = "1.2.3"\n', encoding="utf-8")
            self._set_rules(
                [
                    {"pattern": "*.py", "regex": r'__version__\s*=\s*["\']?(\d+\.\d+\.\d+)["\']?'},
                ]
            )
            with mock.patch.object(core, "get_git_root", return_value=root):
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    core.cmd_ver(["--debug"])
                output = buffer.getvalue()
                self.assertIn("Pattern '*.py' matched files:", output)
                self.assertIn("  module.py", output)
                self.assertIn("Regex match for module.py: yes.", output)
