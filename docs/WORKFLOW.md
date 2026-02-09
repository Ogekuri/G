# Git Alias CLI - Technical Workflow Documentation

This document provides a comprehensive technical call tree structure for the git-alias CLI tool, detailing the execution flow from entry points to internal functions.

## Main Entry Point

- **Entry Point**: CLI Command Execution
  - **Module**: `git_alias`
  - **Entry Function**: `main()`
    - **Functions Called**:
      - `main()`: Main entry point for CLI command execution [`core.py`, 2078-2128]
        - description: Parses command-line arguments, loads configuration from `.g.conf`, checks for updates, and dispatches to the appropriate command handler. Handles management commands (--help, --version, --upgrade, --remove, --write-config) and git alias commands by looking up the command name in the COMMANDS dictionary and calling the corresponding function with extra arguments.
        - input: argv (command-line arguments list), check_updates (boolean flag)
        - output: None (exits with status code or returns normally)
        - calls:
          - `get_git_root()`: Determines the root directory of the current git repository [`core.py`, 225-238]
            - description: Executes `git rev-parse --show-toplevel` to find repository root. Returns Path object of root directory or current working directory if not in a git repo.
            - input: None
            - output: Path object representing git repository root
            - calls:
              - `_run_checked()`: Executes subprocess with error handling [`core.py`, 498-503]
                - description: Wrapper around subprocess.run() that converts CalledProcessError exceptions into CommandExecutionError. Sets check=True by default to raise on non-zero exit codes.
                - input: popenargs (command and arguments), kwargs (subprocess options)
                - output: CompletedProcess object from subprocess.run()
          - `load_cli_config()`: Loads configuration from .g.conf file [`core.py`, 248-280]
            - description: Reads and parses JSON configuration from .g.conf in repository root. Updates global CONFIG dictionary with values for branch names, editor, default_module, and ver_rules. Validates data types and prints warnings for invalid entries.
            - input: root (optional Path to repository root)
            - output: Path object of configuration file
            - calls:
              - `get_config_path()`: Calculates the path to .g.conf configuration file [`core.py`, 242-244]
                - description: Constructs path by joining repository root with CONFIG_FILENAME constant (.g.conf). Uses provided root or calls get_git_root() if not provided.
                - input: root (optional Path)
                - output: Path object to .g.conf file
          - `check_for_newer_version()`: Checks GitHub API for newer releases [`core.py`, 142-221]
            - description: Queries GitHub API for latest release tag, compares with current version using semver comparison. Uses file-based cache with TTL to avoid excessive API calls. Prints upgrade notice to stderr if newer version available.
            - input: timeout_seconds (API request timeout)
            - output: None (prints to stderr if update available)
            - calls:
              - `get_cli_version()`: Retrieves CLI version from __init__.py [`core.py`, 121-130]
                - description: Reads __init__.py file and extracts __version__ string using regex match without importing the module. Returns 'unknown' if file cannot be read or version not found.
                - input: None
                - output: Version string (e.g., "0.0.29")
              - `_parse_semver_tuple()`: Parses semantic version string to tuple [`core.py`, 1115-1120]
                - description: Applies SEMVER_RE regex to extract major, minor, patch as integers. Returns None if string doesn't match semver format.
                - input: text (version string)
                - output: Tuple of (major, minor, patch) integers or None
          - `write_default_config()`: Creates default .g.conf file [`core.py`, 284-289]
            - description: Serializes DEFAULT_CONFIG dictionary to JSON with indentation and writes to .g.conf in repository root. Prints confirmation message with file path.
            - input: root (optional repository root Path)
            - output: Path object to written config file
          - `upgrade_self()`: Reinstalls package via uv tool [`core.py`, 1411-1422]
            - description: Executes `uv tool install git-alias --force --from git+https://github.com/Ogekuri/G.git` to upgrade the CLI tool to latest version from GitHub repository.
            - input: None
            - output: None
          - `remove_self()`: Uninstalls package via uv tool [`core.py`, 1426-1427]
            - description: Executes `uv tool uninstall git-alias` to remove the CLI tool from the system.
            - input: None
            - output: None
          - `print_all_help()`: Prints comprehensive help screen [`core.py`, 2042-2074]
            - description: Displays usage, management commands, configuration parameters, and all available git alias commands sorted alphabetically with descriptions from HELP_TEXTS dictionary.
            - input: None
            - output: None (prints to stdout)
          - `print_command_help()`: Prints help for specific command [`core.py`, 2034-2039]
            - description: Looks up command name in HELP_TEXTS dictionary and prints description. Optionally left-justifies name for aligned output.
            - input: name (command name), width (optional column width)
            - output: None (prints to stdout)

## Feature: Git Alias Commands

### Staging and Commit Operations

- **aa** (Add All): Stages all changes
  - **Function**: `cmd_aa()`
    - `cmd_aa()`: Adds all file changes to staging area [`core.py`, 1431-1436]
      - description: Validates that unstaged changes exist before executing `git add --all`. Exits with error if no changes available.
      - input: extra (additional command arguments)
      - output: CompletedProcess from git add command
      - calls:
        - `_git_status_lines()`: Retrieves git status output as lines [`core.py`, 577-587]
          - description: Executes `git status --porcelain` and splits output into lines. Returns empty list if command fails (check=False).
          - input: None
          - output: List of status line strings
        - `has_unstaged_changes()`: Checks for unstaged modifications [`core.py`, 591-600]
          - description: Parses status lines looking for files starting with '??' (untracked) or having non-space character in second position (modified in working tree).
          - input: status_lines (optional cached status output)
          - output: Boolean indicating unstaged changes exist
        - `run_git_cmd()`: Executes git command with arguments [`core.py`, 517-519]
          - description: Constructs full git command by prepending 'git' to base_args and appending extra arguments. Calls _run_checked() with optional cwd.
          - input: base_args (git subcommand and flags), extra (additional arguments), cwd (working directory), kwargs
          - output: CompletedProcess object

