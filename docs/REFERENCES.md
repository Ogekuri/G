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

# core.py | Python | 2928L | 176 symbols | 16 imports | 758 comments
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

### fn `def _extract_owner_repo(remote_url: str) -> Optional[Tuple[str, str]]` `priv` (L1120-1144)
- Return: Tuple `(owner, repo)` when parsing succeeds; otherwise `None`.

### fn `def _canonical_origin_base(repo_root: Path) -> Optional[str]` `priv` (L1154-1167)
- Sa: tisfies REQ-043, REQ-046

### fn `def get_origin_compare_url(base_url: Optional[str], prev_tag: Optional[str], tag: str) -> Optional[str]` (L1174-1181)
- Return: Result emitted by `get_origin_compare_url` according to command contract.

### fn `def get_release_page_url(base_url: Optional[str], tag: str) -> Optional[str]` (L1187-1192)
- Return: Result emitted by `get_release_page_url` according to command contract.

### fn `def build_history_section(` (L1200-1204)
- Return: Result emitted by `build_history_section` according to command contract.

### fn `def generate_changelog_document(repo_root: Path, include_patch: bool, disable_history: bool = False) -> str` (L1248-1309)
- Sa: tisfies REQ-018, REQ-040, REQ-041, REQ-043, REQ-068, REQ-069, REQ-070

### class `class VersionRuleContext` `@dataclass(frozen=True)` (L1320-1327)
- Note: Complexity: O(1) storage per field; aggregate complexity scales with matched file count per rule.

### fn `def _normalize_version_rule_pattern(pattern: str) -> str` `priv` (L1333-1344)
- Return: Normalized pathspec-compatible pattern string; empty string when input is blank.

### fn `def _build_version_file_inventory(root: Path) -> List[Tuple[Path, str]]` `priv` (L1350-1371)
- Return: List of tuples `(absolute_path, normalized_relative_path)` used by downstream matchers.

### fn `def _collect_version_files(root, pattern, *, inventory=None)` `priv` (L1379-1396)
- Details: Apply pathspec matcher to preserve configured GitIgnore-like semantics.
- Return: Result emitted by `_collect_version_files` according to command contract.

### fn `def _is_version_path_excluded(relative_path: str) -> bool` `priv` (L1401-1404)
- Return: Result emitted by `_is_version_path_excluded` according to command contract.

### fn `def _iter_versions_in_text(text, compiled_regexes)` `priv` (L1410-1421)
- Return: Result emitted by `_iter_versions_in_text` according to command contract.

### fn `def _read_version_file_text(file_path: Path, text_cache: Optional[Dict[Path, str]] = None) -> Optional[str]` `priv` (L1428-1442)
- Return: File text payload or `None` when file cannot be read.

### fn `def _prepare_version_rule_contexts(` `priv` (L1451-1452)
- Throws: VersionDetectionError when a rule matches no files or contains an invalid regex.

### fn `def _determine_canonical_version(` `priv` (L1494-1501)
- Return: Result emitted by `_determine_canonical_version` according to command contract.

### fn `def _parse_semver_tuple(text: str) -> Optional[Tuple[int, int, int]]` `priv` (L1546-1552)
- Return: Result emitted by `_parse_semver_tuple` according to command contract.

### fn `def _replace_versions_in_text(text, compiled_regex, replacement)` `priv` (L1559-1574)
- Return: Result emitted by `_replace_versions_in_text` according to command contract.

### fn `def _current_branch_name()` `priv` (L1578-1590)
- Return: Result emitted by `_current_branch_name` according to command contract.

### fn `def _ref_exists(ref_name)` `priv` (L1595-1604)
- Return: Result emitted by `_ref_exists` according to command contract.

### fn `def _local_branch_exists(branch_name)` `priv` (L1609-1612)
- Return: Result emitted by `_local_branch_exists` according to command contract.

### fn `def _remote_branch_exists(branch_name)` `priv` (L1617-1620)
- Return: Result emitted by `_remote_branch_exists` according to command contract.

### fn `def _ensure_release_prerequisites()` `priv` (L1624-1651)
- Return: Result emitted by `_ensure_release_prerequisites` according to command contract.

### fn `def _bump_semver_version(current_version, level)` `priv` (L1657-1675)
- Return: Result emitted by `_bump_semver_version` according to command contract.

