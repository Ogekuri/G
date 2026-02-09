# Technical Workflow Documentation

This document provides a detailed technical call tree of the git-alias CLI tool implementation.

## Entry Point and Main Execution Flow

* `main()`: Main CLI entry point [`src/git_alias/core.py`, `2078-2128`]
  * description: Parses command-line arguments, loads configuration, checks for updates, and dispatches to the appropriate command handler.
  * input: `argv` (command line arguments list), `check_updates` (boolean flag)
  * output: None (calls sys.exit on errors)
  * calls:
    * `get_git_root()`: Locate the git repository root directory [`src/git_alias/core.py`, `225-238`]
      * description: Executes `git rev-parse --show-toplevel` to find the repository root.
      * input: None
      * output: Path object representing the git root directory
      * calls:
        * `_run_checked()`: Execute subprocess with error handling [`src/git_alias/core.py`, `498-503`]
          * description: Wraps subprocess.run with check=True and converts CalledProcessError to CommandExecutionError.
          * input: `popenargs` (command arguments), `kwargs` (subprocess options)
          * output: CompletedProcess instance
    * `load_cli_config()`: Load configuration from .g.conf file [`src/git_alias/core.py`, `248-280`]
      * description: Reads and parses JSON configuration file, updates global CONFIG dictionary with user settings.
      * input: `root` (repository root path)
      * output: Path object of config file
      * calls:
        * `get_config_path()`: Calculate configuration file path [`src/git_alias/core.py`, `242-244`]
          * description: Constructs the path to .g.conf in the repository root.
          * input: `root` (repository root path)
          * output: Path object for .g.conf
    * `check_for_newer_version()`: Check GitHub API for newer releases [`src/git_alias/core.py`, `142-221`]
      * description: Queries GitHub releases API with caching to notify user of available updates.
      * input: `timeout_seconds` (HTTP request timeout)
      * output: None (prints notification to stderr if update available)
      * calls:
        * `get_cli_version()`: Retrieve current CLI version [`src/git_alias/core.py`, `121-130`]
          * description: Reads __version__ from __init__.py without importing the module.
          * input: None
          * output: Version string or "unknown"
        * `_parse_semver_tuple()`: Parse semantic version string [`src/git_alias/core.py`, `1116-1120`]
          * description: Extracts major, minor, patch numbers from version string using regex.
          * input: `text` (version string)
          * output: Tuple of (major, minor, patch) integers or None
        * `_normalize_semver_text()`: Remove 'v' prefix from version [`src/git_alias/core.py`, `134-138`]
          * description: Strips leading 'v' from version tags to normalize format.
          * input: `text` (version string)
          * output: Normalized version string
    * `write_default_config()`: Generate default configuration file [`src/git_alias/core.py`, `284-289`]
      * description: Writes DEFAULT_CONFIG dictionary to .g.conf as formatted JSON.
      * input: `root` (repository root path)
      * output: Path object of written config file
    * `upgrade_self()`: Reinstall CLI using uv tool [`src/git_alias/core.py`, `1411-1422`]
      * description: Executes `uv tool install --force` to upgrade from GitHub repository.
      * input: None
      * output: None
    * `remove_self()`: Uninstall CLI using uv tool [`src/git_alias/core.py`, `1426-1427`]
      * description: Executes `uv tool uninstall git-alias` to remove the package.
      * input: None
      * output: None
    * `print_all_help()`: Display comprehensive help information [`src/git_alias/core.py`, `2042-2074`]
      * description: Prints formatted help text including management commands, configuration, and all available git aliases.
      * input: None
      * output: None (prints to stdout)
    * `print_command_help()`: Display help for specific command [`src/git_alias/core.py`, `2034-2039`]
      * description: Retrieves and formats help text from HELP_TEXTS dictionary for a single command.
      * input: `name` (command name), `width` (optional column width)
      * output: None (prints to stdout)

## Git Repository State Management

* `_git_status_lines()`: Get repository status in porcelain format [`src/git_alias/core.py`, `577-587`]
  * description: Executes `git status --porcelain` and returns output lines.
  * input: None
  * output: List of status line strings
  * calls:
    * `_run_checked()`: Execute subprocess with error handling [`src/git_alias/core.py`, `498-503`]

* `has_unstaged_changes()`: Detect working tree modifications [`src/git_alias/core.py`, `591-600`]
  * description: Scans status lines for untracked files or modified files not in staging area.
  * input: `status_lines` (optional cached status output)
  * output: Boolean indicating presence of unstaged changes
  * calls:
    * `_git_status_lines()`: Get repository status in porcelain format [`src/git_alias/core.py`, `577-587`]

* `has_staged_changes()`: Detect staged modifications [`src/git_alias/core.py`, `604-611`]
  * description: Checks status lines for files added to staging area ready for commit.
  * input: `status_lines` (optional cached status output)
  * output: Boolean indicating presence of staged changes
  * calls:
    * `_git_status_lines()`: Get repository status in porcelain format [`src/git_alias/core.py`, `577-587`]

