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
    "ver_rules": json.dumps(DEFAULT_VER_RULES),
}
CONFIG = DEFAULT_CONFIG.copy()
BRANCH_KEYS = ("master", "develop", "work")
MANAGEMENT_HELP = [
    ("--write-config", "Genera il file .g.conf nella root del repository con i valori di default."),
    ("--upgrade", "Reinstalla git-alias tramite uv tool install."),
    ("--remove", "Disinstalla git-alias utilizzando uv tool uninstall."),
]


def get_config_value(name):
    """Retrieve a configuration value with fallback to defaults."""
    return CONFIG.get(name, DEFAULT_CONFIG[name])


def get_branch(name):
    """Return the configured name for the requested branch key."""
    if name not in BRANCH_KEYS:
        raise KeyError(f"Unknown branch key {name}")
    return get_config_value(name)


def get_editor():
    """Return the configured editor command."""
    return get_config_value("editor")


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


def get_version_rules():
    """Return the configured wildcard/regex pairs for version scanning."""
    return _load_config_rules("ver_rules", DEFAULT_VER_RULES)


def get_git_root():
    """Return the git repository root or the current working directory."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        location = result.stdout.strip()
        if location:
            return Path(location)
    except subprocess.CalledProcessError:
        pass
    return Path.cwd()


def get_config_path(root=None):
    """Return the expected path of the configuration file."""
    base = Path(root) if root is not None else get_git_root()
    return base / CONFIG_FILENAME


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


def write_default_config(root=None):
    """Write the default configuration file in the repository root."""
    config_path = get_config_path(root)
    keys = ("master", "develop", "work", "editor", "ver_rules")
    lines = [f"{key}={DEFAULT_CONFIG[key]}" for key in keys]
    config_path.write_text("\n".join(lines) + "\n")
    print(f"Configuration written to {config_path}")
    return config_path


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


def run_editor_command(args):
    """Execute the configured editor command with additional arguments."""
    return run_command(_editor_base_command() + list(args))

HELP_TEXTS = {
    "aa": "Add all file changes/added to stage area for commit.",
    "ar": "Archive the configured master branch as zip file. Use tag as filename.",
    "br": "Create a new brach.",
    "changelog": "Generate CHANGELOG.md from conventional commits (supports --include-unreleased, --force-write, --print-only).",
    "ck": "Check differences.",
    "cm": "Commit with annotation: git cm '<descritoon>'.",
    "cma": "Add all files and commit with annotation: git cma '<descritoon>'.",
    "co": "Checkout a specific branch: git co '<branch>'.",
    "de": "Describe current version with tag of last commit.",
    "di": "Discard current changes on file: git di '<filename>'",
    "dime": "Discard merge chanhes in favour of yours files.",
    "diyou": "Discard merge changes in favour of mine files.",
    "ed": "Edit a file. Syntax: git ed <filename>.",
    "edbrc": "Edit bash ~/.bashrc file.",
    "edbsh": "Edit bash ~/.bash_profile file.",
    "edcfg": "Edit git .gitconfig file. This file.",
    "edgit": "Edit this repository configuration file: .git/config.",
    "edign": "Edit git .gitignore configuration file.",
    "edpro": "Edit bash ~/.profile file.",
    "fe": "Fetch new data of current branch from origin.",
    "feall": "Fetch new data from origin for all branch.",
    "gp": "Open git commits graph (Git K).",
    "gr": "Open git tags graph (Git K).",
    "lg": "Show commit history.",
    "lg1": "Show decorated oneline history for all refs.",
    "lg2": "Show a formatted log graph for all refs.",
    "lg3": "Show the commit tree in a more verbose format.",
    "lh": "Show last commit details",
    "ll": "Show lastest full commit hash.",
    "lm": "Show all merges.",
    "lsbr": "Print all branches.",
    "lt": "Show all tag",
    "me": "Merge",
    "pl": "Pull (fetch + merge FETCH_HEAD) from origin on current branch.",
    "pt": "Push all new tags to origin.",
    "pu": "Push current branch to origin (add upstream (tracking) reference for pull).",
    "rf": "Show changes on HEAD reference.",
    "rmloc": "Remove changed files from the working tree.",
    "rmstg": "Remove staged files from index tree.",
    "rmtg": "Remove a tag on current branch and from origin.",
    "rmunt": "Remove untracked files from the working tree.",
    "rmwrk": "Delete the configured work branch locally.",
    "rs": "Reset current branch to HEAD (--hard).",
    "rshrd": "Hard reset alias (--hard).",
    "rskep": "Keep reset alias (--keep).",
    "rsmix": "Mixed reset alias (--mixed).",
    "rsmrg": "Merge reset alias (--merge).",
    "rssft": "Soft reset alias (--soft).",
    "st": "Show current GIT status.",
    "tg": "Create a new annotate tag. Syntax: git tg <description> <tag>.",
    "tree": "Show commit's tree.",
    "unstg": "Un-stage a file from commit: git unstg '<filename>'. Unstage all files with: git unstg *.",
    "ver": "Verify version consistency across configured files.",
}

RESET_HELP = """

 Reset commands help screen

 default mode = '--mixed'

 working - area di lavoro
 index   - staging + ready to commit
 HEAD    - ultimo commit
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