- **ra** (Reset All): Removes all staged files
  - **Function**: `cmd_ra()`
    - `cmd_ra()`: Un-stages all files from index to working tree [`core.py`, 1440-1461]
      - description: Validates current branch is 'work' branch and staging area has content before executing `git reset --mixed`. Ensures clean state before reset.
      - input: extra (command arguments)
      - output: CompletedProcess from git reset command
      - calls:
        - `_current_branch_name()`: Gets active branch name [`core.py`, 1141-1151]
          - description: Executes `git rev-parse --abbrev-ref HEAD` to determine current branch. Raises ReleaseError if HEAD is detached.
          - input: None
          - output: Branch name string
        - `_ensure_commit_ready()`: Validates pre-commit state [`core.py`, 1495-1506]
          - description: Checks that no unstaged changes exist and staging area is not empty. Exits with appropriate error message if validation fails.
          - input: alias (command name for error messages)
          - output: True if validation passes

- **cm** (Commit): Standard commit with message
  - **Function**: `cmd_cm()`
    - `cmd_cm()`: Creates commit with custom message [`core.py`, 1510-1513]
      - description: Prepares commit message from extra arguments, ensures staging area is ready, then executes commit with potential amend for WIP commits.
      - input: extra (commit message as arguments)
      - output: CompletedProcess from git commit
      - calls:
        - `_prepare_commit_message()`: Constructs commit message from arguments [`core.py`, 1345-1353]
          - description: Validates that message arguments exist, checks for --help flag, and joins all arguments into single message string.
          - input: extra (argument list), alias (command name)
          - output: Message string
        - `_execute_commit()`: Performs git commit operation [`core.py`, 1380-1407]
          - description: Determines if existing WIP commit should be amended, constructs commit command with -F flag to read message from stdin, handles errors by checking staging/working tree state.
          - input: message (commit text), alias (command name), allow_amend (boolean)
          - output: CompletedProcess from git commit
          - calls:
            - `_should_amend_existing_commit()`: Checks if HEAD is WIP commit eligible for amend [`core.py`, 698-711]
              - description: Validates HEAD message matches WIP pattern, retrieves commit hash, and ensures WIP commit not already merged into develop or master branches.
              - input: None
              - output: Tuple of (should_amend boolean, reason string)
              - calls:
                - `_head_commit_message()`: Gets last commit message [`core.py`, 668-672]
                  - description: Executes `git log -1 --pretty=%s` to extract commit subject line.
                  - input: None
                  - output: Commit message string
                - `_head_commit_hash()`: Gets HEAD commit hash [`core.py`, 676-680]
                  - description: Executes `git rev-parse HEAD` to get full commit hash.
                  - input: None
                  - output: Commit hash string
                - `_commit_exists_in_branch()`: Checks if commit merged into branch [`core.py`, 684-694]
                  - description: Uses `git merge-base --is-ancestor` to determine if commit_hash is ancestor of branch_name. Returns True if exit code is 0.
                  - input: commit_hash, branch_name
                  - output: Boolean

- **wip** (Work In Progress): Auto-message commit
  - **Function**: `cmd_wip()`
    - `cmd_wip()`: Creates WIP commit with fixed message [`core.py`, 1517-1527]
      - description: Ensures staging ready, then commits with message 'wip: work in progress.' May amend previous WIP commit if applicable.
      - input: extra (should be empty, checked)
      - output: CompletedProcess from git commit

### Conventional Commit Commands

- **new** (New Feature): Conventional commit for new features
  - **Function**: `cmd_new()`
    - `cmd_new()`: Creates new(scope): description commit [`core.py`, 1555-1556]
      - description: Calls generic conventional commit handler with 'new' type.
      - input: extra (message arguments)
      - output: CompletedProcess from commit
      - calls:
        - `_run_conventional_commit()`: Executes conventional commit workflow [`core.py`, 1373-1376]
          - description: Builds conventional message, validates commit readiness, executes commit without amend.
          - input: kind (commit type), alias (command name), extra (arguments)
          - output: CompletedProcess from git commit
          - calls:
            - `_build_conventional_message()`: Formats conventional commit message [`core.py`, 1357-1369]
              - description: Parses message for 'module:' prefix using regex. Extracts scope and body, or uses default_module from config. Constructs 'type(scope): body' format.
              - input: kind (commit type), extra (arguments), alias (command name)
              - output: Formatted commit message string

- **fix** (Bug Fix): Conventional commit for fixes
  - **Function**: `cmd_fix()`
    - `cmd_fix()`: Creates fix(scope): description commit [`core.py`, 1565-1566]
      - description: Calls conventional commit handler with 'fix' type for bug fixes.
      - input: extra (message arguments)
      - output: CompletedProcess from commit

- **change** (Change): Conventional commit for changes
  - **Function**: `cmd_change()`
    - `cmd_change()`: Creates change(scope): description commit [`core.py`, 1570-1571]
      - description: Calls conventional commit handler with 'change' type for modifications.
      - input: extra (message arguments)
      - output: CompletedProcess from commit

