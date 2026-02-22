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

# core.py | Python | 3000L | 180 symbols | 16 imports | 788 comments
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
- var `RESET_HELP_COMMANDS = {"rs", "rshrd", "rskep", "rsmix", "rsmrg", "rssft"}` (L530)
- Brief: Constant `RESET_HELP_COMMANDS` used by CLI runtime paths and policies.
### fn `def _to_args(extra)` `priv` (L537-540)
- Return: Result emitted by `_to_args` according to command contract.

### class `class CommandExecutionError(RuntimeError)` : RuntimeError (L542-583)
- Brief: Class `CommandExecutionError` models a typed runtime container/error boundary. Execute `__init__` runtime logic for Git-Alias CLI. Execute `_format_message` runtime logic for Git-Alias CLI. Execute `_decode_stream` runtime logic for Git-Alias CLI.
- Param: self Input parameter consumed by `__init__`. exc Input parameter consumed by `__init__`. self Input parameter consumed by `_format_message`. data Input parameter consumed by `_decode_stream`.
- Return: Result emitted by `__init__` according to command contract. Result emitted by `_format_message` according to command contract. Result emitted by `_decode_stream` according to command contract.
- fn `def __init__(self, exc: subprocess.CalledProcessError)` `priv` (L547-554)
  - Return: Result emitted by `__init__` according to command contract.
- fn `def _format_message(self) -> str` `priv` (L558-568)
  - Return: Result emitted by `_format_message` according to command contract.
- fn `def _decode_stream(data) -> str` `priv` (L573-583)
  - Return: Result emitted by `_decode_stream` according to command contract.

### fn `def _run_checked(*popenargs, **kwargs)` `priv` (L589-596)
- Return: Result emitted by `_run_checked` according to command contract.

### class `class VersionDetectionError(RuntimeError)` : RuntimeError (L598-601)
- Brief: Class `VersionDetectionError` models a typed runtime container/error boundary.

### class `class ReleaseError(RuntimeError)` : RuntimeError (L603-606)
- Brief: Class `ReleaseError` models a typed runtime container/error boundary.

### fn `def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)` (L614-618)
- Return: Result emitted by `run_git_cmd` according to command contract.

### fn `def capture_git_output(base_args, cwd=None)` (L624-628)
- Return: Result emitted by `capture_git_output` according to command contract.

### fn `def run_command(cmd, cwd=None)` (L634-637)
- Return: Result emitted by `run_command` according to command contract.

### fn `def run_git_text(args, cwd=None, check=True)` (L644-661)
- Return: Result emitted by `run_git_text` according to command contract.

### fn `def run_shell(command, cwd=None)` (L667-670)
- Return: Result emitted by `run_shell` according to command contract.

### fn `def _git_status_lines()` `priv` (L674-686)
- Return: Result emitted by `_git_status_lines` according to command contract.

### fn `def has_unstaged_changes(status_lines=None)` (L691-702)
- Return: Result emitted by `has_unstaged_changes` according to command contract.

### fn `def has_staged_changes(status_lines=None)` (L707-716)
- Return: Result emitted by `has_staged_changes` according to command contract.

- var `WIP_MESSAGE_RE = re.compile(r"^wip: work in progress\.$")` (L722)
- Brief: Constant `WIP_MESSAGE_RE` used by CLI runtime paths and policies.
### fn `def _refresh_remote_refs()` `priv` (L728-739)
- Return: Result emitted by `_refresh_remote_refs` according to command contract.

### fn `def _branch_remote_divergence(branch_key, remote="origin")` `priv` (L745-763)
- Return: Result emitted by `_branch_remote_divergence` according to command contract.

### fn `def has_remote_branch_updates(branch_key, remote="origin")` (L769-773)
- Return: Result emitted by `has_remote_branch_updates` according to command contract.

### fn `def has_remote_develop_updates()` (L777-780)
- Return: Result emitted by `has_remote_develop_updates` according to command contract.

### fn `def has_remote_master_updates()` (L784-787)
- Return: Result emitted by `has_remote_master_updates` according to command contract.

### fn `def _head_commit_message()` `priv` (L791-797)
- Return: Result emitted by `_head_commit_message` according to command contract.

### fn `def _head_commit_hash()` `priv` (L801-807)
- Return: Result emitted by `_head_commit_hash` according to command contract.

### fn `def _commit_exists_in_branch(commit_hash, branch_name)` `priv` (L813-825)
- Return: Result emitted by `_commit_exists_in_branch` according to command contract.

### fn `def _should_amend_existing_commit()` `priv` (L829-844)
- Return: Result emitted by `_should_amend_existing_commit` according to command contract.

### fn `def is_inside_git_repo()` (L848-855)
- Return: Result emitted by `is_inside_git_repo` according to command contract.