# Invia un comando git con argomenti principali e supplementari nella directory indicata.
def run_git_cmd(base_args, extra=None, cwd=None, **kwargs):
    full = ["git"] + list(base_args) + _to_args(extra)
    return subprocess.run(full, check=True, cwd=cwd, **kwargs)


# Esegue git e restituisce l'output come stringa per usi interni.
def capture_git_output(base_args, cwd=None):
    result = subprocess.run(
        ["git"] + list(base_args), check=True, cwd=cwd, stdout=subprocess.PIPE, text=True
    )
    return result.stdout.strip()


# Invoca un comando esterno con la sintassi fornita.
def run_command(cmd, cwd=None):
    return subprocess.run(cmd, check=True, cwd=cwd)


# Run git commands returning stdout as text.
def run_git_text(args, cwd=None, check=True):
    proc = subprocess.run(
        ["git", *args],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


# Esegue una pipeline nella shell quando serve costruire comandi complessi.
def run_shell(command, cwd=None):
    return subprocess.run(command, shell=True, check=True, cwd=cwd)


# Run git commands returning stdout as text.
def run_git_text(args, cwd=None, check=True):
    proc = subprocess.run(
        ["git", *args],
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or f"git {' '.join(args)} failed")
    return proc.stdout.strip()


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
_SEMVER_TAG_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
SECTION_EMOJI = {
    "Features": "⛰️",
    "Bug Fixes": "🐛",
    "Changes": "🚜",
    "Documentation": "📚",
    "Styling": "🎨",
    "Miscellaneous Tasks": "⚙️",
    "Revert": "◀️",
}


def list_tags_sorted_by_date(repo_root: Path) -> List[TagInfo]:
    fmt = f"%(refname:strip=2){DELIM}%(creatordate:short){DELIM}%(objectname)"
    output = run_git_text(
        ["for-each-ref", "--sort=creatordate", f"--format={fmt}", "refs/tags"], cwd=repo_root, check=False
    )
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


def generate_section_for_range(repo_root: Path, title: str, date_s: str, rev_range: str) -> Optional[str]:
    subjects = git_log_subjects(repo_root, rev_range)
    buckets: Dict[str, List[str]] = defaultdict(list)
    for subj in subjects:
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


def get_origin_compare_url(base_url: Optional[str], prev_tag: Optional[str], tag: str) -> Optional[str]:
    if not base_url:
        return None
    if prev_tag:
        return f"{base_url}/compare/{prev_tag}..{tag}"
    return f"{base_url}/releases/tag/{tag}"


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


def generate_changelog_document(repo_root: Path, include_unreleased: bool) -> str:
    tags = list_tags_sorted_by_date(repo_root)
    origin_base = _canonical_origin_base(repo_root)
    lines: List[str] = ["# Changelog", ""]
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
            section = generate_section_for_range(repo_root, title, tag.iso_date, rev_range)
            if section:
                lines.append(section)
            prev = tag.name
    else:
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        section = generate_section_for_range(repo_root, "Unreleased", today, "HEAD")
        if section:
            lines.append(section)
    history = build_history_section(repo_root, tags, include_unreleased)
    if history:
        lines.append("")
        lines.append(history)
    return "\n".join(lines).rstrip() + "\n"


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


def _run_reset_with_help(base_args, extra):
    """Execute a reset command or show the reset help when --help is provided."""
    args = _to_args(extra)
    if "--help" in args:
        print(RESET_HELP.strip("\n"))
        return
    return run_git_cmd(base_args, args)


# Aggiorna il comando installato sfruttando il tool uv.
def upgrade_self():
    subprocess.run(
        [
            "uv",
            "tool",
            "install",
            "git-alias",
            "--force",
            "--from",
            "git+https://github.com/Ogekuri/G.git",
        ],
        check=True,
    )


# Rimuove il comando installato utilizzando lo strumento uv.
def remove_self():
    subprocess.run(["uv", "tool", "uninstall", "git-alias"], check=True)


# Aggiunge tutte le modifiche e i nuovi file all'area di staging (alias aa).
def cmd_aa(extra):
    return run_git_cmd(["add", "--all"], extra)


# Crea un archivio master compresso e lo nomina con il tag corrente (alias ar).
def cmd_ar(extra):
    args = _to_args(extra)
    master_branch = get_branch("master")
    tag = capture_git_output(["describe", master_branch])
    filename = f"{tag}.tar.gz"
    archive_cmd = ["git", "archive", master_branch, "--prefix=/"] + args
    with subprocess.Popen(archive_cmd, stdout=subprocess.PIPE) as archive_proc:
        with open(filename, "wb") as output_io:
            gzip_proc = subprocess.run(["gzip"], stdin=archive_proc.stdout, stdout=output_io, check=True)
        archive_proc.stdout.close()
        archive_proc.wait()
    return gzip_proc


# Mostra i rami locali disponibili (alias br).
def cmd_br(extra):
    return run_git_cmd(["branch"], extra)


# Elenca tutti i rami locali e remoti con informazioni aggiuntive (alias lsbr).
def cmd_lsbr(extra):
    return run_git_cmd(["branch", "-v", "-a"], extra)


# Controlla le differenze e i possibili conflitti (alias ck).
def cmd_ck(extra):
    return run_git_cmd(["diff", "--check"], extra)


# Esegue commit con messaggio (alias cm).
def cmd_cm(extra):
    return run_git_cmd(["commit", "-m"], extra)


# Aggiunge tutto e committa con messaggio (alias cma).
def cmd_cma(extra):
    return run_git_cmd(["commit", "-a", "-m"], extra)


# Esegue checkout del ramo indicato (alias co).
def cmd_co(extra):
    return run_git_cmd(["checkout"], extra)


# Elimina il ramo work locale (alias rmwrk).
def cmd_rmwrk(extra):
    return cmd_br(["-d", get_branch("work")] + _to_args(extra))


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


# Apre ~/.gitconfig (alias edcfg).
def cmd_edcfg(extra):
    return cmd_ed(["~/.gitconfig"] + _to_args(extra))


# Apre ~/.gitignore (alias edign).
def cmd_edign(extra):
    return cmd_ed(["~/.gitignore"] + _to_args(extra))


# Apre ~/.profile (alias edpro).
def cmd_edpro(extra):
    return cmd_ed(["~/.profile"] + _to_args(extra))


# Apre ~/.bash_profile (alias edbsh).
def cmd_edbsh(extra):
    return cmd_ed(["~/.bash_profile"] + _to_args(extra))


# Apre ~/.bashrc (alias edbrc).
def cmd_edbrc(extra):
    return cmd_ed(["~/.bashrc"] + _to_args(extra))

# Apre .git/config con l'editor configurato (alias conf).
def cmd_edgit(extra):
    return cmd_ed([".git/config"] + _to_args(extra))


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


# Mostra la cronologia dei commit delegando a lg2 (alias lg).
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


# Mostra il log decorato in una vista compatta con grafico (alias lg1).
def cmd_lg1(extra):
    return run_git_cmd(
        [
            "log",
            "--all",
            "--decorate",
            "--oneline",
            "--graph",
        ],
        extra,
    )


# Mostra il log formattato con grafico e abbreviazioni per ogni ref (alias lg2).
def cmd_lg2(extra):
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


# Mostra l'albero dei commit con informazioni dettagliate (alias lg3).
def cmd_lg3(extra):
    return run_git_cmd(
        [
            "log",
            "--graph",
            "--abbrev-commit",
            "--decorate",
            "--format=format:%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n %C(white)%s%C(reset) %C(dim white)- %an%C(reset)",
            "--all",
        ],
        extra,
    )


# Mostra i commit nel formato oneline completo (alias ll).
def cmd_ll(extra):
        return run_git_cmd(
        [
            "log",
            "--graph",
            "--decorate",
            "--format=format:%C(bold blue)%h%C(reset) - %C(bold cyan)%aD%C(reset) %C(bold green)(%ar)%C(reset)%C(bold yellow)%d%C(reset)%n %C(white)%s%C(reset) %C(dim white)- %an%C(reset)",
            "--all",
        ],
        extra,
    )


# Mostra soltanto i merge (alias lm).
def cmd_lm(extra):
    return run_git_cmd(["log", "--merges"], extra)


# Mostra i dettagli dell'ultimo commit (alias lh).
def cmd_lh(extra):
    return run_git_cmd(["log", "-1", "HEAD"], extra)


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


# Mostra l'albero dei commit delegando a lg3 (alias tree).
def cmd_tree(extra):
    return cmd_lg3(extra)


# Cancella lo stage dei file con reset --mixed (alias unstg).
def cmd_unstg(extra):
    return run_git_cmd(["reset", "--mixed", "--"], extra)


# Verifica la consistenza delle versioni nei file configurati (alias ver).
def cmd_ver(extra):
    del extra  # unused
    root = get_git_root()
    rules = get_version_rules()
    if not rules:
        print("No version rules configured.", file=sys.stderr)
        sys.exit(1)
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
                    print(
                        f"Version mismatch between {canonical_file} ({canonical}) and {file_path} ({version})",
                        file=sys.stderr,
                    )
                    sys.exit(1)
    if canonical is None:
        print("No version string matched the configured rule list.", file=sys.stderr)
        sys.exit(1)
    print(canonical)


def cmd_changelog(extra):
    parser = argparse.ArgumentParser(prog="g changelog", add_help=False)
    parser.add_argument("--force-write", dest="force_write", action="store_true")
    parser.add_argument("--include-unreleased", action="store_true")
    parser.add_argument("--print-only", action="store_true")
    parser.add_argument("--help", action="store_true")
    try:
        args = parser.parse_args(list(extra))
    except SystemExit:
        print("Argomenti non validi per g changelog.", file=sys.stderr)
        sys.exit(2)
    if args.help:
        print_command_help("changelog")
        return
    if not is_inside_git_repo():
        print("Errore: eseguire g changelog all'interno di un repository Git.", file=sys.stderr)
        sys.exit(2)
    repo_root = get_git_root()
    content = generate_changelog_document(repo_root, args.include_unreleased)
    if args.print_only:
        print(content, end="")
        return
    destination = Path(repo_root) / "CHANGELOG.md"
    if destination.exists() and not args.force_write:
        print(
            "CHANGELOG.md esiste già. Usa --force-write per sovrascrivere il file o --print-only per stampare il nuovo contenuto.",
            file=sys.stderr,
        )
        sys.exit(1)
    destination.write_text(content, encoding="utf-8")
    print(f"\nFile generato: {destination}")

COMMANDS = {
    "aa": cmd_aa,
    "ar": cmd_ar,
    "br": cmd_br,
    "changelog": cmd_changelog,
    "ck": cmd_ck,
    "cm": cmd_cm,
    "cma": cmd_cma,
    "co": cmd_co,
    "de": cmd_de,
    "di": cmd_di,
    "dime": cmd_dime,
    "diyou": cmd_diyou,
    "ed": cmd_ed,
    "edbrc": cmd_edbrc,
    "edbsh": cmd_edbsh,
    "edcfg": cmd_edcfg,
    "edgit": cmd_edgit,
    "edign": cmd_edign,
    "edpro": cmd_edpro,
    "fe": cmd_fe,
    "feall": cmd_feall,
    "gp": cmd_gp,
    "gr": cmd_gr,
    "lg": cmd_lg,
    "lg1": cmd_lg1,
    "lg2": cmd_lg2,
    "lg3": cmd_lg3,
    "lh": cmd_lh,
    "ll": cmd_ll,
    "lm": cmd_lm,
    "lsbr": cmd_lsbr,
    "lt": cmd_lt,
    "me": cmd_me,
    "pl": cmd_pl,
    "pt": cmd_pt,
    "pu": cmd_pu,
    "rf": cmd_rf,
    "rmloc": cmd_rmloc,
    "rmstg": cmd_rmstg,
    "rmtg": cmd_rmtg,
    "rmunt": cmd_rmunt,
    "rmwrk": cmd_rmwrk,
    "rs": cmd_rs,
    "rshrd": cmd_rshrd,
    "rskep": cmd_rskep,
    "rsmix": cmd_rsmix,
    "rsmrg": cmd_rsmrg,
    "rssft": cmd_rssft,
    "st": cmd_st,
    "tg": cmd_tg,
    "tree": cmd_tree,
    "unstg": cmd_unstg,
    "ver": cmd_ver,
}

# Stampa la descrizione di un singolo comando.
def print_command_help(name):
    description = HELP_TEXTS.get(name, "No help text is available for this command.")
    print(f"{name} - {description}")

# Stampa la descrizione di tutti i comandi disponibili in ordine alfabetico.
def print_all_help():
    for flag, description in MANAGEMENT_HELP:
        print(f"{flag} - {description}")
    for name in sorted(COMMANDS.keys()):
        print_command_help(name)


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
    if name not in COMMANDS:
        print(f"Unknown command: {name}", file=sys.stderr)
        print_all_help()
        sys.exit(1)
    if "--help" in extras:
        if name in RESET_HELP_COMMANDS:
            COMMANDS[name](extras)
        else:
            print_command_help(name)
        return
    COMMANDS[name](extras)


if __name__ == "__main__":
    main()
