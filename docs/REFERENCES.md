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

# core.py | Python | 2790L | 170 symbols | 16 imports | 713 comments
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
- Return: Result emitted by `get_config_value` according to command contract.

### fn `def get_branch(name)` (L106-111)
- Return: Result emitted by `get_branch` according to command contract.

### fn `def get_editor()` (L115-118)
- Return: Result emitted by `get_editor` according to command contract.

### fn `def _load_config_rules(key, fallback)` `priv` (L124-149)
- Return: Result emitted by `_load_config_rules` according to command contract.

### fn `def get_version_rules()` (L153-156)
- Return: Result emitted by `get_version_rules` according to command contract.

### fn `def get_cli_version()` (L160-171)
- Return: Result emitted by `get_cli_version` according to command contract.

### fn `def _normalize_semver_text(text: str) -> str` `priv` (L176-182)
- Return: Result emitted by `_normalize_semver_text` according to command contract.

### fn `def check_for_newer_version(timeout_seconds: float = 1.0) -> None` (L187-271)
- Details: Reuse non-expired cache payload before any online request. Emit upgrade warning when cached latest version is newer. Ignore cache read failures because version checks are non-blocking. Skip network request when cache entry is valid. Execute online release lookup when cache is absent or expired. Persist fresh release-check payload with TTL metadata. Ignore cache write failures because command execution must continue. Emit upgrade hint when fetched latest version is newer than current.
- Return: Result emitted by `check_for_newer_version` according to command contract.

### fn `def get_git_root()` (L275-290)
- Return: Result emitted by `get_git_root` according to command contract.

### fn `def get_config_path(root=None)` (L295-299)
- Return: Result emitted by `get_config_path` according to command contract.

### fn `def load_cli_config(root=None)` (L304-338)
- Return: Result emitted by `load_cli_config` according to command contract.

### fn `def write_default_config(root=None)` (L343-350)
- Return: Result emitted by `write_default_config` according to command contract.

### fn `def _editor_base_command()` `priv` (L354-368)
- Return: Result emitted by `_editor_base_command` according to command contract.

### fn `def run_editor_command(args)` (L373-375)
- Return: Result emitted by `run_editor_command` according to command contract.

- var `HELP_TEXTS = {` (L378)
- Brief: Constant `HELP_TEXTS` used by CLI runtime paths and policies.
- var `RESET_HELP_COMMANDS = {"rs", "rshrd", "rskep", "rsmix", "rsmrg", "rssft"}` (L529)
- Brief: Constant `RESET_HELP_COMMANDS` used by CLI runtime paths and policies.
### fn `def _to_args(extra)` `priv` (L536-539)
- Return: Result emitted by `_to_args` according to command contract.

### class `class CommandExecutionError(RuntimeError)` : RuntimeError (L541-582)
- Brief: Class `CommandExecutionError` models a typed runtime container/error boundary. Execute `__init__` runtime logic for Git-Alias CLI. Execute `_format_message` runtime logic for Git-Alias CLI. Execute `_decode_stream` runtime logic for Git-Alias CLI.
- Param: self Input parameter consumed by `__init__`. exc Input parameter consumed by `__init__`. self Input parameter consumed by `_format_message`. data Input parameter consumed by `_decode_stream`.
- Return: Result emitted by `__init__` according to command contract. Result emitted by `_format_message` according to command contract. Result emitted by `_decode_stream` according to command contract.
- fn `def __init__(self, exc: subprocess.CalledProcessError)` `priv` (L546-553)
  - Return: Result emitted by `__init__` according to command contract.
- fn `def _format_message(self) -> str` `priv` (L557-567)
  - Return: Result emitted by `_format_message` according to command contract.
- fn `def _decode_stream(data) -> str` `priv` (L572-582)
  - Return: Result emitted by `_decode_stream` according to command contract.

### fn `def _run_checked(*popenargs, **kwargs)` `priv` (L588-595)
- Return: Result emitted by `_run_checked` according to command contract.

### class `class VersionDetectionError(RuntimeError)` : RuntimeError (L597-600)
- Brief: Class `VersionDetectionError` models a typed runtime container/error boundary.

### class `class ReleaseError(RuntimeError)` : RuntimeError (L602-605)
- Brief: Class `ReleaseError` models a typed runtime container/error boundary.

### fn `def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)` (L613-617)
- Return: Result emitted by `run_git_cmd` according to command contract.

### fn `def capture_git_output(base_args, cwd=None)` (L623-627)
- Return: Result emitted by `capture_git_output` according to command contract.

### fn `def run_command(cmd, cwd=None)` (L633-636)
- Return: Result emitted by `run_command` according to command contract.

