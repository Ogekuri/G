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

# core.py | Python | 3101L | 186 symbols | 16 imports | 820 comments
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
- var `RESET_HELP_COMMANDS = {"rs", "rshrd", "rskep", "rsmix", "rsmrg", "rssft"}` (L534)
- Brief: Constant `RESET_HELP_COMMANDS` used by CLI runtime paths and policies.
### fn `def _to_args(extra)` `priv` (L541-544)
- Brief: Execute `_to_args` runtime logic for Git-Alias CLI.
- Details: Executes `_to_args` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `_to_args`.
- Return: Result emitted by `_to_args` according to command contract.

### class `class CommandExecutionError(RuntimeError)` : RuntimeError (L546-587)
- Brief: Class `CommandExecutionError` models a typed runtime container/error boundary.
- Brief: Execute `__init__` runtime logic for Git-Alias CLI.
- Param: self Input parameter consumed by `__init__`.
- Param: exc Input parameter consumed by `__init__`.
- fn `def __init__(self, exc: subprocess.CalledProcessError)` `priv` (L551-558)
  - Brief: Execute `__init__` runtime logic for Git-Alias CLI.
  - Param: self Input parameter consumed by `__init__`.
  - Param: exc Input parameter consumed by `__init__`.
  - Return: Result emitted by `__init__` according to command contract.
- fn `def _format_message(self) -> str` `priv` (L562-572)
  - Brief: Execute `_format_message` runtime logic for Git-Alias CLI.
  - Param: self Input parameter consumed by `_format_message`.
  - Return: Result emitted by `_format_message` according to command contract.
- fn `def _decode_stream(data) -> str` `priv` (L577-587)
  - Brief: Execute `_decode_stream` runtime logic for Git-Alias CLI.
  - Param: data Input parameter consumed by `_decode_stream`.
  - Return: Result emitted by `_decode_stream` according to command contract.

### fn `def _run_checked(*popenargs, **kwargs)` `priv` (L593-600)
- Brief: Execute `_run_checked` runtime logic for Git-Alias CLI.
- Details: Executes `_run_checked` using deterministic CLI control-flow and explicit error propagation.
- Param: *popenargs Input parameter consumed by `_run_checked`.
- Param: **kwargs Input parameter consumed by `_run_checked`.
- Return: Result emitted by `_run_checked` according to command contract.

### class `class VersionDetectionError(RuntimeError)` : RuntimeError (L602-605)
- Brief: Class `VersionDetectionError` models a typed runtime container/error boundary.

### class `class ReleaseError(RuntimeError)` : RuntimeError (L607-610)
- Brief: Class `ReleaseError` models a typed runtime container/error boundary.

### fn `def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)` (L618-622)
- Brief: Execute `run_git_cmd` runtime logic for Git-Alias CLI.
- Details: Executes `run_git_cmd` using deterministic CLI control-flow and explicit error propagation.
- Param: base_args Input parameter consumed by `run_git_cmd`.
- Param: extra Input parameter consumed by `run_git_cmd`.
- Param: cwd Input parameter consumed by `run_git_cmd`.
- Param: **kwargs Input parameter consumed by `run_git_cmd`.
- Return: Result emitted by `run_git_cmd` according to command contract.

### fn `def capture_git_output(base_args, cwd=None)` (L628-632)
- Brief: Execute `capture_git_output` runtime logic for Git-Alias CLI.
- Details: Executes `capture_git_output` using deterministic CLI control-flow and explicit error propagation.
- Param: base_args Input parameter consumed by `capture_git_output`.
- Param: cwd Input parameter consumed by `capture_git_output`.
- Return: Result emitted by `capture_git_output` according to command contract.

### fn `def run_command(cmd, cwd=None)` (L638-641)
- Brief: Execute `run_command` runtime logic for Git-Alias CLI.
- Details: Executes `run_command` using deterministic CLI control-flow and explicit error propagation.
- Param: cmd Input parameter consumed by `run_command`.
- Param: cwd Input parameter consumed by `run_command`.
- Return: Result emitted by `run_command` according to command contract.

### fn `def run_git_text(args, cwd=None, check=True)` (L648-665)
- Brief: Execute `run_git_text` runtime logic for Git-Alias CLI.
- Details: Executes `run_git_text` using deterministic CLI control-flow and explicit error propagation.
- Param: args Input parameter consumed by `run_git_text`.
- Param: cwd Input parameter consumed by `run_git_text`.
- Param: check Input parameter consumed by `run_git_text`.
- Return: Result emitted by `run_git_text` according to command contract.

### fn `def run_shell(command, cwd=None)` (L671-674)
- Brief: Execute `run_shell` runtime logic for Git-Alias CLI.
- Details: Executes `run_shell` using deterministic CLI control-flow and explicit error propagation.
- Param: command Input parameter consumed by `run_shell`.
- Param: cwd Input parameter consumed by `run_shell`.
- Return: Result emitted by `run_shell` according to command contract.

### fn `def _git_status_lines()` `priv` (L678-690)
- Brief: Execute `_git_status_lines` runtime logic for Git-Alias CLI.
- Details: Executes `_git_status_lines` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_git_status_lines` according to command contract.

### fn `def has_unstaged_changes(status_lines=None)` (L695-706)
- Brief: Execute `has_unstaged_changes` runtime logic for Git-Alias CLI.
- Details: Executes `has_unstaged_changes` using deterministic CLI control-flow and explicit error propagation.
- Param: status_lines Input parameter consumed by `has_unstaged_changes`.
- Return: Result emitted by `has_unstaged_changes` according to command contract.

### fn `def has_staged_changes(status_lines=None)` (L711-720)
- Brief: Execute `has_staged_changes` runtime logic for Git-Alias CLI.
- Details: Executes `has_staged_changes` using deterministic CLI control-flow and explicit error propagation.
- Param: status_lines Input parameter consumed by `has_staged_changes`.
- Return: Result emitted by `has_staged_changes` according to command contract.

- var `WIP_MESSAGE_RE = re.compile(r"^wip: work in progress\.$")` (L726)
- Brief: Constant `WIP_MESSAGE_RE` used by CLI runtime paths and policies.
### fn `def _refresh_remote_refs()` `priv` (L732-743)
- Brief: Execute `_refresh_remote_refs` runtime logic for Git-Alias CLI.
- Details: Executes `_refresh_remote_refs` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_refresh_remote_refs` according to command contract.

### fn `def _branch_remote_divergence(branch_key, remote="origin")` `priv` (L749-767)
- Brief: Execute `_branch_remote_divergence` runtime logic for Git-Alias CLI.
- Details: Executes `_branch_remote_divergence` using deterministic CLI control-flow and explicit error propagation.
- Param: branch_key Input parameter consumed by `_branch_remote_divergence`.
- Param: remote Input parameter consumed by `_branch_remote_divergence`.
- Return: Result emitted by `_branch_remote_divergence` according to command contract.

### fn `def has_remote_branch_updates(branch_key, remote="origin")` (L773-777)
- Brief: Execute `has_remote_branch_updates` runtime logic for Git-Alias CLI.
- Details: Executes `has_remote_branch_updates` using deterministic CLI control-flow and explicit error propagation.
- Param: branch_key Input parameter consumed by `has_remote_branch_updates`.
- Param: remote Input parameter consumed by `has_remote_branch_updates`.
- Return: Result emitted by `has_remote_branch_updates` according to command contract.

### fn `def has_remote_develop_updates()` (L781-784)
- Brief: Execute `has_remote_develop_updates` runtime logic for Git-Alias CLI.
- Details: Executes `has_remote_develop_updates` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `has_remote_develop_updates` according to command contract.

### fn `def has_remote_master_updates()` (L788-791)
- Brief: Execute `has_remote_master_updates` runtime logic for Git-Alias CLI.
- Details: Executes `has_remote_master_updates` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `has_remote_master_updates` according to command contract.

### fn `def _head_commit_message()` `priv` (L795-801)
- Brief: Execute `_head_commit_message` runtime logic for Git-Alias CLI.
- Details: Executes `_head_commit_message` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_head_commit_message` according to command contract.

### fn `def _head_commit_hash()` `priv` (L805-811)
- Brief: Execute `_head_commit_hash` runtime logic for Git-Alias CLI.
- Details: Executes `_head_commit_hash` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_head_commit_hash` according to command contract.