- **refactor** (Refactor): Conventional commit for refactoring
  - **Function**: `cmd_refactor()`
    - `cmd_refactor()`: Creates refactor(scope): description commit [`core.py`, 1560-1561]
      - description: Calls conventional commit handler with 'refactor' type for code restructuring.
      - input: extra (message arguments)
      - output: CompletedProcess from commit

- **docs** (Documentation): Conventional commit for documentation
  - **Function**: `cmd_docs()`
    - `cmd_docs()`: Creates docs(scope): description commit [`core.py`, 1575-1576]
      - description: Calls conventional commit handler with 'docs' type for documentation changes.
      - input: extra (message arguments)
      - output: CompletedProcess from commit

- **style** (Styling): Conventional commit for style changes
  - **Function**: `cmd_style()`
    - `cmd_style()`: Creates style(scope): description commit [`core.py`, 1580-1581]
      - description: Calls conventional commit handler with 'style' type for formatting changes.
      - input: extra (message arguments)
      - output: CompletedProcess from commit

- **revert** (Revert): Conventional commit for reverts
  - **Function**: `cmd_revert()`
    - `cmd_revert()`: Creates revert(scope): description commit [`core.py`, 1585-1586]
      - description: Calls conventional commit handler with 'revert' type for reverting changes.
      - input: extra (message arguments)
      - output: CompletedProcess from commit

- **misc** (Miscellaneous): Conventional commit for misc tasks
  - **Function**: `cmd_misc()`
    - `cmd_misc()`: Creates misc(scope): description commit [`core.py`, 1590-1591]
      - description: Calls conventional commit handler with 'misc' type for miscellaneous tasks.
      - input: extra (message arguments)
      - output: CompletedProcess from commit

- **cover** (Coverage): Conventional commit for requirement coverage
  - **Function**: `cmd_cover()`
    - `cmd_cover()`: Creates cover(scope): description commit [`core.py`, 1595-1596]
      - description: Calls conventional commit handler with 'cover' type for covering requirements.
      - input: extra (message arguments)
      - output: CompletedProcess from commit

### Branch Operations

- **br** (Branch): List or create branches
  - **Function**: `cmd_br()`
    - `cmd_br()`: Executes git branch command [`core.py`, 1480-1481]
      - description: Direct passthrough to `git branch` with extra arguments.
      - input: extra (branch arguments)
      - output: CompletedProcess from git branch

- **bd** (Branch Delete): Delete local branch
  - **Function**: `cmd_bd()`
    - `cmd_bd()`: Deletes local branch [`core.py`, 1485-1486]
      - description: Executes `git branch -d` to delete specified branch.
      - input: extra (branch name)
      - output: CompletedProcess from git branch -d

- **co** (Checkout): Switch branches or restore files
  - **Function**: `cmd_co()`
    - `cmd_co()`: Checks out branch or commit [`core.py`, 1600-1601]
      - description: Direct passthrough to `git checkout` with extra arguments.
      - input: extra (branch/commit/file arguments)
      - output: CompletedProcess from git checkout

- **lb** (List Branches): List all branches with details
  - **Function**: `cmd_lb()`
    - `cmd_lb()`: Lists local and remote branches [`core.py`, 1687-1688]
      - description: Executes `git branch -v -a` to show all branches with last commit info.
      - input: extra (additional arguments)
      - output: CompletedProcess from git branch

### Remote Operations

- **fe** (Fetch): Fetch from remote
  - **Function**: `cmd_fe()`
    - `cmd_fe()`: Fetches updates from remote [`core.py`, 1636-1637]
      - description: Direct passthrough to `git fetch` with extra arguments.
      - input: extra (fetch options)
      - output: CompletedProcess from git fetch

- **feall** (Fetch All): Fetch all remotes with cleanup
  - **Function**: `cmd_feall()`
    - `cmd_feall()`: Fetches all branches and tags with pruning [`core.py`, 1641-1642]
      - description: Calls cmd_fe() with --all --tags --prune flags plus extra arguments.
      - input: extra (additional arguments)
      - output: CompletedProcess from git fetch

- **pl** (Pull): Pull with fast-forward only
  - **Function**: `cmd_pl()`
    - `cmd_pl()`: Pulls changes with fast-forward only [`core.py`, 1741-1742]
      - description: Executes `git pull --ff-only` to fetch and merge safely.
      - input: extra (pull arguments)
      - output: CompletedProcess from git pull

- **pu** (Push): Push with upstream tracking
  - **Function**: `cmd_pu()`
    - `cmd_pu()`: Pushes and sets upstream [`core.py`, 1751-1752]
      - description: Executes `git push -u` to push and set tracking reference.
      - input: extra (push arguments)
      - output: CompletedProcess from git push

- **pt** (Push Tags): Push all tags
  - **Function**: `cmd_pt()`
    - `cmd_pt()`: Pushes all tags to remote [`core.py`, 1746-1747]
      - description: Executes `git push --tags` to push all local tags.
      - input: extra (push arguments)
      - output: CompletedProcess from git push

- **str** (Status Remote): Show detailed remote status
  - **Function**: `cmd_str()`
    - `cmd_str()`: Displays unique remotes and their status [`core.py`, 1656-1683]
      - description: Parses output of `git remote -v` to collect unique remote names, prints list, then executes `git remote show` for each remote to display detailed tracking information.
      - input: extra (ignored)
      - output: None (prints to stdout)
      - calls:
        - `run_git_text()`: Executes git and returns text output [`core.py`, 558-573]
          - description: Runs git command with stdout/stderr captured as text. Raises RuntimeError with decoded stderr if command fails.
          - input: args (git arguments), cwd (working directory), check (raise on error)
          - output: Stdout string stripped

