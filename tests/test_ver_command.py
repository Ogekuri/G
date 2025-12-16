import contextlib
import io
import json
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
        core.CONFIG["ver_rules"] = json.dumps(rules)

    def test_cmd_ver_prints_shared_version(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "module.py").write_text('__version__ = "1.2.3"\n', encoding="utf-8")
            (root / "README.md").write_text('Current version "1.2.3"\n', encoding="utf-8")
            self._set_rules(
                [
                    ["module.py", r'__version__\s*=\s*"(\d+\.\d+\.\d+)"'],
                    ["README.md", r'"(\d+\.\d+\.\d+)"'],
                ]
            )
            with mock.patch.object(core, "get_git_root", return_value=root):
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
                    ["*.py", r'__version__\s*=\s*["\']?(\d+\.\d+\.\d+)["\']?'],
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