### fn `def _commit_exists_in_branch(commit_hash, branch_name)` `priv` (L817-829)
- Brief: Execute `_commit_exists_in_branch` runtime logic for Git-Alias CLI.
- Details: Executes `_commit_exists_in_branch` using deterministic CLI control-flow and explicit error propagation.
- Param: commit_hash Input parameter consumed by `_commit_exists_in_branch`.
- Param: branch_name Input parameter consumed by `_commit_exists_in_branch`.
- Return: Result emitted by `_commit_exists_in_branch` according to command contract.

### fn `def _should_amend_existing_commit()` `priv` (L833-848)
- Brief: Execute `_should_amend_existing_commit` runtime logic for Git-Alias CLI.
- Details: Executes `_should_amend_existing_commit` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_should_amend_existing_commit` according to command contract.

### fn `def is_inside_git_repo()` (L852-859)
- Brief: Execute `is_inside_git_repo` runtime logic for Git-Alias CLI.
- Details: Executes `is_inside_git_repo` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `is_inside_git_repo` according to command contract.

### class `class TagInfo` (L864-872)
- Brief: Class `TagInfo` models a typed runtime container/error boundary.
- Brief: Store raw tag name including `v` prefix when present.
- Brief: Store ISO date string used for changelog section headers.
- Details: Encapsulates tag identity, tag date, and resolved Git object identifier for changelog assembly.

- var `DELIM = "\x1f"` (L875)
- Brief: Constant `DELIM` used by CLI runtime paths and policies.
- var `RECORD = "\x1e"` (L878)
- Brief: Constant `RECORD` used by CLI runtime paths and policies.
- var `SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")` (L894)
- Brief: Constant `SEMVER_RE` used by CLI runtime paths and policies.
- var `SECTION_EMOJI = {` (L897)
- Brief: Constant `SECTION_EMOJI` used by CLI runtime paths and policies.
### fn `def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[int, int, int]]` `priv` (L914-917)
- Brief: Execute `_tag_semver_tuple` runtime logic for Git-Alias CLI.
- Details: Executes `_tag_semver_tuple` using deterministic CLI control-flow and explicit error propagation.
- Param: tag_name Input parameter consumed by `_tag_semver_tuple`.
- Return: Result emitted by `_tag_semver_tuple` according to command contract.

### fn `def _latest_supported_tag_name(tags: List[TagInfo]) -> Optional[str]` `priv` (L922-925)
- Brief: Execute `_latest_supported_tag_name` runtime logic for Git-Alias CLI.
- Details: Executes `_latest_supported_tag_name` using deterministic CLI control-flow and explicit error propagation.
- Param: tags Input parameter consumed by `_latest_supported_tag_name`.
- Return: Result emitted by `_latest_supported_tag_name` according to command contract.

### fn `def _is_minor_release_tag(tag_name: str) -> bool` `priv` (L933-940)
- Brief: Predicate: tag is a minor release.
- Details: Returns `True` when `tag_name` is a semver tag where `patch==0` AND `(major>=1 OR minor>=1)`,
i.e. version `>=0.1.0` with no patch component.
Patch releases (`patch>0`) and pre-0.1.0 tags (`0.0.x`) return `False`.
- Param: tag_name Semver tag string, optionally prefixed with `v` (e.g. `v0.1.0`, `0.2.0`).
- Return: `True` iff tag represents a minor release; `False` otherwise.
- Satisfies: REQ-018, REQ-040

### fn `def _latest_patch_tag_after(all_tags: List[TagInfo], last_minor: Optional[TagInfo]) -> Optional[TagInfo]` `priv` (L949-958)
- Brief: Locate the chronologically latest patch tag after a given minor release.
- Details: Scans `all_tags` (sorted chronologically, ascending) for tags that are NOT minor releases
and appear after `last_minor` in the list. When `last_minor` is `None`, scans all tags.
Returns the last qualifying `TagInfo` (most recent), or `None` if no patch exists.
- Param: all_tags Full list of `TagInfo` sorted by date ascending (from `list_tags_sorted_by_date`).
- Param: last_minor The last minor-release `TagInfo` to anchor the search; `None` means no minor exists.
- Return: Most recent `TagInfo` that is not a minor release and appears after `last_minor`, or `None`.
- Satisfies: REQ-040

### fn `def list_tags_sorted_by_date(repo_root: Path, merged_ref: Optional[str] = None) -> List[TagInfo]` (L964-984)
- Brief: Execute `list_tags_sorted_by_date` runtime logic for Git-Alias CLI.
- Details: Executes `list_tags_sorted_by_date` using deterministic CLI control-flow and explicit error propagation.
- Param: repo_root Input parameter consumed by `list_tags_sorted_by_date`.
- Param: merged_ref Input parameter consumed by `list_tags_sorted_by_date`.
- Return: Result emitted by `list_tags_sorted_by_date` according to command contract.

### fn `def git_log_subjects(repo_root: Path, rev_range: str) -> List[str]` (L991-1002)
- Brief: Execute `git_log_subjects` runtime logic for Git-Alias CLI.
- Details: Executes `git_log_subjects` using deterministic CLI control-flow and explicit error propagation.
Reads full commit messages (subject + body) to preserve multiline conventional descriptions.
- Param: repo_root Input parameter consumed by `git_log_subjects`.
- Param: rev_range Input parameter consumed by `git_log_subjects`.
- Return: Result emitted by `git_log_subjects` according to command contract.

### fn `def parse_conventional_commit(message: str) -> Optional[Tuple[str, Optional[str], bool, str]]` (L1008-1020)
- Brief: Execute `parse_conventional_commit` runtime logic for Git-Alias CLI.
- Details: Parses a conventional-commit header with optional scope and optional breaking marker (`!`),
then returns extracted type/scope/breaking/description fields for changelog rendering.
- Param: message Raw commit message text (subject and optional body).
- Return: Tuple `(type, scope, breaking, description)` when message is parseable; otherwise `None`.

### fn `def _format_changelog_description(desc: str) -> List[str]` `priv` (L1027-1037)
- Brief: Execute `_format_changelog_description` runtime logic for Git-Alias CLI.
- Details: Normalizes a commit description for markdown list rendering while preserving logical lines.
Removes `Co-authored-by:` trailer lines, drops empty lines, and strips leading markdown-list
markers from continuation lines so multiline descriptions can be rendered as nested bullets.
- Param: desc Parsed commit description.
- Return: Ordered non-empty description lines ready for markdown rendering.

### fn `def categorize_commit(subject: str) -> Tuple[Optional[str], str]` (L1046-1073)
- Brief: Execute `categorize_commit` runtime logic for Git-Alias CLI.
- Details: Parses a conventional commit message and maps it to a changelog section and formatted entry line.
Entry format: `- <description> *(<scope>)*` when scope is present; `- <description>` otherwise.
Multiline descriptions are rendered as consecutive indented sub-bullets under the commit line.
When the breaking marker is present, the first description line is prefixed with `BREAKING CHANGE: `.
- Param: subject Conventional commit message string.
- Return: Tuple `(section, line)`: `section` is the changelog section name or `None` if type is unmapped or ignored; `line` is the formatted entry string or `""` when section is `None`.

### fn `def _extract_release_version(subject: str) -> Optional[str]` `priv` (L1077-1087)
- Brief: Execute `_extract_release_version` runtime logic for Git-Alias CLI.
- Details: Executes `_extract_release_version` using deterministic CLI control-flow and explicit error propagation.
- Param: subject Input parameter consumed by `_extract_release_version`.
- Return: Result emitted by `_extract_release_version` according to command contract.

### fn `def _is_release_marker_commit(subject: str) -> bool` `priv` (L1092-1095)
- Brief: Execute `_is_release_marker_commit` runtime logic for Git-Alias CLI.
- Details: Executes `_is_release_marker_commit` using deterministic CLI control-flow and explicit error propagation.
- Param: subject Input parameter consumed by `_is_release_marker_commit`.
- Return: Result emitted by `_is_release_marker_commit` according to command contract.

### fn `def generate_section_for_range(repo_root: Path, title: str, date_s: str, rev_range: str, expected_version: Optional[str] = None) -> Optional[str]` (L1107-1143)
- Brief: Execute `generate_section_for_range` runtime logic for Git-Alias CLI.
- Details: Executes `generate_section_for_range` using deterministic CLI control-flow and explicit error propagation; section entries are rendered as consecutive top-level bullets without blank separator lines.
- Param: repo_root Input parameter consumed by `generate_section_for_range`.
- Param: title Input parameter consumed by `generate_section_for_range`.
- Param: date_s Input parameter consumed by `generate_section_for_range`.
- Param: rev_range Input parameter consumed by `generate_section_for_range`.
- Param: expected_version Input parameter consumed by `generate_section_for_range`.
- Return: Result emitted by `generate_section_for_range` according to command contract.

