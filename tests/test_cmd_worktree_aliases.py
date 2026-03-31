import contextlib
import io
import unittest
from pathlib import Path
from unittest import mock

from git_alias import core


## @brief Validate worktree command registration and coordinated deletion behavior.
# @details Covers alias registration/help exposure, passthrough behavior for list/prune commands,
#          and all-or-nothing deletion semantics shared by `bd` and `wtd`.
class CmdWorktreeAliasesTest(unittest.TestCase):
    ## @brief Reset mutable CLI config to deterministic defaults before each test.
    # @return None.
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    ## @brief Verify worktree aliases are registered in command and help maps.
    # @return None.
    # @satisfies REQ-003, REQ-077
    def test_worktree_aliases_are_registered_with_help(self):
        for alias in ("wt", "wtl", "wtp", "wtd"):
            self.assertIn(alias, core.COMMANDS)
            self.assertIn(alias, core.HELP_TEXTS)

    ## @brief Verify `cmd_wt` forwards list execution unchanged.
    # @return None.
    def test_cmd_wt_runs_worktree_list(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_wt([])
            run_git.assert_called_once_with(["worktree", "list"], [])

    ## @brief Verify `cmd_wtl` forwards optional list arguments unchanged.
    # @return None.
    def test_cmd_wtl_forwards_list_arguments(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_wtl(["--porcelain", "-z"])
            run_git.assert_called_once_with(["worktree", "list"], ["--porcelain", "-z"])

    ## @brief Verify `cmd_wtp` forwards prune arguments unchanged.
    # @return None.
    def test_cmd_wtp_forwards_prune_arguments(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_wtp(["--expire", "now", "-n", "-v"])
            run_git.assert_called_once_with(["worktree", "prune"], ["--expire", "now", "-n", "-v"])

    ## @brief Verify `cmd_wtd` help short-circuits before git inspection.
    # @return None.
    def test_cmd_wtd_help_shortcircuits(self):
        with (
            mock.patch.object(core, "_list_worktree_associations") as associations,
            mock.patch.object(core, "run_git_cmd") as run_git,
        ):
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                core.cmd_wtd(["--help"])
        self.assertIn("wtd -", stdout.getvalue())
        associations.assert_not_called()
        run_git.assert_not_called()

    ## @brief Verify `cmd_wtd` rejects force flags.
    # @return None.
    # @satisfies REQ-077
    def test_cmd_wtd_rejects_force_flag(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as ctx:
                core.cmd_wtd(["--force"])
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("does not support force flags", stderr.getvalue())

    ## @brief Verify `cmd_bd` rejects force flags.
    # @return None.
    # @satisfies REQ-019
    def test_cmd_bd_rejects_force_flag(self):
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            with self.assertRaises(SystemExit) as ctx:
                core.cmd_bd(["-D"])
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("does not support force flags", stderr.getvalue())

    ## @brief Verify worktree porcelain parsing preserves path and branch associations.
    # @return None.
    # @satisfies REQ-139
    def test_list_worktree_associations_parses_porcelain_output(self):
        payload = (
            "worktree /repo/main\n"
            "HEAD abcdef\n"
            "branch refs/heads/main\n"
            "\n"
            "worktree /repo/feature-tree\n"
            "HEAD 123456\n"
            "branch refs/heads/feature/demo\n"
            "\n"
        )
        with mock.patch.object(core, "run_git_text", return_value=payload):
            associations = core._list_worktree_associations()
        self.assertEqual(
            associations,
            [
                core.WorktreeInfo(path=Path("/repo/main"), branch_name="main"),
                core.WorktreeInfo(path=Path("/repo/feature-tree"), branch_name="feature/demo"),
            ],
        )

    ## @brief Verify branch preflight accepts HEAD-merged branches without upstream.
    # @return None.
    def test_preflight_branch_delete_accepts_head_merged_branch(self):
        with (
            mock.patch.object(core, "run_git_text", side_effect=["abc123", ""]),
            mock.patch.object(core, "_is_commit_ancestor", return_value=True) as is_ancestor,
        ):
            core._preflight_branch_delete("feature/demo", "bd")
        is_ancestor.assert_called_once_with("abc123", "HEAD")

    ## @brief Verify branch preflight rejects unmerged branch state.
    # @return None.
    # @satisfies REQ-140
    def test_preflight_branch_delete_rejects_unmerged_branch(self):
        stderr = io.StringIO()
        with (
            mock.patch.object(core, "run_git_text", side_effect=["abc123", ""]),
            mock.patch.object(core, "_is_commit_ancestor", return_value=False),
            contextlib.redirect_stderr(stderr),
        ):
            with self.assertRaises(SystemExit) as ctx:
                core._preflight_branch_delete("feature/demo", "bd")
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("not merged into HEAD", stderr.getvalue())

    ## @brief Verify worktree preflight rejects dirty linked worktrees.
    # @return None.
    # @satisfies REQ-140
    def test_preflight_worktree_delete_rejects_dirty_worktree(self):
        target = Path("/tmp/feature-tree")
        stderr = io.StringIO()
        with (
            mock.patch.object(core, "get_git_root", return_value=Path("/repo/main")),
            mock.patch.object(Path, "exists", return_value=True),
            mock.patch.object(core, "run_git_text", return_value=" M file.txt"),
            contextlib.redirect_stderr(stderr),
        ):
            with self.assertRaises(SystemExit) as ctx:
                core._preflight_worktree_delete(target, "wtd")
        self.assertEqual(ctx.exception.code, 1)
        self.assertIn("cannot be deleted without force because it is not clean", stderr.getvalue())

    ## @brief Verify `cmd_wtd` deletes only the worktree when no branch association exists.
    # @return None.
    # @satisfies REQ-143
    def test_cmd_wtd_deletes_only_worktree_when_unassociated(self):
        target = Path("../feature-tree").resolve()
        with (
            mock.patch.object(core, "_list_worktree_associations", return_value=[]),
            mock.patch.object(core, "_preflight_worktree_delete", return_value=None) as preflight,
            mock.patch.object(core, "run_git_cmd", return_value=None) as run_git,
        ):
            core.cmd_wtd(["../feature-tree"])
        preflight.assert_called_once_with(target, "wtd")
        run_git.assert_called_once_with(["worktree", "remove", str(target)])

    ## @brief Verify `cmd_bd` deletes only the branch when no worktree association exists.
    # @return None.
    # @satisfies REQ-138
    def test_cmd_bd_deletes_only_branch_when_unassociated(self):
        with (
            mock.patch.object(core, "_list_worktree_associations", return_value=[]),
            mock.patch.object(core, "_preflight_branch_delete", return_value=None) as preflight,
            mock.patch.object(core, "run_git_cmd", return_value=None) as run_git,
        ):
            core.cmd_bd(["feature/demo"])
        preflight.assert_called_once_with("feature/demo", "bd")
        run_git.assert_called_once_with(["branch", "-d", "feature/demo"])

    ## @brief Verify `cmd_bd` performs paired deletion and prints explicit evidence.
    # @return None.
    # @satisfies REQ-139, REQ-140, REQ-141, REQ-142
    def test_cmd_bd_deletes_associated_worktree_and_branch(self):
        info = core.WorktreeInfo(
            path=Path("/tmp/feature-tree"),
            branch_name="feature/demo",
        )
        stdout = io.StringIO()
        with (
            mock.patch.object(core, "_list_worktree_associations", return_value=[info]),
            mock.patch.object(core, "_preflight_worktree_delete", return_value=None) as preflight_worktree,
            mock.patch.object(core, "_preflight_branch_delete", return_value=None) as preflight_branch,
            mock.patch.object(core, "run_git_cmd", return_value=None) as run_git,
            contextlib.redirect_stdout(stdout),
        ):
            core.cmd_bd(["feature/demo"])
        preflight_worktree.assert_called_once_with(info.path, "bd")
        preflight_branch.assert_called_once_with("feature/demo", "bd")
        self.assertEqual(
            run_git.call_args_list,
            [
                mock.call(["worktree", "remove", str(info.path)]),
                mock.call(["branch", "-d", "feature/demo"]),
            ],
        )
        output = stdout.getvalue()
        self.assertIn(f"Deleted worktree: {info.path}", output)
        self.assertIn("Deleted branch: feature/demo", output)

    ## @brief Verify `cmd_wtd` performs paired deletion and prints explicit evidence.
    # @return None.
    # @satisfies REQ-139, REQ-140, REQ-141, REQ-142
    def test_cmd_wtd_deletes_associated_worktree_and_branch(self):
        info = core.WorktreeInfo(
            path=Path("/tmp/feature-tree"),
            branch_name="feature/demo",
        )
        stdout = io.StringIO()
        with (
            mock.patch.object(core, "_list_worktree_associations", return_value=[info]),
            mock.patch.object(core, "_preflight_worktree_delete", return_value=None) as preflight_worktree,
            mock.patch.object(core, "_preflight_branch_delete", return_value=None) as preflight_branch,
            mock.patch.object(core, "run_git_cmd", return_value=None) as run_git,
            contextlib.redirect_stdout(stdout),
        ):
            core.cmd_wtd([str(info.path)])
        preflight_worktree.assert_called_once_with(info.path, "wtd")
        preflight_branch.assert_called_once_with("feature/demo", "wtd")
        self.assertEqual(
            run_git.call_args_list,
            [
                mock.call(["worktree", "remove", str(info.path)]),
                mock.call(["branch", "-d", "feature/demo"]),
            ],
        )
        output = stdout.getvalue()
        self.assertIn(f"Deleted worktree: {info.path}", output)
        self.assertIn("Deleted branch: feature/demo", output)

    ## @brief Verify paired deletion aborts before mutations when branch preflight fails.
    # @return None.
    # @satisfies REQ-140
    def test_cmd_bd_aborts_without_partial_delete_when_branch_preflight_fails(self):
        info = core.WorktreeInfo(
            path=Path("/tmp/feature-tree"),
            branch_name="feature/demo",
        )
        stderr = io.StringIO()
        with (
            mock.patch.object(core, "_list_worktree_associations", return_value=[info]),
            mock.patch.object(core, "_preflight_worktree_delete", return_value=None),
            mock.patch.object(core, "_preflight_branch_delete", side_effect=SystemExit(1)),
            mock.patch.object(core, "run_git_cmd") as run_git,
            contextlib.redirect_stderr(stderr),
        ):
            with self.assertRaises(SystemExit) as ctx:
                core.cmd_bd(["feature/demo"])
        self.assertEqual(ctx.exception.code, 1)
        run_git.assert_not_called()

    ## @brief Verify paired deletion aborts before mutations when worktree preflight fails.
    # @return None.
    # @satisfies REQ-140
    def test_cmd_wtd_aborts_without_partial_delete_when_worktree_preflight_fails(self):
        info = core.WorktreeInfo(
            path=Path("/tmp/feature-tree"),
            branch_name="feature/demo",
        )
        with (
            mock.patch.object(core, "_list_worktree_associations", return_value=[info]),
            mock.patch.object(core, "_preflight_worktree_delete", side_effect=SystemExit(1)),
            mock.patch.object(core, "_preflight_branch_delete") as preflight_branch,
            mock.patch.object(core, "run_git_cmd") as run_git,
        ):
            with self.assertRaises(SystemExit) as ctx:
                core.cmd_wtd([str(info.path)])
        self.assertEqual(ctx.exception.code, 1)
        preflight_branch.assert_not_called()
        run_git.assert_not_called()


if __name__ == "__main__":
    unittest.main()
