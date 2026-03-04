# Files Structure
```
.
└── src
    └── git_alias
        ├── __init__.py
        ├── __main__.py
        ├── core.py
        └── foresta.py
```

# __init__.py | Python | 13L | 0 symbols | 1 imports | 7 comments
> Path: `src/git_alias/__init__.py`

## Imports
```
from .core import main  # noqa: F401
```


---

# __main__.py | Python | 11L | 0 symbols | 2 imports | 5 comments
> Path: `src/git_alias/__main__.py`

## Imports
```
from .core import main
import sys
```


---

# core.py | Python | 4248L | 233 symbols | 18 imports | 1028 comments
> Path: `src/git_alias/core.py`

## Imports
```
import argparse
import importlib
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from git_alias import foresta
```

## Definitions

- var `CONFIG_FILENAME = ".g.conf"` (L28)
- @brief Constant `CONFIG_FILENAME` used by CLI runtime paths and policies.
- var `GLOBAL_CONFIG_DIRECTORY = ".g"` (L30)
- @brief Constant `GLOBAL_CONFIG_DIRECTORY` used by CLI runtime paths and policies.
- var `GLOBAL_CONFIG_FILENAME = "g.conf"` (L32)
- @brief Constant `GLOBAL_CONFIG_FILENAME` used by CLI runtime paths and policies.
- var `GITHUB_LATEST_RELEASE_API = "https://api.github.com/repos/Ogekuri/G/releases/latest"` (L36)
- @brief Constant `GITHUB_LATEST_RELEASE_API` used by CLI runtime paths and policies.
- var `VERSION_CHECK_CACHE_FILE = Path(tempfile.gettempdir()) / ".g_version_check_cache.json"` (L39)
- @brief Constant `VERSION_CHECK_CACHE_FILE` used by CLI runtime paths and policies.
- var `VERSION_CHECK_TTL_HOURS = 6` (L42)
- @brief Constant `VERSION_CHECK_TTL_HOURS` used by CLI runtime paths and policies.
- var `DEFAULT_VER_RULES = [` (L46)
- @brief Constant `DEFAULT_VER_RULES` used by CLI runtime paths and policies.
- var `VERSION_CLEANUP_REGEXES = [` (L53)
- @brief Constant `VERSION_CLEANUP_REGEXES` used by CLI runtime paths and policies.
- var `VERSION_CLEANUP_PATTERNS = [re.compile(pattern) for pattern in VERSION_CLEANUP_REGEXES]` (L64)
- @brief Constant `VERSION_CLEANUP_PATTERNS` used by CLI runtime paths and policies.
- var `ANSI_ESCAPE_RE = re.compile(r"\x1b\[[0-9;]*m")` (L65)
- var `DEFAULT_GP_COMMAND = "gitk --all"` (L69)
- @brief Constant `DEFAULT_CONFIG` used by CLI runtime paths and policies.
- @brief Constant `DEFAULT_GP_COMMAND` used by CLI runtime paths and policies.
- var `DEFAULT_GR_COMMAND = "gitk --simplify-by-decoration --all"` (L71)
- @brief Constant `DEFAULT_GR_COMMAND` used by CLI runtime paths and policies.
- var `DEFAULT_CONFIG = {` (L73)
- var `CONFIG = DEFAULT_CONFIG.copy()` (L93)
- @brief Constant `CONFIG` used by CLI runtime paths and policies.
- var `BRANCH_KEYS = ("master", "develop", "work")` (L96)
- @brief Constant `BRANCH_KEYS` used by CLI runtime paths and policies.
- var `LOCAL_CONFIG_KEYS = ("master", "develop", "work", "default_commit_module", "ver_rules")` (L98)
- @brief Constant `LOCAL_CONFIG_KEYS` used by CLI runtime paths and policies.
- var `GLOBAL_CONFIG_KEYS = ("edit_command", "gp_command", "gr_command")` (L100)
- @brief Constant `GLOBAL_CONFIG_KEYS` used by CLI runtime paths and policies.
- var `MANAGEMENT_HELP = [` (L103)
- @brief Constant `MANAGEMENT_HELP` used by CLI runtime paths and policies.
### fn `def get_config_value(name)` (L120-123)
- @brief Execute `get_config_value` runtime logic for Git-Alias CLI.
- @details Executes `get_config_value` using deterministic CLI control-flow and explicit error propagation.
- @param name Input parameter consumed by `get_config_value`.
- @return Result emitted by `get_config_value` according to command contract.

### fn `def get_branch(name)` (L128-133)
- @brief Execute `get_branch` runtime logic for Git-Alias CLI.
- @details Executes `get_branch` using deterministic CLI control-flow and explicit error propagation.
- @param name Input parameter consumed by `get_branch`.
- @return Result emitted by `get_branch` according to command contract.

### fn `def get_editor()` (L137-140)
- @brief Execute `get_editor` runtime logic for Git-Alias CLI.
- @details Executes `get_editor` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `get_editor` according to command contract.

### fn `def _load_config_rules(key, fallback)` `priv` (L146-171)
- @brief Execute `_load_config_rules` runtime logic for Git-Alias CLI.
- @details Executes `_load_config_rules` using deterministic CLI control-flow and explicit error propagation.
- @param key Input parameter consumed by `_load_config_rules`.
- @param fallback Input parameter consumed by `_load_config_rules`.
- @return Result emitted by `_load_config_rules` according to command contract.

### fn `def get_version_rules()` (L175-178)
- @brief Execute `get_version_rules` runtime logic for Git-Alias CLI.
- @details Executes `get_version_rules` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `get_version_rules` according to command contract.

### fn `def get_cli_version()` (L182-193)
- @brief Execute `get_cli_version` runtime logic for Git-Alias CLI.
- @details Executes `get_cli_version` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `get_cli_version` according to command contract.

### fn `def _normalize_semver_text(text: str) -> str` `priv` (L198-204)
- @brief Execute `_normalize_semver_text` runtime logic for Git-Alias CLI.
- @details Executes `_normalize_semver_text` using deterministic CLI control-flow and explicit error propagation.
- @param text Input parameter consumed by `_normalize_semver_text`.
- @return Result emitted by `_normalize_semver_text` according to command contract.

### fn `def check_for_newer_version(timeout_seconds: float = 1.0) -> None` (L209-299)
- @brief Execute `check_for_newer_version` runtime logic for Git-Alias CLI.
- @details Executes `check_for_newer_version` using deterministic CLI control-flow and explicit error propagation.
- @param timeout_seconds Input parameter consumed by `check_for_newer_version`.
- @return Result emitted by `check_for_newer_version` according to command contract.

### fn `def get_git_root()` (L303-318)
- @brief Execute `get_git_root` runtime logic for Git-Alias CLI.
- @details Executes `get_git_root` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `get_git_root` according to command contract.

### fn `def get_config_path(root=None)` (L323-327)
- @brief Execute `get_config_path` runtime logic for Git-Alias CLI.
- @details Executes `get_config_path` using deterministic CLI control-flow and explicit error propagation.
- @param root Input parameter consumed by `get_config_path`.
- @return Result emitted by `get_config_path` according to command contract.

### fn `def get_global_config_path(home=None)` (L332-336)
- @brief Execute `get_global_config_path` runtime logic for Git-Alias CLI.
- @details Executes `get_global_config_path` using deterministic CLI control-flow and explicit error propagation.
- @param home Input parameter consumed by `get_global_config_path`.
- @return Result emitted by `get_global_config_path` according to command contract.

### fn `def _read_config_object(config_path)` `priv` (L341-359)
- @brief Execute `_read_config_object` runtime logic for Git-Alias CLI.
- @details Executes `_read_config_object` using deterministic CLI control-flow and explicit error propagation.
- @param config_path Input parameter consumed by `_read_config_object`.
- @return Result emitted by `_read_config_object` according to command contract.

### fn `def _apply_config_values(data, keys)` `priv` (L365-387)
- @brief Execute `_apply_config_values` runtime logic for Git-Alias CLI.
- @details Executes `_apply_config_values` using deterministic CLI control-flow and explicit error propagation.
- @param data Input parameter consumed by `_apply_config_values`.
- @param keys Input parameter consumed by `_apply_config_values`.
- @return Result emitted by `_apply_config_values` according to command contract.

### fn `def load_cli_config(root=None, home=None)` (L393-405)
- @brief Execute `load_cli_config` runtime logic for Git-Alias CLI.
- @details Executes `load_cli_config` using deterministic CLI control-flow and explicit error propagation.
- @param root Input parameter consumed by `load_cli_config`.
- @param home Input parameter consumed by `load_cli_config`.
- @return Result emitted by `load_cli_config` according to command contract.

### fn `def _write_missing_config_values(config_path, keys, create_parent=False)` `priv` (L412-469)
- @brief Execute `_write_missing_config_values` runtime logic for Git-Alias CLI.
- @details Executes `_write_missing_config_values` using deterministic CLI control-flow and explicit error propagation.
- @param config_path Input parameter consumed by `_write_missing_config_values`.
- @param keys Input parameter consumed by `_write_missing_config_values`.
- @param create_parent Input parameter consumed by `_write_missing_config_values`.
- @return Result emitted by `_write_missing_config_values` according to command contract.

### fn `def write_default_config(root=None, home=None)` (L475-488)
- @brief Execute `write_default_config` runtime logic for Git-Alias CLI.
- @details Executes `write_default_config` using deterministic CLI control-flow and explicit error propagation.
- @param root Input parameter consumed by `write_default_config`.
- @param home Input parameter consumed by `write_default_config`.
- @return Result emitted by `write_default_config` according to command contract.

### fn `def _editor_base_command()` `priv` (L492-506)
- @brief Execute `_editor_base_command` runtime logic for Git-Alias CLI.
- @details Executes `_editor_base_command` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `_editor_base_command` according to command contract.

### fn `def run_editor_command(args)` (L511-514)
- @brief Execute `run_editor_command` runtime logic for Git-Alias CLI.
- @details Executes `run_editor_command` using deterministic CLI control-flow and explicit error propagation.
- @param args Input parameter consumed by `run_editor_command`.
- @return Result emitted by `run_editor_command` according to command contract.

### fn `def _config_command_parts(key: str, default_command: str) -> List[str]` `priv` (L522-546)
- @brief Resolve command parts from config with executable-availability fallback.
- @details Parses a configured command line and verifies the configured executable
is available in PATH. Invalid or unavailable configured commands fall back to
the provided default command template.
- @param key Input parameter consumed by `_config_command_parts`.
- @param default_command Input parameter consumed by `_config_command_parts`.
- @return Result emitted by `_config_command_parts` according to command contract.

- var `HELP_TEXTS = {` (L549)
- @brief Constant `HELP_TEXTS` used by CLI runtime paths and policies.
- var `RESET_HELP_COMMANDS = {"rs", "rshrd", "rskep", "rsmix", "rsmrg", "rssft"}` (L714)
- @brief Constant `RESET_HELP_COMMANDS` used by CLI runtime paths and policies.
- var `LSI_DEFAULT_EXCLUDED_DIRS = frozenset(` (L720)
- @brief Default directory/file names excluded from `lsi` output.
- @details Immutable set of first-path-component names that `cmd_lsi` filters out
by default. Filtering is bypassed when `--include-all` is passed.
- @satisfies REQ-120
### fn `def _to_args(extra)` `priv` (L757-760)
- @brief Execute `_to_args` runtime logic for Git-Alias CLI.
- @details Executes `_to_args` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `_to_args`.
- @return Result emitted by `_to_args` according to command contract.

### class `class CommandExecutionError(RuntimeError)` : RuntimeError (L763-804)
- @brief Class `CommandExecutionError` models a typed runtime container/error boundary.
- @brief Execute `__init__` runtime logic for Git-Alias CLI.
- @details Captures subprocess execution metadata and exposes normalized human-readable failure text.
- @param self Input parameter consumed by `__init__`.
- @param exc Input parameter consumed by `__init__`.
- fn `def __init__(self, exc: subprocess.CalledProcessError)` `priv` (L768-775)
  - @brief Execute `__init__` runtime logic for Git-Alias CLI.
  - @param self Input parameter consumed by `__init__`.
  - @param exc Input parameter consumed by `__init__`.
  - @return Result emitted by `__init__` according to command contract.
- fn `def _format_message(self) -> str` `priv` (L779-789)
  - @brief Execute `_format_message` runtime logic for Git-Alias CLI.
  - @param self Input parameter consumed by `_format_message`.
  - @return Result emitted by `_format_message` according to command contract.
- fn `def _decode_stream(data) -> str` `priv` (L794-804)
  - @brief Execute `_decode_stream` runtime logic for Git-Alias CLI.
  - @param data Input parameter consumed by `_decode_stream`.
  - @return Result emitted by `_decode_stream` according to command contract.

### fn `def _run_checked(*popenargs, **kwargs)` `priv` (L810-817)
- @brief Execute `_run_checked` runtime logic for Git-Alias CLI.
- @details Executes `_run_checked` using deterministic CLI control-flow and explicit error propagation.
- @param *popenargs Input parameter consumed by `_run_checked`.
- @param **kwargs Input parameter consumed by `_run_checked`.
- @return Result emitted by `_run_checked` according to command contract.

### class `class VersionDetectionError(RuntimeError)` : RuntimeError (L820-823)
- @brief Class `VersionDetectionError` models a typed runtime container/error boundary.
- @details Represents deterministic failures encountered while resolving semantic versions from repository files.

### class `class ReleaseError(RuntimeError)` : RuntimeError (L826-829)
- @brief Class `ReleaseError` models a typed runtime container/error boundary.
- @details Represents release-flow precondition or orchestration failures.

### fn `def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)` (L837-841)
- @brief Execute `run_git_cmd` runtime logic for Git-Alias CLI.
- @details Executes `run_git_cmd` using deterministic CLI control-flow and explicit error propagation.
- @param base_args Input parameter consumed by `run_git_cmd`.
- @param extra Input parameter consumed by `run_git_cmd`.
- @param cwd Input parameter consumed by `run_git_cmd`.
- @param **kwargs Input parameter consumed by `run_git_cmd`.
- @return Result emitted by `run_git_cmd` according to command contract.

### fn `def capture_git_output(base_args, cwd=None)` (L847-853)
- @brief Execute `capture_git_output` runtime logic for Git-Alias CLI.
- @details Executes `capture_git_output` using deterministic CLI control-flow and explicit error propagation.
- @param base_args Input parameter consumed by `capture_git_output`.
- @param cwd Input parameter consumed by `capture_git_output`.
- @return Result emitted by `capture_git_output` according to command contract.

### fn `def run_command(cmd, cwd=None)` (L859-862)
- @brief Execute `run_command` runtime logic for Git-Alias CLI.
- @details Executes `run_command` using deterministic CLI control-flow and explicit error propagation.
- @param cmd Input parameter consumed by `run_command`.
- @param cwd Input parameter consumed by `run_command`.
- @return Result emitted by `run_command` according to command contract.

### fn `def run_git_text(args, cwd=None, check=True)` (L869-886)
- @brief Execute `run_git_text` runtime logic for Git-Alias CLI.
- @details Executes `run_git_text` using deterministic CLI control-flow and explicit error propagation.
- @param args Input parameter consumed by `run_git_text`.
- @param cwd Input parameter consumed by `run_git_text`.
- @param check Input parameter consumed by `run_git_text`.
- @return Result emitted by `run_git_text` according to command contract.

