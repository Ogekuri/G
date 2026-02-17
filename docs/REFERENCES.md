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
> Path: `/home/ogekuri/G/src/git_alias/__init__.py`

## Imports
```
from .core import main  # noqa: F401
```


---

# __main__.py | Python | 11L | 0 symbols | 2 imports | 5 comments
> Path: `/home/ogekuri/G/src/git_alias/__main__.py`

## Imports
```
from .core import main
import sys
```


---

# core.py | Python | 2686L | 166 symbols | 16 imports | 655 comments
> Path: `/home/ogekuri/G/src/git_alias/core.py`

## Imports
```
import argparse
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import pathspec
```

## Definitions

- var `CONFIG_FILENAME = ".g.conf"` (L26)
- Brief: Constant `CONFIG_FILENAME` used by CLI runtime paths and policies.
- var `GITHUB_LATEST_RELEASE_API = "https://api.github.com/repos/Ogekuri/G/releases/latest"` (L30)
- Brief: Constant `GITHUB_LATEST_RELEASE_API` used by CLI runtime paths and policies.
- var `VERSION_CHECK_CACHE_FILE = Path(tempfile.gettempdir()) / ".g_version_check_cache.json"` (L33)
- Brief: Constant `VERSION_CHECK_CACHE_FILE` used by CLI runtime paths and policies.
- var `VERSION_CHECK_TTL_HOURS = 6` (L36)
- Brief: Constant `VERSION_CHECK_TTL_HOURS` used by CLI runtime paths and policies.
- var `DEFAULT_VER_RULES = [` (L40)
- Brief: Constant `DEFAULT_VER_RULES` used by CLI runtime paths and policies.
- var `VERSION_CLEANUP_REGEXES = [` (L47)
- Brief: Constant `VERSION_CLEANUP_REGEXES` used by CLI runtime paths and policies.
- var `VERSION_CLEANUP_PATTERNS = [re.compile(pattern) for pattern in VERSION_CLEANUP_REGEXES]` (L58)
- Brief: Constant `VERSION_CLEANUP_PATTERNS` used by CLI runtime paths and policies.
- var `DEFAULT_CONFIG = {` (L62)
- Brief: Constant `DEFAULT_CONFIG` used by CLI runtime paths and policies.
- var `CONFIG = DEFAULT_CONFIG.copy()` (L77)
- Brief: Constant `CONFIG` used by CLI runtime paths and policies.
- var `BRANCH_KEYS = ("master", "develop", "work")` (L80)
- Brief: Constant `BRANCH_KEYS` used by CLI runtime paths and policies.
- var `MANAGEMENT_HELP = [` (L83)
- Brief: Constant `MANAGEMENT_HELP` used by CLI runtime paths and policies.
### fn `def get_config_value(name)` (L97-100)
- Return: Result emitted by `get_config_value` according to command contract.

### fn `def get_branch(name)` (L105-110)
- Return: Result emitted by `get_branch` according to command contract.

### fn `def get_editor()` (L114-117)
- Return: Result emitted by `get_editor` according to command contract.

### fn `def _load_config_rules(key, fallback)` `priv` (L123-148)
- Return: Result emitted by `_load_config_rules` according to command contract.

### fn `def get_version_rules()` (L152-155)
- Return: Result emitted by `get_version_rules` according to command contract.

### fn `def get_cli_version()` (L159-170)
- Return: Result emitted by `get_cli_version` according to command contract.

### fn `def _normalize_semver_text(text: str) -> str` `priv` (L175-181)
- Return: Result emitted by `_normalize_semver_text` according to command contract.

### fn `def check_for_newer_version(timeout_seconds: float = 1.0) -> None` (L186-270)
- Details: Reuse non-expired cache payload before any online request. Emit upgrade warning when cached latest version is newer. Ignore cache read failures because version checks are non-blocking. Skip network request when cache entry is valid. Execute online release lookup when cache is absent or expired. Persist fresh release-check payload with TTL metadata. Ignore cache write failures because command execution must continue. Emit upgrade hint when fetched latest version is newer than current.
- Return: Result emitted by `check_for_newer_version` according to command contract.

### fn `def get_git_root()` (L274-289)
- Return: Result emitted by `get_git_root` according to command contract.

### fn `def get_config_path(root=None)` (L294-298)
- Return: Result emitted by `get_config_path` according to command contract.

### fn `def load_cli_config(root=None)` (L303-337)
- Return: Result emitted by `load_cli_config` according to command contract.

### fn `def write_default_config(root=None)` (L342-349)
- Return: Result emitted by `write_default_config` according to command contract.

### fn `def _editor_base_command()` `priv` (L353-367)
- Return: Result emitted by `_editor_base_command` according to command contract.

### fn `def run_editor_command(args)` (L372-374)
- Return: Result emitted by `run_editor_command` according to command contract.

- var `HELP_TEXTS = {` (L377)
- Brief: Constant `HELP_TEXTS` used by CLI runtime paths and policies.
- var `RESET_HELP_COMMANDS = {"rs", "rshrd", "rskep", "rsmix", "rsmrg", "rssft"}` (L525)
- Brief: Constant `RESET_HELP_COMMANDS` used by CLI runtime paths and policies.
### fn `def _to_args(extra)` `priv` (L532-535)
- Return: Result emitted by `_to_args` according to command contract.

