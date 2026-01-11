import contextlib
import io
import json
import unittest
from unittest import mock

from git_alias import core


class _FakeResponse:
    def __init__(self, payload: dict):
        self._payload = payload

    def read(self):
        return json.dumps(self._payload).encode("utf-8")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False


class UpdateCheckTest(unittest.TestCase):
    def test_check_silently_ignores_network_errors(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            with mock.patch.object(core, "urlopen", side_effect=OSError("network down")):
                core.check_for_newer_version(timeout_seconds=0.01)
        self.assertEqual(err.getvalue(), "")

    def test_check_warns_when_newer_version_available(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            with mock.patch.object(core, "get_cli_version", return_value="0.0.1"):
                with mock.patch.object(core, "urlopen", return_value=_FakeResponse({"tag_name": "v0.0.2"})):
                    core.check_for_newer_version(timeout_seconds=0.01)
        text = err.getvalue()
        self.assertIn("New version available", text)
        self.assertIn("current: 0.0.1", text)
        self.assertIn("latest: 0.0.2", text)
        self.assertIn("--upgrade", text)

    def test_check_does_not_warn_when_latest_is_not_newer(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            with mock.patch.object(core, "get_cli_version", return_value="0.0.2"):
                with mock.patch.object(core, "urlopen", return_value=_FakeResponse({"tag_name": "v0.0.2"})):
                    core.check_for_newer_version(timeout_seconds=0.01)
        self.assertEqual(err.getvalue(), "")