### fn `def _run_release_step(level, step_name, action)` `priv` (L1682-1702)
- Return: Result emitted by `_run_release_step` according to command contract.

### fn `def _create_release_commit_for_flow(target_version)` `priv` (L1707-1712)
- Return: Result emitted by `_create_release_commit_for_flow` according to command contract.

### fn `def _execute_release_flow(level, changelog_args=None)` `priv` (L1724-1771)
- Sa: tisfies REQ-026, REQ-045

### fn `def _run_release_command(level, changelog_args=None)` `priv` (L1777-1792)
- Return: Result emitted by `_run_release_command` according to command contract.

### fn `def _run_reset_with_help(base_args, extra)` `priv` (L1798-1805)
- Return: Result emitted by `_run_reset_with_help` according to command contract.

### fn `def _reject_extra_arguments(extra, alias)` `priv` (L1811-1817)
- Return: Result emitted by `_reject_extra_arguments` according to command contract.

### fn `def _parse_release_flags(extra, alias)` `priv` (L1823-1841)
- Return: Result emitted by `_parse_release_flags` according to command contract.

### fn `def _prepare_commit_message(extra, alias)` `priv` (L1847-1857)
- Return: Result emitted by `_prepare_commit_message` according to command contract.

### fn `def _build_conventional_message(kind: str, extra, alias: str) -> str` `priv` (L1864-1878)
- Return: Result emitted by `_build_conventional_message` according to command contract.

### fn `def _run_conventional_commit(kind: str, alias: str, extra)` `priv` (L1885-1890)
- Return: Result emitted by `_run_conventional_commit` according to command contract.

### fn `def _execute_commit(message, alias, allow_amend=True)` `priv` (L1897-1926)
- Return: Result emitted by `_execute_commit` according to command contract.

### fn `def upgrade_self()` (L1930-1943)
- Return: Result emitted by `upgrade_self` according to command contract.

### fn `def remove_self()` (L1947-1950)
- Return: Result emitted by `remove_self` according to command contract.

### fn `def cmd_aa(extra)` (L1955-1962)
- Return: Result emitted by `cmd_aa` according to command contract.

### fn `def cmd_ra(extra)` (L1967-1990)
- Return: Result emitted by `cmd_ra` according to command contract.

### fn `def cmd_ar(extra)` (L1995-2009)
- Return: Result emitted by `cmd_ar` according to command contract.

### fn `def cmd_br(extra)` (L2014-2017)
- Return: Result emitted by `cmd_br` according to command contract.

### fn `def cmd_bd(extra)` (L2022-2025)
- Return: Result emitted by `cmd_bd` according to command contract.

### fn `def cmd_ck(extra)` (L2030-2033)
- Return: Result emitted by `cmd_ck` according to command contract.

### fn `def _ensure_commit_ready(alias)` `priv` (L2038-2051)
- Return: Result emitted by `_ensure_commit_ready` according to command contract.

### fn `def cmd_cm(extra)` (L2056-2061)
- Return: Result emitted by `cmd_cm` according to command contract.

### fn `def cmd_wip(extra)` (L2066-2078)
- Return: Result emitted by `cmd_wip` according to command contract.

### fn `def cmd_release(extra)` (L2083-2105)
- Return: Result emitted by `cmd_release` according to command contract.

### fn `def cmd_new(extra)` (L2110-2113)
- Return: Result emitted by `cmd_new` according to command contract.

### fn `def cmd_refactor(extra)` (L2118-2121)
- Return: Result emitted by `cmd_refactor` according to command contract.

### fn `def cmd_fix(extra)` (L2126-2129)
- Return: Result emitted by `cmd_fix` according to command contract.

### fn `def cmd_change(extra)` (L2134-2137)
- Return: Result emitted by `cmd_change` according to command contract.

### fn `def cmd_implement(extra)` (L2142-2145)
- Return: Result emitted by `cmd_implement` according to command contract.

### fn `def cmd_docs(extra)` (L2150-2153)
- Return: Result emitted by `cmd_docs` according to command contract.

### fn `def cmd_style(extra)` (L2158-2161)
- Return: Result emitted by `cmd_style` according to command contract.

### fn `def cmd_revert(extra)` (L2166-2169)
- Return: Result emitted by `cmd_revert` according to command contract.

