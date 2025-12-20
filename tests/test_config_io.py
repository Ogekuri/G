import json
import tempfile
import unittest
from pathlib import Path

from git_alias import core


class ConfigIOTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_load_cli_config_reads_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            payload = {
                "master": "main",
                "develop": "develop",
                "work": "work",
                "editor": "vim",
                "default_module": "ui",
                "ver_rules": [{"pattern": "README.md", "regex": "x"}],
            }
            (root / core.CONFIG_FILENAME).write_text(json.dumps(payload), encoding="utf-8")
            core.load_cli_config(root)
            self.assertEqual(core.CONFIG["master"], "main")
            self.assertEqual(core.CONFIG["editor"], "vim")
            self.assertEqual(core.CONFIG["default_module"], "ui")
            self.assertEqual(core.CONFIG["ver_rules"], payload["ver_rules"])

    def test_load_cli_config_ignores_invalid_types(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            payload = {
                "master": 123,
                "editor": "",
                "ver_rules": "bad",
            }
            (root / core.CONFIG_FILENAME).write_text(json.dumps(payload), encoding="utf-8")
            core.load_cli_config(root)
            self.assertEqual(core.CONFIG["master"], core.DEFAULT_CONFIG["master"])
            self.assertEqual(core.CONFIG["editor"], core.DEFAULT_CONFIG["editor"])
            self.assertEqual(core.CONFIG["ver_rules"], core.DEFAULT_CONFIG["ver_rules"])

    def test_write_default_config_writes_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            config_path = core.write_default_config(root)
            content = config_path.read_text(encoding="utf-8")
            data = json.loads(content)
            self.assertEqual(data["master"], core.DEFAULT_CONFIG["master"])
            self.assertIsInstance(data["ver_rules"], list)