### Tag Operations

- **tg** (Tag): Create annotated tag
  - **Function**: `cmd_tg()`
    - `cmd_tg()`: Creates annotated tag [`core.py`, 1823-1824]
      - description: Executes `git tag -a -m` with message and tag name from extra arguments.
      - input: extra (message and tag name)
      - output: CompletedProcess from git tag

- **rmtg** (Remove Tag): Delete tag locally and remotely
  - **Function**: `cmd_rmtg()`
    - `cmd_rmtg()`: Removes tag from local and origin [`core.py`, 1761-1769]
      - description: Validates tag argument exists, executes `git tag --delete` locally, then `git push --delete origin` to remove from remote.
      - input: extra (tag name and options)
      - output: CompletedProcess from git push

- **lt** (List Tags): List all tags
  - **Function**: `cmd_lt()`
    - `cmd_lt()`: Lists all repository tags [`core.py`, 1731-1732]
      - description: Executes `git tag -l` to list tags.
      - input: extra (tag filter arguments)
      - output: CompletedProcess from git tag

- **de** (Describe): Describe current commit with tags
  - **Function**: `cmd_de()`
    - `cmd_de()`: Describes HEAD with tag information [`core.py`, 1605-1606]
      - description: Executes `git describe` to show most recent tag and commit distance.
      - input: extra (describe options)
      - output: CompletedProcess from git describe

### History and Log Operations

- **lg** (Log Graph): Pretty commit history graph
  - **Function**: `cmd_lg()`
    - `cmd_lg()`: Displays formatted commit graph [`core.py`, 1692-1703]
      - description: Executes git log with custom format showing abbreviated hash, relative date, subject, author, and decorations in color. Uses --graph --all for complete history visualization.
      - input: extra (log options)
      - output: CompletedProcess from git log

- **lh** (Log HEAD): Show last commit details
  - **Function**: `cmd_lh()`
    - `cmd_lh()`: Shows details of latest commit [`core.py`, 1707-1708]
      - description: Executes `git log -1 HEAD` to display HEAD commit information.
      - input: extra (log options)
      - output: CompletedProcess from git log

- **ll** (Log Long): Full hash commit history
  - **Function**: `cmd_ll()`
    - `cmd_ll()`: Displays commit graph with full hashes [`core.py`, 1712-1722]
      - description: Similar to lg but uses full commit hash format with detailed date information.
      - input: extra (log options)
      - output: CompletedProcess from git log

- **lm** (Log Merges): Show merge commits only
  - **Function**: `cmd_lm()`
    - `cmd_lm()`: Lists only merge commits [`core.py`, 1726-1727]
      - description: Executes `git log --merges` to filter merge commits.
      - input: extra (log options)
      - output: CompletedProcess from git log

- **rf** (Reflog): Show reference log
  - **Function**: `cmd_rf()`
    - `cmd_rf()`: Displays reflog history [`core.py`, 1756-1757]
      - description: Executes `git reflog` to show reference update history.
      - input: extra (reflog options)
      - output: CompletedProcess from git reflog

### Reset Operations

- **rs** (Reset): Hard reset to HEAD
  - **Function**: `cmd_rs()`
    - `cmd_rs()`: Resets to HEAD with --hard [`core.py`, 1788-1789]
      - description: Calls reset helper with --hard HEAD, displays help if requested.
      - input: extra (reset arguments)
      - output: CompletedProcess from git reset or None if help
      - calls:
        - `_run_reset_with_help()`: Handles reset with help option [`core.py`, 1308-1313]
          - description: Checks for --help in arguments and prints RESET_HELP text if found, otherwise executes git reset with base_args and extra.
          - input: base_args (reset command), extra (arguments)
          - output: None if help, else CompletedProcess

- **rssft** (Reset Soft): Soft reset
  - **Function**: `cmd_rssft()`
    - `cmd_rssft()`: Resets with --soft mode [`core.py`, 1793-1794]
      - description: Executes `git reset --soft` to move HEAD but keep index and working tree.
      - input: extra (reset arguments)
      - output: CompletedProcess or None if help

- **rsmix** (Reset Mixed): Mixed reset
  - **Function**: `cmd_rsmix()`
    - `cmd_rsmix()`: Resets with --mixed mode [`core.py`, 1798-1799]
      - description: Executes `git reset --mixed` to move HEAD and reset index but keep working tree.
      - input: extra (reset arguments)
      - output: CompletedProcess or None if help

- **rshrd** (Reset Hard): Hard reset
  - **Function**: `cmd_rshrd()`
    - `cmd_rshrd()`: Resets with --hard mode [`core.py`, 1803-1804]
      - description: Executes `git reset --hard` to reset HEAD, index, and working tree.
      - input: extra (reset arguments)
      - output: CompletedProcess or None if help

- **rsmrg** (Reset Merge): Merge reset
  - **Function**: `cmd_rsmrg()`
    - `cmd_rsmrg()`: Resets with --merge mode [`core.py`, 1808-1809]
      - description: Executes `git reset --merge` for merge conflict resolution.
      - input: extra (reset arguments)
      - output: CompletedProcess or None if help

- **rskep** (Reset Keep): Keep reset
  - **Function**: `cmd_rskep()`
    - `cmd_rskep()`: Resets with --keep mode [`core.py`, 1813-1814]
      - description: Executes `git reset --keep` to preserve local changes when safe.
      - input: extra (reset arguments)
      - output: CompletedProcess or None if help

