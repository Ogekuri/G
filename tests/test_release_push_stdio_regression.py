## @brief Regression reproducer suite for release-publication transport defects.
# @details Reproduces the release regression introduced by commit 8e4abd26 and
#          evidenced by the failed 0.11.0 release: (1) `git push` executed with
#          piped stdio cannot perform interactive SSH authentication and hides
#          live push output, while the same run's inherited-stdio fetch succeeded;
#          (2) the release preflight silently continues after the remote-reference
#          refresh fails, so the whole local release is prepared before the
#          unverifiable remote state surfaces at publication time (REQ-026,
#          REQ-047). All Git boundaries are mocked; no subprocess, network, or
#          filesystem access.

import unittest
from unittest import mock

from git_alias import core


## @brief Verify release publication and preflight transport contracts in isolation.
# @details Every Git dependency is replaced by deterministic mocks; observable
#          wrapper selection and control flow are the only assertions.
class ReleasePushStdioRegressionTest(unittest.TestCase):
    ## @brief Reset configuration and remote-refresh cache state.
    # @details O(1) fixture setup; guarantees deterministic branch-name resolution.
    # @param self {ReleasePushStdioRegressionTest} Isolated test instance.
    # @return {None} Populates default configuration state.
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)
        core._REMOTE_REFS_UPDATED = False

    ## @brief Reproduce piped-stdio publication and assert inherited-stdio delegation.
    # @details REQ-181 publication MUST delegate `git push` through the shared
    #          inherited-stdio git wrapper (`run_git_cmd`) used by every other git
    #          delegation, NOT through the piped-stdio text wrapper (`run_git_text`),
    #          so interactive SSH/credential authentication stays possible and push
    #          output reaches the user terminal. Fails while `_push_release_refs`
    #          still pipes stdio (regression from commit 8e4abd26).
    # @param self {ReleasePushStdioRegressionTest} Isolated test instance.
    # @return {None} Assert exact publication argv and wrapper selection.
    def test_release_push_delegates_through_inherited_stdio_wrapper(self):
        with mock.patch.object(
            core, "run_git_cmd"
        ) as run_git, mock.patch.object(core, "run_git_text") as run_text:
            core._push_release_refs("minor", "1.3.0", "master", include_tag=True)
        run_git.assert_called_once_with(
            [
                "push", "--no-follow-tags", "--atomic", "origin",
                "refs/heads/master:refs/heads/master",
                "refs/tags/v1.3.0:refs/tags/v1.3.0",
            ]
        )
        run_text.assert_not_called()

    ## @brief Reproduce fail-open preflight and assert fail-closed abort.
    # @details REQ-026 and REQ-047 require release commands to enforce the
    #          remote-update prerequisite; when the remote-reference refresh fails,
    #          the preflight MUST raise ReleaseError before any local mutation.
    #          Fails while `_ensure_release_prerequisites` ignores refresh failure.
    # @param self {ReleasePushStdioRegressionTest} Isolated test instance.
    # @return {None} Assert ReleaseError mentions remote references.
    def test_release_preflight_aborts_when_remote_refresh_fails(self):
        with mock.patch.object(
            core, "_local_branch_exists", return_value=True
        ), mock.patch.object(core, "_refresh_remote_refs", return_value=False):
            with self.assertRaises(core.ReleaseError) as error:
                core._ensure_release_prerequisites()
            self.assertIn("remote", str(error.exception).lower())

    ## @brief Verify the preflight proceeds only after a successful refresh.
    # @details With all downstream checks satisfied, a successful refresh MUST
    #          let the preflight return the configured branch map unchanged.
    # @param self {ReleasePushStdioRegressionTest} Isolated test instance.
    # @return {None} Assert configured branch map emission.
    def test_release_preflight_passes_when_remote_refresh_succeeds(self):
        with mock.patch.object(
            core, "_local_branch_exists", return_value=True
        ), mock.patch.object(
            core, "_refresh_remote_refs", return_value=True
        ), mock.patch.object(
            core, "_remote_branch_exists", return_value=True
        ), mock.patch.object(
            core, "has_remote_branch_updates", return_value=False
        ), mock.patch.object(
            core, "_current_branch_name", return_value="work"
        ), mock.patch.object(core, "_git_status_lines", return_value=[]):
            branches = core._ensure_release_prerequisites()
        self.assertEqual(
            branches, {"master": "master", "develop": "develop", "work": "work"}
        )


if __name__ == "__main__":
    unittest.main()
