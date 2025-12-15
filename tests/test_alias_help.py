import re
import subprocess
import sys
from pathlib import Path
import unittest

from git_alias import core

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "p.python"
GITCONFIG = ROOT / "gitconfig.conf"


def load_hlal_help(config_path):
    """Return the alias/description map that `hlal` prints from the gitconfig."""
    text_lines = config_path.read_text().splitlines()
    block = []
    found = False
    for line in text_lines:
        if not found and "hlal =" in line:
            found = True
        if not found:
            continue
        stripped = line.strip()
        block.append(stripped)
        if stripped.startswith('f"'):
            break
    if not block:
        raise RuntimeError("Could not find hlal alias block")
    mapping = {}
    for line in block:
        match = re.search(r'echo -e \\\\\\\"(.*?)\\\\\\\"', line)
        if not match:
            continue
        text = match.group(1)
        if "=" not in text:
            continue
        alias_part, desc = text.split("=", 1)
        alias = alias_part.strip()
        desc = desc.strip()
        mapping[alias] = desc
    return mapping


class AliasHelpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = core
        cls.hlal_help = load_hlal_help(GITCONFIG)
        cls.expected_help = {
            alias: desc
            for alias, desc in cls.hlal_help.items()
            if alias in cls.module.COMMANDS
        }

    @staticmethod
    def run_script(args):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *args],
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        )
        return result.stdout.strip()

    def test_all_commands_have_help_text(self):
        missing = [
            name
            for name in self.module.COMMANDS
            if name not in self.module.HELP_TEXTS
        ]
        self.assertFalse(
            missing,
            msg=f"Help texts missing for commands: {', '.join(sorted(missing))}",
        )

    def test_hlal_matches_help_dictionary(self):
        for alias, desc in self.expected_help.items():
            self.assertIn(
                alias,
                self.module.HELP_TEXTS,
                msg=f"{alias} missing from HELP_TEXTS",
            )
            self.assertEqual(
                self.module.HELP_TEXTS[alias],
                desc,
                msg=f"{alias} description does not match hlal",
            )

    def test_global_help_contains_hlal_entries(self):
        output = self.run_script(["--help"])
        for alias, desc in self.expected_help.items():
            self.assertIn(
                f"{alias} - {desc}",
                output,
                msg=f"{alias} help missing from global --help",
            )

    def test_individual_help_matches_hlal(self):
        for alias, desc in self.expected_help.items():
            output = self.run_script([alias, "--help"])
            self.assertEqual(
                output,
                f"{alias} - {desc}",
                msg=f"{alias} help output unexpected",
            )