### fn `def cmd_misc(extra)` (L2174-2177)
- Return: Result emitted by `cmd_misc` according to command contract.

### fn `def cmd_cover(extra)` (L2182-2185)
- Return: Result emitted by `cmd_cover` according to command contract.

### fn `def cmd_co(extra)` (L2190-2193)
- Return: Result emitted by `cmd_co` according to command contract.

### fn `def cmd_d(extra)` (L2198-2205)
- Return: Result emitted by `cmd_d` according to command contract.

### fn `def cmd_dcc(extra)` (L2210-2213)
- Return: Result emitted by `cmd_dcc` according to command contract.

### fn `def cmd_dccc(extra)` (L2218-2221)
- Return: Result emitted by `cmd_dccc` according to command contract.

### fn `def cmd_de(extra)` (L2226-2229)
- Return: Result emitted by `cmd_de` according to command contract.

### fn `def cmd_di(extra)` (L2234-2237)
- Return: Result emitted by `cmd_di` according to command contract.

### fn `def cmd_diyou(extra)` (L2242-2245)
- Return: Result emitted by `cmd_diyou` according to command contract.

### fn `def cmd_dime(extra)` (L2250-2253)
- Return: Result emitted by `cmd_dime` according to command contract.

### fn `def cmd_dwc(extra)` (L2258-2261)
- Return: Result emitted by `cmd_dwc` according to command contract.

### fn `def cmd_dwcc(extra)` (L2266-2269)
- Return: Result emitted by `cmd_dwcc` according to command contract.

### fn `def cmd_ed(extra)` (L2274-2283)
- Return: Result emitted by `cmd_ed` according to command contract.

### fn `def cmd_fe(extra)` (L2288-2291)
- Return: Result emitted by `cmd_fe` according to command contract.

### fn `def cmd_feall(extra)` (L2296-2299)
- Return: Result emitted by `cmd_feall` according to command contract.

### fn `def cmd_gp(extra)` (L2304-2307)
- Return: Result emitted by `cmd_gp` according to command contract.

### fn `def cmd_gr(extra)` (L2312-2315)
- Return: Result emitted by `cmd_gr` according to command contract.

### fn `def cmd_str(extra)` (L2320-2349)
- Details: Query git remotes with transport metadata. Deduplicate remote names from `git remote -v` rows. Print normalized remote name inventory. Print detailed status for each unique remote.
- Return: Result emitted by `cmd_str` according to command contract.

### fn `def cmd_lb(extra)` (L2354-2357)
- Return: Result emitted by `cmd_lb` according to command contract.

### fn `def cmd_lg(extra)` (L2362-2375)
- Return: Result emitted by `cmd_lg` according to command contract.

### fn `def cmd_lh(extra)` (L2380-2383)
- Return: Result emitted by `cmd_lh` according to command contract.

### fn `def cmd_ll(extra)` (L2388-2400)
- Return: Result emitted by `cmd_ll` according to command contract.

### fn `def cmd_lm(extra)` (L2405-2408)
- Return: Result emitted by `cmd_lm` according to command contract.

### fn `def cmd_lt(extra)` (L2413-2416)
- Return: Result emitted by `cmd_lt` according to command contract.

### fn `def cmd_me(extra)` (L2421-2424)
- Return: Result emitted by `cmd_me` according to command contract.

### fn `def cmd_pl(extra)` (L2429-2432)
- Return: Result emitted by `cmd_pl` according to command contract.

### fn `def cmd_pt(extra)` (L2437-2440)
- Return: Result emitted by `cmd_pt` according to command contract.

### fn `def cmd_pu(extra)` (L2445-2448)
- Return: Result emitted by `cmd_pu` according to command contract.

### fn `def cmd_rf(extra)` (L2453-2456)
- Return: Result emitted by `cmd_rf` according to command contract.

### fn `def cmd_rmtg(extra)` (L2461-2471)
- Return: Result emitted by `cmd_rmtg` according to command contract.

### fn `def cmd_rmloc(extra)` (L2476-2479)
- Return: Result emitted by `cmd_rmloc` according to command contract.

### fn `def cmd_rmstg(extra)` (L2484-2487)
- Return: Result emitted by `cmd_rmstg` according to command contract.