### File Operations

- **di** (Discard): Discard file changes
  - **Function**: `cmd_di()`
    - `cmd_di()`: Discards changes in specified files [`core.py`, 1610-1611]
      - description: Executes `git checkout --` to restore files from index.
      - input: extra (file paths)
      - output: CompletedProcess from git checkout

- **diyou** (Discard Yours): Keep local version in merge
  - **Function**: `cmd_diyou()`
    - `cmd_diyou()`: Resolves conflicts keeping local changes [`core.py`, 1615-1616]
      - description: Executes `git checkout --ours` to accept local version during merge conflicts.
      - input: extra (file paths)
      - output: CompletedProcess from git checkout

- **dime** (Discard Mine): Keep remote version in merge
  - **Function**: `cmd_dime()`
    - `cmd_dime()`: Resolves conflicts keeping remote changes [`core.py`, 1620-1621]
      - description: Executes `git checkout --theirs` to accept remote version during merge conflicts.
      - input: extra (file paths)
      - output: CompletedProcess from git checkout

- **unstg** (Unstage): Remove files from staging
  - **Function**: `cmd_unstg()`
    - `cmd_unstg()`: Un-stages files from index [`core.py`, 1828-1829]
      - description: Executes `git reset --mixed --` to remove files from staging area while keeping working tree changes.
      - input: extra (file paths)
      - output: CompletedProcess from git reset

- **rmloc** (Remove Local): Reset and clean working tree
  - **Function**: `cmd_rmloc()`
    - `cmd_rmloc()`: Hard resets specified files [`core.py`, 1773-1774]
      - description: Executes `git reset --hard --` to discard all changes in files.
      - input: extra (file paths)
      - output: CompletedProcess from git reset

- **rmstg** (Remove Staged): Remove from index
  - **Function**: `cmd_rmstg()`
    - `cmd_rmstg()`: Removes files from index cache [`core.py`, 1778-1779]
      - description: Executes `git rm --cached --` to un-track files without deleting.
      - input: extra (file paths)
      - output: CompletedProcess from git rm

- **rmunt** (Remove Untracked): Clean untracked files
  - **Function**: `cmd_rmunt()`
    - `cmd_rmunt()`: Removes untracked files and directories [`core.py`, 1783-1784]
      - description: Executes `git clean -d -f` to delete untracked files.
      - input: extra (file paths)
      - output: CompletedProcess from git clean

- **ed** (Edit): Open files in configured editor
  - **Function**: `cmd_ed()`
    - `cmd_ed()`: Opens files in editor [`core.py`, 1625-1632]
      - description: Expands user paths and invokes configured editor command for each file.
      - input: extra (file paths)
      - output: CompletedProcess from editor
      - calls:
        - `run_editor_command()`: Executes editor with arguments [`core.py`, 309-310]
          - description: Constructs full editor command and calls run_command().
          - input: args (file paths)
          - output: CompletedProcess from editor
          - calls:
            - `_editor_base_command()`: Parses editor configuration [`core.py`, 293-305]
              - description: Uses shlex.split() to parse editor string from config, falls back to DEFAULT_CONFIG editor if parsing fails.
              - input: None
              - output: List of command parts

### Merge and Diff Operations

- **me** (Merge): Merge with fast-forward only
  - **Function**: `cmd_me()`
    - `cmd_me()`: Merges branch with --ff-only [`core.py`, 1736-1737]
      - description: Executes `git merge --ff-only` to merge only if fast-forward possible.
      - input: extra (branch name)
      - output: CompletedProcess from git merge

- **ck** (Check): Check for conflicts
  - **Function**: `cmd_ck()`
    - `cmd_ck()`: Checks for whitespace and conflict errors [`core.py`, 1490-1491]
      - description: Executes `git diff --check` to identify problematic changes.
      - input: extra (diff options)
      - output: CompletedProcess from git diff

- **st** (Status): Show repository status
  - **Function**: `cmd_st()`
    - `cmd_st()`: Displays git status [`core.py`, 1818-1819]
      - description: Direct passthrough to `git status` with extra arguments.
      - input: extra (status options)
      - output: CompletedProcess from git status

### Archive Operations

- **ar** (Archive): Create tar.gz archive
  - **Function**: `cmd_ar()`
    - `cmd_ar()`: Archives master branch as tar.gz [`core.py`, 1465-1476]
      - description: Determines tag name from master branch, pipes `git archive` output through gzip to create compressed archive file named after tag.
      - input: extra (archive options)
      - output: CompletedProcess from gzip
      - calls:
        - `capture_git_output()`: Executes git and captures output [`core.py`, 523-525]
          - description: Runs git command with stdout=PIPE and returns stripped output string.
          - input: base_args (git arguments), cwd (working directory)
          - output: Stdout string

### Version Management

