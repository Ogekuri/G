import re
import subprocess
import sys
import unittest

from git_alias import core


class AliasHelpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = core
        cls.expected_help = cls.module.HELP_TEXTS.copy()

    @staticmethod
    def run_script(args):
        result = subprocess.run(
            [sys.executable, "-m", "git_alias.core", *args],
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
            pattern = re.compile(
                rf"^\s*{re.escape(alias)}\s+-\s+{re.escape(desc)}\s*$",
                re.MULTILINE,
            )
            self.assertRegex(
                output,
                pattern,
                msg=f"{alias} help missing from global --help",
            )

    def test_individual_help_matches_hlal(self):
        reset_aliases = getattr(self.module, "RESET_HELP_COMMANDS", set())
        for alias, desc in self.expected_help.items():
            output = self.run_script([alias, "--help"])
            if alias in reset_aliases:
                self.assertEqual(
                    output,
                    self.module.RESET_HELP.strip(),
                    msg=f"{alias} should print RESET_HELP when invoked with --help",
                )
            else:
                self.assertEqual(
                    output,
                    f"{alias} - {desc}",
                    msg=f"{alias} help output unexpected",
                )

    def test_reset_commands_show_reset_help(self):
        expected = self.module.RESET_HELP.strip()
        for alias in sorted(self.module.RESET_HELP_COMMANDS):
            output = self.run_script([alias, "--help"])
            self.assertEqual(
                output,
                expected,
                msg=f"{alias} did not emit RESET_HELP on --help",
            )
