import contextlib
import io
import unittest
from unittest import mock

from git_alias import core


class BackupCommandTest(unittest.TestCase):
    def setUp(self):
        core.CONFIG.update(core.DEFAULT_CONFIG)

    def test_execute_backup_flow_runs_expected_steps_in_order(self):
        steps = []

        def record_step(level, step_name, action):
            steps.append((level, step_name))
            return None

        with mock.patch.object(
            core,
            "_ensure_release_prerequisites",
            return_value={"master": "master", "develop": "develop", "work": "work"},
        ), mock.patch.object(core, "_run_release_step", side_effect=record_step):
            buffer = io.StringIO()
            with contextlib.redirect_stdout(buffer):
                core._execute_backup_flow()

        self.assertEqual([level for level, _step_name in steps], ["backup"] * 4)
        self.assertEqual(
            [step_name for _level, step_name in steps],
            ["checkout develop", "merge work into develop", "push develop", "return to work"],
        )
        self.assertIn("Backup completed successfully", buffer.getvalue())

    def test_cmd_backup_delegates_to_backup_runner(self):
        with mock.patch.object(core, "_run_backup_command") as run_backup:
            core.cmd_backup([])
        run_backup.assert_called_once_with()

    def test_cmd_backup_accepts_help_flag(self):
        with mock.patch.object(core, "print_command_help") as print_help, mock.patch.object(
            core, "_run_backup_command"
        ) as run_backup:
            core.cmd_backup(["--help"])
        print_help.assert_called_once_with("backup")
        run_backup.assert_not_called()

    def test_cmd_backup_rejects_positional_arguments(self):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            with self.assertRaises(SystemExit):
                core.cmd_backup(["unexpected"])
        self.assertIn("git backup does not accept positional arguments", err.getvalue())

