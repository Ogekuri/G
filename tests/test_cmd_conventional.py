import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class ConventionalCommitAliasesTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_fix_uses_default_module_when_prefix_missing(self):
        with mock.patch.object(core, "_ensure_commit_ready") as ensure, mock.patch.object(
            core, "_execute_commit", return_value=None
        ) as execute:
            core.cmd_fix(["Correzione", "bug"])
        ensure.assert_called_once_with("fix")
        execute.assert_called_once_with("fix(core): Correzione bug", "fix", allow_amend=False)

    def test_docs_extracts_scope_from_prefix(self):
        with mock.patch.object(core, "_ensure_commit_ready") as ensure, mock.patch.object(
            core, "_execute_commit", return_value=None
        ) as execute:
            core.cmd_docs(["api:", "Aggiornamento", "documentazione"])
        ensure.assert_called_once_with("docs")
        execute.assert_called_once_with("docs(api): Aggiornamento documentazione", "docs", allow_amend=False)

    def test_change_uses_configured_default_scope(self):
        core.CONFIG["default_module"] = "ui"
        with mock.patch.object(core, "_ensure_commit_ready"), mock.patch.object(
            core, "_execute_commit", return_value=None
        ) as execute:
            core.cmd_change(["Refactoring"])
        execute.assert_called_once_with("change(ui): Refactoring", "change", allow_amend=False)

    def test_missing_message_raises_error(self):
        with mock.patch.object(core, "_ensure_commit_ready"):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit):
                    core.cmd_new([])
            self.assertIn("git new requires a message", err.getvalue())

    def test_prefix_without_body_is_rejected(self):
        with mock.patch.object(core, "_ensure_commit_ready"):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit):
                    core.cmd_misc(["core:"])
            self.assertIn("'<module>:' prefix", err.getvalue())

    def test_help_argument_prints_help(self):
        with mock.patch.object(core, "_ensure_commit_ready") as ensure, mock.patch.object(
            core, "_execute_commit"
        ) as execute:
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_fix(["--help"])
        self.assertEqual(ctx.exception.code, 0)
        self.assertIn("fix -", stdout.getvalue())
        ensure.assert_not_called()
        execute.assert_not_called()


if __name__ == "__main__":
    unittest.main()
