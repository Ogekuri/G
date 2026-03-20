import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path

from git_alias import core


class ConfigIOTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_get_global_config_path_uses_xdg_location(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            home = Path(tmpdir) / "home"
            expected = home / ".config" / "git-alias" / "config.json"
            self.assertEqual(core.get_global_config_path(home), expected)

    def test_load_cli_config_reads_local_and_global_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            home = root / "home"
            local_payload = {
                "master": "main",
                "develop": "develop",
                "work": "work",
                "default_commit_module": "ui",
                "ver_rules": [{"pattern": "README.md", "regex": "x"}],
            }
            global_payload = {
                "edit_command": "vim",
                "gp_command": "gitk --all --date-order",
                "gr_command": "gitk --simplify-by-decoration --all --branches",
            }
            (root / core.CONFIG_FILENAME).write_text(json.dumps(local_payload), encoding="utf-8")
            global_path = core.get_global_config_path(home)
            global_path.parent.mkdir(parents=True, exist_ok=True)
            global_path.write_text(json.dumps(global_payload), encoding="utf-8")
            core.load_cli_config(root, home=home)
            self.assertEqual(core.CONFIG["master"], "main")
            self.assertEqual(core.CONFIG["edit_command"], "vim")
            self.assertEqual(core.CONFIG["default_commit_module"], "ui")
            self.assertEqual(core.CONFIG["gp_command"], global_payload["gp_command"])
            self.assertEqual(core.CONFIG["gr_command"], global_payload["gr_command"])
            self.assertEqual(core.CONFIG["ver_rules"], local_payload["ver_rules"])

    def test_load_cli_config_ignores_invalid_types(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            home = root / "home"
            local_payload = {
                "master": 123,
                "ver_rules": "bad",
            }
            global_payload = {"edit_command": ""}
            (root / core.CONFIG_FILENAME).write_text(json.dumps(local_payload), encoding="utf-8")
            global_path = core.get_global_config_path(home)
            global_path.parent.mkdir(parents=True, exist_ok=True)
            global_path.write_text(json.dumps(global_payload), encoding="utf-8")
            core.load_cli_config(root, home=home)
            self.assertEqual(core.CONFIG["master"], core.DEFAULT_CONFIG["master"])
            self.assertEqual(core.CONFIG["edit_command"], core.DEFAULT_CONFIG["edit_command"])
            self.assertEqual(core.CONFIG["ver_rules"], core.DEFAULT_CONFIG["ver_rules"])

    def test_write_default_config_inserts_missing_keys_without_overwriting(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            home = root / "home"
            local_payload = {
                "master": "main",
                "work": "workbench",
                "default_commit_module": "ui",
                "gp_command": "legacy-gp-command",
            }
            global_payload = {
                "editor": "vim",
                "gp_command": "gitk --all --date-order",
                "master": "legacy-master",
            }
            (root / core.CONFIG_FILENAME).write_text(json.dumps(local_payload), encoding="utf-8")
            global_path = core.get_global_config_path(home)
            global_path.parent.mkdir(parents=True, exist_ok=True)
            global_path.write_text(json.dumps(global_payload), encoding="utf-8")

            config_path = core.write_default_config(root, home=home)
            local_data = json.loads(config_path.read_text(encoding="utf-8"))
            global_data = json.loads(global_path.read_text(encoding="utf-8"))

            self.assertEqual(local_data["master"], "main")
            self.assertEqual(local_data["work"], "workbench")
            self.assertEqual(local_data["default_commit_module"], "ui")
            self.assertEqual(local_data["develop"], core.DEFAULT_CONFIG["develop"])
            self.assertEqual(local_data["ver_rules"], core.DEFAULT_CONFIG["ver_rules"])
            self.assertNotIn("gp_command", local_data)
            self.assertNotIn("edit_command", local_data)

            self.assertEqual(global_data["edit_command"], "vim")
            self.assertEqual(global_data["gp_command"], "gitk --all --date-order")
            self.assertEqual(global_data["gr_command"], core.DEFAULT_CONFIG["gr_command"])
            self.assertNotIn("editor", global_data)
            self.assertNotIn("master", global_data)

    def test_load_cli_config_does_not_persist_missing_global_gpgr_keys(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            home = root / "home"
            local_payload = {
                "master": "main",
                "default_commit_module": "ui",
                "ver_rules": [{"pattern": "README.md", "regex": "x"}],
            }
            global_payload = {"edit_command": "vim"}
            local_path = root / core.CONFIG_FILENAME
            local_path.write_text(json.dumps(local_payload), encoding="utf-8")
            global_path = core.get_global_config_path(home)
            global_path.parent.mkdir(parents=True, exist_ok=True)
            global_path.write_text(json.dumps(global_payload), encoding="utf-8")

            core.load_cli_config(root, home=home)

            persisted_global = json.loads(global_path.read_text(encoding="utf-8"))
            self.assertEqual(persisted_global, global_payload)
            self.assertEqual(core.CONFIG["gp_command"], core.DEFAULT_CONFIG["gp_command"])
            self.assertEqual(core.CONFIG["gr_command"], core.DEFAULT_CONFIG["gr_command"])

    def test_load_cli_config_accepts_empty_default_commit_module(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            home = root / "home"
            local_payload = {
                "master": "main",
                "develop": "develop",
                "work": "work",
                "default_commit_module": "",
                "ver_rules": [{"pattern": "README.md", "regex": "x"}],
            }
            (root / core.CONFIG_FILENAME).write_text(json.dumps(local_payload), encoding="utf-8")
            global_path = core.get_global_config_path(home)
            global_path.parent.mkdir(parents=True, exist_ok=True)
            global_path.write_text(json.dumps({"edit_command": "vim"}), encoding="utf-8")
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                core.load_cli_config(root, home=home)
            self.assertEqual(core.CONFIG["default_commit_module"], "")
            self.assertNotIn("Ignoring default_commit_module", stderr.getvalue())

    def test_write_default_config_keeps_empty_default_commit_module(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            home = root / "home"
            local_payload = {
                "master": "main",
                "develop": "develop",
                "work": "workbench",
                "default_commit_module": "",
                "ver_rules": [{"pattern": "README.md", "regex": "x"}],
            }
            (root / core.CONFIG_FILENAME).write_text(json.dumps(local_payload), encoding="utf-8")
            global_path = core.get_global_config_path(home)
            global_path.parent.mkdir(parents=True, exist_ok=True)
            global_path.write_text(json.dumps({"edit_command": "vim"}), encoding="utf-8")
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                config_path = core.write_default_config(root, home=home)
            local_data = json.loads(config_path.read_text(encoding="utf-8"))
            self.assertEqual(local_data["default_commit_module"], "")
            self.assertNotIn("Ignoring default_commit_module", stderr.getvalue())
