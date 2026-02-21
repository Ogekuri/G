import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class ReleaseFlowTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_release_flow_pushes_tags_last(self):
        steps = []

        def record_step(level, step_name, action):
            steps.append(step_name)

        with mock.patch.object(
            core,
            "_ensure_release_prerequisites",
            return_value={"master": "master", "develop": "develop", "work": "work"},
        ), mock.patch.object(core, "get_version_rules", return_value=[("README.md", "x")]), mock.patch.object(
            core, "_determine_canonical_version", return_value="1.2.3"
        ), mock.patch.object(core, "_bump_semver_version", return_value="1.2.4"), mock.patch.object(
            core, "_run_release_step", side_effect=record_step
        ):
            core._execute_release_flow("patch")

        self.assertTrue(steps)
        self.assertEqual(steps[-1], "push tags")

    def test_release_step_formats_output_with_level(self):
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            core._run_release_step("major", "stage files", lambda: None)
        self.assertEqual(
            buffer.getvalue().strip(),
            "--- [release:major] Step 'stage files' completed successfully. ---",
        )

    def test_release_flow_emits_blank_line_before_steps(self):
        with mock.patch.object(
            core,
            "_ensure_release_prerequisites",
            return_value={"master": "master", "develop": "develop", "work": "work"},
        ), mock.patch.object(core, "get_version_rules", return_value=[("README.md", "x")]), mock.patch.object(
            core, "_determine_canonical_version", return_value="1.2.3"
        ), mock.patch.object(core, "_bump_semver_version", return_value="1.2.4"), mock.patch.object(
            core, "_run_release_step", return_value=None
        ):
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                core._execute_release_flow("minor")
        self.assertTrue(buffer.getvalue().startswith("\n"))

    def test_release_flow_passes_changelog_flags(self):
        def run_step(_level, step_name, action):
            if step_name == "regenerate changelog":
                action()
            return None

        with mock.patch.object(
            core,
            "_ensure_release_prerequisites",
            return_value={"master": "master", "develop": "develop", "work": "work"},
        ), mock.patch.object(core, "get_version_rules", return_value=[("README.md", "x")]), mock.patch.object(
            core, "_determine_canonical_version", return_value="1.2.3"
        ), mock.patch.object(core, "_bump_semver_version", return_value="1.2.4"), mock.patch.object(
            core, "_run_release_step", side_effect=run_step
        ), mock.patch.object(core, "cmd_changelog") as changelog:
            core._execute_release_flow("patch", changelog_args=["--include-unreleased"])
        changelog.assert_called_once_with(["--force-write", "--include-unreleased"])

    def test_release_commands_accept_changelog_flags(self):
        with mock.patch.object(core, "_run_release_command") as run_release:
            core.cmd_major(["--include-unreleased"])
        run_release.assert_called_once_with("major", changelog_args=["--include-unreleased"])

    def test_patch_accepts_include_unreleased_flag(self):
        with mock.patch.object(core, "_run_release_command") as run_release:
            core.cmd_patch(["--include-unreleased"])
        run_release.assert_called_once_with("patch", changelog_args=["--include-unreleased"])

    def test_release_commands_reject_unknown_flags(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit):
                core.cmd_patch(["--unexpected"])
        self.assertIn("accepts only --include-unreleased", err.getvalue())

    def test_create_release_commit_for_flow_uses_release_amend_strategy(self):
        with mock.patch.object(core, "_ensure_commit_ready"), mock.patch.object(core, "_execute_commit") as execute_commit:
            core._create_release_commit_for_flow("2.0.0")
        execute_commit.assert_called_once_with("release: Release version 2.0.0", "release")

    def test_release_flow_uses_internal_release_commit_builder(self):
        def run_step(_level, step_name, action):
            if step_name == "create release commit":
                action()
            return None

        with mock.patch.object(
            core,
            "_ensure_release_prerequisites",
            return_value={"master": "master", "develop": "develop", "work": "work"},
        ), mock.patch.object(core, "get_version_rules", return_value=[("README.md", "x")]), mock.patch.object(
            core, "_determine_canonical_version", return_value="1.2.3"
        ), mock.patch.object(core, "_bump_semver_version", return_value="1.2.4"), mock.patch.object(
            core, "_run_release_step", side_effect=run_step
        ), mock.patch.object(core, "_create_release_commit_for_flow") as create_release_commit:
            core._execute_release_flow("patch")

        create_release_commit.assert_called_once_with("1.2.4")
