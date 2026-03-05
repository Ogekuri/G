---
title: "Git-Alias CLI Requirements"
description: "Software Requirements Specification"
date: "2026-02-25"
author: "Francesco Rolando"
scope:
  paths:
    - "src/**/*.py"
    - ".github/workflows/**/*.yml"
  excludes:
    - "tests/**"
    - "doxygen/**"
visibility: "draft"
tags: ["requirements", "srs", "git-alias"]
---

# Git-Alias CLI Requirements
**Version**: 0.98
**Author**: Francesco Rolando
**Date**: 2026-02-25

## Revision History
| Date | Version | Change Summary |
|------|---------|----------------|
| 2026-02-24 | 0.97 | Added `l` command contracts and foresta engine requirements. |
| 2026-02-25 | 0.98 | Recreated SRS structure in English from repository evidence while preserving existing requirement IDs and appending workflow coverage requirements. |

## 1. Introduction
This SRS defines machine-testable requirements for the Git-Alias CLI and associated release automation implemented in the repository.

### 1.1 Document Rules
- The document MUST be written in English.
- Requirement identifiers MUST remain unique and stable once assigned.
- Existing requirement IDs MUST NOT be renumbered or reused for different behavior.
- Requirement statements MUST use RFC 2119 keywords (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY).
- Each requirement MUST be atomic, verifiable, and testable.

### 1.2 Project Scope
The project provides a Python CLI (`git-alias` / `g`) that executes curated git aliases, manages local/global configuration, automates release-oriented operations, and exposes text/GUI repository inspection commands.

## 2. Project Requirements
### 2.1 Project Functions
- **PRJ-001**: MUST expose `git-alias` and `g` commands that dispatch to aliases implemented in `core.py` for execution in the current git repository.
- **PRJ-002**: MUST provide integrated help that lists available aliases and prints each alias description in English.
- **PRJ-003**: MUST support self-upgrade and self-removal through dedicated CLI management commands (`--upgrade`, `--remove`).

### 2.2 Project Constraints
- **CTN-001**: MUST require Python 3.11 or newer at runtime.
- **CTN-002**: MUST require `git` in PATH and depend on `gitk` and `uv` availability for related aliases and management flows.
- **CTN-003**: MUST file-edit aliases MUST use a CLI-invokable editor configured by `edit_command` in `$HOME/.g/g.conf`, defaulting to `edit` when the file, key, or value is missing or invalid.

### 2.3 Components and Libraries
- **CPT-001**: MUST implement CLI dispatch and alias runtime behavior in `src/git_alias/core.py`.
- **CPT-002**: MUST provide package entrypoints through `src/git_alias/__main__.py` and console scripts `git-alias` and `g`.
- **CPT-003**: MUST include automated tests under `tests/` covering user-visible command contracts.
- **CPT-004**: MUST treat `requirements.txt` as canonical dependency inventory and keep `pyproject.toml` or `setup.py` synchronized with it, with all listed packages limited to runtime execution or package build operations.
- **CPT-005**: MUST invoke external executables `git`, `gitk`, and `uv`/`uvx` for delegated operations.
- **CPT-006**: MUST use `pathspec` for gitignore-style pattern matching in version rules processing.
- **CPT-007**: MUST include root-level `doxygen.sh` to orchestrate Doxygen documentation generation.
- **CPT-008**: MUST include `src/git_alias/foresta.py` implementing text-based commit tree visualization.

