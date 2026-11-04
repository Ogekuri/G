import contextlib
import io
import subprocess
import unittest
from unittest import mock

from git_alias import core


class RemoteStatusTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)
        core._REMOTE_REFS_UPDATED = False

    def test_has_remote_develop_updates_true_when_remote_ahead(self):
        with mock.patch.object(core, "_refresh_remote_refs") as refresh, mock.patch.object(
            core, "run_git_text", return_value="0 2"
        ):
            self.assertTrue(core.has_remote_develop_updates())
            refresh.assert_called_once()

    def test_has_remote_master_updates_false_when_in_sync(self):
        with mock.patch.object(core, "_refresh_remote_refs") as refresh, mock.patch.object(
            core, "run_git_text", return_value="1 0"
        ):
            self.assertFalse(core.has_remote_master_updates())
            refresh.assert_called_once()

    ## @brief Verify origin-scoped refresh runs once and reports success.
    # @details The refresh MUST execute `git remote update origin` (single
    #          configured remote; never `git remote -v update`, which fetches
    #          every configured remote) and MUST return True on success.
    # @param self {RemoteStatusTest} Isolated test instance.
    # @return {None} Assert refresh argv, caching, and boolean result.
    def test_refresh_remote_refs_runs_once(self):
        core._REMOTE_REFS_UPDATED = False
        with mock.patch.object(core, "run_git_cmd") as run_git:
            self.assertTrue(core._refresh_remote_refs())
            run_git.assert_called_once_with(["remote", "update", "origin"])
            core._refresh_remote_refs()
            run_git.assert_called_once()

    ## @brief Verify refresh reports failure without caching completion.
    # @details A failed `git remote update origin` MUST return False, print the
    #          English warning, and leave the cache unset so callers may retry.
    # @param self {RemoteStatusTest} Isolated test instance.
    # @return {None} Assert boolean result and retry-enabled cache state.
    def test_refresh_remote_refs_returns_false_on_failure(self):
        core._REMOTE_REFS_UPDATED = False
        failure = core.CommandExecutionError(
            subprocess.CalledProcessError(1, ["git", "remote", "update", "origin"])
        )
        with mock.patch.object(core, "run_git_cmd", side_effect=failure) as run_git, \
                contextlib.redirect_stderr(io.StringIO()) as stderr:
            self.assertFalse(core._refresh_remote_refs())
            self.assertFalse(core._REMOTE_REFS_UPDATED)
            core._refresh_remote_refs()
            self.assertEqual(run_git.call_count, 2)
        self.assertIn("Unable to update remote references", stderr.getvalue())