### class `class TagInfo` (L860-868)
- Brief: Store raw tag name including `v` prefix when present. Store ISO date string used for changelog section headers. Store object hash associated with the tag reference.
- Details: Encapsulates tag identity, tag date, and resolved Git object identifier for changelog assembly.

- var `DELIM = "\x1f"` (L871)
- Brief: Constant `DELIM` used by CLI runtime paths and policies.
- var `RECORD = "\x1e"` (L874)
- Brief: Constant `RECORD` used by CLI runtime paths and policies.
- var `SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")` (L890)
- Brief: Constant `SEMVER_RE` used by CLI runtime paths and policies.
- var `SECTION_EMOJI = {` (L893)
- Brief: Constant `SECTION_EMOJI` used by CLI runtime paths and policies.
### fn `def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[int, int, int]]` `priv` (L910-913)
- Return: Result emitted by `_tag_semver_tuple` according to command contract.

### fn `def _latest_supported_tag_name(tags: List[TagInfo]) -> Optional[str]` `priv` (L918-921)
- Return: Result emitted by `_latest_supported_tag_name` according to command contract.

### fn `def _is_minor_release_tag(tag_name: str) -> bool` `priv` (L929-936)
- Sa: tisfies REQ-018, REQ-040

### fn `def _latest_patch_tag_after(all_tags: List[TagInfo], last_minor: Optional[TagInfo]) -> Optional[TagInfo]` `priv` (L945-954)
- Sa: tisfies REQ-040

### fn `def list_tags_sorted_by_date(repo_root: Path, merged_ref: Optional[str] = None) -> List[TagInfo]` (L960-980)
- Return: Result emitted by `list_tags_sorted_by_date` according to command contract.

### fn `def git_log_subjects(repo_root: Path, rev_range: str) -> List[str]` (L986-997)
- Return: Result emitted by `git_log_subjects` according to command contract.

### fn `def categorize_commit(subject: str) -> Tuple[Optional[str], str]` (L1003-1027)
- Return: Tuple `(section, line)`: `section` is the changelog section name or `None` if type is unmapped or ignored; `line` is the formatted entry string or `""` when section is `None`.

### fn `def _extract_release_version(subject: str) -> Optional[str]` `priv` (L1032-1042)
- Return: Result emitted by `_extract_release_version` according to command contract.

### fn `def _is_release_marker_commit(subject: str) -> bool` `priv` (L1047-1050)
- Return: Result emitted by `_is_release_marker_commit` according to command contract.

### fn `def generate_section_for_range(repo_root: Path, title: str, date_s: str, rev_range: str, expected_version: Optional[str] = None) -> Optional[str]` (L1059-1097)
- Return: Result emitted by `generate_section_for_range` according to command contract.

### fn `def _get_remote_name_for_branch(branch_name: str, repo_root: Path) -> str` `priv` (L1106-1114)
- Sa: tisfies REQ-046

### fn `def _extract_owner_repo(remote_url: str) -> Optional[Tuple[str, str]]` `priv` (L1121-1145)
- Return: Tuple `(owner, repo)` when parsing succeeds; otherwise `None`.

### fn `def _canonical_origin_base(repo_root: Path) -> Optional[str]` `priv` (L1155-1168)
- Sa: tisfies REQ-043, REQ-046

### fn `def get_origin_compare_url(base_url: Optional[str], prev_tag: Optional[str], tag: str) -> Optional[str]` (L1175-1182)
- Return: Result emitted by `get_origin_compare_url` according to command contract.

### fn `def get_release_page_url(base_url: Optional[str], tag: str) -> Optional[str]` (L1188-1193)
- Return: Result emitted by `get_release_page_url` according to command contract.

### fn `def build_history_section(` (L1201-1205)
- Return: Result emitted by `build_history_section` according to command contract.

### fn `def generate_changelog_document(repo_root: Path, include_patch: bool, disable_history: bool = False) -> str` (L1249-1310)
- Sa: tisfies REQ-018, REQ-040, REQ-041, REQ-043, REQ-068, REQ-069, REQ-070

### class `class VersionRuleContext` `@dataclass(frozen=True)` (L1321-1328)
- Note: Complexity: O(1) storage per field; aggregate complexity scales with matched file count per rule.

### fn `def _normalize_version_rule_pattern(pattern: str) -> str` `priv` (L1334-1345)
- Return: Normalized pathspec-compatible pattern string; empty string when input is blank.

### fn `def _build_version_file_inventory(root: Path) -> List[Tuple[Path, str]]` `priv` (L1351-1372)
- Return: List of tuples `(absolute_path, normalized_relative_path)` used by downstream matchers.

### fn `def _collect_version_files(root, pattern, *, inventory=None)` `priv` (L1380-1397)
- Details: Apply pathspec matcher to preserve configured GitIgnore-like semantics.
- Return: Result emitted by `_collect_version_files` according to command contract.

