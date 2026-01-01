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
            [sys.executable, "-c", "from git_alias.core import main; raise SystemExit(main())", *args],
            check=True,
            stdout=subprocess.PIPE,
            text=True,
        )
        return result.stdout.strip()

    @staticmethod
    def run_script_result(args, check=True):
        return subprocess.run(
            [sys.executable, "-c", "from git_alias.core import main; raise SystemExit(main())", *args],
            check=check,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

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

    def test_management_help_order(self):
        output = self.run_script(["--help"])
        lines = output.splitlines()
        self.assertIn("Management Commands:", lines)
        start = lines.index("Management Commands:")
        entries = []
        for line in lines[start + 1 :]:
            if not line.strip():
                break
            entries.append(line.strip())
        flags = [line.split()[0] for line in entries if line.strip()]
        self.assertGreaterEqual(len(flags), 3)
        self.assertEqual(flags[:3], ["--write-config", "--upgrade", "--remove"])
        self.assertIn("--help", flags)

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

    def test_help_lists_command_options_when_present(self):
        expected_flags = {
            "changelog": ["--include-unreleased", "--include-draft", "--force-write", "--print-only"],
            "major": ["--include-unreleased", "--include-draft"],
            "minor": ["--include-unreleased", "--include-draft"],
            "patch": ["--include-unreleased", "--include-draft"],
        }
        for alias, flags in expected_flags.items():
            output = self.run_script([alias, "--help"])
            for flag in flags:
                self.assertIn(
                    flag,
                    output,
                    msg=f"{alias} help missing option {flag}",
                )

    def test_usage_includes_version_when_no_args(self):
        result = self.run_script_result([], check=False)
        self.assertNotEqual(result.returncode, 0)
        version = self.module.get_cli_version()
        expected = f"Usage: g <command> [options] ({version})"
        self.assertIn(expected, result.stdout.splitlines())

    def test_global_version_flags(self):
        version = self.module.get_cli_version()
        for flag in ("--ver", "--version"):
            result = self.run_script_result([flag], check=True)
            self.assertEqual(result.stdout.strip(), version)
