# __init__.py | Python | 10L | 0 symbols | 1 imports | 4 comments
> Path: `/home/ogekuri/G/src/git_alias/__init__.py`
> @file __init__.py

## Imports
```
from .core import main  # noqa: F401
```

## Comments
- L2-4: @brief Package metadata and public entrypoint exports for git-alias CLI. | @brief Semantic version string exposed by package metadata.
- L9: @brief Public symbols exported by the package root module.


---

# __main__.py | Python | 8L | 0 symbols | 2 imports | 2 comments
> Path: `/home/ogekuri/G/src/git_alias/__main__.py`
> @file __main__.py

## Imports
```
from .core import main
import sys
```

## Comments
- L2: @brief Module-execution adapter for invoking CLI main entrypoint.


---

# core.py | Python | 2508L | 163 symbols | 16 imports | 499 comments
> Path: `/home/ogekuri/G/src/git_alias/core.py`
> @file core.py

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

- var `CONFIG_FILENAME = ".g.conf"` (L25) — @brief Constant `CONFIG_FILENAME` used by CLI runtime paths and policies.
- var `GITHUB_LATEST_RELEASE_API = "https://api.github.com/repos/Ogekuri/G/releases/latest"` (L29) — @brief Constant `GITHUB_LATEST_RELEASE_API` used by CLI runtime paths and policies.
- var `VERSION_CHECK_CACHE_FILE = Path(tempfile.gettempdir()) / ".g_version_check_cache.json"` (L32) — @brief Constant `VERSION_CHECK_CACHE_FILE` used by CLI runtime paths and policies.
- var `VERSION_CHECK_TTL_HOURS = 6` (L35) — @brief Constant `VERSION_CHECK_TTL_HOURS` used by CLI runtime paths and policies.
- var `DEFAULT_VER_RULES = [` (L39) — @brief Constant `DEFAULT_VER_RULES` used by CLI runtime paths and policies.
- var `VERSION_CLEANUP_REGEXES = [` (L46) — @brief Constant `VERSION_CLEANUP_REGEXES` used by CLI runtime paths and policies.
- var `VERSION_CLEANUP_PATTERNS = [re.compile(pattern) for pattern in VERSION_CLEANUP_REGEXES]` (L57) — @brief Constant `VERSION_CLEANUP_PATTERNS` used by CLI runtime paths and policies.
- var `DEFAULT_CONFIG = {` (L61) — @brief Constant `DEFAULT_CONFIG` used by CLI runtime paths and policies.
- var `CONFIG = DEFAULT_CONFIG.copy()` (L76) — @brief Constant `CONFIG` used by CLI runtime paths and policies.
- var `BRANCH_KEYS = ("master", "develop", "work")` (L79) — @brief Constant `BRANCH_KEYS` used by CLI runtime paths and policies.
- var `MANAGEMENT_HELP = [` (L82) — @brief Constant `MANAGEMENT_HELP` used by CLI runtime paths and policies.
### fn `def get_config_value(name)` (L95-98)
L92> @brief Execute `get_config_value` runtime logic for Git-Alias CLI.
L96> `return CONFIG.get(name, DEFAULT_CONFIG[name])`

### fn `def get_branch(name)` (L102-107)
L99> @brief Execute `get_branch` runtime logic for Git-Alias CLI.
L104> `raise KeyError(f"Unknown branch key {name}")`
L105> `return get_config_value(name)`

### fn `def get_editor()` (L110-113)
L108> @brief Execute `get_editor` runtime logic for Git-Alias CLI.
L111> `return get_config_value("editor")`

### fn `def _load_config_rules(key, fallback)` `priv` (L118-143)
L115> @param key Input parameter consumed by `_load_config_rules`.
L122> `return list(fallback)`
L141> `return rules if rules else list(fallback)`

### fn `def get_version_rules()` (L146-149)
L144> @brief Execute `get_version_rules` runtime logic for Git-Alias CLI.
L147> `return _load_config_rules("ver_rules", DEFAULT_VER_RULES)`

### fn `def get_cli_version()` (L152-163)
L150> @brief Execute `get_cli_version` runtime logic for Git-Alias CLI.
L157> `return "unknown"`
L160> `return match.group(1)`
L161> `return "unknown"`

### fn `def _normalize_semver_text(text: str) -> str` `priv` (L167-173)
L164> @brief Execute `_normalize_semver_text` runtime logic for Git-Alias CLI.
L171> `return value`

### fn `def check_for_newer_version(timeout_seconds: float = 1.0) -> None` (L177-258)
L174> @brief Execute `check_for_newer_version` runtime logic for Git-Alias CLI.
L180> `return`
L182> Controlla se esiste una cache valida
L192> Cache valida, controlla se c'è un aggiornamento disponibile
L204> Ignora errori di lettura cache
L207> `return` — Cache valida, skip controllo online
L209> Esegui il controllo online
L222> `return`
L227> `return`
L229> `return`
L234> `return`
L236> Salva nella cache
L247> Ignora errori di scrittura cache
L249> Mostra avviso se disponibile aggiornamento

### fn `def get_git_root()` (L261-276)
L259> @brief Execute `get_git_root` runtime logic for Git-Alias CLI.
L271> `return Path(location)`
L274> `return Path.cwd()`

### fn `def get_config_path(root=None)` (L280-284)
L277> @brief Execute `get_config_path` runtime logic for Git-Alias CLI.
L282> `return base / CONFIG_FILENAME`

### fn `def load_cli_config(root=None)` (L288-322)
L285> @brief Execute `load_cli_config` runtime logic for Git-Alias CLI.
L292> `return config_path`
L297> `return config_path`
L302> `return config_path`
L305> `return config_path`
L320> `return config_path`

### fn `def write_default_config(root=None)` (L326-333)
L323> @brief Execute `write_default_config` runtime logic for Git-Alias CLI.
L331> `return config_path`

### fn `def _editor_base_command()` `priv` (L336-350)
L334> @brief Execute `_editor_base_command` runtime logic for Git-Alias CLI.
L348> `return parts`

### fn `def run_editor_command(args)` (L354-356)
L351> @brief Execute `run_editor_command` runtime logic for Git-Alias CLI.
L355> `return run_command(_editor_base_command() + list(args))`

- var `HELP_TEXTS = {` (L359) — @brief Constant `HELP_TEXTS` used by CLI runtime paths and policies.
- var `RESET_HELP_COMMANDS = {"rs", "rshrd", "rskep", "rsmix", "rsmrg", "rssft"}` (L504) — @brief Constant `RESET_HELP_COMMANDS` used by CLI runtime paths and policies.
### fn `def _to_args(extra)` `priv` (L510-513)
L507> @brief Execute `_to_args` runtime logic for Git-Alias CLI.
L511> `return list(extra) if extra else []`

### class `class CommandExecutionError(RuntimeError)` : RuntimeError (L515-556)
L514> @brief Class `CommandExecutionError` models a typed runtime container/error boundary.
L516> @brief Execute `__init__` runtime logic for Git-Alias CLI.
- fn `def __init__(self, exc: subprocess.CalledProcessError)` `priv` (L520-527) L517> @param self Input parameter consumed by `__init__`.
- fn `def _format_message(self) -> str` `priv` (L531-541) L528> @brief Execute `_format_message` runtime logic for Git-Alias CLI.
  L534> `return text`
  L540> `return f"Command '{cmd_display}' failed with exit code {self.returncode}"`
- fn `def _decode_stream(data) -> str` `priv` (L546-556) L543> @brief Execute `_decode_stream` runtime logic for Git-Alias CLI.
  L548> `return ""`
  L551> `return data.decode("utf-8")`
  L553> `return data.decode("utf-8", errors="replace")`
  L554> `return str(data)`

