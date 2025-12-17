#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse


@dataclass
class TagInfo:
    name: str
    iso_date: str  # YYYY-MM-DD
    object_name: str  # commit hash


DELIM = "\x1f"      # unit separator
RECORD = "\x1e"     # record separator


def run_git(args: List[str], cwd: Optional[str] = None, check: bool = True) -> str:
    """Run a git command and return stdout (stripped)."""
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


def is_inside_git_repo() -> bool:
    try:
        out = run_git(["rev-parse", "--is-inside-work-tree"], check=True)
        return out.strip().lower() == "true"
    except Exception:
        return False


def get_repo_root() -> str:
    return run_git(["rev-parse", "--show-toplevel"], check=True)


def list_tags_sorted_by_date(repo_root: str) -> List[TagInfo]:
    """
    Return tags sorted by creator/committer date ascending, with tag name, date, and target commit hash.
    Works for lightweight & annotated tags.
    """
    # %(creatordate:short) uses taggerdate for annotated tags, committerdate for lightweight tags.
    fmt = f"%(refname:strip=2){DELIM}%(creatordate:short){DELIM}%(objectname)"
    out = run_git(["for-each-ref", "--sort=creatordate", f"--format={fmt}", "refs/tags"], cwd=repo_root)
    tags: List[TagInfo] = []
    if not out:
        return tags
    for line in out.splitlines():
        parts = line.split(DELIM)
        if len(parts) != 3:
            continue
        name, date_s, obj = parts
        if not _SEMVER_TAG_RE.match(name):
            continue
        date_s = date_s or "unknown-date"
        tags.append(TagInfo(name=name, iso_date=date_s, object_name=obj))
    return tags


_CONVENTIONAL_RE = re.compile(
    r"^(?P<type>new|fix|change|docs|style|revert|misc)"
    r"(?:\((?P<scope>[^)]+)\))?"
    r"(?P<breaking>!)?:\s+(?P<desc>.+)$",
    re.IGNORECASE,
)

# Accept only tags like vMAJOR.MINOR.PATCH
_SEMVER_TAG_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")


def categorize_commit(subject: str) -> Tuple[Optional[str], str, bool]:
    """
    Returns (section, rendered_line, is_breaking).
    Sections: Features, Bug Fixes, Changes, Documentation, Styling, Miscellaneous Tasks, Revert.
    """
    s = subject.strip()
    m = _CONVENTIONAL_RE.match(s)
    if not m:
        # Ignore commits that don't match the conventional format
        return (None, "", False)

    ctype = m.group("type").lower()
    scope = m.group("scope")
    breaking = bool(m.group("breaking"))
    desc = m.group("desc").strip()

    # Render line as: - *(scope)* description
    scope_render = f"*({scope})* " if scope else ""
    line = f"- {scope_render}{desc}"

    if ctype == "new":
        section = "Features"
    elif ctype == "fix":
        section = "Bug Fixes"
    elif ctype == "change":
        section = "Changes"
    elif ctype == "docs":
        section = "Documentation"
    elif ctype == "style":
        section = "Styling"
    elif ctype == "revert":
        section = "Revert"
    elif ctype == "misc":
        section = "Miscellaneous Tasks"
    else:
        return (None, "", False)

    return (section, line, breaking)


def git_log_subjects(repo_root: str, rev_range: str) -> List[str]:
    """Get commit subjects (one per commit) for the given revision range."""
    fmt = f"%s{RECORD}"
    out = run_git(["log", "--no-merges", f"--pretty=format:{fmt}", rev_range], cwd=repo_root, check=False)
    if not out:
        return []
    return [x.strip() for x in out.split(RECORD) if x.strip()]


SECTION_EMOJI = {
    "Features": "⛰️",
    "Bug Fixes": "🐛",
    "Changes": "🚜",
    "Documentation": "📚",
    "Styling": "🎨",
    "Miscellaneous Tasks": "⚙️",
    "Revert": "◀️",
}

def generate_section_for_range(repo_root: str, title: str, date_s: str, rev_range: str) -> Optional[str]:
    subjects = git_log_subjects(repo_root, rev_range)
    buckets: Dict[str, List[str]] = {
        "Features": [],
        "Bug Fixes": [],
        "Changes": [],
        "Documentation": [],
        "Styling": [],
        "Miscellaneous Tasks": [],
        "Revert": [],
    }

    for subj in subjects:
        section, line, breaking = categorize_commit(subj)
        if section is None:
            continue
        # We don't render a separate Breaking section in this style; MAJOR bumps are implied by tags.
        buckets[section].append(line)

    # Skip section if no relevant commits for this range
    if not any(buckets.values()):
        return None

    md: List[str] = []
    md.append(f"## {title} - {date_s}")
    for sec in ["Features", "Bug Fixes", "Changes", "Documentation", "Styling", "Miscellaneous Tasks", "Revert"]:
        if buckets.get(sec) and buckets[sec]:
            emoji = SECTION_EMOJI.get(sec, "")
            md.append(f"### {emoji}  {sec}".rstrip())
            md.extend(buckets[sec])
            md.append("")
    return "\n".join(md).rstrip() + "\n"