### class `class CommandExecutionError(RuntimeError)` : RuntimeError (L537-578)
- Brief: Class `CommandExecutionError` models a typed runtime container/error boundary. Execute `__init__` runtime logic for Git-Alias CLI. Execute `_format_message` runtime logic for Git-Alias CLI. Execute `_decode_stream` runtime logic for Git-Alias CLI.
- Param: self Input parameter consumed by `__init__`. exc Input parameter consumed by `__init__`. self Input parameter consumed by `_format_message`. data Input parameter consumed by `_decode_stream`.
- Return: Result emitted by `__init__` according to command contract. Result emitted by `_format_message` according to command contract. Result emitted by `_decode_stream` according to command contract.
- fn `def __init__(self, exc: subprocess.CalledProcessError)` `priv` (L542-549)
  - Return: Result emitted by `__init__` according to command contract.
- fn `def _format_message(self) -> str` `priv` (L553-563)
  - Return: Result emitted by `_format_message` according to command contract.
- fn `def _decode_stream(data) -> str` `priv` (L568-578)
  - Return: Result emitted by `_decode_stream` according to command contract.

### fn `def _run_checked(*popenargs, **kwargs)` `priv` (L584-591)
- Return: Result emitted by `_run_checked` according to command contract.

### class `class VersionDetectionError(RuntimeError)` : RuntimeError (L593-596)
- Brief: Class `VersionDetectionError` models a typed runtime container/error boundary.

### class `class ReleaseError(RuntimeError)` : RuntimeError (L598-601)
- Brief: Class `ReleaseError` models a typed runtime container/error boundary.

### fn `def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)` (L609-613)
- Return: Result emitted by `run_git_cmd` according to command contract.

### fn `def capture_git_output(base_args, cwd=None)` (L619-623)
- Return: Result emitted by `capture_git_output` according to command contract.

### fn `def run_command(cmd, cwd=None)` (L629-632)
- Return: Result emitted by `run_command` according to command contract.

### fn `def run_git_text(args, cwd=None, check=True)` (L639-656)
- Return: Result emitted by `run_git_text` according to command contract.

### fn `def run_shell(command, cwd=None)` (L662-665)
- Return: Result emitted by `run_shell` according to command contract.

### fn `def run_git_text(args, cwd=None, check=True)` (L672-689)
- Return: Result emitted by `run_git_text` according to command contract.

### fn `def _git_status_lines()` `priv` (L693-705)
- Return: Result emitted by `_git_status_lines` according to command contract.

### fn `def has_unstaged_changes(status_lines=None)` (L710-721)
- Return: Result emitted by `has_unstaged_changes` according to command contract.

### fn `def has_staged_changes(status_lines=None)` (L726-735)
- Return: Result emitted by `has_staged_changes` according to command contract.

- var `WIP_MESSAGE_RE = re.compile(r"^wip: work in progress\.$")` (L741)
- Brief: Constant `WIP_MESSAGE_RE` used by CLI runtime paths and policies.
### fn `def _refresh_remote_refs()` `priv` (L747-758)
- Return: Result emitted by `_refresh_remote_refs` according to command contract.

### fn `def _branch_remote_divergence(branch_key, remote="origin")` `priv` (L764-782)
- Return: Result emitted by `_branch_remote_divergence` according to command contract.

### fn `def has_remote_branch_updates(branch_key, remote="origin")` (L788-792)
- Return: Result emitted by `has_remote_branch_updates` according to command contract.

### fn `def has_remote_develop_updates()` (L796-799)
- Return: Result emitted by `has_remote_develop_updates` according to command contract.

### fn `def has_remote_master_updates()` (L803-806)
- Return: Result emitted by `has_remote_master_updates` according to command contract.

### fn `def _head_commit_message()` `priv` (L810-816)
- Return: Result emitted by `_head_commit_message` according to command contract.

### fn `def _head_commit_hash()` `priv` (L820-826)
- Return: Result emitted by `_head_commit_hash` according to command contract.

### fn `def _commit_exists_in_branch(commit_hash, branch_name)` `priv` (L832-844)
- Return: Result emitted by `_commit_exists_in_branch` according to command contract.

### fn `def _should_amend_existing_commit()` `priv` (L848-863)
- Return: Result emitted by `_should_amend_existing_commit` according to command contract.

### fn `def is_inside_git_repo()` (L867-874)
- Return: Result emitted by `is_inside_git_repo` according to command contract.

### class `class TagInfo` (L879-887)
- Brief: Store raw tag name including `v` prefix when present. Store ISO date string used for changelog section headers. Store object hash associated with the tag reference.
- Details: Encapsulates tag identity, tag date, and resolved Git object identifier for changelog assembly.

