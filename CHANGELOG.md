# Changelog

## [0.7.1](https://github.com/Ogekuri/G/compare/v0.7.0..v0.7.1) - 2026-02-27
### 🐛  Bug Fixes
- Remove colors from commits.

### 📚  Documentation
- Update TODO.md file.

## [0.7.0](https://github.com/Ogekuri/G/compare/v0.6.0..v0.7.0) - 2026-02-25
### ⛰️  Features
- Add Acknowledgments section in README.md. *(core)*
- Add 'l' command for text-based commit tree visualization [useReq] *(core)*
  - Added REQ-098..REQ-111 for tree visualization with vine-based graph algorithm
  - Created foresta.py module (Perl-to-Python port) with configurable styles,
  - symbols, colors, margins, and working tree status display
  - Registered cmd_l in COMMANDS/HELP_TEXTS with full option passthrough to git log
  - Added CPT-008 for foresta.py module; updated REQ-008 to include 'l'
  - Added 37 unit tests in test_cmd_l.py covering helpers, styles, symbols, colors
  - Updated WORKFLOW.md and REFERENCES.md

### 🐛  Bug Fixes
- Update default module in G.

### 🚜  Changes
- default to -n 35 with no args [useReq] *(cmd-l)*
  - Update REQ-111 to require default depth limiting only when l has no parameters.
  - Implement cmd_l argument injection: use '-n 35' only for empty invocation and preserve provided args unchanged.
  - Add unit tests validating default injection and non-injection when parameters are provided.
  - Update WORKFLOW runtime note and regenerate REFERENCES for traceability.
- append unconfigured overview branches [useReq] *(core)*
  - Update REQ-096 wording and add REQ-115 for section-5 branch ordering.
  - Implement section 5 to append all non-configured local/remote branches after configured rows.
  - Add normalization helper for git branch -a parsing and extend branch summary rendering.
  - Adjust cmd_o tests and add coverage for normalized branch discovery and appended rows.
  - Update WORKFLOW and regenerate REFERENCES for traceability.
- support empty conventional scope [useReq] *(core)*
  - Update REQ-022 and add REQ-115..REQ-117 for empty-module commit format.
  - Change default_commit_module hardcoded default to empty string.
  - Accept explicit empty default_commit_module in config load/write paths.
  - Emit '<type>: <description>' when effective module is empty.
  - Update conventional and config I/O tests; refresh WORKFLOW and REFERENCES docs.