### fn `def run_git_text(args, cwd=None, check=True)` (L643-660)
- Return: Result emitted by `run_git_text` according to command contract.

### fn `def run_shell(command, cwd=None)` (L666-669)
- Return: Result emitted by `run_shell` according to command contract.

### fn `def _git_status_lines()` `priv` (L673-685)
- Return: Result emitted by `_git_status_lines` according to command contract.

### fn `def has_unstaged_changes(status_lines=None)` (L690-701)
- Return: Result emitted by `has_unstaged_changes` according to command contract.

### fn `def has_staged_changes(status_lines=None)` (L706-715)
- Return: Result emitted by `has_staged_changes` according to command contract.

- var `WIP_MESSAGE_RE = re.compile(r"^wip: work in progress\.$")` (L721)
- Brief: Constant `WIP_MESSAGE_RE` used by CLI runtime paths and policies.
### fn `def _refresh_remote_refs()` `priv` (L727-738)
- Return: Result emitted by `_refresh_remote_refs` according to command contract.

### fn `def _branch_remote_divergence(branch_key, remote="origin")` `priv` (L744-762)
- Return: Result emitted by `_branch_remote_divergence` according to command contract.

### fn `def has_remote_branch_updates(branch_key, remote="origin")` (L768-772)
- Return: Result emitted by `has_remote_branch_updates` according to command contract.

### fn `def has_remote_develop_updates()` (L776-779)
- Return: Result emitted by `has_remote_develop_updates` according to command contract.

### fn `def has_remote_master_updates()` (L783-786)
- Return: Result emitted by `has_remote_master_updates` according to command contract.

### fn `def _head_commit_message()` `priv` (L790-796)
- Return: Result emitted by `_head_commit_message` according to command contract.

### fn `def _head_commit_hash()` `priv` (L800-806)
- Return: Result emitted by `_head_commit_hash` according to command contract.

### fn `def _commit_exists_in_branch(commit_hash, branch_name)` `priv` (L812-824)
- Return: Result emitted by `_commit_exists_in_branch` according to command contract.

### fn `def _should_amend_existing_commit()` `priv` (L828-843)
- Return: Result emitted by `_should_amend_existing_commit` according to command contract.

### fn `def is_inside_git_repo()` (L847-854)
- Return: Result emitted by `is_inside_git_repo` according to command contract.

### class `class TagInfo` (L859-867)
- Brief: Store raw tag name including `v` prefix when present. Store ISO date string used for changelog section headers. Store object hash associated with the tag reference.
- Details: Encapsulates tag identity, tag date, and resolved Git object identifier for changelog assembly.

- var `DELIM = "\x1f"` (L870)
- Brief: Constant `DELIM` used by CLI runtime paths and policies.
- var `RECORD = "\x1e"` (L873)
- Brief: Constant `RECORD` used by CLI runtime paths and policies.
- var `SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")` (L889)
- Brief: Constant `SEMVER_RE` used by CLI runtime paths and policies.
- var `SECTION_EMOJI = {` (L892)
- Brief: Constant `SECTION_EMOJI` used by CLI runtime paths and policies.
### fn `def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[int, int, int]]` `priv` (L909-912)
- Return: Result emitted by `_tag_semver_tuple` according to command contract.

### fn `def _latest_supported_tag_name(tags: List[TagInfo]) -> Optional[str]` `priv` (L917-920)
- Return: Result emitted by `_latest_supported_tag_name` according to command contract.

### fn `def _is_minor_release_tag(tag_name: str) -> bool` `priv` (L928-935)
- Sa: tisfies REQ-018, REQ-040

### fn `def _latest_patch_tag_after(all_tags: List[TagInfo], last_minor: Optional[TagInfo]) -> Optional[TagInfo]` `priv` (L944-953)
- Sa: tisfies REQ-040

### fn `def list_tags_sorted_by_date(repo_root: Path, merged_ref: Optional[str] = None) -> List[TagInfo]` (L959-979)
- Return: Result emitted by `list_tags_sorted_by_date` according to command contract.

### fn `def git_log_subjects(repo_root: Path, rev_range: str) -> List[str]` (L985-996)
- Return: Result emitted by `git_log_subjects` according to command contract.

### fn `def categorize_commit(subject: str) -> Tuple[Optional[str], str]` (L1002-1026)
- Return: Tuple `(section, line)`: `section` is the changelog section name or `None` if type is unmapped or ignored; `line` is the formatted entry string or `""` when section is `None`.

### fn `def _extract_release_version(subject: str) -> Optional[str]` `priv` (L1031-1041)
- Return: Result emitted by `_extract_release_version` according to command contract.

### fn `def _is_release_marker_commit(subject: str) -> bool` `priv` (L1046-1049)
- Return: Result emitted by `_is_release_marker_commit` according to command contract.