### fn `def run_shell(command, cwd=None)` (L892-895)
- @brief Execute `run_shell` runtime logic for Git-Alias CLI.
- @details Executes `run_shell` using deterministic CLI control-flow and explicit error propagation.
- @param command Input parameter consumed by `run_shell`.
- @param cwd Input parameter consumed by `run_shell`.
- @return Result emitted by `run_shell` according to command contract.

### fn `def _git_status_lines()` `priv` (L899-911)
- @brief Execute `_git_status_lines` runtime logic for Git-Alias CLI.
- @details Executes `_git_status_lines` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `_git_status_lines` according to command contract.

### fn `def has_unstaged_changes(status_lines=None)` (L916-927)
- @brief Execute `has_unstaged_changes` runtime logic for Git-Alias CLI.
- @details Executes `has_unstaged_changes` using deterministic CLI control-flow and explicit error propagation.
- @param status_lines Input parameter consumed by `has_unstaged_changes`.
- @return Result emitted by `has_unstaged_changes` according to command contract.

### fn `def has_staged_changes(status_lines=None)` (L932-941)
- @brief Execute `has_staged_changes` runtime logic for Git-Alias CLI.
- @details Executes `has_staged_changes` using deterministic CLI control-flow and explicit error propagation.
- @param status_lines Input parameter consumed by `has_staged_changes`.
- @return Result emitted by `has_staged_changes` according to command contract.

- var `WIP_MESSAGE_RE = re.compile(r"^wip: work in progress\.$")` (L947)
- @brief Constant `WIP_MESSAGE_RE` used by CLI runtime paths and policies.
### fn `def _refresh_remote_refs()` `priv` (L953-964)
- @brief Execute `_refresh_remote_refs` runtime logic for Git-Alias CLI.
- @details Executes `_refresh_remote_refs` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `_refresh_remote_refs` according to command contract.

### fn `def _branch_remote_divergence(branch_key, remote="origin")` `priv` (L970-990)
- @brief Execute `_branch_remote_divergence` runtime logic for Git-Alias CLI.
- @details Executes `_branch_remote_divergence` using deterministic CLI control-flow and explicit error propagation.
- @param branch_key Input parameter consumed by `_branch_remote_divergence`.
- @param remote Input parameter consumed by `_branch_remote_divergence`.
- @return Result emitted by `_branch_remote_divergence` according to command contract.

### fn `def has_remote_branch_updates(branch_key, remote="origin")` (L996-1000)
- @brief Execute `has_remote_branch_updates` runtime logic for Git-Alias CLI.
- @details Executes `has_remote_branch_updates` using deterministic CLI control-flow and explicit error propagation.
- @param branch_key Input parameter consumed by `has_remote_branch_updates`.
- @param remote Input parameter consumed by `has_remote_branch_updates`.
- @return Result emitted by `has_remote_branch_updates` according to command contract.

### fn `def has_remote_develop_updates()` (L1004-1007)
- @brief Execute `has_remote_develop_updates` runtime logic for Git-Alias CLI.
- @details Executes `has_remote_develop_updates` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `has_remote_develop_updates` according to command contract.

### fn `def has_remote_master_updates()` (L1011-1014)
- @brief Execute `has_remote_master_updates` runtime logic for Git-Alias CLI.
- @details Executes `has_remote_master_updates` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `has_remote_master_updates` according to command contract.

### fn `def _head_commit_message()` `priv` (L1018-1024)
- @brief Execute `_head_commit_message` runtime logic for Git-Alias CLI.
- @details Executes `_head_commit_message` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `_head_commit_message` according to command contract.

### fn `def _head_commit_hash()` `priv` (L1028-1034)
- @brief Execute `_head_commit_hash` runtime logic for Git-Alias CLI.
- @details Executes `_head_commit_hash` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `_head_commit_hash` according to command contract.

### fn `def _commit_exists_in_branch(commit_hash, branch_name)` `priv` (L1040-1052)
- @brief Execute `_commit_exists_in_branch` runtime logic for Git-Alias CLI.
- @details Executes `_commit_exists_in_branch` using deterministic CLI control-flow and explicit error propagation.
- @param commit_hash Input parameter consumed by `_commit_exists_in_branch`.
- @param branch_name Input parameter consumed by `_commit_exists_in_branch`.
- @return Result emitted by `_commit_exists_in_branch` according to command contract.

### fn `def _should_amend_existing_commit()` `priv` (L1056-1071)
- @brief Execute `_should_amend_existing_commit` runtime logic for Git-Alias CLI.
- @details Executes `_should_amend_existing_commit` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `_should_amend_existing_commit` according to command contract.

### fn `def is_inside_git_repo()` (L1075-1082)
- @brief Execute `is_inside_git_repo` runtime logic for Git-Alias CLI.
- @details Executes `is_inside_git_repo` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `is_inside_git_repo` according to command contract.

### class `class TagInfo` (L1087-1095)
- @brief Class `TagInfo` models a typed runtime container/error boundary.
- @brief Store raw tag name including `v` prefix when present.
- @brief Store ISO date string used for changelog section headers.
- @details Encapsulates tag identity, tag date, and resolved Git object identifier for changelog assembly.

- var `DELIM = "\x1f"` (L1098)
- @brief Constant `DELIM` used by CLI runtime paths and policies.
- var `RECORD = "\x1e"` (L1101)
- @brief Constant `RECORD` used by CLI runtime paths and policies.
- var `SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")` (L1117)
- @brief Constant `SEMVER_RE` used by CLI runtime paths and policies.
- var `SECTION_EMOJI = {` (L1120)
- @brief Constant `SECTION_EMOJI` used by CLI runtime paths and policies.
### fn `def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[int, int, int]]` `priv` (L1138-1141)
- @brief Execute `_tag_semver_tuple` runtime logic for Git-Alias CLI.
- @details Executes `_tag_semver_tuple` using deterministic CLI control-flow and explicit error propagation.
- @param tag_name Input parameter consumed by `_tag_semver_tuple`.
- @return Result emitted by `_tag_semver_tuple` according to command contract.

### fn `def _latest_supported_tag_name(tags: List[TagInfo]) -> Optional[str]` `priv` (L1146-1149)
- @brief Execute `_latest_supported_tag_name` runtime logic for Git-Alias CLI.
- @details Executes `_latest_supported_tag_name` using deterministic CLI control-flow and explicit error propagation.
- @param tags Input parameter consumed by `_latest_supported_tag_name`.
- @return Result emitted by `_latest_supported_tag_name` according to command contract.

### fn `def _is_minor_release_tag(tag_name: str) -> bool` `priv` (L1157-1164)
- @brief Predicate: tag is a minor release.
- @details Returns `True` when `tag_name` is a semver tag where `patch==0` AND `(major>=1 OR minor>=1)`,
i.e. version `>=0.1.0` with no patch component.
Patch releases (`patch>0`) and pre-0.1.0 tags (`0.0.x`) return `False`.
- @param tag_name Semver tag string, optionally prefixed with `v` (e.g. `v0.1.0`, `0.2.0`).
- @return `True` iff tag represents a minor release; `False` otherwise.
- @satisfies REQ-018, REQ-040

### fn `def _latest_patch_tag_after(` `priv` (L1173-1174)
- @brief Locate the chronologically latest patch tag after a given minor release.
- @details Scans `all_tags` (sorted chronologically, ascending) for tags that are NOT minor releases
and appear after `last_minor` in the list. When `last_minor` is `None`, scans all tags.
Returns the last qualifying `TagInfo` (most recent), or `None` if no patch exists.
- @param all_tags Full list of `TagInfo` sorted by date ascending (from `list_tags_sorted_by_date`).
- @param last_minor The last minor-release `TagInfo` to anchor the search; `None` means no minor exists.
- @return Most recent `TagInfo` that is not a minor release and appears after `last_minor`, or `None`.
- @satisfies REQ-040

### fn `def list_tags_sorted_by_date(` (L1192-1193)
- @brief Execute `list_tags_sorted_by_date` runtime logic for Git-Alias CLI.
- @details Executes `list_tags_sorted_by_date` using deterministic CLI control-flow and explicit error propagation.
- @param repo_root Input parameter consumed by `list_tags_sorted_by_date`.
- @param merged_ref Input parameter consumed by `list_tags_sorted_by_date`.
- @return Result emitted by `list_tags_sorted_by_date` according to command contract.

### fn `def git_log_subjects(repo_root: Path, rev_range: str) -> List[str]` (L1223-1234)
- @brief Execute `git_log_subjects` runtime logic for Git-Alias CLI.
- @details Executes `git_log_subjects` using deterministic CLI control-flow and explicit error propagation.
Reads full commit messages (subject + body) to preserve multiline conventional descriptions.
- @param repo_root Input parameter consumed by `git_log_subjects`.
- @param rev_range Input parameter consumed by `git_log_subjects`.
- @return Result emitted by `git_log_subjects` according to command contract.

### fn `def parse_conventional_commit(` (L1240-1241)
- @brief Execute `parse_conventional_commit` runtime logic for Git-Alias CLI.
- @details Parses a conventional-commit header with optional scope and optional breaking marker (`!`),
then returns extracted type/scope/breaking/description fields for changelog rendering.
- @param message Raw commit message text (subject and optional body).
- @return Tuple `(type, scope, breaking, description)` when message is parseable; otherwise `None`.

### fn `def _format_changelog_description(desc: str) -> List[str]` `priv` (L1261-1274)
- @brief Execute `_format_changelog_description` runtime logic for Git-Alias CLI.
- @details Normalizes a commit description for markdown list rendering while preserving logical lines.
Removes `Co-authored-by:` trailer lines, drops empty lines, and strips leading markdown-list
markers from continuation lines so multiline descriptions can be rendered as nested bullets.
- @param desc Parsed commit description.
- @return Ordered non-empty description lines ready for markdown rendering.

### fn `def categorize_commit(subject: str) -> Tuple[Optional[str], str]` (L1282-1311)
- @brief Execute `categorize_commit` runtime logic for Git-Alias CLI.
- @details Parses a conventional commit message and maps it to a changelog section and formatted entry line.
Entry format: `- <description> *(<scope>)*` when scope is present; `- <description>` otherwise.
Multiline descriptions are rendered as consecutive indented sub-bullets under the commit line.
When the breaking marker is present, the first description line is prefixed with `BREAKING CHANGE: `.
- @param subject Conventional commit message string.
- @return Tuple `(section, line)`: `section` is the changelog section name or `None` if type is unmapped or ignored; `line` is the formatted entry string or `""` when section is `None`.

### fn `def _extract_release_version(subject: str) -> Optional[str]` `priv` (L1316-1326)
- @brief Execute `_extract_release_version` runtime logic for Git-Alias CLI.
- @details Executes `_extract_release_version` using deterministic CLI control-flow and explicit error propagation.
- @param subject Input parameter consumed by `_extract_release_version`.
- @return Result emitted by `_extract_release_version` according to command contract.

### fn `def _is_release_marker_commit(subject: str) -> bool` `priv` (L1331-1334)
- @brief Execute `_is_release_marker_commit` runtime logic for Git-Alias CLI.
- @details Executes `_is_release_marker_commit` using deterministic CLI control-flow and explicit error propagation.
- @param subject Input parameter consumed by `_is_release_marker_commit`.
- @return Result emitted by `_is_release_marker_commit` according to command contract.

### fn `def generate_section_for_range(` (L1343-1348)
- @brief Execute `generate_section_for_range` runtime logic for Git-Alias CLI.
- @details Executes `generate_section_for_range` using deterministic CLI control-flow and explicit error propagation.
- @param repo_root Input parameter consumed by `generate_section_for_range`.
- @param title Input parameter consumed by `generate_section_for_range`.
- @param date_s Input parameter consumed by `generate_section_for_range`.
- @param rev_range Input parameter consumed by `generate_section_for_range`.
- @param expected_version Input parameter consumed by `generate_section_for_range`.
- @return Result emitted by `generate_section_for_range` according to command contract.

### fn `def _get_remote_name_for_branch(branch_name: str, repo_root: Path) -> str` `priv` (L1396-1404)
- @brief Resolve the git remote name configured for a given branch.
- @details Queries `git config branch.<branch_name>.remote` via a local git command.
Returns `origin` as fallback when the config key is absent or the command fails.
No network operations are performed.
- @param branch_name Local branch name whose configured remote is requested (e.g. `"master"`).
- @param repo_root Absolute path used as CWD for the git config query.
- @return Remote name string; never empty (falls back to `"origin"`).
- @satisfies REQ-046

### fn `def _extract_owner_repo(remote_url: str) -> Optional[Tuple[str, str]]` `priv` (L1411-1435)
- @brief Resolve the normalized HTTPS base URL from the master branch's configured remote.
- @details Parses both SSH (`git@<host>:<owner>/<repo>[.git]`) and HTTPS
(`https://<host>/<owner>/<repo>[.git]`) formats and extracts `<owner>` and `<repo>`
through deterministic string parsing.
- @param remote_url Raw git remote URL string.
- @return Tuple `(owner, repo)` when parsing succeeds; otherwise `None`.

### fn `def _canonical_origin_base(repo_root: Path) -> Optional[str]` `priv` (L1445-1460)
- @brief Resolve normalized GitHub URL base from the master-branch configured remote.
- @details Determines remote name using `_get_remote_name_for_branch` with the configured
master branch, then executes local `git remote get-url <remote>` command.
If command execution fails or URL parsing fails, returns `None`.
On success, always emits `https://github.com/<owner>/<repo>` for changelog templates.
No network operation is performed; all data is derived from local git metadata.
- @param repo_root Absolute path to the repository root used as CWD for all git commands.
- @return Normalized HTTPS base URL string (no trailing `.git`), or `None` on failure.
- @satisfies REQ-043, REQ-046

### fn `def get_origin_compare_url(` (L1467-1468)
- @brief Execute `get_origin_compare_url` runtime logic for Git-Alias CLI.
- @details Executes `get_origin_compare_url` using deterministic CLI control-flow and explicit error propagation.
- @param base_url Input parameter consumed by `get_origin_compare_url`.
- @param prev_tag Input parameter consumed by `get_origin_compare_url`.
- @param tag Input parameter consumed by `get_origin_compare_url`.
- @return Result emitted by `get_origin_compare_url` according to command contract.

### fn `def get_release_page_url(base_url: Optional[str], tag: str) -> Optional[str]` (L1482-1487)
- @brief Execute `get_release_page_url` runtime logic for Git-Alias CLI.
- @details Executes `get_release_page_url` using deterministic CLI control-flow and explicit error propagation.
- @param base_url Input parameter consumed by `get_release_page_url`.
- @param tag Input parameter consumed by `get_release_page_url`.
- @return Result emitted by `get_release_page_url` according to command contract.

### fn `def build_history_section(` (L1495-1499)
- @brief Execute `build_history_section` runtime logic for Git-Alias CLI.
- @details Executes `build_history_section` using deterministic CLI control-flow and explicit error propagation.
- @param repo_root Input parameter consumed by `build_history_section`.
- @param tags Input parameter consumed by `build_history_section`.
- @param include_unreleased Input parameter consumed by `build_history_section`.
- @param include_unreleased_link Input parameter consumed by `build_history_section`.
- @return Result emitted by `build_history_section` according to command contract.

