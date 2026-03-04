## @file test_cmd_ls.py
# @brief Unit tests for ls/lsi/lsa alias commands.

import unittest
from unittest import mock

from git_alias import core


## @brief Test suite for ls/lsa alias behaviors.
class CmdLsTest(unittest.TestCase):
    ## @brief Verify `cmd_ls` forwards arguments to `git ls-files --exclude-standard`.
    # @return None.
    def test_cmd_ls_forwards_args(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_ls(["-z"])
        run_git.assert_called_once_with(["ls-files", "--exclude-standard"], ["-z"])

    ## @brief Verify `cmd_lsa` forwards arguments to `git ls-files --others --exclude-standard`.
    # @return None.
    def test_cmd_lsa_forwards_args(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_lsa(["-z"])
        run_git.assert_called_once_with(
            ["ls-files", "--others", "--exclude-standard"],
            ["-z"],
        )


## @brief Test suite for `cmd_lsi` filtering and `--include-all` behaviors.
# @details Validates REQ-080 (default filtering), REQ-120 (constant), REQ-121 (--include-all).
class CmdLsiTest(unittest.TestCase):
    ## @brief Verify `LSI_DEFAULT_EXCLUDED_DIRS` is a frozenset with exactly 21 entries.
    # @return None.
    # @satisfies REQ-120
    def test_lsi_default_excluded_dirs_is_frozenset(self):
        self.assertIsInstance(core.LSI_DEFAULT_EXCLUDED_DIRS, frozenset)
        self.assertEqual(len(core.LSI_DEFAULT_EXCLUDED_DIRS), 21)

    ## @brief Verify `LSI_DEFAULT_EXCLUDED_DIRS` contains all required entries.
    # @return None.
    # @satisfies REQ-120
    def test_lsi_default_excluded_dirs_entries(self):
        expected = {
            ".cache",
            ".eslintcache",
            ".git",
            ".mypy_cache",
            ".npm",
            ".parcel-cache",
            ".pytest_cache",
            ".ruff_cache",
            ".sass-cache",
            ".terragrunt-cache",
            ".tox",
            ".venv",
            ".vscode",
            "__pycache__",
            "build",
            "dist",
            "htmlcov",
            "node_modules",
            "temp",
            "tmp",
            "venv",
        }
        self.assertEqual(core.LSI_DEFAULT_EXCLUDED_DIRS, expected)

    ## @brief Verify `cmd_lsi` filters out lines whose first path component is excluded.
    # @return None.
    # @satisfies REQ-080
    def test_cmd_lsi_filters_excluded_dirs(self):
        git_output = (
            "node_modules/pkg/index.js\nsrc/main.py\n.venv/lib/site.py\ndocs/readme.md"
        )
        with mock.patch.object(core, "run_git_text", return_value=git_output):
            with mock.patch("builtins.print") as mock_print:
                core.cmd_lsi([])
        mock_print.assert_any_call("src/main.py")
        mock_print.assert_any_call("docs/readme.md")
        self.assertEqual(mock_print.call_count, 2)

    ## @brief Verify `cmd_lsi` handles empty git output gracefully.
    # @return None.
    # @satisfies REQ-080
    def test_cmd_lsi_empty_output(self):
        with mock.patch.object(core, "run_git_text", return_value=""):
            with mock.patch("builtins.print") as mock_print:
                result = core.cmd_lsi([])
        mock_print.assert_not_called()
        self.assertIsNone(result)

    ## @brief Verify `cmd_lsi` passes extra arguments to the git command.
    # @return None.
    # @satisfies REQ-080
    def test_cmd_lsi_forwards_extra_args(self):
        with mock.patch.object(
            core, "run_git_text", return_value="readme.txt"
        ) as run_text:
            with mock.patch("builtins.print"):
                core.cmd_lsi(["-z"])
        run_text.assert_called_once_with(
            ["ls-files", "--others", "--ignored", "--exclude-standard", "-z"]
        )

    ## @brief Verify `cmd_lsi --include-all` bypasses filtering via `run_git_cmd`.
    # @return None.
    # @satisfies REQ-121
    def test_cmd_lsi_include_all_bypasses_filter(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_lsi(["--include-all"])
        run_git.assert_called_once_with(
            ["ls-files", "--others", "--ignored", "--exclude-standard"],
            [],
        )

    ## @brief Verify `cmd_lsi --include-all` with extra args forwards them correctly.
    # @return None.
    # @satisfies REQ-121
    def test_cmd_lsi_include_all_with_extra_args(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_lsi(["--include-all", "-z"])
        run_git.assert_called_once_with(
            ["ls-files", "--others", "--ignored", "--exclude-standard", "-z"],
            [],
        )

    ## @brief Verify `cmd_lsi` prints paths not matching any excluded first component.
    # @return None.
    # @satisfies REQ-080
    def test_cmd_lsi_allows_non_excluded_paths(self):
        git_output = "custom_dir/file.txt\nanother/deep/path.py"
        with mock.patch.object(core, "run_git_text", return_value=git_output):
            with mock.patch("builtins.print") as mock_print:
                core.cmd_lsi([])
        calls = [c.args[0] for c in mock_print.call_args_list]
        self.assertEqual(calls, ["custom_dir/file.txt", "another/deep/path.py"])

    ## @brief Verify `cmd_lsi` filters a bare excluded name (no slash) correctly.
    # @return None.
    # @satisfies REQ-080
    def test_cmd_lsi_filters_bare_excluded_name(self):
        git_output = "dist\nbuild\nkeep.txt"
        with mock.patch.object(core, "run_git_text", return_value=git_output):
            with mock.patch("builtins.print") as mock_print:
                core.cmd_lsi([])
        mock_print.assert_called_once_with("keep.txt")


if __name__ == "__main__":
    unittest.main()
