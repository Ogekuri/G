import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class CmdLtTest(unittest.TestCase):
    def test_cmd_lt_prints_tag_with_containing_branches(self):
        with mock.patch.object(
            core,
            "capture_git_output",
            side_effect=[
                "v0.0.4",
                "* work\n  master\n  remotes/origin/master\n  remotes/origin/HEAD -> origin/master",
            ],
        ) as capture:
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                core.cmd_lt([])
        self.assertEqual(stdout.getvalue().strip(), "v0.0.4: work, master, origin/master")
        capture.assert_has_calls(
            [
                mock.call(["tag", "-l"]),
                mock.call(["branch", "-a", "--contains", "v0.0.4"]),
            ]
        )

    def test_cmd_lt_prints_multiple_tags(self):
        with mock.patch.object(
            core,
            "capture_git_output",
            side_effect=[
                "v0.0.40\nv0.0.41",
                "* work",
                "  work\n  develop\n  remotes/origin/develop",
            ],
        ):
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                core.cmd_lt([])
        self.assertEqual(
            stdout.getvalue().strip().splitlines(),
            ["v0.0.40: work", "v0.0.41: work, develop, origin/develop"],
        )

    def test_cmd_lt_forwards_extra_filters_to_tag_list(self):
        with mock.patch.object(core, "capture_git_output", return_value="") as capture:
            stdout = io.StringIO()
            with contextlib.redirect_stdout(stdout):
                core.cmd_lt(["v1.*"])
        self.assertEqual(stdout.getvalue(), "")
        capture.assert_called_once_with(["tag", "-l", "v1.*"])


if __name__ == "__main__":
    unittest.main()
