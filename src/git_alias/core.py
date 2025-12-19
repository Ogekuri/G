#!/usr/bin/env python3
"""Portable implementation of the user's git aliases."""

import argparse
import json
import os
import re
import shlex
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse

CONFIG_FILENAME = ".g.conf"

DEFAULT_VER_RULES = [
    ("README.md", r'\s*"(\d+\.\d+\.\d+)"\s*'),
    ("src/**/*.py", r'__version__\s*=\s*["\']?(\d+\.\d+\.\d+)["\']?'),
    ("pyproject.toml", r'\bversion\s*=\s*"(\d+\.\d+\.\d+)"'),
]

DEFAULT_CONFIG = {
    "master": "master",
    "develop": "develop",
    "work": "work",
    "editor": "edit",
    "default_module": "core",
    "ver_rules": json.dumps(DEFAULT_VER_RULES),
}

CONFIG = DEFAULT_CONFIG.copy()
BRANCH_KEYS = ("master", "develop", "work")
MANAGEMENT_HELP = [
    ("--help", "Print the full help screen or the help text of a specific alias."),
    ("--write-config", "Generate the .g.conf file in the repository root with default values."),
    ("--upgrade", "Reinstall git-alias via uv tool install."),
    ("--remove", "Uninstall git-alias using uv tool uninstall."),
]


# Restituisce un valore di configurazione con fallback ai default.
def get_config_value(name):
    """Retrieve a configuration value with fallback to defaults."""
    return CONFIG.get(name, DEFAULT_CONFIG[name])


# Restituisce il nome di branch configurato per la chiave richiesta.
def get_branch(name):
    """Return the configured name for the requested branch key."""
    if name not in BRANCH_KEYS:
        raise KeyError(f"Unknown branch key {name}")
    return get_config_value(name)


# Recupera il comando di editor definito nella configurazione.
def get_editor():
    """Return the configured editor command."""
    return get_config_value("editor")


# Carica le coppie wildcard/regexp definite nel file di configurazione.
def _load_config_rules(key, fallback):
    """Load wildcard/regex rule pairs from configuration."""
    raw_value = CONFIG.get(key, DEFAULT_CONFIG[key])
    parsed = raw_value if isinstance(raw_value, list) else None
    if parsed is None:
        try:
            parsed = json.loads(raw_value)
        except (json.JSONDecodeError, TypeError) as exc:
            print(f"Ignoring invalid JSON for {key}: {exc}", file=sys.stderr)
            return list(fallback)
    if not isinstance(parsed, list):
        print(f"Ignoring non-list value for {key}", file=sys.stderr)
        return list(fallback)
    rules = []
    for entry in parsed:
        pattern = regex = None
        if isinstance(entry, dict):
            pattern = entry.get("pattern") or entry.get("glob")
            regex = entry.get("regex")
        elif isinstance(entry, (list, tuple)) and len(entry) >= 2:
            pattern, regex = entry[0], entry[1]
        if isinstance(pattern, str):
            pattern = pattern.strip()
        else:
            pattern = None
        if isinstance(regex, str):
            regex = regex.strip()
        else:
            regex = None
        if pattern and regex:
            rules.append((pattern, regex))
    return rules if rules else list(fallback)


# Restituisce le regole usate per rilevare le versioni nei file.
def get_version_rules():
    """Return the configured wildcard/regex pairs for version scanning."""
    return _load_config_rules("ver_rules", DEFAULT_VER_RULES)