def get_origin_compare_url(repo_root: str, prev_tag: Optional[str], tag: str) -> Optional[str]:
    """Build a compare URL for GitHub/GitLab if remote origin exists.
    Returns None if remote cannot be parsed or host unsupported.
    """
    try:
        url = run_git(["remote", "get-url", "origin"], cwd=repo_root, check=False).strip()
        if not url:
            return None
        # Normalize SSH URLs to https
        if url.startswith("git@"):
            # git@github.com:owner/repo.git -> https://github.com/owner/repo
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
        # Construct compare path
        if prev_tag:
            return f"{base}/compare/{prev_tag}..{tag}"
        else:
            # First tag: link to tag page
            return f"{base}/releases/tag/{tag}"
    except Exception:
        return None

def build_history_section(repo_root: str, tags: List[TagInfo], include_unreleased: bool) -> Optional[str]:
    """Build a History section listing all tag links.
    - First tag links to release page
    - Subsequent tags link to compare prev..current
    - If include_unreleased and there are tags, add an Unreleased compare last..HEAD
    Returns None if origin URL is not available.
    """
    # Require an origin URL we can turn into compare links
    origin = run_git(["remote", "get-url", "origin"], cwd=repo_root, check=False).strip()
    if not origin:
        return None

    lines: List[str] = []
    lines.append("# History")

    prev: Optional[str] = None
    for t in tags:
        display_version = t.name.lstrip('v')
        url = get_origin_compare_url(repo_root, prev, t.name)
        if not url:
            continue
        lines.append(f"[{display_version}]: {url}")
        prev = t.name

    # Add Unreleased compare if requested and tags exist
    if include_unreleased and tags:
        last = tags[-1].name
        # Construct compare URL for last..HEAD
        url = get_origin_compare_url(repo_root, last, "HEAD")
        if url:
            lines.append(f"[unreleased]: {url}")

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate a CHANGELOG-like markdown file from Git tags and commit messages."
    )
    parser.add_argument(
        "output_markdown",
        nargs="?",
        default=None,
        help="Nome del file markdown da generare (es: CHANGELOG.md). Se omesso, stampa su stdout.",
    )
    parser.add_argument(
        "--include-unreleased",
        action="store_true",
        help="Aggiunge una sezione 'Unreleased' con i commit dopo l'ultimo tag.",
    )
    args = parser.parse_args()

    if not is_inside_git_repo():
        print("Errore: questo script deve essere eseguito all'interno di un repository Git.", file=sys.stderr)
        return 2

    repo_root = get_repo_root()
    tags = list_tags_sorted_by_date(repo_root)

    parser.add_argument(
        "--debug",
        action="store_true",
        help="Stampa informazioni di debug (es. elenco dei tag trovati).",
    )
    args = parser.parse_args()

    if not is_inside_git_repo():
        print("Errore: questo script deve essere eseguito all'interno di un repository Git.", file=sys.stderr)
        return 2

    repo_root = get_repo_root()
    tags = list_tags_sorted_by_date(repo_root)

    if args.debug:
        print("Tag trovati (ordinati per data):")
        if not tags:
            print("  (nessun tag trovato)")
        else:
            for t in tags:
                print(f"  - {t.name} ({t.iso_date})")

    lines: List[str] = []
    lines.append("# Changelog")
    lines.append("")
    # Intro line removed as requested

    if args.include_unreleased:
        if tags:
            last = tags[-1].name
            unreleased_range = f"{last}..HEAD"
        else:
            unreleased_range = "HEAD"
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        unreleased_md = generate_section_for_range(repo_root, "Unreleased", today, unreleased_range)
        if unreleased_md:
            lines.append(unreleased_md)

    if tags:
        prev: Optional[str] = None
        for t in tags:
            rev_range = t.name if prev is None else f"{prev}..{t.name}"
            # Header title with compare URL and display without leading 'v'
            display_version = t.name.lstrip('v')
            compare_url = get_origin_compare_url(repo_root, prev, t.name)
            header_title = f"[{display_version}]({compare_url})" if compare_url else display_version
            md_section = generate_section_for_range(repo_root, header_title, t.iso_date, rev_range)
            if md_section:
                lines.append(md_section)
            prev = t.name
    else:
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        unreleased_md = generate_section_for_range(repo_root, "Unreleased", today, "HEAD")
        if unreleased_md:
            lines.append(unreleased_md)

    # Append History section at end if possible
    history_md = build_history_section(repo_root, tags, args.include_unreleased)
    if history_md:
        lines.append("")
        lines.append(history_md)

    content = "\n".join(lines).rstrip() + "\n"
    if args.output_markdown:
        out_path = os.path.abspath(args.output_markdown)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"\nFile generato: {out_path}")
    else:
        # Print to stdout if no file is provided
        print(content, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
