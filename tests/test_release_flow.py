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