### fn `def generate_section_for_range(repo_root: Path, title: str, date_s: str, rev_range: str, expected_version: Optional[str] = None) -> Optional[str]` (L1058-1096)
- Return: Result emitted by `generate_section_for_range` according to command contract.

### fn `def _get_remote_name_for_branch(branch_name: str, repo_root: Path) -> str` `priv` (L1105-1113)
- Sa: tisfies REQ-046

### fn `def _canonical_origin_base(repo_root: Path) -> Optional[str]` `priv` (L1123-1142)
- Sa: tisfies REQ-043, REQ-046

### fn `def get_origin_compare_url(base_url: Optional[str], prev_tag: Optional[str], tag: str) -> Optional[str]` (L1149-1156)
- Return: Result emitted by `get_origin_compare_url` according to command contract.

### fn `def get_release_page_url(base_url: Optional[str], tag: str) -> Optional[str]` (L1162-1167)
- Return: Result emitted by `get_release_page_url` according to command contract.

### fn `def build_history_section(` (L1175-1179)
- Return: Result emitted by `build_history_section` according to command contract.

### fn `def generate_changelog_document(repo_root: Path, include_patch: bool) -> str` (L1222-1282)
- Sa: tisfies REQ-018, REQ-040, REQ-041, REQ-043, REQ-068

### fn `def _collect_version_files(root, pattern)` `priv` (L1288-1323)
- Details: Apply pathspec matcher to preserve configured GitIgnore-like semantics.
- Return: Result emitted by `_collect_version_files` according to command contract.

### fn `def _is_version_path_excluded(relative_path: str) -> bool` `priv` (L1328-1331)
- Return: Result emitted by `_is_version_path_excluded` according to command contract.

### fn `def _iter_versions_in_text(text, compiled_regexes)` `priv` (L1337-1348)
- Return: Result emitted by `_iter_versions_in_text` according to command contract.

### fn `def _determine_canonical_version(root: Path, rules, *, verbose: bool = False, debug: bool = False)` `priv` (L1356-1415)
- Return: Result emitted by `_determine_canonical_version` according to command contract.

### fn `def _parse_semver_tuple(text: str) -> Optional[Tuple[int, int, int]]` `priv` (L1420-1426)
- Return: Result emitted by `_parse_semver_tuple` according to command contract.

### fn `def _replace_versions_in_text(text, compiled_regex, replacement)` `priv` (L1433-1448)
- Return: Result emitted by `_replace_versions_in_text` according to command contract.

### fn `def _current_branch_name()` `priv` (L1452-1464)
- Return: Result emitted by `_current_branch_name` according to command contract.

### fn `def _ref_exists(ref_name)` `priv` (L1469-1478)
- Return: Result emitted by `_ref_exists` according to command contract.

### fn `def _local_branch_exists(branch_name)` `priv` (L1483-1486)
- Return: Result emitted by `_local_branch_exists` according to command contract.

### fn `def _remote_branch_exists(branch_name)` `priv` (L1491-1494)
- Return: Result emitted by `_remote_branch_exists` according to command contract.

### fn `def _ensure_release_prerequisites()` `priv` (L1498-1525)
- Return: Result emitted by `_ensure_release_prerequisites` according to command contract.

### fn `def _bump_semver_version(current_version, level)` `priv` (L1531-1549)
- Return: Result emitted by `_bump_semver_version` according to command contract.

### fn `def _run_release_step(level, step_name, action)` `priv` (L1556-1576)
- Return: Result emitted by `_run_release_step` according to command contract.

### fn `def _create_release_commit_for_flow(target_version)` `priv` (L1581-1586)
- Return: Result emitted by `_create_release_commit_for_flow` according to command contract.

### fn `def _execute_release_flow(level, changelog_args=None)` `priv` (L1598-1645)
- Sa: tisfies REQ-026, REQ-045

### fn `def _run_release_command(level, changelog_args=None)` `priv` (L1651-1666)
- Return: Result emitted by `_run_release_command` according to command contract.

### fn `def _run_reset_with_help(base_args, extra)` `priv` (L1672-1679)
- Return: Result emitted by `_run_reset_with_help` according to command contract.

### fn `def _reject_extra_arguments(extra, alias)` `priv` (L1685-1691)
- Return: Result emitted by `_reject_extra_arguments` according to command contract.

### fn `def _parse_release_flags(extra, alias)` `priv` (L1697-1715)
- Return: Result emitted by `_parse_release_flags` according to command contract.

### fn `def _prepare_commit_message(extra, alias)` `priv` (L1721-1731)
- Return: Result emitted by `_prepare_commit_message` according to command contract.