* `_refresh_remote_refs()`: Update remote branch references [`src/git_alias/core.py`, `619-628`]
  * description: Executes `git remote -v update` once per session to sync remote refs.
  * input: None
  * output: None (sets global _REMOTE_REFS_UPDATED flag)
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `_branch_remote_divergence()`: Calculate local/remote commit differences [`src/git_alias/core.py`, `632-648`]
  * description: Uses `git rev-list --left-right --count` to determine how many commits each branch is ahead.
  * input: `branch_key` (configuration key for branch), `remote` (remote name)
  * output: Tuple of (local_ahead, remote_ahead) commit counts
  * calls:
    * `_refresh_remote_refs()`: Update remote branch references [`src/git_alias/core.py`, `619-628`]
    * `get_branch()`: Retrieve configured branch name [`src/git_alias/core.py`, `77-80`]
    * `run_git_text()`: Execute git command and capture text output [`src/git_alias/core.py`, `558-573`]

* `has_remote_branch_updates()`: Check if remote has new commits [`src/git_alias/core.py`, `652-654`]
  * description: Returns true if remote branch has commits not present locally.
  * input: `branch_key` (configuration key), `remote` (remote name)
  * output: Boolean indicating remote updates available
  * calls:
    * `_branch_remote_divergence()`: Calculate local/remote commit differences [`src/git_alias/core.py`, `632-648`]

* `_current_branch_name()`: Get active branch name [`src/git_alias/core.py`, `1141-1151`]
  * description: Executes `git rev-parse --abbrev-ref HEAD` to determine current branch.
  * input: None
  * output: Branch name string
  * calls:
    * `_run_checked()`: Execute subprocess with error handling [`src/git_alias/core.py`, `498-503`]

* `_ref_exists()`: Verify git reference exists [`src/git_alias/core.py`, `1155-1162`]
  * description: Uses `git show-ref --verify` to check if a ref exists.
  * input: `ref_name` (full reference name)
  * output: Boolean indicating reference existence

* `_local_branch_exists()`: Check local branch existence [`src/git_alias/core.py`, `1166-1167`]
  * description: Verifies existence of refs/heads/{branch_name}.
  * input: `branch_name` (branch name)
  * output: Boolean
  * calls:
    * `_ref_exists()`: Verify git reference exists [`src/git_alias/core.py`, `1155-1162`]

* `_remote_branch_exists()`: Check remote branch existence [`src/git_alias/core.py`, `1171-1172`]
  * description: Verifies existence of refs/remotes/origin/{branch_name}.
  * input: `branch_name` (branch name)
  * output: Boolean
  * calls:
    * `_ref_exists()`: Verify git reference exists [`src/git_alias/core.py`, `1155-1162`]

## Version Management System

* `cmd_ver()`: Verify version consistency across files [`src/git_alias/core.py`, `1833-1845`]
  * description: Scans configured files for version strings and ensures they all match.
  * input: `extra` (unused command arguments)
  * output: None (prints canonical version or exits with error)
  * calls:
    * `get_git_root()`: Locate the git repository root directory [`src/git_alias/core.py`, `225-238`]
    * `get_version_rules()`: Load version detection rules from config [`src/git_alias/core.py`, `116-117`]
      * description: Calls _load_config_rules with "ver_rules" key to get pattern/regex pairs.
      * input: None
      * output: List of (pattern, regex) tuples
      * calls:
        * `_load_config_rules()`: Parse configuration rules list [`src/git_alias/core.py`, `89-112`]
          * description: Normalizes various config formats (dict/list/tuple) into consistent (pattern, regex) tuples.
          * input: `key` (config key), `fallback` (default rules)
          * output: List of (pattern, regex) tuples
    * `_determine_canonical_version()`: Extract and validate version [`src/git_alias/core.py`, `1073-1112`]
      * description: Applies all version rules to find version strings and ensures consistency across files.
      * input: `root` (repository root), `rules` (version rules list)
      * output: Canonical version string
      * calls:
        * `_collect_version_files()`: Find files matching pattern [`src/git_alias/core.py`, `1009-1051`]
          * description: Uses git ls-files and pathspec matching to locate files for version detection.
          * input: `root` (repository root), `pattern` (glob pattern)
          * output: List of Path objects
          * calls:
            * `_is_version_path_excluded()`: Check exclusion patterns [`src/git_alias/core.py`, `1055-1056`]
              * description: Tests path against VERSION_CLEANUP_PATTERNS to exclude temp directories.
              * input: `relative_path` (file path)
              * output: Boolean
        * `_iter_versions_in_text()`: Extract version strings using regex [`src/git_alias/core.py`, `1060-1069`]
          * description: Applies compiled regexes to text and yields matched version strings.
          * input: `text` (file content), `compiled_regexes` (list of compiled patterns)
          * output: Iterator of version strings

* `cmd_chver()`: Change project version [`src/git_alias/core.py`, `1849-1917`]
  * description: Updates version strings in all configured files to the specified semantic version.
  * input: `extra` (list containing target version)
  * output: None (modifies files and prints confirmation)
  * calls:
    * `_parse_semver_tuple()`: Parse semantic version string [`src/git_alias/core.py`, `1116-1120`]
    * `get_git_root()`: Locate the git repository root directory [`src/git_alias/core.py`, `225-238`]
    * `get_version_rules()`: Load version detection rules from config [`src/git_alias/core.py`, `116-117`]
    * `_determine_canonical_version()`: Extract and validate version [`src/git_alias/core.py`, `1073-1112`]
    * `_collect_version_files()`: Find files matching pattern [`src/git_alias/core.py`, `1009-1051`]
    * `_replace_versions_in_text()`: Substitute version strings [`src/git_alias/core.py`, `1124-1137`]
      * description: Uses compiled regex to find and replace version occurrences in text.
      * input: `text` (file content), `compiled_regex` (pattern), `replacement` (new version)
      * output: Tuple of (modified_text, replacement_count)