### fn `def generate_changelog_document(` (L1543-1544)
- @brief Generate the full CHANGELOG.md document from repository tags and commits.
- @details Groups commits by minor release (semver where `patch=0` AND version `>=0.1.0`).
By default only minor releases appear; the document body is empty when none exist.
With `include_patch=True`, prepends the latest patch release after the last minor
(or the latest patch overall when no minor exists) including all commits in that range.
Releases are ordered reverse-chronologically in the output.
`# History` contains only the version tags present in the changelog body:
minor tags when `include_patch=False`; minor tags plus the latest patch when
`include_patch=True`. Diff links in `# History` use the same ranges as the
corresponding changelog sections. History generation can be disabled by flag.
- @param repo_root Absolute path to the repository root used as CWD for all git commands.
- @param include_patch When `True`, prepend the latest patch release section to the document.
- @param disable_history When `True`, omit `# History` section from output.
- @return Complete `CHANGELOG.md` string content, terminated with a newline.
- @satisfies REQ-018, REQ-040, REQ-041, REQ-043, REQ-068, REQ-069, REQ-070

### class `class VersionRuleContext` `@dataclass(frozen=True)` (L1616-1623)

### fn `def _normalize_version_rule_pattern(pattern: str) -> str` `priv` (L1629-1640)
- @brief Normalize a `ver_rules` pattern to the internal pathspec matching form.
- @details Converts separators to POSIX style, strips leading `./`, and anchors patterns containing `/`
to repository root by prefixing `/` when missing, preserving REQ-017 semantics.
- @param pattern Input pattern string from configuration.
- @return Normalized pathspec-compatible pattern string; empty string when input is blank.

### fn `def _build_version_file_inventory(root: Path) -> List[Tuple[Path, str]]` `priv` (L1646-1673)
- @brief Build a deduplicated repository file inventory for version rule evaluation.
- @details Executes a single `git ls-files` query from repository root, filters to existing files only,
applies hardcoded exclusion regexes, normalizes relative paths, and deduplicates by resolved path.
- @param root Repository root path used as traversal anchor.
- @return List of tuples `(absolute_path, normalized_relative_path)` used by downstream matchers.

### fn `def _collect_version_files(root, pattern, *, inventory=None)` `priv` (L1681-1704)
- @brief Execute `_collect_version_files` runtime logic for Git-Alias CLI.
- @details Executes `_collect_version_files` using deterministic CLI control-flow and explicit error propagation.
Uses precomputed inventory when provided to avoid repeated repository traversals.
- @param root Input parameter consumed by `_collect_version_files`.
- @param pattern Input parameter consumed by `_collect_version_files`.
- @param inventory Optional precomputed `(path, normalized_relative_path)` list.
- @return Result emitted by `_collect_version_files` according to command contract.

### fn `def _is_version_path_excluded(relative_path: str) -> bool` `priv` (L1709-1712)
- @brief Execute `_is_version_path_excluded` runtime logic for Git-Alias CLI.
- @details Executes `_is_version_path_excluded` using deterministic CLI control-flow and explicit error propagation.
- @param relative_path Input parameter consumed by `_is_version_path_excluded`.
- @return Result emitted by `_is_version_path_excluded` according to command contract.

### fn `def _iter_versions_in_text(text, compiled_regexes)` `priv` (L1718-1729)
- @brief Execute `_iter_versions_in_text` runtime logic for Git-Alias CLI.
- @details Executes `_iter_versions_in_text` using deterministic CLI control-flow and explicit error propagation.
- @param text Input parameter consumed by `_iter_versions_in_text`.
- @param compiled_regexes Input parameter consumed by `_iter_versions_in_text`.
- @return Result emitted by `_iter_versions_in_text` according to command contract.

### fn `def _read_version_file_text(` `priv` (L1736-1737)
- @brief Read and cache UTF-8 text content for a version-managed file.
- @details Loads file content with UTF-8 decoding; falls back to `errors="ignore"` on decode failures.
Emits deterministic stderr diagnostics on I/O failure and returns `None` for caller-managed skip logic.
- @param file_path Absolute path of the file to read.
- @param text_cache Optional mutable cache keyed by `Path` to avoid duplicate reads across phases.
- @return File text payload or `None` when file cannot be read.

### fn `def _prepare_version_rule_contexts(` `priv` (L1761-1762)
- @brief Build reusable per-rule contexts for canonical version evaluation workflows.
- @details Resolves matched files and compiled regex for each `(pattern, regex)` rule exactly once.
Preserves error contracts for unmatched patterns and invalid regex declarations.
- @param root Repository root path used for relative-path rendering.
- @param rules Sequence of `(pattern, regex)` tuples.
- @param inventory Optional precomputed inventory to avoid repeated filesystem traversal.
- @return Ordered list of `VersionRuleContext` objects aligned to input rule order.
- @throws VersionDetectionError when a rule matches no files or contains an invalid regex.

### fn `def _determine_canonical_version(` `priv` (L1805-1812)
- @brief Execute `_determine_canonical_version` runtime logic for Git-Alias CLI.
- @details Executes `_determine_canonical_version` using deterministic CLI control-flow and explicit error propagation.
- @param root Input parameter consumed by `_determine_canonical_version`.
- @param rules Input parameter consumed by `_determine_canonical_version`.
- @param verbose Input parameter consumed by `_determine_canonical_version`.
- @param debug Input parameter consumed by `_determine_canonical_version`.
- @param contexts Optional precomputed `VersionRuleContext` list for reuse across phases.
- @param text_cache Optional mutable cache keyed by file path to avoid duplicate reads.
- @return Result emitted by `_determine_canonical_version` according to command contract.

### fn `def _parse_semver_tuple(text: str) -> Optional[Tuple[int, int, int]]` `priv` (L1865-1871)
- @brief Execute `_parse_semver_tuple` runtime logic for Git-Alias CLI.
- @details Executes `_parse_semver_tuple` using deterministic CLI control-flow and explicit error propagation.
- @param text Input parameter consumed by `_parse_semver_tuple`.
- @return Result emitted by `_parse_semver_tuple` according to command contract.

### fn `def _replace_versions_in_text(text, compiled_regex, replacement)` `priv` (L1878-1893)
- @brief Execute `_replace_versions_in_text` runtime logic for Git-Alias CLI.
- @details Executes `_replace_versions_in_text` using deterministic CLI control-flow and explicit error propagation.
- @param text Input parameter consumed by `_replace_versions_in_text`.
- @param compiled_regex Input parameter consumed by `_replace_versions_in_text`.
- @param replacement Input parameter consumed by `_replace_versions_in_text`.
- @return Result emitted by `_replace_versions_in_text` according to command contract.

### fn `def _current_branch_name()` `priv` (L1897-1909)
- @brief Execute `_current_branch_name` runtime logic for Git-Alias CLI.
- @details Executes `_current_branch_name` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `_current_branch_name` according to command contract.

### fn `def _ref_exists(ref_name)` `priv` (L1914-1923)
- @brief Execute `_ref_exists` runtime logic for Git-Alias CLI.
- @details Executes `_ref_exists` using deterministic CLI control-flow and explicit error propagation.
- @param ref_name Input parameter consumed by `_ref_exists`.
- @return Result emitted by `_ref_exists` according to command contract.

### fn `def _local_branch_exists(branch_name)` `priv` (L1928-1931)
- @brief Execute `_local_branch_exists` runtime logic for Git-Alias CLI.
- @details Executes `_local_branch_exists` using deterministic CLI control-flow and explicit error propagation.
- @param branch_name Input parameter consumed by `_local_branch_exists`.
- @return Result emitted by `_local_branch_exists` according to command contract.

### fn `def _remote_branch_exists(branch_name)` `priv` (L1936-1939)
- @brief Execute `_remote_branch_exists` runtime logic for Git-Alias CLI.
- @details Executes `_remote_branch_exists` using deterministic CLI control-flow and explicit error propagation.
- @param branch_name Input parameter consumed by `_remote_branch_exists`.
- @return Result emitted by `_remote_branch_exists` according to command contract.

### fn `def _ensure_release_prerequisites()` `priv` (L1943-1992)
- @brief Execute `_ensure_release_prerequisites` runtime logic for Git-Alias CLI.
- @details Executes `_ensure_release_prerequisites` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `_ensure_release_prerequisites` according to command contract.

### fn `def _bump_semver_version(current_version, level)` `priv` (L1998-2018)
- @brief Execute `_bump_semver_version` runtime logic for Git-Alias CLI.
- @details Executes `_bump_semver_version` using deterministic CLI control-flow and explicit error propagation.
- @param current_version Input parameter consumed by `_bump_semver_version`.
- @param level Input parameter consumed by `_bump_semver_version`.
- @return Result emitted by `_bump_semver_version` according to command contract.

### fn `def _run_release_step(level, step_name, action)` `priv` (L2025-2051)
- @brief Execute `_run_release_step` runtime logic for Git-Alias CLI.
- @details Executes `_run_release_step` using deterministic CLI control-flow and explicit error propagation.
- @param level Input parameter consumed by `_run_release_step`.
- @param step_name Input parameter consumed by `_run_release_step`.
- @param action Input parameter consumed by `_run_release_step`.
- @return Result emitted by `_run_release_step` according to command contract.

### fn `def _create_release_commit_for_flow(target_version)` `priv` (L2056-2061)
- @brief Execute `_create_release_commit_for_flow` runtime logic for Git-Alias CLI.
- @details Executes release-flow first-commit creation with WIP amend semantics reused from `_execute_commit`.
- @param target_version Input parameter consumed by `_create_release_commit_for_flow`.
- @return Result emitted by `_create_release_commit_for_flow` according to command contract.

### fn `def _push_branch_with_tags(branch_name)` `priv` (L2067-2071)
- @brief Execute `_push_branch_with_tags` runtime logic for Git-Alias CLI.
- @details Pushes the specified local branch to `origin` using an explicit branch refspec and
includes `--tags` in the same push command.
- @param branch_name Local branch name resolved from configured release branches.
- @return Result emitted by `run_git_cmd` according to command contract.

### fn `def _execute_release_flow(level, changelog_args=None)` `priv` (L2087-2178)
- @brief Execute `_execute_release_flow` runtime logic for Git-Alias CLI.
- @details Orchestrates the full release pipeline for `major`, `minor`, and `patch` levels.
Branch integration is level-dependent (REQ-045):
- `patch`: merges `work` into `develop` and pushes `develop` only; skips `master`.
- `major`/`minor`: merges `work` into `develop`, pushes `develop` with tags, then merges
`develop` into `master` and pushes `master`.
Changelog flags always include `--force-write`; `patch` auto-adds `--include-patch`.
A temporary local `v<target>` tag is created on `work` only to generate changelog and
deleted immediately after changelog generation. The definitive `v<target>` tag is then
created on `develop` (`patch`) or `master` (`major`/`minor`) immediately before push
with `--tags`.
- @param level Release level string: `"major"`, `"minor"`, or `"patch"`.
- @param changelog_args Optional list of extra changelog flags forwarded alongside `--force-write`.
- @return None; raises `ReleaseError` or `VersionDetectionError` on failure.
- @satisfies REQ-026, REQ-045

### fn `def _execute_backup_flow()` `priv` (L2186-2203)
- @brief Execute `_execute_backup_flow` runtime logic for Git-Alias CLI.
- @details Executes the `backup` workflow by reusing the release preflight checks, then
fast-forward merges configured `work` into configured `develop`, pushes `develop`
to its configured remote tracking branch, checks out back to `work`, and prints
an explicit success confirmation.
- @return None; raises `ReleaseError` on preflight or workflow failure.
- @satisfies REQ-047, REQ-048, REQ-049

### fn `def _run_release_command(level, changelog_args=None)` `priv` (L2209-2224)
- @brief Execute `_run_release_command` runtime logic for Git-Alias CLI.
- @details Executes `_run_release_command` using deterministic CLI control-flow and explicit error propagation.
- @param level Input parameter consumed by `_run_release_command`.
- @param changelog_args Input parameter consumed by `_run_release_command`.
- @return Result emitted by `_run_release_command` according to command contract.

### fn `def _run_backup_command()` `priv` (L2229-2236)
- @brief Execute `_run_backup_command` runtime logic for Git-Alias CLI.
- @details Runs the `backup` workflow with the same error propagation strategy used by release commands.
- @return None; exits with status 1 on `ReleaseError`.
- @satisfies REQ-047, REQ-048, REQ-049

### fn `def _run_reset_with_help(base_args, extra)` `priv` (L2242-2249)
- @brief Execute `_run_reset_with_help` runtime logic for Git-Alias CLI.
- @details Executes `_run_reset_with_help` using deterministic CLI control-flow and explicit error propagation.
- @param base_args Input parameter consumed by `_run_reset_with_help`.
- @param extra Input parameter consumed by `_run_reset_with_help`.
- @return Result emitted by `_run_reset_with_help` according to command contract.

### fn `def _reject_extra_arguments(extra, alias)` `priv` (L2255-2261)
- @brief Execute `_reject_extra_arguments` runtime logic for Git-Alias CLI.
- @details Executes `_reject_extra_arguments` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `_reject_extra_arguments`.
- @param alias Input parameter consumed by `_reject_extra_arguments`.
- @return Result emitted by `_reject_extra_arguments` according to command contract.

### fn `def _parse_release_flags(extra, alias)` `priv` (L2267-2287)
- @brief Execute `_parse_release_flags` runtime logic for Git-Alias CLI.
- @details Executes `_parse_release_flags` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `_parse_release_flags`.
- @param alias Input parameter consumed by `_parse_release_flags`.
- @return Result emitted by `_parse_release_flags` according to command contract.

### fn `def _prepare_commit_message(extra, alias)` `priv` (L2293-2303)
- @brief Execute `_prepare_commit_message` runtime logic for Git-Alias CLI.
- @details Executes `_prepare_commit_message` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `_prepare_commit_message`.
- @param alias Input parameter consumed by `_prepare_commit_message`.
- @return Result emitted by `_prepare_commit_message` according to command contract.

### fn `def _normalize_conventional_description(description: str) -> str` `priv` (L2310-2320)
- @brief Normalize conventional commit description formatting.
- @details Applies canonical description normalization for conventional aliases:
uppercases the first character unless it is numeric and appends a trailing
period when missing.
- @param description Input parameter consumed by `_normalize_conventional_description`.
- @return Result emitted by `_normalize_conventional_description` according to command contract.

### fn `def _build_conventional_message(kind: str, extra, alias: str) -> str` `priv` (L2329-2350)
- @brief Execute `_build_conventional_message` runtime logic for Git-Alias CLI.
- @details Executes `_build_conventional_message` using deterministic CLI control-flow and explicit error propagation.
The output format is `<type>: <description>` when the effective module is empty,
otherwise `<type>(<module>): <description>`.
- @param kind Input parameter consumed by `_build_conventional_message`.
- @param extra Input parameter consumed by `_build_conventional_message`.
- @param alias Input parameter consumed by `_build_conventional_message`.
- @return Result emitted by `_build_conventional_message` according to command contract.

