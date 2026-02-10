# Workflow Analysis

## Command Line Interface (CLI) Entry Point
*   **Component**: `git_alias.core`
    *   `main()`: Main entry point [`src/git_alias/core.py`, 2078-2220]
        *   description: Handles argument parsing, configuration loading, and command dispatch. It initializes the environment and routes execution to specific command handlers based on user input.
        *   input: argv: list, command line arguments; check_updates: bool, flag to enable version checks
        *   output: None
        *   calls:
            *   `get_git_root()`: Locate git root [`src/git_alias/core.py`, 225-241]
                *   description: Finds the root directory of the current git repository by traversing up from the current working directory.
                *   input: None
                *   output: Path: Path, the absolute path to the git root directory
            *   `load_cli_config()`: Load configuration [`src/git_alias/core.py`, 248-283]
                *   description: Loads the CLI configuration from the repository's config file, merging it with defaults.
                *   input: root: Path, git repository root path
                *   output: None

## Staging Changes
*   **Component**: `git_alias.core`
    *   `cmd_aa()`: Stage all changes [`src/git_alias/core.py`, 1431-1439]
        *   description: Stages all modified and untracked files in the repository. It verifies if there are changes before attempting to stage them.
        *   input: extra: list, additional command line arguments
        *   output: returncode: int, exit code of the git command
        *   calls:
            *   `_git_status_lines()`: Get git status [`src/git_alias/core.py`, 577-590]
                *   description: Retrieves the porcelain status output from git to analyze current repository state.
                *   input: None
                *   output: list[str], lines of git status output
            *   `has_unstaged_changes()`: Check unstaged changes [`src/git_alias/core.py`, 591-603]
                *   description: Analyzes status lines to determine if there are any unstaged changes that can be added.
                *   input: status_lines: list, optional list of status lines
                *   output: bool, True if unstaged changes exist
            *   `run_git_cmd()`: Run git command [`src/git_alias/core.py`, 517-522]
                *   description: Executes a git command with specified arguments.
                *   input: base_args: list, command arguments; extra: list, extra args; cwd: Path, working directory
                *   output: returncode: int, process exit code

## Commit Creation
*   **Component**: `git_alias.core`
    *   `cmd_cm()`: Create commit [`src/git_alias/core.py`, 1510-1516]
        *   description: Creates a new commit using a standard or generated message. It ensures the repository is in a valid state for committing.
        *   input: extra: list, additional arguments
        *   output: returncode: int, exit code of the git commit
        *   calls:
            *   `_prepare_commit_message()`: Prepare message [`src/git_alias/core.py`, 1345-1356]
                *   description: Constructs or retrieves the commit message based on flags and alias type.
                *   input: extra: list, arguments; alias: str, command alias
                *   output: str, final commit message
            *   `_ensure_commit_ready()`: Check commit readiness [`src/git_alias/core.py`, 1495-1509]
                *   description: Verifies preconditions for committing, such as being on a valid branch and having staged changes.
                *   input: alias: str, command alias for error reporting
                *   output: None
            *   `_execute_commit()`: Execute commit [`src/git_alias/core.py`, 1380-1410]
                *   description: Runs the actual git commit command, handling amend logic if applicable.
                *   input: message: str, commit message; alias: str, command alias; allow_amend: bool, flag to allow --amend
                *   output: returncode: int, exit code

## Release Management
*   **Component**: `git_alias.core`
    *   `cmd_major()`: Major release [`src/git_alias/core.py`, 1921-1926]
        *   description: Initiates a major version release workflow. (Note: cmd_minor and cmd_patch follow identical logic).
        *   input: extra: list, arguments
        *   output: None
        *   calls:
            *   `_run_release_command()`: Run release [`src/git_alias/core.py`, 1291-1307]
                *   description: Wrapper that sets up the release process and handles common flags.
                *   input: level: str, increment level (major/minor/patch); changelog_args: list, arguments for changelog
                *   output: None
                *   calls:
                    *   `_execute_release_flow()`: Execute release [`src/git_alias/core.py`, 1247-1290]
                        *   description: Orchestrates the release: checks prerequisites, bumps version, updates files, generates changelog, commits, and tags.
                        *   input: level: str, increment level; changelog_args: list, changelog options
                        *   output: None
                        *   calls:
                            *   `_determine_canonical_version()`: Get current version [`src/git_alias/core.py`, 1073-1115]
                                *   description: Scans project files based on configured rules to find the current version.
                                *   input: root: Path, git root; rules: list, version regex rules
                                *   output: str, current version string
                            *   `_bump_semver_version()`: Bump version [`src/git_alias/core.py`, 1205-1224]
                                *   description: Calculates the next semantic version based on the increment level.
                                *   input: current_version: str; level: str
                                *   output: str, new version string
                            *   `_replace_versions_in_text()`: Update files [`src/git_alias/core.py`, 1124-1140]
                                *   description: Replaces version strings in file content using regex.
                                *   input: text: str; compiled_regex: Pattern; replacement: str
                                *   output: new_text: str; count: int
                            *   `generate_changelog_document()`: Generate changelog [`src/git_alias/core.py`, 959-1008]
                                *   description: Generates the full changelog content from git history.
                                *   input: repo_root: Path; include_unreleased: bool; include_draft: bool
                                *   output: str, markdown content