### fn `def _is_version_path_excluded(relative_path: str) -> bool` `priv` (L1402-1405)
- Return: Result emitted by `_is_version_path_excluded` according to command contract.

### fn `def _iter_versions_in_text(text, compiled_regexes)` `priv` (L1411-1422)
- Return: Result emitted by `_iter_versions_in_text` according to command contract.

### fn `def _read_version_file_text(file_path: Path, text_cache: Optional[Dict[Path, str]] = None) -> Optional[str]` `priv` (L1429-1443)
- Return: File text payload or `None` when file cannot be read.

### fn `def _prepare_version_rule_contexts(` `priv` (L1452-1453)
- Throws: VersionDetectionError when a rule matches no files or contains an invalid regex.

### fn `def _determine_canonical_version(` `priv` (L1495-1502)
- Return: Result emitted by `_determine_canonical_version` according to command contract.

### fn `def _parse_semver_tuple(text: str) -> Optional[Tuple[int, int, int]]` `priv` (L1547-1553)
- Return: Result emitted by `_parse_semver_tuple` according to command contract.

### fn `def _replace_versions_in_text(text, compiled_regex, replacement)` `priv` (L1560-1575)
- Return: Result emitted by `_replace_versions_in_text` according to command contract.

### fn `def _current_branch_name()` `priv` (L1579-1591)
- Return: Result emitted by `_current_branch_name` according to command contract.

### fn `def _ref_exists(ref_name)` `priv` (L1596-1605)
- Return: Result emitted by `_ref_exists` according to command contract.

### fn `def _local_branch_exists(branch_name)` `priv` (L1610-1613)
- Return: Result emitted by `_local_branch_exists` according to command contract.

### fn `def _remote_branch_exists(branch_name)` `priv` (L1618-1621)
- Return: Result emitted by `_remote_branch_exists` according to command contract.

### fn `def _ensure_release_prerequisites()` `priv` (L1625-1652)
- Return: Result emitted by `_ensure_release_prerequisites` according to command contract.

### fn `def _bump_semver_version(current_version, level)` `priv` (L1658-1676)
- Return: Result emitted by `_bump_semver_version` according to command contract.

### fn `def _run_release_step(level, step_name, action)` `priv` (L1683-1703)
- Return: Result emitted by `_run_release_step` according to command contract.

### fn `def _create_release_commit_for_flow(target_version)` `priv` (L1708-1713)
- Return: Result emitted by `_create_release_commit_for_flow` according to command contract.

### fn `def _push_branch_with_tags(branch_name)` `priv` (L1719-1723)
- Return: Result emitted by `run_git_cmd` according to command contract.

### fn `def _execute_release_flow(level, changelog_args=None)` `priv` (L1739-1786)
- Sa: tisfies REQ-026, REQ-045

### fn `def _execute_backup_flow()` `priv` (L1794-1809)
- Sa: tisfies REQ-047, REQ-048, REQ-049

### fn `def _run_release_command(level, changelog_args=None)` `priv` (L1815-1830)
- Return: Result emitted by `_run_release_command` according to command contract.

### fn `def _run_backup_command()` `priv` (L1835-1842)
- Sa: tisfies REQ-047, REQ-048, REQ-049

### fn `def _run_reset_with_help(base_args, extra)` `priv` (L1848-1855)
- Return: Result emitted by `_run_reset_with_help` according to command contract.

### fn `def _reject_extra_arguments(extra, alias)` `priv` (L1861-1867)
- Return: Result emitted by `_reject_extra_arguments` according to command contract.

### fn `def _parse_release_flags(extra, alias)` `priv` (L1873-1891)
- Return: Result emitted by `_parse_release_flags` according to command contract.

### fn `def _prepare_commit_message(extra, alias)` `priv` (L1897-1907)
- Return: Result emitted by `_prepare_commit_message` according to command contract.

### fn `def _build_conventional_message(kind: str, extra, alias: str) -> str` `priv` (L1914-1928)
- Return: Result emitted by `_build_conventional_message` according to command contract.

### fn `def _run_conventional_commit(kind: str, alias: str, extra)` `priv` (L1935-1940)
- Return: Result emitted by `_run_conventional_commit` according to command contract.

### fn `def _execute_commit(message, alias, allow_amend=True)` `priv` (L1947-1976)
- Return: Result emitted by `_execute_commit` according to command contract.

### fn `def upgrade_self()` (L1980-1993)
- Return: Result emitted by `upgrade_self` according to command contract.

### fn `def remove_self()` (L1997-2000)
- Return: Result emitted by `remove_self` according to command contract.

### fn `def cmd_aa(extra)` (L2005-2012)
- Return: Result emitted by `cmd_aa` according to command contract.

