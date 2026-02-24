## @file test_cmd_o.py
# @brief Unit tests for the `o` overview alias.

import contextlib
import io
import unittest
from unittest import mock
from unittest.mock import ANY

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
            core, "get_branch", side_effect=["work", "develop", "master"]
        ), mock.patch.object(core, "_overview_compare_refs"
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
                mock.call("work", "develop", ANY),
                mock.call("work", "master", ANY),
                mock.call("develop", "origin/develop", ANY),
                mock.call("master", "origin/master", ANY),
            ]
        )
        output = out.getvalue()
        self.assertIn("WORKING AREA, STAGE & CURRENT BRANCH", output)
        self.assertIn("BRANCH DISTANCES (COMMITS)", output)
        self.assertIn("ACTIVE WORKTREES", output)
        self.assertIn("QUALITATIVE TOPOLOGY (ASCII TREE)", output)
        self.assertIn("Server Alignment", output)
        self.assertIn("Work(", output)
        self.assertIn("Develop(", output)
        self.assertIn("Master(", output)
        self.assertIn("RemoteDevelop(", output)
        self.assertIn("RemoteMaster(", output)
        self.assertLess(
            output.index("WORKING AREA, STAGE & CURRENT BRANCH"),
            output.index("BRANCH DISTANCES (COMMITS)"),
        )
        self.assertLess(
            output.index("BRANCH DISTANCES (COMMITS)"),
            output.index("ACTIVE WORKTREES"),
        )
        self.assertLess(
            output.index("ACTIVE WORKTREES"),
            output.index("QUALITATIVE TOPOLOGY (ASCII TREE)"),
        )

    ## @brief Verify `cmd_o` uses configured branch names consistently in compare calls.
    # @return None.
    def test_cmd_o_uses_configured_branch_names_for_comparisons(self):
        with mock.patch.object(core, "is_inside_git_repo", return_value=True), mock.patch.object(
            core, "get_branch", side_effect=["wrk", "dev", "mst"]
        ), mock.patch.object(
            core, "_overview_compare_refs"
        ) as compare, mock.patch.object(core, "run_git_cmd", return_value=None):
            core.cmd_o([])
        compare.assert_has_calls(
            [
                mock.call("wrk", "dev", ANY),
                mock.call("wrk", "mst", ANY),
                mock.call("dev", "origin/dev", ANY),
                mock.call("mst", "origin/mst", ANY),
            ]
        )
        self.assertEqual(compare.call_count, 4)

    ## @brief Verify `_overview_compare_refs` formats and prints divergence rows.
    # @return None.
    def test_overview_compare_refs_prints_distance_row(self):
        with mock.patch.object(core, "_overview_ref_is_available", return_value=True), mock.patch.object(
            core, "run_git_text", side_effect=["2", "1"]
        ):
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                state = core._overview_compare_refs("HEAD", "develop", "Current vs Develop")
        line = out.getvalue().strip()
        self.assertIn("Current vs Develop", line)
        self.assertIn("↑ ahead 2", line)
        self.assertIn("↓ behind 1", line)
        self.assertEqual(state, "diverged")

    ## @brief Verify `_overview_compare_refs` prints explicit n/a values when refs are unavailable.
    # @return None.
    def test_overview_compare_refs_marks_missing_refs(self):
        with mock.patch.object(core, "_overview_ref_is_available", side_effect=[True, False]), mock.patch.object(
            core, "run_git_text"
        ) as run_git_text:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                state = core._overview_compare_refs("HEAD", "develop", "Current vs Develop")
        self.assertIn("ahead", out.getvalue())
        self.assertIn("n/a", out.getvalue())
        self.assertIn("behind", out.getvalue())
        self.assertEqual(state, "unknown")
        run_git_text.assert_not_called()

    ## @brief Verify `_overview_ascii_topology_lines` renders a qualitative ASCII tree.
    # @return None.
    def test_overview_ascii_topology_lines_renders_nodes_and_states(self):
        lines = core._overview_ascii_topology_lines(
            work_display="Work(⎇ work)",
            develop_display="Develop(⎇ develop)",
            master_display="Master(⎇ master)",
            remote_develop_display="RemoteDevelop(⎇ origin/develop)",
            remote_master_display="RemoteMaster(⎇ origin/master)",
            worktree_state="clean",
            work_vs_develop="ahead",
            work_vs_master="behind",
            develop_vs_remote="in_sync",
            master_vs_remote="diverged",
        )
        rendered = "\n".join(lines)
        self.assertIn("WorkingTree", rendered)
        self.assertIn("\\-- Work(⎇ work)", rendered)
        self.assertIn("|-- Develop(⎇ develop)", rendered)
        self.assertIn("\\-- RemoteDevelop(⎇ origin/develop)", rendered)
        self.assertIn("\\-- Master(⎇ master)", rendered)
        self.assertIn("\\-- RemoteMaster(⎇ origin/master)", rendered)
        self.assertIn("ahead", rendered)
        self.assertIn("behind", rendered)
        self.assertIn("diverged", rendered)


if __name__ == "__main__":
    unittest.main()