### fn `def _build_conventional_message(kind: str, extra, alias: str) -> str` `priv` (L1738-1752)
- Return: Result emitted by `_build_conventional_message` according to command contract.

### fn `def _run_conventional_commit(kind: str, alias: str, extra)` `priv` (L1759-1764)
- Return: Result emitted by `_run_conventional_commit` according to command contract.

### fn `def _execute_commit(message, alias, allow_amend=True)` `priv` (L1771-1800)
- Return: Result emitted by `_execute_commit` according to command contract.

### fn `def upgrade_self()` (L1804-1817)
- Return: Result emitted by `upgrade_self` according to command contract.

### fn `def remove_self()` (L1821-1824)
- Return: Result emitted by `remove_self` according to command contract.

### fn `def cmd_aa(extra)` (L1829-1836)
- Return: Result emitted by `cmd_aa` according to command contract.

### fn `def cmd_ra(extra)` (L1841-1864)
- Return: Result emitted by `cmd_ra` according to command contract.

### fn `def cmd_ar(extra)` (L1869-1883)
- Return: Result emitted by `cmd_ar` according to command contract.

### fn `def cmd_br(extra)` (L1888-1891)
- Return: Result emitted by `cmd_br` according to command contract.

### fn `def cmd_bd(extra)` (L1896-1899)
- Return: Result emitted by `cmd_bd` according to command contract.

### fn `def cmd_ck(extra)` (L1904-1907)
- Return: Result emitted by `cmd_ck` according to command contract.

### fn `def _ensure_commit_ready(alias)` `priv` (L1912-1925)
- Return: Result emitted by `_ensure_commit_ready` according to command contract.

### fn `def cmd_cm(extra)` (L1930-1935)
- Return: Result emitted by `cmd_cm` according to command contract.

### fn `def cmd_wip(extra)` (L1940-1952)
- Return: Result emitted by `cmd_wip` according to command contract.

### fn `def cmd_release(extra)` (L1957-1979)
- Return: Result emitted by `cmd_release` according to command contract.

### fn `def cmd_new(extra)` (L1984-1987)
- Return: Result emitted by `cmd_new` according to command contract.

### fn `def cmd_refactor(extra)` (L1992-1995)
- Return: Result emitted by `cmd_refactor` according to command contract.

### fn `def cmd_fix(extra)` (L2000-2003)
- Return: Result emitted by `cmd_fix` according to command contract.

### fn `def cmd_change(extra)` (L2008-2011)
- Return: Result emitted by `cmd_change` according to command contract.

### fn `def cmd_implement(extra)` (L2016-2019)
- Return: Result emitted by `cmd_implement` according to command contract.

### fn `def cmd_docs(extra)` (L2024-2027)
- Return: Result emitted by `cmd_docs` according to command contract.

### fn `def cmd_style(extra)` (L2032-2035)
- Return: Result emitted by `cmd_style` according to command contract.

### fn `def cmd_revert(extra)` (L2040-2043)
- Return: Result emitted by `cmd_revert` according to command contract.

### fn `def cmd_misc(extra)` (L2048-2051)
- Return: Result emitted by `cmd_misc` according to command contract.

### fn `def cmd_cover(extra)` (L2056-2059)
- Return: Result emitted by `cmd_cover` according to command contract.

### fn `def cmd_co(extra)` (L2064-2067)
- Return: Result emitted by `cmd_co` according to command contract.

### fn `def cmd_d(extra)` (L2072-2079)
- Return: Result emitted by `cmd_d` according to command contract.

### fn `def cmd_dcc(extra)` (L2084-2087)
- Return: Result emitted by `cmd_dcc` according to command contract.

### fn `def cmd_dccc(extra)` (L2092-2095)
- Return: Result emitted by `cmd_dccc` according to command contract.

### fn `def cmd_de(extra)` (L2100-2103)
- Return: Result emitted by `cmd_de` according to command contract.

### fn `def cmd_di(extra)` (L2108-2111)
- Return: Result emitted by `cmd_di` according to command contract.

### fn `def cmd_diyou(extra)` (L2116-2119)
- Return: Result emitted by `cmd_diyou` according to command contract.

### fn `def cmd_dime(extra)` (L2124-2127)
- Return: Result emitted by `cmd_dime` according to command contract.

### fn `def cmd_dwc(extra)` (L2132-2135)
- Return: Result emitted by `cmd_dwc` according to command contract.

### fn `def cmd_dwcc(extra)` (L2140-2143)
- Return: Result emitted by `cmd_dwcc` according to command contract.

### fn `def cmd_ed(extra)` (L2148-2157)
- Return: Result emitted by `cmd_ed` according to command contract.

### fn `def cmd_fe(extra)` (L2162-2165)
- Return: Result emitted by `cmd_fe` according to command contract.