### fn `def _get_remote_name_for_branch(branch_name: str, repo_root: Path) -> str` `priv` (L1154-1160)
- Brief: Resolve the git remote name configured for a given branch.
- Details: Queries `git config branch.<branch_name>.remote` via a local git command.
Returns `origin` as fallback when the config key is absent or the command fails.
No network operations are performed.
- Param: branch_name Local branch name whose configured remote is requested (e.g. `"master"`).
- Param: repo_root Absolute path used as CWD for the git config query.
- Return: Remote name string; never empty (falls back to `"origin"`).
- Satisfies: REQ-046

### fn `def _extract_owner_repo(remote_url: str) -> Optional[Tuple[str, str]]` `priv` (L1169-1191)
- Brief: Resolve the normalized HTTPS base URL from the master branch's configured remote.
- Details: Parses both SSH (`git@<host>:<owner>/<repo>[.git]`) and HTTPS
(`https://<host>/<owner>/<repo>[.git]`) formats and extracts `<owner>` and `<repo>`
through deterministic string parsing.
- Param: remote_url Raw git remote URL string.
- Return: Tuple `(owner, repo)` when parsing succeeds; otherwise `None`.

### fn `def _canonical_origin_base(repo_root: Path) -> Optional[str]` `priv` (L1203-1214)
- Brief: Resolve normalized GitHub URL base from the master-branch configured remote.
- Details: Determines remote name using `_get_remote_name_for_branch` with the configured
master branch, then executes local `git remote get-url <remote>` command.
If command execution fails or URL parsing fails, returns `None`.
On success, always emits `https://github.com/<owner>/<repo>` for changelog templates.
No network operation is performed; all data is derived from local git metadata.
- Param: repo_root Absolute path to the repository root used as CWD for all git commands.
- Return: Normalized HTTPS base URL string (no trailing `.git`), or `None` on failure.
- Satisfies: REQ-043, REQ-046

### fn `def get_origin_compare_url(base_url: Optional[str], prev_tag: Optional[str], tag: str) -> Optional[str]` (L1220-1227)
- Brief: Execute `get_origin_compare_url` runtime logic for Git-Alias CLI.
- Details: Executes `get_origin_compare_url` using deterministic CLI control-flow and explicit error propagation.
- Param: base_url Input parameter consumed by `get_origin_compare_url`.
- Param: prev_tag Input parameter consumed by `get_origin_compare_url`.
- Param: tag Input parameter consumed by `get_origin_compare_url`.
- Return: Result emitted by `get_origin_compare_url` according to command contract.

### fn `def get_release_page_url(base_url: Optional[str], tag: str) -> Optional[str]` (L1233-1238)
- Brief: Execute `get_release_page_url` runtime logic for Git-Alias CLI.
- Details: Executes `get_release_page_url` using deterministic CLI control-flow and explicit error propagation.
- Param: base_url Input parameter consumed by `get_release_page_url`.
- Param: tag Input parameter consumed by `get_release_page_url`.
- Return: Result emitted by `get_release_page_url` according to command contract.

### fn `def build_history_section(` (L1246-1250)
- Brief: Execute `build_history_section` runtime logic for Git-Alias CLI.
- Details: Executes `build_history_section` using deterministic CLI control-flow and explicit error propagation.
- Param: repo_root Input parameter consumed by `build_history_section`.
- Param: tags Input parameter consumed by `build_history_section`.
- Param: include_unreleased Input parameter consumed by `build_history_section`.
- Param: include_unreleased_link Input parameter consumed by `build_history_section`.
- Return: Result emitted by `build_history_section` according to command contract.

### fn `def generate_changelog_document(repo_root: Path, include_patch: bool, disable_history: bool = False) -> str` (L1297-1356)
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

### class `class VersionRuleContext` `@dataclass(frozen=True)` (L1366-1373)

### fn `def _normalize_version_rule_pattern(pattern: str) -> str` `priv` (L1379-1390)
- Brief: Normalize a `ver_rules` pattern to the internal pathspec matching form.
- Details: Converts separators to POSIX style, strips leading `./`, and anchors patterns containing `/`
to repository root by prefixing `/` when missing, preserving REQ-017 semantics.
- Param: pattern Input pattern string from configuration.
- Return: Normalized pathspec-compatible pattern string; empty string when input is blank.

### fn `def _build_version_file_inventory(root: Path) -> List[Tuple[Path, str]]` `priv` (L1396-1417)
- Brief: Build a deduplicated repository file inventory for version rule evaluation.
- Details: Executes a single `rglob("*")` traversal from repository root, filters to files only,
applies hardcoded exclusion regexes, normalizes relative paths, and deduplicates by resolved path.
- Param: root Repository root path used as traversal anchor.
- Return: List of tuples `(absolute_path, normalized_relative_path)` used by downstream matchers.

### fn `def _collect_version_files(root, pattern, *, inventory=None)` `priv` (L1425-1442)
- Brief: Execute `_collect_version_files` runtime logic for Git-Alias CLI.
- Details: Executes `_collect_version_files` using deterministic CLI control-flow and explicit error propagation.
Uses precomputed inventory when provided to avoid repeated repository traversals.
- Param: root Input parameter consumed by `_collect_version_files`.
- Param: pattern Input parameter consumed by `_collect_version_files`.
- Param: inventory Optional precomputed `(path, normalized_relative_path)` list.
- Return: Result emitted by `_collect_version_files` according to command contract.

### fn `def _is_version_path_excluded(relative_path: str) -> bool` `priv` (L1447-1450)
- Brief: Execute `_is_version_path_excluded` runtime logic for Git-Alias CLI.
- Details: Executes `_is_version_path_excluded` using deterministic CLI control-flow and explicit error propagation.
- Param: relative_path Input parameter consumed by `_is_version_path_excluded`.
- Return: Result emitted by `_is_version_path_excluded` according to command contract.

### fn `def _iter_versions_in_text(text, compiled_regexes)` `priv` (L1456-1467)
- Brief: Execute `_iter_versions_in_text` runtime logic for Git-Alias CLI.
- Details: Executes `_iter_versions_in_text` using deterministic CLI control-flow and explicit error propagation.
- Param: text Input parameter consumed by `_iter_versions_in_text`.
- Param: compiled_regexes Input parameter consumed by `_iter_versions_in_text`.
- Return: Result emitted by `_iter_versions_in_text` according to command contract.

### fn `def _read_version_file_text(file_path: Path, text_cache: Optional[Dict[Path, str]] = None) -> Optional[str]` `priv` (L1474-1488)
- Brief: Read and cache UTF-8 text content for a version-managed file.
- Details: Loads file content with UTF-8 decoding; falls back to `errors="ignore"` on decode failures.
Emits deterministic stderr diagnostics on I/O failure and returns `None` for caller-managed skip logic.
- Param: file_path Absolute path of the file to read.
- Param: text_cache Optional mutable cache keyed by `Path` to avoid duplicate reads across phases.
- Return: File text payload or `None` when file cannot be read.

### fn `def _prepare_version_rule_contexts(` `priv` (L1497-1498)
- Brief: Build reusable per-rule contexts for canonical version evaluation workflows.
- Details: Resolves matched files and compiled regex for each `(pattern, regex)` rule exactly once.
Preserves error contracts for unmatched patterns and invalid regex declarations.
- Param: root Repository root path used for relative-path rendering.
- Param: rules Sequence of `(pattern, regex)` tuples.
- Param: inventory Optional precomputed inventory to avoid repeated filesystem traversal.
- Return: Ordered list of `VersionRuleContext` objects aligned to input rule order.
- Throws: VersionDetectionError when a rule matches no files or contains an invalid regex.

### fn `def _determine_canonical_version(` `priv` (L1540-1547)
- Brief: Execute `_determine_canonical_version` runtime logic for Git-Alias CLI.
- Details: Executes `_determine_canonical_version` using deterministic CLI control-flow and explicit error propagation.
- Param: root Input parameter consumed by `_determine_canonical_version`.
- Param: rules Input parameter consumed by `_determine_canonical_version`.
- Param: verbose Input parameter consumed by `_determine_canonical_version`.
- Param: debug Input parameter consumed by `_determine_canonical_version`.
- Param: contexts Optional precomputed `VersionRuleContext` list for reuse across phases.
- Param: text_cache Optional mutable cache keyed by file path to avoid duplicate reads.
- Return: Result emitted by `_determine_canonical_version` according to command contract.