### fn `def cmd_rmunt(extra)` (L2492-2495)
- Return: Result emitted by `cmd_rmunt` according to command contract.

### fn `def cmd_rs(extra)` (L2500-2503)
- Return: Result emitted by `cmd_rs` according to command contract.

### fn `def cmd_rssft(extra)` (L2508-2511)
- Return: Result emitted by `cmd_rssft` according to command contract.

### fn `def cmd_rsmix(extra)` (L2516-2519)
- Return: Result emitted by `cmd_rsmix` according to command contract.

### fn `def cmd_rshrd(extra)` (L2524-2527)
- Return: Result emitted by `cmd_rshrd` according to command contract.

### fn `def cmd_rsmrg(extra)` (L2532-2535)
- Return: Result emitted by `cmd_rsmrg` according to command contract.

### fn `def cmd_rskep(extra)` (L2540-2543)
- Return: Result emitted by `cmd_rskep` according to command contract.

### fn `def cmd_st(extra)` (L2548-2551)
- Return: Result emitted by `cmd_st` according to command contract.

### fn `def cmd_tg(extra)` (L2556-2559)
- Return: Result emitted by `cmd_tg` according to command contract.

### fn `def cmd_unstg(extra)` (L2564-2567)
- Return: Result emitted by `cmd_unstg` according to command contract.

### fn `def cmd_ver(extra)` (L2572-2598)
- Return: Result emitted by `cmd_ver` according to command contract.

### fn `def cmd_chver(extra)` (L2603-2675)
- Return: Result emitted by `cmd_chver` according to command contract.

### fn `def cmd_major(extra)` (L2683-2687)
- Sa: tisfies REQ-026, REQ-045

### fn `def cmd_minor(extra)` (L2695-2699)
- Sa: tisfies REQ-026, REQ-045

### fn `def cmd_patch(extra)` (L2707-2711)
- Sa: tisfies REQ-026, REQ-045

### fn `def cmd_changelog(extra)` (L2721-2753)
- Sa: tisfies REQ-018, REQ-040, REQ-041, REQ-043

- var `COMMANDS = {` (L2756)
- Brief: Constant `COMMANDS` used by CLI runtime paths and policies.
### fn `def print_command_help(name, width=None)` (L2828-2834)
- Return: Result emitted by `print_command_help` according to command contract.

### fn `def print_all_help()` (L2838-2872)
- Return: Result emitted by `print_all_help` according to command contract.