# Individua la radice del repository git corrente.
def get_git_root():
    """Return the git repository root or the current working directory."""
    try:
        result = _run_checked(
            ["git", "rev-parse", "--show-toplevel"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        location = result.stdout.strip()
        if location:
            return Path(location)
    except CommandExecutionError:
        pass
    return Path.cwd()


# Calcola il percorso del file di configurazione .g.conf.
def get_config_path(root=None):
    """Return the expected path of the configuration file."""
    base = Path(root) if root is not None else get_git_root()
    return base / CONFIG_FILENAME


# Carica nella memoria le impostazioni definite in .g.conf.
def load_cli_config(root=None):
    """Load branch names and editor command from the repository configuration file."""
    CONFIG.update(DEFAULT_CONFIG)
    config_path = get_config_path(root)
    if not config_path.exists():
        return config_path
    try:
        for raw_line in config_path.read_text().splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = [part.strip() for part in line.split("=", 1)]
            if key in DEFAULT_CONFIG and value:
                CONFIG[key] = value
    except OSError as exc:
        print(f"Unable to read {config_path}: {exc}", file=sys.stderr)
    return config_path


# Scrive il file di configurazione con i valori di default.
def write_default_config(root=None):
    """Write the default configuration file in the repository root."""
    config_path = get_config_path(root)
    keys = ("master", "develop", "work", "editor", "default_module", "ver_rules")
    lines = [f"{key}={DEFAULT_CONFIG[key]}" for key in keys]
    config_path.write_text("\n".join(lines) + "\n")
    print(f"Configuration written to {config_path}")
    return config_path


# Parsa la stringa dell'editor e restituisce il comando base.
def _editor_base_command():
    """Return the configured editor command as a list of arguments."""
    raw_value = get_editor() or DEFAULT_CONFIG["editor"]
    try:
        parts = shlex.split(raw_value)
    except ValueError as exc:
        print(
            f"Ignoring invalid editor command '{raw_value}': {exc}. Falling back to '{DEFAULT_CONFIG['editor']}'",
            file=sys.stderr,
        )
        parts = [DEFAULT_CONFIG["editor"]]
    if not parts:
        parts = [DEFAULT_CONFIG["editor"]]
    return parts


# Esegue l'editor configurato con gli argomenti specificati.
def run_editor_command(args):
    """Execute the configured editor command with additional arguments."""
    return run_command(_editor_base_command() + list(args))

HELP_TEXTS = {
    "aa": "Add all file changes/added to stage area for commit.",
    "ar": "Archive the configured master branch as zip file. Use tag as filename.",
    "bd": "Delete a local branch: git bd '<branch>'.",
    "br": "Create a new branch.",
    "chver": "Change the project version to the provided semantic version.",
    "changelog": "Generate CHANGELOG.md from conventional commits (supports --include-unreleased, --force-write, --print-only).",
    "ck": "Check differences.",
    "cm": "Standard commit with staging/worktree validation: git cm '<message>'.",
    "co": "Checkout a specific branch: git co '<branch>'.",
    "de": "Print last tagged commit details.",
    "di": "Discard current changes on file: git di '<filename>'",
    "dime": "Discard merge changes in favor of their files.",
    "diyou": "Discard merge changes in favor of your files.",
    "ed": "Edit a file. Syntax: git ed <filename>.",
    "fe": "Fetch new data of current branch from origin.",
    "feall": "Fetch new data from origin for all branch.",
    "gp": "Open git commits graph (Git K).",
    "gr": "Open git tags graph (Git K).",
    "lb": "Print all branches.",
    "lg": "Print commit history.",
    "lh": "Print last commit details.",
    "ll": "Print latest full commit hash.",
    "lm": "Print all merges.",
    "lt": "Print all tags.",
    "major": "Release a new major version from the work branch.",
    "minor": "Release a new minor version from the work branch.",
    "new": "Conventional commit new(module): description.",
    "fix": "Conventional commit fix(module): description.",
    "change": "Conventional commit change(module): description.",
    "docs": "Conventional commit docs(module): description.",
    "style": "Conventional commit style(module): description.",
    "revert": "Conventional commit revert(module): description.",
    "misc": "Conventional commit misc(module): description.",
    "me": "Merge",
    "pl": "Pull (fetch + merge FETCH_HEAD) from origin on current branch.",
    "pt": "Push all new tags to origin.",
    "pu": "Push current branch to origin (add upstream (tracking) reference for pull).",
    "patch": "Release a new patch version from the work branch.",
    "ra": "Remove all staged files and return them to the working tree (inverse of aa).",
    "release": "Create a release commit using the detected project version.",
    "rf": "Print changes on HEAD reference.",
    "rmloc": "Remove changed files from the working tree.",
    "rmstg": "Remove staged files from index tree.",
    "rmtg": "Remove a tag on current branch and from origin.",
    "rmunt": "Remove untracked files from the working tree.",
    "rs": "Reset current branch to HEAD (--hard).",
    "rshrd": "Hard reset alias (--hard).",
    "rskep": "Keep reset alias (--keep).",
    "rsmix": "Mixed reset alias (--mixed).",
    "rsmrg": "Merge reset alias (--merge).",
    "rssft": "Soft reset alias (--soft).",
    "st": "Print current GIT status.",
    "tg": "Create a new annotate tag. Syntax: git tg <description> <tag>.",
    "unstg": "Un-stage a file from commit: git unstg '<filename>'. Unstage all files with: git unstg *.",
    "wip": "Commit work in progress with an automatic message and the same checks as cm.",
    "ver": "Verify version consistency across configured files.",
}

RESET_HELP = """

 Reset commands help screen

 default mode = '--mixed'

 working - working tree
 index   - staging area ready to commit
 HEAD    - latest commit
 target  - example: origin/master

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  A       B     C    D     --soft   A       B     D
                           --mixed  A       D     D
                           --hard   D       D     D
                           --merge  (disallowed)
                           --keep   (disallowed)

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  A       B     C    C     --soft   A       B     C
                           --mixed  A       C     C
                           --hard   C       C     C
                           --merge  (disallowed)
                           --keep   A       C     C

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  B       B     C    D     --soft   B       B     D
                           --mixed  B       D     D
                           --hard   D       D     D
                           --merge  D       D     D
                           --keep   (disallowed)

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  B       B     C    C     --soft   B       B     C
                           --mixed  B       C     C
                           --hard   C       C     C
                           --merge  C       C     C
                           --keep   B       C     C

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  B       C     C    D     --soft   B       C     D
                           --mixed  B       D     D
                           --hard   D       D     D
                           --merge  (disallowed)
                           --keep   (disallowed)

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  B       C     C    C     --soft   B       C     C
                           --mixed  B       C     C
                           --hard   C       C     C
                           --merge  B       C     C
                           --keep   B       C     C

 The following tables show what happens when there are unmerged entries:
 X means any state and U means an unmerged index.

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  X       U     A    B     --soft   (disallowed)
                           --mixed  X       B     B
                           --hard   B       B     B
                           --merge  B       B     B
                           --keep   (disallowed)

 working index HEAD target         working index HEAD
 ----------------------------------------------------
  X       U     A    A     --soft   (disallowed)
                           --mixed  X       A     A
                           --hard   A       A     A
                           --merge  A       A     A
                           --keep   (disallowed)

"""

RESET_HELP_COMMANDS = {"rshrd", "rskep", "rsmix", "rsmrg", "rssft"}


# Converte la sequenza di argomenti extra in una lista espandibile.
def _to_args(extra):
    return list(extra) if extra else []


# Rappresenta un errore emesso da un processo esterno.
class CommandExecutionError(RuntimeError):
    def __init__(self, exc: subprocess.CalledProcessError):
        self.cmd = exc.cmd
        self.returncode = exc.returncode
        self.stdout = exc.stdout
        self.stderr = exc.stderr
        message = self._format_message()
        super().__init__(message)

    def _format_message(self) -> str:
        text = self._decode_stream(self.stderr).strip()
        if text:
            return text
        cmd_display = ""
        if isinstance(self.cmd, (list, tuple)):
            cmd_display = " ".join(str(part) for part in self.cmd)
        elif self.cmd:
            cmd_display = str(self.cmd)
        return f"Command '{cmd_display}' failed with exit code {self.returncode}"

    @staticmethod
    def _decode_stream(data) -> str:
        if data is None:
            return ""
        if isinstance(data, bytes):
            try:
                return data.decode("utf-8")
            except UnicodeDecodeError:
                return data.decode("utf-8", errors="replace")
        return str(data)


# Esegue un comando esterno e converte gli errori in CommandExecutionError.
def _run_checked(*popenargs, **kwargs):
    kwargs.setdefault("check", True)
    try:
        return subprocess.run(*popenargs, **kwargs)
    except subprocess.CalledProcessError as exc:
        raise CommandExecutionError(exc) from None


# Eccezione dedicata alla rilevazione della versione corrente.
class VersionDetectionError(RuntimeError):
    pass


# Eccezione dedicata al flusso dei rilasci automatici.
class ReleaseError(RuntimeError):
    pass


# Invia un comando git con argomenti principali e supplementari nella directory indicata.
def run_git_cmd(base_args, extra=None, cwd=None, **kwargs):
    full = ["git"] + list(base_args) + _to_args(extra)
    return _run_checked(full, cwd=cwd, **kwargs)


# Esegue git e restituisce l'output come stringa per usi interni.
def capture_git_output(base_args, cwd=None):
    result = _run_checked(["git"] + list(base_args), cwd=cwd, stdout=subprocess.PIPE, text=True)
    return result.stdout.strip()


# Invoca un comando esterno con la sintassi fornita.
def run_command(cmd, cwd=None):
    return _run_checked(cmd, cwd=cwd)


# Esegue comandi git e restituisce l'output testuale.
def run_git_text(args, cwd=None, check=True):
    try:
        proc = _run_checked(
            ["git", *args],
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=check,
        )
    except CommandExecutionError as exc:
        message = CommandExecutionError._decode_stream(exc.stderr).strip()
        if not message:
            message = f"git {' '.join(args)} failed"
        raise RuntimeError(message) from None
    return proc.stdout.strip()


# Esegue una pipeline nella shell quando serve costruire comandi complessi.
def run_shell(command, cwd=None):
    return _run_checked(command, shell=True, cwd=cwd)


# Esegue comandi git e restituisce l'output testuale.
def run_git_text(args, cwd=None, check=True):
    try:
        proc = _run_checked(
            ["git", *args],
            cwd=cwd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=check,
        )
    except CommandExecutionError as exc:
        message = CommandExecutionError._decode_stream(exc.stderr).strip()
        if not message:
            message = f"git {' '.join(args)} failed"
        raise RuntimeError(message) from None
    return proc.stdout.strip()


# Recupera le linee di stato porcelain del repository.
def _git_status_lines():
    """Return the porcelain status lines without trimming leading spaces."""
    proc = _run_checked(
        ["git", "status", "--porcelain"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )
    if proc.returncode != 0:
        return []
    return proc.stdout.splitlines()


# Determina se esistono modifiche non ancora nello staging.
def has_unstaged_changes(status_lines=None):
    """Return True when there are worktree changes waiting to be staged."""
    lines = status_lines if status_lines is not None else _git_status_lines()
    for line in lines:
        if not line:
            continue
        if line.startswith("??"):
            return True
        if len(line) > 1 and line[1] != " ":
            return True
    return False


# Verifica la presenza di elementi già pronti nello staging.
def has_staged_changes(status_lines=None):
    """Return True when there are staged entries ready to be committed."""
    lines = status_lines if status_lines is not None else _git_status_lines()
    for line in lines:
        if not line or line.startswith("??"):
            continue
        if line[0] != " ":
            return True
    return False


_REMOTE_REFS_UPDATED = False
WIP_MESSAGE_RE = re.compile(r"^wip: work in progress\.$")


# Aggiorna una sola volta i riferimenti remoti usando git.
def _refresh_remote_refs():
    """Update remote references once per process to inform pull diagnostics."""
    global _REMOTE_REFS_UPDATED
    if _REMOTE_REFS_UPDATED:
        return
    try:
        run_git_cmd(["remote", "-v", "update"])
    except CommandExecutionError as exc:
        print(f"Unable to update remote references: {exc}", file=sys.stderr)
        return
    _REMOTE_REFS_UPDATED = True


# Calcola la divergenza tra il branch locale e quello remoto.
def _branch_remote_divergence(branch_key, remote="origin"):
    """Return a tuple (local_ahead, remote_ahead) for the requested branch key."""
    _refresh_remote_refs()
    branch = get_branch(branch_key)
    upstream = f"{remote}/{branch}"
    try:
        counts = run_git_text(["rev-list", "--left-right", "--count", f"{branch}...{upstream}"])
    except RuntimeError:
        return (0, 0)
    parts = counts.strip().split()
    if len(parts) < 2:
        return (0, 0)
    try:
        local_ahead = int(parts[0])
        remote_ahead = int(parts[1])
    except ValueError:
        return (0, 0)
    return (local_ahead, remote_ahead)


# Indica se il branch remoto ha commit non ancora recuperati.
def has_remote_branch_updates(branch_key, remote="origin"):
    """Return True if the remote tracking branch contains commits not yet fetched locally."""
    _, remote_ahead = _branch_remote_divergence(branch_key, remote=remote)
    return remote_ahead > 0


# Verifica la presenza di aggiornamenti remoti per develop.
def has_remote_develop_updates():
    """Shortcut that reports pending updates for the configured develop branch."""
    return has_remote_branch_updates("develop")


# Verifica la presenza di aggiornamenti remoti per master.
def has_remote_master_updates():
    """Shortcut that reports pending updates for the configured master branch."""
    return has_remote_branch_updates("master")


# Restituisce il messaggio dell'ultima commit locale.
def _head_commit_message():
    """Return the latest commit subject or an empty string on failure."""
    try:
        return run_git_text(["log", "-1", "--pretty=%s"]).strip()
    except RuntimeError:
        return ""


# Ritorna l'hash della commit HEAD del repository.
def _head_commit_hash():
    """Return the hash of HEAD or an empty string when unavailable."""
    try:
        return run_git_text(["rev-parse", "HEAD"]).strip()
    except RuntimeError:
        return ""


# Controlla se una commit è presente nel branch indicato.
def _commit_exists_in_branch(commit_hash, branch_name):
    """Return True if commit_hash is contained in branch_name."""
    if not commit_hash or not branch_name:
        return False
    proc = _run_checked(
        ["git", "merge-base", "--is-ancestor", commit_hash, branch_name],
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return proc.returncode == 0


# Stabilisce se bisogna ammendare la commit WIP corrente.
def _should_amend_existing_commit():
    """Determine if the current HEAD WIP commit should be amended."""
    message = _head_commit_message()
    if not (message and WIP_MESSAGE_RE.match(message)):
        return (False, "HEAD is not a WIP commit.")
    commit_hash = _head_commit_hash()
    if not commit_hash:
        return (False, "Unable to determine the HEAD commit hash.")
    develop_branch = get_branch("develop")
    master_branch = get_branch("master")
    if _commit_exists_in_branch(commit_hash, develop_branch):
        return (False, f"The last WIP commit is already contained in {develop_branch}.")
    if _commit_exists_in_branch(commit_hash, master_branch):
        return (False, f"The last WIP commit is already contained in {master_branch}.")
    return (True, "HEAD WIP commit is still pending locally.")


# Verifica se il processo si trova all'interno di un repository git.
def is_inside_git_repo():
    try:
        output = run_git_text(["rev-parse", "--is-inside-work-tree"])
    except RuntimeError:
        return False
    return output.strip().lower() == "true"


@dataclass
class TagInfo:
    name: str
    iso_date: str
    object_name: str


DELIM = "\x1f"
RECORD = "\x1e"
_CONVENTIONAL_RE = re.compile(
    r"^(?P<type>new|fix|change|docs|style|revert|misc)"
    r"(?:\((?P<scope>[^)]+)\))?(?P<breaking>!)?:\s+(?P<desc>.+)$",
    re.IGNORECASE,
)
_MODULE_PREFIX_RE = re.compile(r"^(?P<module>[A-Za-z0-9_]+):\s*(?P<body>.*)$")
_SEMVER_TAG_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")
SECTION_EMOJI = {
    "Features": "⛰️",
    "Bug Fixes": "🐛",
    "Changes": "🚜",
    "Documentation": "📚",
    "Styling": "🎨",
    "Miscellaneous Tasks": "⚙️",
    "Revert": "◀️",
}


# Ottiene i tag semantici ordinati per data di creazione.
def list_tags_sorted_by_date(repo_root: Path, merged_ref: Optional[str] = None) -> List[TagInfo]:
    fmt = f"%(refname:strip=2){DELIM}%(creatordate:short){DELIM}%(objectname)"
    args = ["for-each-ref", "--sort=creatordate", f"--format={fmt}"]
    if merged_ref:
        args.extend(["--merged", merged_ref])
    args.append("refs/tags")
    output = run_git_text(args, cwd=repo_root, check=False)
    if not output:
        return []
    tags: List[TagInfo] = []
    for line in output.splitlines():
        parts = line.split(DELIM)
        if len(parts) != 3:
            continue
        name, date_s, obj = parts
        if not _SEMVER_TAG_RE.match(name):
            continue
        tags.append(TagInfo(name=name, iso_date=date_s or "unknown-date", object_name=obj))
    return tags


# Estrae i soggetti dei commit in un intervallo di log.
def git_log_subjects(repo_root: Path, rev_range: str) -> List[str]:
    fmt = f"%s{RECORD}"
    out = run_git_text(
        ["log", "--no-merges", f"--pretty=format:{fmt}", rev_range],
        cwd=repo_root,
        check=False,
    )
    if not out:
        return []
    return [x.strip() for x in out.split(RECORD) if x.strip()]


# Classifica un soggetto di commit secondo le categorie supportate.
def categorize_commit(subject: str) -> Tuple[Optional[str], str]:
    match = _CONVENTIONAL_RE.match(subject.strip())
    if not match:
        return (None, "")
    ctype = match.group("type").lower()
    scope = match.group("scope")
    desc = match.group("desc").strip()
    scope_text = f"*({scope})* " if scope else ""
    line = f"- {scope_text}{desc}"
    mapping = {
        "new": "Features",
        "fix": "Bug Fixes",
        "change": "Changes",
        "docs": "Documentation",
        "style": "Styling",
        "revert": "Revert",
        "misc": "Miscellaneous Tasks",
    }
    section = mapping.get(ctype)
    return (section, line) if section else (None, "")


# Estrae la versione di rilascio da un commit new(core): release version: X.Y.Z.
def _extract_release_version(subject: str) -> Optional[str]:
    match = re.search(r"release version:\s+(\d+\.\d+\.\d+)", subject, re.IGNORECASE)
    if not match:
        return None
    return match.group(1)


# Genera la sezione di changelog relativa a un intervallo di commit.
def generate_section_for_range(repo_root: Path, title: str, date_s: str, rev_range: str, expected_version: Optional[str] = None) -> Optional[str]:
    subjects = git_log_subjects(repo_root, rev_range)
    buckets: Dict[str, List[str]] = defaultdict(list)
    for subj in subjects:
        release_version = _extract_release_version(subj)
        if expected_version and release_version and release_version != expected_version:
            continue
        section, line = categorize_commit(subj)
        if section and line:
            buckets[section].append(line)
    if not any(buckets.values()):
        return None
    lines: List[str] = []
    lines.append(f"## {title} - {date_s}")
    order = [
        "Features",
        "Bug Fixes",
        "Changes",
        "Documentation",
        "Styling",
        "Miscellaneous Tasks",
        "Revert",
    ]
    for sec in order:
        entries = buckets.get(sec, [])
        if entries:
            emoji = SECTION_EMOJI.get(sec, "")
            header = f"### {emoji}  {sec}".rstrip()
            lines.append(header)
            lines.extend(entries)
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


# Deriva l'URL base del remote origin per i link di confronto.
def _canonical_origin_base(repo_root: Path) -> Optional[str]:
    url = run_git_text(["remote", "get-url", "origin"], cwd=repo_root, check=False).strip()
    if not url:
        return None
    if url.startswith("git@"):
        host_repo = url.split(":", 1)[1]
        host = url.split("@", 1)[1].split(":", 1)[0]
        base = f"https://{host}/" + host_repo
    else:
        base = url
    if base.endswith(".git"):
        base = base[:-4]
    parsed = urlparse(base)
    if not parsed.scheme or not parsed.netloc:
        return None
    return base


# Costruisce l'URL di confronto o di release per un tag.
def get_origin_compare_url(base_url: Optional[str], prev_tag: Optional[str], tag: str) -> Optional[str]:
    if not base_url:
        return None
    if prev_tag:
        return f"{base_url}/compare/{prev_tag}..{tag}"
    return f"{base_url}/releases/tag/{tag}"


# Compone la sezione History con i riferimenti di confronto.
def build_history_section(repo_root: Path, tags: List[TagInfo], include_unreleased: bool) -> Optional[str]:
    base = _canonical_origin_base(repo_root)
    if not base:
        return None
    lines = ["# History"]
    prev: Optional[str] = None
    for tag in tags:
        compare = get_origin_compare_url(base, prev, tag.name)
        if compare:
            lines.append(f"[{tag.name.lstrip('v')}]: {compare}")
        prev = tag.name
    if include_unreleased and tags:
        compare = get_origin_compare_url(base, tags[-1].name, "HEAD")
        if compare:
            lines.append(f"[unreleased]: {compare}")
    return "\n".join(lines).rstrip() + "\n"


# Assembla il documento completo del changelog.
def generate_changelog_document(repo_root: Path, include_unreleased: bool) -> str:
    tags = list_tags_sorted_by_date(repo_root)
    history_tags = list_tags_sorted_by_date(repo_root, merged_ref="HEAD")
    origin_base = _canonical_origin_base(repo_root)
    lines: List[str] = ["# Changelog", ""]
    release_sections: List[str] = []
    if include_unreleased:
        rev_range = f"{tags[-1].name}..HEAD" if tags else "HEAD"
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        section = generate_section_for_range(repo_root, "Unreleased", today, rev_range)
        if section:
            lines.append(section)
    if tags:
        prev: Optional[str] = None
        for tag in tags:
            rev_range = tag.name if prev is None else f"{prev}..{tag.name}"
            display = tag.name.lstrip("v")
            compare_url = get_origin_compare_url(origin_base, prev, tag.name)
            title = f"[{display}]({compare_url})" if compare_url else display
            section = generate_section_for_range(repo_root, title, tag.iso_date, rev_range, expected_version=display)
            if section:
                release_sections.append(section)
            prev = tag.name
    else:
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        section = generate_section_for_range(repo_root, "Unreleased", today, "HEAD")
        if section:
            release_sections.append(section)
    if release_sections:
        lines.extend(reversed(release_sections))
    history = build_history_section(repo_root, history_tags, include_unreleased)
    if history:
        lines.append("")
        lines.append(history)
    return "\n".join(lines).rstrip() + "\n"


# Trova i file che corrispondono alla wildcard di versione.
def _collect_version_files(root, pattern):
    """Return an ordered list of files that match the provided glob pattern."""
    files = []
    seen = set()
    trimmed = (pattern or "").strip()
    if not trimmed:
        return files
    for path in root.rglob(trimmed):
        if path.is_file():
            resolved = path.resolve()
            if resolved not in seen:
                seen.add(resolved)
                files.append(path)
    return files


# Itera tutte le versioni estratte tramite le regex fornite.
def _iter_versions_in_text(text, compiled_regexes):
    """Yield every version string extracted by the compiled regex list."""
    for regex in compiled_regexes:
        for match in regex.finditer(text):
            if match.groups():
                for group in match.groups():
                    if group:
                        yield group
                        break
            else:
                yield match.group(0)


# Determina la versione canonica analizzando i file configurati.
def _determine_canonical_version(root: Path, rules):
    canonical = None
    canonical_file = None
    for pattern, expression in rules:
        files = _collect_version_files(root, pattern)
        if not files:
            continue
        try:
            compiled = re.compile(expression)
        except re.error as exc:
            print(f"Ignoring invalid regex '{expression}' for pattern '{pattern}': {exc}", file=sys.stderr)
            continue
        for file_path in files:
            try:
                text = file_path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                text = file_path.read_text(encoding="utf-8", errors="ignore")
            except OSError as exc:
                print(f"Unable to read {file_path}: {exc}", file=sys.stderr)
                continue
            for version in _iter_versions_in_text(text, [compiled]):
                if canonical is None:
                    canonical = version
                    canonical_file = file_path
                elif version != canonical:
                    raise VersionDetectionError(
                        f"Version mismatch between {canonical_file} ({canonical}) and {file_path} ({version})"
                    )
    if canonical is None:
        raise VersionDetectionError("No version string matched the configured rule list.")
    return canonical


# Analizza una stringa di versione semantica e restituisce la tupla numerica.
def _parse_semver_tuple(text):
    match = SEMVER_RE.match((text or "").strip())
    if not match:
        return None
    return tuple(int(match.group(i)) for i in range(1, 4))


# Sostituisce le occorrenze di versione nel testo in base alle regex fornite.
def _replace_versions_in_text(text, compiled_regex, replacement):
    last_index = 0
    pieces = []
    count = 0
    for match in compiled_regex.finditer(text):
        span = match.span(1) if match.groups() else match.span(0)
        pieces.append(text[last_index:span[0]])
        pieces.append(replacement)
        last_index = span[1]
        count += 1
    if count == 0:
        return text, 0
    pieces.append(text[last_index:])
    return "".join(pieces), count


# Determina il nome del branch corrente del repository.
def _current_branch_name():
    """Return the current branch name or raise an error when detached."""
    proc = _run_checked(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    branch = proc.stdout.strip()
    if not branch or branch == "HEAD":
        raise ReleaseError("Release commands require an active branch head.")
    return branch


# Verifica l'esistenza di un riferimento git locale.
def _ref_exists(ref_name):
    """Return True if the provided ref exists locally."""
    proc = subprocess.run(
        ["git", "show-ref", "--verify", "--quiet", ref_name],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return proc.returncode == 0


# Verifica che un branch locale esista.
def _local_branch_exists(branch_name):
    """Return True when the requested local branch exists."""
    return _ref_exists(f"refs/heads/{branch_name}")


# Verifica che il branch remoto esista tra i riferimenti locali.
def _remote_branch_exists(branch_name):
    """Return True when the remote branch exists locally under origin."""
    return _ref_exists(f"refs/remotes/origin/{branch_name}")


# Assicura che i prerequisiti per i rilasci siano soddisfatti.
def _ensure_release_prerequisites():
    """Validate branch layout, remotes and working tree cleanliness."""
    master_branch = get_branch("master")
    develop_branch = get_branch("develop")
    work_branch = get_branch("work")
    missing_local = [name for name in (master_branch, develop_branch, work_branch) if not _local_branch_exists(name)]
    if missing_local:
        joined = ", ".join(missing_local)
        raise ReleaseError(f"Unable to run release command: missing local branches {joined}.")
    _refresh_remote_refs()
    missing_remote = [name for name in (master_branch, develop_branch) if not _remote_branch_exists(name)]
    if missing_remote:
        joined = ", ".join(missing_remote)
        raise ReleaseError(f"Unable to run release command: missing remote branches {joined}.")
    if has_remote_branch_updates("master"):
        raise ReleaseError(f"Remote branch {master_branch} has pending updates. Please pull them first.")
    if has_remote_branch_updates("develop"):
        raise ReleaseError(f"Remote branch {develop_branch} has pending updates. Please pull them first.")
    current_branch = _current_branch_name()
    if current_branch != work_branch:
        raise ReleaseError(f"Release commands must be executed from the {work_branch} branch (current: {current_branch}).")
    status = _git_status_lines()
    if has_unstaged_changes(status):
        raise ReleaseError("Working tree changes detected. Clean or stage them before running a release.")
    if has_staged_changes(status):
        raise ReleaseError("Staging area is not empty. Complete or reset pending commits before running a release.")
    return {"master": master_branch, "develop": develop_branch, "work": work_branch}


# Calcola la prossima versione semantica in base al tipo di rilascio.
def _bump_semver_version(current_version, level):
    """Return the bumped semantic version string according to level."""
    parts = _parse_semver_tuple(current_version)
    if parts is None:
        raise ReleaseError(f"The current version '{current_version}' is not a valid semantic version.")
    major, minor, patch = parts
    if level == "major":
        major += 1
        minor = 0
        patch = 0
    elif level == "minor":
        minor += 1
        patch = 0
    elif level == "patch":
        patch += 1
    else:
        raise ReleaseError(f"Unsupported release level '{level}'.")
    return f"{major}.{minor}.{patch}"


# Esegue un singolo step del rilascio con logging.
def _run_release_step(step_name, action):
    """Execute a release step and report its outcome."""
    try:
        result = action()
        print(f"[release] Step '{step_name}' completed successfully.")
        return result
    except ReleaseError:
        raise
    except VersionDetectionError:
        raise
    except CommandExecutionError as exc:
        err_text = CommandExecutionError._decode_stream(exc.stderr).strip()
        message = err_text if err_text else str(exc)
        raise ReleaseError(f"[release] Step '{step_name}' failed: {message}") from None
    except SystemExit as exc:
        code = exc.code if isinstance(exc.code, int) else 1
        raise ReleaseError(f"[release] Step '{step_name}' failed: command exited with status {code}") from None
    except Exception as exc:
        raise ReleaseError(f"[release] Step '{step_name}' failed: {exc}") from None


# Esegue il flusso completo del rilascio.
def _execute_release_flow(level):
    """Perform the release workflow for the requested level."""
    branches = _ensure_release_prerequisites()
    rules = get_version_rules()
    if not rules:
        raise ReleaseError("No version rules configured. Cannot compute the next version.")
    root = get_git_root()
    current_version = _determine_canonical_version(root, rules)
    target_version = _bump_semver_version(current_version, level)
    release_message = f"release version: {target_version}"

    _run_release_step("update versions", lambda: cmd_chver([target_version]))
    _run_release_step("stage files", lambda: run_git_cmd(["add", "--all"]))
    _run_release_step("create release commit", lambda: cmd_release([]))
    _run_release_step("tag release", lambda: cmd_tg([release_message, f"v{target_version}"]))
    _run_release_step("regenerate changelog", lambda: cmd_changelog(["--force-write"]))
    _run_release_step("stage changelog", lambda: run_git_cmd(["add", "CHANGELOG.md"]))
    _run_release_step("amend release commit", lambda: run_git_cmd(["commit", "--amend", "--no-edit"]))
    _run_release_step(
        "retag release",
        lambda: run_git_cmd(["tag", "--force", "-a", f"v{target_version}", "-m", release_message]),
    )

    work_branch = branches["work"]
    develop_branch = branches["develop"]
    master_branch = branches["master"]

    _run_release_step("checkout develop", lambda: cmd_co([develop_branch]))
    _run_release_step("merge work into develop", lambda: cmd_me([work_branch]))
    _run_release_step("push develop", lambda: run_git_cmd(["push", "origin", develop_branch]))
    _run_release_step("checkout master", lambda: cmd_co([master_branch]))
    _run_release_step("merge develop into master", lambda: cmd_me([develop_branch]))
    _run_release_step("push master", lambda: run_git_cmd(["push", "origin", master_branch]))
    _run_release_step("return to work", lambda: cmd_co([work_branch]))
    _run_release_step("show release details", lambda: cmd_de([]))
    _run_release_step("push tags", lambda: cmd_pt([]))
    print(f"Release {target_version} completed successfully.")


# Gestisce le eccezioni del flusso di rilascio.
def _run_release_command(level):
    """Wrapper that executes the release flow and reports failures."""
    try:
        _execute_release_flow(level)
    except ReleaseError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
    except VersionDetectionError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
    except CommandExecutionError as exc:
        err_text = CommandExecutionError._decode_stream(exc.stderr).strip()
        if err_text:
            print(err_text, file=sys.stderr)
        sys.exit(exc.returncode or 1)


# Gestisce i comandi di reset mostrando l'help quando richiesto.
def _run_reset_with_help(base_args, extra):
    """Execute a reset command or show the reset help when --help is provided."""
    args = _to_args(extra)
    if "--help" in args:
        print(RESET_HELP.strip("\n"))
        return
    return run_git_cmd(base_args, args)


# Verifica che un alias non riceva argomenti posizionali.
def _reject_extra_arguments(extra, alias):
    """Ensure that no positional arguments are provided to the alias."""
    args = _to_args(extra)
    if args:
        print(f"git {alias} does not accept positional arguments.", file=sys.stderr)
        sys.exit(1)


# Prepara le operazioni di commit condivise tra gli alias cm e wip.
def _prepare_commit_message(extra, alias):
    args = _to_args(extra)
    if not args:
        print(f"git {alias} requires a message after the command.", file=sys.stderr)
        sys.exit(1)
    if args[0] == "--help":
        print_command_help(alias)
        sys.exit(0)
    return " ".join(args)


# Costruisce il messaggio convenzionale partendo dagli argomenti.
def _build_conventional_message(kind: str, extra, alias: str) -> str:
    text = _prepare_commit_message(extra, alias).strip()
    match = _MODULE_PREFIX_RE.match(text)
    if match:
        scope = match.group("module")
        body = match.group("body").strip()
    else:
        scope = get_config_value("default_module")
        body = text
    if not body:
        print(f"git {alias} requires text after the '<module>:' prefix to complete the message.", file=sys.stderr)
        sys.exit(1)
    return f"{kind}({scope}): {body}"


# Coordina l'esecuzione dei commit convenzionali condivisi.
def _run_conventional_commit(kind: str, alias: str, extra):
    message = _build_conventional_message(kind, extra, alias)
    _ensure_commit_ready(alias)
    return _execute_commit(message, alias, allow_amend=False)


# Esegue git commit applicando i controlli e l'eventuale amend.
def _execute_commit(message, alias, allow_amend=True):
    if allow_amend:
        amend, reason = _should_amend_existing_commit()
    else:
        amend = False
        reason = "Amend is disabled for this alias."
    if amend:
        print(f"Updating the existing WIP commit (--amend). Reason: {reason}")
    else:
        print(f"Creating a new commit. Reason: {reason}")
    base = ["commit"]
    if amend:
        base.append("--amend")
    base.extend(["-F", "-"])
    try:
        return run_git_cmd(base, input=message, text=True)
    except CommandExecutionError as exc:
        status_lines = _git_status_lines()
        if has_unstaged_changes(status_lines):
            print(
                f"Unable to run git {alias}: unstaged changes are still present.",
                file=sys.stderr,
            )
            sys.exit(exc.returncode or 1)
        if not has_staged_changes(status_lines):
            print(f"Unable to run git {alias}: the staging area is empty.", file=sys.stderr)
            sys.exit(exc.returncode or 1)
        raise


# Aggiorna il comando installato sfruttando il tool uv.
def upgrade_self():
    _run_checked(
        [
            "uv",
            "tool",
            "install",
            "git-alias",
            "--force",
            "--from",
            "git+https://github.com/Ogekuri/G.git",
        ]
    )


# Rimuove il comando installato utilizzando lo strumento uv.
def remove_self():
    _run_checked(["uv", "tool", "uninstall", "git-alias"])


# Aggiunge tutte le modifiche e i nuovi file all'area di staging (alias aa).
def cmd_aa(extra):
    status_lines = _git_status_lines()
    if not has_unstaged_changes(status_lines):
        print("No changes are available to add to the staging area.", file=sys.stderr)
        sys.exit(1)
    return run_git_cmd(["add", "--all"], extra)


# Rimuove tutti i file dallo staging riportandoli nel working tree (alias ra).
def cmd_ra(extra):
    if extra:
        args = _to_args(extra)
        if args == ["--help"]:
            print_command_help("ra")
            return
        print("git ra does not accept positional arguments.", file=sys.stderr)
        sys.exit(1)
    work_branch = get_branch("work")
    try:
        current_branch = _current_branch_name()
    except ReleaseError:
        print("git ra requires an active branch head.", file=sys.stderr)
        sys.exit(1)
    if current_branch != work_branch:
        print(
            f"git ra must be executed from the {work_branch} branch (current: {current_branch}).",
            file=sys.stderr,
        )
        sys.exit(1)
    _ensure_commit_ready("ra")
    return run_git_cmd(["reset", "--mixed"], [])


# Crea un archivio master compresso e lo nomina con il tag corrente (alias ar).
def cmd_ar(extra):
    args = _to_args(extra)
    master_branch = get_branch("master")
    tag = capture_git_output(["describe", master_branch])
    filename = f"{tag}.tar.gz"
    archive_cmd = ["git", "archive", master_branch, "--prefix=/"] + args
    with subprocess.Popen(archive_cmd, stdout=subprocess.PIPE) as archive_proc:
        with open(filename, "wb") as output_io:
            gzip_proc = _run_checked(["gzip"], stdin=archive_proc.stdout, stdout=output_io)
        archive_proc.stdout.close()
        archive_proc.wait()
    return gzip_proc


# Mostra i rami locali disponibili (alias br).
def cmd_br(extra):
    return run_git_cmd(["branch"], extra)


# Elimina un branch locale (alias bd).
def cmd_bd(extra):
    return run_git_cmd(["branch", "-d"], extra)


# Controlla le differenze e i possibili conflitti (alias ck).
def cmd_ck(extra):
    return run_git_cmd(["diff", "--check"], extra)


# Esegue commit con messaggio (alias cm).
def _ensure_commit_ready(alias):
    status_lines = _git_status_lines()
    if has_unstaged_changes(status_lines):
        print(
            f"Unable to run git {alias}: unstaged changes are still present.",
            file=sys.stderr,
        )
        sys.exit(1)
    if not has_staged_changes(status_lines):
        print(f"Unable to run git {alias}: the staging area is empty.", file=sys.stderr)
        sys.exit(1)
    return True


# Esegue l'alias 'cm' con i controlli condivisi di commit.
def cmd_cm(extra):
    message = _prepare_commit_message(extra, "cm")
    _ensure_commit_ready("cm")
    return _execute_commit(message, "cm")


# Esegue l'alias 'wip' con messaggio fisso e verifiche condivise.
def cmd_wip(extra):
    if extra:
        args = _to_args(extra)
        if args == ["--help"]:
            print_command_help("wip")
            return
        print("git wip does not accept positional arguments.", file=sys.stderr)
        sys.exit(1)
    _ensure_commit_ready("wip")
    message = "wip: work in progress."
    return _execute_commit(message, "wip")


# Esegue l'alias 'release' determinando prima la versione corrente.
def cmd_release(extra):
    args = _to_args(extra)
    if args:
        if args == ["--help"]:
            print_command_help("release")
            return
        print("git release does not accept positional arguments.", file=sys.stderr)
        sys.exit(1)
    _ensure_commit_ready("release")
    rules = get_version_rules()
    if not rules:
        print("No version rules configured.", file=sys.stderr)
        sys.exit(1)
    root = get_git_root()
    try:
        version = _determine_canonical_version(root, rules)
    except VersionDetectionError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
    message = f"release version: {version}"
    return _execute_commit(message, "release")


# Esegue l'alias 'new' creando un commit convenzionale.
def cmd_new(extra):
    return _run_conventional_commit("new", "new", extra)


# Esegue l'alias 'fix' creando un commit convenzionale.
def cmd_fix(extra):
    return _run_conventional_commit("fix", "fix", extra)


# Esegue l'alias 'change' creando un commit convenzionale.
def cmd_change(extra):
    return _run_conventional_commit("change", "change", extra)


# Esegue l'alias 'docs' creando un commit convenzionale.
def cmd_docs(extra):
    return _run_conventional_commit("docs", "docs", extra)


# Esegue l'alias 'style' creando un commit convenzionale.
def cmd_style(extra):
    return _run_conventional_commit("style", "style", extra)


# Esegue l'alias 'revert' creando un commit convenzionale.
def cmd_revert(extra):
    return _run_conventional_commit("revert", "revert", extra)


# Esegue l'alias 'misc' creando un commit convenzionale.
def cmd_misc(extra):
    return _run_conventional_commit("misc", "misc", extra)


# Aggiunge tutto e committa con messaggio (alias cma).
def cmd_co(extra):
    return run_git_cmd(["checkout"], extra)


# Descrive la revisione HEAD con git describe (alias de).
def cmd_de(extra):
    return run_git_cmd(["describe"], extra)


# Scarta le modifiche del file indicato (alias di).
def cmd_di(extra):
    return run_git_cmd(["checkout", "--"], extra)


# Mantiene la versione locale durante un conflitto (--ours).
def cmd_diyou(extra):
    return run_git_cmd(["checkout", "--ours", "--"], extra)


# Mantiene la versione remota durante un conflitto (--theirs).
def cmd_dime(extra):
    return run_git_cmd(["checkout", "--theirs", "--"], extra)


# Apre uno o piu file con l'editor configurato (alias ed).
def cmd_ed(extra):
    paths = _to_args(extra)
    if not paths:
        print("git ed requires at least one file path", file=sys.stderr)
        sys.exit(1)
    for path in paths:
        expanded = os.path.expanduser(path)
        run_editor_command([expanded])


# Scarica aggiornamenti dal remote per il ramo corrente (alias fe).
def cmd_fe(extra):
    return run_git_cmd(["fetch"], extra)


# Effettua fetch di tutti i rami, tag e pulisce quelli orfani (alias feall).
def cmd_feall(extra):
    return cmd_fe(["--all", "--tags", "--prune"] + _to_args(extra))


# Apre gitk con tutti i commit (alias gp).
def cmd_gp(extra):
    return run_command(["gitk", "--all"] + _to_args(extra))


# Apre gitk semplificato per semplificare il grafo (alias gr).
def cmd_gr(extra):
    return run_command(["gitk", "--simplify-by-decoration", "--all"] + _to_args(extra))


# Elenca tutti i rami locali e remoti con informazioni aggiuntive (alias lb).
def cmd_lb(extra):
    return run_git_cmd(["branch", "-v", "-a"], extra)


# Esegue l'alias 'lg' per mostrare la cronologia dei commit.
def cmd_lg(extra):
    return run_git_cmd(
        [
            "log",
            "--graph",
            "--abbrev-commit",
            "--decorate",
            "--format=format:%C(bold blue)%h%C(reset) - %C(bold green)(%ar)%C(reset) %C(white)%s%C(reset) %C(dim white)- %an%C(reset)%C(bold yellow)%d%C(reset)",
            "--all",
        ],
        extra,
    )


# Mostra i dettagli dell'ultimo commit (alias lh).
def cmd_lh(extra):
    return run_git_cmd(["log", "-1", "HEAD"], extra)


# Mostra i commit nel formato oneline completo (alias ll).
def cmd_ll(extra):
    return run_git_cmd(
        [
            "log",
            "--graph",
            "--decorate",
            "--format=format:%C(bold blue)%H%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n %C(white)%s%C(reset) %C(dim white)- %an%C(reset)",
            "--all",
        ],
        extra,
    )


# Mostra soltanto i merge (alias lm).
def cmd_lm(extra):
    return run_git_cmd(["log", "--merges"], extra)


# Elenca i tag presenti (alias lt).
def cmd_lt(extra):
    return run_git_cmd(["tag", "-l"], extra)


# Esegue merge con --ff-only (alias me).
def cmd_me(extra):
    return run_git_cmd(["merge", "--ff-only"], extra)


# Esegue pull --ff-only sul ramo corrente (alias pl).
def cmd_pl(extra):
    return run_git_cmd(["pull", "--ff-only"], extra)


# Esegue push di tutti i tag (alias pt).
def cmd_pt(extra):
    return run_git_cmd(["push", "--tags"], extra)


# Esegue push e imposta upstream nel remote (alias pu).
def cmd_pu(extra):
    return run_git_cmd(["push", "-u"], extra)


# Mostra il reflog (alias rf).
def cmd_rf(extra):
    return run_git_cmd(["reflog"], extra)


# Rimuove un tag localmente e lo elimina da origin (alias rmtg).
def cmd_rmtg(extra):
    args = _to_args(extra)
    if not args:
        print("usage: git rmtg \"<tag>\"", file=sys.stderr)
        sys.exit(1)
    tag = args[0]
    tail = args[1:]
    run_git_cmd(["tag", "--delete", tag])
    return run_git_cmd(["push", "--delete", "origin", tag], tail)


# Reset hard e pulisce l'area di lavoro (alias rmloc).
def cmd_rmloc(extra):
    return run_git_cmd(["reset", "--hard", "--"], extra)


# Rimuove i file dallo stage (alias rmstg).
def cmd_rmstg(extra):
    return run_git_cmd(["rm", "--cached", "--"], extra)


# Pulisce i file non tracciati (alias rmunt).
def cmd_rmunt(extra):
    return run_git_cmd(["clean", "-d", "-f", "--"], extra)


# Resetta HEAD con --hard (alias rs).
def cmd_rs(extra):
    return run_git_cmd(["reset", "--hard", "HEAD"], extra)


# Resetta con --soft per mantenere i contenuti (alias rssft).
def cmd_rssft(extra):
    return _run_reset_with_help(["reset", "--soft", "--"], extra)


# Resetta con --mixed per deselezionare gli staged (alias rsmix).
def cmd_rsmix(extra):
    return _run_reset_with_help(["reset", "--mixed", "--"], extra)


# Resetta con --hard (alias rshrd).
def cmd_rshrd(extra):
    return _run_reset_with_help(["reset", "--hard", "--"], extra)


# Resetta con --merge per gestire conflitti parziali (alias rsmrg).
def cmd_rsmrg(extra):
    return _run_reset_with_help(["reset", "--merge", "--"], extra)


# Resetta con --keep mantenendo i file locali (alias rskep).
def cmd_rskep(extra):
    return _run_reset_with_help(["reset", "--keep", "--"], extra)


# Mostra lo stato corrente del repository (alias st).
def cmd_st(extra):
    return run_git_cmd(["status"], extra)


# Crea un tag annotato (alias tg).
def cmd_tg(extra):
    return run_git_cmd(["tag", "-a", "-m"], extra)


# Cancella lo stage dei file con reset --mixed (alias unstg).
def cmd_unstg(extra):
    return run_git_cmd(["reset", "--mixed", "--"], extra)


# Verifica la consistenza delle versioni nei file configurati (alias ver).
def cmd_ver(extra):
    del extra  # non usato
    root = get_git_root()
    rules = get_version_rules()
    if not rules:
        print("No version rules configured.", file=sys.stderr)
        sys.exit(1)
    try:
        canonical = _determine_canonical_version(root, rules)
    except VersionDetectionError as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
    print(canonical)


# Aggiorna tutte le versioni nei file configurati applicando la semantica nuova.
def cmd_chver(extra):
    args = _to_args(extra)
    if len(args) != 1:
        print("usage: git chver <major.minor.patch>", file=sys.stderr)
        sys.exit(1)
    requested = args[0].strip()
    target_tuple = _parse_semver_tuple(requested)
    if not target_tuple:
        print("Please provide the version in the format <major>.<minor>.<patch> (e.g. 1.2.3).", file=sys.stderr)
        sys.exit(1)
    root = get_git_root()
    rules = get_version_rules()
    if not rules:
        print("No version rules configured.", file=sys.stderr)
        sys.exit(1)
    try:
        current = _determine_canonical_version(root, rules)
    except VersionDetectionError as exc:
        print(f"Unable to determine the current version: {exc}", file=sys.stderr)
        sys.exit(1)
    current_tuple = _parse_semver_tuple(current)
    if current_tuple is None:
        print(f"The current version '{current}' is not a valid semantic version.", file=sys.stderr)
        sys.exit(1)
    if requested == current:
        print(f"The project version is already {current}.")
        return
    action = "Upgrade" if target_tuple > current_tuple else "Downgrade"
    replacements = 0
    for pattern, expression in rules:
        files = _collect_version_files(root, pattern)
        if not files:
            continue
        try:
            compiled = re.compile(expression)
        except re.error as exc:
            print(f"Ignoring invalid regex '{expression}' for pattern '{pattern}': {exc}", file=sys.stderr)
            continue
        for file_path in files:
            try:
                text = file_path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                text = file_path.read_text(encoding="utf-8", errors="ignore")
            except OSError as exc:
                print(f"Unable to read {file_path}: {exc}", file=sys.stderr)
                continue
            new_text, count = _replace_versions_in_text(text, compiled, requested)
            if count:
                try:
                    file_path.write_text(new_text, encoding="utf-8")
                except OSError as exc:
                    print(f"Unable to write {file_path}: {exc}", file=sys.stderr)
                    sys.exit(1)
                replacements += count
    if replacements == 0:
        print("No version entries were updated. Ensure ver_rules match the desired files.", file=sys.stderr)
        sys.exit(1)
    try:
        confirmed = _determine_canonical_version(root, rules)
    except VersionDetectionError as exc:
        print(f"Fatal error after updating versions: {exc}", file=sys.stderr)
        sys.exit(1)
    if confirmed != requested:
        print(
            f"Fatal error: the updated files report version {confirmed} instead of {requested}.",
            file=sys.stderr,
        )
        sys.exit(1)
    print(f"{action} completed: version is now {confirmed}.")


# Esegue il rilascio incrementando il numero major.
def cmd_major(extra):
    _reject_extra_arguments(extra, "major")
    _run_release_command("major")


# Esegue il rilascio incrementando il numero minor.
def cmd_minor(extra):
    _reject_extra_arguments(extra, "minor")
    _run_release_command("minor")


# Esegue il rilascio incrementando il numero patch.
def cmd_patch(extra):
    _reject_extra_arguments(extra, "patch")
    _run_release_command("patch")


# Genera il file CHANGELOG.md tramite l'alias 'changelog'.
def cmd_changelog(extra):
    parser = argparse.ArgumentParser(prog="g changelog", add_help=False)
    parser.add_argument("--force-write", dest="force_write", action="store_true")
    parser.add_argument("--include-unreleased", action="store_true")
    parser.add_argument("--print-only", action="store_true")
    parser.add_argument("--help", action="store_true")
    try:
        args = parser.parse_args(list(extra))
    except SystemExit:
        print("Invalid arguments for g changelog.", file=sys.stderr)
        sys.exit(2)
    if args.help:
        print_command_help("changelog")
        return
    if not is_inside_git_repo():
        print("Error: run g changelog inside a Git repository.", file=sys.stderr)
        sys.exit(2)
    repo_root = get_git_root()
    content = generate_changelog_document(repo_root, args.include_unreleased)
    if args.print_only:
        print(content, end="")
        return
    destination = Path(repo_root) / "CHANGELOG.md"
    if destination.exists() and not args.force_write:
        print(
            "CHANGELOG.md already exists. Use --force-write to overwrite it or --print-only to show the new content.",
            file=sys.stderr,
        )
        sys.exit(1)
    destination.write_text(content, encoding="utf-8")
    print(f"\nGenerated file: {destination}")

COMMANDS = {
    "aa": cmd_aa,
    "ar": cmd_ar,
    "bd": cmd_bd,
    "br": cmd_br,
    "chver": cmd_chver,
    "changelog": cmd_changelog,
    "change": cmd_change,
    "ck": cmd_ck,
    "cm": cmd_cm,
    "co": cmd_co,
    "de": cmd_de,
    "di": cmd_di,
    "dime": cmd_dime,
    "diyou": cmd_diyou,
    "docs": cmd_docs,
    "ed": cmd_ed,
    "fix": cmd_fix,
    "fe": cmd_fe,
    "feall": cmd_feall,
    "gp": cmd_gp,
    "gr": cmd_gr,
    "lb": cmd_lb,
    "lg": cmd_lg,
    "lh": cmd_lh,
    "ll": cmd_ll,
    "lm": cmd_lm,
    "lt": cmd_lt,
    "major": cmd_major,
    "misc": cmd_misc,
    "me": cmd_me,
    "minor": cmd_minor,
    "new": cmd_new,
    "patch": cmd_patch,
    "ra": cmd_ra,
    "release": cmd_release,
    "pl": cmd_pl,
    "pt": cmd_pt,
    "pu": cmd_pu,
    "revert": cmd_revert,
    "rf": cmd_rf,
    "rmloc": cmd_rmloc,
    "rmstg": cmd_rmstg,
    "rmtg": cmd_rmtg,
    "rmunt": cmd_rmunt,
    "rs": cmd_rs,
    "rshrd": cmd_rshrd,
    "rskep": cmd_rskep,
    "rsmix": cmd_rsmix,
    "rsmrg": cmd_rsmrg,
    "rssft": cmd_rssft,
    "st": cmd_st,
    "tg": cmd_tg,
    "unstg": cmd_unstg,
    "wip": cmd_wip,
    "ver": cmd_ver,
    "style": cmd_style,
}

# Stampa la descrizione di un singolo comando.
def print_command_help(name, width=None):
    description = HELP_TEXTS.get(name, "No help text is available for this command.")
    if width is None:
        print(f"{name} - {description}")
    else:
        print(f"{name.ljust(width)} - {description}")

# Stampa la descrizione di tutti i comandi disponibili in ordine alfabetico.
def print_all_help():
    print("Usage: g <command> [options]")
    print()
    print("Management Commands:")
    for flag, description in MANAGEMENT_HELP:
        print(f"  {flag} - {description}")
    print()
    print("Configuration Parameters:")
    for key in DEFAULT_CONFIG:
        value = CONFIG.get(key, DEFAULT_CONFIG[key])
        if key == "ver_rules":
            print("  ver_rules:")
            rules = []
            if isinstance(value, list):
                rules = value
            else:
                try:
                    rules = json.loads(value)
                except (json.JSONDecodeError, TypeError):
                    rules = []
            for entry in rules:
                pattern = ""
                regex = ""
                if isinstance(entry, dict):
                    pattern = entry.get("pattern") or entry.get("glob") or ""
                    regex = entry.get("regex") or ""
                elif isinstance(entry, (list, tuple)) and len(entry) >= 2:
                    pattern, regex = entry[0], entry[1]
                print(f"    - pattern={pattern} regex={regex}")
        else:
            print(f"  {key} = {value}")
    print()
    print("Commands:")
    help_width = max(len(name) for name in HELP_TEXTS)
    for name in sorted(COMMANDS.keys()):
        print("  ", end="")
        print_command_help(name, width=help_width)


# Gestisce il parsing degli argomenti ed esegue l'alias richiesto.
def main(argv=None):
    """Parse CLI arguments and either show help text or invoke the requested alias."""
    args = list(argv) if argv is not None else sys.argv[1:]
    git_root = get_git_root()
    load_cli_config(git_root)
    if not args:
        print("Please provide a command or --help", file=sys.stderr)
        print_all_help()
        sys.exit(1)
    if args[0] == "--write-config":
        write_default_config(git_root)
        return
    if args[0] == "--upgrade":
        upgrade_self()
        return
    if args[0] == "--remove":
        remove_self()
        return
    if args[0] == "--help":
        if len(args) == 1:
            print_all_help()
            return
        name = args[1]
        if name in COMMANDS:
            print_command_help(name)
        else:
            print(f"Unknown command: {name}", file=sys.stderr)
            sys.exit(1)
        return
    name = args[0]
    extras = args[1:]
    try:
        if name not in COMMANDS:
            run_git_cmd([name], extras)
            return
        if "--help" in extras:
            if name in RESET_HELP_COMMANDS:
                COMMANDS[name](extras)
            else:
                print_command_help(name)
            return
        COMMANDS[name](extras)
    except CommandExecutionError as exc:
        err_text = CommandExecutionError._decode_stream(exc.stderr).strip()
        if err_text:
            print(err_text, file=sys.stderr)
        sys.exit(exc.returncode or 1)


if __name__ == "__main__":
    main()
