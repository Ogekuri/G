import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class CmdReleaseTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_cmd_release_commits_using_detected_version(self):
        with mock.patch.object(core, "_ensure_commit_ready") as ensure, mock.patch.object(
            core, "_determine_canonical_version", return_value="1.2.3"
        ), mock.patch.object(core, "_execute_commit", return_value=None) as execute:
            core.cmd_release([])
        ensure.assert_called_once_with("release")
        execute.assert_called_once_with("release version: 1.2.3", "release")

    def test_cmd_release_handles_version_detection_error(self):
        with mock.patch.object(core, "_ensure_commit_ready"), mock.patch.object(
            core, "_determine_canonical_version", side_effect=core.VersionDetectionError("no version")
        ):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit):
                    core.cmd_release([])
            self.assertIn("no version", err.getvalue())

    def test_cmd_release_rejects_positional_arguments(self):
        with mock.patch.object(core, "_ensure_commit_ready"):
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                with self.assertRaises(SystemExit):
                    core.cmd_release(["unexpected"])
            self.assertIn("does not accept positional arguments", err.getvalue())

    def test_cmd_release_help(self):
        with mock.patch.object(core, "_ensure_commit_ready") as ensure:
            out = io.StringIO()
            with contextlib.redirect_stdout(out):
                core.cmd_release(["--help"])
            ensure.assert_not_called()
            self.assertIn("release -", out.getvalue())