- **ver** (Verify): Verify version consistency
  - **Function**: `cmd_ver()`
    - `cmd_ver()`: Verifies version across configured files [`core.py`, 1833-1845]
      - description: Uses configured ver_rules to scan files and extract versions. Validates all versions match and prints canonical version or exits with error.
      - input: extra (unused)
      - output: None (prints version or error)
      - calls:
        - `get_version_rules()`: Loads version rules from config [`core.py`, 116-117]
          - description: Calls _load_config_rules() with 'ver_rules' key and DEFAULT_VER_RULES fallback.
          - input: None
          - output: List of (pattern, regex) tuples
          - calls:
            - `_load_config_rules()`: Parses config rules from various formats [`core.py`, 89-112]
              - description: Handles rules as dicts with 'pattern' and 'regex' keys or as tuples/lists. Validates and normalizes to list of (pattern, regex) tuples.
              - input: key (config key name), fallback (default rules)
              - output: List of (pattern, regex) tuples
        - `_determine_canonical_version()`: Detects version from files [`core.py`, 1073-1112]
          - description: Iterates through ver_rules, collects matching files, applies regex to extract versions, validates all versions match. Raises VersionDetectionError on mismatch or no matches.
          - input: root (repository Path), rules (version rules list)
          - output: Version string
          - calls:
            - `_collect_version_files()`: Finds files matching pattern [`core.py`, 1009-1051]
              - description: Executes `git ls-files` to get tracked files, applies pathspec pattern matching, filters excluded paths, returns unique resolved file Paths.
              - input: root (repository Path), pattern (glob pattern)
              - output: List of Path objects
              - calls:
                - `_is_version_path_excluded()`: Checks exclusion patterns [`core.py`, 1055-1056]
                  - description: Tests relative path against VERSION_CLEANUP_PATTERNS regexes to exclude cache/temp directories.
                  - input: relative_path (file path string)
                  - output: Boolean
            - `_iter_versions_in_text()`: Extracts versions from text [`core.py`, 1060-1069]
              - description: Iterates compiled regexes, yields first captured group or full match for each match in text.
              - input: text (file content), compiled_regexes (regex list)
              - output: Generator of version strings

- **chver** (Change Version): Update version in all files
  - **Function**: `cmd_chver()`
    - `cmd_chver()`: Changes version across project [`core.py`, 1849-1917]
      - description: Validates new semver version, determines current version, iterates ver_rules to find and replace version strings in files, confirms update succeeded by re-detecting version.
      - input: extra (new version string)
      - output: None (prints status and exits)
      - calls:
        - `_replace_versions_in_text()`: Replaces version strings in text [`core.py`, 1124-1137]
          - description: Uses regex.finditer() to find version matches, reconstructs text with replacement string, returns (new_text, count).
          - input: text (file content), compiled_regex (version regex), replacement (new version)
          - output: Tuple of (modified text, replacement count)

### Changelog Generation

- **changelog** (Generate Changelog): Generate CHANGELOG.md
  - **Function**: `cmd_changelog()`
    - `cmd_changelog()`: Generates changelog from conventional commits [`core.py`, 1939-1970]
      - description: Parses arguments for flags (--force-write, --include-unreleased, --include-draft, --print-only), generates changelog content from git history, optionally writes to CHANGELOG.md.
      - input: extra (command flags)
      - output: None (prints or writes file)
      - calls:
        - `is_inside_git_repo()`: Validates git repository context [`core.py`, 715-720]
          - description: Executes `git rev-parse --is-inside-work-tree` and checks for "true" output.
          - input: None
          - output: Boolean
        - `generate_changelog_document()`: Builds complete changelog [`core.py`, 959-1004]
          - description: Retrieves all tags, generates unreleased section if requested, iterates tags to create sections for each version with commit categorization, appends history section with compare links.
          - input: repo_root (Path), include_unreleased (bool), include_draft (bool)
          - output: Markdown document string
          - calls:
            - `list_tags_sorted_by_date()`: Gets sorted semver tags [`core.py`, 784-802]
              - description: Executes `git for-each-ref --sort=creatordate` with custom format, filters tags matching semver pattern, returns list of TagInfo objects.
              - input: repo_root (Path), merged_ref (optional branch filter)
              - output: List of TagInfo objects
            - `generate_section_for_range()`: Creates changelog section for version [`core.py`, 852-885]
              - description: Extracts commit subjects from rev_range, categorizes each conventional commit into buckets (Features, Bug Fixes, etc.), builds markdown section with emoji headers and bulleted entries.
              - input: repo_root, title, date_s, rev_range, expected_version
              - output: Markdown section string or None
              - calls:
                - `git_log_subjects()`: Extracts commit messages [`core.py`, 806-815]
                  - description: Executes `git log --no-merges` with custom format, splits by RECORD delimiter, returns list of subject strings.
                  - input: repo_root (Path), rev_range (git range)
                  - output: List of commit subject strings
                - `categorize_commit()`: Parses conventional commit [`core.py`, 819-840]
                  - description: Applies _CONVENTIONAL_RE regex to extract type, scope, description. Maps type to section name and formats as markdown list item.
                  - input: subject (commit message)
                  - output: Tuple of (section name or None, formatted line)
            - `build_history_section()`: Builds history links section [`core.py`, 924-955]
              - description: Generates markdown reference-style links for each tag and optional unreleased section, using GitHub compare URLs.
              - input: repo_root, tags, include_unreleased, include_draft, include_unreleased_link
              - output: Markdown history section string
              - calls:
                - `_canonical_origin_base()`: Extracts GitHub base URL [`core.py`, 889-904]
                  - description: Executes `git remote get-url origin`, parses git@ or https format, strips .git suffix, validates URL structure.
                  - input: repo_root (Path)
                  - output: Base URL string or None
                - `get_origin_compare_url()`: Constructs compare URL [`core.py`, 908-913]
                  - description: Builds GitHub compare URL between two tags or release page URL if no previous tag.
                  - input: base_url, prev_tag, tag
                  - output: Compare URL string or None
                - `get_release_page_url()`: Constructs release page URL [`core.py`, 917-920]
                  - description: Builds GitHub releases/tag URL for given tag.
                  - input: base_url, tag
                  - output: Release page URL string or None