### fn `def _run_conventional_commit(kind: str, alias: str, extra)` `priv` (L2357-2362)
- @brief Execute `_run_conventional_commit` runtime logic for Git-Alias CLI.
- @details Executes `_run_conventional_commit` using deterministic CLI control-flow and explicit error propagation.
- @param kind Input parameter consumed by `_run_conventional_commit`.
- @param alias Input parameter consumed by `_run_conventional_commit`.
- @param extra Input parameter consumed by `_run_conventional_commit`.
- @return Result emitted by `_run_conventional_commit` according to command contract.

### fn `def _execute_commit(message, alias, allow_amend=True)` `priv` (L2369-2401)
- @brief Execute `_execute_commit` runtime logic for Git-Alias CLI.
- @details Executes `_execute_commit` using deterministic CLI control-flow and explicit error propagation.
- @param message Input parameter consumed by `_execute_commit`.
- @param alias Input parameter consumed by `_execute_commit`.
- @param allow_amend Input parameter consumed by `_execute_commit`.
- @return Result emitted by `_execute_commit` according to command contract.

### fn `def upgrade_self()` (L2405-2418)
- @brief Execute `upgrade_self` runtime logic for Git-Alias CLI.
- @details Executes `upgrade_self` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `upgrade_self` according to command contract.

### fn `def remove_self()` (L2422-2425)
- @brief Execute `remove_self` runtime logic for Git-Alias CLI.
- @details Executes `remove_self` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `remove_self` according to command contract.

### fn `def cmd_aa(extra)` (L2430-2437)
- @brief Execute `cmd_aa` runtime logic for Git-Alias CLI.
- @details Executes `cmd_aa` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_aa`.
- @return Result emitted by `cmd_aa` according to command contract.

### fn `def cmd_ra(extra)` (L2442-2465)
- @brief Execute `cmd_ra` runtime logic for Git-Alias CLI.
- @details Executes `cmd_ra` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_ra`.
- @return Result emitted by `cmd_ra` according to command contract.

### fn `def cmd_ar(extra)` (L2470-2486)
- @brief Execute `cmd_ar` runtime logic for Git-Alias CLI.
- @details Executes `cmd_ar` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_ar`.
- @return Result emitted by `cmd_ar` according to command contract.

### fn `def cmd_br(extra)` (L2491-2494)
- @brief Execute `cmd_br` runtime logic for Git-Alias CLI.
- @details Executes `cmd_br` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_br`.
- @return Result emitted by `cmd_br` according to command contract.

### fn `def cmd_bd(extra)` (L2499-2502)
- @brief Execute `cmd_bd` runtime logic for Git-Alias CLI.
- @details Executes `cmd_bd` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_bd`.
- @return Result emitted by `cmd_bd` according to command contract.

### fn `def cmd_ck(extra)` (L2507-2510)
- @brief Execute `cmd_ck` runtime logic for Git-Alias CLI.
- @details Executes `cmd_ck` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_ck`.
- @return Result emitted by `cmd_ck` according to command contract.

### fn `def _ensure_commit_ready(alias)` `priv` (L2515-2528)
- @brief Execute `_ensure_commit_ready` runtime logic for Git-Alias CLI.
- @details Executes `_ensure_commit_ready` using deterministic CLI control-flow and explicit error propagation.
- @param alias Input parameter consumed by `_ensure_commit_ready`.
- @return Result emitted by `_ensure_commit_ready` according to command contract.

### fn `def cmd_cm(extra)` (L2533-2538)
- @brief Execute `cmd_cm` runtime logic for Git-Alias CLI.
- @details Executes `cmd_cm` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_cm`.
- @return Result emitted by `cmd_cm` according to command contract.

### fn `def cmd_wip(extra)` (L2543-2555)
- @brief Execute `cmd_wip` runtime logic for Git-Alias CLI.
- @details Executes `cmd_wip` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_wip`.
- @return Result emitted by `cmd_wip` according to command contract.

### fn `def cmd_release(extra)` (L2560-2582)
- @brief Execute `cmd_release` runtime logic for Git-Alias CLI.
- @details Executes `cmd_release` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_release`.
- @return Result emitted by `cmd_release` according to command contract.

### fn `def cmd_new(extra)` (L2587-2590)
- @brief Execute `cmd_new` runtime logic for Git-Alias CLI.
- @details Executes `cmd_new` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_new`.
- @return Result emitted by `cmd_new` according to command contract.

### fn `def cmd_refactor(extra)` (L2595-2598)
- @brief Execute `cmd_refactor` runtime logic for Git-Alias CLI.
- @details Executes `cmd_refactor` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_refactor`.
- @return Result emitted by `cmd_refactor` according to command contract.

### fn `def cmd_fix(extra)` (L2603-2606)
- @brief Execute `cmd_fix` runtime logic for Git-Alias CLI.
- @details Executes `cmd_fix` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_fix`.
- @return Result emitted by `cmd_fix` according to command contract.

### fn `def cmd_change(extra)` (L2611-2614)
- @brief Execute `cmd_change` runtime logic for Git-Alias CLI.
- @details Executes `cmd_change` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_change`.
- @return Result emitted by `cmd_change` according to command contract.

### fn `def cmd_implement(extra)` (L2619-2622)
- @brief Execute `cmd_implement` runtime logic for Git-Alias CLI.
- @details Executes `cmd_implement` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_implement`.
- @return Result emitted by `cmd_implement` according to command contract.

### fn `def cmd_docs(extra)` (L2627-2630)
- @brief Execute `cmd_docs` runtime logic for Git-Alias CLI.
- @details Executes `cmd_docs` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_docs`.
- @return Result emitted by `cmd_docs` according to command contract.

### fn `def cmd_style(extra)` (L2635-2638)
- @brief Execute `cmd_style` runtime logic for Git-Alias CLI.
- @details Executes `cmd_style` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_style`.
- @return Result emitted by `cmd_style` according to command contract.

### fn `def cmd_revert(extra)` (L2643-2646)
- @brief Execute `cmd_revert` runtime logic for Git-Alias CLI.
- @details Executes `cmd_revert` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_revert`.
- @return Result emitted by `cmd_revert` according to command contract.

### fn `def cmd_misc(extra)` (L2651-2654)
- @brief Execute `cmd_misc` runtime logic for Git-Alias CLI.
- @details Executes `cmd_misc` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_misc`.
- @return Result emitted by `cmd_misc` according to command contract.

### fn `def cmd_cover(extra)` (L2659-2662)
- @brief Execute `cmd_cover` runtime logic for Git-Alias CLI.
- @details Executes `cmd_cover` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_cover`.
- @return Result emitted by `cmd_cover` according to command contract.

### fn `def cmd_co(extra)` (L2667-2670)
- @brief Execute `cmd_co` runtime logic for Git-Alias CLI.
- @details Executes `cmd_co` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_co`.
- @return Result emitted by `cmd_co` according to command contract.

### fn `def cmd_dc(extra)` (L2675-2684)
- @brief Execute `cmd_dc` runtime logic for Git-Alias CLI.
- @details Executes `cmd_dc` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_dc`.
- @return Result emitted by `cmd_dc` according to command contract.

### fn `def cmd_dcc(extra)` (L2689-2692)
- @brief Execute `cmd_dcc` runtime logic for Git-Alias CLI.
- @details Executes `cmd_dcc` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_dcc`.
- @return Result emitted by `cmd_dcc` according to command contract.

### fn `def cmd_dccc(extra)` (L2697-2700)
- @brief Execute `cmd_dccc` runtime logic for Git-Alias CLI.
- @details Executes `cmd_dccc` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_dccc`.
- @return Result emitted by `cmd_dccc` according to command contract.

### fn `def cmd_de(extra)` (L2705-2708)
- @brief Execute `cmd_de` runtime logic for Git-Alias CLI.
- @details Executes `cmd_de` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_de`.
- @return Result emitted by `cmd_de` according to command contract.

### fn `def cmd_di(extra)` (L2713-2716)
- @brief Execute `cmd_di` runtime logic for Git-Alias CLI.
- @details Executes `cmd_di` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_di`.
- @return Result emitted by `cmd_di` according to command contract.

### fn `def cmd_diyou(extra)` (L2721-2724)
- @brief Execute `cmd_diyou` runtime logic for Git-Alias CLI.
- @details Executes `cmd_diyou` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_diyou`.
- @return Result emitted by `cmd_diyou` according to command contract.

### fn `def cmd_dime(extra)` (L2729-2732)
- @brief Execute `cmd_dime` runtime logic for Git-Alias CLI.
- @details Executes `cmd_dime` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_dime`.
- @return Result emitted by `cmd_dime` according to command contract.

### fn `def cmd_dwc(extra)` (L2737-2740)
- @brief Execute `cmd_dwc` runtime logic for Git-Alias CLI.
- @details Executes `cmd_dwc` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_dwc`.
- @return Result emitted by `cmd_dwc` according to command contract.

### fn `def cmd_dw(extra)` (L2745-2752)
- @brief Execute `cmd_dw` runtime logic for Git-Alias CLI.
- @details Executes `cmd_dw` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_dw`.
- @return Result emitted by `cmd_dw` according to command contract.

### fn `def cmd_dwcc(extra)` (L2757-2760)
- @brief Execute `cmd_dwcc` runtime logic for Git-Alias CLI.
- @details Executes `cmd_dwcc` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_dwcc`.
- @return Result emitted by `cmd_dwcc` according to command contract.

### fn `def cmd_dcd(extra)` (L2766-2771)
- @brief Execute `cmd_dcd` runtime logic for Git-Alias CLI.
- @details Executes `cmd_dcd` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_dcd`.
- @return Result emitted by `cmd_dcd` according to command contract.
- @satisfies REQ-119

### fn `def cmd_dcm(extra)` (L2777-2782)
- @brief Execute `cmd_dcm` runtime logic for Git-Alias CLI.
- @details Executes `cmd_dcm` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_dcm`.
- @return Result emitted by `cmd_dcm` according to command contract.
- @satisfies REQ-119

### fn `def cmd_ddm(extra)` (L2788-2793)
- @brief Execute `cmd_ddm` runtime logic for Git-Alias CLI.
- @details Executes `cmd_ddm` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_ddm`.
- @return Result emitted by `cmd_ddm` according to command contract.
- @satisfies REQ-119

### fn `def cmd_ed(extra)` (L2798-2807)
- @brief Execute `cmd_ed` runtime logic for Git-Alias CLI.
- @details Executes `cmd_ed` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_ed`.
- @return Result emitted by `cmd_ed` according to command contract.

### fn `def cmd_fe(extra)` (L2812-2815)
- @brief Execute `cmd_fe` runtime logic for Git-Alias CLI.
- @details Executes `cmd_fe` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_fe`.
- @return Result emitted by `cmd_fe` according to command contract.

### fn `def cmd_feall(extra)` (L2820-2823)
- @brief Execute `cmd_feall` runtime logic for Git-Alias CLI.
- @details Executes `cmd_feall` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_feall`.
- @return Result emitted by `cmd_feall` according to command contract.

### fn `def cmd_gp(extra)` (L2828-2833)
- @brief Execute `cmd_gp` runtime logic for Git-Alias CLI.
- @details Executes `cmd_gp` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_gp`.
- @return Result emitted by `cmd_gp` according to command contract.

### fn `def cmd_gr(extra)` (L2838-2843)
- @brief Execute `cmd_gr` runtime logic for Git-Alias CLI.
- @details Executes `cmd_gr` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_gr`.
- @return Result emitted by `cmd_gr` according to command contract.

- var `OVERVIEW_COLOR_RESET = "\033[0m"` (L2845)
- @brief Constant `OVERVIEW_COLOR_RESET` used by CLI runtime paths and policies.
- var `OVERVIEW_COLOR_SECTION_PURPLE = "\033[35;1m"` (L2847)
- @brief Constant `OVERVIEW_COLOR_SECTION_PURPLE` used by CLI runtime paths and policies.
- var `OVERVIEW_COLOR_AHEAD = "\033[92m"` (L2849)
- @brief Constant `OVERVIEW_COLOR_AHEAD` used by CLI runtime paths and policies.
- var `OVERVIEW_COLOR_BEHIND = "\033[31;1m"` (L2851)
- @brief Constant `OVERVIEW_COLOR_BEHIND` used by CLI runtime paths and policies.
- var `OVERVIEW_COLOR_LABEL = "\033[38;5;226m"` (L2853)
- @brief Constant `OVERVIEW_COLOR_LABEL` used by CLI runtime paths and policies.
- var `OVERVIEW_COLOR_WHITE = "\033[97m"` (L2855)
- @brief Constant `OVERVIEW_COLOR_WHITE` used by CLI runtime paths and policies.
- var `OVERVIEW_COLOR_WHITE_BOLD = "\033[97;1m"` (L2857)
- @brief Constant `OVERVIEW_COLOR_WHITE_BOLD` used by CLI runtime paths and policies.
- var `OVERVIEW_SECTION_TEMPLATE = "{color}=== {title} ==={reset}"` (L2859)
- @brief Constant `OVERVIEW_SECTION_TEMPLATE` used by CLI runtime paths and policies.
- var `OVERVIEW_SUBSECTION_TEMPLATE = "{color}--- {title} ---{reset}"` (L2861)
- @brief Constant `OVERVIEW_SUBSECTION_TEMPLATE` used by CLI runtime paths and policies.
- var `OVERVIEW_DISTANCE_TEMPLATE = "{text_color}{label}{reset} | {ahead} | {behind}"` (L2863)
- @brief Constant `OVERVIEW_DISTANCE_TEMPLATE` used by CLI runtime paths and policies.
### fn `def _overview_branch_identifier(` `priv` (L2872-2875)
- @brief Execute `_overview_branch_identifier` runtime logic for Git-Alias CLI.
- @details Executes `_overview_branch_identifier` using deterministic CLI control-flow and explicit error propagation.
- @param logical_name Input parameter consumed by `_overview_branch_identifier`.
- @param ref_name Input parameter consumed by `_overview_branch_identifier`.
- @param prefix_color Input parameter consumed by `_overview_branch_identifier`.
- @return Result emitted by `_overview_branch_identifier` according to command contract.

### fn `def _overview_work_prefix_color(worktree_state: str) -> str` `priv` (L2889-2896)
- @brief Execute `_overview_work_prefix_color` runtime logic for Git-Alias CLI.
- @details Executes `_overview_work_prefix_color` using deterministic CLI control-flow and explicit error propagation.
- @param worktree_state Input parameter consumed by `_overview_work_prefix_color`.
- @return Result emitted by `_overview_work_prefix_color` according to command contract.

### fn `def _overview_logical_branch_name(` `priv` (L2904-2908)
- @brief Execute `_overview_logical_branch_name` runtime logic for Git-Alias CLI.
- @details Executes `_overview_logical_branch_name` using deterministic CLI control-flow and explicit error propagation.
- @param current_branch Input parameter consumed by `_overview_logical_branch_name`.
- @param work_branch Input parameter consumed by `_overview_logical_branch_name`.
- @param develop_branch Input parameter consumed by `_overview_logical_branch_name`.
- @param master_branch Input parameter consumed by `_overview_logical_branch_name`.
- @return Result emitted by `_overview_logical_branch_name` according to command contract.

