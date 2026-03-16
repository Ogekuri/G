import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class CmdRollbackTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_help_argument_prints_help(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            core.cmd_rollback(["--help"])
        self.assertIn("rollback -", out.getvalue())

    def test_rejects_missing_target_argument(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit) as ctx:
                core.cmd_rollback([])
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("requires exactly one target", err.getvalue())

    def test_fails_when_working_tree_is_not_clean(self):
        with mock.patch.object(core, "_git_status_lines", return_value=[" M file.txt"]):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_rollback(["abc123"])
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("working tree is not clean", err.getvalue())

    def test_fails_when_staging_area_is_not_empty(self):
        with mock.patch.object(core, "_git_status_lines", return_value=["M  file.txt"]):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_rollback(["abc123"])
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("staging area is not empty", err.getvalue())

    def test_fails_when_target_is_not_resolvable(self):
        with (
            mock.patch.object(core, "_git_status_lines", return_value=[]),
            mock.patch.object(core, "_tag_exists", return_value=True),
            mock.patch.object(
                core, "run_git_text", side_effect=RuntimeError("invalid target")
            ),
        ):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_rollback(["missing-tag"])
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("not a valid commit hash or tag", err.getvalue())

    def test_fails_when_target_is_neither_hash_nor_existing_tag(self):
        with mock.patch.object(core, "_tag_exists", return_value=False):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_rollback(["not-a-hash"])
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("must be an existing tag or a commit hash", err.getvalue())

    def test_fails_when_target_is_not_in_current_branch(self):
        with (
            mock.patch.object(core, "_git_status_lines", return_value=[]),
            mock.patch.object(core, "_tag_exists", return_value=True),
            mock.patch.object(
                core,
                "run_git_text",
                return_value="0123456789abcdef0123456789abcdef01234567",
            ),
            mock.patch.object(core, "_is_commit_ancestor", return_value=False),
        ):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_rollback(["v1.2.3"])
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("not reachable from the current branch HEAD", err.getvalue())

    def test_fails_when_target_matches_head(self):
        target_hash = "0123456789abcdef0123456789abcdef01234567"
        with (
            mock.patch.object(core, "_git_status_lines", return_value=[]),
            mock.patch.object(core, "_tag_exists", return_value=True),
            mock.patch.object(core, "_resolve_rollback_target_commit", return_value=target_hash),
            mock.patch.object(core, "_is_commit_ancestor", return_value=True),
            mock.patch.object(core, "run_git_text", return_value=target_hash),
        ):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_rollback(["v1.2.3"])
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("target matches HEAD", err.getvalue())

    def test_executes_revert_range_and_creates_non_amend_commit(self):
        resolved_hash = "0123456789abcdef0123456789abcdef01234567"
        with (
            mock.patch.object(core, "_git_status_lines", return_value=[]),
            mock.patch.object(core, "_tag_exists", return_value=True),
            mock.patch.object(core, "_resolve_rollback_target_commit", return_value=resolved_hash),
            mock.patch.object(core, "_is_commit_ancestor", return_value=True),
            mock.patch.object(core, "run_git_text", return_value="fedcba9876543210fedcba9876543210fedcba98"),
            mock.patch.object(core, "run_git_cmd", return_value=None) as run_git,
            mock.patch.object(core, "_execute_commit", return_value=None) as execute_commit,
        ):
            core.cmd_rollback(["v1.2.3"])
        run_git.assert_called_once_with(["revert", "--no-commit", f"{resolved_hash}..HEAD"])
        execute_commit.assert_called_once_with(
            f"revert: Roll back branch to v1.2.3 ({resolved_hash}).",
            "rollback",
            allow_amend=False,
        )


if __name__ == "__main__":
    unittest.main()