- var `DELIM = "\x1f"` (L890)
- Brief: Constant `DELIM` used by CLI runtime paths and policies.
- var `RECORD = "\x1e"` (L893)
- Brief: Constant `RECORD` used by CLI runtime paths and policies.
- var `SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")` (L909)
- Brief: Constant `SEMVER_RE` used by CLI runtime paths and policies.
- var `SECTION_EMOJI = {` (L912)
- Brief: Constant `SECTION_EMOJI` used by CLI runtime paths and policies.
- var `MIN_SUPPORTED_HISTORY_VERSION = (0, 1, 0)` (L926)
- Brief: Constant `MIN_SUPPORTED_HISTORY_VERSION` used by CLI runtime paths and policies.
### fn `def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[int, int, int]]` `priv` (L933-936)
- Return: Result emitted by `_tag_semver_tuple` according to command contract.

### fn `def _is_supported_release_tag(tag_name: str) -> bool` `priv` (L941-947)
- Return: Result emitted by `_is_supported_release_tag` according to command contract.

### fn `def _should_include_tag(tag_name: str, include_draft: bool) -> bool` `priv` (L953-956)
- Return: Result emitted by `_should_include_tag` according to command contract.

### fn `def _latest_supported_tag_name(tags: List[TagInfo], include_draft: bool) -> Optional[str]` `priv` (L962-970)
- Return: Result emitted by `_latest_supported_tag_name` according to command contract.

### fn `def list_tags_sorted_by_date(repo_root: Path, merged_ref: Optional[str] = None) -> List[TagInfo]` (L976-996)
- Return: Result emitted by `list_tags_sorted_by_date` according to command contract.

### fn `def git_log_subjects(repo_root: Path, rev_range: str) -> List[str]` (L1002-1013)
- Return: Result emitted by `git_log_subjects` according to command contract.

### fn `def categorize_commit(subject: str) -> Tuple[Optional[str], str]` (L1018-1041)
- Return: Result emitted by `categorize_commit` according to command contract.

### fn `def _extract_release_version(subject: str) -> Optional[str]` `priv` (L1046-1052)
- Return: Result emitted by `_extract_release_version` according to command contract.

### fn `def generate_section_for_range(repo_root: Path, title: str, date_s: str, rev_range: str, expected_version: Optional[str] = None) -> Optional[str]` (L1061-1096)
- Return: Result emitted by `generate_section_for_range` according to command contract.

### fn `def _canonical_origin_base(repo_root: Path) -> Optional[str]` `priv` (L1101-1118)
- Return: Result emitted by `_canonical_origin_base` according to command contract.

### fn `def get_origin_compare_url(base_url: Optional[str], prev_tag: Optional[str], tag: str) -> Optional[str]` (L1125-1132)
- Return: Result emitted by `get_origin_compare_url` according to command contract.

### fn `def get_release_page_url(base_url: Optional[str], tag: str) -> Optional[str]` (L1138-1143)
- Return: Result emitted by `get_release_page_url` according to command contract.

### fn `def build_history_section(` (L1152-1157)
- Return: Result emitted by `build_history_section` according to command contract.

### fn `def generate_changelog_document(repo_root: Path, include_unreleased: bool, include_draft: bool = False) -> str` (L1192-1239)
- Return: Result emitted by `generate_changelog_document` according to command contract.

### fn `def _collect_version_files(root, pattern)` `priv` (L1245-1280)
- Details: Apply pathspec matcher to preserve configured GitIgnore-like semantics.
- Return: Result emitted by `_collect_version_files` according to command contract.

### fn `def _is_version_path_excluded(relative_path: str) -> bool` `priv` (L1285-1288)
- Return: Result emitted by `_is_version_path_excluded` according to command contract.

### fn `def _iter_versions_in_text(text, compiled_regexes)` `priv` (L1294-1305)
- Return: Result emitted by `_iter_versions_in_text` according to command contract.

### fn `def _determine_canonical_version(root: Path, rules, *, verbose: bool = False, debug: bool = False)` `priv` (L1313-1372)
- Return: Result emitted by `_determine_canonical_version` according to command contract.

### fn `def _parse_semver_tuple(text)` `priv` (L1377-1383)
- Return: Result emitted by `_parse_semver_tuple` according to command contract.

### fn `def _replace_versions_in_text(text, compiled_regex, replacement)` `priv` (L1390-1405)
- Return: Result emitted by `_replace_versions_in_text` according to command contract.

### fn `def _current_branch_name()` `priv` (L1409-1421)
- Return: Result emitted by `_current_branch_name` according to command contract.

### fn `def _ref_exists(ref_name)` `priv` (L1426-1435)
- Return: Result emitted by `_ref_exists` according to command contract.

### fn `def _local_branch_exists(branch_name)` `priv` (L1440-1443)
- Return: Result emitted by `_local_branch_exists` according to command contract.

### fn `def _remote_branch_exists(branch_name)` `priv` (L1448-1451)
- Return: Result emitted by `_remote_branch_exists` according to command contract.

### fn `def _ensure_release_prerequisites()` `priv` (L1455-1482)
- Return: Result emitted by `_ensure_release_prerequisites` according to command contract.

### fn `def _bump_semver_version(current_version, level)` `priv` (L1488-1506)
- Return: Result emitted by `_bump_semver_version` according to command contract.