## 3. Software Requirements
### 3.1 Design and Implementation
- **DES-001**: MUST accept the first CLI argument as command, dispatch mapped aliases, and fallback to native `git <command> <args>` when command is unknown while preserving help/error behavior.
- **DES-002**: MUST forward extra arguments to delegated git commands, propagate external exit codes, and convert subprocess failures into explicit user-facing errors without raw Python tracebacks.
- **DES-003**: MUST define help text for every command and list commands alphabetically in global help output.
- **DES-004**: MUST print an explicit message plus full help and exit non-zero when invoked without arguments.
- **DES-005**: MUST compose complex aliases by reusing simpler alias functions when overlapping behavior exists.
- **DES-006**: MUST the executable MUST load `.g.conf` for `master`, `develop`, `work`, `default_commit_module`, and `ver_rules`, and `$HOME/.g/g.conf` for `edit_command`, `gp_command`, and `gr_command`, and MUST ignore out-of-scope keys in each file.
- **DES-007**: MUST centralize commit-readiness checks in reusable functions shared by `cm`, `wip`, and related aliases; readiness MUST succeed when staging is non-empty OR working-tree is dirty; MUST fail when both staging and working-tree have no committable data; MUST invoke `aa` to auto-stage working-tree changes when staging is empty and working-tree is dirty.
- **DES-008**: MUST print all console messages in English.
- **DES-009**: MUST the global `--help` output MUST be ordered as usage, Management Commands, Configuration Parameters, and Commands, and Configuration Parameters MUST print resolved values from `.g.conf` plus `$HOME/.g/g.conf`, otherwise defaults from `DEFAULT_CONFIG`.