### fn `def _parse_semver_tuple(text: str) -> Optional[Tuple[int, int, int]]` `priv` (L1592-1598)
- Brief: Execute `_parse_semver_tuple` runtime logic for Git-Alias CLI.
- Details: Executes `_parse_semver_tuple` using deterministic CLI control-flow and explicit error propagation.
- Param: text Input parameter consumed by `_parse_semver_tuple`.
- Return: Result emitted by `_parse_semver_tuple` according to command contract.

### fn `def _replace_versions_in_text(text, compiled_regex, replacement)` `priv` (L1605-1620)
- Brief: Execute `_replace_versions_in_text` runtime logic for Git-Alias CLI.
- Details: Executes `_replace_versions_in_text` using deterministic CLI control-flow and explicit error propagation.
- Param: text Input parameter consumed by `_replace_versions_in_text`.
- Param: compiled_regex Input parameter consumed by `_replace_versions_in_text`.
- Param: replacement Input parameter consumed by `_replace_versions_in_text`.
- Return: Result emitted by `_replace_versions_in_text` according to command contract.

### fn `def _current_branch_name()` `priv` (L1624-1636)
- Brief: Execute `_current_branch_name` runtime logic for Git-Alias CLI.
- Details: Executes `_current_branch_name` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_current_branch_name` according to command contract.

### fn `def _ref_exists(ref_name)` `priv` (L1641-1650)
- Brief: Execute `_ref_exists` runtime logic for Git-Alias CLI.
- Details: Executes `_ref_exists` using deterministic CLI control-flow and explicit error propagation.
- Param: ref_name Input parameter consumed by `_ref_exists`.
- Return: Result emitted by `_ref_exists` according to command contract.

### fn `def _local_branch_exists(branch_name)` `priv` (L1655-1658)
- Brief: Execute `_local_branch_exists` runtime logic for Git-Alias CLI.
- Details: Executes `_local_branch_exists` using deterministic CLI control-flow and explicit error propagation.
- Param: branch_name Input parameter consumed by `_local_branch_exists`.
- Return: Result emitted by `_local_branch_exists` according to command contract.

### fn `def _remote_branch_exists(branch_name)` `priv` (L1663-1666)
- Brief: Execute `_remote_branch_exists` runtime logic for Git-Alias CLI.
- Details: Executes `_remote_branch_exists` using deterministic CLI control-flow and explicit error propagation.
- Param: branch_name Input parameter consumed by `_remote_branch_exists`.
- Return: Result emitted by `_remote_branch_exists` according to command contract.

### fn `def _ensure_release_prerequisites()` `priv` (L1670-1697)
- Brief: Execute `_ensure_release_prerequisites` runtime logic for Git-Alias CLI.
- Details: Executes `_ensure_release_prerequisites` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `_ensure_release_prerequisites` according to command contract.

### fn `def _bump_semver_version(current_version, level)` `priv` (L1703-1721)
- Brief: Execute `_bump_semver_version` runtime logic for Git-Alias CLI.
- Details: Executes `_bump_semver_version` using deterministic CLI control-flow and explicit error propagation.
- Param: current_version Input parameter consumed by `_bump_semver_version`.
- Param: level Input parameter consumed by `_bump_semver_version`.
- Return: Result emitted by `_bump_semver_version` according to command contract.

### fn `def _run_release_step(level, step_name, action)` `priv` (L1728-1748)
- Brief: Execute `_run_release_step` runtime logic for Git-Alias CLI.
- Details: Executes `_run_release_step` using deterministic CLI control-flow and explicit error propagation.
- Param: level Input parameter consumed by `_run_release_step`.
- Param: step_name Input parameter consumed by `_run_release_step`.
- Param: action Input parameter consumed by `_run_release_step`.
- Return: Result emitted by `_run_release_step` according to command contract.

### fn `def _create_release_commit_for_flow(target_version)` `priv` (L1753-1758)
- Brief: Execute `_create_release_commit_for_flow` runtime logic for Git-Alias CLI.
- Details: Executes release-flow first-commit creation with WIP amend semantics reused from `_execute_commit`.
- Param: target_version Input parameter consumed by `_create_release_commit_for_flow`.
- Return: Result emitted by `_create_release_commit_for_flow` according to command contract.

### fn `def _push_branch_with_tags(branch_name)` `priv` (L1764-1768)
- Brief: Execute `_push_branch_with_tags` runtime logic for Git-Alias CLI.
- Details: Pushes the specified local branch to `origin` using an explicit branch refspec and
includes `--tags` in the same push command.
- Param: branch_name Local branch name resolved from configured release branches.
- Return: Result emitted by `run_git_cmd` according to command contract.

### fn `def _execute_release_flow(level, changelog_args=None)` `priv` (L1784-1831)
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

### fn `def _execute_backup_flow()` `priv` (L1839-1854)
- Brief: Execute `_execute_backup_flow` runtime logic for Git-Alias CLI.
- Details: Executes the `backup` workflow by reusing the release preflight checks, then
fast-forward merges configured `work` into configured `develop`, pushes `develop`
to its configured remote tracking branch, checks out back to `work`, and prints
an explicit success confirmation.
- Return: None; raises `ReleaseError` on preflight or workflow failure.
- Satisfies: REQ-047, REQ-048, REQ-049

### fn `def _run_release_command(level, changelog_args=None)` `priv` (L1860-1875)
- Brief: Execute `_run_release_command` runtime logic for Git-Alias CLI.
- Details: Executes `_run_release_command` using deterministic CLI control-flow and explicit error propagation.
- Param: level Input parameter consumed by `_run_release_command`.
- Param: changelog_args Input parameter consumed by `_run_release_command`.
- Return: Result emitted by `_run_release_command` according to command contract.

### fn `def _run_backup_command()` `priv` (L1880-1887)
- Brief: Execute `_run_backup_command` runtime logic for Git-Alias CLI.
- Details: Runs the `backup` workflow with the same error propagation strategy used by release commands.
- Return: None; exits with status 1 on `ReleaseError`.
- Satisfies: REQ-047, REQ-048, REQ-049

### fn `def _run_reset_with_help(base_args, extra)` `priv` (L1893-1900)
- Brief: Execute `_run_reset_with_help` runtime logic for Git-Alias CLI.
- Details: Executes `_run_reset_with_help` using deterministic CLI control-flow and explicit error propagation.
- Param: base_args Input parameter consumed by `_run_reset_with_help`.
- Param: extra Input parameter consumed by `_run_reset_with_help`.
- Return: Result emitted by `_run_reset_with_help` according to command contract.

### fn `def _reject_extra_arguments(extra, alias)` `priv` (L1906-1912)
- Brief: Execute `_reject_extra_arguments` runtime logic for Git-Alias CLI.
- Details: Executes `_reject_extra_arguments` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `_reject_extra_arguments`.
- Param: alias Input parameter consumed by `_reject_extra_arguments`.
- Return: Result emitted by `_reject_extra_arguments` according to command contract.

### fn `def _parse_release_flags(extra, alias)` `priv` (L1918-1936)
- Brief: Execute `_parse_release_flags` runtime logic for Git-Alias CLI.
- Details: Executes `_parse_release_flags` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `_parse_release_flags`.
- Param: alias Input parameter consumed by `_parse_release_flags`.
- Return: Result emitted by `_parse_release_flags` according to command contract.

### fn `def _prepare_commit_message(extra, alias)` `priv` (L1942-1952)
- Brief: Execute `_prepare_commit_message` runtime logic for Git-Alias CLI.
- Details: Executes `_prepare_commit_message` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `_prepare_commit_message`.
- Param: alias Input parameter consumed by `_prepare_commit_message`.
- Return: Result emitted by `_prepare_commit_message` according to command contract.

### fn `def _build_conventional_message(kind: str, extra, alias: str) -> str` `priv` (L1959-1973)
- Brief: Execute `_build_conventional_message` runtime logic for Git-Alias CLI.
- Details: Executes `_build_conventional_message` using deterministic CLI control-flow and explicit error propagation.
- Param: kind Input parameter consumed by `_build_conventional_message`.
- Param: extra Input parameter consumed by `_build_conventional_message`.
- Param: alias Input parameter consumed by `_build_conventional_message`.
- Return: Result emitted by `_build_conventional_message` according to command contract.

### fn `def _run_conventional_commit(kind: str, alias: str, extra)` `priv` (L1980-1985)
- Brief: Execute `_run_conventional_commit` runtime logic for Git-Alias CLI.
- Details: Executes `_run_conventional_commit` using deterministic CLI control-flow and explicit error propagation.
- Param: kind Input parameter consumed by `_run_conventional_commit`.
- Param: alias Input parameter consumed by `_run_conventional_commit`.
- Param: extra Input parameter consumed by `_run_conventional_commit`.
- Return: Result emitted by `_run_conventional_commit` according to command contract.

### fn `def _execute_commit(message, alias, allow_amend=True)` `priv` (L1992-2021)
- Brief: Execute `_execute_commit` runtime logic for Git-Alias CLI.
- Details: Executes `_execute_commit` using deterministic CLI control-flow and explicit error propagation.
- Param: message Input parameter consumed by `_execute_commit`.
- Param: alias Input parameter consumed by `_execute_commit`.
- Param: allow_amend Input parameter consumed by `_execute_commit`.
- Return: Result emitted by `_execute_commit` according to command contract.

### fn `def upgrade_self()` (L2025-2038)
- Brief: Execute `upgrade_self` runtime logic for Git-Alias CLI.
- Details: Executes `upgrade_self` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `upgrade_self` according to command contract.

### fn `def remove_self()` (L2042-2045)
- Brief: Execute `remove_self` runtime logic for Git-Alias CLI.
- Details: Executes `remove_self` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `remove_self` according to command contract.

### fn `def cmd_aa(extra)` (L2050-2057)
- Brief: Execute `cmd_aa` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_aa` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_aa`.
- Return: Result emitted by `cmd_aa` according to command contract.

### fn `def cmd_ra(extra)` (L2062-2085)
- Brief: Execute `cmd_ra` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ra` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ra`.
- Return: Result emitted by `cmd_ra` according to command contract.

### fn `def cmd_ar(extra)` (L2090-2104)
- Brief: Execute `cmd_ar` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ar` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ar`.
- Return: Result emitted by `cmd_ar` according to command contract.

### fn `def cmd_br(extra)` (L2109-2112)
- Brief: Execute `cmd_br` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_br` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_br`.
- Return: Result emitted by `cmd_br` according to command contract.

### fn `def cmd_bd(extra)` (L2117-2120)
- Brief: Execute `cmd_bd` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_bd` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_bd`.
- Return: Result emitted by `cmd_bd` according to command contract.

### fn `def cmd_ck(extra)` (L2125-2128)
- Brief: Execute `cmd_ck` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ck` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ck`.
- Return: Result emitted by `cmd_ck` according to command contract.

### fn `def _ensure_commit_ready(alias)` `priv` (L2133-2146)
- Brief: Execute `_ensure_commit_ready` runtime logic for Git-Alias CLI.
- Details: Executes `_ensure_commit_ready` using deterministic CLI control-flow and explicit error propagation.
- Param: alias Input parameter consumed by `_ensure_commit_ready`.
- Return: Result emitted by `_ensure_commit_ready` according to command contract.

### fn `def cmd_cm(extra)` (L2151-2156)
- Brief: Execute `cmd_cm` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_cm` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_cm`.
- Return: Result emitted by `cmd_cm` according to command contract.

### fn `def cmd_wip(extra)` (L2161-2173)
- Brief: Execute `cmd_wip` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_wip` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_wip`.
- Return: Result emitted by `cmd_wip` according to command contract.

### fn `def cmd_release(extra)` (L2178-2200)
- Brief: Execute `cmd_release` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_release` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_release`.
- Return: Result emitted by `cmd_release` according to command contract.

### fn `def cmd_new(extra)` (L2205-2208)
- Brief: Execute `cmd_new` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_new` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_new`.
- Return: Result emitted by `cmd_new` according to command contract.

### fn `def cmd_refactor(extra)` (L2213-2216)
- Brief: Execute `cmd_refactor` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_refactor` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_refactor`.
- Return: Result emitted by `cmd_refactor` according to command contract.

### fn `def cmd_fix(extra)` (L2221-2224)
- Brief: Execute `cmd_fix` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_fix` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_fix`.
- Return: Result emitted by `cmd_fix` according to command contract.

### fn `def cmd_change(extra)` (L2229-2232)
- Brief: Execute `cmd_change` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_change` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_change`.
- Return: Result emitted by `cmd_change` according to command contract.

### fn `def cmd_implement(extra)` (L2237-2240)
- Brief: Execute `cmd_implement` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_implement` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_implement`.
- Return: Result emitted by `cmd_implement` according to command contract.

### fn `def cmd_docs(extra)` (L2245-2248)
- Brief: Execute `cmd_docs` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_docs` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_docs`.
- Return: Result emitted by `cmd_docs` according to command contract.

### fn `def cmd_style(extra)` (L2253-2256)
- Brief: Execute `cmd_style` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_style` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_style`.
- Return: Result emitted by `cmd_style` according to command contract.

### fn `def cmd_revert(extra)` (L2261-2264)
- Brief: Execute `cmd_revert` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_revert` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_revert`.
- Return: Result emitted by `cmd_revert` according to command contract.

### fn `def cmd_misc(extra)` (L2269-2272)
- Brief: Execute `cmd_misc` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_misc` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_misc`.
- Return: Result emitted by `cmd_misc` according to command contract.

### fn `def cmd_cover(extra)` (L2277-2280)
- Brief: Execute `cmd_cover` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_cover` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_cover`.
- Return: Result emitted by `cmd_cover` according to command contract.

### fn `def cmd_co(extra)` (L2285-2288)
- Brief: Execute `cmd_co` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_co` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_co`.
- Return: Result emitted by `cmd_co` according to command contract.

### fn `def cmd_d(extra)` (L2293-2300)
- Brief: Execute `cmd_d` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_d` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_d`.
- Return: Result emitted by `cmd_d` according to command contract.

### fn `def cmd_dcc(extra)` (L2305-2308)
- Brief: Execute `cmd_dcc` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_dcc` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_dcc`.
- Return: Result emitted by `cmd_dcc` according to command contract.

### fn `def cmd_dccc(extra)` (L2313-2316)
- Brief: Execute `cmd_dccc` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_dccc` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_dccc`.
- Return: Result emitted by `cmd_dccc` according to command contract.

### fn `def cmd_de(extra)` (L2321-2324)
- Brief: Execute `cmd_de` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_de` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_de`.
- Return: Result emitted by `cmd_de` according to command contract.

### fn `def cmd_di(extra)` (L2329-2332)
- Brief: Execute `cmd_di` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_di` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_di`.
- Return: Result emitted by `cmd_di` according to command contract.

### fn `def cmd_diyou(extra)` (L2337-2340)
- Brief: Execute `cmd_diyou` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_diyou` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_diyou`.
- Return: Result emitted by `cmd_diyou` according to command contract.

### fn `def cmd_dime(extra)` (L2345-2348)
- Brief: Execute `cmd_dime` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_dime` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_dime`.
- Return: Result emitted by `cmd_dime` according to command contract.

### fn `def cmd_dwc(extra)` (L2353-2356)
- Brief: Execute `cmd_dwc` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_dwc` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_dwc`.
- Return: Result emitted by `cmd_dwc` according to command contract.

### fn `def cmd_dwcc(extra)` (L2361-2364)
- Brief: Execute `cmd_dwcc` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_dwcc` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_dwcc`.
- Return: Result emitted by `cmd_dwcc` according to command contract.

### fn `def cmd_ed(extra)` (L2369-2378)
- Brief: Execute `cmd_ed` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ed` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ed`.
- Return: Result emitted by `cmd_ed` according to command contract.

### fn `def cmd_fe(extra)` (L2383-2386)
- Brief: Execute `cmd_fe` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_fe` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_fe`.
- Return: Result emitted by `cmd_fe` according to command contract.

### fn `def cmd_feall(extra)` (L2391-2394)
- Brief: Execute `cmd_feall` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_feall` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_feall`.
- Return: Result emitted by `cmd_feall` according to command contract.

### fn `def cmd_gp(extra)` (L2399-2402)
- Brief: Execute `cmd_gp` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_gp` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_gp`.
- Return: Result emitted by `cmd_gp` according to command contract.

### fn `def cmd_gr(extra)` (L2407-2410)
- Brief: Execute `cmd_gr` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_gr` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_gr`.
- Return: Result emitted by `cmd_gr` according to command contract.

### fn `def cmd_str(extra)` (L2415-2444)
- Brief: Execute `cmd_str` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_str` using deterministic CLI control-flow and explicit error propagation.
- Details: Query git remotes with transport metadata.
- Param: extra Input parameter consumed by `cmd_str`.
- Return: Result emitted by `cmd_str` according to command contract.