### fn `def cmd_ra(extra)` (L2017-2040)
- Return: Result emitted by `cmd_ra` according to command contract.

### fn `def cmd_ar(extra)` (L2045-2059)
- Return: Result emitted by `cmd_ar` according to command contract.

### fn `def cmd_br(extra)` (L2064-2067)
- Return: Result emitted by `cmd_br` according to command contract.

### fn `def cmd_bd(extra)` (L2072-2075)
- Return: Result emitted by `cmd_bd` according to command contract.

### fn `def cmd_ck(extra)` (L2080-2083)
- Return: Result emitted by `cmd_ck` according to command contract.

### fn `def _ensure_commit_ready(alias)` `priv` (L2088-2101)
- Return: Result emitted by `_ensure_commit_ready` according to command contract.

### fn `def cmd_cm(extra)` (L2106-2111)
- Return: Result emitted by `cmd_cm` according to command contract.

### fn `def cmd_wip(extra)` (L2116-2128)
- Return: Result emitted by `cmd_wip` according to command contract.

### fn `def cmd_release(extra)` (L2133-2155)
- Return: Result emitted by `cmd_release` according to command contract.

### fn `def cmd_new(extra)` (L2160-2163)
- Return: Result emitted by `cmd_new` according to command contract.

### fn `def cmd_refactor(extra)` (L2168-2171)
- Return: Result emitted by `cmd_refactor` according to command contract.

### fn `def cmd_fix(extra)` (L2176-2179)
- Return: Result emitted by `cmd_fix` according to command contract.

### fn `def cmd_change(extra)` (L2184-2187)
- Return: Result emitted by `cmd_change` according to command contract.

### fn `def cmd_implement(extra)` (L2192-2195)
- Return: Result emitted by `cmd_implement` according to command contract.

### fn `def cmd_docs(extra)` (L2200-2203)
- Return: Result emitted by `cmd_docs` according to command contract.

### fn `def cmd_style(extra)` (L2208-2211)
- Return: Result emitted by `cmd_style` according to command contract.

### fn `def cmd_revert(extra)` (L2216-2219)
- Return: Result emitted by `cmd_revert` according to command contract.

### fn `def cmd_misc(extra)` (L2224-2227)
- Return: Result emitted by `cmd_misc` according to command contract.

### fn `def cmd_cover(extra)` (L2232-2235)
- Return: Result emitted by `cmd_cover` according to command contract.

### fn `def cmd_co(extra)` (L2240-2243)
- Return: Result emitted by `cmd_co` according to command contract.

### fn `def cmd_d(extra)` (L2248-2255)
- Return: Result emitted by `cmd_d` according to command contract.

### fn `def cmd_dcc(extra)` (L2260-2263)
- Return: Result emitted by `cmd_dcc` according to command contract.

### fn `def cmd_dccc(extra)` (L2268-2271)
- Return: Result emitted by `cmd_dccc` according to command contract.

### fn `def cmd_de(extra)` (L2276-2279)
- Return: Result emitted by `cmd_de` according to command contract.

### fn `def cmd_di(extra)` (L2284-2287)
- Return: Result emitted by `cmd_di` according to command contract.

### fn `def cmd_diyou(extra)` (L2292-2295)
- Return: Result emitted by `cmd_diyou` according to command contract.

### fn `def cmd_dime(extra)` (L2300-2303)
- Return: Result emitted by `cmd_dime` according to command contract.

### fn `def cmd_dwc(extra)` (L2308-2311)
- Return: Result emitted by `cmd_dwc` according to command contract.

### fn `def cmd_dwcc(extra)` (L2316-2319)
- Return: Result emitted by `cmd_dwcc` according to command contract.

### fn `def cmd_ed(extra)` (L2324-2333)
- Return: Result emitted by `cmd_ed` according to command contract.

### fn `def cmd_fe(extra)` (L2338-2341)
- Return: Result emitted by `cmd_fe` according to command contract.

### fn `def cmd_feall(extra)` (L2346-2349)
- Return: Result emitted by `cmd_feall` according to command contract.

### fn `def cmd_gp(extra)` (L2354-2357)
- Return: Result emitted by `cmd_gp` according to command contract.

### fn `def cmd_gr(extra)` (L2362-2365)
- Return: Result emitted by `cmd_gr` according to command contract.

### fn `def cmd_str(extra)` (L2370-2399)
- Details: Query git remotes with transport metadata. Deduplicate remote names from `git remote -v` rows. Print normalized remote name inventory. Print detailed status for each unique remote.
- Return: Result emitted by `cmd_str` according to command contract.

### fn `def cmd_lb(extra)` (L2404-2407)
- Return: Result emitted by `cmd_lb` according to command contract.

### fn `def cmd_lg(extra)` (L2412-2425)
- Return: Result emitted by `cmd_lg` according to command contract.

