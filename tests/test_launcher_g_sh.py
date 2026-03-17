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
            env["PATH"] = f"{fake_bin}:{env.get('PATH', '')}"
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
            self.assertEqual(
                capture_path.read_text(encoding="utf-8").splitlines(),
                [
                    "run",
                    "--project",
                    str(self.REPO_ROOT),
                    "python",
                    "-m",
                    "git_alias",
                    "st",
                    "--help",
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