### 3.2 Functional Requirements
- **REQ-001**: MUST reinstall the utility via `uv tool install git-alias --force --from git+https://github.com/Ogekuri/G.git` when `--upgrade` is invoked.
- **REQ-002**: MUST uninstall the utility via `uv tool uninstall git-alias` when `--remove` is invoked.
- **REQ-003**: MUST show global command help or specific command help via `--help`, and per-command help text MUST explicitly list supported options when present.
- **REQ-004**: MUST execute `git add --all` for alias `aa` only after reusable diagnostics confirm pending unstaged/untracked changes, and MUST fail with explicit error when nothing can be added.
- **REQ-005**: MUST validate `cm` preconditions (no unstaged changes, non-empty index, and WIP-amend decision) and MUST amend `wip: work in progress.` only when not yet merged to configured `develop` and `master`.
- **REQ-006**: MUST support targeted branch checkout via `co` using configured branch names from `.g.conf` defaults (`work`, `develop`, `master`).
- **REQ-007**: MUST implement generic current-branch fetch/pull/push aliases (`fe`, `feall`, `pl`, `pt`, `pu`) without dedicated per-branch shortcuts.
- **REQ-008**: MUST inspection aliases MUST provide branch, log, and status views via `br`, `lb`, `ck`, `l`, `lg`, `ll`, `lm`, `lh`, `lt`, `ver`, `gp`, `gr`, `de`, `rf`, `st`, `str`, `dw`, `dwc`, `dcc`, `dc`, `ls`, `lsi`, `lsa`.
- **REQ-009**: MUST provide generic merge integration through alias `me` for configured branch workflows without extra automation wrappers.
- **REQ-010**: MUST the system MUST limit automated workflow aliases to the documented set (currently `major`, `minor`, `patch`, `backup`) and MUST NOT introduce additional automatic workflow shortcuts beyond those specified.
- **REQ-011**: MUST provide reset/cleanup aliases (`rs`, `rssft`, `rsmix`, `rshrd`, `rsmrg`, `rskep`, `unstg`, `rmloc`, `rmstg`, `rmunt`) and MUST print dedicated reset help when `rs*` commands receive `--help`.
- **REQ-012**: MUST tagging and archive aliases MUST support annotated tag creation (`tg`), local/remote tag deletion (`rmtg`), tag listing (`lt`), and archiving configured `master` in tar.gz (`ar`).
- **REQ-013**: MUST open file paths through `ed` using `edit_command` from `$HOME/.g/g.conf` (default `edit`) and MUST fail with explicit error when no path is supplied.
- **REQ-014**: MUST normalize `.g.conf` to keys `master`, `develop`, `work`, `default_commit_module`, `ver_rules` and normalize `$HOME/.g/g.conf` to keys `edit_command`, `gp_command`, `gr_command` when `--write-config` runs.
- **REQ-015**: MUST migrate legacy global key `editor` to `edit_command` during `--write-config` when `edit_command` is missing, and MUST remove `editor` from persisted output.
- **REQ-016**: MUST show management commands before alias listings when global help is requested or when command input is missing.
- **REQ-017**: MUST evaluate `ver_rules` from `.g.conf` (or defaults), build repository candidates from `git ls-files`, apply pathspec matching plus hardcoded cache/temp exclusions, and fail on mismatched or missing version matches as specified.
- **REQ-118**: MUST abort `ver` and `chver` when a `ver_rules.pattern` matches zero repository files, and MUST report the offending pattern with guidance that only repository files can be configured in `ver_rules.pattern`.
- **REQ-018**: MUST the `changelog` command MUST generate `CHANGELOG.md` grouping commits by minor releases (semver tags where `patch=0` AND version `>=0.1.0`); MUST include only minor releases by default with all commits between consecutive minor releases (from repository beginning for the first minor); MUST produce an empty changelog body when no minor releases exist; MUST list releases reverse-chronologically (newest first).
- **REQ-019**: MUST delete a user-specified local branch via `git branch -d <branch>` for alias `bd`.
- **REQ-020**: MUST provide reusable checks for unstaged changes, staged changes, and remote-forward status of configured `develop` and `master`, including remote reference update before ahead/behind evaluation.
- **REQ-021**: MUST implement `wip` using the fixed message `wip: work in progress.`; MUST call `aa` (stage all) when staging is empty and working-tree is dirty; MUST fail with explicit error when both working-tree and staging have no committable data.
- **REQ-022**: MUST aliases `new`, `fix`, `change`, `implement`, `refactor`, `docs`, `style`, `revert`, `misc`, and `cover` execute conventional commits; MUST call `aa` when staging is empty and working-tree is dirty; MUST fail with explicit error when both working-tree and staging have no committable data; MUST reuse WIP-amend decision logic used by `cm` and `wip`.
- **REQ-115**: MUST conventional aliases require non-empty commit text and support optional `<module>: <description>` prefix parsing before message construction.
- **REQ-116**: MUST resolve omitted module from `.g.conf.default_commit_module`; when key is absent use hardcoded default `""`; when effective module is empty emit `<type>: <description>`, otherwise emit `<type>(<module>): <description>`.
- **REQ-117**: MUST uppercase the first character of `<description>` unless numeric and MUST append `.` when `<description>` does not already end with a period.
- **REQ-023**: MUST keep all `core.py` output messages (stdout/stderr, normal/verbose/debug, help/errors) in English.
- **REQ-025**: MUST require exactly one `major.minor.patch` argument for `chver`, update matching version occurrences from active `ver_rules`, and re-run `ver` to confirm the requested target version.
- **REQ-026**: MUST the `major`, `minor`, and `patch` commands MUST automate version release by incrementing the corresponding semver index (resetting lower-order indices), MUST share the same support implementation, MUST accept `--include-patch` flag forwarded to `changelog` together with `--force-write`; the `patch` command MUST automatically include `--include-patch` in the changelog regeneration step even when the flag is not supplied by the user; the `major` and `minor` commands MUST NOT automatically include `--include-patch`, MUST enforce release prerequisites on configured local branches (`master`, `develop`, `work`), configured remotes (`origin/master`, `origin/develop`), remote update status for `master` and `develop`, current branch equal to `work`, clean working tree, and empty index, MUST print release step logs in the `--- [release:<level>] ... ---` format with one blank line before the first release step, and after `chver` plus staging MUST create the first release commit by amending HEAD when HEAD is an amendable `wip: work in progress.` commit not yet contained in configured `develop` and `master` or by creating a new commit otherwise; before changelog regeneration the flow MUST create a temporary annotated `v<target>` tag on configured local `work`, MUST regenerate changelog, and MUST delete that temporary local tag before any branch integration.
- **REQ-027**: MUST the internal `cmd_release` function MUST reuse the same staging/worktree readiness and WIP amend decision logic used by `wip`, MUST determine the current version via `ver` before committing, MUST fail with the propagated detection error when version resolution fails, MUST create a `release: Release version <ver>` commit (where `<ver>` is `major.minor.patch`) by amending HEAD only when HEAD is an amendable `wip: work in progress.` commit not yet contained in configured `develop` and `master` and otherwise by creating a new commit, and MUST remain unavailable as a user-exposed CLI command.
- **REQ-028**: MUST implement `ra` as inverse of `aa` by requiring configured `work` branch, no pending unstaged changes, and non-empty staging before unstaging all indexed entries.
- **REQ-029**: MUST print usage with package version suffix `(x.y.z)` when CLI is invoked without command arguments.
- **REQ-030**: MUST print the package version and exit successfully when invoked with `--ver` or `--version`.
- **REQ-031**: MUST keep all CLI output messages in English, including usage/help/info/debug/error paths.
- **REQ-033**: MUST perform pre-execution latest-version checks using a 6-hour temp-file cache `.g_version_check_cache.json`, fetch GitHub release data with 1-second timeout when cache is stale, and continue silently on network/cache failures.
- **REQ-034**: MUST run `git remote -v`, print unique remote names, and run `git remote show <remote>` for each discovered remote in alias `str`.
- **REQ-035**: MUST support `ver --verbose` (per-file regex outcome output) and `ver --debug` (full glob-match listing for each rule pattern).
- **REQ-036**: MUST provide executable root script `doxygen.sh` that runs system `doxygen` to generate HTML/PDF/Markdown documentation under `doxygen/` from `src/`, and generated API docs MUST include every declaration indexed in `docs/REFERENCES.md`.
- **REQ-037**: MUST visual diff aliases MUST execute fixed `git difftool -d` mappings: `dwc` MUST execute `git difftool -d HEAD` (working tree vs latest commit), `dcc` MUST execute `git difftool -d HEAD~1 HEAD` (penultimate vs latest commit), `dc` MUST require exactly two positional git refs (`<ref_a> <ref_b>`) and execute `git difftool -d <ref_a> <ref_b>`, and `dw` MUST require exactly one positional git ref (`<ref>`) and execute `git difftool -d <ref>` (working tree vs specified ref), forwarding git errors without additional transformations.
- **REQ-038**: MUST the visual diff aliases MUST include `dwcc` mapped to `git difftool -d HEAD~1` (working tree vs penultimate commit) and `dccc` mapped to `git difftool -d HEAD~2 HEAD` (third-last vs last commit), and both aliases MUST expose explicit help text in global and per-command help outputs.
- **REQ-039**: MUST every command `<command>` present in the CLI command dispatch map MUST be implemented by a Python function named exactly `cmd_<command>`, and the dispatch entry for `<command>` MUST reference that exact function symbol.
- **REQ-040**: MUST the `changelog` `--include-patch` option MUST prepend the chronologically latest patch release after the last minor release, including all commits from the last minor to that patch; if no minor release exists MUST include only the latest patch with all commits from the beginning.
- **REQ-041**: MUST the `changelog` command MUST support `--force-write`, `--print-only`, and `--disable-history`; command help MUST list all available options; disk writes MUST occur only when `CHANGELOG.md` is absent or `--force-write` is provided.
- **REQ-042**: MUST the `changelog` commit parser MUST recognize types: `new` (Features), `implement` (Implementations), `fix` (Bug Fixes), `change` (Changes), `cover` (Cover Requirements), `refactor` (Refactor), `docs` (Documentation), `style` (Styling), `revert` (Revert), `misc` (Miscellaneous Tasks); MUST parse headers `<type>:`, `<type>(<module>):`, `<type>!:`, and `<type>(<module>)!:` extracting type, optional module, optional breaking marker, and description; MUST ignore `perf`, `test`, `build`, `ci`, `chore`; MUST ignore commits whose subject matches `release: Release version <semver>`; MUST NOT generate an "Other" section; Implementations section header MUST use the 🏗️ icon.
- **REQ-043**: MUST the `changelog` `# History` section MUST be enabled by default, MUST be skipped when `--disable-history` is provided, and MUST be skipped when owner/repository resolution via REQ-046 fails with command error.
- **REQ-044**: MUST each `changelog` entry MUST remove lines matching `^Co-authored-by:.*` before normalization and MUST remove empty lines from commit descriptions.
- **REQ-045**: MUST the `patch` command MUST merge and push only configured `develop` using `git push origin <develop> --tags`, and MUST NOT merge to or push `master`.
- **REQ-046**: MUST the `changelog` GitHub URL resolver MUST query `git config branch.<master_branch>.remote` (fallback `origin`) and `git remote get-url <remote>`; MUST parse SSH/HTTPS URL formats into `<owner>` and `<repo>` using shared string-parsing utilities; MUST NOT perform network operations.
- **REQ-047**: MUST the `backup` command MUST enforce the same preflight checks and error reporting used by the `major`/`minor`/`patch` workflows, including: current branch equals configured `work`, clean working tree, empty index, and remote-update checks for configured `develop` and `master`.
- **REQ-048**: MUST the `backup` command MUST merge the configured local `work` branch into the configured local `develop` branch, and MUST push the updated `develop` branch to its configured remote tracking branch.
- **REQ-049**: MUST on success, the `backup` command MUST checkout back to configured `work` and MUST print a success message stating that all local `work` changes were merged and pushed to the configured remote `develop`.
- **REQ-068**: MUST without `--include-patch`, `# History` MUST contain only minor-release tags present in the changelog body; with `--include-patch`, it MUST additionally include the latest patch tag, using last minor or repository start as diff baseline.
- **REQ-069**: MUST `# History` release links MUST use template `https://github.com/<OWNER>/<REPO>/releases/tag/<TAG>` and diff links MUST use template `https://github.com/<OWNER>/<REPO>/compare/<TAG_FROM>..<TAG_TO>` generated deterministically from local changelog tags.
- **REQ-070**: MUST `# History` generation MUST NOT verify remote tag existence and MUST NOT query remote tags; changelog tag and commit collection MUST use only local git commands.
- **REQ-071**: MUST when a CLI command is added, modified, or removed in the dispatch map, `README.md` MUST be updated for user-facing usage changes; internal logic-only refactors with unchanged command behavior MUST NOT require README updates.
- **REQ-072**: MUST the `major` and `minor` commands MUST push configured `develop` and configured `master` using `git push origin <branch> --tags` for each pushed branch, and MUST create definitive annotated `v<target>` on configured `master` immediately before master push.
- **REQ-073**: MUST the `lt` alias MUST print one line per tag as `<tag>: <branch_1>, <branch_2>, ...`, where branches are the refs returned by `git branch -a --contains <tag>` after marker trimming.
- **REQ-074**: MUST the alias `wt` MUST execute `git worktree list`, and `wtl` MUST execute `git worktree list` while forwarding all provided arguments unchanged.
- **REQ-075**: MUST the alias `wtl` MUST accept and forward `-v`, `--porcelain`, and `-z` options as native `git worktree list` arguments without CLI-side transformation.
- **REQ-076**: MUST the alias `wtp` MUST execute `git worktree prune` and MUST forward `-n`, `-v`, `--expire <expire>`, and additional git-compatible arguments unchanged.
- **REQ-077**: MUST the alias `wtr` MUST execute `git worktree remove` and MUST forward `-f`, required `<worktree>`, and additional git-compatible arguments unchanged.
- **REQ-078**: MUST changelog markdown MUST render one top-level bullet per commit; multiline description lines MUST become consecutive indented sub-bullets; renderer MUST NOT insert blank separator lines between consecutive top-level commit bullets.
- **REQ-079**: MUST the `ls` alias MUST run `git ls-files --exclude-standard` and MUST pass any additional arguments to the git command unchanged.
- **REQ-080**: MUST the `lsi` alias MUST run `git ls-files --others --ignored --exclude-standard`, MUST filter output by excluding paths where any path component matches any entry in `LSI_DEFAULT_EXCLUDED_DIRS` or ends with any suffix in `LSI_DEFAULT_EXCLUDED_DIR_SUFFIXES`, and MUST pass any additional arguments to the git command unchanged.
- **REQ-081**: MUST the `lsa` alias MUST run `git ls-files --others --exclude-standard` and MUST pass any additional arguments to the git command unchanged.
- **REQ-082**: MUST the CLI MUST expose an `o` alias in `COMMANDS` and `HELP_TEXTS`, and `--help` outputs MUST include `o` in global and per-command help paths.
- **REQ-083**: MUST the `o` alias MUST terminate with non-zero exit when executed outside a Git repository and MUST print an explicit English error message to stderr.
- **REQ-084**: MUST the `o` alias MUST print sections in order as: section 1 working area context, section 2 branch distances, section 3 active worktrees, section 4 qualitative topology, section 5 branches, and section 6 current-branch state only when `WorkingTree` state is not `clean`.
- **REQ-085**: MUST the `o` alias MUST always use configured `work`, `develop`, and `master` branch names, MUST print identifiers `Work(⎇ <work>)`, `Develop(⎇ <develop>)`, `Master(⎇ <master>)`, and MUST print `Current Branch: <Logical>(⎇ <current>)`.
- **REQ-086**: MUST the `o` alias MUST print verbose divergence rows with explicit configured labels and remote labels `RemoteDevelop(⎇ origin/<develop>)` and `RemoteMaster(⎇ origin/<master>)`, using `git rev-list` counts when compared refs exist.
- **REQ-087**: MUST the `o` alias MUST color ahead counters with bright green (`\033[92m`) and behind counters with bright red (`\033[31;1m`); zero-value counters and non-delta text MUST remain white.
- **REQ-088**: MUST the `o` alias MUST render section titles in purple (`\033[35;1m`), branch/remote identifier tuples `(⎇ <name>)` in bright yellow (`\033[38;5;226m`), subsection titles in bright white, and every rendered `Work(⎇ <work>)` logical prefix in bright green (`\033[92m`) when state is `clean`, bright red (`\033[31;1m`) when state is `unstaged`, otherwise bright white (`\033[97m`), reusing the same formatting in all sections.
- **REQ-089**: MUST the `o` alias MUST print section 4 with title `QUALITATIVE TOPOLOGY` and MUST render a chronological-position tree where node placement derives from actual commit positions in the repository history.
- **REQ-090**: MUST the section-4 infographic MUST include `WorkingTree`, `Work`, `Develop`, `RemoteDevelop`, `Master`, and `RemoteMaster`; MUST resolve each ref hash via `git rev-parse`; MUST group refs sharing the same commit hash on the same output line except `WorkingTree`; MUST order nodes by descending `git rev-list --count` from the octopus merge-base of available refs.
- **REQ-091**: MUST the section-4 infographic MUST NOT emit qualitative-state labels (`in_sync`, `ahead`, `behind`, `diverged`, `unknown`) in the topology output lines.
- **REQ-092**: MUST the section-4 root node MUST be the node or group with the highest commit count from the merge-base; remaining nodes MUST appear as `|-- ` children ordered by descending commit count; `WorkingTree` MUST be positioned immediately above the line containing `Work` when at the same commit position or when the working tree is dirty.
- **REQ-093**: MUST the section-4 infographic MUST preserve the overview color contract: purple section title, yellow `(⎇ <name>)` tuples, and white generic text including tree connectors and `WorkingTree` state annotation.
- **REQ-094**: MUST the `o` alias MUST execute `git worktree list --verbose` in section 3, MUST execute `git status -sb` only when `WorkingTree` state is not `clean`, and in section 6 MUST normalize the status header line from `## <branch>` to `## <Logical>(⎇ <branch>)` using the same color formatting as section-1 `Current Branch`, and MUST render each non-header status line two-character status prefix in bright red (`\033[31;1m`).
- **REQ-095**: MUST the section-4 `WorkingTree` node MUST display `WorkingTree [<state>]` where `<state>` is the working-tree state string (`clean`, `unstaged`, `staged`, or `mixed`) derived from the same diagnostic function used by `cmd_o`.
- **REQ-096**: MUST the `o` alias MUST print section `=== 5. BRANCHES ===` with configured aligned rows for `Work`, `Develop`, `Master`, `RemoteDevelop`, `RemoteMaster`, formatted `<Identifier> | <latest commit subject>`; commit subject text MUST be uncolored and MUST strip ANSI escape sequences before rendering.
- **REQ-097**: MUST runtime configuration loading MUST NOT append, persist, or mutate configuration files; file normalization and key insertion MUST occur only when `--write-config` is explicitly executed.
- **REQ-098**: MUST the CLI MUST expose an `l` alias in `COMMANDS` and `HELP_TEXTS`, and `--help` outputs MUST include `l` in global and per-command help paths.
- **REQ-099**: MUST the `l` alias MUST render a text-based tree visualization of git commit history by invoking `git log --date-order` with a custom pretty format and processing the output through a vine-based graph algorithm.
- **REQ-100**: MUST each `l` output line MUST display columns in fixed order: abbreviated commit hash, author date formatted as `%Y-%m-%d %H:%M`, graph tree segment, author name, ref decoration, commit subject.
- **REQ-101**: MUST the `l` alias MUST support `--style=<n>` with values: 1 (single-line Unicode, default), 2 (double-line Unicode), 10 (rounded Unicode edges), 15 (bold-line Unicode).
- **REQ-102**: MUST the `l` alias MUST use configurable graph symbols with defaults: commit `●`, merge `◎`, overpass `═`, root `■`, tip `○`; overridable via `--graph-symbol-commit=<s>`, `--graph-symbol-merge=<s>`, `--graph-symbol-overpass=<s>`, `--graph-symbol-root=<s>`, `--graph-symbol-tip=<s>`.
- **REQ-103**: MUST the `l` alias MUST apply ANSI color scheme: tree (cyan `\033[0;36m`), hash (magenta `\033[0;35m`), date (blue `\033[0;34m`), author (yellow `\033[0;33m`), tag (bold magenta `\033[1;35m`), default (reset `\033[0m`); `--no-color` MUST disable all ANSI color output.
- **REQ-104**: MUST the `l` alias MUST support options: `--all` (show all branches and HEAD), `--reverse` (reverse output order), `--abbrev=<n>` (hash abbreviation width 4..40, default auto-detect from `git rev-parse --short HEAD`), `--svdepth=<n>` (maximum subvine merge depth, default 2), `--no-status` (disable working tree status display).
- **REQ-105**: MUST the `l` alias MUST support `--graph-margin-left=<n>` (left margin columns, default 2) and `--graph-margin-right=<n>` (right margin columns, default 1) controlling spacing around the graph tree segment.
- **REQ-106**: MUST the `l` alias MUST display working tree status indicators appended to the HEAD ref decoration: `*` (unstaged changes), `+` (staged changes), `$` (stash entries), `%` (untracked files); the status display MUST be disabled when `--no-status` is specified.
- **REQ-107**: MUST the `l` alias MUST detect and display mid-flow state indicators appended to the working tree status: `|REBASE-i`, `|REBASE-m`, `|REBASE`, `|AM`, `|AM/REBASE`, `|MERGING`, `|CHERRY-PICKING`, `|REVERTING`, `|BISECTING`.
- **REQ-108**: MUST the `l` alias MUST detect an active interactive rebase state and annotate the ref map with `rebase/next`, `rebase/onto`, and `rebase/new` markers at the corresponding commit SHA positions.
- **REQ-109**: MUST the `l` alias MUST implement a vine-based graph algorithm with three phases per commit: vine_branch (draw branch convergence connectors), vine_commit (place commit node and assign tip positions), vine_merge (draw merge fan-out connectors and allocate parent vine slots).
- **REQ-110**: MUST the `l` alias MUST cycle branch colors from a predefined palette (`blue_bold`, `yellow_bold`, `magenta_bold`, `green_bold`, `cyan_bold`) with neighbor-avoidance logic ensuring adjacent branches use distinct colors.
- **REQ-111**: MUST the `l` alias MUST inject `-n 35` only when invoked with no user arguments, and MUST pass all user-provided unrecognized arguments through to `git log` unchanged without appending `-n 35`.
- **REQ-112**: MUST trigger GitHub release workflow `release-uvx.yml` only on pushed tags matching `v<major>.<minor>.<patch>`, and MUST continue release execution only when the tagged commit is contained in `origin/master`.
- **REQ-113**: MUST build release distributions in GitHub Actions with Python 3.11 using `python -m build`, and MUST attest provenance for `dist/*` artifacts.
- **REQ-114**: MUST publish a non-draft, non-prerelease GitHub Release for the triggering tag and upload `dist/**/*` assets using changelog content produced by the configured changelog-builder step.
- **REQ-115**: MUST section `=== 5. BRANCHES ===` append, after configured rows, aligned `<Identifier> | <latest commit subject>` rows for every discovered local or remote branch not already rendered.
- **REQ-119**: MUST visual diff aliases include `dcd` mapped to `git difftool -d <develop> <work>`, `dcm` mapped to `git difftool -d <master> <work>`, and `ddm` mapped to `git difftool -d <master> <develop>`, using configured branch names from `.g.conf`; `dcd`, `dcm`, and `ddm` MUST each expose explicit help text in global and per-command help outputs.
- **REQ-120**: MUST define `LSI_DEFAULT_EXCLUDED_DIRS` as a `frozenset` containing: `.cache`, `.claude`, `.codex`, `.eslintcache`, `.gemini`, `.git`, `.github`, `.kiro`, `.mypy_cache`, `.npm`, `.opencode`, `.parcel-cache`, `.pytest_cache`, `.ruff_cache`, `.sass-cache`, `.terragrunt-cache`, `.tox`, `.venv`, `.vscode`, `__pycache__`, `build`, `dist`, `htmlcov`, `node_modules`, `temp`, `tmp`, `venv`.
- **REQ-121**: MUST the `lsi` alias MUST accept `--include-all` flag; when present, MUST bypass `LSI_DEFAULT_EXCLUDED_DIRS` and `LSI_DEFAULT_EXCLUDED_DIR_SUFFIXES` filtering and print all ignored files unfiltered.
- **REQ-122**: MUST define `LSI_DEFAULT_EXCLUDED_DIR_SUFFIXES` as a `tuple` containing: `.egg-info`.