### fn `def _overview_current_branch_display(` `priv` (L2927-2932)
- @brief Execute `_overview_current_branch_display` runtime logic for Git-Alias CLI.
- @details Executes `_overview_current_branch_display` using deterministic CLI control-flow and explicit error propagation.
- @param current_branch Input parameter consumed by `_overview_current_branch_display`.
- @param work_branch Input parameter consumed by `_overview_current_branch_display`.
- @param develop_branch Input parameter consumed by `_overview_current_branch_display`.
- @param master_branch Input parameter consumed by `_overview_current_branch_display`.
- @param worktree_state Input parameter consumed by `_overview_current_branch_display`.
- @return Result emitted by `_overview_current_branch_display` according to command contract.

### fn `def _overview_ref_is_available(ref_name: str) -> bool` `priv` (L2954-2963)
- @brief Execute `_overview_ref_is_available` runtime logic for Git-Alias CLI.
- @details Executes `_overview_ref_is_available` using deterministic CLI control-flow and explicit error propagation.
- @param ref_name Input parameter consumed by `_overview_ref_is_available`.
- @return Result emitted by `_overview_ref_is_available` according to command contract.

### fn `def _overview_ref_latest_subject(ref_name: str) -> str` `priv` (L2969-2979)
- @brief Resolve latest commit subject for an overview ref.
- @details Returns the `%s` subject of `git log -1` for the input ref, or `n/a`
when the ref is unavailable or the lookup fails.
- @param ref_name Input parameter consumed by `_overview_ref_latest_subject`.
- @return Result emitted by `_overview_ref_latest_subject` according to command contract.

### fn `def _overview_discovered_branch_refs() -> List[str]` `priv` (L2984-3007)
- @brief Collect normalized branch refs from `git branch -a` for overview rendering.
- @details Returns ordered unique branch refs, stripping current-branch marker and
`remotes/` prefix and excluding symbolic-ref redirect rows.
- @return Result emitted by `_overview_discovered_branch_refs` according to command contract.

### fn `def _overview_branch_summary_lines(` `priv` (L3026-3037)
- @brief Build section-5 aligned branch summary lines for overview output.
- @details Produces one row for each configured branch/ref identifier using
`<Identifier> | <latest commit subject>` formatting, aligned by visible
identifier width and with commit subject in bright white bold; appends rows
for additional branch refs after configured rows.
- @param work_ref Input parameter consumed by `_overview_branch_summary_lines`.
- @param develop_ref Input parameter consumed by `_overview_branch_summary_lines`.
- @param master_ref Input parameter consumed by `_overview_branch_summary_lines`.
- @param remote_develop_ref Input parameter consumed by `_overview_branch_summary_lines`.
- @param remote_master_ref Input parameter consumed by `_overview_branch_summary_lines`.
- @param work_display Input parameter consumed by `_overview_branch_summary_lines`.
- @param develop_display Input parameter consumed by `_overview_branch_summary_lines`.
- @param master_display Input parameter consumed by `_overview_branch_summary_lines`.
- @param remote_develop_display Input parameter consumed by `_overview_branch_summary_lines`.
- @param remote_master_display Input parameter consumed by `_overview_branch_summary_lines`.
- @param additional_refs Input parameter consumed by `_overview_branch_summary_lines`.
- @return Result emitted by `_overview_branch_summary_lines` according to command contract.
- @satisfies REQ-094, REQ-096, REQ-115

### fn `def _overview_relation_state(ahead: int, behind: int) -> str` `priv` (L3080-3089)
- @brief Execute `_overview_relation_state` runtime logic for Git-Alias CLI.
- @details Executes `_overview_relation_state` using deterministic CLI control-flow and explicit error propagation.
- @param ahead Input parameter consumed by `_overview_relation_state`.
- @param behind Input parameter consumed by `_overview_relation_state`.
- @return Result emitted by `_overview_relation_state` according to command contract.

### fn `def _overview_worktree_state(status_lines=None) -> str` `priv` (L3094-3106)
- @brief Execute `_overview_worktree_state` runtime logic for Git-Alias CLI.
- @details Executes `_overview_worktree_state` using deterministic CLI control-flow and explicit error propagation.
- @param status_lines Input parameter consumed by `_overview_worktree_state`.
- @return Result emitted by `_overview_worktree_state` according to command contract.

### fn `def _overview_distance_text(is_ahead: bool, count: int) -> str` `priv` (L3112-3120)
- @brief Execute `_overview_distance_text` runtime logic for Git-Alias CLI.
- @details Executes `_overview_distance_text` using deterministic CLI control-flow and explicit error propagation.
- @param is_ahead Input parameter consumed by `_overview_distance_text`.
- @param count Input parameter consumed by `_overview_distance_text`.
- @return Result emitted by `_overview_distance_text` according to command contract.

### fn `def _overview_compare_refs(base_ref: str, target_ref: str, label: str) -> str` `priv` (L3127-3169)
- @brief Execute `_overview_compare_refs` runtime logic for Git-Alias CLI.
- @details Executes `_overview_compare_refs` using deterministic CLI control-flow and explicit error propagation.
- @param base_ref Input parameter consumed by `_overview_compare_refs`.
- @param target_ref Input parameter consumed by `_overview_compare_refs`.
- @param label Input parameter consumed by `_overview_compare_refs`.
- @return Result emitted by `_overview_compare_refs` according to command contract.

### fn `def _overview_ascii_topology_lines(` `priv` (L3190-3201)
- @brief Build chronological-position topology tree from actual commit positions.
- @details Resolves commit hashes for each ref, computes commit counts from
octopus merge-base, groups refs sharing the same hash on one output line,
and orders nodes from most-ahead (root) to most-behind (deepest child).
WorkingTree always occupies a dedicated line above the line that contains
Work when tied or dirty. Complexity O(R) git
subprocess calls where R is the number of available refs.
- @param work_ref {str} Git ref name for work branch.
- @param develop_ref {str} Git ref name for develop branch.
- @param master_ref {str} Git ref name for master branch.
- @param remote_develop_ref {str} Git ref name for remote develop (e.g., origin/develop).
- @param remote_master_ref {str} Git ref name for remote master (e.g., origin/master).
- @param work_display {str} Rendered display string for Work identifier.
- @param develop_display {str} Rendered display string for Develop identifier.
- @param master_display {str} Rendered display string for Master identifier.
- @param remote_develop_display {str} Rendered display string for RemoteDevelop identifier.
- @param remote_master_display {str} Rendered display string for RemoteMaster identifier.
- @param worktree_state {str} Working tree state (clean/unstaged/staged/mixed).
- @return {List[str]} Rendered topology lines with ANSI color codes.
- @satisfies REQ-089, REQ-090, REQ-091, REQ-092, REQ-093, REQ-095

### fn `def _overview_current_branch_state_lines(current_branch_display: str) -> List[str]` `priv` (L3293-3312)
- @brief Build normalized section-6 status lines for overview output.
- @details Executes `git status -sb`, rewrites the header line from
`## <branch>` to `## <Logical>(⎇ <branch>)` with the same color formatting
used by section-1 current-branch output, and preserves all other lines.
- @param current_branch_display Input parameter consumed by `_overview_current_branch_state_lines`.
- @return {List[str]} Result emitted by `_overview_current_branch_state_lines` according to command contract.
- @satisfies REQ-094

### fn `def cmd_o(extra)` (L3318-3472)
- @brief Execute `cmd_o` runtime logic for Git-Alias CLI.
- @details Executes `cmd_o` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_o`.
- @return Result emitted by `cmd_o` according to command contract.
- @satisfies REQ-082, REQ-083, REQ-084, REQ-085, REQ-086, REQ-087, REQ-088, REQ-089, REQ-090, REQ-091, REQ-092, REQ-093, REQ-094, REQ-095, REQ-096, REQ-115

### fn `def cmd_str(extra)` (L3477-3506)
- @brief Execute `cmd_str` runtime logic for Git-Alias CLI.
- @details Executes `cmd_str` using deterministic CLI control-flow and explicit error propagation.
- @details Query git remotes with transport metadata.
- @param extra Input parameter consumed by `cmd_str`.
- @return Result emitted by `cmd_str` according to command contract.

### fn `def cmd_l(extra)` (L3515-3521)
- @brief Execute `cmd_l` runtime logic for Git-Alias CLI.
- @details Delegates to `foresta.run()` which renders a text-based tree visualization
of git commit history using a vine-based graph algorithm with configurable styles,
symbols, colors, and margins. Injects `-n 35` only when invoked without
user arguments; otherwise forwards provided arguments unchanged.
- @param extra {list} Additional CLI arguments forwarded to the foresta engine.
- @return None.
- @satisfies REQ-098, REQ-099, REQ-111

### fn `def cmd_lb(extra)` (L3526-3529)
- @brief Execute `cmd_lb` runtime logic for Git-Alias CLI.
- @details Executes `cmd_lb` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_lb`.
- @return Result emitted by `cmd_lb` according to command contract.

### fn `def cmd_lg(extra)` (L3534-3547)
- @brief Execute `cmd_lg` runtime logic for Git-Alias CLI.
- @details Executes `cmd_lg` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_lg`.
- @return Result emitted by `cmd_lg` according to command contract.

### fn `def cmd_lh(extra)` (L3552-3555)
- @brief Execute `cmd_lh` runtime logic for Git-Alias CLI.
- @details Executes `cmd_lh` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_lh`.
- @return Result emitted by `cmd_lh` according to command contract.

### fn `def cmd_ll(extra)` (L3560-3572)
- @brief Execute `cmd_ll` runtime logic for Git-Alias CLI.
- @details Executes `cmd_ll` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_ll`.
- @return Result emitted by `cmd_ll` according to command contract.

### fn `def cmd_lm(extra)` (L3577-3580)
- @brief Execute `cmd_lm` runtime logic for Git-Alias CLI.
- @details Executes `cmd_lm` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_lm`.
- @return Result emitted by `cmd_lm` according to command contract.

### fn `def cmd_ls(extra)` (L3586-3589)
- @brief Execute `cmd_ls` runtime logic for Git-Alias CLI.
- @details Executes `cmd_ls` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_ls`.
- @return Result emitted by `cmd_ls` according to command contract.
- @satisfies REQ-079

### fn `def cmd_lsi(extra)` (L3600-3617)
- @brief Execute `cmd_lsi` runtime logic for Git-Alias CLI.
- @details Runs `git ls-files --others --ignored --exclude-standard` and filters
output by excluding paths where any path component matches any entry in
`LSI_DEFAULT_EXCLUDED_DIRS`. When `--include-all` is present in @p extra,
filtering is bypassed and all output is printed. Additional arguments
are forwarded to the underlying git command unchanged. Path component
matching uses `frozenset.intersection` for O(min(n,m)) lookup per line.
- @param extra List[str] CLI arguments passed after the alias name.
- @return None. Filtered output is printed to stdout.
- @satisfies REQ-080, REQ-121

### fn `def cmd_lsa(extra)` (L3623-3626)
- @brief Execute `cmd_lsa` runtime logic for Git-Alias CLI.
- @details Executes `cmd_lsa` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_lsa`.
- @return Result emitted by `cmd_lsa` according to command contract.
- @satisfies REQ-081

### fn `def cmd_lt(extra)` (L3632-3651)
- @brief Execute `cmd_lt` runtime logic for Git-Alias CLI.
- @details Enumerates tags via `git tag -l`, resolves containing refs via `git branch -a --contains <tag>`,
trims branch markers/prefixes from git output, and prints deterministic `<tag>: <branch_1>, <branch_2>, ...` lines.
- @param extra Input parameter consumed by `cmd_lt`.
- @return Result emitted by `cmd_lt` according to command contract.

### fn `def cmd_me(extra)` (L3656-3659)
- @brief Execute `cmd_me` runtime logic for Git-Alias CLI.
- @details Executes `cmd_me` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_me`.
- @return Result emitted by `cmd_me` according to command contract.

### fn `def cmd_pl(extra)` (L3664-3667)
- @brief Execute `cmd_pl` runtime logic for Git-Alias CLI.
- @details Executes `cmd_pl` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_pl`.
- @return Result emitted by `cmd_pl` according to command contract.

### fn `def cmd_pt(extra)` (L3672-3675)
- @brief Execute `cmd_pt` runtime logic for Git-Alias CLI.
- @details Executes `cmd_pt` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_pt`.
- @return Result emitted by `cmd_pt` according to command contract.

### fn `def cmd_pu(extra)` (L3680-3683)
- @brief Execute `cmd_pu` runtime logic for Git-Alias CLI.
- @details Executes `cmd_pu` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_pu`.
- @return Result emitted by `cmd_pu` according to command contract.

### fn `def cmd_rf(extra)` (L3688-3691)
- @brief Execute `cmd_rf` runtime logic for Git-Alias CLI.
- @details Executes `cmd_rf` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_rf`.
- @return Result emitted by `cmd_rf` according to command contract.

### fn `def cmd_rmtg(extra)` (L3696-3706)
- @brief Execute `cmd_rmtg` runtime logic for Git-Alias CLI.
- @details Executes `cmd_rmtg` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_rmtg`.
- @return Result emitted by `cmd_rmtg` according to command contract.

### fn `def cmd_rmloc(extra)` (L3711-3714)
- @brief Execute `cmd_rmloc` runtime logic for Git-Alias CLI.
- @details Executes `cmd_rmloc` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_rmloc`.
- @return Result emitted by `cmd_rmloc` according to command contract.

### fn `def cmd_rmstg(extra)` (L3719-3722)
- @brief Execute `cmd_rmstg` runtime logic for Git-Alias CLI.
- @details Executes `cmd_rmstg` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_rmstg`.
- @return Result emitted by `cmd_rmstg` according to command contract.

### fn `def cmd_rmunt(extra)` (L3727-3730)
- @brief Execute `cmd_rmunt` runtime logic for Git-Alias CLI.
- @details Executes `cmd_rmunt` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_rmunt`.
- @return Result emitted by `cmd_rmunt` according to command contract.

### fn `def cmd_rs(extra)` (L3735-3738)
- @brief Execute `cmd_rs` runtime logic for Git-Alias CLI.
- @details Executes `cmd_rs` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_rs`.
- @return Result emitted by `cmd_rs` according to command contract.

### fn `def cmd_rssft(extra)` (L3743-3746)
- @brief Execute `cmd_rssft` runtime logic for Git-Alias CLI.
- @details Executes `cmd_rssft` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_rssft`.
- @return Result emitted by `cmd_rssft` according to command contract.

### fn `def cmd_rsmix(extra)` (L3751-3754)
- @brief Execute `cmd_rsmix` runtime logic for Git-Alias CLI.
- @details Executes `cmd_rsmix` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_rsmix`.
- @return Result emitted by `cmd_rsmix` according to command contract.

### fn `def cmd_rshrd(extra)` (L3759-3762)
- @brief Execute `cmd_rshrd` runtime logic for Git-Alias CLI.
- @details Executes `cmd_rshrd` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_rshrd`.
- @return Result emitted by `cmd_rshrd` according to command contract.

### fn `def cmd_rsmrg(extra)` (L3767-3770)
- @brief Execute `cmd_rsmrg` runtime logic for Git-Alias CLI.
- @details Executes `cmd_rsmrg` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_rsmrg`.
- @return Result emitted by `cmd_rsmrg` according to command contract.

