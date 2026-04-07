## @file test_launcher_g_sh.py
# @brief Unit tests for `scripts/g.sh` launcher behavior.

import os
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path


## @brief Test suite for Bash launcher delegation to Astral uv.
# @details Validates launcher runtime delegation and absence of legacy
#          virtualenv bootstrap mechanics.
# @satisfies CTN-002 CPT-005
class LauncherGShTest(unittest.TestCase):
    ## @brief Repository root path for launcher tests.
    REPO_ROOT = Path(__file__).resolve().parents[1]
    ## @brief Absolute path of launcher script under test.
    SCRIPT_PATH = REPO_ROOT / "scripts" / "g.sh"

    ## @brief Write executable shell helper file.
    # @param path {Path} Destination executable path.
    # @param content {str} Script body text encoded as UTF-8.
    # @return None.
    @staticmethod
    def _write_executable(path: Path, content: str) -> None:
        path.write_text(content, encoding="utf-8")
        path.chmod(path.stat().st_mode | stat.S_IXUSR)

    ## @brief Normalize Windows-style drive and separator formatting for asserts.
    # @details Converts backslashes to forward slashes and lowercases only the
    #          drive letter prefix when present so launcher assertions remain
    #          stable across PowerShell and Git Bash path renderings.
    # @param path_text {str} Path text captured from launcher subprocess output.
    # @return {str} Normalized path text.
    @staticmethod
    def _normalize_launcher_path_text(path_text: str) -> str:
        normalized = path_text.replace("\\", "/")
        if len(normalized) >= 3 and normalized[1:3] == ":/":
            return normalized[0].lower() + normalized[1:]
        return normalized

    ## @brief Build Git Bash compatible PATH string for fake executables.
    # @param fake_bin {Path} Directory containing fake command shims.
    # @param inherited_path {str} Existing PATH environment value.
    # @return {str} PATH value with fake_bin prepended using POSIX separators.
    @staticmethod
    def _prepend_fake_bin_to_path(fake_bin: Path, inherited_path: str) -> str:
        return f"{fake_bin.as_posix()}:{inherited_path}"

    ## @brief Verify launcher delegates execution to `uv run` with forwarded args.
    # @details Replaces `uv` in PATH with deterministic fake executable that
    #          captures argv payload and exits successfully.
    # @return None.
    # @satisfies CTN-002 CPT-005
    def test_g_sh_executes_uv_run_python_module_with_forwarded_args(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            temp_root = Path(tmp_dir)
            fake_bin = temp_root / "bin"
            fake_bin.mkdir()
            capture_path = temp_root / "uv-args.txt"
            fake_uv = fake_bin / "uv"
            self._write_executable(
                fake_uv,
                "#!/bin/sh\n"
                "printf '%s\\n' \"$@\" > \"$UV_CAPTURE_FILE\"\n"
                "exit 0\n",
            )

            env = os.environ.copy()
            env["PATH"] = self._prepend_fake_bin_to_path(
                fake_bin, env.get("PATH", "")
            )
            env["UV_CAPTURE_FILE"] = str(capture_path)

            completed = subprocess.run(
                ["bash", str(self.SCRIPT_PATH), "st", "--help"],
                cwd=str(self.REPO_ROOT),
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            self.assertTrue(capture_path.exists())
            captured_args = capture_path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(
                captured_args[:2],
                [
                    "run",
                    "--project",
                ],
            )
            self.assertEqual(
                self._normalize_launcher_path_text(captured_args[2]),
                self._normalize_launcher_path_text(str(self.REPO_ROOT)),
            )
            self.assertEqual(
                captured_args[3:],
                [
                    "python",
                    "-m",
                    "git_alias",
                    "st",
                    "--help",
                ],
            )

    ## @brief Verify launcher accepts equivalent Git Bash Windows paths.
    # @details Executes the launcher through a lowercase-drive path on Windows
    #          so Git Bash path resolution is exercised against the real
    #          repository root returned by `git rev-parse --show-toplevel`.
    # @return None.
    # @satisfies CTN-002
    def test_g_sh_accepts_windows_drive_letter_case_mismatch(self):
        script_path_text = self.SCRIPT_PATH.as_posix()
        if len(script_path_text) < 3 or script_path_text[1:3] != ":/":
            self.skipTest("Windows drive-letter semantics are not available.")

        lowercase_script_path = script_path_text[0].lower() + script_path_text[1:]

        with tempfile.TemporaryDirectory() as tmp_dir:
            temp_root = Path(tmp_dir)
            fake_bin = temp_root / "bin"
            fake_bin.mkdir()
            capture_path = temp_root / "uv-args.txt"
            self._write_executable(
                fake_bin / "uv",
                "#!/bin/sh\n"
                "printf '%s\\n' \"$@\" > \"$UV_CAPTURE_FILE\"\n"
                "exit 0\n",
            )

            env = os.environ.copy()
            env["PATH"] = self._prepend_fake_bin_to_path(
                fake_bin, env.get("PATH", "")
            )
            env["UV_CAPTURE_FILE"] = str(capture_path)

            completed = subprocess.run(
                ["bash", lowercase_script_path, "st"],
                cwd=str(self.REPO_ROOT),
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(completed.returncode, 0, msg=completed.stderr)
            self.assertFalse(
                "Launcher base directory mismatch with git root."
                in completed.stdout,
                msg=completed.stdout,
            )
            captured_args = capture_path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(
                captured_args[:2],
                [
                    "run",
                    "--project",
                ],
            )
            self.assertEqual(
                self._normalize_launcher_path_text(captured_args[2]),
                self._normalize_launcher_path_text(str(self.REPO_ROOT)),
            )
            self.assertEqual(
                captured_args[3:],
                [
                    "python",
                    "-m",
                    "git_alias",
                    "st",
                ],
            )

    ## @brief Verify launcher source removes legacy virtualenv bootstrap commands.
    # @return None.
    # @satisfies CTN-002
    def test_g_sh_source_has_no_virtualenv_bootstrap_commands(self):
        source = self.SCRIPT_PATH.read_text(encoding="utf-8")
        self.assertNotIn("virtualenv --python", source)
        self.assertNotIn("pip install -r", source)
        self.assertNotIn("source \"${VENVDIR}/bin/activate\"", source)


if __name__ == "__main__":
    unittest.main()