### fn `def _run_release_step(level, step_name, action)` `priv` (L1513-1533)
- Return: Result emitted by `_run_release_step` according to command contract.

### fn `def _execute_release_flow(level, changelog_args=None)` `priv` (L1539-1581)
- Return: Result emitted by `_execute_release_flow` according to command contract.

### fn `def _run_release_command(level, changelog_args=None)` `priv` (L1587-1602)
- Return: Result emitted by `_run_release_command` according to command contract.

### fn `def _run_reset_with_help(base_args, extra)` `priv` (L1608-1615)
- Return: Result emitted by `_run_reset_with_help` according to command contract.

### fn `def _reject_extra_arguments(extra, alias)` `priv` (L1621-1627)
- Return: Result emitted by `_reject_extra_arguments` according to command contract.

### fn `def _parse_release_flags(extra, alias)` `priv` (L1633-1651)
- Return: Result emitted by `_parse_release_flags` according to command contract.

### fn `def _prepare_commit_message(extra, alias)` `priv` (L1657-1667)
- Return: Result emitted by `_prepare_commit_message` according to command contract.

### fn `def _build_conventional_message(kind: str, extra, alias: str) -> str` `priv` (L1674-1688)
- Return: Result emitted by `_build_conventional_message` according to command contract.

### fn `def _run_conventional_commit(kind: str, alias: str, extra)` `priv` (L1695-1700)
- Return: Result emitted by `_run_conventional_commit` according to command contract.

### fn `def _execute_commit(message, alias, allow_amend=True)` `priv` (L1707-1736)
- Return: Result emitted by `_execute_commit` according to command contract.

### fn `def upgrade_self()` (L1740-1753)
- Return: Result emitted by `upgrade_self` according to command contract.

### fn `def remove_self()` (L1757-1760)
- Return: Result emitted by `remove_self` according to command contract.

### fn `def cmd_aa(extra)` (L1765-1772)
- Return: Result emitted by `cmd_aa` according to command contract.

### fn `def cmd_ra(extra)` (L1777-1800)
- Return: Result emitted by `cmd_ra` according to command contract.

### fn `def cmd_ar(extra)` (L1805-1818)
- Return: Result emitted by `cmd_ar` according to command contract.

### fn `def cmd_br(extra)` (L1823-1826)
- Return: Result emitted by `cmd_br` according to command contract.

### fn `def cmd_bd(extra)` (L1831-1834)
- Return: Result emitted by `cmd_bd` according to command contract.

### fn `def cmd_ck(extra)` (L1839-1842)
- Return: Result emitted by `cmd_ck` according to command contract.

### fn `def _ensure_commit_ready(alias)` `priv` (L1847-1860)
- Return: Result emitted by `_ensure_commit_ready` according to command contract.

### fn `def cmd_cm(extra)` (L1865-1870)
- Return: Result emitted by `cmd_cm` according to command contract.

### fn `def cmd_wip(extra)` (L1875-1887)
- Return: Result emitted by `cmd_wip` according to command contract.

### fn `def cmd_release(extra)` (L1892-1914)
- Return: Result emitted by `cmd_release` according to command contract.

### fn `def cmd_new(extra)` (L1919-1922)
- Return: Result emitted by `cmd_new` according to command contract.

### fn `def cmd_refactor(extra)` (L1927-1930)
- Return: Result emitted by `cmd_refactor` according to command contract.

### fn `def cmd_fix(extra)` (L1935-1938)
- Return: Result emitted by `cmd_fix` according to command contract.

### fn `def cmd_change(extra)` (L1943-1946)
- Return: Result emitted by `cmd_change` according to command contract.

### fn `def cmd_docs(extra)` (L1951-1954)
- Return: Result emitted by `cmd_docs` according to command contract.

### fn `def cmd_style(extra)` (L1959-1962)
- Return: Result emitted by `cmd_style` according to command contract.

### fn `def cmd_revert(extra)` (L1967-1970)
- Return: Result emitted by `cmd_revert` according to command contract.

### fn `def cmd_misc(extra)` (L1975-1978)
- Return: Result emitted by `cmd_misc` according to command contract.

### fn `def cmd_cover(extra)` (L1983-1986)
- Return: Result emitted by `cmd_cover` according to command contract.

### fn `def cmd_co(extra)` (L1991-1994)
- Return: Result emitted by `cmd_co` according to command contract.

### fn `def cmd_d(extra)` (L1999-2006)
- Return: Result emitted by `cmd_d` according to command contract.

### fn `def cmd_dc(extra)` (L2011-2014)
- Return: Result emitted by `cmd_dc` according to command contract.

### fn `def cmd_de(extra)` (L2019-2022)
- Return: Result emitted by `cmd_de` according to command contract.

### fn `def cmd_di(extra)` (L2027-2030)
- Return: Result emitted by `cmd_di` according to command contract.

### fn `def cmd_diyou(extra)` (L2035-2038)
- Return: Result emitted by `cmd_diyou` according to command contract.

### fn `def cmd_dime(extra)` (L2043-2046)
- Return: Result emitted by `cmd_dime` according to command contract.

### fn `def cmd_dw(extra)` (L2051-2054)
- Return: Result emitted by `cmd_dw` according to command contract.

