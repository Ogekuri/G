🚧 **DRAFT:** Preliminary Version 📝 - Work in Progress 🏗️ 🚧

⚠️ **IMPORTANT NOTICE**: Created with **[useReq/req](https://github.com/Ogekuri/useReq)** 🤖✨ ⚠️

# G/Git-Alias CLI (0.0.42)

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/license-GPL--3.0-491?style=flat-square" alt="License: GPL-3.0">
  <img src="https://img.shields.io/badge/platform-Linux-6A7EC2?style=flat-square&logo=terminal&logoColor=white" alt="Platforms">
  <img src="https://img.shields.io/badge/docs-live-b31b1b" alt="Docs">
<img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json" alt="uv">
</p>

<p align="center">
<strong>Git-Alias CLI provides a command-line interface to replicate the Git aliases defined in this package.</strong><br>
This allows them to be run both as a Python package (installed as <b>g</b> or <b>git-alias</b>) and directly using <b>uvx</b>.<br>
This is a companion script for the <b><a href="https://github.com/Ogekuri/useReq">useReq</a></b> app.
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> |
  <a href="#feature-highlights">Feature Highlights</a> |
  <a href="#upgrading-or-removing">Upgrading or Removing</a> |
  <a href="#cli-examples">CLI Examples</a>
<p>


## Feature Highlights
- Support [Conventional Commit Standards](https://www.conventionalcommits.org/en/v1.0.0/) compatible with [release-changelog-builder-action](https://github.com/mikepenz/release-changelog-builder-action).
- Auto-amending `wip` command for day-to-day "work in progress" commits.
- Common aliases for repetitive tasks like `add --all` (`aa`) and more.
- Acts like a `.gitconfig` [alias] section, providing all standard Git commands with a fallback mechanism.
- Customizable three-branch workflow: `master`, `develop`, and `work`.
- Standardized commits with specific commands like: `new(core): foo bar..`. Use these commands for common activities such as:
    - `new`: Implement new features.
    - `fix`: Bug fixes.
    - `change`: Software changes.
    - `docs`: Add/modify documentation.
    - `style`: Styling modifications.
    - `revert`: Revert changes.
    - `misc`: Miscellaneous tasks.
- Provides `major`, `minor`, and `patch` commands that auto-generate a `CHANGELOG.md`, create a new tag and commit, and release a new `x.y.z` version on the `master` branch.
- Version management commands: `ver` checks version consistency (supports `--verbose`/`--debug`), `chver <major.minor.patch>` updates files matched by `ver_rules`, and `changelog` generates `CHANGELOG.md` (supports `--force-write`, `--include-unreleased`, `--include-draft`, `--print-only`).
- Self-upgrading feature.

## Quick Start

### Prerequisites

- Use supported environment: `linux`
- Install the `uv` tool from: [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)


### Install G/Git-Alias

  - Install or Upgrade
  ```bash
  uv tool install git-alias --force --from git+https://github.com/Ogekuri/G.git
  ```

  - Run Directly from the Repository
  ```bash
  uvx --from git+https://github.com/Ogekuri/G.git git-alias <alias> [args...]
  ```


### Create a `.g.conf` Configuration File

```bash
g --write-config
```


### Edit the `.g.conf` Configuration File

- Customize your `.g.conf` JSON file with `master`, `develop`, `work`, `editor`, and `default_module` values.
- Configure `ver_rules` (pattern/regex pairs) to define which files `g ver`, `g chver`, and release commands read/update for version consistency.


### Work-in-Progress Commits

```bash
g st
g aa
g wip
```


### Override a `wip` Commit with a Final Commit

```bash
g aa
g new(core): foo bar
```

### Release a New Version (with all changes committed)

When your `work` branch is fully committed, release a new version with:

```bash
g minor
```

The command must run from the `work` branch with a clean working tree; it bumps versions per `ver_rules`, creates/retags an annotated `v<next>` tag, regenerates `CHANGELOG.md`, merges `work` -> `develop` -> `master`, and pushes branches and tags to `origin`.

## Management Commands

Upgrade or remove the Git-Alias CLI:

- `g --upgrade` / `git-alias --upgrade`: Upgrades the tool to the latest version from the GitHub repository.
- `g --remove` / `git-alias --remove`: Uninstalls the tool.
- `g --ver` / `g --version` / `git-alias --version`: Prints the CLI version.
- `g --help` / `git-alias --help`: Prints management commands, configuration parameters, and the alias list; use `g --help <alias>` for a single command.


## CLI Examples

Some CLI examples:

- `g --help` / `git-alias --help`: Prints management commands, configuration parameters, and the alias list; use `g --help <alias>` for a single command.
- `g lg --help`: Shows the help text for the `lg` alias.
- `g cm "Message"`: Runs `git commit` with the provided message.
- `g ver --verbose`: Verifies version consistency with detailed output.
- `g chver 1.2.3`: Updates the project version to 1.2.3 using `ver_rules`.
- `g changelog --print-only`: Prints the generated changelog without writing `CHANGELOG.md`.
