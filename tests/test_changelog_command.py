import contextlib
import io
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from git_alias import core


class ChangelogCommandTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_creates_file_when_missing(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            with mock.patch.object(core, "is_inside_git_repo", return_value=True), mock.patch.object(
                core, "get_git_root", return_value=repo_root
            ), mock.patch.object(core, "generate_changelog_document", return_value="# Changelog\n"):
                core.cmd_changelog([])
            content = (repo_root / "CHANGELOG.md").read_text(encoding="utf-8")
            self.assertEqual(content, "# Changelog\n")

    def test_refuses_overwrite_without_force(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            (repo_root / "CHANGELOG.md").write_text("old", encoding="utf-8")
            with mock.patch.object(core, "is_inside_git_repo", return_value=True), mock.patch.object(
                core, "get_git_root", return_value=repo_root
            ), mock.patch.object(core, "generate_changelog_document", return_value="new"):
                with self.assertRaises(SystemExit):
                    core.cmd_changelog([])

    def test_print_only_outputs_content(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            with mock.patch.object(core, "is_inside_git_repo", return_value=True), mock.patch.object(
                core, "get_git_root", return_value=repo_root
            ), mock.patch.object(core, "generate_changelog_document", return_value="markdown"):
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    core.cmd_changelog(["--print-only"])
                self.assertEqual(buffer.getvalue(), "markdown")
            self.assertFalse((repo_root / "CHANGELOG.md").exists())

    def test_include_unreleased_flag_propagates(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            with mock.patch.object(core, "is_inside_git_repo", return_value=True), mock.patch.object(
                core, "get_git_root", return_value=repo_root
            ), mock.patch.object(core, "generate_changelog_document", return_value="data") as gen:
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    core.cmd_changelog(["--include-unreleased", "--print-only"])
                gen.assert_called_once_with(repo_root, True)