### fn `def _run_checked(*popenargs, **kwargs)` `priv` (L561-568)
L558> @param *popenargs Input parameter consumed by `_run_checked`.
L564> `return subprocess.run(*popenargs, **kwargs)`
L566> `raise CommandExecutionError(exc) from None`

### class `class VersionDetectionError(RuntimeError)` : RuntimeError (L570-573)
L569> @brief Class `VersionDetectionError` models a typed runtime container/error boundary.

### class `class ReleaseError(RuntimeError)` : RuntimeError (L575-578)
L574> @brief Class `ReleaseError` models a typed runtime container/error boundary.

### fn `def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)` (L585-589)
L582> @param cwd Input parameter consumed by `run_git_cmd`.
L587> `return _run_checked(full, cwd=cwd, **kwargs)`

### fn `def capture_git_output(base_args, cwd=None)` (L594-598)
L591> @param base_args Input parameter consumed by `capture_git_output`.
L596> `return result.stdout.strip()`

### fn `def run_command(cmd, cwd=None)` (L603-606)
L600> @param cmd Input parameter consumed by `run_command`.
L604> `return _run_checked(cmd, cwd=cwd)`

### fn `def run_git_text(args, cwd=None, check=True)` (L612-629)
L609> @param cwd Input parameter consumed by `run_git_text`.
L626> `raise RuntimeError(message) from None`
L627> `return proc.stdout.strip()`

### fn `def run_shell(command, cwd=None)` (L634-637)
L631> @param command Input parameter consumed by `run_shell`.
L635> `return _run_checked(command, shell=True, cwd=cwd)`

### fn `def run_git_text(args, cwd=None, check=True)` (L643-660)
L640> @param cwd Input parameter consumed by `run_git_text`.
L657> `raise RuntimeError(message) from None`
L658> `return proc.stdout.strip()`

### fn `def _git_status_lines()` `priv` (L663-675)
L661> @brief Execute `_git_status_lines` runtime logic for Git-Alias CLI.
L672> `return []`
L673> `return proc.stdout.splitlines()`

### fn `def has_unstaged_changes(status_lines=None)` (L679-690)
L676> @brief Execute `has_unstaged_changes` runtime logic for Git-Alias CLI.
L685> `return True`
L687> `return True`
L688> `return False`

### fn `def has_staged_changes(status_lines=None)` (L694-703)
L691> @brief Execute `has_staged_changes` runtime logic for Git-Alias CLI.
L700> `return True`
L701> `return False`

- var `WIP_MESSAGE_RE = re.compile(r"^wip: work in progress\.$")` (L709) — @brief Constant `WIP_MESSAGE_RE` used by CLI runtime paths and policies.
### fn `def _refresh_remote_refs()` `priv` (L714-725)
L712> @brief Execute `_refresh_remote_refs` runtime logic for Git-Alias CLI.
L717> `return`
L722> `return`

### fn `def _branch_remote_divergence(branch_key, remote="origin")` `priv` (L730-748)
L727> @param branch_key Input parameter consumed by `_branch_remote_divergence`.
L737> `return (0, 0)`
L740> `return (0, 0)`
L745> `return (0, 0)`
L746> `return (local_ahead, remote_ahead)`

### fn `def has_remote_branch_updates(branch_key, remote="origin")` (L753-757)
L750> @param branch_key Input parameter consumed by `has_remote_branch_updates`.
L755> `return remote_ahead > 0`

### fn `def has_remote_develop_updates()` (L760-763)
L758> @brief Execute `has_remote_develop_updates` runtime logic for Git-Alias CLI.
L761> `return has_remote_branch_updates("develop")`

### fn `def has_remote_master_updates()` (L766-769)
L764> @brief Execute `has_remote_master_updates` runtime logic for Git-Alias CLI.
L767> `return has_remote_branch_updates("master")`

### fn `def _head_commit_message()` `priv` (L772-778)
L770> @brief Execute `_head_commit_message` runtime logic for Git-Alias CLI.
L774> `return run_git_text(["log", "-1", "--pretty=%s"]).strip()`
L776> `return ""`

### fn `def _head_commit_hash()` `priv` (L781-787)
L779> @brief Execute `_head_commit_hash` runtime logic for Git-Alias CLI.
L783> `return run_git_text(["rev-parse", "HEAD"]).strip()`
L785> `return ""`

### fn `def _commit_exists_in_branch(commit_hash, branch_name)` `priv` (L792-804)
L789> @param commit_hash Input parameter consumed by `_commit_exists_in_branch`.
L794> `return False`
L802> `return proc.returncode == 0`

### fn `def _should_amend_existing_commit()` `priv` (L807-822)
L805> @brief Execute `_should_amend_existing_commit` runtime logic for Git-Alias CLI.
L810> `return (False, "HEAD is not a WIP commit.")`
L813> `return (False, "Unable to determine the HEAD commit hash.")`
L817> `return (False, f"The last WIP commit is already contained in {develop_branch}.")`
L819> `return (False, f"The last WIP commit is already contained in {master_branch}.")`
L820> `return (True, "HEAD WIP commit is still pending locally.")`

### fn `def is_inside_git_repo()` (L825-832)
L823> @brief Execute `is_inside_git_repo` runtime logic for Git-Alias CLI.
L829> `return False`
L830> `return output.strip().lower() == "true"`

### class `class TagInfo` (L836-841)
L834> @brief Class `TagInfo` models a typed runtime container/error boundary.

- var `DELIM = "\x1f"` (L844) — @brief Constant `DELIM` used by CLI runtime paths and policies.
- var `RECORD = "\x1e"` (L847) — @brief Constant `RECORD` used by CLI runtime paths and policies.
- var `SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")` (L863) — @brief Constant `SEMVER_RE` used by CLI runtime paths and policies.
- var `SECTION_EMOJI = {` (L866) — @brief Constant `SECTION_EMOJI` used by CLI runtime paths and policies.
- var `MIN_SUPPORTED_HISTORY_VERSION = (0, 1, 0)` (L880) — @brief Constant `MIN_SUPPORTED_HISTORY_VERSION` used by CLI runtime paths and policies.
### fn `def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[int, int, int]]` `priv` (L886-889)
L883> @brief Execute `_tag_semver_tuple` runtime logic for Git-Alias CLI.
L887> `return _parse_semver_tuple(tag_name.lstrip("v"))`

### fn `def _is_supported_release_tag(tag_name: str) -> bool` `priv` (L893-899)
L890> @brief Execute `_is_supported_release_tag` runtime logic for Git-Alias CLI.
L896> `return True`
L897> `return semver >= MIN_SUPPORTED_HISTORY_VERSION`

### fn `def _should_include_tag(tag_name: str, include_draft: bool) -> bool` `priv` (L904-907)
L901> @param tag_name Input parameter consumed by `_should_include_tag`.
L905> `return include_draft or _is_supported_release_tag(tag_name)`

### fn `def _latest_supported_tag_name(tags: List[TagInfo], include_draft: bool) -> Optional[str]` `priv` (L912-920)
L909> @param tags Input parameter consumed by `_latest_supported_tag_name`.
L914> `return tags[-1].name if tags else None`
L917> `return tag.name`
L918> `return None`

### fn `def list_tags_sorted_by_date(repo_root: Path, merged_ref: Optional[str] = None) -> List[TagInfo]` (L925-945)
L922> @param repo_root Input parameter consumed by `list_tags_sorted_by_date`.
L933> `return []`
L943> `return tags`