## Changelog Generation System

* `cmd_changelog()`: Generate CHANGELOG.md from commits [`src/git_alias/core.py`, `1939-1970`]
  * description: Parses conventional commits between tags to build a structured changelog document.
  * input: `extra` (command arguments including flags)
  * output: None (writes CHANGELOG.md file)
  * calls:
    * `is_inside_git_repo()`: Verify git repository context [`src/git_alias/core.py`, `715-720`]
      * description: Executes `git rev-parse --is-inside-work-tree` to confirm repository.
      * input: None
      * output: Boolean
    * `get_git_root()`: Locate the git repository root directory [`src/git_alias/core.py`, `225-238`]
    * `generate_changelog_document()`: Build complete changelog content [`src/git_alias/core.py`, `959-1004`]
      * description: Orchestrates tag collection, commit parsing, and section generation for full changelog.
      * input: `repo_root` (repository path), `include_unreleased` (flag), `include_draft` (flag)
      * output: Complete changelog markdown string
      * calls:
        * `list_tags_sorted_by_date()`: Get semver tags chronologically [`src/git_alias/core.py`, `784-802`]
          * description: Uses `git for-each-ref --sort=creatordate` to retrieve annotated tags.
          * input: `repo_root` (repository path), `merged_ref` (optional branch filter)
          * output: List of TagInfo objects with name, date, object hash
        * `_canonical_origin_base()`: Extract repository URL from origin [`src/git_alias/core.py`, `889-904`]
          * description: Parses git remote URL to construct base URL for GitHub links.
          * input: `repo_root` (repository path)
          * output: Base URL string or None
        * `_latest_supported_tag_name()`: Find most recent non-draft tag [`src/git_alias/core.py`, `774-780`]
          * description: Filters tags by MIN_SUPPORTED_HISTORY_VERSION to get baseline.
          * input: `tags` (list of TagInfo), `include_draft` (flag)
          * output: Tag name string or None
          * calls:
            * `_is_supported_release_tag()`: Check tag version threshold [`src/git_alias/core.py`, `761-765`]
              * description: Compares tag semver against MIN_SUPPORTED_HISTORY_VERSION.
              * input: `tag_name` (tag string)
              * output: Boolean
              * calls:
                * `_tag_semver_tuple()`: Parse tag version [`src/git_alias/core.py`, `756-757`]
                  * description: Strips 'v' prefix and calls _parse_semver_tuple.
                  * input: `tag_name` (tag string)
                  * output: Tuple or None
        * `generate_section_for_range()`: Create changelog section for commit range [`src/git_alias/core.py`, `852-885`]
          * description: Extracts commits in range, categorizes by conventional type, formats as markdown section.
          * input: `repo_root` (path), `title` (section header), `date_s` (date string), `rev_range` (git range), `expected_version` (optional filter)
          * output: Markdown section string or None
          * calls:
            * `git_log_subjects()`: Extract commit subject lines [`src/git_alias/core.py`, `806-815`]
              * description: Uses `git log --no-merges --pretty=format` to get commit messages.
              * input: `repo_root` (path), `rev_range` (git range)
              * output: List of subject strings
            * `_extract_release_version()`: Parse release commit version [`src/git_alias/core.py`, `844-848`]
              * description: Uses regex to extract version from "release version: X.Y.Z" commits.
              * input: `subject` (commit message)
              * output: Version string or None
            * `categorize_commit()`: Classify conventional commit [`src/git_alias/core.py`, `819-840`]
              * description: Matches commit against _CONVENTIONAL_RE pattern to determine section and format.
              * input: `subject` (commit message)
              * output: Tuple of (section_name, formatted_line) or (None, "")
        * `get_origin_compare_url()`: Build GitHub compare URL [`src/git_alias/core.py`, `908-913`]
          * description: Constructs URL for comparing two tags or tag to HEAD.
          * input: `base_url` (repo URL), `prev_tag` (earlier tag), `tag` (current tag)
          * output: Compare URL string or None
        * `build_history_section()`: Generate reference links section [`src/git_alias/core.py`, `924-955`]
          * description: Creates markdown History section with tag links and compare references.
          * input: `repo_root` (path), `tags` (list), `include_unreleased` (flag), `include_draft` (flag), `include_unreleased_link` (flag)
          * output: History section markdown or None

## Commit Management