### fn `def cmd_lb(extra)` (L2449-2452)
- Brief: Execute `cmd_lb` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_lb` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_lb`.
- Return: Result emitted by `cmd_lb` according to command contract.

### fn `def cmd_lg(extra)` (L2457-2470)
- Brief: Execute `cmd_lg` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_lg` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_lg`.
- Return: Result emitted by `cmd_lg` according to command contract.

### fn `def cmd_lh(extra)` (L2475-2478)
- Brief: Execute `cmd_lh` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_lh` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_lh`.
- Return: Result emitted by `cmd_lh` according to command contract.

### fn `def cmd_ll(extra)` (L2483-2495)
- Brief: Execute `cmd_ll` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ll` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ll`.
- Return: Result emitted by `cmd_ll` according to command contract.

### fn `def cmd_lm(extra)` (L2500-2503)
- Brief: Execute `cmd_lm` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_lm` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_lm`.
- Return: Result emitted by `cmd_lm` according to command contract.

### fn `def cmd_lt(extra)` (L2509-2528)
- Brief: Execute `cmd_lt` runtime logic for Git-Alias CLI.
- Details: Enumerates tags via `git tag -l`, resolves containing refs via `git branch -a --contains <tag>`,
trims branch markers/prefixes from git output, and prints deterministic `<tag>: <branch_1>, <branch_2>, ...` lines.
- Param: extra Input parameter consumed by `cmd_lt`.
- Return: Result emitted by `cmd_lt` according to command contract.

