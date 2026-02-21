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

    def test_patch_release_auto_includes_patch_flag(self):
        # patch level must automatically add --include-patch to changelog flags
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
            core._execute_release_flow("patch")
        changelog.assert_called_once_with(["--force-write", "--include-patch"])

    def test_release_flow_passes_explicit_include_patch_flag(self):
        # user-supplied --include-patch is forwarded without duplication
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
            core._execute_release_flow("patch", changelog_args=["--include-patch"])
        changelog.assert_called_once_with(["--force-write", "--include-patch"])

    def test_minor_release_does_not_auto_include_patch_flag(self):
        # minor level must NOT automatically add --include-patch
        def run_step(_level, step_name, action):
            if step_name == "regenerate changelog":
                action()
            return None

        with mock.patch.object(
            core,
            "_ensure_release_prerequisites",
            return_value={"master": "master", "develop": "develop", "work": "work"},
        ), mock.patch.object(core, "get_version_rules", return_value=[("README.md", "x")]), mock.patch.object(
            core, "_determine_canonical_version", return_value="1.2.0"
        ), mock.patch.object(core, "_bump_semver_version", return_value="1.3.0"), mock.patch.object(
            core, "_run_release_step", side_effect=run_step
        ), mock.patch.object(core, "cmd_changelog") as changelog:
            core._execute_release_flow("minor")
        changelog.assert_called_once_with(["--force-write"])

    def test_release_commands_accept_include_patch_flag(self):
        with mock.patch.object(core, "_run_release_command") as run_release:
            core.cmd_patch(["--include-patch"])
        run_release.assert_called_once_with("patch", changelog_args=["--include-patch"])

    def test_release_commands_reject_unknown_flags(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit):
                core.cmd_patch(["--unexpected"])
        self.assertIn("accepts only --include-patch", err.getvalue())

    def test_patch_release_skips_master_steps(self):
        # patch level MUST NOT execute checkout master / merge develop into master / push master
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

        self.assertNotIn("checkout master", steps)
        self.assertNotIn("merge develop into master", steps)
        self.assertNotIn("push master", steps)

    def test_major_release_includes_master_steps(self):
        # major level MUST execute checkout master / merge develop into master / push master
        steps = []

        def record_step(level, step_name, action):
            steps.append(step_name)

        with mock.patch.object(
            core,
            "_ensure_release_prerequisites",
            return_value={"master": "master", "develop": "develop", "work": "work"},
        ), mock.patch.object(core, "get_version_rules", return_value=[("README.md", "x")]), mock.patch.object(
            core, "_determine_canonical_version", return_value="1.2.0"
        ), mock.patch.object(core, "_bump_semver_version", return_value="2.0.0"), mock.patch.object(
            core, "_run_release_step", side_effect=record_step
        ):
            core._execute_release_flow("major")

        self.assertIn("checkout master", steps)
        self.assertIn("merge develop into master", steps)
        self.assertIn("push master", steps)

    def test_minor_release_includes_master_steps(self):
        # minor level MUST execute checkout master / merge develop into master / push master
        steps = []

        def record_step(level, step_name, action):
            steps.append(step_name)

        with mock.patch.object(
            core,
            "_ensure_release_prerequisites",
            return_value={"master": "master", "develop": "develop", "work": "work"},
        ), mock.patch.object(core, "get_version_rules", return_value=[("README.md", "x")]), mock.patch.object(
            core, "_determine_canonical_version", return_value="1.2.0"
        ), mock.patch.object(core, "_bump_semver_version", return_value="1.3.0"), mock.patch.object(
            core, "_run_release_step", side_effect=record_step
        ):
            core._execute_release_flow("minor")

        self.assertIn("checkout master", steps)
        self.assertIn("merge develop into master", steps)
        self.assertIn("push master", steps)

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