* `cmd_cm()`: Standard commit with validation [`src/git_alias/core.py`, `1510-1513`]
  * description: Creates a commit with user message after ensuring staging area is ready.
  * input: `extra` (list containing commit message)
  * output: None
  * calls:
    * `_prepare_commit_message()`: Validate and join message arguments [`src/git_alias/core.py`, `1345-1353`]
      * description: Ensures message is provided, handles --help, concatenates arguments.
      * input: `extra` (arguments), `alias` (command name)
      * output: Complete message string
    * `_ensure_commit_ready()`: Verify commit preconditions [`src/git_alias/core.py`, `1495-1506`]
      * description: Checks that staging area has changes and working tree is clean.
      * input: `alias` (command name)
      * output: Boolean (True or exits)
      * calls:
        * `_git_status_lines()`: Get repository status in porcelain format [`src/git_alias/core.py`, `577-587`]
        * `has_unstaged_changes()`: Detect working tree modifications [`src/git_alias/core.py`, `591-600`]
        * `has_staged_changes()`: Detect staged modifications [`src/git_alias/core.py`, `604-611`]
    * `_execute_commit()`: Execute git commit with amend logic [`src/git_alias/core.py`, `1380-1407`]
      * description: Determines whether to amend existing WIP commit or create new one, executes git commit.
      * input: `message` (commit message), `alias` (command name), `allow_amend` (flag)
      * output: None
      * calls:
        * `_should_amend_existing_commit()`: Check WIP commit amendability [`src/git_alias/core.py`, `698-711`]
          * description: Verifies HEAD is WIP commit not yet merged to develop or master.
          * input: None
          * output: Tuple of (should_amend, reason_string)
          * calls:
            * `_head_commit_message()`: Get last commit message [`src/git_alias/core.py`, `668-672`]
              * description: Executes `git log -1 --pretty=%s` to retrieve HEAD message.
              * input: None
              * output: Message string
            * `_head_commit_hash()`: Get HEAD commit hash [`src/git_alias/core.py`, `676-680`]
              * description: Executes `git rev-parse HEAD` to get commit SHA.
              * input: None
              * output: Hash string
            * `_commit_exists_in_branch()`: Check commit ancestry [`src/git_alias/core.py`, `684-694`]
              * description: Uses `git merge-base --is-ancestor` to test if commit is in branch.
              * input: `commit_hash` (SHA), `branch_name` (branch)
              * output: Boolean
        * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_wip()`: Work-in-progress commit [`src/git_alias/core.py`, `1517-1527`]
  * description: Creates or amends commit with fixed "wip: work in progress." message.
  * input: `extra` (should be empty or --help)
  * output: None
  * calls:
    * `_ensure_commit_ready()`: Verify commit preconditions [`src/git_alias/core.py`, `1495-1506`]
    * `_execute_commit()`: Execute git commit with amend logic [`src/git_alias/core.py`, `1380-1407`]

* `cmd_new()`: Conventional commit for new feature [`src/git_alias/core.py`, `1555-1556`]
  * description: Creates commit with "new(scope): description" format.
  * input: `extra` (message arguments)
  * output: None
  * calls:
    * `_run_conventional_commit()`: Execute conventional commit workflow [`src/git_alias/core.py`, `1373-1376`]
      * description: Builds conventional message and executes commit with validation.
      * input: `kind` (commit type), `alias` (command name), `extra` (arguments)
      * output: None
      * calls:
        * `_build_conventional_message()`: Format conventional message [`src/git_alias/core.py`, `1357-1369`]
          * description: Parses "module: description" format or uses default_module, constructs "kind(scope): body".
          * input: `kind` (commit type), `extra` (arguments), `alias` (command name)
          * output: Formatted message string
        * `_ensure_commit_ready()`: Verify commit preconditions [`src/git_alias/core.py`, `1495-1506`]
        * `_execute_commit()`: Execute git commit with amend logic [`src/git_alias/core.py`, `1380-1407`]

* `cmd_fix()`: Conventional commit for bug fix [`src/git_alias/core.py`, `1565-1566`]
  * description: Creates commit with "fix(scope): description" format.
  * input: `extra` (message arguments)
  * output: None
  * calls:
    * `_run_conventional_commit()`: Execute conventional commit workflow [`src/git_alias/core.py`, `1373-1376`]

* `cmd_change()`: Conventional commit for changes [`src/git_alias/core.py`, `1570-1571`]
  * description: Creates commit with "change(scope): description" format.
  * input: `extra` (message arguments)
  * output: None
  * calls:
    * `_run_conventional_commit()`: Execute conventional commit workflow [`src/git_alias/core.py`, `1373-1376`]

* `cmd_refactor()`: Conventional commit for refactoring [`src/git_alias/core.py`, `1560-1561`]
  * description: Creates commit with "refactor(scope): description" format.
  * input: `extra` (message arguments)
  * output: None
  * calls:
    * `_run_conventional_commit()`: Execute conventional commit workflow [`src/git_alias/core.py`, `1373-1376`]

* `cmd_docs()`: Conventional commit for documentation [`src/git_alias/core.py`, `1575-1576`]
  * description: Creates commit with "docs(scope): description" format.
  * input: `extra` (message arguments)
  * output: None
  * calls:
    * `_run_conventional_commit()`: Execute conventional commit workflow [`src/git_alias/core.py`, `1373-1376`]

* `cmd_style()`: Conventional commit for styling [`src/git_alias/core.py`, `1580-1581`]
  * description: Creates commit with "style(scope): description" format.
  * input: `extra` (message arguments)
  * output: None
  * calls:
    * `_run_conventional_commit()`: Execute conventional commit workflow [`src/git_alias/core.py`, `1373-1376`]

* `cmd_revert()`: Conventional commit for reverts [`src/git_alias/core.py`, `1585-1586`]
  * description: Creates commit with "revert(scope): description" format.
  * input: `extra` (message arguments)
  * output: None
  * calls:
    * `_run_conventional_commit()`: Execute conventional commit workflow [`src/git_alias/core.py`, `1373-1376`]

* `cmd_misc()`: Conventional commit for miscellaneous [`src/git_alias/core.py`, `1590-1591`]
  * description: Creates commit with "misc(scope): description" format.
  * input: `extra` (message arguments)
  * output: None
  * calls:
    * `_run_conventional_commit()`: Execute conventional commit workflow [`src/git_alias/core.py`, `1373-1376`]

* `cmd_cover()`: Conventional commit for requirement coverage [`src/git_alias/core.py`, `1595-1596`]
  * description: Creates commit with "cover(scope): description" format.
  * input: `extra` (message arguments)
  * output: None
  * calls:
    * `_run_conventional_commit()`: Execute conventional commit workflow [`src/git_alias/core.py`, `1373-1376`]

## Release Automation

* `cmd_major()`: Major version release workflow [`src/git_alias/core.py`, `1921-1923`]
  * description: Increments major version number (X.0.0) and executes full release process.
  * input: `extra` (optional --include-unreleased, --include-draft flags)
  * output: None
  * calls:
    * `_parse_release_flags()`: Validate release command flags [`src/git_alias/core.py`, `1325-1341`]
      * description: Ensures only --include-unreleased and --include-draft are provided.
      * input: `extra` (arguments), `alias` (command name)
      * output: List of validated flags
    * `_run_release_command()`: Execute release with error handling [`src/git_alias/core.py`, `1291-1304`]
      * description: Wraps _execute_release_flow with exception handling and error reporting.
      * input: `level` (major/minor/patch), `changelog_args` (flags)
      * output: None
      * calls:
        * `_execute_release_flow()`: Complete release workflow orchestration [`src/git_alias/core.py`, `1247-1287`]
          * description: Coordinates version bump, commits, tagging, changelog, branch merging, and push operations.
          * input: `level` (release type), `changelog_args` (flags)
          * output: None
          * calls:
            * `_ensure_release_prerequisites()`: Validate release conditions [`src/git_alias/core.py`, `1176-1201`]
              * description: Verifies all required branches exist, no remote updates pending, on work branch, clean working tree.
              * input: None
              * output: Dictionary of branch names
              * calls:
                * `get_branch()`: Retrieve configured branch name [`src/git_alias/core.py`, `77-80`]
                * `_local_branch_exists()`: Check local branch existence [`src/git_alias/core.py`, `1166-1167`]
                * `_refresh_remote_refs()`: Update remote branch references [`src/git_alias/core.py`, `619-628`]
                * `_remote_branch_exists()`: Check remote branch existence [`src/git_alias/core.py`, `1171-1172`]
                * `has_remote_branch_updates()`: Check if remote has new commits [`src/git_alias/core.py`, `652-654`]
                * `_current_branch_name()`: Get active branch name [`src/git_alias/core.py`, `1141-1151`]
                * `_git_status_lines()`: Get repository status in porcelain format [`src/git_alias/core.py`, `577-587`]
                * `has_unstaged_changes()`: Detect working tree modifications [`src/git_alias/core.py`, `591-600`]
                * `has_staged_changes()`: Detect staged modifications [`src/git_alias/core.py`, `604-611`]
            * `get_version_rules()`: Load version detection rules from config [`src/git_alias/core.py`, `116-117`]
            * `get_git_root()`: Locate the git repository root directory [`src/git_alias/core.py`, `225-238`]
            * `_determine_canonical_version()`: Extract and validate version [`src/git_alias/core.py`, `1073-1112`]
            * `_bump_semver_version()`: Calculate next version [`src/git_alias/core.py`, `1205-1221`]
              * description: Increments major, minor, or patch according to level, resets lower components.
              * input: `current_version` (string), `level` (major/minor/patch)
              * output: New version string
            * `_run_release_step()`: Execute single release step with logging [`src/git_alias/core.py`, `1225-1243`]
              * description: Wraps step action with try/catch, prints progress, converts errors to ReleaseError.
              * input: `level` (release type), `step_name` (description), `action` (callable)
              * output: Action result
              * calls:
                * `cmd_chver()`: Change project version [`src/git_alias/core.py`, `1849-1917`]
                * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]
                * `cmd_release()`: Create release commit [`src/git_alias/core.py`, `1531-1551`]
                  * description: Validates version and creates commit with "release version: X.Y.Z" message.
                  * input: `extra` (arguments)
                  * output: None
                * `cmd_tg()`: Create annotated tag [`src/git_alias/core.py`, `1823-1824`]
                  * description: Executes `git tag -a -m` with provided message and tag name.
                  * input: `extra` (message and tag arguments)
                  * output: None
                * `cmd_changelog()`: Generate CHANGELOG.md from commits [`src/git_alias/core.py`, `1939-1970`]
                * `cmd_co()`: Checkout branch [`src/git_alias/core.py`, `1600-1601`]
                  * description: Executes `git checkout` to switch branches.
                  * input: `extra` (branch name)
                  * output: None
                * `cmd_me()`: Merge with fast-forward only [`src/git_alias/core.py`, `1736-1737`]
                  * description: Executes `git merge --ff-only` to integrate branches.
                  * input: `extra` (branch to merge)
                  * output: None
                * `cmd_de()`: Describe tagged commit [`src/git_alias/core.py`, `1605-1606`]
                  * description: Executes `git describe` to show tag information.
                  * input: `extra` (arguments)
                  * output: None
                * `cmd_pt()`: Push tags to origin [`src/git_alias/core.py`, `1746-1747`]
                  * description: Executes `git push --tags` to upload all tags.
                  * input: `extra` (arguments)
                  * output: None

* `cmd_minor()`: Minor version release workflow [`src/git_alias/core.py`, `1927-1929`]
  * description: Increments minor version number (x.Y.0) and executes full release process.
  * input: `extra` (optional flags)
  * output: None
  * calls:
    * `_parse_release_flags()`: Validate release command flags [`src/git_alias/core.py`, `1325-1341`]
    * `_run_release_command()`: Execute release with error handling [`src/git_alias/core.py`, `1291-1304`]

* `cmd_patch()`: Patch version release workflow [`src/git_alias/core.py`, `1933-1935`]
  * description: Increments patch version number (x.y.Z) and executes full release process.
  * input: `extra` (optional flags)
  * output: None
  * calls:
    * `_parse_release_flags()`: Validate release command flags [`src/git_alias/core.py`, `1325-1341`]
    * `_run_release_command()`: Execute release with error handling [`src/git_alias/core.py`, `1291-1304`]

## Staging and Reset Operations

* `cmd_aa()`: Add all changes to staging [`src/git_alias/core.py`, `1431-1436`]
  * description: Executes `git add --all` after verifying unstaged changes exist.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `_git_status_lines()`: Get repository status in porcelain format [`src/git_alias/core.py`, `577-587`]
    * `has_unstaged_changes()`: Detect working tree modifications [`src/git_alias/core.py`, `591-600`]
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_ra()`: Remove all from staging [`src/git_alias/core.py`, `1440-1461`]
  * description: Executes `git reset --mixed` to unstage all files, only allowed on work branch.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `get_branch()`: Retrieve configured branch name [`src/git_alias/core.py`, `77-80`]
    * `_current_branch_name()`: Get active branch name [`src/git_alias/core.py`, `1141-1151`]
    * `_ensure_commit_ready()`: Verify commit preconditions [`src/git_alias/core.py`, `1495-1506`]
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_unstg()`: Unstage specific files [`src/git_alias/core.py`, `1828-1829`]
  * description: Executes `git reset --mixed --` with file arguments to unstage files.
  * input: `extra` (file paths)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_rs()`: Hard reset to HEAD [`src/git_alias/core.py`, `1788-1789`]
  * description: Executes `git reset --hard HEAD`, shows help if --help provided.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `_run_reset_with_help()`: Execute reset with help handling [`src/git_alias/core.py`, `1308-1313`]
      * description: Checks for --help flag and displays RESET_HELP, otherwise executes git reset.
      * input: `base_args` (git reset arguments), `extra` (user arguments)
      * output: None