### fn `def cmd_me(extra)` (L2533-2536)
- Brief: Execute `cmd_me` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_me` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_me`.
- Return: Result emitted by `cmd_me` according to command contract.

### fn `def cmd_pl(extra)` (L2541-2544)
- Brief: Execute `cmd_pl` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_pl` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_pl`.
- Return: Result emitted by `cmd_pl` according to command contract.

### fn `def cmd_pt(extra)` (L2549-2552)
- Brief: Execute `cmd_pt` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_pt` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_pt`.
- Return: Result emitted by `cmd_pt` according to command contract.

### fn `def cmd_pu(extra)` (L2557-2560)
- Brief: Execute `cmd_pu` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_pu` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_pu`.
- Return: Result emitted by `cmd_pu` according to command contract.

### fn `def cmd_rf(extra)` (L2565-2568)
- Brief: Execute `cmd_rf` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rf` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rf`.
- Return: Result emitted by `cmd_rf` according to command contract.

### fn `def cmd_rmtg(extra)` (L2573-2583)
- Brief: Execute `cmd_rmtg` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rmtg` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rmtg`.
- Return: Result emitted by `cmd_rmtg` according to command contract.

### fn `def cmd_rmloc(extra)` (L2588-2591)
- Brief: Execute `cmd_rmloc` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rmloc` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rmloc`.
- Return: Result emitted by `cmd_rmloc` according to command contract.

### fn `def cmd_rmstg(extra)` (L2596-2599)
- Brief: Execute `cmd_rmstg` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rmstg` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rmstg`.
- Return: Result emitted by `cmd_rmstg` according to command contract.

### fn `def cmd_rmunt(extra)` (L2604-2607)
- Brief: Execute `cmd_rmunt` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rmunt` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rmunt`.
- Return: Result emitted by `cmd_rmunt` according to command contract.

### fn `def cmd_rs(extra)` (L2612-2615)
- Brief: Execute `cmd_rs` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rs` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rs`.
- Return: Result emitted by `cmd_rs` according to command contract.

### fn `def cmd_rssft(extra)` (L2620-2623)
- Brief: Execute `cmd_rssft` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rssft` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rssft`.
- Return: Result emitted by `cmd_rssft` according to command contract.

### fn `def cmd_rsmix(extra)` (L2628-2631)
- Brief: Execute `cmd_rsmix` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rsmix` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rsmix`.
- Return: Result emitted by `cmd_rsmix` according to command contract.

### fn `def cmd_rshrd(extra)` (L2636-2639)
- Brief: Execute `cmd_rshrd` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rshrd` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rshrd`.
- Return: Result emitted by `cmd_rshrd` according to command contract.

### fn `def cmd_rsmrg(extra)` (L2644-2647)
- Brief: Execute `cmd_rsmrg` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rsmrg` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rsmrg`.
- Return: Result emitted by `cmd_rsmrg` according to command contract.

### fn `def cmd_rskep(extra)` (L2652-2655)
- Brief: Execute `cmd_rskep` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_rskep` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_rskep`.
- Return: Result emitted by `cmd_rskep` according to command contract.

### fn `def cmd_st(extra)` (L2660-2663)
- Brief: Execute `cmd_st` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_st` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_st`.
- Return: Result emitted by `cmd_st` according to command contract.

### fn `def cmd_tg(extra)` (L2668-2671)
- Brief: Execute `cmd_tg` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_tg` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_tg`.
- Return: Result emitted by `cmd_tg` according to command contract.

### fn `def cmd_unstg(extra)` (L2676-2679)
- Brief: Execute `cmd_unstg` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_unstg` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_unstg`.
- Return: Result emitted by `cmd_unstg` according to command contract.

### fn `def cmd_wt(extra)` (L2684-2687)
- Brief: Execute `cmd_wt` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_wt` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_wt`.
- Return: Result emitted by `cmd_wt` according to command contract.

### fn `def cmd_wtl(extra)` (L2692-2695)
- Brief: Execute `cmd_wtl` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_wtl` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_wtl`.
- Return: Result emitted by `cmd_wtl` according to command contract.

### fn `def cmd_wtp(extra)` (L2700-2703)
- Brief: Execute `cmd_wtp` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_wtp` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_wtp`.
- Return: Result emitted by `cmd_wtp` according to command contract.

### fn `def cmd_wtr(extra)` (L2708-2711)
- Brief: Execute `cmd_wtr` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_wtr` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_wtr`.
- Return: Result emitted by `cmd_wtr` according to command contract.

### fn `def cmd_ver(extra)` (L2716-2742)
- Brief: Execute `cmd_ver` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_ver` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_ver`.
- Return: Result emitted by `cmd_ver` according to command contract.

### fn `def cmd_chver(extra)` (L2747-2819)
- Brief: Execute `cmd_chver` runtime logic for Git-Alias CLI.
- Details: Executes `cmd_chver` using deterministic CLI control-flow and explicit error propagation.
- Param: extra Input parameter consumed by `cmd_chver`.
- Return: Result emitted by `cmd_chver` according to command contract.

### fn `def cmd_major(extra)` (L2828-2832)
- Brief: CLI entry-point for the `major` release subcommand.
- Details: Increments the major semver index (resets minor and patch to 0), merges and pushes
to both configured `develop` and `master` branches, regenerates changelog via a
temporary local tag on `work`, and creates the definitive release tag on `master`
immediately before pushing `master` with `--tags`.
- Param: extra Iterable of CLI argument strings; accepted flag: `--include-patch`.
- Return: None; delegates to `_run_release_command("major", ...)`.
- Satisfies: REQ-026, REQ-045

### fn `def cmd_minor(extra)` (L2841-2845)
- Brief: CLI entry-point for the `minor` release subcommand.
- Details: Increments the minor semver index (resets patch to 0), merges and pushes to both
configured `develop` and `master` branches, regenerates changelog via a temporary local
tag on `work`, and creates the definitive release tag on `master` immediately before
pushing `master` with `--tags`.
- Param: extra Iterable of CLI argument strings; accepted flag: `--include-patch`.
- Return: None; delegates to `_run_release_command("minor", ...)`.
- Satisfies: REQ-026, REQ-045

### fn `def cmd_patch(extra)` (L2854-2858)
- Brief: CLI entry-point for the `patch` release subcommand.
- Details: Increments the patch semver index, merges and pushes to configured `develop` only
(MUST NOT merge or push to `master`), regenerates changelog via a temporary local tag
on `work`, and creates the definitive release tag on `develop` immediately before
pushing `develop` with `--tags`; `--include-patch` is auto-included.
- Param: extra Iterable of CLI argument strings; accepted flag: `--include-patch`.
- Return: None; delegates to `_run_release_command("patch", ...)`.
- Satisfies: REQ-026, REQ-045

### fn `def cmd_backup(extra)` (L2866-2876)
- Brief: CLI entry-point for the `backup` workflow subcommand.
- Details: Runs the same preflight checks used by `major`/`minor`/`patch`, then integrates the
configured `work` branch into the configured `develop` branch and pushes `develop`
to its remote tracking branch before returning to `work`.
- Param: extra Iterable of CLI argument strings; accepted token: `--help` only.
- Return: None; delegates to `_run_backup_command()`.
- Satisfies: REQ-047, REQ-048, REQ-049

