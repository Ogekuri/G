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
        with mock.patch.object(core, "is_inside_git_repo", return_value=True), \
             mock.patch.object(core, "get_branch", side_effect=["work", "develop", "master"]), \
             mock.patch.object(core, "run_git_text", return_value="work"), \
             mock.patch.object(core, "_overview_compare_refs") as compare, \
             mock.patch.object(core, "_overview_ascii_topology_lines", return_value=[]) as topo, \
             mock.patch.object(core, "_overview_worktree_state", return_value="clean"), \
             mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
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
        topo.assert_called_once_with(
            work_ref="work",
            develop_ref="develop",
            master_ref="master",
            remote_develop_ref="origin/develop",
            remote_master_ref="origin/master",
            work_display=ANY,
            develop_display=ANY,
            master_display=ANY,
            remote_develop_display=ANY,
            remote_master_display=ANY,
            worktree_state="clean",
        )

    ## @brief Verify `cmd_o` uses configured branch names consistently in compare calls.
    # @return None.
    def test_cmd_o_uses_configured_branch_names_for_comparisons(self):
        with mock.patch.object(core, "is_inside_git_repo", return_value=True), \
             mock.patch.object(core, "get_branch", side_effect=["wrk", "dev", "mst"]), \
             mock.patch.object(core, "run_git_text", return_value="wrk"), \
             mock.patch.object(core, "_overview_compare_refs") as compare, \
             mock.patch.object(core, "_overview_ascii_topology_lines", return_value=[]), \
             mock.patch.object(core, "_overview_worktree_state", return_value="clean"), \
             mock.patch.object(core, "run_git_cmd", return_value=None):
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

    ## @brief Verify `_overview_ascii_topology_lines` renders chronological-position tree
    #  when all refs are at the same commit (in_sync scenario).
    # @return None.
    def test_topology_all_in_sync_clean(self):
        same_hash = "aaa111"
        with mock.patch.object(core, "_overview_ref_is_available", return_value=True), \
             mock.patch.object(core, "run_git_text", side_effect=[
                 same_hash, same_hash, same_hash, same_hash, same_hash,
                 same_hash,
                 "0", "0", "0", "0", "0",
             ]):
            lines = core._overview_ascii_topology_lines(
                work_ref="work",
                develop_ref="develop",
                master_ref="master",
                remote_develop_ref="origin/develop",
                remote_master_ref="origin/master",
                work_display="Work(⎇ work)",
                develop_display="Develop(⎇ develop)",
                master_display="Master(⎇ master)",
                remote_develop_display="RemoteDevelop(⎇ origin/develop)",
                remote_master_display="RemoteMaster(⎇ origin/master)",
                worktree_state="clean",
            )
        rendered = "\n".join(lines)
        normalized = re.sub(r"\x1b\[[0-9;]*m", "", rendered)
        self.assertIn("WorkingTree [clean]", normalized)
        self.assertIn("Work(⎇ work)", normalized)
        self.assertIn("Develop(⎇ develop)", normalized)
        self.assertIn("Master(⎇ master)", normalized)
        self.assertIn("RemoteDevelop(⎇ origin/develop)", normalized)
        self.assertIn("RemoteMaster(⎇ origin/master)", normalized)
        self.assertNotIn("in_sync", normalized)
        self.assertNotIn("ahead", normalized)
        self.assertNotIn("behind", normalized)
        self.assertNotIn("diverged", normalized)
        self.assertNotIn("unknown", normalized)
        norm_lines = [re.sub(r"\x1b\[[0-9;]*m", "", l) for l in lines]
        self.assertIn("WorkingTree [clean]", norm_lines[0])
        self.assertEqual("|", norm_lines[1])
        work_idx = next(i for i, l in enumerate(norm_lines) if "Work(⎇ work)" in l)
        others_idx = next(
            i for i, l in enumerate(norm_lines)
            if "Develop(⎇ develop)" in l and "Master(⎇ master)" in l
        )
        self.assertGreater(others_idx, work_idx)

    ## @brief Verify `_overview_ascii_topology_lines` places dirty WorkingTree above Work.
    # @return None.
    def test_topology_dirty_worktree_above_work(self):
        work_hash = "bbb222"
        other_hash = "ccc333"
        with mock.patch.object(core, "_overview_ref_is_available", return_value=True), \
             mock.patch.object(core, "run_git_text", side_effect=[
                 work_hash, other_hash, other_hash, other_hash, other_hash,
                 work_hash,
                 "3", "1", "1", "1", "1",
             ]):
            lines = core._overview_ascii_topology_lines(
                work_ref="work",
                develop_ref="develop",
                master_ref="master",
                remote_develop_ref="origin/develop",
                remote_master_ref="origin/master",
                work_display="Work(⎇ work)",
                develop_display="Develop(⎇ develop)",
                master_display="Master(⎇ master)",
                remote_develop_display="RemoteDevelop(⎇ origin/develop)",
                remote_master_display="RemoteMaster(⎇ origin/master)",
                worktree_state="unstaged",
            )
        norm_lines = [re.sub(r"\x1b\[[0-9;]*m", "", l) for l in lines]
        wt_idx = next(i for i, l in enumerate(norm_lines) if "WorkingTree" in l)
        work_idx = next(i for i, l in enumerate(norm_lines) if "Work(⎇ work)" in l)
        self.assertLess(wt_idx, work_idx)
        self.assertIn("[unstaged]", norm_lines[wt_idx])

    ## @brief Verify topology places remote ahead of local when remote has more commits.
    # @return None.
    def test_topology_remote_ahead_becomes_root(self):
        work_hash = "ddd444"
        dev_hash = "eee555"
        remote_dev_hash = "fff666"
        master_hash = "ggg777"
        with mock.patch.object(core, "_overview_ref_is_available", return_value=True), \
             mock.patch.object(core, "run_git_text", side_effect=[
                 work_hash, dev_hash, master_hash, remote_dev_hash, master_hash,
                 "aaa000",
                 "2", "1", "0", "4", "0",
             ]):
            lines = core._overview_ascii_topology_lines(
                work_ref="work",
                develop_ref="develop",
                master_ref="master",
                remote_develop_ref="origin/develop",
                remote_master_ref="origin/master",
                work_display="Work(⎇ work)",
                develop_display="Develop(⎇ develop)",
                master_display="Master(⎇ master)",
                remote_develop_display="RemoteDevelop(⎇ origin/develop)",
                remote_master_display="RemoteMaster(⎇ origin/master)",
                worktree_state="unstaged",
            )
        norm_lines = [re.sub(r"\x1b\[[0-9;]*m", "", l) for l in lines]
        self.assertIn("RemoteDevelop(⎇ origin/develop)", norm_lines[0])
        wt_idx = next(i for i, l in enumerate(norm_lines) if "WorkingTree" in l)
        work_idx = next(i for i, l in enumerate(norm_lines) if "Work(⎇ work)" in l)
        self.assertLess(wt_idx, work_idx)

    ## @brief Verify topology groups refs sharing the same commit hash on one line.
    # @return None.
    def test_topology_groups_same_hash_refs(self):
        same_hash = "hhh888"
        work_hash = "iii999"
        with mock.patch.object(core, "_overview_ref_is_available", return_value=True), \
             mock.patch.object(core, "run_git_text", side_effect=[
                 work_hash, same_hash, same_hash, same_hash, same_hash,
                 "jjj000",
                 "3", "1", "1", "1", "1",
             ]):
            lines = core._overview_ascii_topology_lines(
                work_ref="work",
                develop_ref="develop",
                master_ref="master",
                remote_develop_ref="origin/develop",
                remote_master_ref="origin/master",
                work_display="Work(⎇ work)",
                develop_display="Develop(⎇ develop)",
                master_display="Master(⎇ master)",
                remote_develop_display="RemoteDevelop(⎇ origin/develop)",
                remote_master_display="RemoteMaster(⎇ origin/master)",
                worktree_state="clean",
            )
        norm_lines = [re.sub(r"\x1b\[[0-9;]*m", "", l) for l in lines]
        grouped_line = next(
            l for l in norm_lines
            if "Develop(⎇ develop)" in l and "Master(⎇ master)" in l
        )
        self.assertIn("RemoteDevelop(⎇ origin/develop)", grouped_line)
        self.assertIn("RemoteMaster(⎇ origin/master)", grouped_line)

    ## @brief Verify topology does not emit qualitative-state labels.
    # @return None.
    def test_topology_no_qualitative_state_labels(self):
        same_hash = "kkk111"
        with mock.patch.object(core, "_overview_ref_is_available", return_value=True), \
             mock.patch.object(core, "run_git_text", side_effect=[
                 same_hash, same_hash, same_hash, same_hash, same_hash,
                 same_hash,
                 "0", "0", "0", "0", "0",
             ]):
            lines = core._overview_ascii_topology_lines(
                work_ref="work",
                develop_ref="develop",
                master_ref="master",
                remote_develop_ref="origin/develop",
                remote_master_ref="origin/master",
                work_display="Work(⎇ work)",
                develop_display="Develop(⎇ develop)",
                master_display="Master(⎇ master)",
                remote_develop_display="RemoteDevelop(⎇ origin/develop)",
                remote_master_display="RemoteMaster(⎇ origin/master)",
                worktree_state="clean",
            )
        rendered = "\n".join(lines)
        normalized = re.sub(r"\x1b\[[0-9;]*m", "", rendered)
        for label in ["in_sync", "ahead", "behind", "diverged", "unknown"]:
            self.assertNotIn(label, normalized)


if __name__ == "__main__":
    unittest.main()