### fn `def cmd_feall(extra)` (L2170-2173)
- Return: Result emitted by `cmd_feall` according to command contract.

### fn `def cmd_gp(extra)` (L2178-2181)
- Return: Result emitted by `cmd_gp` according to command contract.

### fn `def cmd_gr(extra)` (L2186-2189)
- Return: Result emitted by `cmd_gr` according to command contract.

### fn `def cmd_str(extra)` (L2194-2223)
- Details: Query git remotes with transport metadata. Deduplicate remote names from `git remote -v` rows. Print normalized remote name inventory. Print detailed status for each unique remote.
- Return: Result emitted by `cmd_str` according to command contract.

### fn `def cmd_lb(extra)` (L2228-2231)
- Return: Result emitted by `cmd_lb` according to command contract.

### fn `def cmd_lg(extra)` (L2236-2249)
- Return: Result emitted by `cmd_lg` according to command contract.

### fn `def cmd_lh(extra)` (L2254-2257)
- Return: Result emitted by `cmd_lh` according to command contract.

### fn `def cmd_ll(extra)` (L2262-2274)
- Return: Result emitted by `cmd_ll` according to command contract.

### fn `def cmd_lm(extra)` (L2279-2282)
- Return: Result emitted by `cmd_lm` according to command contract.

### fn `def cmd_lt(extra)` (L2287-2290)
- Return: Result emitted by `cmd_lt` according to command contract.

### fn `def cmd_me(extra)` (L2295-2298)
- Return: Result emitted by `cmd_me` according to command contract.

### fn `def cmd_pl(extra)` (L2303-2306)
- Return: Result emitted by `cmd_pl` according to command contract.

### fn `def cmd_pt(extra)` (L2311-2314)
- Return: Result emitted by `cmd_pt` according to command contract.

### fn `def cmd_pu(extra)` (L2319-2322)
- Return: Result emitted by `cmd_pu` according to command contract.

### fn `def cmd_rf(extra)` (L2327-2330)
- Return: Result emitted by `cmd_rf` according to command contract.

### fn `def cmd_rmtg(extra)` (L2335-2345)
- Return: Result emitted by `cmd_rmtg` according to command contract.

### fn `def cmd_rmloc(extra)` (L2350-2353)
- Return: Result emitted by `cmd_rmloc` according to command contract.

### fn `def cmd_rmstg(extra)` (L2358-2361)
- Return: Result emitted by `cmd_rmstg` according to command contract.

### fn `def cmd_rmunt(extra)` (L2366-2369)
- Return: Result emitted by `cmd_rmunt` according to command contract.

### fn `def cmd_rs(extra)` (L2374-2377)
- Return: Result emitted by `cmd_rs` according to command contract.

### fn `def cmd_rssft(extra)` (L2382-2385)
- Return: Result emitted by `cmd_rssft` according to command contract.

### fn `def cmd_rsmix(extra)` (L2390-2393)
- Return: Result emitted by `cmd_rsmix` according to command contract.

### fn `def cmd_rshrd(extra)` (L2398-2401)
- Return: Result emitted by `cmd_rshrd` according to command contract.

### fn `def cmd_rsmrg(extra)` (L2406-2409)
- Return: Result emitted by `cmd_rsmrg` according to command contract.

### fn `def cmd_rskep(extra)` (L2414-2417)
- Return: Result emitted by `cmd_rskep` according to command contract.

### fn `def cmd_st(extra)` (L2422-2425)
- Return: Result emitted by `cmd_st` according to command contract.

### fn `def cmd_tg(extra)` (L2430-2433)
- Return: Result emitted by `cmd_tg` according to command contract.

### fn `def cmd_unstg(extra)` (L2438-2441)
- Return: Result emitted by `cmd_unstg` according to command contract.

### fn `def cmd_ver(extra)` (L2446-2464)
- Return: Result emitted by `cmd_ver` according to command contract.

### fn `def cmd_chver(extra)` (L2469-2539)
- Return: Result emitted by `cmd_chver` according to command contract.

### fn `def cmd_major(extra)` (L2547-2551)
- Sa: tisfies REQ-026, REQ-045

### fn `def cmd_minor(extra)` (L2559-2563)
- Sa: tisfies REQ-026, REQ-045

### fn `def cmd_patch(extra)` (L2571-2575)
- Sa: tisfies REQ-026, REQ-045

### fn `def cmd_changelog(extra)` (L2584-2615)
- Sa: tisfies REQ-018, REQ-040, REQ-041

- var `COMMANDS = {` (L2618)
- Brief: Constant `COMMANDS` used by CLI runtime paths and policies.
### fn `def print_command_help(name, width=None)` (L2690-2696)
- Return: Result emitted by `print_command_help` according to command contract.