### fn `def main(argv=None, *, check_updates: bool = True)` (L2878-2928)
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
|`_extract_owner_repo`|fn|priv|1120-1144|def _extract_owner_repo(remote_url: str) -> Optional[Tupl...|
|`_canonical_origin_base`|fn|priv|1154-1167|def _canonical_origin_base(repo_root: Path) -> Optional[str]|
|`get_origin_compare_url`|fn|pub|1174-1181|def get_origin_compare_url(base_url: Optional[str], prev_...|
|`get_release_page_url`|fn|pub|1187-1192|def get_release_page_url(base_url: Optional[str], tag: st...|
|`build_history_section`|fn|pub|1200-1204|def build_history_section(|
|`generate_changelog_document`|fn|pub|1248-1309|def generate_changelog_document(repo_root: Path, include_...|
|`VersionRuleContext`|class|pub|1320-1327|class VersionRuleContext|
|`_normalize_version_rule_pattern`|fn|priv|1333-1344|def _normalize_version_rule_pattern(pattern: str) -> str|
|`_build_version_file_inventory`|fn|priv|1350-1371|def _build_version_file_inventory(root: Path) -> List[Tup...|
|`_collect_version_files`|fn|priv|1379-1396|def _collect_version_files(root, pattern, *, inventory=None)|
|`_is_version_path_excluded`|fn|priv|1401-1404|def _is_version_path_excluded(relative_path: str) -> bool|
|`_iter_versions_in_text`|fn|priv|1410-1421|def _iter_versions_in_text(text, compiled_regexes)|
|`_read_version_file_text`|fn|priv|1428-1442|def _read_version_file_text(file_path: Path, text_cache: ...|
|`_prepare_version_rule_contexts`|fn|priv|1451-1452|def _prepare_version_rule_contexts(|
|`_determine_canonical_version`|fn|priv|1494-1501|def _determine_canonical_version(|
|`_parse_semver_tuple`|fn|priv|1546-1552|def _parse_semver_tuple(text: str) -> Optional[Tuple[int,...|
|`_replace_versions_in_text`|fn|priv|1559-1574|def _replace_versions_in_text(text, compiled_regex, repla...|
|`_current_branch_name`|fn|priv|1578-1590|def _current_branch_name()|
|`_ref_exists`|fn|priv|1595-1604|def _ref_exists(ref_name)|
|`_local_branch_exists`|fn|priv|1609-1612|def _local_branch_exists(branch_name)|
|`_remote_branch_exists`|fn|priv|1617-1620|def _remote_branch_exists(branch_name)|
|`_ensure_release_prerequisites`|fn|priv|1624-1651|def _ensure_release_prerequisites()|
|`_bump_semver_version`|fn|priv|1657-1675|def _bump_semver_version(current_version, level)|
|`_run_release_step`|fn|priv|1682-1702|def _run_release_step(level, step_name, action)|
|`_create_release_commit_for_flow`|fn|priv|1707-1712|def _create_release_commit_for_flow(target_version)|
|`_execute_release_flow`|fn|priv|1724-1771|def _execute_release_flow(level, changelog_args=None)|
|`_run_release_command`|fn|priv|1777-1792|def _run_release_command(level, changelog_args=None)|
|`_run_reset_with_help`|fn|priv|1798-1805|def _run_reset_with_help(base_args, extra)|
|`_reject_extra_arguments`|fn|priv|1811-1817|def _reject_extra_arguments(extra, alias)|
|`_parse_release_flags`|fn|priv|1823-1841|def _parse_release_flags(extra, alias)|
|`_prepare_commit_message`|fn|priv|1847-1857|def _prepare_commit_message(extra, alias)|
|`_build_conventional_message`|fn|priv|1864-1878|def _build_conventional_message(kind: str, extra, alias: ...|
|`_run_conventional_commit`|fn|priv|1885-1890|def _run_conventional_commit(kind: str, alias: str, extra)|
|`_execute_commit`|fn|priv|1897-1926|def _execute_commit(message, alias, allow_amend=True)|
|`upgrade_self`|fn|pub|1930-1943|def upgrade_self()|
|`remove_self`|fn|pub|1947-1950|def remove_self()|
|`cmd_aa`|fn|pub|1955-1962|def cmd_aa(extra)|
|`cmd_ra`|fn|pub|1967-1990|def cmd_ra(extra)|
|`cmd_ar`|fn|pub|1995-2009|def cmd_ar(extra)|
|`cmd_br`|fn|pub|2014-2017|def cmd_br(extra)|
|`cmd_bd`|fn|pub|2022-2025|def cmd_bd(extra)|
|`cmd_ck`|fn|pub|2030-2033|def cmd_ck(extra)|
|`_ensure_commit_ready`|fn|priv|2038-2051|def _ensure_commit_ready(alias)|
|`cmd_cm`|fn|pub|2056-2061|def cmd_cm(extra)|
|`cmd_wip`|fn|pub|2066-2078|def cmd_wip(extra)|
|`cmd_release`|fn|pub|2083-2105|def cmd_release(extra)|
|`cmd_new`|fn|pub|2110-2113|def cmd_new(extra)|
|`cmd_refactor`|fn|pub|2118-2121|def cmd_refactor(extra)|
|`cmd_fix`|fn|pub|2126-2129|def cmd_fix(extra)|
|`cmd_change`|fn|pub|2134-2137|def cmd_change(extra)|
|`cmd_implement`|fn|pub|2142-2145|def cmd_implement(extra)|
|`cmd_docs`|fn|pub|2150-2153|def cmd_docs(extra)|
|`cmd_style`|fn|pub|2158-2161|def cmd_style(extra)|
|`cmd_revert`|fn|pub|2166-2169|def cmd_revert(extra)|
|`cmd_misc`|fn|pub|2174-2177|def cmd_misc(extra)|
|`cmd_cover`|fn|pub|2182-2185|def cmd_cover(extra)|
|`cmd_co`|fn|pub|2190-2193|def cmd_co(extra)|
|`cmd_d`|fn|pub|2198-2205|def cmd_d(extra)|
|`cmd_dcc`|fn|pub|2210-2213|def cmd_dcc(extra)|
|`cmd_dccc`|fn|pub|2218-2221|def cmd_dccc(extra)|
|`cmd_de`|fn|pub|2226-2229|def cmd_de(extra)|
|`cmd_di`|fn|pub|2234-2237|def cmd_di(extra)|
|`cmd_diyou`|fn|pub|2242-2245|def cmd_diyou(extra)|
|`cmd_dime`|fn|pub|2250-2253|def cmd_dime(extra)|
|`cmd_dwc`|fn|pub|2258-2261|def cmd_dwc(extra)|
|`cmd_dwcc`|fn|pub|2266-2269|def cmd_dwcc(extra)|
|`cmd_ed`|fn|pub|2274-2283|def cmd_ed(extra)|
|`cmd_fe`|fn|pub|2288-2291|def cmd_fe(extra)|
|`cmd_feall`|fn|pub|2296-2299|def cmd_feall(extra)|
|`cmd_gp`|fn|pub|2304-2307|def cmd_gp(extra)|
|`cmd_gr`|fn|pub|2312-2315|def cmd_gr(extra)|
|`cmd_str`|fn|pub|2320-2349|def cmd_str(extra)|
|`cmd_lb`|fn|pub|2354-2357|def cmd_lb(extra)|
|`cmd_lg`|fn|pub|2362-2375|def cmd_lg(extra)|
|`cmd_lh`|fn|pub|2380-2383|def cmd_lh(extra)|
|`cmd_ll`|fn|pub|2388-2400|def cmd_ll(extra)|
|`cmd_lm`|fn|pub|2405-2408|def cmd_lm(extra)|
|`cmd_lt`|fn|pub|2413-2416|def cmd_lt(extra)|
|`cmd_me`|fn|pub|2421-2424|def cmd_me(extra)|
|`cmd_pl`|fn|pub|2429-2432|def cmd_pl(extra)|
|`cmd_pt`|fn|pub|2437-2440|def cmd_pt(extra)|
|`cmd_pu`|fn|pub|2445-2448|def cmd_pu(extra)|
|`cmd_rf`|fn|pub|2453-2456|def cmd_rf(extra)|
|`cmd_rmtg`|fn|pub|2461-2471|def cmd_rmtg(extra)|
|`cmd_rmloc`|fn|pub|2476-2479|def cmd_rmloc(extra)|
|`cmd_rmstg`|fn|pub|2484-2487|def cmd_rmstg(extra)|
|`cmd_rmunt`|fn|pub|2492-2495|def cmd_rmunt(extra)|
|`cmd_rs`|fn|pub|2500-2503|def cmd_rs(extra)|
|`cmd_rssft`|fn|pub|2508-2511|def cmd_rssft(extra)|
|`cmd_rsmix`|fn|pub|2516-2519|def cmd_rsmix(extra)|
|`cmd_rshrd`|fn|pub|2524-2527|def cmd_rshrd(extra)|
|`cmd_rsmrg`|fn|pub|2532-2535|def cmd_rsmrg(extra)|
|`cmd_rskep`|fn|pub|2540-2543|def cmd_rskep(extra)|
|`cmd_st`|fn|pub|2548-2551|def cmd_st(extra)|
|`cmd_tg`|fn|pub|2556-2559|def cmd_tg(extra)|
|`cmd_unstg`|fn|pub|2564-2567|def cmd_unstg(extra)|
|`cmd_ver`|fn|pub|2572-2598|def cmd_ver(extra)|
|`cmd_chver`|fn|pub|2603-2675|def cmd_chver(extra)|
|`cmd_major`|fn|pub|2683-2687|def cmd_major(extra)|
|`cmd_minor`|fn|pub|2695-2699|def cmd_minor(extra)|
|`cmd_patch`|fn|pub|2707-2711|def cmd_patch(extra)|
|`cmd_changelog`|fn|pub|2721-2753|def cmd_changelog(extra)|
|`COMMANDS`|var|pub|2756||
|`print_command_help`|fn|pub|2828-2834|def print_command_help(name, width=None)|
|`print_all_help`|fn|pub|2838-2872|def print_all_help()|
|`main`|fn|pub|2878-2928|def main(argv=None, *, check_updates: bool = True)|