### fn `def cmd_ed(extra)` (L2059-2068)
- Return: Result emitted by `cmd_ed` according to command contract.

### fn `def cmd_fe(extra)` (L2073-2076)
- Return: Result emitted by `cmd_fe` according to command contract.

### fn `def cmd_feall(extra)` (L2081-2084)
- Return: Result emitted by `cmd_feall` according to command contract.

### fn `def cmd_gp(extra)` (L2089-2092)
- Return: Result emitted by `cmd_gp` according to command contract.

### fn `def cmd_gr(extra)` (L2097-2100)
- Return: Result emitted by `cmd_gr` according to command contract.

### fn `def cmd_str(extra)` (L2105-2134)
- Details: Query git remotes with transport metadata. Deduplicate remote names from `git remote -v` rows. Print normalized remote name inventory. Print detailed status for each unique remote.
- Return: Result emitted by `cmd_str` according to command contract.

### fn `def cmd_lb(extra)` (L2139-2142)
- Return: Result emitted by `cmd_lb` according to command contract.

### fn `def cmd_lg(extra)` (L2147-2160)
- Return: Result emitted by `cmd_lg` according to command contract.

### fn `def cmd_lh(extra)` (L2165-2168)
- Return: Result emitted by `cmd_lh` according to command contract.

### fn `def cmd_ll(extra)` (L2173-2185)
- Return: Result emitted by `cmd_ll` according to command contract.

### fn `def cmd_lm(extra)` (L2190-2193)
- Return: Result emitted by `cmd_lm` according to command contract.

### fn `def cmd_lt(extra)` (L2198-2201)
- Return: Result emitted by `cmd_lt` according to command contract.

### fn `def cmd_me(extra)` (L2206-2209)
- Return: Result emitted by `cmd_me` according to command contract.

### fn `def cmd_pl(extra)` (L2214-2217)
- Return: Result emitted by `cmd_pl` according to command contract.

### fn `def cmd_pt(extra)` (L2222-2225)
- Return: Result emitted by `cmd_pt` according to command contract.

### fn `def cmd_pu(extra)` (L2230-2233)
- Return: Result emitted by `cmd_pu` according to command contract.

### fn `def cmd_rf(extra)` (L2238-2241)
- Return: Result emitted by `cmd_rf` according to command contract.

### fn `def cmd_rmtg(extra)` (L2246-2256)
- Return: Result emitted by `cmd_rmtg` according to command contract.

### fn `def cmd_rmloc(extra)` (L2261-2264)
- Return: Result emitted by `cmd_rmloc` according to command contract.

### fn `def cmd_rmstg(extra)` (L2269-2272)
- Return: Result emitted by `cmd_rmstg` according to command contract.

### fn `def cmd_rmunt(extra)` (L2277-2280)
- Return: Result emitted by `cmd_rmunt` according to command contract.

### fn `def cmd_rs(extra)` (L2285-2288)
- Return: Result emitted by `cmd_rs` according to command contract.

### fn `def cmd_rssft(extra)` (L2293-2296)
- Return: Result emitted by `cmd_rssft` according to command contract.

### fn `def cmd_rsmix(extra)` (L2301-2304)
- Return: Result emitted by `cmd_rsmix` according to command contract.

### fn `def cmd_rshrd(extra)` (L2309-2312)
- Return: Result emitted by `cmd_rshrd` according to command contract.

### fn `def cmd_rsmrg(extra)` (L2317-2320)
- Return: Result emitted by `cmd_rsmrg` according to command contract.

### fn `def cmd_rskep(extra)` (L2325-2328)
- Return: Result emitted by `cmd_rskep` according to command contract.

### fn `def cmd_st(extra)` (L2333-2336)
- Return: Result emitted by `cmd_st` according to command contract.

### fn `def cmd_tg(extra)` (L2341-2344)
- Return: Result emitted by `cmd_tg` according to command contract.

### fn `def cmd_unstg(extra)` (L2349-2352)
- Return: Result emitted by `cmd_unstg` according to command contract.

### fn `def cmd_ver(extra)` (L2357-2375)
- Return: Result emitted by `cmd_ver` according to command contract.

### fn `def cmd_chver(extra)` (L2380-2450)
- Return: Result emitted by `cmd_chver` according to command contract.

### fn `def cmd_major(extra)` (L2455-2459)
- Return: Result emitted by `cmd_major` according to command contract.

### fn `def cmd_minor(extra)` (L2464-2468)
- Return: Result emitted by `cmd_minor` according to command contract.

### fn `def cmd_patch(extra)` (L2473-2477)
- Return: Result emitted by `cmd_patch` according to command contract.

### fn `def cmd_changelog(extra)` (L2482-2514)
- Return: Result emitted by `cmd_changelog` according to command contract.

- var `COMMANDS = {` (L2517)
- Brief: Constant `COMMANDS` used by CLI runtime paths and policies.
### fn `def print_command_help(name, width=None)` (L2586-2592)
- Return: Result emitted by `print_command_help` according to command contract.

### fn `def print_all_help()` (L2596-2630)
- Return: Result emitted by `print_all_help` according to command contract.

