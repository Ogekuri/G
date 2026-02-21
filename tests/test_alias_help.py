import contextlib
import io
import re
import unittest

from git_alias import core


class AliasHelpTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = core
        cls.expected_help = cls.module.HELP_TEXTS.copy()

    @staticmethod
    def run_script(args):
        code, stdout, _ = AliasHelpTest.run_script_result(args, check=True)
        if code != 0:
            raise AssertionError(f"Expected exit code 0, got {code}")
        return stdout.strip()

    @staticmethod
    def run_script_result(args, check=True):
        out = io.StringIO()
        err = io.StringIO()
        exit_code = 0
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            try:
                core.main(args, check_updates=False)
            except SystemExit as exc:
                exit_code = int(exc.code) if isinstance(exc.code, int) else 1
        if check and exit_code != 0:
            raise AssertionError(f"Expected exit code 0, got {exit_code}: {err.getvalue()}")
        return exit_code, out.getvalue(), err.getvalue()

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
            "changelog": ["--include-patch", "--force-write", "--print-only", "--disable-history"],
            "patch": ["--include-patch"],
            "ver": ["--verbose", "--debug"],
        }
        for alias, flags in expected_flags.items():
            output = self.run_script([alias, "--help"])
            for flag in flags:
                self.assertIn(
                    flag,
                    output,
                    msg=f"{alias} help missing option {flag}",
                )

    def test_conventional_alias_help_documents_module_prefix(self):
        aliases = ["new", "fix", "change", "implement", "refactor", "docs", "style", "revert", "misc", "cover"]
        for alias in aliases:
            output = self.run_script([alias, "--help"])
            self.assertIn("<module>: <description>", output, msg=f"{alias} help missing module prefix syntax")
            self.assertIn("default_module", output, msg=f"{alias} help missing default module fallback")

    def test_usage_includes_version_when_no_args(self):
        code, stdout, _ = self.run_script_result([], check=False)
        self.assertNotEqual(code, 0)
        version = self.module.get_cli_version()
        expected = f"Usage: g <command> [options] ({version})"
        self.assertIn(expected, stdout.splitlines())

    def test_global_version_flags(self):
        version = self.module.get_cli_version()
        for flag in ("--ver", "--version"):
            _, stdout, _ = self.run_script_result([flag], check=True)
            self.assertEqual(stdout.strip(), version)