### fn `def cmd_changelog(extra)` (L2889-2920)
- Brief: CLI entry-point for the `changelog` subcommand.
- Details: Parses flags, delegates to `generate_changelog_document`, and writes or prints the result.
Accepted flags: `--include-patch`, `--force-write`, `--print-only`,
`--disable-history`, `--help`.
Exits with status 2 on argument errors or when not inside a git repository.
Exits with status 1 when `CHANGELOG.md` already exists and `--force-write` was not supplied.
- Param: extra Iterable of CLI argument strings following the `changelog` subcommand token.
- Return: None; side-effects: writes `CHANGELOG.md` to disk or prints to stdout.
- Satisfies: REQ-018, REQ-040, REQ-041, REQ-043

- var `COMMANDS = {` (L2921)
- Brief: Constant `COMMANDS` used by CLI runtime paths and policies.
### fn `def print_command_help(name, width=None)` (L2998-3004)
- Brief: Execute `print_command_help` runtime logic for Git-Alias CLI.
- Details: Executes `print_command_help` using deterministic CLI control-flow and explicit error propagation.
- Param: name Input parameter consumed by `print_command_help`.
- Param: width Input parameter consumed by `print_command_help`.
- Return: Result emitted by `print_command_help` according to command contract.

### fn `def print_all_help()` (L3008-3042)
- Brief: Execute `print_all_help` runtime logic for Git-Alias CLI.
- Details: Executes `print_all_help` using deterministic CLI control-flow and explicit error propagation.
- Return: Result emitted by `print_all_help` according to command contract.

