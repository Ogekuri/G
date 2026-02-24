## @file test_cmd_o.py
# @brief Unit tests for the `o` overview alias.

import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


## @brief Test suite for `cmd_o` and overview helpers.
class CmdOverviewTest(unittest.TestCase):
    ## @brief Reset runtime config for each test.
    # @return None.
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    ## @brief Verify command registration and help exposure for `o`.
    # @return None.
    def test_cmd_o_is_registered_and_documented(self):
        self.assertIn("o", core.COMMANDS)
        self.assertIs(core.COMMANDS["o"], core.cmd_o)
        self.assertIn("o", core.HELP_TEXTS)

    ## @brief Verify `cmd_o` fails with explicit stderr message outside Git repositories.
    # @return None.
    def test_cmd_o_requires_git_repository(self):
        with mock.patch.object(core, "is_inside_git_repo", return_value=False):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit) as ctx:
                    core.cmd_o([])
        self.assertEqual(ctx.exception.code, 2)
        self.assertIn("overview command", err.getvalue())

    ## @brief Verify `cmd_o` emits headings and performs all comparisons on feature branches.
    # @return None.
    def test_cmd_o_runs_status_and_all_comparisons(self):
        with mock.patch.object(core, "is_inside_git_repo", return_value=True), mock.patch.object(
            core, "_overview_primary_branch_name", return_value="main"
        ), mock.patch.object(core, "run_git_text", return_value="feature"), mock.patch.object(
            core, "_overview_compare_refs"
        ) as compare, mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                core.cmd_o([])
        run_git.assert_has_calls(
            [
                mock.call(["status", "-sb"]),
                mock.call(["worktree", "list", "--verbose"]),
            ]
        )
        self.assertEqual(run_git.call_count, 2)
        compare.assert_has_calls(
            [
                mock.call("HEAD", "develop", "Current vs Develop"),
                mock.call("HEAD", "main", "Current vs main"),
                mock.call("develop", "origin/develop", "Develop vs origin/Develop"),
                mock.call("main", "origin/main", "main vs origin"),
            ]
        )
        output = out.getvalue()
        self.assertIn("WORKING AREA, STAGE & CURRENT BRANCH", output)
        self.assertIn("BRANCH DISTANCES (COMMITS)", output)
        self.assertIn("ACTIVE WORKTREES", output)
        self.assertIn("Server Alignment", output)
        self.assertLess(
            output.index("WORKING AREA, STAGE & CURRENT BRANCH"),
            output.index("BRANCH DISTANCES (COMMITS)"),
        )
        self.assertLess(
            output.index("BRANCH DISTANCES (COMMITS)"),
            output.index("ACTIVE WORKTREES"),
        )

    ## @brief Verify `cmd_o` skips local-branch comparisons when already on `develop` or primary.
    # @return None.
    def test_cmd_o_skips_current_branch_comparisons_on_primary(self):
        with mock.patch.object(core, "is_inside_git_repo", return_value=True), mock.patch.object(
            core, "_overview_primary_branch_name", return_value="main"
        ), mock.patch.object(core, "run_git_text", return_value="main"), mock.patch.object(
            core, "_overview_compare_refs"
        ) as compare, mock.patch.object(core, "run_git_cmd", return_value=None):
            core.cmd_o([])
        compare.assert_has_calls(
            [
                mock.call("develop", "origin/develop", "Develop vs origin/Develop"),
                mock.call("main", "origin/main", "main vs origin"),
            ]
        )
        self.assertEqual(compare.call_count, 2)

    ## @brief Verify `_overview_compare_refs` formats and prints divergence rows.
    # @return None.
    def test_overview_compare_refs_prints_distance_row(self):
        with mock.patch.object(core, "_overview_ref_is_available", return_value=True), mock.patch.object(
            core, "run_git_text", side_effect=["2", "1"]
        ):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                core._overview_compare_refs("HEAD", "develop", "Current vs Develop")
        line = out.getvalue().strip()
        self.assertIn("Current vs Develop", line)
        self.assertIn("↑ ahead 2", line)
        self.assertIn("↓ behind 1", line)

    ## @brief Verify `_overview_compare_refs` skips output when compared refs are unavailable.
    # @return None.
    def test_overview_compare_refs_skips_missing_refs(self):
        with mock.patch.object(core, "_overview_ref_is_available", side_effect=[True, False]), mock.patch.object(
            core, "run_git_text"
        ) as run_git_text:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                core._overview_compare_refs("HEAD", "develop", "Current vs Develop")
        self.assertEqual(out.getvalue(), "")
        run_git_text.assert_not_called()


if __name__ == "__main__":
    unittest.main()