### fn `def cmd_lh(extra)` (L2430-2433)
- Return: Result emitted by `cmd_lh` according to command contract.

### fn `def cmd_ll(extra)` (L2438-2450)
- Return: Result emitted by `cmd_ll` according to command contract.

### fn `def cmd_lm(extra)` (L2455-2458)
- Return: Result emitted by `cmd_lm` according to command contract.

### fn `def cmd_lt(extra)` (L2463-2466)
- Return: Result emitted by `cmd_lt` according to command contract.

### fn `def cmd_me(extra)` (L2471-2474)
- Return: Result emitted by `cmd_me` according to command contract.

### fn `def cmd_pl(extra)` (L2479-2482)
- Return: Result emitted by `cmd_pl` according to command contract.

### fn `def cmd_pt(extra)` (L2487-2490)
- Return: Result emitted by `cmd_pt` according to command contract.

### fn `def cmd_pu(extra)` (L2495-2498)
- Return: Result emitted by `cmd_pu` according to command contract.

### fn `def cmd_rf(extra)` (L2503-2506)
- Return: Result emitted by `cmd_rf` according to command contract.

### fn `def cmd_rmtg(extra)` (L2511-2521)
- Return: Result emitted by `cmd_rmtg` according to command contract.

### fn `def cmd_rmloc(extra)` (L2526-2529)
- Return: Result emitted by `cmd_rmloc` according to command contract.

### fn `def cmd_rmstg(extra)` (L2534-2537)
- Return: Result emitted by `cmd_rmstg` according to command contract.

### fn `def cmd_rmunt(extra)` (L2542-2545)
- Return: Result emitted by `cmd_rmunt` according to command contract.

### fn `def cmd_rs(extra)` (L2550-2553)
- Return: Result emitted by `cmd_rs` according to command contract.

### fn `def cmd_rssft(extra)` (L2558-2561)
- Return: Result emitted by `cmd_rssft` according to command contract.

### fn `def cmd_rsmix(extra)` (L2566-2569)
- Return: Result emitted by `cmd_rsmix` according to command contract.

### fn `def cmd_rshrd(extra)` (L2574-2577)
- Return: Result emitted by `cmd_rshrd` according to command contract.

### fn `def cmd_rsmrg(extra)` (L2582-2585)
- Return: Result emitted by `cmd_rsmrg` according to command contract.

### fn `def cmd_rskep(extra)` (L2590-2593)
- Return: Result emitted by `cmd_rskep` according to command contract.

### fn `def cmd_st(extra)` (L2598-2601)
- Return: Result emitted by `cmd_st` according to command contract.

### fn `def cmd_tg(extra)` (L2606-2609)
- Return: Result emitted by `cmd_tg` according to command contract.

### fn `def cmd_unstg(extra)` (L2614-2617)
- Return: Result emitted by `cmd_unstg` according to command contract.

### fn `def cmd_ver(extra)` (L2622-2648)
- Return: Result emitted by `cmd_ver` according to command contract.

### fn `def cmd_chver(extra)` (L2653-2725)
- Return: Result emitted by `cmd_chver` according to command contract.

### fn `def cmd_major(extra)` (L2734-2738)
- Sa: tisfies REQ-026, REQ-045

### fn `def cmd_minor(extra)` (L2747-2751)
- Sa: tisfies REQ-026, REQ-045

### fn `def cmd_patch(extra)` (L2760-2764)
- Sa: tisfies REQ-026, REQ-045

### fn `def cmd_backup(extra)` (L2772-2782)
- Sa: tisfies REQ-047, REQ-048, REQ-049

### fn `def cmd_changelog(extra)` (L2792-2824)
- Sa: tisfies REQ-018, REQ-040, REQ-041, REQ-043

- var `COMMANDS = {` (L2827)
- Brief: Constant `COMMANDS` used by CLI runtime paths and policies.
### fn `def print_command_help(name, width=None)` (L2900-2906)
- Return: Result emitted by `print_command_help` according to command contract.

### fn `def print_all_help()` (L2910-2944)
- Return: Result emitted by `print_all_help` according to command contract.