### fn `def cmd_rskep(extra)` (L3775-3778)
- @brief Execute `cmd_rskep` runtime logic for Git-Alias CLI.
- @details Executes `cmd_rskep` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_rskep`.
- @return Result emitted by `cmd_rskep` according to command contract.

### fn `def cmd_st(extra)` (L3783-3786)
- @brief Execute `cmd_st` runtime logic for Git-Alias CLI.
- @details Executes `cmd_st` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_st`.
- @return Result emitted by `cmd_st` according to command contract.

### fn `def cmd_tg(extra)` (L3791-3794)
- @brief Execute `cmd_tg` runtime logic for Git-Alias CLI.
- @details Executes `cmd_tg` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_tg`.
- @return Result emitted by `cmd_tg` according to command contract.

### fn `def cmd_unstg(extra)` (L3799-3802)
- @brief Execute `cmd_unstg` runtime logic for Git-Alias CLI.
- @details Executes `cmd_unstg` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_unstg`.
- @return Result emitted by `cmd_unstg` according to command contract.

### fn `def cmd_wt(extra)` (L3807-3810)
- @brief Execute `cmd_wt` runtime logic for Git-Alias CLI.
- @details Executes `cmd_wt` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_wt`.
- @return Result emitted by `cmd_wt` according to command contract.

### fn `def cmd_wtl(extra)` (L3815-3818)
- @brief Execute `cmd_wtl` runtime logic for Git-Alias CLI.
- @details Executes `cmd_wtl` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_wtl`.
- @return Result emitted by `cmd_wtl` according to command contract.

### fn `def cmd_wtp(extra)` (L3823-3826)
- @brief Execute `cmd_wtp` runtime logic for Git-Alias CLI.
- @details Executes `cmd_wtp` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_wtp`.
- @return Result emitted by `cmd_wtp` according to command contract.

### fn `def cmd_wtr(extra)` (L3831-3834)
- @brief Execute `cmd_wtr` runtime logic for Git-Alias CLI.
- @details Executes `cmd_wtr` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_wtr`.
- @return Result emitted by `cmd_wtr` according to command contract.

