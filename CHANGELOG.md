# Changelog

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

[0.1.0]: https://github.com/Ogekuri/G/releases/tag/v0.1.0
[0.2.0]: https://github.com/Ogekuri/G/compare/v0.1.0..v0.2.0
[0.3.0]: https://github.com/Ogekuri/G/compare/v0.2.0..v0.3.0
[0.4.0]: https://github.com/Ogekuri/G/compare/v0.3.0..v0.4.0
[0.5.0]: https://github.com/Ogekuri/G/compare/v0.4.0..v0.5.0