### fn `def main(argv=None, *, check_updates: bool = True)` (L2636-2686)
- Return: Result emitted by `main` according to command contract.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`CONFIG_FILENAME`|var|pub|26||
|`GITHUB_LATEST_RELEASE_API`|var|pub|30||
|`VERSION_CHECK_CACHE_FILE`|var|pub|33||
|`VERSION_CHECK_TTL_HOURS`|var|pub|36||
|`DEFAULT_VER_RULES`|var|pub|40||
|`VERSION_CLEANUP_REGEXES`|var|pub|47||
|`VERSION_CLEANUP_PATTERNS`|var|pub|58||
|`DEFAULT_CONFIG`|var|pub|62||
|`CONFIG`|var|pub|77||
|`BRANCH_KEYS`|var|pub|80||
|`MANAGEMENT_HELP`|var|pub|83||
|`get_config_value`|fn|pub|97-100|def get_config_value(name)|
|`get_branch`|fn|pub|105-110|def get_branch(name)|
|`get_editor`|fn|pub|114-117|def get_editor()|
|`_load_config_rules`|fn|priv|123-148|def _load_config_rules(key, fallback)|
|`get_version_rules`|fn|pub|152-155|def get_version_rules()|
|`get_cli_version`|fn|pub|159-170|def get_cli_version()|
|`_normalize_semver_text`|fn|priv|175-181|def _normalize_semver_text(text: str) -> str|
|`check_for_newer_version`|fn|pub|186-270|def check_for_newer_version(timeout_seconds: float = 1.0)...|
|`get_git_root`|fn|pub|274-289|def get_git_root()|
|`get_config_path`|fn|pub|294-298|def get_config_path(root=None)|
|`load_cli_config`|fn|pub|303-337|def load_cli_config(root=None)|
|`write_default_config`|fn|pub|342-349|def write_default_config(root=None)|
|`_editor_base_command`|fn|priv|353-367|def _editor_base_command()|
|`run_editor_command`|fn|pub|372-374|def run_editor_command(args)|
|`HELP_TEXTS`|var|pub|377||
|`RESET_HELP_COMMANDS`|var|pub|525||
|`_to_args`|fn|priv|532-535|def _to_args(extra)|
|`CommandExecutionError`|class|pub|537-578|class CommandExecutionError(RuntimeError)|
|`CommandExecutionError.__init__`|fn|priv|542-549|def __init__(self, exc: subprocess.CalledProcessError)|
|`CommandExecutionError._format_message`|fn|priv|553-563|def _format_message(self) -> str|
|`CommandExecutionError._decode_stream`|fn|priv|568-578|def _decode_stream(data) -> str|
|`_run_checked`|fn|priv|584-591|def _run_checked(*popenargs, **kwargs)|
|`VersionDetectionError`|class|pub|593-596|class VersionDetectionError(RuntimeError)|
|`ReleaseError`|class|pub|598-601|class ReleaseError(RuntimeError)|
|`run_git_cmd`|fn|pub|609-613|def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)|
|`capture_git_output`|fn|pub|619-623|def capture_git_output(base_args, cwd=None)|
|`run_command`|fn|pub|629-632|def run_command(cmd, cwd=None)|
|`run_git_text`|fn|pub|639-656|def run_git_text(args, cwd=None, check=True)|
|`run_shell`|fn|pub|662-665|def run_shell(command, cwd=None)|
|`run_git_text`|fn|pub|672-689|def run_git_text(args, cwd=None, check=True)|
|`_git_status_lines`|fn|priv|693-705|def _git_status_lines()|
|`has_unstaged_changes`|fn|pub|710-721|def has_unstaged_changes(status_lines=None)|
|`has_staged_changes`|fn|pub|726-735|def has_staged_changes(status_lines=None)|
|`WIP_MESSAGE_RE`|var|pub|741||
|`_refresh_remote_refs`|fn|priv|747-758|def _refresh_remote_refs()|
|`_branch_remote_divergence`|fn|priv|764-782|def _branch_remote_divergence(branch_key, remote="origin")|
|`has_remote_branch_updates`|fn|pub|788-792|def has_remote_branch_updates(branch_key, remote="origin")|
|`has_remote_develop_updates`|fn|pub|796-799|def has_remote_develop_updates()|
|`has_remote_master_updates`|fn|pub|803-806|def has_remote_master_updates()|
|`_head_commit_message`|fn|priv|810-816|def _head_commit_message()|
|`_head_commit_hash`|fn|priv|820-826|def _head_commit_hash()|
|`_commit_exists_in_branch`|fn|priv|832-844|def _commit_exists_in_branch(commit_hash, branch_name)|
|`_should_amend_existing_commit`|fn|priv|848-863|def _should_amend_existing_commit()|
|`is_inside_git_repo`|fn|pub|867-874|def is_inside_git_repo()|
|`TagInfo`|class|pub|879-887|class TagInfo|
|`DELIM`|var|pub|890||
|`RECORD`|var|pub|893||
|`SEMVER_RE`|var|pub|909||
|`SECTION_EMOJI`|var|pub|912||
|`MIN_SUPPORTED_HISTORY_VERSION`|var|pub|926||
|`_tag_semver_tuple`|fn|priv|933-936|def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[in...|
|`_is_supported_release_tag`|fn|priv|941-947|def _is_supported_release_tag(tag_name: str) -> bool|
|`_should_include_tag`|fn|priv|953-956|def _should_include_tag(tag_name: str, include_draft: boo...|
|`_latest_supported_tag_name`|fn|priv|962-970|def _latest_supported_tag_name(tags: List[TagInfo], inclu...|
|`list_tags_sorted_by_date`|fn|pub|976-996|def list_tags_sorted_by_date(repo_root: Path, merged_ref:...|
|`git_log_subjects`|fn|pub|1002-1013|def git_log_subjects(repo_root: Path, rev_range: str) -> ...|
|`categorize_commit`|fn|pub|1018-1041|def categorize_commit(subject: str) -> Tuple[Optional[str...|
|`_extract_release_version`|fn|priv|1046-1052|def _extract_release_version(subject: str) -> Optional[str]|
|`generate_section_for_range`|fn|pub|1061-1096|def generate_section_for_range(repo_root: Path, title: st...|
|`_canonical_origin_base`|fn|priv|1101-1118|def _canonical_origin_base(repo_root: Path) -> Optional[str]|
|`get_origin_compare_url`|fn|pub|1125-1132|def get_origin_compare_url(base_url: Optional[str], prev_...|
|`get_release_page_url`|fn|pub|1138-1143|def get_release_page_url(base_url: Optional[str], tag: st...|
|`build_history_section`|fn|pub|1152-1157|def build_history_section(|
|`generate_changelog_document`|fn|pub|1192-1239|def generate_changelog_document(repo_root: Path, include_...|
|`_collect_version_files`|fn|priv|1245-1280|def _collect_version_files(root, pattern)|
|`_is_version_path_excluded`|fn|priv|1285-1288|def _is_version_path_excluded(relative_path: str) -> bool|
|`_iter_versions_in_text`|fn|priv|1294-1305|def _iter_versions_in_text(text, compiled_regexes)|
|`_determine_canonical_version`|fn|priv|1313-1372|def _determine_canonical_version(root: Path, rules, *, ve...|
|`_parse_semver_tuple`|fn|priv|1377-1383|def _parse_semver_tuple(text)|
|`_replace_versions_in_text`|fn|priv|1390-1405|def _replace_versions_in_text(text, compiled_regex, repla...|
|`_current_branch_name`|fn|priv|1409-1421|def _current_branch_name()|
|`_ref_exists`|fn|priv|1426-1435|def _ref_exists(ref_name)|
|`_local_branch_exists`|fn|priv|1440-1443|def _local_branch_exists(branch_name)|
|`_remote_branch_exists`|fn|priv|1448-1451|def _remote_branch_exists(branch_name)|
|`_ensure_release_prerequisites`|fn|priv|1455-1482|def _ensure_release_prerequisites()|
|`_bump_semver_version`|fn|priv|1488-1506|def _bump_semver_version(current_version, level)|
|`_run_release_step`|fn|priv|1513-1533|def _run_release_step(level, step_name, action)|
|`_execute_release_flow`|fn|priv|1539-1581|def _execute_release_flow(level, changelog_args=None)|
|`_run_release_command`|fn|priv|1587-1602|def _run_release_command(level, changelog_args=None)|
|`_run_reset_with_help`|fn|priv|1608-1615|def _run_reset_with_help(base_args, extra)|
|`_reject_extra_arguments`|fn|priv|1621-1627|def _reject_extra_arguments(extra, alias)|
|`_parse_release_flags`|fn|priv|1633-1651|def _parse_release_flags(extra, alias)|
|`_prepare_commit_message`|fn|priv|1657-1667|def _prepare_commit_message(extra, alias)|
|`_build_conventional_message`|fn|priv|1674-1688|def _build_conventional_message(kind: str, extra, alias: ...|
|`_run_conventional_commit`|fn|priv|1695-1700|def _run_conventional_commit(kind: str, alias: str, extra)|
|`_execute_commit`|fn|priv|1707-1736|def _execute_commit(message, alias, allow_amend=True)|
|`upgrade_self`|fn|pub|1740-1753|def upgrade_self()|
|`remove_self`|fn|pub|1757-1760|def remove_self()|
|`cmd_aa`|fn|pub|1765-1772|def cmd_aa(extra)|
|`cmd_ra`|fn|pub|1777-1800|def cmd_ra(extra)|
|`cmd_ar`|fn|pub|1805-1818|def cmd_ar(extra)|
|`cmd_br`|fn|pub|1823-1826|def cmd_br(extra)|
|`cmd_bd`|fn|pub|1831-1834|def cmd_bd(extra)|
|`cmd_ck`|fn|pub|1839-1842|def cmd_ck(extra)|
|`_ensure_commit_ready`|fn|priv|1847-1860|def _ensure_commit_ready(alias)|
|`cmd_cm`|fn|pub|1865-1870|def cmd_cm(extra)|
|`cmd_wip`|fn|pub|1875-1887|def cmd_wip(extra)|
|`cmd_release`|fn|pub|1892-1914|def cmd_release(extra)|
|`cmd_new`|fn|pub|1919-1922|def cmd_new(extra)|
|`cmd_refactor`|fn|pub|1927-1930|def cmd_refactor(extra)|
|`cmd_fix`|fn|pub|1935-1938|def cmd_fix(extra)|
|`cmd_change`|fn|pub|1943-1946|def cmd_change(extra)|
|`cmd_docs`|fn|pub|1951-1954|def cmd_docs(extra)|
|`cmd_style`|fn|pub|1959-1962|def cmd_style(extra)|
|`cmd_revert`|fn|pub|1967-1970|def cmd_revert(extra)|
|`cmd_misc`|fn|pub|1975-1978|def cmd_misc(extra)|
|`cmd_cover`|fn|pub|1983-1986|def cmd_cover(extra)|
|`cmd_co`|fn|pub|1991-1994|def cmd_co(extra)|
|`cmd_d`|fn|pub|1999-2006|def cmd_d(extra)|
|`cmd_dc`|fn|pub|2011-2014|def cmd_dc(extra)|
|`cmd_de`|fn|pub|2019-2022|def cmd_de(extra)|
|`cmd_di`|fn|pub|2027-2030|def cmd_di(extra)|
|`cmd_diyou`|fn|pub|2035-2038|def cmd_diyou(extra)|
|`cmd_dime`|fn|pub|2043-2046|def cmd_dime(extra)|
|`cmd_dw`|fn|pub|2051-2054|def cmd_dw(extra)|
|`cmd_ed`|fn|pub|2059-2068|def cmd_ed(extra)|
|`cmd_fe`|fn|pub|2073-2076|def cmd_fe(extra)|
|`cmd_feall`|fn|pub|2081-2084|def cmd_feall(extra)|
|`cmd_gp`|fn|pub|2089-2092|def cmd_gp(extra)|
|`cmd_gr`|fn|pub|2097-2100|def cmd_gr(extra)|
|`cmd_str`|fn|pub|2105-2134|def cmd_str(extra)|
|`cmd_lb`|fn|pub|2139-2142|def cmd_lb(extra)|
|`cmd_lg`|fn|pub|2147-2160|def cmd_lg(extra)|
|`cmd_lh`|fn|pub|2165-2168|def cmd_lh(extra)|
|`cmd_ll`|fn|pub|2173-2185|def cmd_ll(extra)|
|`cmd_lm`|fn|pub|2190-2193|def cmd_lm(extra)|
|`cmd_lt`|fn|pub|2198-2201|def cmd_lt(extra)|
|`cmd_me`|fn|pub|2206-2209|def cmd_me(extra)|
|`cmd_pl`|fn|pub|2214-2217|def cmd_pl(extra)|
|`cmd_pt`|fn|pub|2222-2225|def cmd_pt(extra)|
|`cmd_pu`|fn|pub|2230-2233|def cmd_pu(extra)|
|`cmd_rf`|fn|pub|2238-2241|def cmd_rf(extra)|
|`cmd_rmtg`|fn|pub|2246-2256|def cmd_rmtg(extra)|
|`cmd_rmloc`|fn|pub|2261-2264|def cmd_rmloc(extra)|
|`cmd_rmstg`|fn|pub|2269-2272|def cmd_rmstg(extra)|
|`cmd_rmunt`|fn|pub|2277-2280|def cmd_rmunt(extra)|
|`cmd_rs`|fn|pub|2285-2288|def cmd_rs(extra)|
|`cmd_rssft`|fn|pub|2293-2296|def cmd_rssft(extra)|
|`cmd_rsmix`|fn|pub|2301-2304|def cmd_rsmix(extra)|
|`cmd_rshrd`|fn|pub|2309-2312|def cmd_rshrd(extra)|
|`cmd_rsmrg`|fn|pub|2317-2320|def cmd_rsmrg(extra)|
|`cmd_rskep`|fn|pub|2325-2328|def cmd_rskep(extra)|
|`cmd_st`|fn|pub|2333-2336|def cmd_st(extra)|
|`cmd_tg`|fn|pub|2341-2344|def cmd_tg(extra)|
|`cmd_unstg`|fn|pub|2349-2352|def cmd_unstg(extra)|
|`cmd_ver`|fn|pub|2357-2375|def cmd_ver(extra)|
|`cmd_chver`|fn|pub|2380-2450|def cmd_chver(extra)|
|`cmd_major`|fn|pub|2455-2459|def cmd_major(extra)|
|`cmd_minor`|fn|pub|2464-2468|def cmd_minor(extra)|
|`cmd_patch`|fn|pub|2473-2477|def cmd_patch(extra)|
|`cmd_changelog`|fn|pub|2482-2514|def cmd_changelog(extra)|
|`COMMANDS`|var|pub|2517||
|`print_command_help`|fn|pub|2586-2592|def print_command_help(name, width=None)|
|`print_all_help`|fn|pub|2596-2630|def print_all_help()|
|`main`|fn|pub|2636-2686|def main(argv=None, *, check_updates: bool = True)|

