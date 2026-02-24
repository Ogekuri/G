## @file test_cmd_ls.py
# @brief Unit tests for ls/lsi/lsa alias commands.

import unittest
from unittest import mock

from git_alias import core


## @brief Test suite for ls/lsi/lsa alias behaviors.
class CmdLsTest(unittest.TestCase):
    ## @brief Verify `cmd_ls` forwards arguments to `git ls-files --exclude-standard`.
    # @return None.
    def test_cmd_ls_forwards_args(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_ls(["-z"])
        run_git.assert_called_once_with(["ls-files", "--exclude-standard"], ["-z"])

    ## @brief Verify `cmd_lsi` forwards arguments to `git ls-files --others --ignored --exclude-standard`.
    # @return None.
    def test_cmd_lsi_forwards_args(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_lsi(["--others"])
        run_git.assert_called_once_with(
            ["ls-files", "--others", "--ignored", "--exclude-standard"],
            ["--others"],
        )

    ## @brief Verify `cmd_lsa` forwards arguments to `git ls-files --others --exclude-standard`.
    # @return None.
    def test_cmd_lsa_forwards_args(self):
        with mock.patch.object(core, "run_git_cmd", return_value=None) as run_git:
            core.cmd_lsa(["-z"])
        run_git.assert_called_once_with(
            ["ls-files", "--others", "--exclude-standard"],
            ["-z"],
        )


if __name__ == "__main__":
    unittest.main()
