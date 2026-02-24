## @file test_cmd_o.py
# @brief Unit tests for the `o` overview alias.

import contextlib
import io
import re
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
        ), mock.patch.object(
            core, "run_git_text", return_value="work"
        ), mock.patch.object(
            core, "_overview_compare_relation", side_effect=["in_sync", "behind"]
        ), mock.patch.object(core, "_overview_compare_refs"
        ) as compare, mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                core.cmd_o([])
        run_git.assert_has_calls(
            [
                mock.call(["worktree", "list", "--verbose"]),
                mock.call(["status", "-sb"]),
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
        normalized_output = re.sub(r"\x1b\[[0-9;]*m", "", output)
        self.assertIn("WORKING AREA, STAGE & CURRENT BRANCH", output)
        self.assertIn("BRANCH DISTANCES (COMMITS)", output)
        self.assertIn("ACTIVE WORKTREES", output)
        self.assertIn("QUALITATIVE TOPOLOGY", output)
        self.assertIn("CURRENT BRANCH STATE", output)
        self.assertIn("Server Alignment", output)
        self.assertIn("Current Branch:", output)
        self.assertIn("Work(⎇ work)", normalized_output)
        self.assertIn("Develop(⎇ develop)", normalized_output)
        self.assertIn("Master(⎇ master)", normalized_output)
        self.assertIn("RemoteDevelop(⎇ origin/develop)", normalized_output)
        self.assertIn("RemoteMaster(⎇ origin/master)", normalized_output)
        self.assertLess(
            normalized_output.index("WORKING AREA, STAGE & CURRENT BRANCH"),
            normalized_output.index("BRANCH DISTANCES (COMMITS)"),
        )
        self.assertLess(
            normalized_output.index("BRANCH DISTANCES (COMMITS)"),
            normalized_output.index("ACTIVE WORKTREES"),
        )
        self.assertLess(
            normalized_output.index("ACTIVE WORKTREES"),
            normalized_output.index("QUALITATIVE TOPOLOGY"),
        )
        self.assertLess(
            normalized_output.index("QUALITATIVE TOPOLOGY"),
            normalized_output.index("CURRENT BRANCH STATE"),
        )

    ## @brief Verify `cmd_o` uses configured branch names consistently in compare calls.
    # @return None.
    def test_cmd_o_uses_configured_branch_names_for_comparisons(self):
        with mock.patch.object(core, "is_inside_git_repo", return_value=True), mock.patch.object(
            core, "get_branch", side_effect=["wrk", "dev", "mst"]
        ), mock.patch.object(
            core, "run_git_text", return_value="wrk"
        ), mock.patch.object(
            core, "_overview_compare_relation", side_effect=["in_sync", "behind"]
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

    ## @brief Verify current branch identifier uses red logical prefix and yellow tuple.
    # @return None.
    def test_overview_current_branch_display_uses_expected_colors(self):
        rendered = core._overview_current_branch_display(
            current_branch="work",
            work_branch="work",
            develop_branch="develop",
            master_branch="master",
        )
        self.assertIn(f"{core.OVERVIEW_COLOR_BEHIND}Work", rendered)
        self.assertIn(f"{core.OVERVIEW_COLOR_LABEL}⎇ work", rendered)

    ## @brief Verify `_overview_ascii_topology_lines` renders commit-alignment groups.
    # @return None.
    def test_overview_ascii_topology_lines_renders_commit_alignment_groups(self):
        lines = core._overview_ascii_topology_lines(
            work_display="Work(⎇ work)",
            develop_display="Develop(⎇ develop)",
            master_display="Master(⎇ master)",
            remote_develop_display="RemoteDevelop(⎇ origin/develop)",
            remote_master_display="RemoteMaster(⎇ origin/master)",
            worktree_state="clean",
            work_vs_develop="ahead",
            work_vs_master="behind",
            work_vs_remote_develop="in_sync",
            work_vs_remote_master="diverged",
        )
        rendered = "\n".join(lines)
        normalized_rendered = re.sub(r"\x1b\[[0-9;]*m", "", rendered)
        self.assertIn("WorkingTree", normalized_rendered)
        self.assertIn("in_sync with Work", normalized_rendered)
        self.assertIn("ahead of Work", normalized_rendered)
        self.assertIn("behind Work", normalized_rendered)
        self.assertIn("Work(⎇ work)", normalized_rendered)
        self.assertIn("Develop(⎇ develop)", normalized_rendered)
        self.assertIn("RemoteDevelop(⎇ origin/develop)", normalized_rendered)
        self.assertIn("Master(⎇ master)", normalized_rendered)
        self.assertIn("RemoteMaster(⎇ origin/master)", normalized_rendered)
        self.assertIn("ahead", rendered)
        self.assertIn("behind", rendered)
        self.assertIn("diverged", rendered)


if __name__ == "__main__":
    unittest.main()