### fn `def git_log_subjects(repo_root: Path, rev_range: str) -> List[str]` (L950-961)
L947> @param repo_root Input parameter consumed by `git_log_subjects`.
L958> `return []`
L959> `return [x.strip() for x in out.split(RECORD) if x.strip()]`

### fn `def categorize_commit(subject: str) -> Tuple[Optional[str], str]` (L965-988)
L962> @brief Execute `categorize_commit` runtime logic for Git-Alias CLI.
L968> `return (None, "")`
L986> `return (section, line) if section else (None, "")`

### fn `def _extract_release_version(subject: str) -> Optional[str]` `priv` (L992-998)
L989> @brief Execute `_extract_release_version` runtime logic for Git-Alias CLI.
L995> `return None`
L996> `return match.group(1)`

### fn `def generate_section_for_range(repo_root: Path, title: str, date_s: str, rev_range: str, expected_version: Optional[str] = None) -> Optional[str]` (L1006-1041)
L1003> @param rev_range Input parameter consumed by `generate_section_for_range`.
L1017> `return None`
L1039> `return "\n".join(lines).rstrip() + "\n"`

### fn `def _canonical_origin_base(repo_root: Path) -> Optional[str]` `priv` (L1045-1062)
L1042> @brief Execute `_canonical_origin_base` runtime logic for Git-Alias CLI.
L1048> `return None`
L1059> `return None`
L1060> `return base`

### fn `def get_origin_compare_url(base_url: Optional[str], prev_tag: Optional[str], tag: str) -> Optional[str]` (L1068-1075)
L1065> @param prev_tag Input parameter consumed by `get_origin_compare_url`.
L1070> `return None`
L1072> `return f"{base_url}/compare/{prev_tag}..{tag}"`
L1073> `return f"{base_url}/releases/tag/{tag}"`

### fn `def get_release_page_url(base_url: Optional[str], tag: str) -> Optional[str]` (L1080-1085)
L1077> @param base_url Input parameter consumed by `get_release_page_url`.
L1082> `return None`
L1083> `return f"{base_url}/releases/tag/{tag}"`

### fn `def build_history_section(` (L1093-1098)
L1090> @param include_draft Input parameter consumed by `build_history_section`.

### fn `def generate_changelog_document(repo_root: Path, include_unreleased: bool, include_draft: bool = False) -> str` (L1132-1179)
L1129> @param include_unreleased Input parameter consumed by `generate_changelog_document`.
L1177> `return "\n".join(lines).rstrip() + "\n"`

### fn `def _collect_version_files(root, pattern)` `priv` (L1184-1219)
L1181> @param root Input parameter consumed by `_collect_version_files`.
L1189> `return files`
L1195> Applica il pattern usando pathspec (mantiene REQ-017)
L1204> skip empty lines
L1217> `return files`

### fn `def _is_version_path_excluded(relative_path: str) -> bool` `priv` (L1223-1226)
L1220> @brief Execute `_is_version_path_excluded` runtime logic for Git-Alias CLI.
L1224> `return any(regex.search(relative_path) for regex in VERSION_CLEANUP_PATTERNS)`

### fn `def _iter_versions_in_text(text, compiled_regexes)` `priv` (L1231-1242)
L1228> @param text Input parameter consumed by `_iter_versions_in_text`.
L1237> `yield group`
L1240> `yield match.group(0)`

### fn `def _determine_canonical_version(root: Path, rules, *, verbose: bool = False, debug: bool = False)` `priv` (L1249-1308)
L1246> @param verbose Input parameter consumed by `_determine_canonical_version`.
L1268> `raise VersionDetectionError(`
L1274> `raise VersionDetectionError(`
L1297> `raise VersionDetectionError(`
L1301> `raise VersionDetectionError(`
L1305> `raise VersionDetectionError("No version string matched the configured rule list.")`
L1306> `return canonical`

### fn `def _parse_semver_tuple(text)` `priv` (L1312-1318)
L1309> @brief Execute `_parse_semver_tuple` runtime logic for Git-Alias CLI.
L1315> `return None`
L1316> `return tuple(int(match.group(i)) for i in range(1, 4))`

### fn `def _replace_versions_in_text(text, compiled_regex, replacement)` `priv` (L1324-1339)
L1321> @param compiled_regex Input parameter consumed by `_replace_versions_in_text`.
L1335> `return text, 0`
L1337> `return "".join(pieces), count`

### fn `def _current_branch_name()` `priv` (L1342-1354)
L1340> @brief Execute `_current_branch_name` runtime logic for Git-Alias CLI.
L1351> `raise ReleaseError("Release commands require an active branch head.")`
L1352> `return branch`

### fn `def _ref_exists(ref_name)` `priv` (L1358-1367)
L1355> @brief Execute `_ref_exists` runtime logic for Git-Alias CLI.
L1365> `return proc.returncode == 0`

### fn `def _local_branch_exists(branch_name)` `priv` (L1371-1374)
L1368> @brief Execute `_local_branch_exists` runtime logic for Git-Alias CLI.
L1372> `return _ref_exists(f"refs/heads/{branch_name}")`

### fn `def _remote_branch_exists(branch_name)` `priv` (L1378-1381)
L1375> @brief Execute `_remote_branch_exists` runtime logic for Git-Alias CLI.
L1379> `return _ref_exists(f"refs/remotes/origin/{branch_name}")`

### fn `def _ensure_release_prerequisites()` `priv` (L1384-1411)
L1382> @brief Execute `_ensure_release_prerequisites` runtime logic for Git-Alias CLI.
L1391> `raise ReleaseError(f"Unable to run release command: missing local branches {joined}.")`
L1396> `raise ReleaseError(f"Unable to run release command: missing remote branches {joined}.")`
L1398> `raise ReleaseError(f"Remote branch {master_branch} has pending updates. Please pull them first.")`
L1400> `raise ReleaseError(f"Remote branch {develop_branch} has pending updates. Please pull them first.")`
L1403> `raise ReleaseError(f"Release commands must be executed from the {work_branch} branch (current: {current_branch}).")`
L1406> `raise ReleaseError("Working tree changes detected. Clean or stage them before running a release.")`
L1408> `raise ReleaseError("Staging area is not empty. Complete or reset pending commits before running a release.")`
L1409> `return {"master": master_branch, "develop": develop_branch, "work": work_branch}`

### fn `def _bump_semver_version(current_version, level)` `priv` (L1416-1434)
L1413> @param current_version Input parameter consumed by `_bump_semver_version`.
L1419> `raise ReleaseError(f"The current version '{current_version}' is not a valid semantic version.")`
L1431> `raise ReleaseError(f"Unsupported release level '{level}'.")`
L1432> `return f"{major}.{minor}.{patch}"`

### fn `def _run_release_step(level, step_name, action)` `priv` (L1440-1460)
L1437> @param step_name Input parameter consumed by `_run_release_step`.
L1445> `return result`
L1447> `raise`
L1449> `raise`
L1453> `raise ReleaseError(f"\n--- {label} Step '{step_name}' failed: {message} ---") from None`
L1456> `raise ReleaseError(f"\n--- {label} Step '{step_name}' failed: command exited with status {code} ---") from None`
L1458> `raise ReleaseError(f"\n--- {label} Step '{step_name}' failed: {exc} ---") from None`

### fn `def _execute_release_flow(level, changelog_args=None)` `priv` (L1465-1507)
L1462> @param level Input parameter consumed by `_execute_release_flow`.
L1469> `raise ReleaseError("No version rules configured. Cannot compute the next version.")`

### fn `def _run_release_command(level, changelog_args=None)` `priv` (L1512-1527)
L1509> @param level Input parameter consumed by `_run_release_command`.
L1517> `sys.exit(1)`
L1520> `sys.exit(1)`
L1525> `sys.exit(exc.returncode or 1)`

