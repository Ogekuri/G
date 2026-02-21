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

    def test_include_patch_flag_propagates(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            with mock.patch.object(core, "is_inside_git_repo", return_value=True), mock.patch.object(
                core, "get_git_root", return_value=repo_root
            ), mock.patch.object(core, "generate_changelog_document", return_value="data") as gen:
                buffer = io.StringIO()
                with contextlib.redirect_stdout(buffer):
                    core.cmd_changelog(["--include-patch", "--print-only"])
                gen.assert_called_once_with(repo_root, True)

    def test_unknown_flag_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            repo_root = Path(tmpdir)
            with mock.patch.object(core, "is_inside_git_repo", return_value=True), mock.patch.object(
                core, "get_git_root", return_value=repo_root
            ):
                buffer = io.StringIO()
                with contextlib.redirect_stderr(buffer):
                    with self.assertRaises(SystemExit):
                        core.cmd_changelog(["--include-unreleased", "--print-only"])
                self.assertIn("Invalid arguments for g changelog.", buffer.getvalue())

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
                document = core.generate_changelog_document(Path("/tmp"), include_patch=False)
        sections = [line for line in document.splitlines() if line.startswith("sec-")]
        self.assertEqual(sections, ["sec-new", "sec-mid", "sec-old"])
        self.assertIn("# History\nchrono", document)

    def test_generate_document_only_includes_minor_tags_by_default(self):
        repo_root = Path("/tmp")
        release_tags = [
            core.TagInfo(name="v0.0.9", iso_date="2024-02-01", object_name="b"),
            core.TagInfo(name="v0.1.0", iso_date="2024-03-01", object_name="c"),
        ]

        def list_tags(root, merged_ref=None):
            self.assertEqual(root, repo_root)
            return release_tags

        with mock.patch.object(core, "list_tags_sorted_by_date", side_effect=lambda root, merged_ref=None: list_tags(root, merged_ref)), mock.patch.object(
            core, "_canonical_origin_base", return_value=None
        ), mock.patch.object(core, "build_history_section", return_value="# History\n"), mock.patch.object(
            core, "generate_section_for_range", return_value="sec"
        ) as generate_section:
            core.generate_changelog_document(repo_root, include_patch=False)
        # v0.0.9 is not a minor release; only v0.1.0 produces a section
        self.assertEqual(generate_section.call_count, 1)

    def test_generate_document_uses_minor_tag_ranges_only(self):
        tags = [
            core.TagInfo(name="v0.0.5", iso_date="2024-01-01", object_name="a"),
            core.TagInfo(name="v0.1.0", iso_date="2024-02-01", object_name="b"),
            core.TagInfo(name="v0.2.0", iso_date="2024-03-01", object_name="c"),
        ]
        calls = []

        def record_range(_root, _title, _date, rev_range, expected_version=None):
            calls.append(rev_range)
            return f"sec-{rev_range}"

        with mock.patch.object(core, "list_tags_sorted_by_date", return_value=tags), mock.patch.object(
            core, "_canonical_origin_base", return_value=None
        ), mock.patch.object(
            core, "generate_section_for_range", side_effect=record_range
        ), mock.patch.object(core, "build_history_section", return_value=None):
            core.generate_changelog_document(Path("/tmp"), include_patch=False)
        # v0.0.5 is not a minor release; only v0.1.0 and v0.2.0 produce sections
        self.assertEqual(calls, ["v0.1.0", "v0.1.0..v0.2.0"])

    def test_generate_document_empty_without_minor_releases(self):
        # All tags are pre-0.1.0; without --include-patch the body is empty
        tags = [core.TagInfo(name="v0.0.5", iso_date="2024-01-01", object_name="a")]

        with mock.patch.object(core, "list_tags_sorted_by_date", return_value=tags), mock.patch.object(
            core, "_canonical_origin_base", return_value=None
        ), mock.patch.object(
            core, "generate_section_for_range", return_value="sec"
        ) as generate_section, mock.patch.object(core, "build_history_section", return_value=None):
            document = core.generate_changelog_document(Path("/tmp"), include_patch=False)
        generate_section.assert_not_called()
        self.assertNotIn("sec", document)

    def test_generate_document_includes_patch_when_no_minor(self):
        # All tags are pre-0.1.0; with --include-patch the latest patch appears
        tags = [
            core.TagInfo(name="v0.0.5", iso_date="2024-01-01", object_name="a"),
            core.TagInfo(name="v0.0.9", iso_date="2024-02-01", object_name="b"),
        ]
        calls = []

        def record_range(_root, _title, _date, rev_range, expected_version=None):
            calls.append(rev_range)
            return "sec"

        with mock.patch.object(core, "list_tags_sorted_by_date", return_value=tags), mock.patch.object(
            core, "_canonical_origin_base", return_value=None
        ), mock.patch.object(
            core, "generate_section_for_range", side_effect=record_range
        ), mock.patch.object(core, "build_history_section", return_value=None):
            document = core.generate_changelog_document(Path("/tmp"), include_patch=True)
        # Only v0.0.9 (latest patch) appears; range is the tag itself (from beginning)
        self.assertEqual(calls, ["v0.0.9"])
        self.assertIn("sec", document)

    def test_generate_document_includes_patch_after_minor(self):
        # With --include-patch the latest patch after the last minor is prepended
        tags = [
            core.TagInfo(name="v0.1.0", iso_date="2024-01-01", object_name="a"),
            core.TagInfo(name="v0.1.1", iso_date="2024-02-01", object_name="b"),
            core.TagInfo(name="v0.1.2", iso_date="2024-03-01", object_name="c"),
        ]
        calls = []

        def record_range(_root, _title, _date, rev_range, expected_version=None):
            calls.append(rev_range)
            return f"sec-{rev_range}"

        with mock.patch.object(core, "list_tags_sorted_by_date", return_value=tags), mock.patch.object(
            core, "_canonical_origin_base", return_value=None
        ), mock.patch.object(
            core, "generate_section_for_range", side_effect=record_range
        ), mock.patch.object(core, "build_history_section", return_value=None):
            document = core.generate_changelog_document(Path("/tmp"), include_patch=True)
        # v0.1.2 is the latest patch after last minor v0.1.0; v0.1.1 is not the latest
        self.assertIn("v0.1.0..v0.1.2", calls)
        # v0.1.0 minor section also present (from beginning)
        self.assertIn("v0.1.0", calls)
        # v0.1.2 patch section appears first in document (newest); split by newline to avoid substring overlap
        sections = [line for line in document.splitlines() if line.startswith("sec-")]
        self.assertEqual(sections[0], "sec-v0.1.0..v0.1.2", "patch section must be first")
        self.assertIn("sec-v0.1.0", sections, "minor section must also appear")

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
            core.generate_changelog_document(repo_root, include_patch=False)
        build_history.assert_called_once_with(repo_root, history_tags, False, include_unreleased_link=False)

    def test_history_includes_release_list(self):
        repo_root = Path("/tmp")
        tags = [
            core.TagInfo(name="v0.1.0", iso_date="2024-03-01", object_name="c"),
            core.TagInfo(name="v0.1.1", iso_date="2024-04-01", object_name="d"),
        ]
        with mock.patch.object(core, "_canonical_origin_base", return_value="https://github.com/Ogekuri/G"):
            history = core.build_history_section(repo_root, tags, include_unreleased=False)
        self.assertIsNotNone(history)
        lines = history.splitlines()
        self.assertEqual(lines[0], "# History")
        self.assertIn("- \\[0.1.0\\]: https://github.com/Ogekuri/G/releases/tag/v0.1.0", lines)
        self.assertIn("- \\[0.1.1\\]: https://github.com/Ogekuri/G/releases/tag/v0.1.1", lines)

    def test_history_omits_unreleased_link_without_section(self):
        repo_root = Path("/tmp")
        tags = [core.TagInfo(name="v0.1.0", iso_date="2024-03-01", object_name="c")]
        with mock.patch.object(core, "_canonical_origin_base", return_value="https://github.com/Ogekuri/G"):
            history = core.build_history_section(repo_root, tags, include_unreleased=True, include_unreleased_link=False)
        self.assertNotIn("[unreleased]:", history)

    def test_history_includes_unreleased_link_when_requested(self):
        repo_root = Path("/tmp")
        tags = [core.TagInfo(name="v0.1.0", iso_date="2024-03-01", object_name="c")]
        with mock.patch.object(core, "_canonical_origin_base", return_value="https://github.com/Ogekuri/G"):
            history = core.build_history_section(repo_root, tags, include_unreleased=True, include_unreleased_link=True)
        self.assertIn("[unreleased]: https://github.com/Ogekuri/G/compare/v0.1.0..HEAD", history)

    def test_history_includes_draft_releases_by_default(self):
        repo_root = Path("/tmp")
        tags = [
            core.TagInfo(name="v0.0.9", iso_date="2024-02-01", object_name="b"),
            core.TagInfo(name="v0.1.0", iso_date="2024-03-01", object_name="c"),
        ]
        with mock.patch.object(core, "_canonical_origin_base", return_value="https://github.com/Ogekuri/G"):
            history = core.build_history_section(repo_root, tags, include_unreleased=False)
        lines = history.splitlines()
        self.assertIn("- \\[0.0.9\\]: https://github.com/Ogekuri/G/releases/tag/v0.0.9", lines)
        self.assertIn("- \\[0.1.0\\]: https://github.com/Ogekuri/G/releases/tag/v0.1.0", lines)

    def test_categorize_commit_maps_implement_type(self):
        section, line = core.categorize_commit("implement(core): Add implementation command")
        self.assertEqual(section, "Implementations")
        self.assertEqual(line, "- Add implementation command *(core)*")

    def test_generate_section_renders_implementations_header_with_icon(self):
        with mock.patch.object(
            core,
            "git_log_subjects",
            return_value=["implement(core): Build command pipeline"],
        ):
            section = core.generate_section_for_range(Path("/tmp"), "v1.2.3", "2026-02-18", "v1.2.2..v1.2.3")
        self.assertIsNotNone(section)
        self.assertIn("### 🏗️  Implementations", section)

    def test_extract_release_version_accepts_new_release_marker(self):
        self.assertEqual(core._extract_release_version("release: Release version 1.2.3"), "1.2.3")

    def test_extract_release_version_keeps_legacy_release_marker(self):
        self.assertEqual(core._extract_release_version("release version: 1.2.3"), "1.2.3")

    def test_generate_section_ignores_release_marker_commits(self):
        with mock.patch.object(
            core,
            "git_log_subjects",
            return_value=["release: Release version 1.2.3"],
        ):
            section = core.generate_section_for_range(Path("/tmp"), "v1.2.3", "2026-02-18", "v1.2.2..v1.2.3")
        self.assertIsNone(section)


class MinorReleaseTagPredicateTest(unittest.TestCase):
    def test_minor_release_tags(self):
        for tag in ("v0.1.0", "0.1.0", "v0.2.0", "v1.0.0", "v1.1.0", "v2.3.0"):
            with self.subTest(tag=tag):
                self.assertTrue(core._is_minor_release_tag(tag), f"{tag} should be minor")

    def test_non_minor_release_tags(self):
        for tag in ("v0.0.1", "v0.0.42", "v0.1.1", "v1.0.1", "v1.2.3", "notasemver"):
            with self.subTest(tag=tag):
                self.assertFalse(core._is_minor_release_tag(tag), f"{tag} should not be minor")


class LatestPatchTagAfterTest(unittest.TestCase):
    def _make(self, name, date="2024-01-01"):
        return core.TagInfo(name=name, iso_date=date, object_name="x")

    def test_returns_latest_patch_after_last_minor(self):
        tags = [
            self._make("v0.1.0", "2024-01-01"),
            self._make("v0.1.1", "2024-02-01"),
            self._make("v0.1.2", "2024-03-01"),
        ]
        last_minor = tags[0]
        result = core._latest_patch_tag_after(tags, last_minor)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "v0.1.2")

    def test_returns_none_when_no_patch_after_minor(self):
        tags = [
            self._make("v0.1.0", "2024-01-01"),
            self._make("v0.2.0", "2024-02-01"),
        ]
        last_minor = tags[1]
        self.assertIsNone(core._latest_patch_tag_after(tags, last_minor))

    def test_returns_latest_patch_when_no_minor(self):
        tags = [
            self._make("v0.0.1", "2024-01-01"),
            self._make("v0.0.9", "2024-02-01"),
            self._make("v0.0.42", "2024-03-01"),
        ]
        result = core._latest_patch_tag_after(tags, None)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "v0.0.42")

    def test_returns_none_when_all_tags_empty(self):
        self.assertIsNone(core._latest_patch_tag_after([], None))
