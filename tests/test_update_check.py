import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from uuid import uuid4
from unittest import mock
from urllib.error import HTTPError

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
    def _isolated_cache(self):
        return mock.patch.object(
            core,
            "VERSION_CHECK_CACHE_FILE",
            Path(tempfile.gettempdir())
            / f".github_api_idle-time.{core.UV_TOOL_NAME}.test.{uuid4().hex}",
        )

    def test_check_prints_red_error_on_network_failure(self):
        err = io.StringIO()
        with self._isolated_cache():
            with contextlib.redirect_stderr(err):
                with mock.patch.object(core, "_resolve_release_api_url", return_value="https://api.github.com/repos/acme/tool/releases/latest"):
                    with mock.patch.object(core, "urlopen", side_effect=OSError("network down")):
                        core.check_for_newer_version(timeout_seconds=0.01)
        self.assertIn("\033[31;1m", err.getvalue())
        self.assertIn("Version check failed: network down", err.getvalue())

    def test_check_warns_when_newer_version_available(self):
        err = io.StringIO()
        with self._isolated_cache():
            with contextlib.redirect_stderr(err):
                with mock.patch.object(core, "get_cli_version", return_value="0.0.1"):
                    with mock.patch.object(core, "_resolve_release_api_url", return_value="https://api.github.com/repos/acme/tool/releases/latest"):
                        with mock.patch.object(core, "urlopen", return_value=_FakeResponse({"tag_name": "v0.0.2"})):
                            core.check_for_newer_version(timeout_seconds=0.01)
        text = err.getvalue()
        self.assertIn("\033[92;1m", text)
        self.assertIn("Update available: 0.0.2 (installed: 0.0.1)", text)
        self.assertIn("\033[0m", text)

    def test_check_does_not_warn_when_latest_is_not_newer(self):
        err = io.StringIO()
        with self._isolated_cache():
            with contextlib.redirect_stderr(err):
                with mock.patch.object(core, "get_cli_version", return_value="0.0.2"):
                    with mock.patch.object(core, "_resolve_release_api_url", return_value="https://api.github.com/repos/acme/tool/releases/latest"):
                        with mock.patch.object(core, "urlopen", return_value=_FakeResponse({"tag_name": "v0.0.2"})):
                            core.check_for_newer_version(timeout_seconds=0.01)
        self.assertEqual(err.getvalue(), "")

    def test_check_skips_network_when_idle_time_is_not_expired(self):
        with self._isolated_cache():
            cache_data = {
                "last_check_unix": 1,
                "last_check_human": "1970-01-01 00:00:01",
                "idle_until_unix": 4_000_000_000,
                "idle_until_human": "2096-10-02 07:06:40",
            }
            core.VERSION_CHECK_CACHE_FILE.write_text(
                json.dumps(cache_data),
                encoding="utf-8",
            )
            with mock.patch.object(core, "_resolve_release_api_url", return_value="https://api.github.com/repos/acme/tool/releases/latest"):
                with mock.patch.object(core, "urlopen") as urlopen_mock:
                    core.check_for_newer_version(timeout_seconds=0.01)
            urlopen_mock.assert_not_called()

    def test_check_writes_idle_time_state_on_success(self):
        with self._isolated_cache():
            with mock.patch.object(core, "_resolve_release_api_url", return_value="https://api.github.com/repos/acme/tool/releases/latest"):
                with mock.patch.object(core, "urlopen", return_value=_FakeResponse({"tag_name": "v0.0.2"})):
                    core.check_for_newer_version(timeout_seconds=0.01)
            data = json.loads(core.VERSION_CHECK_CACHE_FILE.read_text(encoding="utf-8"))
        self.assertEqual(
            sorted(data.keys()),
            [
                "idle_until_human",
                "idle_until_unix",
                "last_check_human",
                "last_check_unix",
            ],
        )
        self.assertIsInstance(data["last_check_unix"], int)
        self.assertIsInstance(data["idle_until_unix"], int)
        self.assertGreater(data["idle_until_unix"], data["last_check_unix"])

    def test_check_prints_http_403_rate_limit_error_details(self):
        err = io.StringIO()
        rate_limit_error = HTTPError(
            url="https://api.github.com/repos/acme/tool/releases/latest",
            code=403,
            msg="Forbidden",
            hdrs=None,
            fp=io.BytesIO(b'{"message":"rate limit exceeded"}'),
        )
        with self._isolated_cache():
            with contextlib.redirect_stderr(err):
                with mock.patch.object(core, "_resolve_release_api_url", return_value="https://api.github.com/repos/acme/tool/releases/latest"):
                    with mock.patch.object(core, "urlopen", side_effect=rate_limit_error):
                        core.check_for_newer_version(timeout_seconds=0.01)
        text = err.getvalue()
        self.assertIn("\033[31;1m", text)
        self.assertIn("Version check failed: HTTP 403: rate limit exceeded", text)

    def test_resolve_release_api_url_from_active_remote(self):
        with mock.patch.object(
            core,
            "run_git_text",
            side_effect=["work", "origin", "git@github.com:Acme/Tool.git"],
        ):
            api_url = core._resolve_release_api_url(Path("/repo"))
        self.assertEqual(
            api_url,
            "https://api.github.com/repos/Acme/Tool/releases/latest",
        )

    def test_resolve_release_api_url_from_ssh_scheme_remote(self):
        with mock.patch.object(
            core,
            "run_git_text",
            side_effect=["work", "origin", "ssh://git@github.com/Acme/Tool.git"],
        ):
            api_url = core._resolve_release_api_url(Path("/repo"))
        self.assertEqual(
            api_url,
            "https://api.github.com/repos/Acme/Tool/releases/latest",
        )

    def test_upgrade_self_uses_uv_tool_install_program_name(self):
        with mock.patch.object(core, "_resolve_github_owner_repo", return_value=("Acme", "Tool")):
            with mock.patch.object(core, "_run_checked") as run_checked:
                core.upgrade_self(Path("/repo"))
        run_checked.assert_called_once_with(
            [
                "uv",
                "tool",
                "install",
                core.UV_TOOL_NAME,
                "--force",
                "--from",
                "git+https://github.com/Acme/Tool.git",
            ]
        )

    def test_uninstall_self_uses_uv_tool_uninstall(self):
        with mock.patch.object(core, "_run_checked") as run_checked:
            core.uninstall_self()
        run_checked.assert_called_once_with(
            ["uv", "tool", "uninstall", core.UV_TOOL_NAME]
        )
