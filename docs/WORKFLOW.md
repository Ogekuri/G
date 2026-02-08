# Workflow Analysis

## CLI Initialization and Command Dispatch
- **Component**: `src/git_alias/core.py`
- **Trace**:
  - `main(argv=None, check_updates=True)`: Entry point. Parses arguments, loads config, and dispatches commands. [`src/git_alias/core.py`, 2078-2128]
    - description: Main execution loop. Handles help, version checks, and command routing. Maps command names to functions in `COMMANDS` or passes through to git.
    - input: `argv` (list of strings), `check_updates` (bool)
    - output: System exit code.
    - calls: `get_git_root()`, `load_cli_config()`, `check_for_newer_version()`, `run_git_cmd()`.

## Release Automation
- **Component**: `src/git_alias/core.py`
- **Trace**:
  - `cmd_major(extra)`: Initiates a major release (X.0.0). [`src/git_alias/core.py`, 1921-1926]
    - description: Alias for major version bump.
    - input: `extra` (CLI args)
    - output: None
    - calls: `_run_release_command()`.
  - `_run_release_command(level, changelog_args=None)`: Error handling wrapper for release flow. [`src/git_alias/core.py`, 1291-1300]
    - description: Wraps the release execution in try-except blocks to handle `ReleaseError` and `VersionDetectionError`.
    - input: `level` (semver part), `changelog_args`
    - output: None
    - calls: `_execute_release_flow()`.
  - `_execute_release_flow(level, changelog_args=None)`: Orchestrates the complete release process. [`src/git_alias/core.py`, 1247-1288]
    - description: Executes release steps: checks prerequisites, bumps version, updates files, commits, tags, generates changelog, amends commit, merges branches, and pushes.
    - input: `level` (release type), `changelog_args`
    - output: None
    - calls: `_ensure_release_prerequisites()`, `_determine_canonical_version()`, `_bump_semver_version()`, `_run_release_step()`.
  - `_run_release_step(level, step_name, action)`: Executes a single release step. [`src/git_alias/core.py`, 1225-1246]
    - description: Runs a lambda action and prints status.
    - input: `level`, `step_name`, `action` (callable)
    - output: None
    - calls: `action()` (e.g., `cmd_chver`, `cmd_release`, `cmd_tg`).

## Changelog Generation
- **Component**: `src/git_alias/core.py`
- **Trace**:
  - `cmd_changelog(extra)`: Generates or updates CHANGELOG.md. [`src/git_alias/core.py`, 1939-2033]
    - description: Command to generate changelog from git history. Supports dry-run and checking unreleased commits.
    - input: `extra` (CLI flags like --dry-run)
    - output: None
    - calls: `generate_changelog_document()`, `run_git_cmd()`.
  - `generate_changelog_document(repo_root, include_unreleased, include_draft=False)`: Builds markdown content. [`src/git_alias/core.py`, 959-1008]
    - description: Aggregates git tags and commits into a markdown document. Iterates through tags and commits to build history.
    - input: `repo_root`, `include_unreleased`, `include_draft`
    - output: String content of CHANGELOG.md.
    - calls: `list_tags_sorted_by_date()`, `git_log_subjects()`, `build_history_section()`.
  - `git_log_subjects(repo_root, rev_range)`: Retrieves commit messages. [`src/git_alias/core.py`, 806-818]
    - description: Runs `git log` to get commit subjects for a revision range.
    - input: `repo_root`, `rev_range`
    - output: List of commit subject strings.
    - calls: `capture_git_output()`.

## Version Management
- **Component**: `src/git_alias/core.py`
- **Trace**:
  - `cmd_chver(extra)`: Updates version numbers in project files. [`src/git_alias/core.py`, 1849-1920]
    - description: Scans configured files (e.g., pyproject.toml, version.json) and updates version strings.
    - input: `extra` (target version)
    - output: None
    - calls: `_collect_version_files()`, `_replace_versions_in_text()`.
  - `_collect_version_files(root, pattern)`: Finds files matching version patterns. [`src/git_alias/core.py`, 1009-1053]
    - description: Recursively searches directory for files to update, respecting exclusion rules.
    - input: `root`, `pattern`
    - output: List of file paths.
    - calls: `os.walk()`.
  - `_replace_versions_in_text(text, compiled_regex, replacement)`: Performs regex replacement. [`src/git_alias/core.py`, 1124-1140]
    - description: Replaces found version strings with the new version.
    - input: `text`, `compiled_regex`, `replacement`
    - output: Updated text.
    - calls: `re.sub()`.

## Git Operations
- **Component**: `src/git_alias/core.py`
- **Trace**:
  - `run_git_cmd(base_args, extra=None, cwd=None, **kwargs)`: Executes git commands. [`src/git_alias/core.py`, 517-522]
    - description: Wrapper around `run_command` specifically for git.
    - input: `base_args` (git subcommand), `extra` (flags)
    - output: None (prints to stdout/stderr).
    - calls: `run_command()`.
  - `_git_status_lines()`: Gets status output. [`src/git_alias/core.py`, 577-590]
    - description: Runs `git status --porcelain` to check repo state.
    - input: None
    - output: List of status lines.
    - calls: `capture_git_output()`.