## Changelog Generation
*   **Component**: `git_alias.core`
    *   `cmd_changelog()`: Generate changelog command [`src/git_alias/core.py`, 1939-2033]
        *   description: CLI command to generate or print the changelog.
        *   input: extra: list, arguments
        *   output: None
        *   calls:
            *   `generate_changelog_document()`: Generate document [`src/git_alias/core.py`, 959-1008]
                *   description: Core logic to build the changelog markdown.
                *   input: repo_root: Path; include_unreleased: bool; include_draft: bool
                *   output: str, markdown content
                *   calls:
                    *   `generate_section_for_range()`: Generate section [`src/git_alias/core.py`, 852-888]
                        *   description: Generates a changelog section for a specific revision range (e.g., between tags).
                        *   input: repo_root: Path; title: str; date_s: str; rev_range: str
                        *   output: Optional[str], section markdown or None
                        *   calls:
                            *   `git_log_subjects()`: Get commits [`src/git_alias/core.py`, 806-818]
                                *   description: Retrieves commit subjects for a given range.
                                *   input: repo_root: Path; rev_range: str
                                *   output: List[str], list of commit subjects
                            *   `categorize_commit()`: Categorize commit [`src/git_alias/core.py`, 819-843]
                                *   description: Parses a commit message to determine its category (Features, Fixes, etc.) based on conventional commits.
                                *   input: subject: str
                                *   output: section: Optional[str]; line: str

## Version Verification
*   **Component**: `git_alias.core`
    *   `cmd_ver()`: Verify version consistency [`src/git_alias/core.py`, 1850-1867]
        *   description: Validates version rules, emits optional verbose/debug diagnostics, and prints the canonical version.
        *   input: extra: list, additional arguments
        *   output: None
        *   calls:
            *   `get_git_root()`: Locate repository root [`src/git_alias/core.py`, 225-238]
                *   description: Finds the root directory of the current git repository by traversing up from the current working directory.
                *   input: None
                *   output: Path: Path, the absolute path to the git root directory
            *   `get_version_rules()`: Load version rules [`src/git_alias/core.py`, 115-117]
                *   description: Retrieves the version rule list from configuration defaults or overrides.
                *   input: None
                *   output: list, version rule tuples
            *   `_determine_canonical_version()`: Determine canonical version [`src/git_alias/core.py`, 1073-1130]
                *   description: Applies pathspec filtering, regex matching, and consistency checks while emitting verbose/debug match evidence.
                *   input: root: Path, git root; rules: list, version rules; verbose: bool, verbose diagnostics flag; debug: bool, debug diagnostics flag
                *   output: canonical: str, detected version string
                *   calls:
                    *   `_collect_version_files()`: Collect files for pattern [`src/git_alias/core.py`, 1009-1051]
                        *   description: Lists tracked files or falls back to rglob, then filters by pathspec to select candidates.
                        *   input: root: Path, git root; pattern: str, glob pattern
                        *   output: files: list, matched file paths
                        *   calls:
                            *   `_is_version_path_excluded()`: Filter excluded paths [`src/git_alias/core.py`, 1054-1056]
                                *   description: Checks if a relative path matches known cache/temp exclusions.
                                *   input: relative_path: str, relative path
                                *   output: bool, True when excluded
                    *   `_iter_versions_in_text()`: Extract version matches [`src/git_alias/core.py`, 1059-1069]
                        *   description: Iterates regex matches and yields the detected version tokens.
                        *   input: text: str, file content; compiled_regexes: list, compiled regex patterns
                        *   output: version: str, matched version token
