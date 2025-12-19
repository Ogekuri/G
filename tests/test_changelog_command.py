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

    def test_generate_document_orders_releases_descending(self):
        tags = [
            core.TagInfo(name="v1.0.0", iso_date="2024-01-01", object_name="a"),
            core.TagInfo(name="v1.1.0", iso_date="2024-02-01", object_name="b"),
            core.TagInfo(name="v1.2.0", iso_date="2024-03-01", object_name="c"),
        ]
        with mock.patch.object(core, "list_tags_sorted_by_date", return_value=tags), mock.patch.object(
            core, "_canonical_origin_base", return_value=None
        ), mock.patch.object(
            core,
            "generate_section_for_range",
            side_effect=["sec-old", "sec-mid", "sec-new"],
        ), mock.patch.object(core, "build_history_section", return_value="# History\nchrono"):
            document = core.generate_changelog_document(Path("/tmp"), include_unreleased=False)
        sections = [line for line in document.splitlines() if line.startswith("sec-")]
        self.assertEqual(sections, ["sec-new", "sec-mid", "sec-old"])
        self.assertIn("# History\nchrono", document)

    def test_history_uses_tags_merged_into_head(self):
        repo_root = Path("/tmp")
        tags = [core.TagInfo(name="v1.0.0", iso_date="2024-01-01", object_name="a")]
        history_tags = [core.TagInfo(name="v1.1.0", iso_date="2024-02-01", object_name="b")]

        def list_tags(root, merged_ref=None):
            self.assertEqual(root, repo_root)
            if merged_ref == "HEAD":
                return history_tags
            return tags

        with mock.patch.object(core, "list_tags_sorted_by_date", side_effect=list_tags), mock.patch.object(
            core, "_canonical_origin_base", return_value="https://example.com/repo"
        ), mock.patch.object(
            core, "generate_section_for_range", return_value=None
        ), mock.patch.object(core, "build_history_section", return_value="# History\n") as build_history:
            core.generate_changelog_document(repo_root, include_unreleased=False)
        build_history.assert_called_once_with(repo_root, history_tags, False)