### Release Management

- **major** (Major Release): Release major version
  - **Function**: `cmd_major()`
    - `cmd_major()`: Executes major version release [`core.py`, 1921-1923]
      - description: Parses release flags and calls release command with 'major' level.
      - input: extra (release flags)
      - output: None (exits on completion)
      - calls:
        - `_parse_release_flags()`: Validates release arguments [`core.py`, 1325-1341]
          - description: Checks that only --include-unreleased and --include-draft flags are present, deduplicates flags, returns list.
          - input: extra (arguments), alias (command name)
          - output: List of valid flags
        - `_run_release_command()`: Manages release flow with error handling [`core.py`, 1291-1304]
          - description: Calls _execute_release_flow() and catches ReleaseError, VersionDetectionError, CommandExecutionError to print errors and exit with appropriate codes.
          - input: level (major/minor/patch), changelog_args (flags)
          - output: None (exits on error)
          - calls:
            - `_execute_release_flow()`: Orchestrates full release process [`core.py`, 1247-1287]
              - description: Validates prerequisites, determines current version, bumps version, executes sequence of release steps: update versions, commit, tag, regenerate changelog, amend commit, retag, merge to develop, push, merge to master, push, return to work branch, show release, push tags.
              - input: level (major/minor/patch), changelog_args (flags)
              - output: None (prints status)
              - calls:
                - `_ensure_release_prerequisites()`: Validates release conditions [`core.py`, 1176-1201]
                  - description: Checks master/develop/work branches exist locally and remotely, validates no remote updates pending, ensures current branch is work, verifies no unstaged or staged changes.
                  - input: None
                  - output: Dictionary with branch names
                  - calls:
                    - `_local_branch_exists()`: Checks local branch existence [`core.py`, 1166-1167]
                      - description: Calls _ref_exists() with refs/heads/ prefix.
                      - input: branch_name
                      - output: Boolean
                      - calls:
                        - `_ref_exists()`: Verifies git reference [`core.py`, 1155-1162]
                          - description: Executes `git show-ref --verify --quiet` with ref name, returns True if exit code 0.
                          - input: ref_name
                          - output: Boolean
                    - `_remote_branch_exists()`: Checks remote branch existence [`core.py`, 1171-1172]
                      - description: Calls _ref_exists() with refs/remotes/origin/ prefix.
                      - input: branch_name
                      - output: Boolean
                    - `_refresh_remote_refs()`: Updates remote references [`core.py`, 619-628]
                      - description: Executes `git remote -v update` once per session to refresh remote tracking branches. Sets global flag to prevent repeated calls.
                      - input: None
                      - output: None
                    - `has_remote_branch_updates()`: Checks for remote commits [`core.py`, 652-654]
                      - description: Calls _branch_remote_divergence() and returns True if remote_ahead > 0.
                      - input: branch_key (config key), remote (remote name)
                      - output: Boolean
                      - calls:
                        - `_branch_remote_divergence()`: Calculates commit divergence [`core.py`, 632-648]
                          - description: Refreshes remote refs, executes `git rev-list --left-right --count` to compare local and remote branches, parses counts.
                          - input: branch_key, remote
                          - output: Tuple of (local_ahead, remote_ahead) integers
                - `_bump_semver_version()`: Increments version number [`core.py`, 1205-1221]
                  - description: Parses current version to tuple, increments major/minor/patch according to level, resets lower components to zero.
                  - input: current_version, level (major/minor/patch)
                  - output: New version string
                - `_run_release_step()`: Executes and logs release step [`core.py`, 1225-1243]
                  - description: Calls action lambda, prints success message with [release:level] label, catches and wraps exceptions as ReleaseError with step name.
                  - input: level, step_name, action (callable)
                  - output: Action result or raises ReleaseError
                - `cmd_release()`: Creates release commit [`core.py`, 1531-1551]
                  - description: Validates commit ready, determines current version, creates commit with 'release version: X.Y.Z' message.
                  - input: extra (must be empty)
                  - output: CompletedProcess from git commit

- **minor** (Minor Release): Release minor version
  - **Function**: `cmd_minor()`
    - `cmd_minor()`: Executes minor version release [`core.py`, 1927-1929]
      - description: Parses release flags and calls release command with 'minor' level.
      - input: extra (release flags)
      - output: None (exits on completion)

- **patch** (Patch Release): Release patch version
  - **Function**: `cmd_patch()`
    - `cmd_patch()`: Executes patch version release [`core.py`, 1933-1935]
      - description: Parses release flags and calls release command with 'patch' level.
      - input: extra (release flags)
      - output: None (exits on completion)

### Visual Tools

- **gp** (Git Program): Open gitk with all commits
  - **Function**: `cmd_gp()`
    - `cmd_gp()`: Opens gitk GUI for all branches [`core.py`, 1646-1647]
      - description: Executes `gitk --all` to visualize complete commit graph.
      - input: extra (gitk options)
      - output: CompletedProcess from gitk
      - calls:
        - `run_command()`: Executes external command [`core.py`, 529-530]
          - description: Calls _run_checked() with cmd list and optional cwd.
          - input: cmd (command list), cwd (working directory)
          - output: CompletedProcess

- **gr** (Git References): Open simplified gitk
  - **Function**: `cmd_gr()`
    - `cmd_gr()`: Opens gitk with simplified decoration view [`core.py`, 1651-1652]
      - description: Executes `gitk --simplify-by-decoration --all` to show only tagged/branched commits.
      - input: extra (gitk options)
      - output: CompletedProcess from gitk