### fn `def main(argv=None, *, check_updates: bool = True)` (L2950-3000)
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
|`RESET_HELP_COMMANDS`|var|pub|530||
|`_to_args`|fn|priv|537-540|def _to_args(extra)|
|`CommandExecutionError`|class|pub|542-583|class CommandExecutionError(RuntimeError)|
|`CommandExecutionError.__init__`|fn|priv|547-554|def __init__(self, exc: subprocess.CalledProcessError)|
|`CommandExecutionError._format_message`|fn|priv|558-568|def _format_message(self) -> str|
|`CommandExecutionError._decode_stream`|fn|priv|573-583|def _decode_stream(data) -> str|
|`_run_checked`|fn|priv|589-596|def _run_checked(*popenargs, **kwargs)|
|`VersionDetectionError`|class|pub|598-601|class VersionDetectionError(RuntimeError)|
|`ReleaseError`|class|pub|603-606|class ReleaseError(RuntimeError)|
|`run_git_cmd`|fn|pub|614-618|def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)|
|`capture_git_output`|fn|pub|624-628|def capture_git_output(base_args, cwd=None)|
|`run_command`|fn|pub|634-637|def run_command(cmd, cwd=None)|
|`run_git_text`|fn|pub|644-661|def run_git_text(args, cwd=None, check=True)|
|`run_shell`|fn|pub|667-670|def run_shell(command, cwd=None)|
|`_git_status_lines`|fn|priv|674-686|def _git_status_lines()|
|`has_unstaged_changes`|fn|pub|691-702|def has_unstaged_changes(status_lines=None)|
|`has_staged_changes`|fn|pub|707-716|def has_staged_changes(status_lines=None)|
|`WIP_MESSAGE_RE`|var|pub|722||
|`_refresh_remote_refs`|fn|priv|728-739|def _refresh_remote_refs()|
|`_branch_remote_divergence`|fn|priv|745-763|def _branch_remote_divergence(branch_key, remote="origin")|
|`has_remote_branch_updates`|fn|pub|769-773|def has_remote_branch_updates(branch_key, remote="origin")|
|`has_remote_develop_updates`|fn|pub|777-780|def has_remote_develop_updates()|
|`has_remote_master_updates`|fn|pub|784-787|def has_remote_master_updates()|
|`_head_commit_message`|fn|priv|791-797|def _head_commit_message()|
|`_head_commit_hash`|fn|priv|801-807|def _head_commit_hash()|
|`_commit_exists_in_branch`|fn|priv|813-825|def _commit_exists_in_branch(commit_hash, branch_name)|
|`_should_amend_existing_commit`|fn|priv|829-844|def _should_amend_existing_commit()|
|`is_inside_git_repo`|fn|pub|848-855|def is_inside_git_repo()|
|`TagInfo`|class|pub|860-868|class TagInfo|
|`DELIM`|var|pub|871||
|`RECORD`|var|pub|874||
|`SEMVER_RE`|var|pub|890||
|`SECTION_EMOJI`|var|pub|893||
|`_tag_semver_tuple`|fn|priv|910-913|def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[in...|
|`_latest_supported_tag_name`|fn|priv|918-921|def _latest_supported_tag_name(tags: List[TagInfo]) -> Op...|
|`_is_minor_release_tag`|fn|priv|929-936|def _is_minor_release_tag(tag_name: str) -> bool|
|`_latest_patch_tag_after`|fn|priv|945-954|def _latest_patch_tag_after(all_tags: List[TagInfo], last...|
|`list_tags_sorted_by_date`|fn|pub|960-980|def list_tags_sorted_by_date(repo_root: Path, merged_ref:...|
|`git_log_subjects`|fn|pub|986-997|def git_log_subjects(repo_root: Path, rev_range: str) -> ...|
|`categorize_commit`|fn|pub|1003-1027|def categorize_commit(subject: str) -> Tuple[Optional[str...|
|`_extract_release_version`|fn|priv|1032-1042|def _extract_release_version(subject: str) -> Optional[str]|
|`_is_release_marker_commit`|fn|priv|1047-1050|def _is_release_marker_commit(subject: str) -> bool|
|`generate_section_for_range`|fn|pub|1059-1097|def generate_section_for_range(repo_root: Path, title: st...|
|`_get_remote_name_for_branch`|fn|priv|1106-1114|def _get_remote_name_for_branch(branch_name: str, repo_ro...|
|`_extract_owner_repo`|fn|priv|1121-1145|def _extract_owner_repo(remote_url: str) -> Optional[Tupl...|
|`_canonical_origin_base`|fn|priv|1155-1168|def _canonical_origin_base(repo_root: Path) -> Optional[str]|
|`get_origin_compare_url`|fn|pub|1175-1182|def get_origin_compare_url(base_url: Optional[str], prev_...|
|`get_release_page_url`|fn|pub|1188-1193|def get_release_page_url(base_url: Optional[str], tag: st...|
|`build_history_section`|fn|pub|1201-1205|def build_history_section(|
|`generate_changelog_document`|fn|pub|1249-1310|def generate_changelog_document(repo_root: Path, include_...|
|`VersionRuleContext`|class|pub|1321-1328|class VersionRuleContext|
|`_normalize_version_rule_pattern`|fn|priv|1334-1345|def _normalize_version_rule_pattern(pattern: str) -> str|
|`_build_version_file_inventory`|fn|priv|1351-1372|def _build_version_file_inventory(root: Path) -> List[Tup...|
|`_collect_version_files`|fn|priv|1380-1397|def _collect_version_files(root, pattern, *, inventory=None)|
|`_is_version_path_excluded`|fn|priv|1402-1405|def _is_version_path_excluded(relative_path: str) -> bool|
|`_iter_versions_in_text`|fn|priv|1411-1422|def _iter_versions_in_text(text, compiled_regexes)|
|`_read_version_file_text`|fn|priv|1429-1443|def _read_version_file_text(file_path: Path, text_cache: ...|
|`_prepare_version_rule_contexts`|fn|priv|1452-1453|def _prepare_version_rule_contexts(|
|`_determine_canonical_version`|fn|priv|1495-1502|def _determine_canonical_version(|
|`_parse_semver_tuple`|fn|priv|1547-1553|def _parse_semver_tuple(text: str) -> Optional[Tuple[int,...|
|`_replace_versions_in_text`|fn|priv|1560-1575|def _replace_versions_in_text(text, compiled_regex, repla...|
|`_current_branch_name`|fn|priv|1579-1591|def _current_branch_name()|
|`_ref_exists`|fn|priv|1596-1605|def _ref_exists(ref_name)|
|`_local_branch_exists`|fn|priv|1610-1613|def _local_branch_exists(branch_name)|
|`_remote_branch_exists`|fn|priv|1618-1621|def _remote_branch_exists(branch_name)|
|`_ensure_release_prerequisites`|fn|priv|1625-1652|def _ensure_release_prerequisites()|
|`_bump_semver_version`|fn|priv|1658-1676|def _bump_semver_version(current_version, level)|
|`_run_release_step`|fn|priv|1683-1703|def _run_release_step(level, step_name, action)|
|`_create_release_commit_for_flow`|fn|priv|1708-1713|def _create_release_commit_for_flow(target_version)|
|`_push_branch_with_tags`|fn|priv|1719-1723|def _push_branch_with_tags(branch_name)|
|`_execute_release_flow`|fn|priv|1739-1786|def _execute_release_flow(level, changelog_args=None)|
|`_execute_backup_flow`|fn|priv|1794-1809|def _execute_backup_flow()|
|`_run_release_command`|fn|priv|1815-1830|def _run_release_command(level, changelog_args=None)|
|`_run_backup_command`|fn|priv|1835-1842|def _run_backup_command()|
|`_run_reset_with_help`|fn|priv|1848-1855|def _run_reset_with_help(base_args, extra)|
|`_reject_extra_arguments`|fn|priv|1861-1867|def _reject_extra_arguments(extra, alias)|
|`_parse_release_flags`|fn|priv|1873-1891|def _parse_release_flags(extra, alias)|
|`_prepare_commit_message`|fn|priv|1897-1907|def _prepare_commit_message(extra, alias)|
|`_build_conventional_message`|fn|priv|1914-1928|def _build_conventional_message(kind: str, extra, alias: ...|
|`_run_conventional_commit`|fn|priv|1935-1940|def _run_conventional_commit(kind: str, alias: str, extra)|
|`_execute_commit`|fn|priv|1947-1976|def _execute_commit(message, alias, allow_amend=True)|
|`upgrade_self`|fn|pub|1980-1993|def upgrade_self()|
|`remove_self`|fn|pub|1997-2000|def remove_self()|
|`cmd_aa`|fn|pub|2005-2012|def cmd_aa(extra)|
|`cmd_ra`|fn|pub|2017-2040|def cmd_ra(extra)|
|`cmd_ar`|fn|pub|2045-2059|def cmd_ar(extra)|
|`cmd_br`|fn|pub|2064-2067|def cmd_br(extra)|
|`cmd_bd`|fn|pub|2072-2075|def cmd_bd(extra)|
|`cmd_ck`|fn|pub|2080-2083|def cmd_ck(extra)|
|`_ensure_commit_ready`|fn|priv|2088-2101|def _ensure_commit_ready(alias)|
|`cmd_cm`|fn|pub|2106-2111|def cmd_cm(extra)|
|`cmd_wip`|fn|pub|2116-2128|def cmd_wip(extra)|
|`cmd_release`|fn|pub|2133-2155|def cmd_release(extra)|
|`cmd_new`|fn|pub|2160-2163|def cmd_new(extra)|
|`cmd_refactor`|fn|pub|2168-2171|def cmd_refactor(extra)|
|`cmd_fix`|fn|pub|2176-2179|def cmd_fix(extra)|
|`cmd_change`|fn|pub|2184-2187|def cmd_change(extra)|
|`cmd_implement`|fn|pub|2192-2195|def cmd_implement(extra)|
|`cmd_docs`|fn|pub|2200-2203|def cmd_docs(extra)|
|`cmd_style`|fn|pub|2208-2211|def cmd_style(extra)|
|`cmd_revert`|fn|pub|2216-2219|def cmd_revert(extra)|
|`cmd_misc`|fn|pub|2224-2227|def cmd_misc(extra)|
|`cmd_cover`|fn|pub|2232-2235|def cmd_cover(extra)|
|`cmd_co`|fn|pub|2240-2243|def cmd_co(extra)|
|`cmd_d`|fn|pub|2248-2255|def cmd_d(extra)|
|`cmd_dcc`|fn|pub|2260-2263|def cmd_dcc(extra)|
|`cmd_dccc`|fn|pub|2268-2271|def cmd_dccc(extra)|
|`cmd_de`|fn|pub|2276-2279|def cmd_de(extra)|
|`cmd_di`|fn|pub|2284-2287|def cmd_di(extra)|
|`cmd_diyou`|fn|pub|2292-2295|def cmd_diyou(extra)|
|`cmd_dime`|fn|pub|2300-2303|def cmd_dime(extra)|
|`cmd_dwc`|fn|pub|2308-2311|def cmd_dwc(extra)|
|`cmd_dwcc`|fn|pub|2316-2319|def cmd_dwcc(extra)|
|`cmd_ed`|fn|pub|2324-2333|def cmd_ed(extra)|
|`cmd_fe`|fn|pub|2338-2341|def cmd_fe(extra)|
|`cmd_feall`|fn|pub|2346-2349|def cmd_feall(extra)|
|`cmd_gp`|fn|pub|2354-2357|def cmd_gp(extra)|
|`cmd_gr`|fn|pub|2362-2365|def cmd_gr(extra)|
|`cmd_str`|fn|pub|2370-2399|def cmd_str(extra)|
|`cmd_lb`|fn|pub|2404-2407|def cmd_lb(extra)|
|`cmd_lg`|fn|pub|2412-2425|def cmd_lg(extra)|
|`cmd_lh`|fn|pub|2430-2433|def cmd_lh(extra)|
|`cmd_ll`|fn|pub|2438-2450|def cmd_ll(extra)|
|`cmd_lm`|fn|pub|2455-2458|def cmd_lm(extra)|
|`cmd_lt`|fn|pub|2463-2466|def cmd_lt(extra)|
|`cmd_me`|fn|pub|2471-2474|def cmd_me(extra)|
|`cmd_pl`|fn|pub|2479-2482|def cmd_pl(extra)|
|`cmd_pt`|fn|pub|2487-2490|def cmd_pt(extra)|
|`cmd_pu`|fn|pub|2495-2498|def cmd_pu(extra)|
|`cmd_rf`|fn|pub|2503-2506|def cmd_rf(extra)|
|`cmd_rmtg`|fn|pub|2511-2521|def cmd_rmtg(extra)|
|`cmd_rmloc`|fn|pub|2526-2529|def cmd_rmloc(extra)|
|`cmd_rmstg`|fn|pub|2534-2537|def cmd_rmstg(extra)|
|`cmd_rmunt`|fn|pub|2542-2545|def cmd_rmunt(extra)|
|`cmd_rs`|fn|pub|2550-2553|def cmd_rs(extra)|
|`cmd_rssft`|fn|pub|2558-2561|def cmd_rssft(extra)|
|`cmd_rsmix`|fn|pub|2566-2569|def cmd_rsmix(extra)|
|`cmd_rshrd`|fn|pub|2574-2577|def cmd_rshrd(extra)|
|`cmd_rsmrg`|fn|pub|2582-2585|def cmd_rsmrg(extra)|
|`cmd_rskep`|fn|pub|2590-2593|def cmd_rskep(extra)|
|`cmd_st`|fn|pub|2598-2601|def cmd_st(extra)|
|`cmd_tg`|fn|pub|2606-2609|def cmd_tg(extra)|
|`cmd_unstg`|fn|pub|2614-2617|def cmd_unstg(extra)|
|`cmd_ver`|fn|pub|2622-2648|def cmd_ver(extra)|
|`cmd_chver`|fn|pub|2653-2725|def cmd_chver(extra)|
|`cmd_major`|fn|pub|2734-2738|def cmd_major(extra)|
|`cmd_minor`|fn|pub|2747-2751|def cmd_minor(extra)|
|`cmd_patch`|fn|pub|2760-2764|def cmd_patch(extra)|
|`cmd_backup`|fn|pub|2772-2782|def cmd_backup(extra)|
|`cmd_changelog`|fn|pub|2792-2824|def cmd_changelog(extra)|
|`COMMANDS`|var|pub|2827||
|`print_command_help`|fn|pub|2900-2906|def print_command_help(name, width=None)|
|`print_all_help`|fn|pub|2910-2944|def print_all_help()|
|`main`|fn|pub|2950-3000|def main(argv=None, *, check_updates: bool = True)|