* `cmd_rssft()`: Soft reset [`src/git_alias/core.py`, `1793-1794`]
  * description: Executes `git reset --soft` to move HEAD without touching index or working tree.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `_run_reset_with_help()`: Execute reset with help handling [`src/git_alias/core.py`, `1308-1313`]

* `cmd_rsmix()`: Mixed reset [`src/git_alias/core.py`, `1798-1799`]
  * description: Executes `git reset --mixed` to move HEAD and update index.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `_run_reset_with_help()`: Execute reset with help handling [`src/git_alias/core.py`, `1308-1313`]

* `cmd_rshrd()`: Hard reset [`src/git_alias/core.py`, `1803-1804`]
  * description: Executes `git reset --hard` to reset index and working tree.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `_run_reset_with_help()`: Execute reset with help handling [`src/git_alias/core.py`, `1308-1313`]

* `cmd_rsmrg()`: Merge reset [`src/git_alias/core.py`, `1808-1809`]
  * description: Executes `git reset --merge` to handle merge conflicts.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `_run_reset_with_help()`: Execute reset with help handling [`src/git_alias/core.py`, `1308-1313`]

* `cmd_rskep()`: Keep reset [`src/git_alias/core.py`, `1813-1814`]
  * description: Executes `git reset --keep` to preserve local changes.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `_run_reset_with_help()`: Execute reset with help handling [`src/git_alias/core.py`, `1308-1313`]