### fn `def main(argv=None, *, check_updates: bool = True)` (L3048-3098)
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
|`RESET_HELP_COMMANDS`|var|pub|534||
|`_to_args`|fn|priv|541-544|def _to_args(extra)|
|`CommandExecutionError`|class|pub|546-587|class CommandExecutionError(RuntimeError)|
|`CommandExecutionError.__init__`|fn|priv|551-558|def __init__(self, exc: subprocess.CalledProcessError)|
|`CommandExecutionError._format_message`|fn|priv|562-572|def _format_message(self) -> str|
|`CommandExecutionError._decode_stream`|fn|priv|577-587|def _decode_stream(data) -> str|
|`_run_checked`|fn|priv|593-600|def _run_checked(*popenargs, **kwargs)|
|`VersionDetectionError`|class|pub|602-605|class VersionDetectionError(RuntimeError)|
|`ReleaseError`|class|pub|607-610|class ReleaseError(RuntimeError)|
|`run_git_cmd`|fn|pub|618-622|def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)|
|`capture_git_output`|fn|pub|628-632|def capture_git_output(base_args, cwd=None)|
|`run_command`|fn|pub|638-641|def run_command(cmd, cwd=None)|
|`run_git_text`|fn|pub|648-665|def run_git_text(args, cwd=None, check=True)|
|`run_shell`|fn|pub|671-674|def run_shell(command, cwd=None)|
|`_git_status_lines`|fn|priv|678-690|def _git_status_lines()|
|`has_unstaged_changes`|fn|pub|695-706|def has_unstaged_changes(status_lines=None)|
|`has_staged_changes`|fn|pub|711-720|def has_staged_changes(status_lines=None)|
|`WIP_MESSAGE_RE`|var|pub|726||
|`_refresh_remote_refs`|fn|priv|732-743|def _refresh_remote_refs()|
|`_branch_remote_divergence`|fn|priv|749-767|def _branch_remote_divergence(branch_key, remote="origin")|
|`has_remote_branch_updates`|fn|pub|773-777|def has_remote_branch_updates(branch_key, remote="origin")|
|`has_remote_develop_updates`|fn|pub|781-784|def has_remote_develop_updates()|
|`has_remote_master_updates`|fn|pub|788-791|def has_remote_master_updates()|
|`_head_commit_message`|fn|priv|795-801|def _head_commit_message()|
|`_head_commit_hash`|fn|priv|805-811|def _head_commit_hash()|
|`_commit_exists_in_branch`|fn|priv|817-829|def _commit_exists_in_branch(commit_hash, branch_name)|
|`_should_amend_existing_commit`|fn|priv|833-848|def _should_amend_existing_commit()|
|`is_inside_git_repo`|fn|pub|852-859|def is_inside_git_repo()|
|`TagInfo`|class|pub|864-872|class TagInfo|
|`DELIM`|var|pub|875||
|`RECORD`|var|pub|878||
|`SEMVER_RE`|var|pub|894||
|`SECTION_EMOJI`|var|pub|897||
|`_tag_semver_tuple`|fn|priv|914-917|def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[in...|
|`_latest_supported_tag_name`|fn|priv|922-925|def _latest_supported_tag_name(tags: List[TagInfo]) -> Op...|
|`_is_minor_release_tag`|fn|priv|933-940|def _is_minor_release_tag(tag_name: str) -> bool|
|`_latest_patch_tag_after`|fn|priv|949-958|def _latest_patch_tag_after(all_tags: List[TagInfo], last...|
|`list_tags_sorted_by_date`|fn|pub|964-984|def list_tags_sorted_by_date(repo_root: Path, merged_ref:...|
|`git_log_subjects`|fn|pub|991-1002|def git_log_subjects(repo_root: Path, rev_range: str) -> ...|
|`parse_conventional_commit`|fn|pub|1008-1020|def parse_conventional_commit(message: str) -> Optional[T...|
|`_format_changelog_description`|fn|priv|1027-1037|def _format_changelog_description(desc: str) -> List[str]|
|`categorize_commit`|fn|pub|1046-1073|def categorize_commit(subject: str) -> Tuple[Optional[str...|
|`_extract_release_version`|fn|priv|1077-1087|def _extract_release_version(subject: str) -> Optional[str]|
|`_is_release_marker_commit`|fn|priv|1092-1095|def _is_release_marker_commit(subject: str) -> bool|
|`generate_section_for_range`|fn|pub|1107-1143|def generate_section_for_range(repo_root: Path, title: st...|
|`_get_remote_name_for_branch`|fn|priv|1154-1160|def _get_remote_name_for_branch(branch_name: str, repo_ro...|
|`_extract_owner_repo`|fn|priv|1169-1191|def _extract_owner_repo(remote_url: str) -> Optional[Tupl...|
|`_canonical_origin_base`|fn|priv|1203-1214|def _canonical_origin_base(repo_root: Path) -> Optional[str]|
|`get_origin_compare_url`|fn|pub|1220-1227|def get_origin_compare_url(base_url: Optional[str], prev_...|
|`get_release_page_url`|fn|pub|1233-1238|def get_release_page_url(base_url: Optional[str], tag: st...|
|`build_history_section`|fn|pub|1246-1250|def build_history_section(|
|`generate_changelog_document`|fn|pub|1297-1356|def generate_changelog_document(repo_root: Path, include_...|
|`VersionRuleContext`|class|pub|1366-1373|class VersionRuleContext|
|`_normalize_version_rule_pattern`|fn|priv|1379-1390|def _normalize_version_rule_pattern(pattern: str) -> str|
|`_build_version_file_inventory`|fn|priv|1396-1417|def _build_version_file_inventory(root: Path) -> List[Tup...|
|`_collect_version_files`|fn|priv|1425-1442|def _collect_version_files(root, pattern, *, inventory=None)|
|`_is_version_path_excluded`|fn|priv|1447-1450|def _is_version_path_excluded(relative_path: str) -> bool|
|`_iter_versions_in_text`|fn|priv|1456-1467|def _iter_versions_in_text(text, compiled_regexes)|
|`_read_version_file_text`|fn|priv|1474-1488|def _read_version_file_text(file_path: Path, text_cache: ...|
|`_prepare_version_rule_contexts`|fn|priv|1497-1498|def _prepare_version_rule_contexts(|
|`_determine_canonical_version`|fn|priv|1540-1547|def _determine_canonical_version(|
|`_parse_semver_tuple`|fn|priv|1592-1598|def _parse_semver_tuple(text: str) -> Optional[Tuple[int,...|
|`_replace_versions_in_text`|fn|priv|1605-1620|def _replace_versions_in_text(text, compiled_regex, repla...|
|`_current_branch_name`|fn|priv|1624-1636|def _current_branch_name()|
|`_ref_exists`|fn|priv|1641-1650|def _ref_exists(ref_name)|
|`_local_branch_exists`|fn|priv|1655-1658|def _local_branch_exists(branch_name)|
|`_remote_branch_exists`|fn|priv|1663-1666|def _remote_branch_exists(branch_name)|
|`_ensure_release_prerequisites`|fn|priv|1670-1697|def _ensure_release_prerequisites()|
|`_bump_semver_version`|fn|priv|1703-1721|def _bump_semver_version(current_version, level)|
|`_run_release_step`|fn|priv|1728-1748|def _run_release_step(level, step_name, action)|
|`_create_release_commit_for_flow`|fn|priv|1753-1758|def _create_release_commit_for_flow(target_version)|
|`_push_branch_with_tags`|fn|priv|1764-1768|def _push_branch_with_tags(branch_name)|
|`_execute_release_flow`|fn|priv|1784-1831|def _execute_release_flow(level, changelog_args=None)|
|`_execute_backup_flow`|fn|priv|1839-1854|def _execute_backup_flow()|
|`_run_release_command`|fn|priv|1860-1875|def _run_release_command(level, changelog_args=None)|
|`_run_backup_command`|fn|priv|1880-1887|def _run_backup_command()|
|`_run_reset_with_help`|fn|priv|1893-1900|def _run_reset_with_help(base_args, extra)|
|`_reject_extra_arguments`|fn|priv|1906-1912|def _reject_extra_arguments(extra, alias)|
|`_parse_release_flags`|fn|priv|1918-1936|def _parse_release_flags(extra, alias)|
|`_prepare_commit_message`|fn|priv|1942-1952|def _prepare_commit_message(extra, alias)|
|`_build_conventional_message`|fn|priv|1959-1973|def _build_conventional_message(kind: str, extra, alias: ...|
|`_run_conventional_commit`|fn|priv|1980-1985|def _run_conventional_commit(kind: str, alias: str, extra)|
|`_execute_commit`|fn|priv|1992-2021|def _execute_commit(message, alias, allow_amend=True)|
|`upgrade_self`|fn|pub|2025-2038|def upgrade_self()|
|`remove_self`|fn|pub|2042-2045|def remove_self()|
|`cmd_aa`|fn|pub|2050-2057|def cmd_aa(extra)|
|`cmd_ra`|fn|pub|2062-2085|def cmd_ra(extra)|
|`cmd_ar`|fn|pub|2090-2104|def cmd_ar(extra)|
|`cmd_br`|fn|pub|2109-2112|def cmd_br(extra)|
|`cmd_bd`|fn|pub|2117-2120|def cmd_bd(extra)|
|`cmd_ck`|fn|pub|2125-2128|def cmd_ck(extra)|
|`_ensure_commit_ready`|fn|priv|2133-2146|def _ensure_commit_ready(alias)|
|`cmd_cm`|fn|pub|2151-2156|def cmd_cm(extra)|
|`cmd_wip`|fn|pub|2161-2173|def cmd_wip(extra)|
|`cmd_release`|fn|pub|2178-2200|def cmd_release(extra)|
|`cmd_new`|fn|pub|2205-2208|def cmd_new(extra)|
|`cmd_refactor`|fn|pub|2213-2216|def cmd_refactor(extra)|
|`cmd_fix`|fn|pub|2221-2224|def cmd_fix(extra)|
|`cmd_change`|fn|pub|2229-2232|def cmd_change(extra)|
|`cmd_implement`|fn|pub|2237-2240|def cmd_implement(extra)|
|`cmd_docs`|fn|pub|2245-2248|def cmd_docs(extra)|
|`cmd_style`|fn|pub|2253-2256|def cmd_style(extra)|
|`cmd_revert`|fn|pub|2261-2264|def cmd_revert(extra)|
|`cmd_misc`|fn|pub|2269-2272|def cmd_misc(extra)|
|`cmd_cover`|fn|pub|2277-2280|def cmd_cover(extra)|
|`cmd_co`|fn|pub|2285-2288|def cmd_co(extra)|
|`cmd_d`|fn|pub|2293-2300|def cmd_d(extra)|
|`cmd_dcc`|fn|pub|2305-2308|def cmd_dcc(extra)|
|`cmd_dccc`|fn|pub|2313-2316|def cmd_dccc(extra)|
|`cmd_de`|fn|pub|2321-2324|def cmd_de(extra)|
|`cmd_di`|fn|pub|2329-2332|def cmd_di(extra)|
|`cmd_diyou`|fn|pub|2337-2340|def cmd_diyou(extra)|
|`cmd_dime`|fn|pub|2345-2348|def cmd_dime(extra)|
|`cmd_dwc`|fn|pub|2353-2356|def cmd_dwc(extra)|
|`cmd_dwcc`|fn|pub|2361-2364|def cmd_dwcc(extra)|
|`cmd_ed`|fn|pub|2369-2378|def cmd_ed(extra)|
|`cmd_fe`|fn|pub|2383-2386|def cmd_fe(extra)|
|`cmd_feall`|fn|pub|2391-2394|def cmd_feall(extra)|
|`cmd_gp`|fn|pub|2399-2402|def cmd_gp(extra)|
|`cmd_gr`|fn|pub|2407-2410|def cmd_gr(extra)|
|`cmd_str`|fn|pub|2415-2444|def cmd_str(extra)|
|`cmd_lb`|fn|pub|2449-2452|def cmd_lb(extra)|
|`cmd_lg`|fn|pub|2457-2470|def cmd_lg(extra)|
|`cmd_lh`|fn|pub|2475-2478|def cmd_lh(extra)|
|`cmd_ll`|fn|pub|2483-2495|def cmd_ll(extra)|
|`cmd_lm`|fn|pub|2500-2503|def cmd_lm(extra)|
|`cmd_lt`|fn|pub|2509-2528|def cmd_lt(extra)|
|`cmd_me`|fn|pub|2533-2536|def cmd_me(extra)|
|`cmd_pl`|fn|pub|2541-2544|def cmd_pl(extra)|
|`cmd_pt`|fn|pub|2549-2552|def cmd_pt(extra)|
|`cmd_pu`|fn|pub|2557-2560|def cmd_pu(extra)|
|`cmd_rf`|fn|pub|2565-2568|def cmd_rf(extra)|
|`cmd_rmtg`|fn|pub|2573-2583|def cmd_rmtg(extra)|
|`cmd_rmloc`|fn|pub|2588-2591|def cmd_rmloc(extra)|
|`cmd_rmstg`|fn|pub|2596-2599|def cmd_rmstg(extra)|
|`cmd_rmunt`|fn|pub|2604-2607|def cmd_rmunt(extra)|
|`cmd_rs`|fn|pub|2612-2615|def cmd_rs(extra)|
|`cmd_rssft`|fn|pub|2620-2623|def cmd_rssft(extra)|
|`cmd_rsmix`|fn|pub|2628-2631|def cmd_rsmix(extra)|
|`cmd_rshrd`|fn|pub|2636-2639|def cmd_rshrd(extra)|
|`cmd_rsmrg`|fn|pub|2644-2647|def cmd_rsmrg(extra)|
|`cmd_rskep`|fn|pub|2652-2655|def cmd_rskep(extra)|
|`cmd_st`|fn|pub|2660-2663|def cmd_st(extra)|
|`cmd_tg`|fn|pub|2668-2671|def cmd_tg(extra)|
|`cmd_unstg`|fn|pub|2676-2679|def cmd_unstg(extra)|
|`cmd_wt`|fn|pub|2684-2687|def cmd_wt(extra)|
|`cmd_wtl`|fn|pub|2692-2695|def cmd_wtl(extra)|
|`cmd_wtp`|fn|pub|2700-2703|def cmd_wtp(extra)|
|`cmd_wtr`|fn|pub|2708-2711|def cmd_wtr(extra)|
|`cmd_ver`|fn|pub|2716-2742|def cmd_ver(extra)|
|`cmd_chver`|fn|pub|2747-2819|def cmd_chver(extra)|
|`cmd_major`|fn|pub|2828-2832|def cmd_major(extra)|
|`cmd_minor`|fn|pub|2841-2845|def cmd_minor(extra)|
|`cmd_patch`|fn|pub|2854-2858|def cmd_patch(extra)|
|`cmd_backup`|fn|pub|2866-2876|def cmd_backup(extra)|
|`cmd_changelog`|fn|pub|2889-2920|def cmd_changelog(extra)|
|`COMMANDS`|var|pub|2921||
|`print_command_help`|fn|pub|2998-3004|def print_command_help(name, width=None)|
|`print_all_help`|fn|pub|3008-3042|def print_all_help()|
|`main`|fn|pub|3048-3098|def main(argv=None, *, check_updates: bool = True)|