### fn `def _run_reset_with_help(base_args, extra)` `priv` (L1532-1539)
L1529> @param base_args Input parameter consumed by `_run_reset_with_help`.
L1536> `return`
L1537> `return run_git_cmd(base_args, args)`

### fn `def _reject_extra_arguments(extra, alias)` `priv` (L1544-1550)
L1541> @param extra Input parameter consumed by `_reject_extra_arguments`.
L1548> `sys.exit(1)`

### fn `def _parse_release_flags(extra, alias)` `priv` (L1555-1573)
L1552> @param extra Input parameter consumed by `_parse_release_flags`.
L1558> `return []`
L1564> `sys.exit(1)`
L1571> `return deduped`

### fn `def _prepare_commit_message(extra, alias)` `priv` (L1578-1588)
L1575> @param extra Input parameter consumed by `_prepare_commit_message`.
L1582> `sys.exit(1)`
L1585> `sys.exit(0)`
L1586> `return " ".join(args)`

### fn `def _build_conventional_message(kind: str, extra, alias: str) -> str` `priv` (L1594-1608)
L1591> @param extra Input parameter consumed by `_build_conventional_message`.
L1605> `sys.exit(1)`
L1606> `return f"{kind}({scope}): {body}"`

### fn `def _run_conventional_commit(kind: str, alias: str, extra)` `priv` (L1614-1619)
L1611> @param alias Input parameter consumed by `_run_conventional_commit`.
L1617> `return _execute_commit(message, alias, allow_amend=False)`

### fn `def _execute_commit(message, alias, allow_amend=True)` `priv` (L1625-1654)
L1622> @param alias Input parameter consumed by `_execute_commit`.
L1640> `return run_git_cmd(base, input=message, text=True)`
L1648> `sys.exit(exc.returncode or 1)`
L1651> `sys.exit(exc.returncode or 1)`
L1652> `raise`

### fn `def upgrade_self()` (L1657-1670)
L1655> @brief Execute `upgrade_self` runtime logic for Git-Alias CLI.

### fn `def remove_self()` (L1673-1676)
L1671> @brief Execute `remove_self` runtime logic for Git-Alias CLI.

### fn `def cmd_aa(extra)` (L1680-1687)
L1677> @brief Execute `cmd_aa` runtime logic for Git-Alias CLI.
L1684> `sys.exit(1)`
L1685> `return run_git_cmd(["add", "--all"], extra)`

### fn `def cmd_ra(extra)` (L1691-1714)
L1688> @brief Execute `cmd_ra` runtime logic for Git-Alias CLI.
L1696> `return`
L1698> `sys.exit(1)`
L1704> `sys.exit(1)`
L1710> `sys.exit(1)`
L1712> `return run_git_cmd(["reset", "--mixed"], [])`

### fn `def cmd_ar(extra)` (L1718-1731)
L1715> @brief Execute `cmd_ar` runtime logic for Git-Alias CLI.
L1729> `return gzip_proc`

### fn `def cmd_br(extra)` (L1735-1738)
L1732> @brief Execute `cmd_br` runtime logic for Git-Alias CLI.
L1736> `return run_git_cmd(["branch"], extra)`

### fn `def cmd_bd(extra)` (L1742-1745)
L1739> @brief Execute `cmd_bd` runtime logic for Git-Alias CLI.
L1743> `return run_git_cmd(["branch", "-d"], extra)`

### fn `def cmd_ck(extra)` (L1749-1752)
L1746> @brief Execute `cmd_ck` runtime logic for Git-Alias CLI.
L1750> `return run_git_cmd(["diff", "--check"], extra)`

### fn `def _ensure_commit_ready(alias)` `priv` (L1756-1769)
L1753> @brief Execute `_ensure_commit_ready` runtime logic for Git-Alias CLI.
L1763> `sys.exit(1)`
L1766> `sys.exit(1)`
L1767> `return True`

### fn `def cmd_cm(extra)` (L1773-1778)
L1770> @brief Execute `cmd_cm` runtime logic for Git-Alias CLI.
L1776> `return _execute_commit(message, "cm")`

### fn `def cmd_wip(extra)` (L1782-1794)
L1779> @brief Execute `cmd_wip` runtime logic for Git-Alias CLI.
L1787> `return`
L1789> `sys.exit(1)`
L1792> `return _execute_commit(message, "wip")`

### fn `def cmd_release(extra)` (L1798-1820)
L1795> @brief Execute `cmd_release` runtime logic for Git-Alias CLI.
L1803> `return`
L1805> `sys.exit(1)`
L1810> `sys.exit(1)`
L1816> `sys.exit(1)`
L1818> `return _execute_commit(message, "release")`

### fn `def cmd_new(extra)` (L1824-1827)
L1821> @brief Execute `cmd_new` runtime logic for Git-Alias CLI.
L1825> `return _run_conventional_commit("new", "new", extra)`

### fn `def cmd_refactor(extra)` (L1831-1834)
L1828> @brief Execute `cmd_refactor` runtime logic for Git-Alias CLI.
L1832> `return _run_conventional_commit("refactor", "refactor", extra)`

### fn `def cmd_fix(extra)` (L1838-1841)
L1835> @brief Execute `cmd_fix` runtime logic for Git-Alias CLI.
L1839> `return _run_conventional_commit("fix", "fix", extra)`

### fn `def cmd_change(extra)` (L1845-1848)
L1842> @brief Execute `cmd_change` runtime logic for Git-Alias CLI.
L1846> `return _run_conventional_commit("change", "change", extra)`

### fn `def cmd_docs(extra)` (L1852-1855)
L1849> @brief Execute `cmd_docs` runtime logic for Git-Alias CLI.
L1853> `return _run_conventional_commit("docs", "docs", extra)`

### fn `def cmd_style(extra)` (L1859-1862)
L1856> @brief Execute `cmd_style` runtime logic for Git-Alias CLI.
L1860> `return _run_conventional_commit("style", "style", extra)`

### fn `def cmd_revert(extra)` (L1866-1869)
L1863> @brief Execute `cmd_revert` runtime logic for Git-Alias CLI.
L1867> `return _run_conventional_commit("revert", "revert", extra)`

### fn `def cmd_misc(extra)` (L1873-1876)
L1870> @brief Execute `cmd_misc` runtime logic for Git-Alias CLI.
L1874> `return _run_conventional_commit("misc", "misc", extra)`

### fn `def cmd_cover(extra)` (L1880-1883)
L1877> @brief Execute `cmd_cover` runtime logic for Git-Alias CLI.
L1881> `return _run_conventional_commit("cover", "cover", extra)`

### fn `def cmd_co(extra)` (L1887-1890)
L1884> @brief Execute `cmd_co` runtime logic for Git-Alias CLI.
L1888> `return run_git_cmd(["checkout"], extra)`

### fn `def cmd_de(extra)` (L1894-1897)
L1891> @brief Execute `cmd_de` runtime logic for Git-Alias CLI.
L1895> `return run_git_cmd(["describe"], extra)`

### fn `def cmd_di(extra)` (L1901-1904)
L1898> @brief Execute `cmd_di` runtime logic for Git-Alias CLI.
L1902> `return run_git_cmd(["checkout", "--"], extra)`

### fn `def cmd_diyou(extra)` (L1908-1911)
L1905> @brief Execute `cmd_diyou` runtime logic for Git-Alias CLI.
L1909> `return run_git_cmd(["checkout", "--ours", "--"], extra)`

