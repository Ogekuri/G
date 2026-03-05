import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class ConventionalCommitAliasesTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_fix_uses_default_module_when_prefix_missing(self):
        with (
            mock.patch.object(core, "_ensure_commit_ready_with_stage") as ensure,
            mock.patch.object(core, "_execute_commit", return_value=None) as execute,
        ):
            core.cmd_fix(["Correzione", "bug"])
        ensure.assert_called_once_with("fix")
        execute.assert_called_once_with("fix: Correzione bug.", "fix")

    def test_docs_extracts_scope_from_prefix(self):
        with (
            mock.patch.object(core, "_ensure_commit_ready_with_stage") as ensure,
            mock.patch.object(core, "_execute_commit", return_value=None) as execute,
        ):
            core.cmd_docs(["api:", "Aggiornamento", "documentazione"])
        ensure.assert_called_once_with("docs")
        execute.assert_called_once_with(
            "docs(api): Aggiornamento documentazione.", "docs"
        )

    def test_change_uses_configured_default_scope(self):
        core.CONFIG["default_commit_module"] = "ui"
        with (
            mock.patch.object(core, "_ensure_commit_ready_with_stage"),
            mock.patch.object(core, "_execute_commit", return_value=None) as execute,
        ):
            core.cmd_change(["Refactoring"])
        execute.assert_called_once_with("change(ui): Refactoring.", "change")

    def test_implement_uses_default_module_when_prefix_missing(self):
        with (
            mock.patch.object(core, "_ensure_commit_ready_with_stage") as ensure,
            mock.patch.object(core, "_execute_commit", return_value=None) as execute,
        ):
            core.cmd_implement(["Nuova", "feature"])
        ensure.assert_called_once_with("implement")
        execute.assert_called_once_with("implement: Nuova feature.", "implement")

    def test_new_capitalizes_first_description_character_unless_numeric(self):
        with (
            mock.patch.object(core, "_ensure_commit_ready_with_stage"),
            mock.patch.object(core, "_execute_commit", return_value=None) as execute,
        ):
            core.cmd_new(["core:", "cleanup", "pipeline"])
        execute.assert_called_once_with("new(core): Cleanup pipeline.", "new")

    def test_cover_preserves_numeric_first_character(self):
        with (
            mock.patch.object(core, "_ensure_commit_ready_with_stage"),
            mock.patch.object(core, "_execute_commit", return_value=None) as execute,
        ):
            core.cmd_cover(["core:", "123", "tasks"])
        execute.assert_called_once_with("cover(core): 123 tasks.", "cover")

    def test_revert_omits_scope_when_configured_default_scope_is_empty(self):
        core.CONFIG["default_commit_module"] = ""
        with (
            mock.patch.object(core, "_ensure_commit_ready_with_stage"),
            mock.patch.object(core, "_execute_commit", return_value=None) as execute,
        ):
            core.cmd_revert(["ripristino", "stabile"])
        execute.assert_called_once_with("revert: Ripristino stabile.", "revert")

    def test_style_keeps_single_trailing_period_when_present(self):
        with (
            mock.patch.object(core, "_ensure_commit_ready_with_stage"),
            mock.patch.object(core, "_execute_commit", return_value=None) as execute,
        ):
            core.cmd_style(["ui:", "Already done."])
        execute.assert_called_once_with("style(ui): Already done.", "style")

    def test_missing_message_raises_error(self):
        with mock.patch.object(core, "_ensure_commit_ready_with_stage"):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit):
                    core.cmd_new([])
            self.assertIn("git new requires a message", err.getvalue())

    def test_prefix_without_body_is_rejected(self):
        with mock.patch.object(core, "_ensure_commit_ready_with_stage"):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit):
                    core.cmd_misc(["core:"])
            self.assertIn("'<module>:' prefix", err.getvalue())

    def test_help_argument_prints_help(self):
        with (
            mock.patch.object(core, "_ensure_commit_ready_with_stage") as ensure,
            mock.patch.object(core, "_execute_commit") as execute,
        ):
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_fix(["--help"])
        self.assertEqual(ctx.exception.code, 0)
        self.assertIn("fix -", stdout.getvalue())
        ensure.assert_not_called()
        execute.assert_not_called()

    def test_conventional_commit_auto_stages_when_staging_empty_and_working_tree_dirty(
        self,
    ):
        # Arrange: unstaged changes only (working-tree dirty, staging empty).
        # _git_status_lines called once inside _ensure_commit_ready_with_stage,
        # then cmd_aa calls _git_status_lines again (has_unstaged_changes check).
        status_side_effect = [
            [" M file"],  # _ensure_commit_ready_with_stage: staged=False, unstaged=True
            [" M file"],  # cmd_aa -> has_unstaged_changes check
        ]
        with (
            mock.patch.object(
                core, "_git_status_lines", side_effect=status_side_effect
            ),
            mock.patch.object(
                core,
                "_should_amend_existing_commit",
                return_value=(False, "Unit test: new commit"),
            ),
            mock.patch.object(core, "run_git_cmd", return_value=None) as run_git,
        ):
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                core.cmd_fix(["Some fix."])
        # First run_git_cmd call must be "git add --all" (from cmd_aa), second is the commit.
        calls = run_git.call_args_list
        self.assertEqual(calls[0], mock.call(["add", "--all"], []))
        self.assertEqual(
            calls[1],
            mock.call(["commit", "-F", "-"], input="fix: Some fix.", text=True),
        )

    def test_conventional_commit_fails_when_both_staging_and_working_tree_are_empty(
        self,
    ):
        # Arrange: completely clean repository — nothing staged, nothing unstaged.
        with mock.patch.object(core, "_git_status_lines", return_value=[]):
            stderr = io.StringIO()
            with contextlib.redirect_stderr(stderr):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_fix(["Some fix."])
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("no changes to commit", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
