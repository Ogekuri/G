# Release Workflow

This document lists the stages and functions executed during `major`, `minor`, and `patch` release processes.

## Initial Common Stages
Preliminary preparation and validation operations.

*   **Config Loading**: Reading the `.g.conf` file and initializing parameters.
*   **Update Check**: Online check for new CLI version availability.
*   **Argument Parsing**: Validation of `--include-unreleased` and `--include-draft` flags.
*   **Prerequisites Check**: Verifying the existence of branches (`master`, `develop`, `work`), remote (`origin`), and "clean" status.
*   **Version Detection**: Scanning configured files (root-anchored glob patterns) to determine the current version.
*   **New Version Calculation**: Determining the next version number based on the converter used.

## Processing Stages (Release Flow)
Sequence of repository state transformation (`_execute_release_flow` function).

*   **Update Versions**: Updating version strings in source files.
*   **Stage Files**: Adding all modified files to the staging area.
*   **Create Release Commit**: Creating the preliminary release commit ("release version: X.Y.Z").
*   **Tag Release**: Creating a temporary git tag for the new version. This allows the changelog generator to correctly identify the new commit range.
*   **Regenerate Changelog**: Generating the updated `CHANGELOG.md` file including commits up to the new tag.
*   **Stage Changelog**: Adding the generated changelog to the staging area.
*   **Amend Release Commit**: Executing `git commit --amend --no-edit`. This operation incorporates the `CHANGELOG.md` file into the previously created release commit, maintaining a single atomic commit for the version.
*   **Retag Release**: Forcing the tag move (`--force`) to the new hash of the amended commit (amend changes the commit hash).
*   **Checkout Develop**: Switching to the `develop` branch.
*   **Merge Work into Develop**: Merging release changes into `develop`.
*   **Push Develop**: Sending `develop` updates to the remote.
*   **Checkout Master**: Switching to the `master` branch.
*   **Merge Develop into Master**: Merging `develop` into `master`.
*   **Push Master**: Sending `master` updates to the remote.
*   **Return to Work**: Returning to the original work branch.
*   **Show Release Details**: Displaying details of the release commit.
*   **Push Tags**: Sending tags to the origin remote.

## Final Common Stages
Concluding operations.

*   **Success Message**: User confirmation of operation completion.
*   **Error Handling**: Exception capture and exit with appropriate error code in case of failure.