### fn `def cmd_dime(extra)` (L1915-1918)
L1912> @brief Execute `cmd_dime` runtime logic for Git-Alias CLI.
L1916> `return run_git_cmd(["checkout", "--theirs", "--"], extra)`

### fn `def cmd_ed(extra)` (L1922-1931)
L1919> @brief Execute `cmd_ed` runtime logic for Git-Alias CLI.
L1926> `sys.exit(1)`

### fn `def cmd_fe(extra)` (L1935-1938)
L1932> @brief Execute `cmd_fe` runtime logic for Git-Alias CLI.
L1936> `return run_git_cmd(["fetch"], extra)`

### fn `def cmd_feall(extra)` (L1942-1945)
L1939> @brief Execute `cmd_feall` runtime logic for Git-Alias CLI.
L1943> `return cmd_fe(["--all", "--tags", "--prune"] + _to_args(extra))`

### fn `def cmd_gp(extra)` (L1949-1952)
L1946> @brief Execute `cmd_gp` runtime logic for Git-Alias CLI.
L1950> `return run_command(["gitk", "--all"] + _to_args(extra))`

### fn `def cmd_gr(extra)` (L1956-1959)
L1953> @brief Execute `cmd_gr` runtime logic for Git-Alias CLI.
L1957> `return run_command(["gitk", "--simplify-by-decoration", "--all"] + _to_args(extra))`

### fn `def cmd_str(extra)` (L1963-1992)
L1960> @brief Execute `cmd_str` runtime logic for Git-Alias CLI.
L1964> Esegue git remote -v per ottenere l'elenco dei remote
L1968> Filtra e raccoglie tutti i remote univoci
L1977> Stampa i remote trovati
L1983> Per ogni remote univoco esegue git remote show
L1990> `raise`

### fn `def cmd_lb(extra)` (L1996-1999)
L1993> @brief Execute `cmd_lb` runtime logic for Git-Alias CLI.
L1997> `return run_git_cmd(["branch", "-v", "-a"], extra)`

### fn `def cmd_lg(extra)` (L2003-2016)
L2000> @brief Execute `cmd_lg` runtime logic for Git-Alias CLI.
L2004> `return run_git_cmd(`

### fn `def cmd_lh(extra)` (L2020-2023)
L2017> @brief Execute `cmd_lh` runtime logic for Git-Alias CLI.
L2021> `return run_git_cmd(["log", "-1", "HEAD"], extra)`

### fn `def cmd_ll(extra)` (L2027-2039)
L2024> @brief Execute `cmd_ll` runtime logic for Git-Alias CLI.
L2028> `return run_git_cmd(`

### fn `def cmd_lm(extra)` (L2043-2046)
L2040> @brief Execute `cmd_lm` runtime logic for Git-Alias CLI.
L2044> `return run_git_cmd(["log", "--merges"], extra)`

### fn `def cmd_lt(extra)` (L2050-2053)
L2047> @brief Execute `cmd_lt` runtime logic for Git-Alias CLI.
L2051> `return run_git_cmd(["tag", "-l"], extra)`

### fn `def cmd_me(extra)` (L2057-2060)
L2054> @brief Execute `cmd_me` runtime logic for Git-Alias CLI.
L2058> `return run_git_cmd(["merge", "--ff-only"], extra)`

### fn `def cmd_pl(extra)` (L2064-2067)
L2061> @brief Execute `cmd_pl` runtime logic for Git-Alias CLI.
L2065> `return run_git_cmd(["pull", "--ff-only"], extra)`

### fn `def cmd_pt(extra)` (L2071-2074)
L2068> @brief Execute `cmd_pt` runtime logic for Git-Alias CLI.
L2072> `return run_git_cmd(["push", "--tags"], extra)`

### fn `def cmd_pu(extra)` (L2078-2081)
L2075> @brief Execute `cmd_pu` runtime logic for Git-Alias CLI.
L2079> `return run_git_cmd(["push", "-u"], extra)`

### fn `def cmd_rf(extra)` (L2085-2088)
L2082> @brief Execute `cmd_rf` runtime logic for Git-Alias CLI.
L2086> `return run_git_cmd(["reflog"], extra)`

### fn `def cmd_rmtg(extra)` (L2092-2102)
L2089> @brief Execute `cmd_rmtg` runtime logic for Git-Alias CLI.
L2096> `sys.exit(1)`
L2100> `return run_git_cmd(["push", "--delete", "origin", tag], tail)`

### fn `def cmd_rmloc(extra)` (L2106-2109)
L2103> @brief Execute `cmd_rmloc` runtime logic for Git-Alias CLI.
L2107> `return run_git_cmd(["reset", "--hard", "--"], extra)`

### fn `def cmd_rmstg(extra)` (L2113-2116)
L2110> @brief Execute `cmd_rmstg` runtime logic for Git-Alias CLI.
L2114> `return run_git_cmd(["rm", "--cached", "--"], extra)`

### fn `def cmd_rmunt(extra)` (L2120-2123)
L2117> @brief Execute `cmd_rmunt` runtime logic for Git-Alias CLI.
L2121> `return run_git_cmd(["clean", "-d", "-f", "--"], extra)`

### fn `def cmd_rs(extra)` (L2127-2130)
L2124> @brief Execute `cmd_rs` runtime logic for Git-Alias CLI.
L2128> `return _run_reset_with_help(["reset", "--hard", "HEAD"], extra)`

### fn `def cmd_rssft(extra)` (L2134-2137)
L2131> @brief Execute `cmd_rssft` runtime logic for Git-Alias CLI.
L2135> `return _run_reset_with_help(["reset", "--soft", "--"], extra)`

### fn `def cmd_rsmix(extra)` (L2141-2144)
L2138> @brief Execute `cmd_rsmix` runtime logic for Git-Alias CLI.
L2142> `return _run_reset_with_help(["reset", "--mixed", "--"], extra)`

### fn `def cmd_rshrd(extra)` (L2148-2151)
L2145> @brief Execute `cmd_rshrd` runtime logic for Git-Alias CLI.
L2149> `return _run_reset_with_help(["reset", "--hard", "--"], extra)`

### fn `def cmd_rsmrg(extra)` (L2155-2158)
L2152> @brief Execute `cmd_rsmrg` runtime logic for Git-Alias CLI.
L2156> `return _run_reset_with_help(["reset", "--merge", "--"], extra)`

### fn `def cmd_rskep(extra)` (L2162-2165)
L2159> @brief Execute `cmd_rskep` runtime logic for Git-Alias CLI.
L2163> `return _run_reset_with_help(["reset", "--keep", "--"], extra)`

### fn `def cmd_st(extra)` (L2169-2172)
L2166> @brief Execute `cmd_st` runtime logic for Git-Alias CLI.
L2170> `return run_git_cmd(["status"], extra)`

### fn `def cmd_tg(extra)` (L2176-2179)
L2173> @brief Execute `cmd_tg` runtime logic for Git-Alias CLI.
L2177> `return run_git_cmd(["tag", "-a", "-m"], extra)`

### fn `def cmd_unstg(extra)` (L2183-2186)
L2180> @brief Execute `cmd_unstg` runtime logic for Git-Alias CLI.
L2184> `return run_git_cmd(["reset", "--mixed", "--"], extra)`

### fn `def cmd_ver(extra)` (L2190-2208)
L2187> @brief Execute `cmd_ver` runtime logic for Git-Alias CLI.
L2200> `sys.exit(1)`
L2205> `sys.exit(1)`