## Workflow Automation

### CI/CD Pipeline (.github/workflows/release-uvx.yml)

- **Release Build**: Automated GitHub release on tag push
  - **Trigger**: Push of v* tags
  - **Jobs**:
    - **build-release**: Builds and publishes Python package
      - **Steps**:
        1. Checkout repository with full history
        2. Setup Python 3.11 environment
        3. Setup uv package manager
        4. Install build dependencies from requirements.txt
        5. Build distribution packages (wheel and sdist)
        6. Attest build provenance for security
        7. Create GitHub release with generated notes and upload artifacts

## Configuration System

- **Configuration File**: `.g.conf` (JSON format)
  - **Default Configuration Values**:
    - `master`: "master" - Name of production branch
    - `develop`: "develop" - Name of development branch
    - `work`: "work" - Name of working branch
    - `editor`: "edit" - Default editor command
    - `default_module`: "core" - Default scope for conventional commits
    - `ver_rules`: List of version detection rules with pattern and regex

- **Configuration Functions**:
  - `get_config_value()`: Retrieves config value with fallback [`core.py`, 72-73]
    - description: Returns CONFIG[name] or DEFAULT_CONFIG[name] if not found.
    - input: name (config key)
    - output: Configuration value
  - `get_branch()`: Gets configured branch name [`core.py`, 77-80]
    - description: Validates key is in BRANCH_KEYS, returns configured branch name.
    - input: name (branch key: master/develop/work)
    - output: Branch name string
  - `get_editor()`: Gets editor command [`core.py`, 84-85]
    - description: Returns configured editor command string.
    - input: None
    - output: Editor command string

## Error Handling

- **Exception Classes**:
  - `CommandExecutionError`: Subprocess execution failures [`core.py`, 462-494]
    - description: Wraps subprocess.CalledProcessError with formatted error messages. Decodes stderr/stdout streams to provide meaningful error text. Stores cmd, returncode, stdout, stderr attributes.
  - `VersionDetectionError`: Version consistency issues [`core.py`, 507-508]
    - description: Raised when version detection fails due to missing files, no matches, or version mismatches between files.
  - `ReleaseError`: Release workflow problems [`core.py`, 512-513]
    - description: Raised for release prerequisite failures, branch validation errors, or release step execution failures.

## Utility Functions

- **Git Operations**:
  - `run_git_cmd()`: Basic git command execution [`core.py`, 517-519]
  - `capture_git_output()`: Git command with output capture [`core.py`, 523-525]
  - `run_git_text()`: Git command returning text [`core.py`, 558-573]
  - `run_shell()`: Shell command execution [`core.py`, 553-554]

- **Status Checking**:
  - `_git_status_lines()`: Get status porcelain output [`core.py`, 577-587]
  - `has_unstaged_changes()`: Check for working tree changes [`core.py`, 591-600]
  - `has_staged_changes()`: Check for staged changes [`core.py`, 604-611]
  - `has_remote_develop_updates()`: Check develop branch updates [`core.py`, 658-659]
  - `has_remote_master_updates()`: Check master branch updates [`core.py`, 663-664]

- **Version Parsing**:
  - `_normalize_semver_text()`: Normalize version string [`core.py`, 134-138]
  - `_parse_semver_tuple()`: Parse semver to tuple [`core.py`, 1115-1120]
  - `_tag_semver_tuple()`: Extract semver from tag [`core.py`, 756-757]
  - `_is_supported_release_tag()`: Check tag version support [`core.py`, 761-765]

- **Text Processing**:
  - `_to_args()`: Convert extra arguments to list [`core.py`, 457-458]
  - `_reject_extra_arguments()`: Validate no extra args [`core.py`, 1317-1321]

## Common Code Logic

### Commit Validation Pattern

All commit commands (cm, wip, conventional commits) follow the same validation pattern:
1. Check for unstaged changes (must be none)
2. Check for staged changes (must exist)
3. Determine if existing WIP commit should be amended
4. Execute commit with message (new or amend)

### Version File Discovery Pattern

Version management commands (ver, chver) use consistent file discovery:
1. Load ver_rules from configuration
2. For each rule, execute `git ls-files` to get tracked files
3. Apply pathspec pattern matching to filter files
4. Exclude cache/temp directories via VERSION_CLEANUP_PATTERNS
5. Read files and apply regex to extract/replace versions
6. Validate all versions match across files

### Release Workflow Pattern

All release commands (major, minor, patch) execute identical flow:
1. Validate prerequisites (branches exist, no remote updates, clean state)
2. Determine current version from files
3. Bump version according to level
4. Update version files
5. Stage all changes
6. Create release commit
7. Create version tag
8. Regenerate changelog with new version
9. Amend commit to include changelog
10. Force-retag with updated commit
11. Merge work → develop → master
12. Push branches and tags

### Remote Update Checking Pattern

Remote operations refresh refs once per session, then compare local and remote branches:
1. Execute `git remote -v update` (once per session via global flag)
2. Execute `git rev-list --left-right --count local...remote`
3. Parse counts to determine divergence
4. Cache results to avoid repeated API calls

### Conventional Commit Pattern

All conventional commit commands share message formatting logic:
1. Parse arguments for module prefix (e.g., "core: message")
2. Extract scope and body, or use default_module from config
3. Format as "type(scope): body"
4. Execute commit with validation checks