## Branch and Remote Operations

* `cmd_br()`: List branches [`src/git_alias/core.py`, `1480-1481`]
  * description: Executes `git branch` to display local branches.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_bd()`: Delete branch [`src/git_alias/core.py`, `1485-1486`]
  * description: Executes `git branch -d` to delete specified branch.
  * input: `extra` (branch name)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_lb()`: List all branches with details [`src/git_alias/core.py`, `1687-1688`]
  * description: Executes `git branch -v -a` to show local and remote branches.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_co()`: Checkout branch [`src/git_alias/core.py`, `1600-1601`]
  * description: Executes `git checkout` to switch to specified branch.
  * input: `extra` (branch name)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_fe()`: Fetch from remote [`src/git_alias/core.py`, `1636-1637`]
  * description: Executes `git fetch` to download remote changes.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_feall()`: Fetch all remotes with cleanup [`src/git_alias/core.py`, `1641-1642`]
  * description: Executes `git fetch --all --tags --prune` to sync all remotes.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `cmd_fe()`: Fetch from remote [`src/git_alias/core.py`, `1636-1637`]

* `cmd_pl()`: Pull with fast-forward [`src/git_alias/core.py`, `1741-1742`]
  * description: Executes `git pull --ff-only` to fetch and merge.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_pu()`: Push with upstream [`src/git_alias/core.py`, `1751-1752`]
  * description: Executes `git push -u` to push and set tracking.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_str()`: Show remote status [`src/git_alias/core.py`, `1656-1683`]
  * description: Lists all unique remotes and displays detailed status for each.
  * input: `extra` (arguments)
  * output: None (prints to stdout)
  * calls:
    * `run_git_text()`: Execute git command and capture text output [`src/git_alias/core.py`, `558-573`]
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

## Status and Logging

* `cmd_st()`: Show repository status [`src/git_alias/core.py`, `1818-1819`]
  * description: Executes `git status` to display working tree state.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_lg()`: Show commit graph [`src/git_alias/core.py`, `1692-1703`]
  * description: Executes `git log` with custom format showing graph, colors, author, date.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_lh()`: Show last commit [`src/git_alias/core.py`, `1707-1708`]
  * description: Executes `git log -1 HEAD` to display most recent commit details.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_ll()`: Show commit log with full hashes [`src/git_alias/core.py`, `1712-1722`]
  * description: Executes `git log` with full SHA hashes and detailed formatting.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_lm()`: Show merge commits [`src/git_alias/core.py`, `1726-1727`]
  * description: Executes `git log --merges` to display only merge commits.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_lt()`: List tags [`src/git_alias/core.py`, `1731-1732`]
  * description: Executes `git tag -l` to show all repository tags.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_rf()`: Show reflog [`src/git_alias/core.py`, `1756-1757`]
  * description: Executes `git reflog` to display reference log history.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

## File and Working Tree Management

* `cmd_di()`: Discard file changes [`src/git_alias/core.py`, `1610-1611`]
  * description: Executes `git checkout --` to restore files from HEAD.
  * input: `extra` (file paths)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_diyou()`: Keep your version in merge [`src/git_alias/core.py`, `1615-1616`]
  * description: Executes `git checkout --ours --` to resolve conflicts with local version.
  * input: `extra` (file paths)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_dime()`: Keep their version in merge [`src/git_alias/core.py`, `1620-1621`]
  * description: Executes `git checkout --theirs --` to resolve conflicts with remote version.
  * input: `extra` (file paths)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_ed()`: Edit files with configured editor [`src/git_alias/core.py`, `1625-1632`]
  * description: Opens specified files using editor command from configuration.
  * input: `extra` (file paths)
  * output: None
  * calls:
    * `run_editor_command()`: Execute editor with arguments [`src/git_alias/core.py`, `309-310`]
      * description: Combines base editor command with file arguments and executes.
      * input: `args` (file paths)
      * output: None
      * calls:
        * `_editor_base_command()`: Parse editor configuration [`src/git_alias/core.py`, `293-305`]
          * description: Extracts editor command from config, handles shell quoting, returns command parts.
          * input: None
          * output: List of command parts
        * `run_command()`: Execute external command [`src/git_alias/core.py`, `529-530`]