### fn `def cmd_chver(extra)` (L2212-2282)
L2209> @brief Execute `cmd_chver` runtime logic for Git-Alias CLI.
L2216> `sys.exit(1)`
L2221> `sys.exit(1)`
L2226> `sys.exit(1)`
L2231> `sys.exit(1)`
L2235> `sys.exit(1)`
L2238> `return`
L2264> `sys.exit(1)`
L2268> `sys.exit(1)`
L2273> `sys.exit(1)`
L2279> `sys.exit(1)`

### fn `def cmd_major(extra)` (L2286-2290)
L2283> @brief Execute `cmd_major` runtime logic for Git-Alias CLI.

### fn `def cmd_minor(extra)` (L2294-2298)
L2291> @brief Execute `cmd_minor` runtime logic for Git-Alias CLI.

### fn `def cmd_patch(extra)` (L2302-2306)
L2299> @brief Execute `cmd_patch` runtime logic for Git-Alias CLI.

### fn `def cmd_changelog(extra)` (L2310-2342)
L2307> @brief Execute `cmd_changelog` runtime logic for Git-Alias CLI.
L2321> `sys.exit(2)`
L2324> `return`
L2327> `sys.exit(2)`
L2332> `return`
L2339> `sys.exit(1)`

- var `COMMANDS = {` (L2345) — @brief Constant `COMMANDS` used by CLI runtime paths and policies.
### fn `def print_command_help(name, width=None)` (L2410-2416)
L2407> @param name Input parameter consumed by `print_command_help`.

### fn `def print_all_help()` (L2419-2453)
L2417> @brief Execute `print_all_help` runtime logic for Git-Alias CLI.

### fn `def main(argv=None, *, check_updates: bool = True)` (L2458-2508)
L2455> @param argv Input parameter consumed by `main`.
L2465> `sys.exit(1)`
L2468> `sys.exit(1)`
L2473> `return`
L2476> `return`
L2479> `return`
L2482> `return`
L2486> `return`
L2490> `return`
L2496> `return`
L2502> `return`
L2508> `sys.exit(exc.returncode or 1)`

## Comments
- L2-3: @file core.py | @brief Core command dispatch and git-alias runtime orchestration.
- L114: @brief Execute `_load_config_rules` runtime logic for Git-Alias CLI.
- L182: Controlla se esiste una cache valida
- L192: Cache valida, controlla se c'è un aggiornamento disponibile
- L209: Esegui il controllo online
- L236: Salva nella cache
- L249: Mostra avviso se disponibile aggiornamento
- L420-500: @brief Constant `RESET_HELP` used by CLI runtime paths and policies. | RESET_HELP = Reset commands help screen ...
- L516: @brief Execute `__init__` runtime logic for Git-Alias CLI.
- L557: @brief Execute `_run_checked` runtime logic for Git-Alias CLI.
- L579-581: @brief Execute `run_git_cmd` runtime logic for Git-Alias CLI. | @param base_args Input parameter consumed by `run_git_cmd`. | @param extra Input parameter consumed by `run_git_cmd`.
- L590: @brief Execute `capture_git_output` runtime logic for Git-Alias CLI.
- L599: @brief Execute `run_command` runtime logic for Git-Alias CLI.
- L607-608: @brief Execute `run_git_text` runtime logic for Git-Alias CLI. | @param args Input parameter consumed by `run_git_text`.
- L630: @brief Execute `run_shell` runtime logic for Git-Alias CLI.
- L638-639: @brief Execute `run_git_text` runtime logic for Git-Alias CLI. | @param args Input parameter consumed by `run_git_text`.
- L704: @brief Constant `_REMOTE_REFS_UPDATED` used by CLI runtime paths and policies.
- L726: @brief Execute `_branch_remote_divergence` runtime logic for Git-Alias CLI.
- L749: @brief Execute `has_remote_branch_updates` runtime logic for Git-Alias CLI.
- L788: @brief Execute `_commit_exists_in_branch` runtime logic for Git-Alias CLI.
- L848: @brief Constant `_CONVENTIONAL_RE` used by CLI runtime paths and policies.
- L855: @brief Constant `_MODULE_PREFIX_RE` used by CLI runtime paths and policies.
- L858: @brief Constant `_SEMVER_TAG_RE` used by CLI runtime paths and policies.
- L900: @brief Execute `_should_include_tag` runtime logic for Git-Alias CLI.
- L908: @brief Execute `_latest_supported_tag_name` runtime logic for Git-Alias CLI.
- L921: @brief Execute `list_tags_sorted_by_date` runtime logic for Git-Alias CLI.
- L946: @brief Execute `git_log_subjects` runtime logic for Git-Alias CLI.
- L999-1002: @brief Execute `generate_section_for_range` runtime logic for Git-Alias CLI. | @param repo_root Input parameter consumed by `generate_section_for_range`. | @param title Input parameter consumed by `generate_section_for_range`. | @param date_s Input parameter consumed by `generate_section_for_range`.
- L1063-1064: @brief Execute `get_origin_compare_url` runtime logic for Git-Alias CLI. | @param base_url Input parameter consumed by `get_origin_compare_url`.
- L1076: @brief Execute `get_release_page_url` runtime logic for Git-Alias CLI.
- L1086-1089: @brief Execute `build_history_section` runtime logic for Git-Alias CLI. | @param repo_root Input parameter consumed by `build_history_section`. | @param tags Input parameter consumed by `build_history_section`. | @param include_unreleased Input parameter consumed by `build_history_section`.
- L1127-1128: @brief Execute `generate_changelog_document` runtime logic for Git-Alias CLI. | @param repo_root Input parameter consumed by `generate_changelog_document`.
- L1180: @brief Execute `_collect_version_files` runtime logic for Git-Alias CLI.
- L1195: Applica il pattern usando pathspec (mantiene REQ-017)
- L1227: @brief Execute `_iter_versions_in_text` runtime logic for Git-Alias CLI.
- L1243-1245: @brief Execute `_determine_canonical_version` runtime logic for Git-Alias CLI. | @param root Input parameter consumed by `_determine_canonical_version`. | @param rules Input parameter consumed by `_determine_canonical_version`.
- L1319-1320: @brief Execute `_replace_versions_in_text` runtime logic for Git-Alias CLI. | @param text Input parameter consumed by `_replace_versions_in_text`.
- L1412: @brief Execute `_bump_semver_version` runtime logic for Git-Alias CLI.
- L1435-1436: @brief Execute `_run_release_step` runtime logic for Git-Alias CLI. | @param level Input parameter consumed by `_run_release_step`.
- L1461: @brief Execute `_execute_release_flow` runtime logic for Git-Alias CLI.
- L1508: @brief Execute `_run_release_command` runtime logic for Git-Alias CLI.
- L1528: @brief Execute `_run_reset_with_help` runtime logic for Git-Alias CLI.
- L1540: @brief Execute `_reject_extra_arguments` runtime logic for Git-Alias CLI.
- L1551: @brief Execute `_parse_release_flags` runtime logic for Git-Alias CLI.
- L1574: @brief Execute `_prepare_commit_message` runtime logic for Git-Alias CLI.
- L1589-1590: @brief Execute `_build_conventional_message` runtime logic for Git-Alias CLI. | @param kind Input parameter consumed by `_build_conventional_message`.
- L1609-1610: @brief Execute `_run_conventional_commit` runtime logic for Git-Alias CLI. | @param kind Input parameter consumed by `_run_conventional_commit`.
- L1620-1621: @brief Execute `_execute_commit` runtime logic for Git-Alias CLI. | @param message Input parameter consumed by `_execute_commit`.
- L1964: Esegue git remote -v per ottenere l'elenco dei remote
- L1968: Filtra e raccoglie tutti i remote univoci
- L1977: Stampa i remote trovati
- L1983: Per ogni remote univoco esegue git remote show
- L2406: @brief Execute `print_command_help` runtime logic for Git-Alias CLI.
- L2454: @brief Execute `main` runtime logic for Git-Alias CLI.