### 📚  Documentation
- Update README.md file.
- align README overview branch-table behavior [useReq] *(cmd-o)*
  - Update Feature Highlights and CLI Examples for /home/ogekuri/G                              5f8bd03 [work]
  - /home/ogekuri/userReq-G-work-20260225142452  5f8bd03 [userReq-G-work-20260225142452]
  - [35;1m=== 1. WORKING AREA, STAGE & CURRENT BRANCH ===[0m
  - [97mConfigured branches: [97mWork[97m([38;5;226m⎇ work[0m[97m)[0m, [97mDevelop[97m([38;5;226m⎇ develop[0m[97m)[0m, [97mMaster[97m([38;5;226m⎇ master[0m[97m)[0m[0m
  - [97mConfigured remotes: [97mRemoteDevelop[97m([38;5;226m⎇ origin/develop[0m[97m)[0m, [97mRemoteMaster[97m([38;5;226m⎇ origin/master[0m[97m)[0m[0m
  - [97mCurrent Branch: [31;1mCurrent[97m([38;5;226m⎇ userReq-G-work-20260225142452[0m[97m)[0m[0m
  - [35;1m=== 2. BRANCH DISTANCES (COMMITS) ===[0m
  - [97m[97mWork[97m([38;5;226m⎇ work[0m[97m)[0m vs [97mDevelop[97m([38;5;226m⎇ develop[0m[97m)[0m[0m | [97mahead 0[0m | [97mbehind 0[0m
  - [97m[97mWork[97m([38;5;226m⎇ work[0m[97m)[0m vs [97mMaster[97m([38;5;226m⎇ master[0m[97m)[0m[0m | [92m↑ ahead 7[0m | [97mbehind 0[0m
  - [97;1m--- Server Alignment ---[0m
  - [97m[97mDevelop[97m([38;5;226m⎇ develop[0m[97m)[0m vs [97mRemoteDevelop[97m([38;5;226m⎇ origin/develop[0m[97m)[0m[0m | [97mahead 0[0m | [97mbehind 0[0m
  - [97m[97mMaster[97m([38;5;226m⎇ master[0m[97m)[0m vs [97mRemoteMaster[97m([38;5;226m⎇ origin/master[0m[97m)[0m[0m | [97mahead 0[0m | [97mbehind 0[0m
  - [35;1m=== 3. ACTIVE WORKTREES ===[0m
  - [35;1m=== 4. QUALITATIVE TOPOLOGY ===[0m
  - [97mWorkingTree [staged][0m
  - [97m|[0m
  - [97m|-- [0m[97mWork[97m([38;5;226m⎇ work[0m[97m)[0m, [97mDevelop[97m([38;5;226m⎇ develop[0m[97m)[0m, [97mRemoteDevelop[97m([38;5;226m⎇ origin/develop[0m[97m)[0m
  - [97m|-- [0m[97mMaster[97m([38;5;226m⎇ master[0m[97m)[0m, [97mRemoteMaster[97m([38;5;226m⎇ origin/master[0m[97m)[0m
  - [97m|[0m
  - [35;1m=== 5. BRANCHES ===[0m
  - [97m[97mWork[97m([38;5;226m⎇ work[0m[97m)[0m[97m                                                   | [0m[97;1mrelease: Release version 0.6.1[0m[0m
  - [97m[97mDevelop[97m([38;5;226m⎇ develop[0m[97m)[0m[97m                                             | [0m[97;1mrelease: Release version 0.6.1[0m[0m
  - [97m[97mMaster[97m([38;5;226m⎇ master[0m[97m)[0m[97m                                               | [0m[97;1mrelease: Release version 0.6.0[0m[0m
  - [97m[97mRemoteDevelop[97m([38;5;226m⎇ origin/develop[0m[97m)[0m[97m                                | [0m[97;1mrelease: Release version 0.6.1[0m[0m
  - [97m[97mRemoteMaster[97m([38;5;226m⎇ origin/master[0m[97m)[0m[97m                                  | [0m[97;1mrelease: Release version 0.6.0[0m[0m
  - [97m[97muserReq-G-work-20260225142452[97m([38;5;226m⎇ userReq-G-work-20260225142452[0m[97m)[0m[97m | [0m[97;1mrelease: Release version 0.6.1[0m[0m
  - [97m[97m+ work[97m([38;5;226m⎇ + work[0m[97m)[0m[97m                                               | [0m[97;1mn/a[0m[0m
  - [35;1m=== 6. CURRENT BRANCH STATE ===[0m
  - [97m## [31;1mCurrent[97m([38;5;226m⎇ userReq-G-work-20260225142452[0m[97m)[0m[0m
  - [31;1mM [0m README.md.
  - Document that section  prints configured rows first and appends all other local/remote branches with latest commit subjects.
- Recreate SRS in English [useReq] *(requirements)*
  - Reorganized requirements with RFC 2119 statements.
  - Preserved existing IDs and appended REQ-112..REQ-114.

## [0.6.0](https://github.com/Ogekuri/G/compare/v0.5.0..v0.6.0) - 2026-02-24
### ⛰️  Features
- add overview ASCII topology section [useReq] *(core)*
  - append REQ-089..REQ-093 for qualitative topology output\n- add section 4 ASCII tree rendering in cmd_o\n- map divergence counts to qualitative states\n- extend overview tests for section ordering and topology nodes\n- update workflow and regenerate references
- add o overview alias with templates [useReq] *(core)*
  - append REQ-082..REQ-088 for overview command\n- implement cmd_o with reusable formatting templates and help wiring\n- add tests and update README/WORKFLOW/REFERENCES
- add .place-holder files. *(core)*
- add ls/lsi file listing aliases [useReq] *(cli)*
  - Add REQ-079/REQ-080 and update REQ-008.\nAdd cmd_ls/cmd_lsi, help text, tests.\nUpdate WORKFLOW/REFERENCES and README.\nTests: PYTHONPATH=src /tmp/venv-userReq-G-work-3af15715-c78b-405c-a749-bf538bb2225a/bin/python -m pytest
- add guidelines/, update .gitignore. *(core)*

### 🐛  Bug Fixes
- Fix workflow file. *(core)*
- .g.conf. *(core)*
- fiw workflow file. *(core)*

### 🚜  Changes
- BREAKING CHANGE: enforce strict local/global config schemas [useReq] *(config)*
  - Normalize .g.conf to local-only keys and $HOME/.g/g.conf to global-only keys.
  - Rename global legacy key editor to edit_command during --write-config.
  - Keep startup configuration loading read-only with scoped key application.
  - Update requirements, workflow model, references, and configuration IO tests.
- BREAKING CHANGE: split local and global configuration files [useReq] *(config)*
  - Update REQUIREMENTS for split local/global config contracts and renamed keys.
  - Refactor core config loading to read .g.conf and $HOME/.g/g.conf.
  - Rename default_module->default_commit_module and editor->edit_command.
  - Make --write-config add only missing keys without overwriting existing values.
  - Remove runtime autofill persistence for missing gp_command/gr_command.
  - Update config/help/conventional tests and refresh WORKFLOW/REFERENCES docs.
- normalize description casing and period [useReq] *(conventional-commit)*
  - Update REQ-022 to require conventional commit description normalization.
  - Capitalize first description character unless numeric.
  - Append trailing period when missing across conventional aliases.
  - Add regression tests and refresh workflow/reference docs.
- make gp/gr commands configurable [useReq] *(config)*
  - Update DES-006, REQ-014, and REQ-015 for gp/gr configurable command keys and runtime fallback behavior.
  - Add REQ-097 to persist missing gp_command/gr_command defaults into existing .g.conf while preserving existing keys.
  - Refactor core command resolution for gp/gr with executable availability checks and fallback to default templates.
  - Add tests for config IO autofill and gp/gr command execution/fallback; refresh WORKFLOW and REFERENCES docs.
- color status prefixes in section 6 [useReq] *(overview-o)*
  - Update REQ-094 for bright-red two-character status prefixes in CURRENT BRANCH STATE.
  - Apply prefix coloring in _overview_current_branch_state_lines and keep header normalization.
  - Add/adjust tests for section-6 prefix color rendering and regenerate workflow/reference docs.
- normalize work label and conditional state section [useReq] *(overview-o)*
  - Update REQ-084/088/094 and bump SRS version to 0.91.
  - Implement state-aware Work prefix color across overview sections.
  - Render section 6 only for non-clean worktree and normalize status header.
  - Add/adjust cmd_o tests for clean/non-clean rendering behavior.
  - Regenerate WORKFLOW and REFERENCES for updated call-trace/symbol map.
- render aligned configured branch rows [useReq] *(overview-branches)*
  - Replace section-5 lb-like listing with configured branch summary rows.
  - Render '<Identifier> | <latest commit subject>' with aligned identifiers.
  - Print commit subject in bright white bold and update cmd_o tests/spec/docs.
- group Work with aligned refs in topology [useReq] *(overview-topology)*
  - Update REQ-090 and REQ-092 to allow Work hash grouping.
  - Implement topology grouping change in _overview_ascii_topology_lines.
  - Adjust and extend cmd_o topology tests for aligned Work/Develop refs.
- add overview branches section ordering [useReq] *(core)*
  - update REQ-084 and REQ-094 for six-section overview layout
  - add section 5 BRANCHES in cmd_o using lb-equivalent branch listing
  - renumber current branch state heading to section 6
  - extend cmd_o tests for new section ordering and branch output
  - update WORKFLOW.md and regenerate REFERENCES.md
- replace qualitative topology with chronological-position tree [useReq] *(core)*
  - Updated REQ-089..REQ-093, added REQ-095 for chronological topology
  - Rewritten _overview_ascii_topology_lines to derive node positions
  - from actual commit hashes via git rev-parse and git merge-base
  - Removed qualitative-state labels (in_sync/ahead/behind/diverged/unknown)
  - from section-4 infographic output
  - Removed _overview_compare_relation, _overview_inverse_relation_state,
  - _overview_relation_state_text, _overview_normalize_relation_state,
  - and OVERVIEW_RELATION_STATES constant
  - Nodes grouped by shared commit hash, ordered most-ahead to most-behind
  - WorkingTree always separate with [state] annotation
  - Updated tests, WORKFLOW.md, REFERENCES.md
- rework overview topology infographic [useReq] *(core)*
  - revise REQ-089/090/092 for commit-alignment semantics\n- render section 4 as work-relative alignment groups\n- add silent relation helper for topology grouping\n- keep ahead/behind color semantics and section title\n- align tests, workflow trace, and regenerated references
- refine overview current branch rendering [useReq] *(core)*
  - update REQ-084/085/088/089 and add REQ-094 for section flow\n- add highlighted current-branch line in section 1\n- move git status branch-state output to new section 5\n- rename section 4 title to QUALITATIVE TOPOLOGY\n- align tests, workflow model, and regenerated references
- redesign o overview visual output [useReq] *(core)*
  - revise REQ-084..REQ-088 for configured branch/remote labels and color contract\n- render Work/Develop/Master and RemoteDevelop/RemoteMaster identifiers verbosely\n- enforce purple section titles, bright white subsection title, yellow branch tuples\n- color ahead counters bright green and behind counters bright red\n- align overview tests and refresh WORKFLOW/REFERENCES docs
- extend o overview with active worktree section [useReq] *(core)*
  - update REQ-084 and REQ-088 for third overview section behavior\n- add section 3 in cmd_o using git worktree list --verbose\n- keep existing overview templates/colors and update tests\n- refresh WORKFLOW.md and regenerate REFERENCES.md
- rename d alias to dr and align handlers [useReq] *(core)*
  - update REQ-008 and REQ-037 for dr visual diff alias
  - rename cmd_d to cmd_dr and map command dispatch key to dr
  - update diff alias tests and regenerate workflow/references docs
- add lsa alias and align lsi ls-files flags [useReq] *(cli)*
  - Requirement Delta: update REQ-008, REQ-080, add REQ-081 for ls/lsi/lsa behavior.
  - Implementation Delta: add cmd_lsa, update cmd_lsi flags, register HELP_TEXTS/COMMANDS entries.
  - Test Delta: extend tests/test_cmd_ls.py for lsi and new lsa forwarding assertions.
  - Docs Delta: update docs/WORKFLOW.md call-trace nodes and regenerate docs/REFERENCES.md.
  - Execution-ID: b348bd2e-c5b4-4c5e-b78c-beb5e3b6c97d

### 📚  Documentation
- align config file documentation [useReq] *(readme)*
  - Update README to document split local/global configuration files.
  - Document default_commit_module and global edit_command key usage.
  - Clarify --write-config normalization and legacy editor->edit_command migration.

## [0.5.0](https://github.com/Ogekuri/G/compare/v0.4.0..v0.5.0) - 2026-02-22
### ⛰️  Features
- add worktree aliases wt/wtl/wtp/wtr docs/tests [2026-02-22 16:27:03] *(core)*

### 🐛  Bug Fixes
- normalize multiline list markers [2026-02-22 18:07:32] *(changelog)*
- normalize multiline entry indentation [2026-02-22 17:33:22] *(changelog)*
- align multiline markdown list indentation [2026-02-22 17:25:57] *(changelog)*

### 🚜  Changes
- remove blank commit separators [useReq] *(changelog)*
- resolve duplicate requirement id [useReq] *(requirements)*
- preserve multiline markdown bullets [useReq] *(changelog)*
- remove co-author trailers in markdown [2026-02-22 17:55:36] *(changelog)*
- normalize commit description line breaks [2026-02-22 17:39:18] *(changelog)*
- support breaking and multiline parsing [2026-02-22 13:26:20] *(changelog)*

## [0.4.0](https://github.com/Ogekuri/G/compare/v0.3.0..v0.4.0) - 2026-02-22
### 🐛  Bug Fixes
- workflow. *(core)*

## [0.3.0](https://github.com/Ogekuri/G/compare/v0.2.0..v0.3.0) - 2026-02-22
### 🐛  Bug Fixes
- fix workflow. *(core)*

### 🚜  Changes
- print containing branches for lt tags [2026-02-22 11:42:22] *(cmd_lt)*
- enforce tagged branch pushes in release flow [2026-02-22 11:01:35] *(core)*

### 📚  Documentation
- update README.md. *(core)*

## [0.2.0](https://github.com/Ogekuri/G/compare/v0.1.0..v0.2.0) - 2026-02-22
### 🐛  Bug Fixes
- fix workflow. *(core)*

### 🚜  Changes
- revise tag lifecycle and docs [2026-02-22 10:32:49] *(release-flow)*

### 📚  Documentation
- update README.md. *(core)*
- update README.md. *(core)*

## [0.1.0](https://github.com/Ogekuri/G/releases/tag/v0.1.0) - 2026-02-21
### ⛰️  Features
- update github workflow. *(core)*
- add dwcc and dccc diff aliases [2026-02-20 11:08:34] *(core)*
- add implement command and changelog support [2026-02-18 10:10:46] *(core)*
- add difftool aliases dw dc d [2026-02-17 17:07:56] *(core)*
- add req/ dir. *(core)*
- add test .g.conf for debug. *(core)*
- add clean.sh script. *(core)*
- add pathspec to requirements.txt *(core)*
- add new version check. *(core)*
- removed obsolete release command. *(core)*
- add support for --ver and --version commands. *(core)*
- add ra command. *(core)*
- release version: 0.0.4 *(core)*
- added new release command. *(core)*
- release version: 0.0.3 *(core)*
- release version: 0.0.2 *(core)*
- release version: 0.0.1 *(core)*
- draft release. *(core)*

### 🐛  Bug Fixes
- document module prefix and backup usage [2026-02-21 19:48:24] *(help)*
- fix workflow. *(core)*
- fix workflow file. *(core)*
- fix workflow. *(core)*
- workflow fix. *(core)*
- workflow fix. *(core)*
- workflow fix. *(core)*
- workflow fix. *(core)*
- workflow fix. *(core)*
- workflow fix. *(core)*
- workflow fix. *(core)*
- workflow fix. *(core)*
- workflow fix. *(core)*
- Update REFERENCES.md based on current implementation [2026-02-20 15:08:15] *(docs)*
- drop prova ver rule [2026-02-10 18:54:24] *(ver)*
- normalize git ls-files version paths [2026-02-10 18:22:17] *(ver)*
- normalize pathspec matching and update tests/docs [2026-02-10 17:58:26] *(ver)*
- WORKFLOW.md position. *(core)*
- fix undefined function references [2026-02-04 09:21:40] *(ori)*
- anchor ver_rules glob matching to repo root [2026-02-03 13:21:15] *(useReq)*
- change cover strings. *(core)*
- fix virtual environment creation on g.sh script. *(core)*
- add regression test for --include-draft *(core)*
- fix .gitignore file. *(core)*
- manual update version numbers. *(core)*
- minor changes on major, minor, patch prints. *(core)*
- fix changelog command. *(core)*
- fix history on chanchelog command. *(core)*
- fix history on chanchelog command. *(core)*
- fix on changelog command. *(core)*
- fix test according new code. *(core)*
- minor fix on patch command. *(core)*

### 🚜  Changes
- add backup workflow command [2026-02-21 19:39:09] *(backup)*
- add --disable-history and local history link resolver [2026-02-21 19:18:29] *(changelog)*
- resolve GitHub URL from master-branch remote using only local git commands [2026-02-21 18:15:15] *(_canonical_origin_base)*
  - Add _get_remote_name_for_branch: queries git config branch.<master>.remote, falls back to origin
  - Update _canonical_origin_base: uses master-branch remote instead of hardcoded origin
  - REQ-043 updated: # History links use GitHub templates with OWNER/REPO from master remote URL
  - REQ-046 added: URL resolver contract (local git commands only, SSH+HTTPS parsing)
  - tests/test_changelog_command.py: GetRemoteNameForBranchTest + CanonicalOriginBaseTest added (9 new cases)
- scope # History to changelog-body tags only [2026-02-21 17:39:45] *(changelog)*
  - REQ-043 updated: # History now contains only tags present in the changelog body
  - REQ-068 added: minor-only tags without --include-patch; minor + latest patch with --include-patch
  - generate_changelog_document: removed list_tags_sorted_by_date(merged_ref=HEAD) call; builds history_tags from minor_tags + optional latest_patch
  - Tests: replaced test_history_uses_tags_merged_into_head with two focused tests covering both modes
- restrict patch release to develop-only branch integration; update major/minor help [2026-02-21 17:17:41] *(patch)*
  - REQ-045 added: patch MUST NOT merge/push master; major/minor MUST merge/push develop+master
  - _execute_release_flow: master branch steps conditioned on level != "patch"
  - HELP_TEXTS: major and minor now mention Options: --include-patch
  - Doxygen: updated @details and @satisfies for cmd_major, cmd_minor, cmd_patch, _execute_release_flow
  - tests: added test_patch_release_skips_master_steps, test_major/minor_release_includes_master_steps
  - docs/REQUIREMENTS.md: version 0.67, REQ-045 appended
  - docs/WORKFLOW.md: call-trace updated for level-conditional master branch steps
  - docs/REFERENCES.md: regenerated
  - Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
- move scope indicator to suffix in changelog entry lines [2026-02-21 17:05:56] *(categorize_commit)*
- group by minor releases; replace --include-unreleased with --include-patch [2026-02-21 16:41:16] *(changelog)*
- remove include-draft flag path [2026-02-21 16:21:11] *(core)*
- update release marker commit format [2026-02-21 11:25:21] *(core)*
- amend first release commit from WIP when possible [2026-02-20 13:49:48] *(release-flow)*
- amend conventional commits on pending wip [2026-02-20 13:22:59] *(commit)*
- align command handler naming with aliases [2026-02-20 11:28:33] *(core)*
- rename diff aliases to dwc/dcc and align specs/tests [2026-02-20 11:01:23] *(core)*
- add multi-format doxygen generation workflow [2026-02-17 15:20:24] *(doxygen)*
- enforce doxygen metadata coverage [2026-02-17 15:01:55] *(core)*
- remove doc-comment requirements and normalize source comments [2026-02-15 19:42:27] *(core)*
- standardize Doxygen documentation and specs [2026-02-15 19:26:22] *(core)*
- switch ver matching to rglob and update specs/tests [2026-02-10 19:09:39] *(ver)*
- update ver verbose/debug requirements and tests [2026-02-10 17:44:31] *(core)*
- rename ori command to str, update requirements, code, and comments [2026-02-04 09:26:42] *(str)*
- Add ori command for remote inspection [2026-02-04 08:14:31] *(ori)*
- Optimize performance with git ls-files and version check cache [2026-02-03 14:01:40] *(useReq)*
- filter ver_rules matches from cache paths and cover tests [2026-02-03 13:39:07] *(useReq)*
- use pathspec gitignore for ver_rules matching [2026-02-03 13:28:29] *(useReq)*
- add cover conventional commit alias with emoji 🎯 and update requirements [2026-01-25 14:36:20] *(useReq)*
- add 'refactor' conventional commit type and alias; update requirements to include refactor and ✨ icon [e283ce7d-85bb-472c-b36a-e7c70b68f0ce] *(useReq)*

### ✨  Refactor
- cache ver/chver file discovery and rule contexts [2026-02-21 19:08:32] *(versioning)*

### 📚  Documentation
- Review README.md. *(core)*
- update README.md. *(core)*
- review README.md. *(core)*
- Review README.md. *(core)*
- update README.md. *(core)*
- regenerate runtime model [2026-02-20 15:32:32] *(workflow)*
- Update WORKFLOW.md to match current implementation [2026-02-20 15:16:17] *(core)*
- refresh references index [2026-02-19 17:52:25] *(core)*
- regenerate runtime execution model [2026-02-19 17:47:51] *(workflow)*
- generate source references documentation [2026-02-15 19:19:57] *(references)*
- regenerate workflow call tree [2026-02-15 18:54:30] *(core)*
- add workflow documentation [2026-02-09 16:19:23] *(core)*
- update workflow documentation [2026-02-09 10:24:18] *(core)*
- update WORKFLOW.md with comprehensive technical call tree [2026-02-09 10:19:09] *(core)*
- create WORKFLOW.md with technical call tree structure [2026-02-09 09:53:54] *(core)*
- update WORKFLOW.md with comprehensive technical call tree [2026-02-09 09:25:32] *(core)*
- add workflow analysis [2026-02-08 19:00:42] *(core)*
- update README.md. *(core)*
- add WORKFLOW.md. *(core)*
- update README.md and TODO.md files. *(core)*
- fix command's help. *(core)*
- change TODO.md. *(core)*
- update README.md. *(core)*
- update requirements.md *(core)*
- update requirements file. *(core)*

### ⚙️  Miscellaneous Tasks
- update prompts. *(core)*
- fix git repo. *(core)*


# History

- \[0.1.0\]: https://github.com/Ogekuri/G/releases/tag/v0.1.0
- \[0.2.0\]: https://github.com/Ogekuri/G/releases/tag/v0.2.0
- \[0.3.0\]: https://github.com/Ogekuri/G/releases/tag/v0.3.0
- \[0.4.0\]: https://github.com/Ogekuri/G/releases/tag/v0.4.0
- \[0.5.0\]: https://github.com/Ogekuri/G/releases/tag/v0.5.0
- \[0.6.0\]: https://github.com/Ogekuri/G/releases/tag/v0.6.0
- \[0.7.0\]: https://github.com/Ogekuri/G/releases/tag/v0.7.0
- \[0.7.1\]: https://github.com/Ogekuri/G/releases/tag/v0.7.1

[0.1.0]: https://github.com/Ogekuri/G/releases/tag/v0.1.0
[0.2.0]: https://github.com/Ogekuri/G/compare/v0.1.0..v0.2.0
[0.3.0]: https://github.com/Ogekuri/G/compare/v0.2.0..v0.3.0
[0.4.0]: https://github.com/Ogekuri/G/compare/v0.3.0..v0.4.0
[0.5.0]: https://github.com/Ogekuri/G/compare/v0.4.0..v0.5.0
[0.6.0]: https://github.com/Ogekuri/G/compare/v0.5.0..v0.6.0
[0.7.0]: https://github.com/Ogekuri/G/compare/v0.6.0..v0.7.0
[0.7.1]: https://github.com/Ogekuri/G/compare/v0.7.0..v0.7.1