### fn `def print_all_help()` (L2700-2734)
- Return: Result emitted by `print_all_help` according to command contract.

### fn `def main(argv=None, *, check_updates: bool = True)` (L2740-2790)
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
|`RESET_HELP_COMMANDS`|var|pub|529||
|`_to_args`|fn|priv|536-539|def _to_args(extra)|
|`CommandExecutionError`|class|pub|541-582|class CommandExecutionError(RuntimeError)|
|`CommandExecutionError.__init__`|fn|priv|546-553|def __init__(self, exc: subprocess.CalledProcessError)|
|`CommandExecutionError._format_message`|fn|priv|557-567|def _format_message(self) -> str|
|`CommandExecutionError._decode_stream`|fn|priv|572-582|def _decode_stream(data) -> str|
|`_run_checked`|fn|priv|588-595|def _run_checked(*popenargs, **kwargs)|
|`VersionDetectionError`|class|pub|597-600|class VersionDetectionError(RuntimeError)|
|`ReleaseError`|class|pub|602-605|class ReleaseError(RuntimeError)|
|`run_git_cmd`|fn|pub|613-617|def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)|
|`capture_git_output`|fn|pub|623-627|def capture_git_output(base_args, cwd=None)|
|`run_command`|fn|pub|633-636|def run_command(cmd, cwd=None)|
|`run_git_text`|fn|pub|643-660|def run_git_text(args, cwd=None, check=True)|
|`run_shell`|fn|pub|666-669|def run_shell(command, cwd=None)|
|`_git_status_lines`|fn|priv|673-685|def _git_status_lines()|
|`has_unstaged_changes`|fn|pub|690-701|def has_unstaged_changes(status_lines=None)|
|`has_staged_changes`|fn|pub|706-715|def has_staged_changes(status_lines=None)|
|`WIP_MESSAGE_RE`|var|pub|721||
|`_refresh_remote_refs`|fn|priv|727-738|def _refresh_remote_refs()|
|`_branch_remote_divergence`|fn|priv|744-762|def _branch_remote_divergence(branch_key, remote="origin")|
|`has_remote_branch_updates`|fn|pub|768-772|def has_remote_branch_updates(branch_key, remote="origin")|
|`has_remote_develop_updates`|fn|pub|776-779|def has_remote_develop_updates()|
|`has_remote_master_updates`|fn|pub|783-786|def has_remote_master_updates()|
|`_head_commit_message`|fn|priv|790-796|def _head_commit_message()|
|`_head_commit_hash`|fn|priv|800-806|def _head_commit_hash()|
|`_commit_exists_in_branch`|fn|priv|812-824|def _commit_exists_in_branch(commit_hash, branch_name)|
|`_should_amend_existing_commit`|fn|priv|828-843|def _should_amend_existing_commit()|
|`is_inside_git_repo`|fn|pub|847-854|def is_inside_git_repo()|
|`TagInfo`|class|pub|859-867|class TagInfo|
|`DELIM`|var|pub|870||
|`RECORD`|var|pub|873||
|`SEMVER_RE`|var|pub|889||
|`SECTION_EMOJI`|var|pub|892||
|`_tag_semver_tuple`|fn|priv|909-912|def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[in...|
|`_latest_supported_tag_name`|fn|priv|917-920|def _latest_supported_tag_name(tags: List[TagInfo]) -> Op...|
|`_is_minor_release_tag`|fn|priv|928-935|def _is_minor_release_tag(tag_name: str) -> bool|
|`_latest_patch_tag_after`|fn|priv|944-953|def _latest_patch_tag_after(all_tags: List[TagInfo], last...|
|`list_tags_sorted_by_date`|fn|pub|959-979|def list_tags_sorted_by_date(repo_root: Path, merged_ref:...|
|`git_log_subjects`|fn|pub|985-996|def git_log_subjects(repo_root: Path, rev_range: str) -> ...|
|`categorize_commit`|fn|pub|1002-1026|def categorize_commit(subject: str) -> Tuple[Optional[str...|
|`_extract_release_version`|fn|priv|1031-1041|def _extract_release_version(subject: str) -> Optional[str]|
|`_is_release_marker_commit`|fn|priv|1046-1049|def _is_release_marker_commit(subject: str) -> bool|
|`generate_section_for_range`|fn|pub|1058-1096|def generate_section_for_range(repo_root: Path, title: st...|
|`_get_remote_name_for_branch`|fn|priv|1105-1113|def _get_remote_name_for_branch(branch_name: str, repo_ro...|
|`_canonical_origin_base`|fn|priv|1123-1142|def _canonical_origin_base(repo_root: Path) -> Optional[str]|
|`get_origin_compare_url`|fn|pub|1149-1156|def get_origin_compare_url(base_url: Optional[str], prev_...|
|`get_release_page_url`|fn|pub|1162-1167|def get_release_page_url(base_url: Optional[str], tag: st...|
|`build_history_section`|fn|pub|1175-1179|def build_history_section(|
|`generate_changelog_document`|fn|pub|1222-1282|def generate_changelog_document(repo_root: Path, include_...|
|`_collect_version_files`|fn|priv|1288-1323|def _collect_version_files(root, pattern)|
|`_is_version_path_excluded`|fn|priv|1328-1331|def _is_version_path_excluded(relative_path: str) -> bool|
|`_iter_versions_in_text`|fn|priv|1337-1348|def _iter_versions_in_text(text, compiled_regexes)|
|`_determine_canonical_version`|fn|priv|1356-1415|def _determine_canonical_version(root: Path, rules, *, ve...|
|`_parse_semver_tuple`|fn|priv|1420-1426|def _parse_semver_tuple(text: str) -> Optional[Tuple[int,...|
|`_replace_versions_in_text`|fn|priv|1433-1448|def _replace_versions_in_text(text, compiled_regex, repla...|
|`_current_branch_name`|fn|priv|1452-1464|def _current_branch_name()|
|`_ref_exists`|fn|priv|1469-1478|def _ref_exists(ref_name)|
|`_local_branch_exists`|fn|priv|1483-1486|def _local_branch_exists(branch_name)|
|`_remote_branch_exists`|fn|priv|1491-1494|def _remote_branch_exists(branch_name)|
|`_ensure_release_prerequisites`|fn|priv|1498-1525|def _ensure_release_prerequisites()|
|`_bump_semver_version`|fn|priv|1531-1549|def _bump_semver_version(current_version, level)|
|`_run_release_step`|fn|priv|1556-1576|def _run_release_step(level, step_name, action)|
|`_create_release_commit_for_flow`|fn|priv|1581-1586|def _create_release_commit_for_flow(target_version)|
|`_execute_release_flow`|fn|priv|1598-1645|def _execute_release_flow(level, changelog_args=None)|
|`_run_release_command`|fn|priv|1651-1666|def _run_release_command(level, changelog_args=None)|
|`_run_reset_with_help`|fn|priv|1672-1679|def _run_reset_with_help(base_args, extra)|
|`_reject_extra_arguments`|fn|priv|1685-1691|def _reject_extra_arguments(extra, alias)|
|`_parse_release_flags`|fn|priv|1697-1715|def _parse_release_flags(extra, alias)|
|`_prepare_commit_message`|fn|priv|1721-1731|def _prepare_commit_message(extra, alias)|
|`_build_conventional_message`|fn|priv|1738-1752|def _build_conventional_message(kind: str, extra, alias: ...|
|`_run_conventional_commit`|fn|priv|1759-1764|def _run_conventional_commit(kind: str, alias: str, extra)|
|`_execute_commit`|fn|priv|1771-1800|def _execute_commit(message, alias, allow_amend=True)|
|`upgrade_self`|fn|pub|1804-1817|def upgrade_self()|
|`remove_self`|fn|pub|1821-1824|def remove_self()|
|`cmd_aa`|fn|pub|1829-1836|def cmd_aa(extra)|
|`cmd_ra`|fn|pub|1841-1864|def cmd_ra(extra)|
|`cmd_ar`|fn|pub|1869-1883|def cmd_ar(extra)|
|`cmd_br`|fn|pub|1888-1891|def cmd_br(extra)|
|`cmd_bd`|fn|pub|1896-1899|def cmd_bd(extra)|
|`cmd_ck`|fn|pub|1904-1907|def cmd_ck(extra)|
|`_ensure_commit_ready`|fn|priv|1912-1925|def _ensure_commit_ready(alias)|
|`cmd_cm`|fn|pub|1930-1935|def cmd_cm(extra)|
|`cmd_wip`|fn|pub|1940-1952|def cmd_wip(extra)|
|`cmd_release`|fn|pub|1957-1979|def cmd_release(extra)|
|`cmd_new`|fn|pub|1984-1987|def cmd_new(extra)|
|`cmd_refactor`|fn|pub|1992-1995|def cmd_refactor(extra)|
|`cmd_fix`|fn|pub|2000-2003|def cmd_fix(extra)|
|`cmd_change`|fn|pub|2008-2011|def cmd_change(extra)|
|`cmd_implement`|fn|pub|2016-2019|def cmd_implement(extra)|
|`cmd_docs`|fn|pub|2024-2027|def cmd_docs(extra)|
|`cmd_style`|fn|pub|2032-2035|def cmd_style(extra)|
|`cmd_revert`|fn|pub|2040-2043|def cmd_revert(extra)|
|`cmd_misc`|fn|pub|2048-2051|def cmd_misc(extra)|
|`cmd_cover`|fn|pub|2056-2059|def cmd_cover(extra)|
|`cmd_co`|fn|pub|2064-2067|def cmd_co(extra)|
|`cmd_d`|fn|pub|2072-2079|def cmd_d(extra)|
|`cmd_dcc`|fn|pub|2084-2087|def cmd_dcc(extra)|
|`cmd_dccc`|fn|pub|2092-2095|def cmd_dccc(extra)|
|`cmd_de`|fn|pub|2100-2103|def cmd_de(extra)|
|`cmd_di`|fn|pub|2108-2111|def cmd_di(extra)|
|`cmd_diyou`|fn|pub|2116-2119|def cmd_diyou(extra)|
|`cmd_dime`|fn|pub|2124-2127|def cmd_dime(extra)|
|`cmd_dwc`|fn|pub|2132-2135|def cmd_dwc(extra)|
|`cmd_dwcc`|fn|pub|2140-2143|def cmd_dwcc(extra)|
|`cmd_ed`|fn|pub|2148-2157|def cmd_ed(extra)|
|`cmd_fe`|fn|pub|2162-2165|def cmd_fe(extra)|
|`cmd_feall`|fn|pub|2170-2173|def cmd_feall(extra)|
|`cmd_gp`|fn|pub|2178-2181|def cmd_gp(extra)|
|`cmd_gr`|fn|pub|2186-2189|def cmd_gr(extra)|
|`cmd_str`|fn|pub|2194-2223|def cmd_str(extra)|
|`cmd_lb`|fn|pub|2228-2231|def cmd_lb(extra)|
|`cmd_lg`|fn|pub|2236-2249|def cmd_lg(extra)|
|`cmd_lh`|fn|pub|2254-2257|def cmd_lh(extra)|
|`cmd_ll`|fn|pub|2262-2274|def cmd_ll(extra)|
|`cmd_lm`|fn|pub|2279-2282|def cmd_lm(extra)|
|`cmd_lt`|fn|pub|2287-2290|def cmd_lt(extra)|
|`cmd_me`|fn|pub|2295-2298|def cmd_me(extra)|
|`cmd_pl`|fn|pub|2303-2306|def cmd_pl(extra)|
|`cmd_pt`|fn|pub|2311-2314|def cmd_pt(extra)|
|`cmd_pu`|fn|pub|2319-2322|def cmd_pu(extra)|
|`cmd_rf`|fn|pub|2327-2330|def cmd_rf(extra)|
|`cmd_rmtg`|fn|pub|2335-2345|def cmd_rmtg(extra)|
|`cmd_rmloc`|fn|pub|2350-2353|def cmd_rmloc(extra)|
|`cmd_rmstg`|fn|pub|2358-2361|def cmd_rmstg(extra)|
|`cmd_rmunt`|fn|pub|2366-2369|def cmd_rmunt(extra)|
|`cmd_rs`|fn|pub|2374-2377|def cmd_rs(extra)|
|`cmd_rssft`|fn|pub|2382-2385|def cmd_rssft(extra)|
|`cmd_rsmix`|fn|pub|2390-2393|def cmd_rsmix(extra)|
|`cmd_rshrd`|fn|pub|2398-2401|def cmd_rshrd(extra)|
|`cmd_rsmrg`|fn|pub|2406-2409|def cmd_rsmrg(extra)|
|`cmd_rskep`|fn|pub|2414-2417|def cmd_rskep(extra)|
|`cmd_st`|fn|pub|2422-2425|def cmd_st(extra)|
|`cmd_tg`|fn|pub|2430-2433|def cmd_tg(extra)|
|`cmd_unstg`|fn|pub|2438-2441|def cmd_unstg(extra)|
|`cmd_ver`|fn|pub|2446-2464|def cmd_ver(extra)|
|`cmd_chver`|fn|pub|2469-2539|def cmd_chver(extra)|
|`cmd_major`|fn|pub|2547-2551|def cmd_major(extra)|
|`cmd_minor`|fn|pub|2559-2563|def cmd_minor(extra)|
|`cmd_patch`|fn|pub|2571-2575|def cmd_patch(extra)|
|`cmd_changelog`|fn|pub|2584-2615|def cmd_changelog(extra)|
|`COMMANDS`|var|pub|2618||
|`print_command_help`|fn|pub|2690-2696|def print_command_help(name, width=None)|
|`print_all_help`|fn|pub|2700-2734|def print_all_help()|
|`main`|fn|pub|2740-2790|def main(argv=None, *, check_updates: bool = True)|