### 3.3 Project File Structure
```
.
├── .github/
│   └── workflows/
│       └── release-uvx.yml
├── docs/
│   ├── REQUIREMENTS.md
│   ├── REFERENCES.md
│   └── WORKFLOW.md
├── src/
│   └── git_alias/
│       ├── __init__.py
│       ├── __main__.py
│       ├── core.py
│       └── foresta.py
├── tests/
├── pyproject.toml
├── README.md
└── CHANGELOG.md
```

### 3.4 Component Organization
- `core.py` implements dispatch, command handlers, config loading/writing, git subprocess wrappers, and release/changelog flows.
- `foresta.py` implements vine-based text tree rendering for git history (`l` alias).
- `release-uvx.yml` implements tag-gated CI release build and publication workflow.
- No explicit performance optimizations identified.

### 3.5 Evidence for Added Requirements
- **REQ-112** evidence: `.github/workflows/release-uvx.yml` lines 3-6 (tag trigger), lines 25-35 (master containment gate).
- **REQ-113** evidence: `.github/workflows/release-uvx.yml` lines 50-53 (Python 3.11), line 62 (`python -m build`), lines 64-67 (attestation over `dist/*`).
- **REQ-114** evidence: `.github/workflows/release-uvx.yml` lines 117-127 (GitHub Release creation, non-draft/non-prerelease, `dist/**/*` assets, changelog body wiring).
