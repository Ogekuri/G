# Files Structure
```
.
└── src
    └── git_alias
        ├── __init__.py
        ├── __main__.py
        └── core.py
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

# core.py | Python | 3651L | 211 symbols | 16 imports | 934 comments
> Path: `src/git_alias/core.py`

## Imports
```
import argparse
import importlib
import json
import os
import re
import shlex
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
```

## Definitions

- var `CONFIG_FILENAME = ".g.conf"` (L27)
- Brief: Constant `CONFIG_FILENAME` used by CLI runtime paths and policies.
- var `GITHUB_LATEST_RELEASE_API = "https://api.github.com/repos/Ogekuri/G/releases/latest"` (L31)
- Brief: Constant `GITHUB_LATEST_RELEASE_API` used by CLI runtime paths and policies.
- var `VERSION_CHECK_CACHE_FILE = Path(tempfile.gettempdir()) / ".g_version_check_cache.json"` (L34)
- Brief: Constant `VERSION_CHECK_CACHE_FILE` used by CLI runtime paths and policies.
- var `VERSION_CHECK_TTL_HOURS = 6` (L37)
- Brief: Constant `VERSION_CHECK_TTL_HOURS` used by CLI runtime paths and policies.
- var `DEFAULT_VER_RULES = [` (L41)
- Brief: Constant `DEFAULT_VER_RULES` used by CLI runtime paths and policies.
- var `VERSION_CLEANUP_REGEXES = [` (L48)
- Brief: Constant `VERSION_CLEANUP_REGEXES` used by CLI runtime paths and policies.
- var `VERSION_CLEANUP_PATTERNS = [re.compile(pattern) for pattern in VERSION_CLEANUP_REGEXES]` (L59)
- Brief: Constant `VERSION_CLEANUP_PATTERNS` used by CLI runtime paths and policies.
- var `DEFAULT_CONFIG = {` (L63)
- Brief: Constant `DEFAULT_CONFIG` used by CLI runtime paths and policies.
- var `CONFIG = DEFAULT_CONFIG.copy()` (L78)
- Brief: Constant `CONFIG` used by CLI runtime paths and policies.
- var `BRANCH_KEYS = ("master", "develop", "work")` (L81)
- Brief: Constant `BRANCH_KEYS` used by CLI runtime paths and policies.
- var `MANAGEMENT_HELP = [` (L84)
- Brief: Constant `MANAGEMENT_HELP` used by CLI runtime paths and policies.
### fn `def get_config_value(name)` (L98-101)
- Brief: Execute `get_config_value` runtime logic for Git-Alias CLI.
- Details: Executes `get_config_value` using deterministic CLI control-flow and explicit error propagation.
- Param: name Input parameter consumed by `get_config_value`.
- Return: Result emitted by `get_config_value` according to command contract.

### fn `def get_branch(name)` (L106-111)
- Brief: Execute `get_branch` runtime logic for Git-Alias CLI.
- Details: Executes `get_branch` using deterministic CLI control-flow and explicit error propagation.
- Param: name Input parameter consumed by `get_branch`.
- Return: Result emitted by `get_branch` according to command contract.

### fn `def get_editor()` (L115-118)
- Brief: Execute `get_editor` runtime logic for Git-Alias CLI.
- Details: Executes `get_editor` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `get_editor` according to command contract.

### fn `def _load_config_rules(key, fallback)` `priv` (L124-149)
- Brief: Execute `_load_config_rules` runtime logic for Git-Alias CLI.
- Details: Executes `_load_config_rules` using deterministic CLI control-flow and explicit error propagation.
- Param: key Input parameter consumed by `_load_config_rules`.
- Param: fallback Input parameter consumed by `_load_config_rules`.
- Return: Result emitted by `_load_config_rules` according to command contract.

### fn `def get_version_rules()` (L153-156)
- Brief: Execute `get_version_rules` runtime logic for Git-Alias CLI.
- Details: Executes `get_version_rules` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `get_version_rules` according to command contract.

### fn `def get_cli_version()` (L160-171)
- Brief: Execute `get_cli_version` runtime logic for Git-Alias CLI.
- Details: Executes `get_cli_version` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `get_cli_version` according to command contract.

### fn `def _normalize_semver_text(text: str) -> str` `priv` (L176-182)
- Brief: Execute `_normalize_semver_text` runtime logic for Git-Alias CLI.
- Details: Executes `_normalize_semver_text` using deterministic CLI control-flow and explicit error propagation.
- Param: text Input parameter consumed by `_normalize_semver_text`.
- Return: Result emitted by `_normalize_semver_text` according to command contract.

### fn `def check_for_newer_version(timeout_seconds: float = 1.0) -> None` (L187-271)
- Brief: Execute `check_for_newer_version` runtime logic for Git-Alias CLI.
- Details: Executes `check_for_newer_version` using deterministic CLI control-flow and explicit error propagation.
- Param: timeout_seconds Input parameter consumed by `check_for_newer_version`.
- Return: Result emitted by `check_for_newer_version` according to command contract.

### fn `def get_git_root()` (L275-290)
- Brief: Execute `get_git_root` runtime logic for Git-Alias CLI.
- Details: Executes `get_git_root` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `get_git_root` according to command contract.

### fn `def get_config_path(root=None)` (L295-299)
- Brief: Execute `get_config_path` runtime logic for Git-Alias CLI.
- Details: Executes `get_config_path` using deterministic CLI control-flow and explicit error propagation.
- Param: root Input parameter consumed by `get_config_path`.
- Return: Result emitted by `get_config_path` according to command contract.

### fn `def load_cli_config(root=None)` (L304-338)
- Brief: Execute `load_cli_config` runtime logic for Git-Alias CLI.
- Details: Executes `load_cli_config` using deterministic CLI control-flow and explicit error propagation.
- Param: root Input parameter consumed by `load_cli_config`.
- Return: Result emitted by `load_cli_config` according to command contract.

### fn `def write_default_config(root=None)` (L343-350)
- Brief: Execute `write_default_config` runtime logic for Git-Alias CLI.
- Details: Executes `write_default_config` using deterministic CLI control-flow and explicit error propagation.
- Param: root Input parameter consumed by `write_default_config`.
- Return: Result emitted by `write_default_config` according to command contract.

### fn `def _editor_base_command()` `priv` (L354-368)
- Brief: Execute `_editor_base_command` runtime logic for Git-Alias CLI.
- Details: Executes `_editor_base_command` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_editor_base_command` according to command contract.

### fn `def run_editor_command(args)` (L373-375)
- Brief: Execute `run_editor_command` runtime logic for Git-Alias CLI.
- Details: Executes `run_editor_command` using deterministic CLI control-flow and explicit error propagation.
- Param: args Input parameter consumed by `run_editor_command`.
- Return: Result emitted by `run_editor_command` according to command contract.

- var `HELP_TEXTS = {` (L378)
- Brief: Constant `HELP_TEXTS` used by CLI runtime paths and policies.
- var `RESET_HELP_COMMANDS = {"rs", "rshrd", "rskep", "rsmix", "rsmrg", "rssft"}` (L538)
- Brief: Constant `RESET_HELP_COMMANDS` used by CLI runtime paths and policies.
### fn `def _to_args(extra)` `priv` (L545-548)
- Brief: Execute `_to_args` runtime logic for Git-Alias CLI.
- Details: Executes `_to_args` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `_to_args`.
- Return: Result emitted by `_to_args` according to command contract.

### class `class CommandExecutionError(RuntimeError)` : RuntimeError (L550-591)
- Brief: Class `CommandExecutionError` models a typed runtime container/error boundary.
- Brief: Execute `__init__` runtime logic for Git-Alias CLI.
- Param: self Input parameter consumed by `__init__`.
- Param: exc Input parameter consumed by `__init__`.
- fn `def __init__(self, exc: subprocess.CalledProcessError)` `priv` (L555-562)
  - Brief: Execute `__init__` runtime logic for Git-Alias CLI.
  - Param: self Input parameter consumed by `__init__`.
  - Param: exc Input parameter consumed by `__init__`.
  - Return: Result emitted by `__init__` according to command contract.
- fn `def _format_message(self) -> str` `priv` (L566-576)
  - Brief: Execute `_format_message` runtime logic for Git-Alias CLI.
  - Param: self Input parameter consumed by `_format_message`.
  - Return: Result emitted by `_format_message` according to command contract.
- fn `def _decode_stream(data) -> str` `priv` (L581-591)
  - Brief: Execute `_decode_stream` runtime logic for Git-Alias CLI.
  - Param: data Input parameter consumed by `_decode_stream`.
  - Return: Result emitted by `_decode_stream` according to command contract.

### fn `def _run_checked(*popenargs, **kwargs)` `priv` (L597-604)
- Brief: Execute `_run_checked` runtime logic for Git-Alias CLI.
- Details: Executes `_run_checked` using deterministic CLI control-flow and explicit error propagation.
- Param: *popenargs Input parameter consumed by `_run_checked`.
- Param: **kwargs Input parameter consumed by `_run_checked`.
- Return: Result emitted by `_run_checked` according to command contract.

### class `class VersionDetectionError(RuntimeError)` : RuntimeError (L606-609)
- Brief: Class `VersionDetectionError` models a typed runtime container/error boundary.

### class `class ReleaseError(RuntimeError)` : RuntimeError (L611-614)
- Brief: Class `ReleaseError` models a typed runtime container/error boundary.

### fn `def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)` (L622-626)
- Brief: Execute `run_git_cmd` runtime logic for Git-Alias CLI.
- Details: Executes `run_git_cmd` using deterministic CLI control-flow and explicit error propagation.
- Param: base_args Input parameter consumed by `run_git_cmd`.
- Param: extra Input parameter consumed by `run_git_cmd`.
- Param: cwd Input parameter consumed by `run_git_cmd`.
- Param: **kwargs Input parameter consumed by `run_git_cmd`.
- Return: Result emitted by `run_git_cmd` according to command contract.

### fn `def capture_git_output(base_args, cwd=None)` (L632-636)
- Brief: Execute `capture_git_output` runtime logic for Git-Alias CLI.
- Details: Executes `capture_git_output` using deterministic CLI control-flow and explicit error propagation.
- Param: base_args Input parameter consumed by `capture_git_output`.
- Param: cwd Input parameter consumed by `capture_git_output`.
- Return: Result emitted by `capture_git_output` according to command contract.

### fn `def run_command(cmd, cwd=None)` (L642-645)
- Brief: Execute `run_command` runtime logic for Git-Alias CLI.
- Details: Executes `run_command` using deterministic CLI control-flow and explicit error propagation.
- Param: cmd Input parameter consumed by `run_command`.
- Param: cwd Input parameter consumed by `run_command`.
- Return: Result emitted by `run_command` according to command contract.

### fn `def run_git_text(args, cwd=None, check=True)` (L652-669)
- Brief: Execute `run_git_text` runtime logic for Git-Alias CLI.
- Details: Executes `run_git_text` using deterministic CLI control-flow and explicit error propagation.
- Param: args Input parameter consumed by `run_git_text`.
- Param: cwd Input parameter consumed by `run_git_text`.
- Param: check Input parameter consumed by `run_git_text`.
- Return: Result emitted by `run_git_text` according to command contract.

### fn `def run_shell(command, cwd=None)` (L675-678)
- Brief: Execute `run_shell` runtime logic for Git-Alias CLI.
- Details: Executes `run_shell` using deterministic CLI control-flow and explicit error propagation.
- Param: command Input parameter consumed by `run_shell`.
- Param: cwd Input parameter consumed by `run_shell`.
- Return: Result emitted by `run_shell` according to command contract.

### fn `def _git_status_lines()` `priv` (L682-694)
- Brief: Execute `_git_status_lines` runtime logic for Git-Alias CLI.
- Details: Executes `_git_status_lines` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_git_status_lines` according to command contract.

### fn `def has_unstaged_changes(status_lines=None)` (L699-710)
- Brief: Execute `has_unstaged_changes` runtime logic for Git-Alias CLI.
- Details: Executes `has_unstaged_changes` using deterministic CLI control-flow and explicit error propagation.
- Param: status_lines Input parameter consumed by `has_unstaged_changes`.
- Return: Result emitted by `has_unstaged_changes` according to command contract.

### fn `def has_staged_changes(status_lines=None)` (L715-724)
- Brief: Execute `has_staged_changes` runtime logic for Git-Alias CLI.
- Details: Executes `has_staged_changes` using deterministic CLI control-flow and explicit error propagation.
- Param: status_lines Input parameter consumed by `has_staged_changes`.
- Return: Result emitted by `has_staged_changes` according to command contract.

- var `WIP_MESSAGE_RE = re.compile(r"^wip: work in progress\.$")` (L730)
- Brief: Constant `WIP_MESSAGE_RE` used by CLI runtime paths and policies.
### fn `def _refresh_remote_refs()` `priv` (L736-747)
- Brief: Execute `_refresh_remote_refs` runtime logic for Git-Alias CLI.
- Details: Executes `_refresh_remote_refs` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_refresh_remote_refs` according to command contract.

### fn `def _branch_remote_divergence(branch_key, remote="origin")` `priv` (L753-771)
- Brief: Execute `_branch_remote_divergence` runtime logic for Git-Alias CLI.
- Details: Executes `_branch_remote_divergence` using deterministic CLI control-flow and explicit error propagation.
- Param: branch_key Input parameter consumed by `_branch_remote_divergence`.
- Param: remote Input parameter consumed by `_branch_remote_divergence`.
- Return: Result emitted by `_branch_remote_divergence` according to command contract.

### fn `def has_remote_branch_updates(branch_key, remote="origin")` (L777-781)
- Brief: Execute `has_remote_branch_updates` runtime logic for Git-Alias CLI.
- Details: Executes `has_remote_branch_updates` using deterministic CLI control-flow and explicit error propagation.
- Param: branch_key Input parameter consumed by `has_remote_branch_updates`.
- Param: remote Input parameter consumed by `has_remote_branch_updates`.
- Return: Result emitted by `has_remote_branch_updates` according to command contract.

### fn `def has_remote_develop_updates()` (L785-788)
- Brief: Execute `has_remote_develop_updates` runtime logic for Git-Alias CLI.
- Details: Executes `has_remote_develop_updates` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `has_remote_develop_updates` according to command contract.

### fn `def has_remote_master_updates()` (L792-795)
- Brief: Execute `has_remote_master_updates` runtime logic for Git-Alias CLI.
- Details: Executes `has_remote_master_updates` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `has_remote_master_updates` according to command contract.

### fn `def _head_commit_message()` `priv` (L799-805)
- Brief: Execute `_head_commit_message` runtime logic for Git-Alias CLI.
- Details: Executes `_head_commit_message` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_head_commit_message` according to command contract.

### fn `def _head_commit_hash()` `priv` (L809-815)
- Brief: Execute `_head_commit_hash` runtime logic for Git-Alias CLI.
- Details: Executes `_head_commit_hash` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_head_commit_hash` according to command contract.

### fn `def _commit_exists_in_branch(commit_hash, branch_name)` `priv` (L821-833)
- Brief: Execute `_commit_exists_in_branch` runtime logic for Git-Alias CLI.
- Details: Executes `_commit_exists_in_branch` using deterministic CLI control-flow and explicit error propagation.
- Param: commit_hash Input parameter consumed by `_commit_exists_in_branch`.
- Param: branch_name Input parameter consumed by `_commit_exists_in_branch`.
- Return: Result emitted by `_commit_exists_in_branch` according to command contract.

### fn `def _should_amend_existing_commit()` `priv` (L837-852)
- Brief: Execute `_should_amend_existing_commit` runtime logic for Git-Alias CLI.
- Details: Executes `_should_amend_existing_commit` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_should_amend_existing_commit` according to command contract.

### fn `def is_inside_git_repo()` (L856-863)
- Brief: Execute `is_inside_git_repo` runtime logic for Git-Alias CLI.
- Details: Executes `is_inside_git_repo` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `is_inside_git_repo` according to command contract.

### class `class TagInfo` (L868-876)
- Brief: Class `TagInfo` models a typed runtime container/error boundary.
- Brief: Store raw tag name including `v` prefix when present.
- Brief: Store ISO date string used for changelog section headers.
- Details: Encapsulates tag identity, tag date, and resolved Git object identifier for changelog assembly.

- var `DELIM = "\x1f"` (L879)
- Brief: Constant `DELIM` used by CLI runtime paths and policies.
- var `RECORD = "\x1e"` (L882)
- Brief: Constant `RECORD` used by CLI runtime paths and policies.
- var `SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")` (L898)
- Brief: Constant `SEMVER_RE` used by CLI runtime paths and policies.
- var `SECTION_EMOJI = {` (L901)
- Brief: Constant `SECTION_EMOJI` used by CLI runtime paths and policies.
### fn `def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[int, int, int]]` `priv` (L918-921)
- Brief: Execute `_tag_semver_tuple` runtime logic for Git-Alias CLI.
- Details: Executes `_tag_semver_tuple` using deterministic CLI control-flow and explicit error propagation.
- Param: tag_name Input parameter consumed by `_tag_semver_tuple`.
- Return: Result emitted by `_tag_semver_tuple` according to command contract.

### fn `def _latest_supported_tag_name(tags: List[TagInfo]) -> Optional[str]` `priv` (L926-929)
- Brief: Execute `_latest_supported_tag_name` runtime logic for Git-Alias CLI.
- Details: Executes `_latest_supported_tag_name` using deterministic CLI control-flow and explicit error propagation.
- Param: tags Input parameter consumed by `_latest_supported_tag_name`.
- Return: Result emitted by `_latest_supported_tag_name` according to command contract.

### fn `def _is_minor_release_tag(tag_name: str) -> bool` `priv` (L937-944)
- Brief: Predicate: tag is a minor release.
- Details: Returns `True` when `tag_name` is a semver tag where `patch==0` AND `(major>=1 OR minor>=1)`,
i.e. version `>=0.1.0` with no patch component.
Patch releases (`patch>0`) and pre-0.1.0 tags (`0.0.x`) return `False`.
- Param: tag_name Semver tag string, optionally prefixed with `v` (e.g. `v0.1.0`, `0.2.0`).
- Return: `True` iff tag represents a minor release; `False` otherwise.
- Satisfies: REQ-018, REQ-040

### fn `def _latest_patch_tag_after(all_tags: List[TagInfo], last_minor: Optional[TagInfo]) -> Optional[TagInfo]` `priv` (L953-962)
- Brief: Locate the chronologically latest patch tag after a given minor release.
- Details: Scans `all_tags` (sorted chronologically, ascending) for tags that are NOT minor releases
and appear after `last_minor` in the list. When `last_minor` is `None`, scans all tags.
Returns the last qualifying `TagInfo` (most recent), or `None` if no patch exists.
- Param: all_tags Full list of `TagInfo` sorted by date ascending (from `list_tags_sorted_by_date`).
- Param: last_minor The last minor-release `TagInfo` to anchor the search; `None` means no minor exists.
- Return: Most recent `TagInfo` that is not a minor release and appears after `last_minor`, or `None`.
- Satisfies: REQ-040

### fn `def list_tags_sorted_by_date(repo_root: Path, merged_ref: Optional[str] = None) -> List[TagInfo]` (L968-988)
- Brief: Execute `list_tags_sorted_by_date` runtime logic for Git-Alias CLI.
- Details: Executes `list_tags_sorted_by_date` using deterministic CLI control-flow and explicit error propagation.
- Param: repo_root Input parameter consumed by `list_tags_sorted_by_date`.
- Param: merged_ref Input parameter consumed by `list_tags_sorted_by_date`.
- Return: Result emitted by `list_tags_sorted_by_date` according to command contract.

### fn `def git_log_subjects(repo_root: Path, rev_range: str) -> List[str]` (L995-1006)
- Brief: Execute `git_log_subjects` runtime logic for Git-Alias CLI.
- Details: Executes `git_log_subjects` using deterministic CLI control-flow and explicit error propagation.
Reads full commit messages (subject + body) to preserve multiline conventional descriptions.
- Param: repo_root Input parameter consumed by `git_log_subjects`.
- Param: rev_range Input parameter consumed by `git_log_subjects`.
- Return: Result emitted by `git_log_subjects` according to command contract.

### fn `def parse_conventional_commit(message: str) -> Optional[Tuple[str, Optional[str], bool, str]]` (L1012-1024)
- Brief: Execute `parse_conventional_commit` runtime logic for Git-Alias CLI.
- Details: Parses a conventional-commit header with optional scope and optional breaking marker (`!`),
then returns extracted type/scope/breaking/description fields for changelog rendering.
- Param: message Raw commit message text (subject and optional body).
- Return: Tuple `(type, scope, breaking, description)` when message is parseable; otherwise `None`.

### fn `def _format_changelog_description(desc: str) -> List[str]` `priv` (L1031-1042)
- Brief: Execute `_format_changelog_description` runtime logic for Git-Alias CLI.
- Details: Normalizes a commit description for markdown list rendering while preserving logical lines.
Removes `Co-authored-by:` trailer lines, drops empty lines, and strips leading markdown-list
markers from continuation lines so multiline descriptions can be rendered as nested bullets.
- Param: desc Parsed commit description.
- Return: Ordered non-empty description lines ready for markdown rendering.

### fn `def categorize_commit(subject: str) -> Tuple[Optional[str], str]` (L1050-1079)
- Brief: Execute `categorize_commit` runtime logic for Git-Alias CLI.
- Details: Parses a conventional commit message and maps it to a changelog section and formatted entry line.
Entry format: `- <description> *(<scope>)*` when scope is present; `- <description>` otherwise.
Multiline descriptions are rendered as consecutive indented sub-bullets under the commit line.
When the breaking marker is present, the first description line is prefixed with `BREAKING CHANGE: `.
- Param: subject Conventional commit message string.
- Return: Tuple `(section, line)`: `section` is the changelog section name or `None` if type is unmapped or ignored; `line` is the formatted entry string or `""` when section is `None`.

### fn `def _extract_release_version(subject: str) -> Optional[str]` `priv` (L1084-1094)
- Brief: Execute `_extract_release_version` runtime logic for Git-Alias CLI.
- Details: Executes `_extract_release_version` using deterministic CLI control-flow and explicit error propagation.
- Param: subject Input parameter consumed by `_extract_release_version`.
- Return: Result emitted by `_extract_release_version` according to command contract.

### fn `def _is_release_marker_commit(subject: str) -> bool` `priv` (L1099-1102)
- Brief: Execute `_is_release_marker_commit` runtime logic for Git-Alias CLI.
- Details: Executes `_is_release_marker_commit` using deterministic CLI control-flow and explicit error propagation.
- Param: subject Input parameter consumed by `_is_release_marker_commit`.
- Return: Result emitted by `_is_release_marker_commit` according to command contract.

### fn `def generate_section_for_range(repo_root: Path, title: str, date_s: str, rev_range: str, expected_version: Optional[str] = None) -> Optional[str]` (L1111-1149)
- Brief: Execute `generate_section_for_range` runtime logic for Git-Alias CLI.
- Details: Executes `generate_section_for_range` using deterministic CLI control-flow and explicit error propagation.
- Param: repo_root Input parameter consumed by `generate_section_for_range`.
- Param: title Input parameter consumed by `generate_section_for_range`.
- Param: date_s Input parameter consumed by `generate_section_for_range`.
- Param: rev_range Input parameter consumed by `generate_section_for_range`.
- Param: expected_version Input parameter consumed by `generate_section_for_range`.
- Return: Result emitted by `generate_section_for_range` according to command contract.

### fn `def _get_remote_name_for_branch(branch_name: str, repo_root: Path) -> str` `priv` (L1158-1166)
- Brief: Resolve the git remote name configured for a given branch.
- Details: Queries `git config branch.<branch_name>.remote` via a local git command.
Returns `origin` as fallback when the config key is absent or the command fails.
No network operations are performed.
- Param: branch_name Local branch name whose configured remote is requested (e.g. `"master"`).
- Param: repo_root Absolute path used as CWD for the git config query.
- Return: Remote name string; never empty (falls back to `"origin"`).
- Satisfies: REQ-046

### fn `def _extract_owner_repo(remote_url: str) -> Optional[Tuple[str, str]]` `priv` (L1173-1197)
- Brief: Resolve the normalized HTTPS base URL from the master branch's configured remote.
- Details: Parses both SSH (`git@<host>:<owner>/<repo>[.git]`) and HTTPS
(`https://<host>/<owner>/<repo>[.git]`) formats and extracts `<owner>` and `<repo>`
through deterministic string parsing.
- Param: remote_url Raw git remote URL string.
- Return: Tuple `(owner, repo)` when parsing succeeds; otherwise `None`.

### fn `def _canonical_origin_base(repo_root: Path) -> Optional[str]` `priv` (L1207-1220)
- Brief: Resolve normalized GitHub URL base from the master-branch configured remote.
- Details: Determines remote name using `_get_remote_name_for_branch` with the configured
master branch, then executes local `git remote get-url <remote>` command.
If command execution fails or URL parsing fails, returns `None`.
On success, always emits `https://github.com/<owner>/<repo>` for changelog templates.
No network operation is performed; all data is derived from local git metadata.
- Param: repo_root Absolute path to the repository root used as CWD for all git commands.
- Return: Normalized HTTPS base URL string (no trailing `.git`), or `None` on failure.
- Satisfies: REQ-043, REQ-046

### fn `def get_origin_compare_url(base_url: Optional[str], prev_tag: Optional[str], tag: str) -> Optional[str]` (L1227-1234)
- Brief: Execute `get_origin_compare_url` runtime logic for Git-Alias CLI.
- Details: Executes `get_origin_compare_url` using deterministic CLI control-flow and explicit error propagation.
- Param: base_url Input parameter consumed by `get_origin_compare_url`.
- Param: prev_tag Input parameter consumed by `get_origin_compare_url`.
- Param: tag Input parameter consumed by `get_origin_compare_url`.
- Return: Result emitted by `get_origin_compare_url` according to command contract.

### fn `def get_release_page_url(base_url: Optional[str], tag: str) -> Optional[str]` (L1240-1245)
- Brief: Execute `get_release_page_url` runtime logic for Git-Alias CLI.
- Details: Executes `get_release_page_url` using deterministic CLI control-flow and explicit error propagation.
- Param: base_url Input parameter consumed by `get_release_page_url`.
- Param: tag Input parameter consumed by `get_release_page_url`.
- Return: Result emitted by `get_release_page_url` according to command contract.

### fn `def build_history_section(` (L1253-1257)
- Brief: Execute `build_history_section` runtime logic for Git-Alias CLI.
- Details: Executes `build_history_section` using deterministic CLI control-flow and explicit error propagation.
- Param: repo_root Input parameter consumed by `build_history_section`.
- Param: tags Input parameter consumed by `build_history_section`.
- Param: include_unreleased Input parameter consumed by `build_history_section`.
- Param: include_unreleased_link Input parameter consumed by `build_history_section`.
- Return: Result emitted by `build_history_section` according to command contract.

### fn `def generate_changelog_document(repo_root: Path, include_patch: bool, disable_history: bool = False) -> str` (L1301-1362)
- Brief: Generate the full CHANGELOG.md document from repository tags and commits.
- Details: Groups commits by minor release (semver where `patch=0` AND version `>=0.1.0`).
By default only minor releases appear; the document body is empty when none exist.
With `include_patch=True`, prepends the latest patch release after the last minor
(or the latest patch overall when no minor exists) including all commits in that range.
Releases are ordered reverse-chronologically in the output.
`# History` contains only the version tags present in the changelog body:
minor tags when `include_patch=False`; minor tags plus the latest patch when
`include_patch=True`. Diff links in `# History` use the same ranges as the
corresponding changelog sections. History generation can be disabled by flag.
- Param: repo_root Absolute path to the repository root used as CWD for all git commands.
- Param: include_patch When `True`, prepend the latest patch release section to the document.
- Param: disable_history When `True`, omit `# History` section from output.
- Return: Complete `CHANGELOG.md` string content, terminated with a newline.
- Satisfies: REQ-018, REQ-040, REQ-041, REQ-043, REQ-068, REQ-069, REQ-070

### class `class VersionRuleContext` `@dataclass(frozen=True)` (L1373-1380)

### fn `def _normalize_version_rule_pattern(pattern: str) -> str` `priv` (L1386-1397)
- Brief: Normalize a `ver_rules` pattern to the internal pathspec matching form.
- Details: Converts separators to POSIX style, strips leading `./`, and anchors patterns containing `/`
to repository root by prefixing `/` when missing, preserving REQ-017 semantics.
- Param: pattern Input pattern string from configuration.
- Return: Normalized pathspec-compatible pattern string; empty string when input is blank.

### fn `def _build_version_file_inventory(root: Path) -> List[Tuple[Path, str]]` `priv` (L1403-1424)
- Brief: Build a deduplicated repository file inventory for version rule evaluation.
- Details: Executes a single `rglob("*")` traversal from repository root, filters to files only,
applies hardcoded exclusion regexes, normalizes relative paths, and deduplicates by resolved path.
- Param: root Repository root path used as traversal anchor.
- Return: List of tuples `(absolute_path, normalized_relative_path)` used by downstream matchers.

### fn `def _collect_version_files(root, pattern, *, inventory=None)` `priv` (L1432-1449)
- Brief: Execute `_collect_version_files` runtime logic for Git-Alias CLI.
- Details: Executes `_collect_version_files` using deterministic CLI control-flow and explicit error propagation.
Uses precomputed inventory when provided to avoid repeated repository traversals.
- Param: root Input parameter consumed by `_collect_version_files`.
- Param: pattern Input parameter consumed by `_collect_version_files`.
- Param: inventory Optional precomputed `(path, normalized_relative_path)` list.
- Return: Result emitted by `_collect_version_files` according to command contract.

### fn `def _is_version_path_excluded(relative_path: str) -> bool` `priv` (L1454-1457)
- Brief: Execute `_is_version_path_excluded` runtime logic for Git-Alias CLI.
- Details: Executes `_is_version_path_excluded` using deterministic CLI control-flow and explicit error propagation.
- Param: relative_path Input parameter consumed by `_is_version_path_excluded`.
- Return: Result emitted by `_is_version_path_excluded` according to command contract.

### fn `def _iter_versions_in_text(text, compiled_regexes)` `priv` (L1463-1474)
- Brief: Execute `_iter_versions_in_text` runtime logic for Git-Alias CLI.
- Details: Executes `_iter_versions_in_text` using deterministic CLI control-flow and explicit error propagation.
- Param: text Input parameter consumed by `_iter_versions_in_text`.
- Param: compiled_regexes Input parameter consumed by `_iter_versions_in_text`.
- Return: Result emitted by `_iter_versions_in_text` according to command contract.

### fn `def _read_version_file_text(file_path: Path, text_cache: Optional[Dict[Path, str]] = None) -> Optional[str]` `priv` (L1481-1495)
- Brief: Read and cache UTF-8 text content for a version-managed file.
- Details: Loads file content with UTF-8 decoding; falls back to `errors="ignore"` on decode failures.
Emits deterministic stderr diagnostics on I/O failure and returns `None` for caller-managed skip logic.
- Param: file_path Absolute path of the file to read.
- Param: text_cache Optional mutable cache keyed by `Path` to avoid duplicate reads across phases.
- Return: File text payload or `None` when file cannot be read.

### fn `def _prepare_version_rule_contexts(` `priv` (L1504-1505)
- Brief: Build reusable per-rule contexts for canonical version evaluation workflows.
- Details: Resolves matched files and compiled regex for each `(pattern, regex)` rule exactly once.
Preserves error contracts for unmatched patterns and invalid regex declarations.
- Param: root Repository root path used for relative-path rendering.
- Param: rules Sequence of `(pattern, regex)` tuples.
- Param: inventory Optional precomputed inventory to avoid repeated filesystem traversal.
- Return: Ordered list of `VersionRuleContext` objects aligned to input rule order.
- Throws: VersionDetectionError when a rule matches no files or contains an invalid regex.

### fn `def _determine_canonical_version(` `priv` (L1547-1554)
- Brief: Execute `_determine_canonical_version` runtime logic for Git-Alias CLI.
- Details: Executes `_determine_canonical_version` using deterministic CLI control-flow and explicit error propagation.
- Param: root Input parameter consumed by `_determine_canonical_version`.
- Param: rules Input parameter consumed by `_determine_canonical_version`.
- Param: verbose Input parameter consumed by `_determine_canonical_version`.
- Param: debug Input parameter consumed by `_determine_canonical_version`.
- Param: contexts Optional precomputed `VersionRuleContext` list for reuse across phases.
- Param: text_cache Optional mutable cache keyed by file path to avoid duplicate reads.
- Return: Result emitted by `_determine_canonical_version` according to command contract.

### fn `def _parse_semver_tuple(text: str) -> Optional[Tuple[int, int, int]]` `priv` (L1599-1605)
- Brief: Execute `_parse_semver_tuple` runtime logic for Git-Alias CLI.
- Details: Executes `_parse_semver_tuple` using deterministic CLI control-flow and explicit error propagation.
- Param: text Input parameter consumed by `_parse_semver_tuple`.
- Return: Result emitted by `_parse_semver_tuple` according to command contract.

### fn `def _replace_versions_in_text(text, compiled_regex, replacement)` `priv` (L1612-1627)
- Brief: Execute `_replace_versions_in_text` runtime logic for Git-Alias CLI.
- Details: Executes `_replace_versions_in_text` using deterministic CLI control-flow and explicit error propagation.
- Param: text Input parameter consumed by `_replace_versions_in_text`.
- Param: compiled_regex Input parameter consumed by `_replace_versions_in_text`.
- Param: replacement Input parameter consumed by `_replace_versions_in_text`.
- Return: Result emitted by `_replace_versions_in_text` according to command contract.

### fn `def _current_branch_name()` `priv` (L1631-1643)
- Brief: Execute `_current_branch_name` runtime logic for Git-Alias CLI.
- Details: Executes `_current_branch_name` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_current_branch_name` according to command contract.

### fn `def _ref_exists(ref_name)` `priv` (L1648-1657)
- Brief: Execute `_ref_exists` runtime logic for Git-Alias CLI.
- Details: Executes `_ref_exists` using deterministic CLI control-flow and explicit error propagation.
- Param: ref_name Input parameter consumed by `_ref_exists`.
- Return: Result emitted by `_ref_exists` according to command contract.

### fn `def _local_branch_exists(branch_name)` `priv` (L1662-1665)
- Brief: Execute `_local_branch_exists` runtime logic for Git-Alias CLI.
- Details: Executes `_local_branch_exists` using deterministic CLI control-flow and explicit error propagation.
- Param: branch_name Input parameter consumed by `_local_branch_exists`.
- Return: Result emitted by `_local_branch_exists` according to command contract.

### fn `def _remote_branch_exists(branch_name)` `priv` (L1670-1673)
- Brief: Execute `_remote_branch_exists` runtime logic for Git-Alias CLI.
- Details: Executes `_remote_branch_exists` using deterministic CLI control-flow and explicit error propagation.
- Param: branch_name Input parameter consumed by `_remote_branch_exists`.
- Return: Result emitted by `_remote_branch_exists` according to command contract.

### fn `def _ensure_release_prerequisites()` `priv` (L1677-1704)
- Brief: Execute `_ensure_release_prerequisites` runtime logic for Git-Alias CLI.
- Details: Executes `_ensure_release_prerequisites` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_ensure_release_prerequisites` according to command contract.

### fn `def _bump_semver_version(current_version, level)` `priv` (L1710-1728)
- Brief: Execute `_bump_semver_version` runtime logic for Git-Alias CLI.
- Details: Executes `_bump_semver_version` using deterministic CLI control-flow and explicit error propagation.
- Param: current_version Input parameter consumed by `_bump_semver_version`.
- Param: level Input parameter consumed by `_bump_semver_version`.
- Return: Result emitted by `_bump_semver_version` according to command contract.

### fn `def _run_release_step(level, step_name, action)` `priv` (L1735-1755)
- Brief: Execute `_run_release_step` runtime logic for Git-Alias CLI.
- Details: Executes `_run_release_step` using deterministic CLI control-flow and explicit error propagation.
- Param: level Input parameter consumed by `_run_release_step`.
- Param: step_name Input parameter consumed by `_run_release_step`.
- Param: action Input parameter consumed by `_run_release_step`.
- Return: Result emitted by `_run_release_step` according to command contract.

### fn `def _create_release_commit_for_flow(target_version)` `priv` (L1760-1765)
- Brief: Execute `_create_release_commit_for_flow` runtime logic for Git-Alias CLI.
- Details: Executes release-flow first-commit creation with WIP amend semantics reused from `_execute_commit`.
- Param: target_version Input parameter consumed by `_create_release_commit_for_flow`.
- Return: Result emitted by `_create_release_commit_for_flow` according to command contract.

### fn `def _push_branch_with_tags(branch_name)` `priv` (L1771-1775)
- Brief: Execute `_push_branch_with_tags` runtime logic for Git-Alias CLI.
- Details: Pushes the specified local branch to `origin` using an explicit branch refspec and
includes `--tags` in the same push command.
- Param: branch_name Local branch name resolved from configured release branches.
- Return: Result emitted by `run_git_cmd` according to command contract.

### fn `def _execute_release_flow(level, changelog_args=None)` `priv` (L1791-1838)
- Brief: Execute `_execute_release_flow` runtime logic for Git-Alias CLI.
- Details: Orchestrates the full release pipeline for `major`, `minor`, and `patch` levels.
Branch integration is level-dependent (REQ-045):
- `patch`: merges `work` into `develop` and pushes `develop` only; skips `master`.
- `major`/`minor`: merges `work` into `develop`, pushes `develop` with tags, then merges
`develop` into `master` and pushes `master`.
Changelog flags always include `--force-write`; `patch` auto-adds `--include-patch`.
A temporary local `v<target>` tag is created on `work` only to generate changelog and
deleted immediately after changelog generation. The definitive `v<target>` tag is then
created on `develop` (`patch`) or `master` (`major`/`minor`) immediately before push
with `--tags`.
- Param: level Release level string: `"major"`, `"minor"`, or `"patch"`.
- Param: changelog_args Optional list of extra changelog flags forwarded alongside `--force-write`.
- Return: None; raises `ReleaseError` or `VersionDetectionError` on failure.
- Satisfies: REQ-026, REQ-045

### fn `def _execute_backup_flow()` `priv` (L1846-1861)
- Brief: Execute `_execute_backup_flow` runtime logic for Git-Alias CLI.
- Details: Executes the `backup` workflow by reusing the release preflight checks, then
fast-forward merges configured `work` into configured `develop`, pushes `develop`
to its configured remote tracking branch, checks out back to `work`, and prints
an explicit success confirmation.
- Return: None; raises `ReleaseError` on preflight or workflow failure.
- Satisfies: REQ-047, REQ-048, REQ-049

### fn `def _run_release_command(level, changelog_args=None)` `priv` (L1867-1882)
- Brief: Execute `_run_release_command` runtime logic for Git-Alias CLI.
- Details: Executes `_run_release_command` using deterministic CLI control-flow and explicit error propagation.
- Param: level Input parameter consumed by `_run_release_command`.
- Param: changelog_args Input parameter consumed by `_run_release_command`.
- Return: Result emitted by `_run_release_command` according to command contract.

### fn `def _run_backup_command()` `priv` (L1887-1894)
- Brief: Execute `_run_backup_command` runtime logic for Git-Alias CLI.
- Details: Runs the `backup` workflow with the same error propagation strategy used by release commands.
- Return: None; exits with status 1 on `ReleaseError`.
- Satisfies: REQ-047, REQ-048, REQ-049

### fn `def _run_reset_with_help(base_args, extra)` `priv` (L1900-1907)
- Brief: Execute `_run_reset_with_help` runtime logic for Git-Alias CLI.
- Details: Executes `_run_reset_with_help` using deterministic CLI control-flow and explicit error propagation.
- Param: base_args Input parameter consumed by `_run_reset_with_help`.
- Param: extra Input parameter consumed by `_run_reset_with_help`.
- Return: Result emitted by `_run_reset_with_help` according to command contract.

### fn `def _reject_extra_arguments(extra, alias)` `priv` (L1913-1919)
- Brief: Execute `_reject_extra_arguments` runtime logic for Git-Alias CLI.
- Details: Executes `_reject_extra_arguments` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `_reject_extra_arguments`.
- Param: alias Input parameter consumed by `_reject_extra_arguments`.
- Return: Result emitted by `_reject_extra_arguments` according to command contract.

### fn `def _parse_release_flags(extra, alias)` `priv` (L1925-1943)
- Brief: Execute `_parse_release_flags` runtime logic for Git-Alias CLI.
- Details: Executes `_parse_release_flags` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `_parse_release_flags`.
- Param: alias Input parameter consumed by `_parse_release_flags`.
- Return: Result emitted by `_parse_release_flags` according to command contract.

### fn `def _prepare_commit_message(extra, alias)` `priv` (L1949-1959)
- Brief: Execute `_prepare_commit_message` runtime logic for Git-Alias CLI.
- Details: Executes `_prepare_commit_message` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `_prepare_commit_message`.
- Param: alias Input parameter consumed by `_prepare_commit_message`.
- Return: Result emitted by `_prepare_commit_message` according to command contract.

### fn `def _build_conventional_message(kind: str, extra, alias: str) -> str` `priv` (L1966-1980)
- Brief: Execute `_build_conventional_message` runtime logic for Git-Alias CLI.
- Details: Executes `_build_conventional_message` using deterministic CLI control-flow and explicit error propagation.
- Param: kind Input parameter consumed by `_build_conventional_message`.
- Param: extra Input parameter consumed by `_build_conventional_message`.
- Param: alias Input parameter consumed by `_build_conventional_message`.
- Return: Result emitted by `_build_conventional_message` according to command contract.

### fn `def _run_conventional_commit(kind: str, alias: str, extra)` `priv` (L1987-1992)
- Brief: Execute `_run_conventional_commit` runtime logic for Git-Alias CLI.
- Details: Executes `_run_conventional_commit` using deterministic CLI control-flow and explicit error propagation.
- Param: kind Input parameter consumed by `_run_conventional_commit`.
- Param: alias Input parameter consumed by `_run_conventional_commit`.
- Param: extra Input parameter consumed by `_run_conventional_commit`.
- Return: Result emitted by `_run_conventional_commit` according to command contract.

### fn `def _execute_commit(message, alias, allow_amend=True)` `priv` (L1999-2028)
- Brief: Execute `_execute_commit` runtime logic for Git-Alias CLI.
- Details: Executes `_execute_commit` using deterministic CLI control-flow and explicit error propagation.
- Param: message Input parameter consumed by `_execute_commit`.
- Param: alias Input parameter consumed by `_execute_commit`.
- Param: allow_amend Input parameter consumed by `_execute_commit`.
- Return: Result emitted by `_execute_commit` according to command contract.

### fn `def upgrade_self()` (L2032-2045)
- Brief: Execute `upgrade_self` runtime logic for Git-Alias CLI.
- Details: Executes `upgrade_self` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `upgrade_self` according to command contract.

### fn `def remove_self()` (L2049-2052)
- Brief: Execute `remove_self` runtime logic for Git-Alias CLI.
- Details: Executes `remove_self` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `remove_self` according to command contract.

### fn `def cmd_aa(extra)` (L2057-2064)
- Brief: Execute `cmd_aa` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_aa` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_aa`.
- Return: Result emitted by `cmd_aa` according to command contract.

### fn `def cmd_ra(extra)` (L2069-2092)
- Brief: Execute `cmd_ra` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ra` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ra`.
- Return: Result emitted by `cmd_ra` according to command contract.

### fn `def cmd_ar(extra)` (L2097-2111)
- Brief: Execute `cmd_ar` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ar` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ar`.
- Return: Result emitted by `cmd_ar` according to command contract.

### fn `def cmd_br(extra)` (L2116-2119)
- Brief: Execute `cmd_br` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_br` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_br`.
- Return: Result emitted by `cmd_br` according to command contract.

### fn `def cmd_bd(extra)` (L2124-2127)
- Brief: Execute `cmd_bd` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_bd` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_bd`.
- Return: Result emitted by `cmd_bd` according to command contract.

### fn `def cmd_ck(extra)` (L2132-2135)
- Brief: Execute `cmd_ck` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ck` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ck`.
- Return: Result emitted by `cmd_ck` according to command contract.

### fn `def _ensure_commit_ready(alias)` `priv` (L2140-2153)
- Brief: Execute `_ensure_commit_ready` runtime logic for Git-Alias CLI.
- Details: Executes `_ensure_commit_ready` using deterministic CLI control-flow and explicit error propagation.
- Param: alias Input parameter consumed by `_ensure_commit_ready`.
- Return: Result emitted by `_ensure_commit_ready` according to command contract.

### fn `def cmd_cm(extra)` (L2158-2163)
- Brief: Execute `cmd_cm` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_cm` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_cm`.
- Return: Result emitted by `cmd_cm` according to command contract.

### fn `def cmd_wip(extra)` (L2168-2180)
- Brief: Execute `cmd_wip` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_wip` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_wip`.
- Return: Result emitted by `cmd_wip` according to command contract.

### fn `def cmd_release(extra)` (L2185-2207)
- Brief: Execute `cmd_release` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_release` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_release`.
- Return: Result emitted by `cmd_release` according to command contract.

### fn `def cmd_new(extra)` (L2212-2215)
- Brief: Execute `cmd_new` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_new` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_new`.
- Return: Result emitted by `cmd_new` according to command contract.

### fn `def cmd_refactor(extra)` (L2220-2223)
- Brief: Execute `cmd_refactor` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_refactor` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_refactor`.
- Return: Result emitted by `cmd_refactor` according to command contract.

### fn `def cmd_fix(extra)` (L2228-2231)
- Brief: Execute `cmd_fix` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_fix` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_fix`.
- Return: Result emitted by `cmd_fix` according to command contract.

### fn `def cmd_change(extra)` (L2236-2239)
- Brief: Execute `cmd_change` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_change` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_change`.
- Return: Result emitted by `cmd_change` according to command contract.

### fn `def cmd_implement(extra)` (L2244-2247)
- Brief: Execute `cmd_implement` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_implement` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_implement`.
- Return: Result emitted by `cmd_implement` according to command contract.

### fn `def cmd_docs(extra)` (L2252-2255)
- Brief: Execute `cmd_docs` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_docs` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_docs`.
- Return: Result emitted by `cmd_docs` according to command contract.

### fn `def cmd_style(extra)` (L2260-2263)
- Brief: Execute `cmd_style` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_style` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_style`.
- Return: Result emitted by `cmd_style` according to command contract.

### fn `def cmd_revert(extra)` (L2268-2271)
- Brief: Execute `cmd_revert` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_revert` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_revert`.
- Return: Result emitted by `cmd_revert` according to command contract.

### fn `def cmd_misc(extra)` (L2276-2279)
- Brief: Execute `cmd_misc` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_misc` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_misc`.
- Return: Result emitted by `cmd_misc` according to command contract.

### fn `def cmd_cover(extra)` (L2284-2287)
- Brief: Execute `cmd_cover` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_cover` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_cover`.
- Return: Result emitted by `cmd_cover` according to command contract.

### fn `def cmd_co(extra)` (L2292-2295)
- Brief: Execute `cmd_co` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_co` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_co`.
- Return: Result emitted by `cmd_co` according to command contract.

### fn `def cmd_dr(extra)` (L2300-2307)
- Brief: Execute `cmd_dr` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_dr` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_dr`.
- Return: Result emitted by `cmd_dr` according to command contract.

### fn `def cmd_dcc(extra)` (L2312-2315)
- Brief: Execute `cmd_dcc` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_dcc` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_dcc`.
- Return: Result emitted by `cmd_dcc` according to command contract.

### fn `def cmd_dccc(extra)` (L2320-2323)
- Brief: Execute `cmd_dccc` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_dccc` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_dccc`.
- Return: Result emitted by `cmd_dccc` according to command contract.

### fn `def cmd_de(extra)` (L2328-2331)
- Brief: Execute `cmd_de` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_de` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_de`.
- Return: Result emitted by `cmd_de` according to command contract.

### fn `def cmd_di(extra)` (L2336-2339)
- Brief: Execute `cmd_di` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_di` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_di`.
- Return: Result emitted by `cmd_di` according to command contract.

### fn `def cmd_diyou(extra)` (L2344-2347)
- Brief: Execute `cmd_diyou` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_diyou` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_diyou`.
- Return: Result emitted by `cmd_diyou` according to command contract.

### fn `def cmd_dime(extra)` (L2352-2355)
- Brief: Execute `cmd_dime` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_dime` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_dime`.
- Return: Result emitted by `cmd_dime` according to command contract.

### fn `def cmd_dwc(extra)` (L2360-2363)
- Brief: Execute `cmd_dwc` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_dwc` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_dwc`.
- Return: Result emitted by `cmd_dwc` according to command contract.

### fn `def cmd_dwcc(extra)` (L2368-2371)
- Brief: Execute `cmd_dwcc` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_dwcc` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_dwcc`.
- Return: Result emitted by `cmd_dwcc` according to command contract.

### fn `def cmd_ed(extra)` (L2376-2385)
- Brief: Execute `cmd_ed` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ed` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ed`.
- Return: Result emitted by `cmd_ed` according to command contract.

### fn `def cmd_fe(extra)` (L2390-2393)
- Brief: Execute `cmd_fe` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_fe` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_fe`.
- Return: Result emitted by `cmd_fe` according to command contract.

### fn `def cmd_feall(extra)` (L2398-2401)
- Brief: Execute `cmd_feall` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_feall` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_feall`.
- Return: Result emitted by `cmd_feall` according to command contract.

### fn `def cmd_gp(extra)` (L2406-2409)
- Brief: Execute `cmd_gp` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_gp` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_gp`.
- Return: Result emitted by `cmd_gp` according to command contract.

### fn `def cmd_gr(extra)` (L2414-2417)
- Brief: Execute `cmd_gr` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_gr` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_gr`.
- Return: Result emitted by `cmd_gr` according to command contract.

- var `OVERVIEW_COLOR_RESET = "\033[0m"` (L2419)
- Brief: Constant `OVERVIEW_COLOR_RESET` used by CLI runtime paths and policies.
- var `OVERVIEW_COLOR_SECTION_PURPLE = "\033[35;1m"` (L2421)
- Brief: Constant `OVERVIEW_COLOR_SECTION_PURPLE` used by CLI runtime paths and policies.
- var `OVERVIEW_COLOR_AHEAD = "\033[92m"` (L2423)
- Brief: Constant `OVERVIEW_COLOR_AHEAD` used by CLI runtime paths and policies.
- var `OVERVIEW_COLOR_BEHIND = "\033[31;1m"` (L2425)
- Brief: Constant `OVERVIEW_COLOR_BEHIND` used by CLI runtime paths and policies.
- var `OVERVIEW_COLOR_LABEL = "\033[38;5;226m"` (L2427)
- Brief: Constant `OVERVIEW_COLOR_LABEL` used by CLI runtime paths and policies.
- var `OVERVIEW_COLOR_WHITE = "\033[97m"` (L2429)
- Brief: Constant `OVERVIEW_COLOR_WHITE` used by CLI runtime paths and policies.
- var `OVERVIEW_COLOR_WHITE_BOLD = "\033[97;1m"` (L2431)
- Brief: Constant `OVERVIEW_COLOR_WHITE_BOLD` used by CLI runtime paths and policies.
- var `OVERVIEW_SECTION_TEMPLATE = "{color}=== {title} ==={reset}"` (L2433)
- Brief: Constant `OVERVIEW_SECTION_TEMPLATE` used by CLI runtime paths and policies.
- var `OVERVIEW_SUBSECTION_TEMPLATE = "{color}--- {title} ---{reset}"` (L2435)
- Brief: Constant `OVERVIEW_SUBSECTION_TEMPLATE` used by CLI runtime paths and policies.
- var `OVERVIEW_DISTANCE_TEMPLATE = "{text_color}{label}{reset} | {ahead} | {behind}"` (L2437)
- Brief: Constant `OVERVIEW_DISTANCE_TEMPLATE` used by CLI runtime paths and policies.
### fn `def _overview_branch_identifier(` `priv` (L2446-2449)
- Brief: Execute `_overview_branch_identifier` runtime logic for Git-Alias CLI.
- Details: Executes `_overview_branch_identifier` using deterministic CLI control-flow and explicit error propagation.
- Param: logical_name Input parameter consumed by `_overview_branch_identifier`.
- Param: ref_name Input parameter consumed by `_overview_branch_identifier`.
- Param: prefix_color Input parameter consumed by `_overview_branch_identifier`.
- Return: Result emitted by `_overview_branch_identifier` according to command contract.

### fn `def _overview_logical_branch_name(` `priv` (L2466-2470)
- Brief: Execute `_overview_logical_branch_name` runtime logic for Git-Alias CLI.
- Details: Executes `_overview_logical_branch_name` using deterministic CLI control-flow and explicit error propagation.
- Param: current_branch Input parameter consumed by `_overview_logical_branch_name`.
- Param: work_branch Input parameter consumed by `_overview_logical_branch_name`.
- Param: develop_branch Input parameter consumed by `_overview_logical_branch_name`.
- Param: master_branch Input parameter consumed by `_overview_logical_branch_name`.
- Return: Result emitted by `_overview_logical_branch_name` according to command contract.

### fn `def _overview_current_branch_display(` `priv` (L2488-2492)
- Brief: Execute `_overview_current_branch_display` runtime logic for Git-Alias CLI.
- Details: Executes `_overview_current_branch_display` using deterministic CLI control-flow and explicit error propagation.
- Param: current_branch Input parameter consumed by `_overview_current_branch_display`.
- Param: work_branch Input parameter consumed by `_overview_current_branch_display`.
- Param: develop_branch Input parameter consumed by `_overview_current_branch_display`.
- Param: master_branch Input parameter consumed by `_overview_current_branch_display`.
- Return: Result emitted by `_overview_current_branch_display` according to command contract.

### fn `def _overview_ref_is_available(ref_name: str) -> bool` `priv` (L2511-2520)
- Brief: Execute `_overview_ref_is_available` runtime logic for Git-Alias CLI.
- Details: Executes `_overview_ref_is_available` using deterministic CLI control-flow and explicit error propagation.
- Param: ref_name Input parameter consumed by `_overview_ref_is_available`.
- Return: Result emitted by `_overview_ref_is_available` according to command contract.

### fn `def _overview_ref_latest_subject(ref_name: str) -> str` `priv` (L2526-2535)
- Brief: Resolve latest commit subject for an overview ref.
- Details: Returns the `%s` subject of `git log -1` for the input ref, or `n/a`
when the ref is unavailable or the lookup fails.
- Param: ref_name Input parameter consumed by `_overview_ref_latest_subject`.
- Return: Result emitted by `_overview_ref_latest_subject` according to command contract.

### fn `def _overview_branch_summary_lines(` `priv` (L2552-2562)
- Brief: Build section-5 aligned branch summary lines for overview output.
- Details: Produces one row for each configured branch/ref identifier using
`<Identifier> | <latest commit subject>` formatting, aligned by visible
identifier width and with commit subject in bright white bold.
- Param: work_ref Input parameter consumed by `_overview_branch_summary_lines`.
- Param: develop_ref Input parameter consumed by `_overview_branch_summary_lines`.
- Param: master_ref Input parameter consumed by `_overview_branch_summary_lines`.
- Param: remote_develop_ref Input parameter consumed by `_overview_branch_summary_lines`.
- Param: remote_master_ref Input parameter consumed by `_overview_branch_summary_lines`.
- Param: work_display Input parameter consumed by `_overview_branch_summary_lines`.
- Param: develop_display Input parameter consumed by `_overview_branch_summary_lines`.
- Param: master_display Input parameter consumed by `_overview_branch_summary_lines`.
- Param: remote_develop_display Input parameter consumed by `_overview_branch_summary_lines`.
- Param: remote_master_display Input parameter consumed by `_overview_branch_summary_lines`.
- Return: Result emitted by `_overview_branch_summary_lines` according to command contract.
- Satisfies: REQ-094, REQ-096

### fn `def _overview_relation_state(ahead: int, behind: int) -> str` `priv` (L2590-2599)
- Brief: Execute `_overview_relation_state` runtime logic for Git-Alias CLI.
- Details: Executes `_overview_relation_state` using deterministic CLI control-flow and explicit error propagation.
- Param: ahead Input parameter consumed by `_overview_relation_state`.
- Param: behind Input parameter consumed by `_overview_relation_state`.
- Return: Result emitted by `_overview_relation_state` according to command contract.

### fn `def _overview_worktree_state(status_lines=None) -> str` `priv` (L2604-2616)
- Brief: Execute `_overview_worktree_state` runtime logic for Git-Alias CLI.
- Details: Executes `_overview_worktree_state` using deterministic CLI control-flow and explicit error propagation.
- Param: status_lines Input parameter consumed by `_overview_worktree_state`.
- Return: Result emitted by `_overview_worktree_state` according to command contract.

### fn `def _overview_distance_text(is_ahead: bool, count: int) -> str` `priv` (L2622-2630)
- Brief: Execute `_overview_distance_text` runtime logic for Git-Alias CLI.
- Details: Executes `_overview_distance_text` using deterministic CLI control-flow and explicit error propagation.
- Param: is_ahead Input parameter consumed by `_overview_distance_text`.
- Param: count Input parameter consumed by `_overview_distance_text`.
- Return: Result emitted by `_overview_distance_text` according to command contract.

### fn `def _overview_compare_refs(base_ref: str, target_ref: str, label: str) -> str` `priv` (L2637-2677)
- Brief: Execute `_overview_compare_refs` runtime logic for Git-Alias CLI.
- Details: Executes `_overview_compare_refs` using deterministic CLI control-flow and explicit error propagation.
- Param: base_ref Input parameter consumed by `_overview_compare_refs`.
- Param: target_ref Input parameter consumed by `_overview_compare_refs`.
- Param: label Input parameter consumed by `_overview_compare_refs`.
- Return: Result emitted by `_overview_compare_refs` according to command contract.

### fn `def _overview_ascii_topology_lines(` `priv` (L2698-2709)
- Brief: Build chronological-position topology tree from actual commit positions.
- Details: Resolves commit hashes for each ref, computes commit counts from
octopus merge-base, groups refs sharing the same hash on one output line,
and orders nodes from most-ahead (root) to most-behind (deepest child).
WorkingTree always occupies a dedicated line above the line that contains
Work when tied or dirty. Complexity O(R) git
subprocess calls where R is the number of available refs.
- Param: work_ref {str} Git ref name for work branch.
- Param: develop_ref {str} Git ref name for develop branch.
- Param: master_ref {str} Git ref name for master branch.
- Param: remote_develop_ref {str} Git ref name for remote develop (e.g., origin/develop).
- Param: remote_master_ref {str} Git ref name for remote master (e.g., origin/master).
- Param: work_display {str} Rendered display string for Work identifier.
- Param: develop_display {str} Rendered display string for Develop identifier.
- Param: master_display {str} Rendered display string for Master identifier.
- Param: remote_develop_display {str} Rendered display string for RemoteDevelop identifier.
- Param: remote_master_display {str} Rendered display string for RemoteMaster identifier.
- Param: worktree_state {str} Working tree state (clean/unstaged/staged/mixed).
- Return: {List[str]} Rendered topology lines with ANSI color codes.
- Satisfies: REQ-089, REQ-090, REQ-091, REQ-092, REQ-093, REQ-095

### fn `def cmd_o(extra)` (L2797-2929)
- Brief: Execute `cmd_o` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_o` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_o`.
- Return: Result emitted by `cmd_o` according to command contract.
- Satisfies: REQ-082, REQ-083, REQ-084, REQ-085, REQ-086, REQ-087, REQ-088, REQ-089, REQ-090, REQ-091, REQ-092, REQ-093, REQ-094, REQ-095, REQ-096

### fn `def cmd_str(extra)` (L2934-2963)
- Brief: Execute `cmd_str` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_str` using deterministic CLI control-flow and explicit error propagation.
- Details: Query git remotes with transport metadata.
- Param: extra Input parameter consumed by `cmd_str`.
- Return: Result emitted by `cmd_str` according to command contract.

### fn `def cmd_lb(extra)` (L2968-2971)
- Brief: Execute `cmd_lb` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_lb` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_lb`.
- Return: Result emitted by `cmd_lb` according to command contract.

### fn `def cmd_lg(extra)` (L2976-2989)
- Brief: Execute `cmd_lg` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_lg` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_lg`.
- Return: Result emitted by `cmd_lg` according to command contract.

### fn `def cmd_lh(extra)` (L2994-2997)
- Brief: Execute `cmd_lh` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_lh` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_lh`.
- Return: Result emitted by `cmd_lh` according to command contract.

### fn `def cmd_ll(extra)` (L3002-3014)
- Brief: Execute `cmd_ll` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ll` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ll`.
- Return: Result emitted by `cmd_ll` according to command contract.

### fn `def cmd_lm(extra)` (L3019-3022)
- Brief: Execute `cmd_lm` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_lm` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_lm`.
- Return: Result emitted by `cmd_lm` according to command contract.

### fn `def cmd_ls(extra)` (L3028-3031)
- Brief: Execute `cmd_ls` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ls` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ls`.
- Return: Result emitted by `cmd_ls` according to command contract.
- Satisfies: REQ-079

### fn `def cmd_lsi(extra)` (L3037-3043)
- Brief: Execute `cmd_lsi` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_lsi` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_lsi`.
- Return: Result emitted by `cmd_lsi` according to command contract.
- Satisfies: REQ-080

### fn `def cmd_lsa(extra)` (L3049-3052)
- Brief: Execute `cmd_lsa` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_lsa` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_lsa`.
- Return: Result emitted by `cmd_lsa` according to command contract.
- Satisfies: REQ-081

### fn `def cmd_lt(extra)` (L3058-3077)
- Brief: Execute `cmd_lt` runtime logic for Git-Alias CLI.
- Details: Enumerates tags via `git tag -l`, resolves containing refs via `git branch -a --contains <tag>`,
trims branch markers/prefixes from git output, and prints deterministic `<tag>: <branch_1>, <branch_2>, ...` lines.
- Param: extra Input parameter consumed by `cmd_lt`.
- Return: Result emitted by `cmd_lt` according to command contract.

### fn `def cmd_me(extra)` (L3082-3085)
- Brief: Execute `cmd_me` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_me` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_me`.
- Return: Result emitted by `cmd_me` according to command contract.

### fn `def cmd_pl(extra)` (L3090-3093)
- Brief: Execute `cmd_pl` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_pl` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_pl`.
- Return: Result emitted by `cmd_pl` according to command contract.

### fn `def cmd_pt(extra)` (L3098-3101)
- Brief: Execute `cmd_pt` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_pt` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_pt`.
- Return: Result emitted by `cmd_pt` according to command contract.

### fn `def cmd_pu(extra)` (L3106-3109)
- Brief: Execute `cmd_pu` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_pu` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_pu`.
- Return: Result emitted by `cmd_pu` according to command contract.

### fn `def cmd_rf(extra)` (L3114-3117)
- Brief: Execute `cmd_rf` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rf` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rf`.
- Return: Result emitted by `cmd_rf` according to command contract.

### fn `def cmd_rmtg(extra)` (L3122-3132)
- Brief: Execute `cmd_rmtg` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rmtg` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rmtg`.
- Return: Result emitted by `cmd_rmtg` according to command contract.

### fn `def cmd_rmloc(extra)` (L3137-3140)
- Brief: Execute `cmd_rmloc` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rmloc` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rmloc`.
- Return: Result emitted by `cmd_rmloc` according to command contract.

### fn `def cmd_rmstg(extra)` (L3145-3148)
- Brief: Execute `cmd_rmstg` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rmstg` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rmstg`.
- Return: Result emitted by `cmd_rmstg` according to command contract.

### fn `def cmd_rmunt(extra)` (L3153-3156)
- Brief: Execute `cmd_rmunt` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rmunt` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rmunt`.
- Return: Result emitted by `cmd_rmunt` according to command contract.

### fn `def cmd_rs(extra)` (L3161-3164)
- Brief: Execute `cmd_rs` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rs` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rs`.
- Return: Result emitted by `cmd_rs` according to command contract.

### fn `def cmd_rssft(extra)` (L3169-3172)
- Brief: Execute `cmd_rssft` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rssft` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rssft`.
- Return: Result emitted by `cmd_rssft` according to command contract.

### fn `def cmd_rsmix(extra)` (L3177-3180)
- Brief: Execute `cmd_rsmix` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rsmix` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rsmix`.
- Return: Result emitted by `cmd_rsmix` according to command contract.

### fn `def cmd_rshrd(extra)` (L3185-3188)
- Brief: Execute `cmd_rshrd` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rshrd` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rshrd`.
- Return: Result emitted by `cmd_rshrd` according to command contract.

### fn `def cmd_rsmrg(extra)` (L3193-3196)
- Brief: Execute `cmd_rsmrg` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rsmrg` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rsmrg`.
- Return: Result emitted by `cmd_rsmrg` according to command contract.

### fn `def cmd_rskep(extra)` (L3201-3204)
- Brief: Execute `cmd_rskep` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rskep` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rskep`.
- Return: Result emitted by `cmd_rskep` according to command contract.

### fn `def cmd_st(extra)` (L3209-3212)
- Brief: Execute `cmd_st` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_st` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_st`.
- Return: Result emitted by `cmd_st` according to command contract.

### fn `def cmd_tg(extra)` (L3217-3220)
- Brief: Execute `cmd_tg` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_tg` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_tg`.
- Return: Result emitted by `cmd_tg` according to command contract.

### fn `def cmd_unstg(extra)` (L3225-3228)
- Brief: Execute `cmd_unstg` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_unstg` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_unstg`.
- Return: Result emitted by `cmd_unstg` according to command contract.

### fn `def cmd_wt(extra)` (L3233-3236)
- Brief: Execute `cmd_wt` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_wt` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_wt`.
- Return: Result emitted by `cmd_wt` according to command contract.

### fn `def cmd_wtl(extra)` (L3241-3244)
- Brief: Execute `cmd_wtl` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_wtl` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_wtl`.
- Return: Result emitted by `cmd_wtl` according to command contract.

### fn `def cmd_wtp(extra)` (L3249-3252)
- Brief: Execute `cmd_wtp` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_wtp` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_wtp`.
- Return: Result emitted by `cmd_wtp` according to command contract.

### fn `def cmd_wtr(extra)` (L3257-3260)
- Brief: Execute `cmd_wtr` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_wtr` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_wtr`.
- Return: Result emitted by `cmd_wtr` according to command contract.

### fn `def cmd_ver(extra)` (L3265-3291)
- Brief: Execute `cmd_ver` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ver` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ver`.
- Return: Result emitted by `cmd_ver` according to command contract.

### fn `def cmd_chver(extra)` (L3296-3368)
- Brief: Execute `cmd_chver` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_chver` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_chver`.
- Return: Result emitted by `cmd_chver` according to command contract.

### fn `def cmd_major(extra)` (L3377-3381)
- Brief: CLI entry-point for the `major` release subcommand.
- Details: Increments the major semver index (resets minor and patch to 0), merges and pushes
to both configured `develop` and `master` branches, regenerates changelog via a
temporary local tag on `work`, and creates the definitive release tag on `master`
immediately before pushing `master` with `--tags`.
- Param: extra Iterable of CLI argument strings; accepted flag: `--include-patch`.
- Return: None; delegates to `_run_release_command("major", ...)`.
- Satisfies: REQ-026, REQ-045

### fn `def cmd_minor(extra)` (L3390-3394)
- Brief: CLI entry-point for the `minor` release subcommand.
- Details: Increments the minor semver index (resets patch to 0), merges and pushes to both
configured `develop` and `master` branches, regenerates changelog via a temporary local
tag on `work`, and creates the definitive release tag on `master` immediately before
pushing `master` with `--tags`.
- Param: extra Iterable of CLI argument strings; accepted flag: `--include-patch`.
- Return: None; delegates to `_run_release_command("minor", ...)`.
- Satisfies: REQ-026, REQ-045

### fn `def cmd_patch(extra)` (L3403-3407)
- Brief: CLI entry-point for the `patch` release subcommand.
- Details: Increments the patch semver index, merges and pushes to configured `develop` only
(MUST NOT merge or push to `master`), regenerates changelog via a temporary local tag
on `work`, and creates the definitive release tag on `develop` immediately before
pushing `develop` with `--tags`; `--include-patch` is auto-included.
- Param: extra Iterable of CLI argument strings; accepted flag: `--include-patch`.
- Return: None; delegates to `_run_release_command("patch", ...)`.
- Satisfies: REQ-026, REQ-045

### fn `def cmd_backup(extra)` (L3415-3425)
- Brief: CLI entry-point for the `backup` workflow subcommand.
- Details: Runs the same preflight checks used by `major`/`minor`/`patch`, then integrates the
configured `work` branch into the configured `develop` branch and pushes `develop`
to its remote tracking branch before returning to `work`.
- Param: extra Iterable of CLI argument strings; accepted token: `--help` only.
- Return: None; delegates to `_run_backup_command()`.
- Satisfies: REQ-047, REQ-048, REQ-049

### fn `def cmd_changelog(extra)` (L3435-3467)
- Brief: CLI entry-point for the `changelog` subcommand.
- Details: Parses flags, delegates to `generate_changelog_document`, and writes or prints the result.
Accepted flags: `--include-patch`, `--force-write`, `--print-only`,
`--disable-history`, `--help`.
Exits with status 2 on argument errors or when not inside a git repository.
Exits with status 1 when `CHANGELOG.md` already exists and `--force-write` was not supplied.
- Param: extra Iterable of CLI argument strings following the `changelog` subcommand token.
- Return: None; side-effects: writes `CHANGELOG.md` to disk or prints to stdout.
- Satisfies: REQ-018, REQ-040, REQ-041, REQ-043

- var `COMMANDS = {` (L3470)
- Brief: Constant `COMMANDS` used by CLI runtime paths and policies.
### fn `def print_command_help(name, width=None)` (L3551-3557)
- Brief: Execute `print_command_help` runtime logic for Git-Alias CLI.
- Details: Executes `print_command_help` using deterministic CLI control-flow and explicit error propagation.
- Param: name Input parameter consumed by `print_command_help`.
- Param: width Input parameter consumed by `print_command_help`.
- Return: Result emitted by `print_command_help` according to command contract.

### fn `def print_all_help()` (L3561-3595)
- Brief: Execute `print_all_help` runtime logic for Git-Alias CLI.
- Details: Executes `print_all_help` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `print_all_help` according to command contract.

### fn `def main(argv=None, *, check_updates: bool = True)` (L3601-3651)
- Brief: Execute `main` runtime logic for Git-Alias CLI.
- Details: Executes `main` using deterministic CLI control-flow and explicit error propagation.
- Param: argv Input parameter consumed by `main`.
- Param: check_updates Input parameter consumed by `main`.
- Return: Result emitted by `main` according to command contract.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`CONFIG_FILENAME`|var|pub|27||
|`GITHUB_LATEST_RELEASE_API`|var|pub|31||
|`VERSION_CHECK_CACHE_FILE`|var|pub|34||
|`VERSION_CHECK_TTL_HOURS`|var|pub|37||
|`DEFAULT_VER_RULES`|var|pub|41||
|`VERSION_CLEANUP_REGEXES`|var|pub|48||
|`VERSION_CLEANUP_PATTERNS`|var|pub|59||
|`DEFAULT_CONFIG`|var|pub|63||
|`CONFIG`|var|pub|78||
|`BRANCH_KEYS`|var|pub|81||
|`MANAGEMENT_HELP`|var|pub|84||
|`get_config_value`|fn|pub|98-101|def get_config_value(name)|
|`get_branch`|fn|pub|106-111|def get_branch(name)|
|`get_editor`|fn|pub|115-118|def get_editor()|
|`_load_config_rules`|fn|priv|124-149|def _load_config_rules(key, fallback)|
|`get_version_rules`|fn|pub|153-156|def get_version_rules()|
|`get_cli_version`|fn|pub|160-171|def get_cli_version()|
|`_normalize_semver_text`|fn|priv|176-182|def _normalize_semver_text(text: str) -> str|
|`check_for_newer_version`|fn|pub|187-271|def check_for_newer_version(timeout_seconds: float = 1.0)...|
|`get_git_root`|fn|pub|275-290|def get_git_root()|
|`get_config_path`|fn|pub|295-299|def get_config_path(root=None)|
|`load_cli_config`|fn|pub|304-338|def load_cli_config(root=None)|
|`write_default_config`|fn|pub|343-350|def write_default_config(root=None)|
|`_editor_base_command`|fn|priv|354-368|def _editor_base_command()|
|`run_editor_command`|fn|pub|373-375|def run_editor_command(args)|
|`HELP_TEXTS`|var|pub|378||
|`RESET_HELP_COMMANDS`|var|pub|538||
|`_to_args`|fn|priv|545-548|def _to_args(extra)|
|`CommandExecutionError`|class|pub|550-591|class CommandExecutionError(RuntimeError)|
|`CommandExecutionError.__init__`|fn|priv|555-562|def __init__(self, exc: subprocess.CalledProcessError)|
|`CommandExecutionError._format_message`|fn|priv|566-576|def _format_message(self) -> str|
|`CommandExecutionError._decode_stream`|fn|priv|581-591|def _decode_stream(data) -> str|
|`_run_checked`|fn|priv|597-604|def _run_checked(*popenargs, **kwargs)|
|`VersionDetectionError`|class|pub|606-609|class VersionDetectionError(RuntimeError)|
|`ReleaseError`|class|pub|611-614|class ReleaseError(RuntimeError)|
|`run_git_cmd`|fn|pub|622-626|def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)|
|`capture_git_output`|fn|pub|632-636|def capture_git_output(base_args, cwd=None)|
|`run_command`|fn|pub|642-645|def run_command(cmd, cwd=None)|
|`run_git_text`|fn|pub|652-669|def run_git_text(args, cwd=None, check=True)|
|`run_shell`|fn|pub|675-678|def run_shell(command, cwd=None)|
|`_git_status_lines`|fn|priv|682-694|def _git_status_lines()|
|`has_unstaged_changes`|fn|pub|699-710|def has_unstaged_changes(status_lines=None)|
|`has_staged_changes`|fn|pub|715-724|def has_staged_changes(status_lines=None)|
|`WIP_MESSAGE_RE`|var|pub|730||
|`_refresh_remote_refs`|fn|priv|736-747|def _refresh_remote_refs()|
|`_branch_remote_divergence`|fn|priv|753-771|def _branch_remote_divergence(branch_key, remote="origin")|
|`has_remote_branch_updates`|fn|pub|777-781|def has_remote_branch_updates(branch_key, remote="origin")|
|`has_remote_develop_updates`|fn|pub|785-788|def has_remote_develop_updates()|
|`has_remote_master_updates`|fn|pub|792-795|def has_remote_master_updates()|
|`_head_commit_message`|fn|priv|799-805|def _head_commit_message()|
|`_head_commit_hash`|fn|priv|809-815|def _head_commit_hash()|
|`_commit_exists_in_branch`|fn|priv|821-833|def _commit_exists_in_branch(commit_hash, branch_name)|
|`_should_amend_existing_commit`|fn|priv|837-852|def _should_amend_existing_commit()|
|`is_inside_git_repo`|fn|pub|856-863|def is_inside_git_repo()|
|`TagInfo`|class|pub|868-876|class TagInfo|
|`DELIM`|var|pub|879||
|`RECORD`|var|pub|882||
|`SEMVER_RE`|var|pub|898||
|`SECTION_EMOJI`|var|pub|901||
|`_tag_semver_tuple`|fn|priv|918-921|def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[in...|
|`_latest_supported_tag_name`|fn|priv|926-929|def _latest_supported_tag_name(tags: List[TagInfo]) -> Op...|
|`_is_minor_release_tag`|fn|priv|937-944|def _is_minor_release_tag(tag_name: str) -> bool|
|`_latest_patch_tag_after`|fn|priv|953-962|def _latest_patch_tag_after(all_tags: List[TagInfo], last...|
|`list_tags_sorted_by_date`|fn|pub|968-988|def list_tags_sorted_by_date(repo_root: Path, merged_ref:...|
|`git_log_subjects`|fn|pub|995-1006|def git_log_subjects(repo_root: Path, rev_range: str) -> ...|
|`parse_conventional_commit`|fn|pub|1012-1024|def parse_conventional_commit(message: str) -> Optional[T...|
|`_format_changelog_description`|fn|priv|1031-1042|def _format_changelog_description(desc: str) -> List[str]|
|`categorize_commit`|fn|pub|1050-1079|def categorize_commit(subject: str) -> Tuple[Optional[str...|
|`_extract_release_version`|fn|priv|1084-1094|def _extract_release_version(subject: str) -> Optional[str]|
|`_is_release_marker_commit`|fn|priv|1099-1102|def _is_release_marker_commit(subject: str) -> bool|
|`generate_section_for_range`|fn|pub|1111-1149|def generate_section_for_range(repo_root: Path, title: st...|
|`_get_remote_name_for_branch`|fn|priv|1158-1166|def _get_remote_name_for_branch(branch_name: str, repo_ro...|
|`_extract_owner_repo`|fn|priv|1173-1197|def _extract_owner_repo(remote_url: str) -> Optional[Tupl...|
|`_canonical_origin_base`|fn|priv|1207-1220|def _canonical_origin_base(repo_root: Path) -> Optional[str]|
|`get_origin_compare_url`|fn|pub|1227-1234|def get_origin_compare_url(base_url: Optional[str], prev_...|
|`get_release_page_url`|fn|pub|1240-1245|def get_release_page_url(base_url: Optional[str], tag: st...|
|`build_history_section`|fn|pub|1253-1257|def build_history_section(|
|`generate_changelog_document`|fn|pub|1301-1362|def generate_changelog_document(repo_root: Path, include_...|
|`VersionRuleContext`|class|pub|1373-1380|class VersionRuleContext|
|`_normalize_version_rule_pattern`|fn|priv|1386-1397|def _normalize_version_rule_pattern(pattern: str) -> str|
|`_build_version_file_inventory`|fn|priv|1403-1424|def _build_version_file_inventory(root: Path) -> List[Tup...|
|`_collect_version_files`|fn|priv|1432-1449|def _collect_version_files(root, pattern, *, inventory=None)|
|`_is_version_path_excluded`|fn|priv|1454-1457|def _is_version_path_excluded(relative_path: str) -> bool|
|`_iter_versions_in_text`|fn|priv|1463-1474|def _iter_versions_in_text(text, compiled_regexes)|
|`_read_version_file_text`|fn|priv|1481-1495|def _read_version_file_text(file_path: Path, text_cache: ...|
|`_prepare_version_rule_contexts`|fn|priv|1504-1505|def _prepare_version_rule_contexts(|
|`_determine_canonical_version`|fn|priv|1547-1554|def _determine_canonical_version(|
|`_parse_semver_tuple`|fn|priv|1599-1605|def _parse_semver_tuple(text: str) -> Optional[Tuple[int,...|
|`_replace_versions_in_text`|fn|priv|1612-1627|def _replace_versions_in_text(text, compiled_regex, repla...|
|`_current_branch_name`|fn|priv|1631-1643|def _current_branch_name()|
|`_ref_exists`|fn|priv|1648-1657|def _ref_exists(ref_name)|
|`_local_branch_exists`|fn|priv|1662-1665|def _local_branch_exists(branch_name)|
|`_remote_branch_exists`|fn|priv|1670-1673|def _remote_branch_exists(branch_name)|
|`_ensure_release_prerequisites`|fn|priv|1677-1704|def _ensure_release_prerequisites()|
|`_bump_semver_version`|fn|priv|1710-1728|def _bump_semver_version(current_version, level)|
|`_run_release_step`|fn|priv|1735-1755|def _run_release_step(level, step_name, action)|
|`_create_release_commit_for_flow`|fn|priv|1760-1765|def _create_release_commit_for_flow(target_version)|
|`_push_branch_with_tags`|fn|priv|1771-1775|def _push_branch_with_tags(branch_name)|
|`_execute_release_flow`|fn|priv|1791-1838|def _execute_release_flow(level, changelog_args=None)|
|`_execute_backup_flow`|fn|priv|1846-1861|def _execute_backup_flow()|
|`_run_release_command`|fn|priv|1867-1882|def _run_release_command(level, changelog_args=None)|
|`_run_backup_command`|fn|priv|1887-1894|def _run_backup_command()|
|`_run_reset_with_help`|fn|priv|1900-1907|def _run_reset_with_help(base_args, extra)|
|`_reject_extra_arguments`|fn|priv|1913-1919|def _reject_extra_arguments(extra, alias)|
|`_parse_release_flags`|fn|priv|1925-1943|def _parse_release_flags(extra, alias)|
|`_prepare_commit_message`|fn|priv|1949-1959|def _prepare_commit_message(extra, alias)|
|`_build_conventional_message`|fn|priv|1966-1980|def _build_conventional_message(kind: str, extra, alias: ...|
|`_run_conventional_commit`|fn|priv|1987-1992|def _run_conventional_commit(kind: str, alias: str, extra)|
|`_execute_commit`|fn|priv|1999-2028|def _execute_commit(message, alias, allow_amend=True)|
|`upgrade_self`|fn|pub|2032-2045|def upgrade_self()|
|`remove_self`|fn|pub|2049-2052|def remove_self()|
|`cmd_aa`|fn|pub|2057-2064|def cmd_aa(extra)|
|`cmd_ra`|fn|pub|2069-2092|def cmd_ra(extra)|
|`cmd_ar`|fn|pub|2097-2111|def cmd_ar(extra)|
|`cmd_br`|fn|pub|2116-2119|def cmd_br(extra)|
|`cmd_bd`|fn|pub|2124-2127|def cmd_bd(extra)|
|`cmd_ck`|fn|pub|2132-2135|def cmd_ck(extra)|
|`_ensure_commit_ready`|fn|priv|2140-2153|def _ensure_commit_ready(alias)|
|`cmd_cm`|fn|pub|2158-2163|def cmd_cm(extra)|
|`cmd_wip`|fn|pub|2168-2180|def cmd_wip(extra)|
|`cmd_release`|fn|pub|2185-2207|def cmd_release(extra)|
|`cmd_new`|fn|pub|2212-2215|def cmd_new(extra)|
|`cmd_refactor`|fn|pub|2220-2223|def cmd_refactor(extra)|
|`cmd_fix`|fn|pub|2228-2231|def cmd_fix(extra)|
|`cmd_change`|fn|pub|2236-2239|def cmd_change(extra)|
|`cmd_implement`|fn|pub|2244-2247|def cmd_implement(extra)|
|`cmd_docs`|fn|pub|2252-2255|def cmd_docs(extra)|
|`cmd_style`|fn|pub|2260-2263|def cmd_style(extra)|
|`cmd_revert`|fn|pub|2268-2271|def cmd_revert(extra)|
|`cmd_misc`|fn|pub|2276-2279|def cmd_misc(extra)|
|`cmd_cover`|fn|pub|2284-2287|def cmd_cover(extra)|
|`cmd_co`|fn|pub|2292-2295|def cmd_co(extra)|
|`cmd_dr`|fn|pub|2300-2307|def cmd_dr(extra)|
|`cmd_dcc`|fn|pub|2312-2315|def cmd_dcc(extra)|
|`cmd_dccc`|fn|pub|2320-2323|def cmd_dccc(extra)|
|`cmd_de`|fn|pub|2328-2331|def cmd_de(extra)|
|`cmd_di`|fn|pub|2336-2339|def cmd_di(extra)|
|`cmd_diyou`|fn|pub|2344-2347|def cmd_diyou(extra)|
|`cmd_dime`|fn|pub|2352-2355|def cmd_dime(extra)|
|`cmd_dwc`|fn|pub|2360-2363|def cmd_dwc(extra)|
|`cmd_dwcc`|fn|pub|2368-2371|def cmd_dwcc(extra)|
|`cmd_ed`|fn|pub|2376-2385|def cmd_ed(extra)|
|`cmd_fe`|fn|pub|2390-2393|def cmd_fe(extra)|
|`cmd_feall`|fn|pub|2398-2401|def cmd_feall(extra)|
|`cmd_gp`|fn|pub|2406-2409|def cmd_gp(extra)|
|`cmd_gr`|fn|pub|2414-2417|def cmd_gr(extra)|
|`OVERVIEW_COLOR_RESET`|var|pub|2419||
|`OVERVIEW_COLOR_SECTION_PURPLE`|var|pub|2421||
|`OVERVIEW_COLOR_AHEAD`|var|pub|2423||
|`OVERVIEW_COLOR_BEHIND`|var|pub|2425||
|`OVERVIEW_COLOR_LABEL`|var|pub|2427||
|`OVERVIEW_COLOR_WHITE`|var|pub|2429||
|`OVERVIEW_COLOR_WHITE_BOLD`|var|pub|2431||
|`OVERVIEW_SECTION_TEMPLATE`|var|pub|2433||
|`OVERVIEW_SUBSECTION_TEMPLATE`|var|pub|2435||
|`OVERVIEW_DISTANCE_TEMPLATE`|var|pub|2437||
|`_overview_branch_identifier`|fn|priv|2446-2449|def _overview_branch_identifier(|
|`_overview_logical_branch_name`|fn|priv|2466-2470|def _overview_logical_branch_name(|
|`_overview_current_branch_display`|fn|priv|2488-2492|def _overview_current_branch_display(|
|`_overview_ref_is_available`|fn|priv|2511-2520|def _overview_ref_is_available(ref_name: str) -> bool|
|`_overview_ref_latest_subject`|fn|priv|2526-2535|def _overview_ref_latest_subject(ref_name: str) -> str|
|`_overview_branch_summary_lines`|fn|priv|2552-2562|def _overview_branch_summary_lines(|
|`_overview_relation_state`|fn|priv|2590-2599|def _overview_relation_state(ahead: int, behind: int) -> str|
|`_overview_worktree_state`|fn|priv|2604-2616|def _overview_worktree_state(status_lines=None) -> str|
|`_overview_distance_text`|fn|priv|2622-2630|def _overview_distance_text(is_ahead: bool, count: int) -...|
|`_overview_compare_refs`|fn|priv|2637-2677|def _overview_compare_refs(base_ref: str, target_ref: str...|
|`_overview_ascii_topology_lines`|fn|priv|2698-2709|def _overview_ascii_topology_lines(|
|`cmd_o`|fn|pub|2797-2929|def cmd_o(extra)|
|`cmd_str`|fn|pub|2934-2963|def cmd_str(extra)|
|`cmd_lb`|fn|pub|2968-2971|def cmd_lb(extra)|
|`cmd_lg`|fn|pub|2976-2989|def cmd_lg(extra)|
|`cmd_lh`|fn|pub|2994-2997|def cmd_lh(extra)|
|`cmd_ll`|fn|pub|3002-3014|def cmd_ll(extra)|
|`cmd_lm`|fn|pub|3019-3022|def cmd_lm(extra)|
|`cmd_ls`|fn|pub|3028-3031|def cmd_ls(extra)|
|`cmd_lsi`|fn|pub|3037-3043|def cmd_lsi(extra)|
|`cmd_lsa`|fn|pub|3049-3052|def cmd_lsa(extra)|
|`cmd_lt`|fn|pub|3058-3077|def cmd_lt(extra)|
|`cmd_me`|fn|pub|3082-3085|def cmd_me(extra)|
|`cmd_pl`|fn|pub|3090-3093|def cmd_pl(extra)|
|`cmd_pt`|fn|pub|3098-3101|def cmd_pt(extra)|
|`cmd_pu`|fn|pub|3106-3109|def cmd_pu(extra)|
|`cmd_rf`|fn|pub|3114-3117|def cmd_rf(extra)|
|`cmd_rmtg`|fn|pub|3122-3132|def cmd_rmtg(extra)|
|`cmd_rmloc`|fn|pub|3137-3140|def cmd_rmloc(extra)|
|`cmd_rmstg`|fn|pub|3145-3148|def cmd_rmstg(extra)|
|`cmd_rmunt`|fn|pub|3153-3156|def cmd_rmunt(extra)|
|`cmd_rs`|fn|pub|3161-3164|def cmd_rs(extra)|
|`cmd_rssft`|fn|pub|3169-3172|def cmd_rssft(extra)|
|`cmd_rsmix`|fn|pub|3177-3180|def cmd_rsmix(extra)|
|`cmd_rshrd`|fn|pub|3185-3188|def cmd_rshrd(extra)|
|`cmd_rsmrg`|fn|pub|3193-3196|def cmd_rsmrg(extra)|
|`cmd_rskep`|fn|pub|3201-3204|def cmd_rskep(extra)|
|`cmd_st`|fn|pub|3209-3212|def cmd_st(extra)|
|`cmd_tg`|fn|pub|3217-3220|def cmd_tg(extra)|
|`cmd_unstg`|fn|pub|3225-3228|def cmd_unstg(extra)|
|`cmd_wt`|fn|pub|3233-3236|def cmd_wt(extra)|
|`cmd_wtl`|fn|pub|3241-3244|def cmd_wtl(extra)|
|`cmd_wtp`|fn|pub|3249-3252|def cmd_wtp(extra)|
|`cmd_wtr`|fn|pub|3257-3260|def cmd_wtr(extra)|
|`cmd_ver`|fn|pub|3265-3291|def cmd_ver(extra)|
|`cmd_chver`|fn|pub|3296-3368|def cmd_chver(extra)|
|`cmd_major`|fn|pub|3377-3381|def cmd_major(extra)|
|`cmd_minor`|fn|pub|3390-3394|def cmd_minor(extra)|
|`cmd_patch`|fn|pub|3403-3407|def cmd_patch(extra)|
|`cmd_backup`|fn|pub|3415-3425|def cmd_backup(extra)|
|`cmd_changelog`|fn|pub|3435-3467|def cmd_changelog(extra)|
|`COMMANDS`|var|pub|3470||
|`print_command_help`|fn|pub|3551-3557|def print_command_help(name, width=None)|
|`print_all_help`|fn|pub|3561-3595|def print_all_help()|
|`main`|fn|pub|3601-3651|def main(argv=None, *, check_updates: bool = True)|