### fn `def cmd_ver(extra)` (L3839-3865)
- @brief Execute `cmd_ver` runtime logic for Git-Alias CLI.
- @details Executes `cmd_ver` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_ver`.
- @return Result emitted by `cmd_ver` according to command contract.

### fn `def cmd_chver(extra)` (L3870-3953)
- @brief Execute `cmd_chver` runtime logic for Git-Alias CLI.
- @details Executes `cmd_chver` using deterministic CLI control-flow and explicit error propagation.
- @param extra Input parameter consumed by `cmd_chver`.
- @return Result emitted by `cmd_chver` according to command contract.

### fn `def cmd_major(extra)` (L3962-3966)
- @brief CLI entry-point for the `major` release subcommand.
- @details Increments the major semver index (resets minor and patch to 0), merges and pushes
to both configured `develop` and `master` branches, regenerates changelog via a
temporary local tag on `work`, and creates the definitive release tag on `master`
immediately before pushing `master` with `--tags`.
- @param extra Iterable of CLI argument strings; accepted flag: `--include-patch`.
- @return None; delegates to `_run_release_command("major", ...)`.
- @satisfies REQ-026, REQ-045

### fn `def cmd_minor(extra)` (L3975-3979)
- @brief CLI entry-point for the `minor` release subcommand.
- @details Increments the minor semver index (resets patch to 0), merges and pushes to both
configured `develop` and `master` branches, regenerates changelog via a temporary local
tag on `work`, and creates the definitive release tag on `master` immediately before
pushing `master` with `--tags`.
- @param extra Iterable of CLI argument strings; accepted flag: `--include-patch`.
- @return None; delegates to `_run_release_command("minor", ...)`.
- @satisfies REQ-026, REQ-045

### fn `def cmd_patch(extra)` (L3988-3992)
- @brief CLI entry-point for the `patch` release subcommand.
- @details Increments the patch semver index, merges and pushes to configured `develop` only
(MUST NOT merge or push to `master`), regenerates changelog via a temporary local tag
on `work`, and creates the definitive release tag on `develop` immediately before
pushing `develop` with `--tags`; `--include-patch` is auto-included.
- @param extra Iterable of CLI argument strings; accepted flag: `--include-patch`.
- @return None; delegates to `_run_release_command("patch", ...)`.
- @satisfies REQ-026, REQ-045

### fn `def cmd_backup(extra)` (L4000-4010)
- @brief CLI entry-point for the `backup` workflow subcommand.
- @details Runs the same preflight checks used by `major`/`minor`/`patch`, then integrates the
configured `work` branch into the configured `develop` branch and pushes `develop`
to its remote tracking branch before returning to `work`.
- @param extra Iterable of CLI argument strings; accepted token: `--help` only.
- @return None; delegates to `_run_backup_command()`.
- @satisfies REQ-047, REQ-048, REQ-049

### fn `def cmd_changelog(extra)` (L4020-4057)
- @brief CLI entry-point for the `changelog` subcommand.
- @details Parses flags, delegates to `generate_changelog_document`, and writes or prints the result.
Accepted flags: `--include-patch`, `--force-write`, `--print-only`,
`--disable-history`, `--help`.
Exits with status 2 on argument errors or when not inside a git repository.
Exits with status 1 when `CHANGELOG.md` already exists and `--force-write` was not supplied.
- @param extra Iterable of CLI argument strings following the `changelog` subcommand token.
- @return None; side-effects: writes `CHANGELOG.md` to disk or prints to stdout.
- @satisfies REQ-018, REQ-040, REQ-041, REQ-043

- var `COMMANDS = {` (L4060)
- @brief Constant `COMMANDS` used by CLI runtime paths and policies.
### fn `def print_command_help(name, width=None)` (L4147-4154)
- @brief Execute `print_command_help` runtime logic for Git-Alias CLI.
- @details Executes `print_command_help` using deterministic CLI control-flow and explicit error propagation.
- @param name Input parameter consumed by `print_command_help`.
- @param width Input parameter consumed by `print_command_help`.
- @return Result emitted by `print_command_help` according to command contract.

### fn `def print_all_help()` (L4158-4192)
- @brief Execute `print_all_help` runtime logic for Git-Alias CLI.
- @details Executes `print_all_help` using deterministic CLI control-flow and explicit error propagation.
- @return Result emitted by `print_all_help` according to command contract.

### fn `def main(argv=None, *, check_updates: bool = True)` (L4198-4248)
- @brief Execute `main` runtime logic for Git-Alias CLI.
- @details Executes `main` using deterministic CLI control-flow and explicit error propagation.
- @param argv Input parameter consumed by `main`.
- @param check_updates Input parameter consumed by `main`.
- @return Result emitted by `main` according to command contract.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`CONFIG_FILENAME`|var|pub|28||
|`GLOBAL_CONFIG_DIRECTORY`|var|pub|30||
|`GLOBAL_CONFIG_FILENAME`|var|pub|32||
|`GITHUB_LATEST_RELEASE_API`|var|pub|36||
|`VERSION_CHECK_CACHE_FILE`|var|pub|39||
|`VERSION_CHECK_TTL_HOURS`|var|pub|42||
|`DEFAULT_VER_RULES`|var|pub|46||
|`VERSION_CLEANUP_REGEXES`|var|pub|53||
|`VERSION_CLEANUP_PATTERNS`|var|pub|64||
|`ANSI_ESCAPE_RE`|var|pub|65||
|`DEFAULT_GP_COMMAND`|var|pub|69||
|`DEFAULT_GR_COMMAND`|var|pub|71||
|`DEFAULT_CONFIG`|var|pub|73||
|`CONFIG`|var|pub|93||
|`BRANCH_KEYS`|var|pub|96||
|`LOCAL_CONFIG_KEYS`|var|pub|98||
|`GLOBAL_CONFIG_KEYS`|var|pub|100||
|`MANAGEMENT_HELP`|var|pub|103||
|`get_config_value`|fn|pub|120-123|def get_config_value(name)|
|`get_branch`|fn|pub|128-133|def get_branch(name)|
|`get_editor`|fn|pub|137-140|def get_editor()|
|`_load_config_rules`|fn|priv|146-171|def _load_config_rules(key, fallback)|
|`get_version_rules`|fn|pub|175-178|def get_version_rules()|
|`get_cli_version`|fn|pub|182-193|def get_cli_version()|
|`_normalize_semver_text`|fn|priv|198-204|def _normalize_semver_text(text: str) -> str|
|`check_for_newer_version`|fn|pub|209-299|def check_for_newer_version(timeout_seconds: float = 1.0)...|
|`get_git_root`|fn|pub|303-318|def get_git_root()|
|`get_config_path`|fn|pub|323-327|def get_config_path(root=None)|
|`get_global_config_path`|fn|pub|332-336|def get_global_config_path(home=None)|
|`_read_config_object`|fn|priv|341-359|def _read_config_object(config_path)|
|`_apply_config_values`|fn|priv|365-387|def _apply_config_values(data, keys)|
|`load_cli_config`|fn|pub|393-405|def load_cli_config(root=None, home=None)|
|`_write_missing_config_values`|fn|priv|412-469|def _write_missing_config_values(config_path, keys, creat...|
|`write_default_config`|fn|pub|475-488|def write_default_config(root=None, home=None)|
|`_editor_base_command`|fn|priv|492-506|def _editor_base_command()|
|`run_editor_command`|fn|pub|511-514|def run_editor_command(args)|
|`_config_command_parts`|fn|priv|522-546|def _config_command_parts(key: str, default_command: str)...|
|`HELP_TEXTS`|var|pub|549||
|`RESET_HELP_COMMANDS`|var|pub|714||
|`LSI_DEFAULT_EXCLUDED_DIRS`|var|pub|720||
|`_to_args`|fn|priv|757-760|def _to_args(extra)|
|`CommandExecutionError`|class|pub|763-804|class CommandExecutionError(RuntimeError)|
|`CommandExecutionError.__init__`|fn|priv|768-775|def __init__(self, exc: subprocess.CalledProcessError)|
|`CommandExecutionError._format_message`|fn|priv|779-789|def _format_message(self) -> str|
|`CommandExecutionError._decode_stream`|fn|priv|794-804|def _decode_stream(data) -> str|
|`_run_checked`|fn|priv|810-817|def _run_checked(*popenargs, **kwargs)|
|`VersionDetectionError`|class|pub|820-823|class VersionDetectionError(RuntimeError)|
|`ReleaseError`|class|pub|826-829|class ReleaseError(RuntimeError)|
|`run_git_cmd`|fn|pub|837-841|def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)|
|`capture_git_output`|fn|pub|847-853|def capture_git_output(base_args, cwd=None)|
|`run_command`|fn|pub|859-862|def run_command(cmd, cwd=None)|
|`run_git_text`|fn|pub|869-886|def run_git_text(args, cwd=None, check=True)|
|`run_shell`|fn|pub|892-895|def run_shell(command, cwd=None)|
|`_git_status_lines`|fn|priv|899-911|def _git_status_lines()|
|`has_unstaged_changes`|fn|pub|916-927|def has_unstaged_changes(status_lines=None)|
|`has_staged_changes`|fn|pub|932-941|def has_staged_changes(status_lines=None)|
|`WIP_MESSAGE_RE`|var|pub|947||
|`_refresh_remote_refs`|fn|priv|953-964|def _refresh_remote_refs()|
|`_branch_remote_divergence`|fn|priv|970-990|def _branch_remote_divergence(branch_key, remote="origin")|
|`has_remote_branch_updates`|fn|pub|996-1000|def has_remote_branch_updates(branch_key, remote="origin")|
|`has_remote_develop_updates`|fn|pub|1004-1007|def has_remote_develop_updates()|
|`has_remote_master_updates`|fn|pub|1011-1014|def has_remote_master_updates()|
|`_head_commit_message`|fn|priv|1018-1024|def _head_commit_message()|
|`_head_commit_hash`|fn|priv|1028-1034|def _head_commit_hash()|
|`_commit_exists_in_branch`|fn|priv|1040-1052|def _commit_exists_in_branch(commit_hash, branch_name)|
|`_should_amend_existing_commit`|fn|priv|1056-1071|def _should_amend_existing_commit()|
|`is_inside_git_repo`|fn|pub|1075-1082|def is_inside_git_repo()|
|`TagInfo`|class|pub|1087-1095|class TagInfo|
|`DELIM`|var|pub|1098||
|`RECORD`|var|pub|1101||
|`SEMVER_RE`|var|pub|1117||
|`SECTION_EMOJI`|var|pub|1120||
|`_tag_semver_tuple`|fn|priv|1138-1141|def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[in...|
|`_latest_supported_tag_name`|fn|priv|1146-1149|def _latest_supported_tag_name(tags: List[TagInfo]) -> Op...|
|`_is_minor_release_tag`|fn|priv|1157-1164|def _is_minor_release_tag(tag_name: str) -> bool|
|`_latest_patch_tag_after`|fn|priv|1173-1174|def _latest_patch_tag_after(|
|`list_tags_sorted_by_date`|fn|pub|1192-1193|def list_tags_sorted_by_date(|
|`git_log_subjects`|fn|pub|1223-1234|def git_log_subjects(repo_root: Path, rev_range: str) -> ...|
|`parse_conventional_commit`|fn|pub|1240-1241|def parse_conventional_commit(|
|`_format_changelog_description`|fn|priv|1261-1274|def _format_changelog_description(desc: str) -> List[str]|
|`categorize_commit`|fn|pub|1282-1311|def categorize_commit(subject: str) -> Tuple[Optional[str...|
|`_extract_release_version`|fn|priv|1316-1326|def _extract_release_version(subject: str) -> Optional[str]|
|`_is_release_marker_commit`|fn|priv|1331-1334|def _is_release_marker_commit(subject: str) -> bool|
|`generate_section_for_range`|fn|pub|1343-1348|def generate_section_for_range(|
|`_get_remote_name_for_branch`|fn|priv|1396-1404|def _get_remote_name_for_branch(branch_name: str, repo_ro...|
|`_extract_owner_repo`|fn|priv|1411-1435|def _extract_owner_repo(remote_url: str) -> Optional[Tupl...|
|`_canonical_origin_base`|fn|priv|1445-1460|def _canonical_origin_base(repo_root: Path) -> Optional[str]|
|`get_origin_compare_url`|fn|pub|1467-1468|def get_origin_compare_url(|
|`get_release_page_url`|fn|pub|1482-1487|def get_release_page_url(base_url: Optional[str], tag: st...|
|`build_history_section`|fn|pub|1495-1499|def build_history_section(|
|`generate_changelog_document`|fn|pub|1543-1544|def generate_changelog_document(|
|`VersionRuleContext`|class|pub|1616-1623|class VersionRuleContext|
|`_normalize_version_rule_pattern`|fn|priv|1629-1640|def _normalize_version_rule_pattern(pattern: str) -> str|
|`_build_version_file_inventory`|fn|priv|1646-1673|def _build_version_file_inventory(root: Path) -> List[Tup...|
|`_collect_version_files`|fn|priv|1681-1704|def _collect_version_files(root, pattern, *, inventory=None)|
|`_is_version_path_excluded`|fn|priv|1709-1712|def _is_version_path_excluded(relative_path: str) -> bool|
|`_iter_versions_in_text`|fn|priv|1718-1729|def _iter_versions_in_text(text, compiled_regexes)|
|`_read_version_file_text`|fn|priv|1736-1737|def _read_version_file_text(|
|`_prepare_version_rule_contexts`|fn|priv|1761-1762|def _prepare_version_rule_contexts(|
|`_determine_canonical_version`|fn|priv|1805-1812|def _determine_canonical_version(|
|`_parse_semver_tuple`|fn|priv|1865-1871|def _parse_semver_tuple(text: str) -> Optional[Tuple[int,...|
|`_replace_versions_in_text`|fn|priv|1878-1893|def _replace_versions_in_text(text, compiled_regex, repla...|
|`_current_branch_name`|fn|priv|1897-1909|def _current_branch_name()|
|`_ref_exists`|fn|priv|1914-1923|def _ref_exists(ref_name)|
|`_local_branch_exists`|fn|priv|1928-1931|def _local_branch_exists(branch_name)|
|`_remote_branch_exists`|fn|priv|1936-1939|def _remote_branch_exists(branch_name)|
|`_ensure_release_prerequisites`|fn|priv|1943-1992|def _ensure_release_prerequisites()|
|`_bump_semver_version`|fn|priv|1998-2018|def _bump_semver_version(current_version, level)|
|`_run_release_step`|fn|priv|2025-2051|def _run_release_step(level, step_name, action)|
|`_create_release_commit_for_flow`|fn|priv|2056-2061|def _create_release_commit_for_flow(target_version)|
|`_push_branch_with_tags`|fn|priv|2067-2071|def _push_branch_with_tags(branch_name)|
|`_execute_release_flow`|fn|priv|2087-2178|def _execute_release_flow(level, changelog_args=None)|
|`_execute_backup_flow`|fn|priv|2186-2203|def _execute_backup_flow()|
|`_run_release_command`|fn|priv|2209-2224|def _run_release_command(level, changelog_args=None)|
|`_run_backup_command`|fn|priv|2229-2236|def _run_backup_command()|
|`_run_reset_with_help`|fn|priv|2242-2249|def _run_reset_with_help(base_args, extra)|
|`_reject_extra_arguments`|fn|priv|2255-2261|def _reject_extra_arguments(extra, alias)|
|`_parse_release_flags`|fn|priv|2267-2287|def _parse_release_flags(extra, alias)|
|`_prepare_commit_message`|fn|priv|2293-2303|def _prepare_commit_message(extra, alias)|
|`_normalize_conventional_description`|fn|priv|2310-2320|def _normalize_conventional_description(description: str)...|
|`_build_conventional_message`|fn|priv|2329-2350|def _build_conventional_message(kind: str, extra, alias: ...|
|`_run_conventional_commit`|fn|priv|2357-2362|def _run_conventional_commit(kind: str, alias: str, extra)|
|`_execute_commit`|fn|priv|2369-2401|def _execute_commit(message, alias, allow_amend=True)|
|`upgrade_self`|fn|pub|2405-2418|def upgrade_self()|
|`remove_self`|fn|pub|2422-2425|def remove_self()|
|`cmd_aa`|fn|pub|2430-2437|def cmd_aa(extra)|
|`cmd_ra`|fn|pub|2442-2465|def cmd_ra(extra)|
|`cmd_ar`|fn|pub|2470-2486|def cmd_ar(extra)|
|`cmd_br`|fn|pub|2491-2494|def cmd_br(extra)|
|`cmd_bd`|fn|pub|2499-2502|def cmd_bd(extra)|
|`cmd_ck`|fn|pub|2507-2510|def cmd_ck(extra)|
|`_ensure_commit_ready`|fn|priv|2515-2528|def _ensure_commit_ready(alias)|
|`cmd_cm`|fn|pub|2533-2538|def cmd_cm(extra)|
|`cmd_wip`|fn|pub|2543-2555|def cmd_wip(extra)|
|`cmd_release`|fn|pub|2560-2582|def cmd_release(extra)|
|`cmd_new`|fn|pub|2587-2590|def cmd_new(extra)|
|`cmd_refactor`|fn|pub|2595-2598|def cmd_refactor(extra)|
|`cmd_fix`|fn|pub|2603-2606|def cmd_fix(extra)|
|`cmd_change`|fn|pub|2611-2614|def cmd_change(extra)|
|`cmd_implement`|fn|pub|2619-2622|def cmd_implement(extra)|
|`cmd_docs`|fn|pub|2627-2630|def cmd_docs(extra)|
|`cmd_style`|fn|pub|2635-2638|def cmd_style(extra)|
|`cmd_revert`|fn|pub|2643-2646|def cmd_revert(extra)|
|`cmd_misc`|fn|pub|2651-2654|def cmd_misc(extra)|
|`cmd_cover`|fn|pub|2659-2662|def cmd_cover(extra)|
|`cmd_co`|fn|pub|2667-2670|def cmd_co(extra)|
|`cmd_dc`|fn|pub|2675-2684|def cmd_dc(extra)|
|`cmd_dcc`|fn|pub|2689-2692|def cmd_dcc(extra)|
|`cmd_dccc`|fn|pub|2697-2700|def cmd_dccc(extra)|
|`cmd_de`|fn|pub|2705-2708|def cmd_de(extra)|
|`cmd_di`|fn|pub|2713-2716|def cmd_di(extra)|
|`cmd_diyou`|fn|pub|2721-2724|def cmd_diyou(extra)|
|`cmd_dime`|fn|pub|2729-2732|def cmd_dime(extra)|
|`cmd_dwc`|fn|pub|2737-2740|def cmd_dwc(extra)|
|`cmd_dw`|fn|pub|2745-2752|def cmd_dw(extra)|
|`cmd_dwcc`|fn|pub|2757-2760|def cmd_dwcc(extra)|
|`cmd_dcd`|fn|pub|2766-2771|def cmd_dcd(extra)|
|`cmd_dcm`|fn|pub|2777-2782|def cmd_dcm(extra)|
|`cmd_ddm`|fn|pub|2788-2793|def cmd_ddm(extra)|
|`cmd_ed`|fn|pub|2798-2807|def cmd_ed(extra)|
|`cmd_fe`|fn|pub|2812-2815|def cmd_fe(extra)|
|`cmd_feall`|fn|pub|2820-2823|def cmd_feall(extra)|
|`cmd_gp`|fn|pub|2828-2833|def cmd_gp(extra)|
|`cmd_gr`|fn|pub|2838-2843|def cmd_gr(extra)|
|`OVERVIEW_COLOR_RESET`|var|pub|2845||
|`OVERVIEW_COLOR_SECTION_PURPLE`|var|pub|2847||
|`OVERVIEW_COLOR_AHEAD`|var|pub|2849||
|`OVERVIEW_COLOR_BEHIND`|var|pub|2851||
|`OVERVIEW_COLOR_LABEL`|var|pub|2853||
|`OVERVIEW_COLOR_WHITE`|var|pub|2855||
|`OVERVIEW_COLOR_WHITE_BOLD`|var|pub|2857||
|`OVERVIEW_SECTION_TEMPLATE`|var|pub|2859||
|`OVERVIEW_SUBSECTION_TEMPLATE`|var|pub|2861||
|`OVERVIEW_DISTANCE_TEMPLATE`|var|pub|2863||
|`_overview_branch_identifier`|fn|priv|2872-2875|def _overview_branch_identifier(|
|`_overview_work_prefix_color`|fn|priv|2889-2896|def _overview_work_prefix_color(worktree_state: str) -> str|
|`_overview_logical_branch_name`|fn|priv|2904-2908|def _overview_logical_branch_name(|
|`_overview_current_branch_display`|fn|priv|2927-2932|def _overview_current_branch_display(|
|`_overview_ref_is_available`|fn|priv|2954-2963|def _overview_ref_is_available(ref_name: str) -> bool|
|`_overview_ref_latest_subject`|fn|priv|2969-2979|def _overview_ref_latest_subject(ref_name: str) -> str|
|`_overview_discovered_branch_refs`|fn|priv|2984-3007|def _overview_discovered_branch_refs() -> List[str]|
|`_overview_branch_summary_lines`|fn|priv|3026-3037|def _overview_branch_summary_lines(|
|`_overview_relation_state`|fn|priv|3080-3089|def _overview_relation_state(ahead: int, behind: int) -> str|
|`_overview_worktree_state`|fn|priv|3094-3106|def _overview_worktree_state(status_lines=None) -> str|
|`_overview_distance_text`|fn|priv|3112-3120|def _overview_distance_text(is_ahead: bool, count: int) -...|
|`_overview_compare_refs`|fn|priv|3127-3169|def _overview_compare_refs(base_ref: str, target_ref: str...|
|`_overview_ascii_topology_lines`|fn|priv|3190-3201|def _overview_ascii_topology_lines(|
|`_overview_current_branch_state_lines`|fn|priv|3293-3312|def _overview_current_branch_state_lines(current_branch_d...|
|`cmd_o`|fn|pub|3318-3472|def cmd_o(extra)|
|`cmd_str`|fn|pub|3477-3506|def cmd_str(extra)|
|`cmd_l`|fn|pub|3515-3521|def cmd_l(extra)|
|`cmd_lb`|fn|pub|3526-3529|def cmd_lb(extra)|
|`cmd_lg`|fn|pub|3534-3547|def cmd_lg(extra)|
|`cmd_lh`|fn|pub|3552-3555|def cmd_lh(extra)|
|`cmd_ll`|fn|pub|3560-3572|def cmd_ll(extra)|
|`cmd_lm`|fn|pub|3577-3580|def cmd_lm(extra)|
|`cmd_ls`|fn|pub|3586-3589|def cmd_ls(extra)|
|`cmd_lsi`|fn|pub|3600-3617|def cmd_lsi(extra)|
|`cmd_lsa`|fn|pub|3623-3626|def cmd_lsa(extra)|
|`cmd_lt`|fn|pub|3632-3651|def cmd_lt(extra)|
|`cmd_me`|fn|pub|3656-3659|def cmd_me(extra)|
|`cmd_pl`|fn|pub|3664-3667|def cmd_pl(extra)|
|`cmd_pt`|fn|pub|3672-3675|def cmd_pt(extra)|
|`cmd_pu`|fn|pub|3680-3683|def cmd_pu(extra)|
|`cmd_rf`|fn|pub|3688-3691|def cmd_rf(extra)|
|`cmd_rmtg`|fn|pub|3696-3706|def cmd_rmtg(extra)|
|`cmd_rmloc`|fn|pub|3711-3714|def cmd_rmloc(extra)|
|`cmd_rmstg`|fn|pub|3719-3722|def cmd_rmstg(extra)|
|`cmd_rmunt`|fn|pub|3727-3730|def cmd_rmunt(extra)|
|`cmd_rs`|fn|pub|3735-3738|def cmd_rs(extra)|
|`cmd_rssft`|fn|pub|3743-3746|def cmd_rssft(extra)|
|`cmd_rsmix`|fn|pub|3751-3754|def cmd_rsmix(extra)|
|`cmd_rshrd`|fn|pub|3759-3762|def cmd_rshrd(extra)|
|`cmd_rsmrg`|fn|pub|3767-3770|def cmd_rsmrg(extra)|
|`cmd_rskep`|fn|pub|3775-3778|def cmd_rskep(extra)|
|`cmd_st`|fn|pub|3783-3786|def cmd_st(extra)|
|`cmd_tg`|fn|pub|3791-3794|def cmd_tg(extra)|
|`cmd_unstg`|fn|pub|3799-3802|def cmd_unstg(extra)|
|`cmd_wt`|fn|pub|3807-3810|def cmd_wt(extra)|
|`cmd_wtl`|fn|pub|3815-3818|def cmd_wtl(extra)|
|`cmd_wtp`|fn|pub|3823-3826|def cmd_wtp(extra)|
|`cmd_wtr`|fn|pub|3831-3834|def cmd_wtr(extra)|
|`cmd_ver`|fn|pub|3839-3865|def cmd_ver(extra)|
|`cmd_chver`|fn|pub|3870-3953|def cmd_chver(extra)|
|`cmd_major`|fn|pub|3962-3966|def cmd_major(extra)|
|`cmd_minor`|fn|pub|3975-3979|def cmd_minor(extra)|
|`cmd_patch`|fn|pub|3988-3992|def cmd_patch(extra)|
|`cmd_backup`|fn|pub|4000-4010|def cmd_backup(extra)|
|`cmd_changelog`|fn|pub|4020-4057|def cmd_changelog(extra)|
|`COMMANDS`|var|pub|4060||
|`print_command_help`|fn|pub|4147-4154|def print_command_help(name, width=None)|
|`print_all_help`|fn|pub|4158-4192|def print_all_help()|
|`main`|fn|pub|4198-4248|def main(argv=None, *, check_updates: bool = True)|


---

# foresta.py | Python | 1496L | 31 symbols | 7 imports | 261 comments
> Path: `src/git_alias/foresta.py`

## Imports
```
import os
import re
import signal
import subprocess
import sys
from time import localtime, strftime
from typing import Dict, List, Optional, Tuple
```

## Definitions

### fn `def _maxof(x: int, y: int) -> int` `priv` (L130-140)
- @brief Default graph symbol for a tip (branch head).
- @brief Return the greater of two integers.
- @details Performs a single conditional comparison and returns the larger operand.
- @param x {int} First operand.
- @param y {int} Second operand.
- @return {int} max(x, y).
- @satisfies REQ-102

### fn `def _round_down2(i: int) -> int` `priv` (L141-152)
- @brief Round down to the nearest even number.
- @details Preserves negative values; for non-negative values clears the least-significant bit.
- @param i {int} Input integer.
- @return {int} Nearest even number <= i; returns i unchanged if negative.

### fn `def _str_expand(s: str, length: int) -> str` `priv` (L153-165)
- @brief Expand string to at least the given length with spaces.
- @details Appends trailing spaces only when the current length is smaller than the target.
- @param s {str} Input string.
- @param length {int} Minimum required length.
- @return {str} String padded with trailing spaces if shorter than length.

### fn `def _remove_trailing_blanks(vine: list) -> None` `priv` (L166-176)
- @brief Remove trailing None entries from vine array in place.
- @details Pops elements from the tail while the last slot is `None`.
- @param vine {list} Column array of expected parent commit IDs.
- @return None. Mutates vine in place.

### fn `def _trgen(` `priv` (L192-197)
- @brief Build a character translation function for graph control codes.
- @details Maps single-character control codes C/M/O/r/t to the configured graph symbols.
Uses a chained replace pipeline because `str.translate` does not support
multi-codepoint replacement targets.
- @param sym_commit {str} Replacement for 'C' (commit marker).
- @param sym_merge {str} Replacement for 'M' (merge marker).
- @param sym_overpass {str} Replacement for 'O' (overpass marker).
- @param sym_root {str} Replacement for 'r' (root marker).
- @param sym_tip {str} Replacement for 't' (tip marker).
- @return {Callable[[str], str]} Translator closure that maps control strings to rendered symbols.

### fn `def translate(s: str) -> str` (L204-211)
- @brief Translate graph control markers into configured symbol glyphs.
- @details Applies deterministic single-character substitutions for commit, merge,
overpass, root, and tip tokens.
- @param s {str} Graph control-string segment to transform.
- @return {str} Transformed control string with configured symbols.

### fn `def _git_command(args: List[str], cwd: Optional[str] = None) -> str` `priv` (L220-239)
- @brief Execute a git command and return stripped stdout.
- @details Invokes `subprocess.run(..., check=True)` and propagates non-zero exits as `CalledProcessError`.
- @param args {List[str]} Git sub-command and arguments.
- @param cwd {Optional[str]} Working directory override.
- @return {str} Stripped stdout text.
- @throws {subprocess.CalledProcessError} On non-zero git exit.

### fn `def _git_command_output_pipe(` `priv` (L245-246)
- @brief Open a git command subprocess with piped stdout for streaming.
- @details Spawns `git <args>` with text-mode stdout/stderr pipes and optional working-directory override.
- @param args {List[str]} Git sub-command tokens forwarded without transformation.
- @param cwd {Optional[str]} Optional command working directory.
- @return {subprocess.Popen} Process handle with readable stdout pipe.

### fn `def _get_status(repo_path: str, git_dir: str) -> str` `priv` (L262-335)
- @brief Determine working tree dirty flags and mid-flow state indicators.
- @details Checks for unstaged, staged, stash, and untracked changes, then probes git internal state files for rebase/merge/cherry-pick/revert/bisect.
- @param repo_path {str} Path to .git directory (or gitdir for worktrees).
- @param git_dir {str} GIT_DIR value used for git commands.
- @return {str} Status string like " *+$%|REBASE-i" or empty.
- @satisfies REQ-106, REQ-107

### fn `def _get_next_pick(lines: List[str], start: int) -> Optional[str]` `priv` (L341-357)
- @brief Parse rebase-todo file lines to find the next pick target.
- @details Skips comments/blank lines and returns the second token from the first actionable row.
- @param lines {List[str]} Lines from git-rebase-todo.
- @param start {int} Starting line index.
- @return {Optional[str]} Short SHA of next pick target, or None.

### fn `def _get_refs(` `priv` (L364-365)
- @brief Build a SHA-to-ref mapping from repository references and HEAD state.
- @details Parses `git show-ref`, resolves annotated tags to target commits, and conditionally
augments the map with active rebase markers (`rebase/next`, `rebase/onto`, `rebase/new`).
- @param show_rebase {bool} Enables inclusion of rebase markers when true.
- @return {Dict[str, List[str]]} Map from full commit SHA to rendered ref labels.
- @satisfies REQ-108

### fn `def _vine_branch(` `priv` (L470-481)
- @brief Draw branch fan topology when a commit SHA appears in multiple vine columns.
- @details Scans vine slots for duplicate commit references, emits a branch fan line when needed,
and preserves branch-color continuity via `_vis_post`.
- @param vine {list} Mutable vine columns storing expected parent SHAs.
- @param rev {str} Current commit SHA.
- @param color {Dict[str,str]} ANSI color token map.
- @param hash_width {int} Width of abbreviated hash column.
- @param date_width {int} Width of formatted date column.
- @param graph_margin_left {int} Left-side graph margin.
- @param style {int} Active graph style identifier.
- @param reverse_order {bool} Indicates reverse rendering order.
- @param graph_symbol_tr {Callable[[str], str]} Graph control-code translator.
- @param branch_colors_now {List[str]} Current branch color assignments.
- @param branch_colors_ref {List[str]} Allowed branch color palette.
- @return {Optional[str]} Rendered branch line or None if no duplicate SHA columns exist.
- @satisfies REQ-109

### fn `def _vine_commit(vine: list, rev: str, parents: List[str]) -> str` `priv` (L522-571)
- @brief Draw commit node on the vine graph.
- @details Places the commit at its vine position or allocates a new tip slot. Differentiates commit types: 'C' regular, 'r' root (no parents), M' merge (multiple parents), 't' tip (new branch head).
- @param vine {list} Column array of expected parent IDs.
- @param rev {str} Current commit SHA.
- @param parents {List[str]} Parent commit SHAs.
- @return {str} Control string representing the commit line.
- @satisfies REQ-109

### fn `def _vine_merge(` `priv` (L590-603)
- @brief Draw merge fan topology and update vine state across commit parents.
- @details For single-parent commits the vine is only advanced; for merge commits a fan visualization
is generated, using lookahead heuristics to preserve adjacent branch continuity.
- @param vine {list} Mutable vine columns storing expected parent SHAs.
- @param rev {str} Current commit SHA.
- @param next_sha {List[Optional[str]]} Lookahead SHAs used for branch-placement heuristics.
- @param parents {list} Mutable parent SHA list for merge fan rendering.
- @param color {Dict[str,str]} ANSI color token map.
- @param hash_width {int} Width of abbreviated hash column.
- @param date_width {int} Width of formatted date column.
- @param graph_margin_left {int} Left-side graph margin.
- @param style {int} Active graph style identifier.
- @param reverse_order {bool} Indicates reverse rendering order.
- @param graph_symbol_tr {Callable[[str], str]} Graph control-code translator.
- @param branch_colors_now {List[str]} Current branch color assignments.
- @param branch_colors_ref {List[str]} Allowed branch color palette.
- @return {Optional[str]} Rendered merge line or None when no explicit merge line is emitted.
- @satisfies REQ-109

### fn `def _vis_commit(s: str, f: Optional[str] = None) -> str` `priv` (L738-751)
- @brief Post-process commit control string.
- @details Trims trailing spaces and appends the optional suffix segment when provided.
- @param s {str} Raw control string from vine_commit.
- @param f {Optional[str]} Optional suffix.
- @return {str} Trimmed control string.

### fn `def _vis_fan(s: str, fan_type: str) -> str` `priv` (L752-827)
- @brief Transform control string for branch/merge fan visualization.
- @details Converts 's' fan markers into directional edge characters, resolves overpass sequences, and performs left/right edge transforms.
- @param s {str} Raw control string.
- @param fan_type {str} Either "branch" or "merge".
- @return {str} Transformed control string.

### fn `def _overpass_replace(m)` `priv` (L783-785)
- @brief Expand matched overpass control segments to contiguous overpass markers.
- @details Converts regex match groups for `O[DO]+O` into equal-length `O...O` spans.
- @param m {re.Match[str]} Regex match object for the overpass control segment.
- @return {str} Replacement string composed only of `O` markers.

### fn `def _vis_fan2L(left: str) -> str` `priv` (L828-840)
- @brief Transform left side of fan visualization.
- @details Converts leading `s` to `e` and remaining `s` markers to `f`.
- @param left {str} Left portion of control string.
- @return {str} Transformed left portion.

### fn `def _vis_fan2R(right: str) -> str` `priv` (L841-853)
- @brief Transform right side of fan visualization.
- @details Converts trailing `s` to `g` and remaining `s` markers to `f`.
- @param right {str} Right portion of control string.
- @return {str} Transformed right portion.

### fn `def _vis_xfrm(` `priv` (L886-891)
- @brief Convert graph control-string tokens into styled Unicode output.
- @details Applies optional space-filling after commit markers, reverse-order fan transformation,
style-specific Unicode translation, and final graph-symbol replacement.
- @param s {str} Graph control-string line.
- @param spc {bool} Enables post-commit-space fill when true.
- @param style {int} Style selector (`1`, `2`, `10`, `15`).
- @param reverse_order {bool} Enables reverse fan transformation when true.
- @param graph_symbol_tr {Callable[[str], str]} Control-to-symbol translator function.
- @return {str} Rendered graph line with selected style and symbols.
- @satisfies REQ-101

### fn `def _vis_post(` `priv` (L928-936)
- @brief Post-process graph control strings with style transform and branch coloring.
- @details Applies `_vis_xfrm` to graph/control suffix segments, preserves ANSI spans, and injects
branch-color-specific commit glyph coloring based on tracked branch state.
- @param s {str} Primary graph control string.
- @param f {Optional[str]} Optional suffix containing refs/message text.
- @param style {int} Active graph style identifier.
- @param reverse_order {bool} Indicates reverse rendering order.
- @param graph_symbol_tr {Callable[[str], str]} Graph control-code translator.
- @param color {Dict[str,str]} ANSI color token map (empty in no-color mode).
- @param branch_colors_now {List[str]} Current branch color assignments.
- @param branch_colors_ref {List[str]} Allowed branch color palette.
- @return {str} Final rendered line with style transformation and ANSI colors.

### fn `def _update_branch_colors(` `priv` (L1005-1008)
- @brief Update branch-color assignments using current vine control-string content.
- @details Scans even vine slots for branch indicators (`e`, `f`, `g`, `t`) and assigns colors
from the reference palette while avoiding immediate neighbor color collisions.
- @param s {str} Vine control string for the current rendered line.
- @param branch_colors_now {List[str]} Mutable current branch-color assignments.
- @param branch_colors_ref {List[str]} Fixed branch-color palette.
- @return None. Mutates `branch_colors_now` in place.
- @satisfies REQ-110

### fn `def _get_line_block(` `priv` (L1052-1053)
- @brief Read one commit-log line plus bounded lookahead for subvine processing.
- @details Maintains a rolling prefetch buffer and returns the current line with up to
`max_count - 1` subsequent entries for merge lookahead heuristics.
- @param lines_iter {Iterator[str]} Iterator yielding raw git-log lines.
- @param buffer {list} Mutable rolling prefetch buffer.
- @param max_count {int} Maximum total items in returned block.
- @return {Tuple[Optional[str], List[Optional[str]]]} Current line and lookahead list.

### class `class _ReverseOutput` `priv` (L1075-1114)
- @brief Buffer that collects output and writes it in reverse line order.
- @details Used when --reverse is specified. Accumulates all printed output and flushes in reverse order on close().
- fn `def __init__(self, stream)` `priv` (L1082-1089)
  - @brief Buffer that collects output and writes it in reverse line order.
  - @brief Initialize reverse output buffer.
  - @details Used when --reverse is specified. Accumulates all printed output
and flushes in reverse order on close().
  - @param stream Output stream to write reversed content to.
- fn `def write(self, text: str) -> None` (L1090-1096)
  - @brief Accumulate text for later reversed output.
  - @param text {str} Text to buffer.
- fn `def flush(self) -> None` (L1097-1102)
  - @brief No-op flush for buffered mode.
- fn `def close(self) -> None` (L1103-1114)
  - @brief Write buffered content in reverse line order to the stream.

### fn `def _process(` `priv` (L1143-1161)
- @brief Stream git log commits, render vine graph lines, and emit final output.
- @details Opens a `git log` pipe, iterates commits, executes vine_branch/vine_commit/vine_merge
rendering stages, and writes normalized lines to the configured output stream.
- @param refs {Dict[str,List[str]]} SHA-to-reference mapping.
- @param status {str} Working-tree status token set.
- @param show_status {bool} Enables status markers in HEAD decorations.
- @param pretty_fmt {str} Git pretty-format expression.
- @param argv {List[str]} Additional passthrough arguments for `git log`.
- @param color {Dict[str,str]} ANSI color token map.
- @param hash_width {int} Width of hash output column.
- @param date_width {int} Width of date output column.
- @param date_format {str} Datetime format string for commit dates.
- @param graph_margin_left {int} Left graph margin width.
- @param graph_margin_right {int} Right graph margin width.
- @param subvine_depth {int} Maximum subvine lookahead depth.
- @param style {int} Active graph style identifier.
- @param reverse_order {bool} Enables reverse commit-output ordering.
- @param graph_symbol_tr {Callable[[str], str]} Graph symbol translator function.
- @param output_stream {IO[str]} Destination stream for rendered lines.
- @param branch_colors_now {List[str]} Mutable current branch-color state.
- @param branch_colors_ref {List[str]} Fixed branch-color palette.
- @return None.
- @satisfies REQ-099, REQ-100, REQ-109

### fn `def _lines_iter()` `priv` (L1178-1182)
- @brief Yield streamed git-log lines from subprocess stdout.
- @details Wraps `proc.stdout` iteration to keep generator creation local to `_process`.
- @return {Iterator[str]} Iterator emitting raw log lines including trailing newlines.

### fn `def run(extra_args: Optional[List[str]] = None) -> None` (L1329-1496)
- @brief Execute the tree visualization command.
- @details Parses command-line options, configures the visualization engine, and runs the main processing loop. Unrecognized options are passed through to git log.
- @param extra_args {Optional[List[str]]} CLI arguments from the dispatcher.
- @return None. Output written to stdout.
- @satisfies REQ-098, REQ-099, REQ-104, REQ-111

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`_maxof`|fn|priv|130-140|def _maxof(x: int, y: int) -> int|
|`_round_down2`|fn|priv|141-152|def _round_down2(i: int) -> int|
|`_str_expand`|fn|priv|153-165|def _str_expand(s: str, length: int) -> str|
|`_remove_trailing_blanks`|fn|priv|166-176|def _remove_trailing_blanks(vine: list) -> None|
|`_trgen`|fn|priv|192-197|def _trgen(|
|`translate`|fn|pub|204-211|def translate(s: str) -> str|
|`_git_command`|fn|priv|220-239|def _git_command(args: List[str], cwd: Optional[str] = No...|
|`_git_command_output_pipe`|fn|priv|245-246|def _git_command_output_pipe(|
|`_get_status`|fn|priv|262-335|def _get_status(repo_path: str, git_dir: str) -> str|
|`_get_next_pick`|fn|priv|341-357|def _get_next_pick(lines: List[str], start: int) -> Optio...|
|`_get_refs`|fn|priv|364-365|def _get_refs(|
|`_vine_branch`|fn|priv|470-481|def _vine_branch(|
|`_vine_commit`|fn|priv|522-571|def _vine_commit(vine: list, rev: str, parents: List[str]...|
|`_vine_merge`|fn|priv|590-603|def _vine_merge(|
|`_vis_commit`|fn|priv|738-751|def _vis_commit(s: str, f: Optional[str] = None) -> str|
|`_vis_fan`|fn|priv|752-827|def _vis_fan(s: str, fan_type: str) -> str|
|`_overpass_replace`|fn|priv|783-785|def _overpass_replace(m)|
|`_vis_fan2L`|fn|priv|828-840|def _vis_fan2L(left: str) -> str|
|`_vis_fan2R`|fn|priv|841-853|def _vis_fan2R(right: str) -> str|
|`_vis_xfrm`|fn|priv|886-891|def _vis_xfrm(|
|`_vis_post`|fn|priv|928-936|def _vis_post(|
|`_update_branch_colors`|fn|priv|1005-1008|def _update_branch_colors(|
|`_get_line_block`|fn|priv|1052-1053|def _get_line_block(|
|`_ReverseOutput`|class|priv|1075-1114|class _ReverseOutput|
|`_ReverseOutput.__init__`|fn|priv|1082-1089|def __init__(self, stream)|
|`_ReverseOutput.write`|fn|pub|1090-1096|def write(self, text: str) -> None|
|`_ReverseOutput.flush`|fn|pub|1097-1102|def flush(self) -> None|
|`_ReverseOutput.close`|fn|pub|1103-1114|def close(self) -> None|
|`_process`|fn|priv|1143-1161|def _process(|
|`_lines_iter`|fn|priv|1178-1182|def _lines_iter()|
|`run`|fn|pub|1329-1496|def run(extra_args: Optional[List[str]] = None) -> None|