## Symbol Index
|Symbol|Kind|Vis|Lines|Sig|
|---|---|---|---|---|
|`CONFIG_FILENAME`|var|pub|25||
|`GITHUB_LATEST_RELEASE_API`|var|pub|29||
|`VERSION_CHECK_CACHE_FILE`|var|pub|32||
|`VERSION_CHECK_TTL_HOURS`|var|pub|35||
|`DEFAULT_VER_RULES`|var|pub|39||
|`VERSION_CLEANUP_REGEXES`|var|pub|46||
|`VERSION_CLEANUP_PATTERNS`|var|pub|57||
|`DEFAULT_CONFIG`|var|pub|61||
|`CONFIG`|var|pub|76||
|`BRANCH_KEYS`|var|pub|79||
|`MANAGEMENT_HELP`|var|pub|82||
|`get_config_value`|fn|pub|95-98|def get_config_value(name)|
|`get_branch`|fn|pub|102-107|def get_branch(name)|
|`get_editor`|fn|pub|110-113|def get_editor()|
|`_load_config_rules`|fn|priv|118-143|def _load_config_rules(key, fallback)|
|`get_version_rules`|fn|pub|146-149|def get_version_rules()|
|`get_cli_version`|fn|pub|152-163|def get_cli_version()|
|`_normalize_semver_text`|fn|priv|167-173|def _normalize_semver_text(text: str) -> str|
|`check_for_newer_version`|fn|pub|177-258|def check_for_newer_version(timeout_seconds: float = 1.0)...|
|`get_git_root`|fn|pub|261-276|def get_git_root()|
|`get_config_path`|fn|pub|280-284|def get_config_path(root=None)|
|`load_cli_config`|fn|pub|288-322|def load_cli_config(root=None)|
|`write_default_config`|fn|pub|326-333|def write_default_config(root=None)|
|`_editor_base_command`|fn|priv|336-350|def _editor_base_command()|
|`run_editor_command`|fn|pub|354-356|def run_editor_command(args)|
|`HELP_TEXTS`|var|pub|359||
|`RESET_HELP_COMMANDS`|var|pub|504||
|`_to_args`|fn|priv|510-513|def _to_args(extra)|
|`CommandExecutionError`|class|pub|515-556|class CommandExecutionError(RuntimeError)|
|`CommandExecutionError.__init__`|fn|priv|520-527|def __init__(self, exc: subprocess.CalledProcessError)|
|`CommandExecutionError._format_message`|fn|priv|531-541|def _format_message(self) -> str|
|`CommandExecutionError._decode_stream`|fn|priv|546-556|def _decode_stream(data) -> str|
|`_run_checked`|fn|priv|561-568|def _run_checked(*popenargs, **kwargs)|
|`VersionDetectionError`|class|pub|570-573|class VersionDetectionError(RuntimeError)|
|`ReleaseError`|class|pub|575-578|class ReleaseError(RuntimeError)|
|`run_git_cmd`|fn|pub|585-589|def run_git_cmd(base_args, extra=None, cwd=None, **kwargs)|
|`capture_git_output`|fn|pub|594-598|def capture_git_output(base_args, cwd=None)|
|`run_command`|fn|pub|603-606|def run_command(cmd, cwd=None)|
|`run_git_text`|fn|pub|612-629|def run_git_text(args, cwd=None, check=True)|
|`run_shell`|fn|pub|634-637|def run_shell(command, cwd=None)|
|`run_git_text`|fn|pub|643-660|def run_git_text(args, cwd=None, check=True)|
|`_git_status_lines`|fn|priv|663-675|def _git_status_lines()|
|`has_unstaged_changes`|fn|pub|679-690|def has_unstaged_changes(status_lines=None)|
|`has_staged_changes`|fn|pub|694-703|def has_staged_changes(status_lines=None)|
|`WIP_MESSAGE_RE`|var|pub|709||
|`_refresh_remote_refs`|fn|priv|714-725|def _refresh_remote_refs()|
|`_branch_remote_divergence`|fn|priv|730-748|def _branch_remote_divergence(branch_key, remote="origin")|
|`has_remote_branch_updates`|fn|pub|753-757|def has_remote_branch_updates(branch_key, remote="origin")|
|`has_remote_develop_updates`|fn|pub|760-763|def has_remote_develop_updates()|
|`has_remote_master_updates`|fn|pub|766-769|def has_remote_master_updates()|
|`_head_commit_message`|fn|priv|772-778|def _head_commit_message()|
|`_head_commit_hash`|fn|priv|781-787|def _head_commit_hash()|
|`_commit_exists_in_branch`|fn|priv|792-804|def _commit_exists_in_branch(commit_hash, branch_name)|
|`_should_amend_existing_commit`|fn|priv|807-822|def _should_amend_existing_commit()|
|`is_inside_git_repo`|fn|pub|825-832|def is_inside_git_repo()|
|`TagInfo`|class|pub|836-841|class TagInfo|
|`DELIM`|var|pub|844||
|`RECORD`|var|pub|847||
|`SEMVER_RE`|var|pub|863||
|`SECTION_EMOJI`|var|pub|866||
|`MIN_SUPPORTED_HISTORY_VERSION`|var|pub|880||
|`_tag_semver_tuple`|fn|priv|886-889|def _tag_semver_tuple(tag_name: str) -> Optional[Tuple[in...|
|`_is_supported_release_tag`|fn|priv|893-899|def _is_supported_release_tag(tag_name: str) -> bool|
|`_should_include_tag`|fn|priv|904-907|def _should_include_tag(tag_name: str, include_draft: boo...|
|`_latest_supported_tag_name`|fn|priv|912-920|def _latest_supported_tag_name(tags: List[TagInfo], inclu...|
|`list_tags_sorted_by_date`|fn|pub|925-945|def list_tags_sorted_by_date(repo_root: Path, merged_ref:...|
|`git_log_subjects`|fn|pub|950-961|def git_log_subjects(repo_root: Path, rev_range: str) -> ...|
|`categorize_commit`|fn|pub|965-988|def categorize_commit(subject: str) -> Tuple[Optional[str...|
|`_extract_release_version`|fn|priv|992-998|def _extract_release_version(subject: str) -> Optional[str]|
|`generate_section_for_range`|fn|pub|1006-1041|def generate_section_for_range(repo_root: Path, title: st...|
|`_canonical_origin_base`|fn|priv|1045-1062|def _canonical_origin_base(repo_root: Path) -> Optional[str]|
|`get_origin_compare_url`|fn|pub|1068-1075|def get_origin_compare_url(base_url: Optional[str], prev_...|
|`get_release_page_url`|fn|pub|1080-1085|def get_release_page_url(base_url: Optional[str], tag: st...|
|`build_history_section`|fn|pub|1093-1098|def build_history_section(|
|`generate_changelog_document`|fn|pub|1132-1179|def generate_changelog_document(repo_root: Path, include_...|
|`_collect_version_files`|fn|priv|1184-1219|def _collect_version_files(root, pattern)|
|`_is_version_path_excluded`|fn|priv|1223-1226|def _is_version_path_excluded(relative_path: str) -> bool|
|`_iter_versions_in_text`|fn|priv|1231-1242|def _iter_versions_in_text(text, compiled_regexes)|
|`_determine_canonical_version`|fn|priv|1249-1308|def _determine_canonical_version(root: Path, rules, *, ve...|
|`_parse_semver_tuple`|fn|priv|1312-1318|def _parse_semver_tuple(text)|
|`_replace_versions_in_text`|fn|priv|1324-1339|def _replace_versions_in_text(text, compiled_regex, repla...|
|`_current_branch_name`|fn|priv|1342-1354|def _current_branch_name()|
|`_ref_exists`|fn|priv|1358-1367|def _ref_exists(ref_name)|
|`_local_branch_exists`|fn|priv|1371-1374|def _local_branch_exists(branch_name)|
|`_remote_branch_exists`|fn|priv|1378-1381|def _remote_branch_exists(branch_name)|
|`_ensure_release_prerequisites`|fn|priv|1384-1411|def _ensure_release_prerequisites()|
|`_bump_semver_version`|fn|priv|1416-1434|def _bump_semver_version(current_version, level)|
|`_run_release_step`|fn|priv|1440-1460|def _run_release_step(level, step_name, action)|
|`_execute_release_flow`|fn|priv|1465-1507|def _execute_release_flow(level, changelog_args=None)|
|`_run_release_command`|fn|priv|1512-1527|def _run_release_command(level, changelog_args=None)|
|`_run_reset_with_help`|fn|priv|1532-1539|def _run_reset_with_help(base_args, extra)|
|`_reject_extra_arguments`|fn|priv|1544-1550|def _reject_extra_arguments(extra, alias)|
|`_parse_release_flags`|fn|priv|1555-1573|def _parse_release_flags(extra, alias)|
|`_prepare_commit_message`|fn|priv|1578-1588|def _prepare_commit_message(extra, alias)|
|`_build_conventional_message`|fn|priv|1594-1608|def _build_conventional_message(kind: str, extra, alias: ...|
|`_run_conventional_commit`|fn|priv|1614-1619|def _run_conventional_commit(kind: str, alias: str, extra)|
|`_execute_commit`|fn|priv|1625-1654|def _execute_commit(message, alias, allow_amend=True)|
|`upgrade_self`|fn|pub|1657-1670|def upgrade_self()|
|`remove_self`|fn|pub|1673-1676|def remove_self()|
|`cmd_aa`|fn|pub|1680-1687|def cmd_aa(extra)|
|`cmd_ra`|fn|pub|1691-1714|def cmd_ra(extra)|
|`cmd_ar`|fn|pub|1718-1731|def cmd_ar(extra)|
|`cmd_br`|fn|pub|1735-1738|def cmd_br(extra)|
|`cmd_bd`|fn|pub|1742-1745|def cmd_bd(extra)|
|`cmd_ck`|fn|pub|1749-1752|def cmd_ck(extra)|
|`_ensure_commit_ready`|fn|priv|1756-1769|def _ensure_commit_ready(alias)|
|`cmd_cm`|fn|pub|1773-1778|def cmd_cm(extra)|
|`cmd_wip`|fn|pub|1782-1794|def cmd_wip(extra)|
|`cmd_release`|fn|pub|1798-1820|def cmd_release(extra)|
|`cmd_new`|fn|pub|1824-1827|def cmd_new(extra)|
|`cmd_refactor`|fn|pub|1831-1834|def cmd_refactor(extra)|
|`cmd_fix`|fn|pub|1838-1841|def cmd_fix(extra)|
|`cmd_change`|fn|pub|1845-1848|def cmd_change(extra)|
|`cmd_docs`|fn|pub|1852-1855|def cmd_docs(extra)|
|`cmd_style`|fn|pub|1859-1862|def cmd_style(extra)|
|`cmd_revert`|fn|pub|1866-1869|def cmd_revert(extra)|
|`cmd_misc`|fn|pub|1873-1876|def cmd_misc(extra)|
|`cmd_cover`|fn|pub|1880-1883|def cmd_cover(extra)|
|`cmd_co`|fn|pub|1887-1890|def cmd_co(extra)|
|`cmd_de`|fn|pub|1894-1897|def cmd_de(extra)|
|`cmd_di`|fn|pub|1901-1904|def cmd_di(extra)|
|`cmd_diyou`|fn|pub|1908-1911|def cmd_diyou(extra)|
|`cmd_dime`|fn|pub|1915-1918|def cmd_dime(extra)|
|`cmd_ed`|fn|pub|1922-1931|def cmd_ed(extra)|
|`cmd_fe`|fn|pub|1935-1938|def cmd_fe(extra)|
|`cmd_feall`|fn|pub|1942-1945|def cmd_feall(extra)|
|`cmd_gp`|fn|pub|1949-1952|def cmd_gp(extra)|
|`cmd_gr`|fn|pub|1956-1959|def cmd_gr(extra)|
|`cmd_str`|fn|pub|1963-1992|def cmd_str(extra)|
|`cmd_lb`|fn|pub|1996-1999|def cmd_lb(extra)|
|`cmd_lg`|fn|pub|2003-2016|def cmd_lg(extra)|
|`cmd_lh`|fn|pub|2020-2023|def cmd_lh(extra)|
|`cmd_ll`|fn|pub|2027-2039|def cmd_ll(extra)|
|`cmd_lm`|fn|pub|2043-2046|def cmd_lm(extra)|
|`cmd_lt`|fn|pub|2050-2053|def cmd_lt(extra)|
|`cmd_me`|fn|pub|2057-2060|def cmd_me(extra)|
|`cmd_pl`|fn|pub|2064-2067|def cmd_pl(extra)|
|`cmd_pt`|fn|pub|2071-2074|def cmd_pt(extra)|
|`cmd_pu`|fn|pub|2078-2081|def cmd_pu(extra)|
|`cmd_rf`|fn|pub|2085-2088|def cmd_rf(extra)|
|`cmd_rmtg`|fn|pub|2092-2102|def cmd_rmtg(extra)|
|`cmd_rmloc`|fn|pub|2106-2109|def cmd_rmloc(extra)|
|`cmd_rmstg`|fn|pub|2113-2116|def cmd_rmstg(extra)|
|`cmd_rmunt`|fn|pub|2120-2123|def cmd_rmunt(extra)|
|`cmd_rs`|fn|pub|2127-2130|def cmd_rs(extra)|
|`cmd_rssft`|fn|pub|2134-2137|def cmd_rssft(extra)|
|`cmd_rsmix`|fn|pub|2141-2144|def cmd_rsmix(extra)|
|`cmd_rshrd`|fn|pub|2148-2151|def cmd_rshrd(extra)|
|`cmd_rsmrg`|fn|pub|2155-2158|def cmd_rsmrg(extra)|
|`cmd_rskep`|fn|pub|2162-2165|def cmd_rskep(extra)|
|`cmd_st`|fn|pub|2169-2172|def cmd_st(extra)|
|`cmd_tg`|fn|pub|2176-2179|def cmd_tg(extra)|
|`cmd_unstg`|fn|pub|2183-2186|def cmd_unstg(extra)|
|`cmd_ver`|fn|pub|2190-2208|def cmd_ver(extra)|
|`cmd_chver`|fn|pub|2212-2282|def cmd_chver(extra)|
|`cmd_major`|fn|pub|2286-2290|def cmd_major(extra)|
|`cmd_minor`|fn|pub|2294-2298|def cmd_minor(extra)|
|`cmd_patch`|fn|pub|2302-2306|def cmd_patch(extra)|
|`cmd_changelog`|fn|pub|2310-2342|def cmd_changelog(extra)|
|`COMMANDS`|var|pub|2345||
|`print_command_help`|fn|pub|2410-2416|def print_command_help(name, width=None)|
|`print_all_help`|fn|pub|2419-2453|def print_all_help()|
|`main`|fn|pub|2458-2508|def main(argv=None, *, check_updates: bool = True)|

