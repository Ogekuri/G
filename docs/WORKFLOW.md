## Execution Units Index

- `PROC:main`
  - Type: Process
  - Role: Main CLI process
  - Entrypoint: `src/git_alias/__main__.py`, `src/git_alias/core.py:main`
  - Defining File: `src/git_alias/core.py`

- `PROC:build-release`
  - Type: Process
  - Role: GitHub Actions Build & Release Job
  - Entrypoint: `.github/workflows/release-uvx.yml`
  - Defining File: `.github/workflows/release-uvx.yml`

## Execution Units

### `PROC:main`

- **Entrypoint**: `src/git_alias/__main__.py` -> `src/git_alias/core.py:main`
- **Lifecycle/Trigger**: Ephemeral process triggered by user CLI invocation. Exits after command execution.
- **Internal Call-Trace Tree**:
  - `main(argv, check_updates)`: Dispatcher and entrypoint [src/git_alias/core.py]
    - `get_git_root()`: Resolve repository root [src/git_alias/core.py]
      - `_run_checked(...)`: Execute git rev-parse [src/git_alias/core.py]
    - `load_cli_config(root)`: Load .g.conf [src/git_alias/core.py]
      - `get_config_path(root)`: Resolve config path [src/git_alias/core.py]
    - `check_for_newer_version(timeout_seconds)`: Check GitHub for updates [src/git_alias/core.py]
      - `get_cli_version()`: Read local version [src/git_alias/core.py]
      - `_parse_semver_tuple(text)`: Parse version string [src/git_alias/core.py]
      - `_normalize_semver_text(text)`: Normalize version string [src/git_alias/core.py]
      - External Boundary: `urllib.request.urlopen` (HTTP GET https://api.github.com/repos/Ogekuri/G/releases/latest)
    - `write_default_config(root)`: [src/git_alias/core.py]
      - `get_config_path(root)`: [src/git_alias/core.py]
    - `upgrade_self()`: [src/git_alias/core.py]
    - `remove_self()`: [src/git_alias/core.py]
    - `print_all_help()`: [src/git_alias/core.py]
    - `print_command_help(name)`: [src/git_alias/core.py]
    - `cmd_*(...)`: Command handlers [src/git_alias/core.py]
      - `cmd_aa(extra)`: Stage all [src/git_alias/core.py]
        - `run_git_cmd(...)`: Execute git add [src/git_alias/core.py]
      - `cmd_cm(extra)`: Commit [src/git_alias/core.py]
        - `_execute_commit(message, ...)`: [src/git_alias/core.py]
          - `_ensure_commit_ready(...)`: [src/git_alias/core.py]
            - `has_unstaged_changes(...)`: [src/git_alias/core.py]
            - `has_staged_changes(...)`: [src/git_alias/core.py]
          - `run_git_cmd(...)`: Execute git commit [src/git_alias/core.py]
      - `cmd_major(extra)`: Release major [src/git_alias/core.py]
        - `_run_release_command('major', ...)`: [src/git_alias/core.py]
          - `_execute_release_flow('major', ...)`: [src/git_alias/core.py]
            - `_ensure_release_prerequisites()`: [src/git_alias/core.py]
              - `get_branch(name)`: [src/git_alias/core.py]
              - `_local_branch_exists(...)`: [src/git_alias/core.py]
              - `_remote_branch_exists(...)`: [src/git_alias/core.py]
              - `has_remote_branch_updates(...)`: [src/git_alias/core.py]
            - `get_version_rules()`: [src/git_alias/core.py]
              - `_load_config_rules(...)`: [src/git_alias/core.py]
            - `_determine_canonical_version(...)`: [src/git_alias/core.py]
              - `_collect_version_files(...)`: [src/git_alias/core.py]
            - `_bump_semver_version(...)`: [src/git_alias/core.py]
            - `_run_release_step(...)`: Execute release steps [src/git_alias/core.py]
              - `cmd_chver(...)`: Change version [src/git_alias/core.py]
              - `cmd_tg(...)`: Tag [src/git_alias/core.py]
              - `cmd_changelog(...)`: Generate changelog [src/git_alias/core.py]
                - `generate_changelog_document(...)`: [src/git_alias/core.py]
                  - `list_tags_sorted_by_date(...)`: [src/git_alias/core.py]
                  - `generate_section_for_range(...)`: [src/git_alias/core.py]
                    - `git_log_subjects(...)`: [src/git_alias/core.py]
                    - `categorize_commit(...)`: [src/git_alias/core.py]
      - `cmd_minor(extra)`: Release minor [src/git_alias/core.py]
        - `_run_release_command('minor', ...)`: [src/git_alias/core.py]
      - `cmd_patch(extra)`: Release patch [src/git_alias/core.py]
        - `_run_release_command('patch', ...)`: [src/git_alias/core.py]
      - `cmd_wip(extra)`: Work in progress [src/git_alias/core.py]
        - `_should_amend_existing_commit()`: [src/git_alias/core.py]
        - `run_git_cmd(...)`: [src/git_alias/core.py]
      - `cmd_ver(extra)`: Verify versions [src/git_alias/core.py]
        - `_determine_canonical_version(...)`: [src/git_alias/core.py]
- **External Boundaries**:
  - `subprocess.run`: Invoking `git` executable for all operations.
  - `urllib.request.urlopen`: Fetching latest release info from GitHub API.
  - Filesystem: Reading/Writing `.g.conf`, `.g_version_check_cache.json`, `CHANGELOG.md`, and source files for version bumping.
  - `sys.stdout/stderr`: User interaction.

### `PROC:build-release`

- **Entrypoint**: `.github/workflows/release-uvx.yml`
- **Lifecycle/Trigger**: Triggered by `push` event on tags matching `v*`.
- **Internal Call-Trace Tree**:
  - `jobs:build-release`: Main job [.github/workflows/release-uvx.yml]
    - `steps:checkout`: uses actions/checkout@v4 [.github/workflows/release-uvx.yml]
    - `steps:setup-python`: uses actions/setup-python@v5 [.github/workflows/release-uvx.yml]
    - `steps:setup-uv`: uses astral-sh/setup-uv@v3 [.github/workflows/release-uvx.yml]
    - `steps:install-deps`: run uv pip install [.github/workflows/release-uvx.yml]
    - `steps:build`: run python -m build [.github/workflows/release-uvx.yml]
    - `steps:attest`: uses actions/attest-build-provenance@v1 [.github/workflows/release-uvx.yml]
    - `steps:create-release`: uses softprops/action-gh-release@v2 [.github/workflows/release-uvx.yml]
- **External Boundaries**:
  - GitHub Actions Runner Environment.
  - PyPI (via `uv pip install`).
  - GitHub API (via actions).

## Communication Edges

- **Edge 1**: `PROC:main` -> `Subprocess (git)`
  - Direction: Outbound
  - Mechanism: `subprocess.run` (IPC)
  - Endpoint: `git` executable in PATH
  - Payload: Git commands/arguments
  - Evidence: `src/git_alias/core.py:run_git_cmd`, `src/git_alias/core.py:_run_checked`

- **Edge 2**: `PROC:main` -> `GitHub API`
  - Direction: Outbound
  - Mechanism: HTTP/HTTPS
  - Endpoint: `https://api.github.com/repos/Ogekuri/G/releases/latest`
  - Payload: JSON response (release info)
  - Evidence: `src/git_alias/core.py:check_for_newer_version`, `src/git_alias/core.py:GITHUB_LATEST_RELEASE_API`

- **Edge 3**: `PROC:main` -> `Filesystem (Config/Cache)`
  - Direction: Read/Write
  - Mechanism: File I/O
  - Endpoint: `.g.conf`, `.g_version_check_cache.json`
  - Payload: JSON configuration and cache data
  - Evidence: `src/git_alias/core.py:load_cli_config`, `src/git_alias/core.py:check_for_newer_version`

- **Edge 4**: `PROC:build-release` -> `GitHub API`
  - Direction: Outbound
  - Mechanism: GitHub Actions API
  - Endpoint: GitHub Release / Attestation APIs
  - Payload: Build artifacts (`dist/*`), Provenance data
  - Evidence: `.github/workflows/release-uvx.yml` steps using `actions/attest-build-provenance` and `softprops/action-gh-release`