* `cmd_rmloc()`: Remove local changes [`src/git_alias/core.py`, `1773-1774`]
  * description: Executes `git reset --hard --` to discard all local modifications.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_rmstg()`: Remove from staging [`src/git_alias/core.py`, `1778-1779`]
  * description: Executes `git rm --cached --` to unstage files while preserving working copy.
  * input: `extra` (file paths)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_rmunt()`: Remove untracked files [`src/git_alias/core.py`, `1783-1784`]
  * description: Executes `git clean -d -f --` to delete untracked files and directories.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_ck()`: Check for conflicts [`src/git_alias/core.py`, `1490-1491`]
  * description: Executes `git diff --check` to detect whitespace errors and conflicts.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

## Tag and Archive Operations

* `cmd_tg()`: Create annotated tag [`src/git_alias/core.py`, `1823-1824`]
  * description: Executes `git tag -a -m` to create tag with message.
  * input: `extra` (message and tag name)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_rmtg()`: Remove tag locally and remotely [`src/git_alias/core.py`, `1761-1769`]
  * description: Deletes tag locally with `git tag --delete` then pushes deletion to origin.
  * input: `extra` (tag name and additional arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_de()`: Describe commit with tags [`src/git_alias/core.py`, `1605-1606`]
  * description: Executes `git describe` to show most recent tag reachable from commit.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_git_cmd()`: Execute git command with arguments [`src/git_alias/core.py`, `517-519`]

* `cmd_ar()`: Archive master branch [`src/git_alias/core.py`, `1465-1476`]
  * description: Creates gzip compressed tar archive of master branch named with current tag.
  * input: `extra` (archive arguments)
  * output: None
  * calls:
    * `get_branch()`: Retrieve configured branch name [`src/git_alias/core.py`, `77-80`]
    * `capture_git_output()`: Execute git and return output [`src/git_alias/core.py`, `523-525`]
      * description: Runs git command with stdout capture and returns stripped output.
      * input: `base_args` (git command arguments), `cwd` (working directory)
      * output: Output string
    * `_run_checked()`: Execute subprocess with error handling [`src/git_alias/core.py`, `498-503`]

## Visual Tools

* `cmd_gp()`: Open gitk with all commits [`src/git_alias/core.py`, `1646-1647`]
  * description: Launches gitk GUI with `--all` flag to visualize entire commit graph.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_command()`: Execute external command [`src/git_alias/core.py`, `529-530`]

* `cmd_gr()`: Open simplified gitk [`src/git_alias/core.py`, `1651-1652`]
  * description: Launches gitk with `--simplify-by-decoration --all` to show only important commits.
  * input: `extra` (arguments)
  * output: None
  * calls:
    * `run_command()`: Execute external command [`src/git_alias/core.py`, `529-530`]

## Configuration Utilities

* `get_config_value()`: Retrieve configuration value [`src/git_alias/core.py`, `72-73`]
  * description: Returns value from CONFIG dict with fallback to DEFAULT_CONFIG.
  * input: `name` (config key)
  * output: Configuration value

* `get_branch()`: Get branch name from config [`src/git_alias/core.py`, `77-80`]
  * description: Retrieves branch name for master/develop/work keys with validation.
  * input: `name` (branch key)
  * output: Branch name string
  * calls:
    * `get_config_value()`: Retrieve configuration value [`src/git_alias/core.py`, `72-73`]

* `get_editor()`: Get editor command from config [`src/git_alias/core.py`, `84-85`]
  * description: Returns configured editor command string.
  * input: None
  * output: Editor command string
  * calls:
    * `get_config_value()`: Retrieve configuration value [`src/git_alias/core.py`, `72-73`]

## Utility Functions

* `run_git_cmd()`: Execute git with arguments [`src/git_alias/core.py`, `517-519`]
  * description: Constructs full git command from base args and extra args, executes via _run_checked.
  * input: `base_args` (git subcommand), `extra` (additional arguments), `cwd` (working directory), `kwargs` (subprocess options)
  * output: CompletedProcess instance
  * calls:
    * `_to_args()`: Convert extra to list [`src/git_alias/core.py`, `457-458`]
      * description: Safely converts extra arguments to list or returns empty list.
      * input: `extra` (arguments)
      * output: List
    * `_run_checked()`: Execute subprocess with error handling [`src/git_alias/core.py`, `498-503`]

* `run_git_text()`: Execute git and capture text [`src/git_alias/core.py`, `558-573`]
  * description: Runs git command with stdout/stderr capture in text mode, strips output.
  * input: `args` (git command arguments), `cwd` (working directory), `check` (error handling flag)
  * output: Stripped stdout string
  * calls:
    * `_run_checked()`: Execute subprocess with error handling [`src/git_alias/core.py`, `498-503`]

* `run_command()`: Execute arbitrary command [`src/git_alias/core.py`, `529-530`]
  * description: Executes external command using _run_checked.
  * input: `cmd` (command list), `cwd` (working directory)
  * output: CompletedProcess instance
  * calls:
    * `_run_checked()`: Execute subprocess with error handling [`src/git_alias/core.py`, `498-503`]

* `run_shell()`: Execute shell command [`src/git_alias/core.py`, `553-554`]
  * description: Runs command through shell with shell=True for complex pipelines.
  * input: `command` (shell command string), `cwd` (working directory)
  * output: CompletedProcess instance
  * calls:
    * `_run_checked()`: Execute subprocess with error handling [`src/git_alias/core.py`, `498-503`]

## Exception Classes

* `CommandExecutionError`: Subprocess execution failure [`src/git_alias/core.py`, `462-494`]
  * description: Custom exception wrapping CalledProcessError with formatted error messages.
  * input: Exception initialization with CalledProcessError instance
  * output: Exception with cmd, returncode, stdout, stderr attributes
  * calls:
    * `_decode_stream()`: Convert bytes to string [`src/git_alias/core.py`, `486-494`]
      * description: Safely decodes bytes stream to UTF-8 string with error replacement.
      * input: `data` (bytes or string)
      * output: Decoded string

* `VersionDetectionError`: Version parsing failure [`src/git_alias/core.py`, `507-508`]
  * description: Raised when version strings cannot be found or are inconsistent.
  * input: Error message string
  * output: RuntimeError exception

* `ReleaseError`: Release workflow failure [`src/git_alias/core.py`, `512-513`]
  * description: Raised when release prerequisites are not met or release steps fail.
  * input: Error message string
  * output: RuntimeError exception

## Data Classes

* `TagInfo`: Tag metadata container [`src/git_alias/core.py`, `723-727`]
  * description: Dataclass storing tag name, creation date, and object hash.
  * input: name (tag name), iso_date (creation date), object_name (commit hash)
  * output: TagInfo instance with three string attributes

## GitHub Actions CI/CD Workflow

* Release Workflow: Automated package build and release [``.github/workflows/release-uvx.yml`, `1-48`]
  * description: Triggered on version tags, builds Python package, creates attestations, uploads to GitHub releases.
  * trigger: Git tags matching `v*` pattern
  * steps:
    * Checkout repository with full history
    * Setup Python 3.11 environment
    * Install uv package manager
    * Install build dependencies from requirements.txt
    * Build source and wheel distributions with python -m build
    * Generate build provenance attestations for supply chain security
    * Create GitHub release with generated notes and upload distribution artifacts
