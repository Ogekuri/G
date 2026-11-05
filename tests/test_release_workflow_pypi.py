## @file test_release_workflow_pypi.py
# @brief Unit tests validating the PyPI release workflow and packaging contracts.

import re
import tomllib
import unittest
from pathlib import Path


## @brief Test suite for release-pypi.yml workflow and PyPI packaging contracts.
# @details Level 1 static-contract tests over committed release assets: verifies
#          the workflow rename (REQ-112), preserved build/attestation/release
#          steps (REQ-113, REQ-114), OIDC permissions (REQ-193), PyPI Trusted
#          Publishing post-steps without credentials (REQ-194, REQ-195),
#          PyPI project metadata (REQ-196), PEP 639 license declaration
#          (REQ-197), and README install documentation (REQ-198).
# @satisfies REQ-112, REQ-113, REQ-114, REQ-193, REQ-194, REQ-195, REQ-196, REQ-197, REQ-198
class ReleaseWorkflowPyPiTest(unittest.TestCase):
    ## @brief Repository root path used by release-contract tests.
    REPO_ROOT = Path(__file__).resolve().parents[1]

    ## @brief Resolve the release workflow file path.
    # @return {Path} Absolute path of .github/workflows/release-pypi.yml.
    def _workflow_path(self) -> Path:
        return self.REPO_ROOT / ".github" / "workflows" / "release-pypi.yml"

    ## @brief Read the release workflow text.
    # @return {str} Full YAML text of the release workflow.
    def _workflow_text(self) -> str:
        return self._workflow_path().read_text(encoding="utf-8")

    ## @brief Extract one workflow step block by anchor token.
    # @details Returns the text spanning from the `- name:` line preceding the
    #          anchor occurrence up to the next sibling step start or EOF.
    # @param anchor {str} Unique token identifying the step (e.g. action ref).
    # @return {str} Step block text containing the anchor.
    def _workflow_step_block(self, anchor: str) -> str:
        text = self._workflow_text()
        anchor_index = text.index(anchor)
        step_start = text.rindex("\n      - name:", 0, anchor_index)
        next_step = text.find("\n      - name:", anchor_index)
        step_end = len(text) if next_step == -1 else next_step
        return text[step_start:step_end]

    ## @brief Load the pyproject.toml project table.
    # @return {dict} Parsed [project] table mapping.
    def _pyproject(self) -> dict:
        return tomllib.loads((self.REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8"))

    ## @brief Verify workflow file is renamed to release-pypi.yml.
    # @return None.
    # @satisfies REQ-112
    def test_workflow_file_renamed_to_release_pypi(self):
        self.assertTrue(self._workflow_path().is_file())
        legacy = self.REPO_ROOT / ".github" / "workflows" / "release-uvx.yml"
        self.assertFalse(legacy.exists())

    ## @brief Verify workflow triggers and master-containment gate are preserved.
    # @return None.
    # @satisfies REQ-112
    def test_workflow_triggers_and_master_gate_preserved(self):
        text = self._workflow_text()
        self.assertIn("workflow_dispatch:", text)
        self.assertIn("'v[0-9]+.[0-9]+.[0-9]+'", text)
        self.assertIn("origin/master", text)

    ## @brief Verify workflow grants OIDC release permissions.
    # @return None.
    # @satisfies REQ-193
    def test_workflow_grants_oidc_release_permissions(self):
        text = self._workflow_text()
        permissions_block = text[text.index("permissions:") : text.index("jobs:")]
        self.assertIn("contents: write", permissions_block)
        self.assertIn("id-token: write", permissions_block)
        self.assertIn("attestations: write", permissions_block)

    ## @brief Verify build and provenance attestation steps are preserved.
    # @return None.
    # @satisfies REQ-113
    def test_workflow_build_and_attestation_steps_preserved(self):
        text = self._workflow_text()
        self.assertIn('python-version: "3.11"', text)
        self.assertIn("python -m build", text)
        attestation_block = self._workflow_step_block("actions/attest-build-provenance")
        self.assertIn("subject-path: dist/*", attestation_block)

    ## @brief Verify GitHub Release step semantics are preserved.
    # @return None.
    # @satisfies REQ-114
    def test_workflow_github_release_step_preserved(self):
        release_block = self._workflow_step_block("softprops/action-gh-release")
        self.assertIn("draft: false", release_block)
        self.assertIn("prerelease: false", release_block)
        self.assertIn("files: dist/**/*", release_block)

    ## @brief Verify PyPI publication runs after the GitHub Release step.
    # @return None.
    # @satisfies REQ-195
    def test_workflow_pypi_publish_runs_after_github_release(self):
        text = self._workflow_text()
        release_index = text.index("softprops/action-gh-release")
        publish_index = text.index("pypa/gh-action-pypi-publish")
        self.assertLess(release_index, publish_index)

    ## @brief Verify PyPI publication uses OIDC without credential inputs.
    # @return None.
    # @satisfies REQ-194
    def test_workflow_pypi_publish_uses_oidc_without_credentials(self):
        publish_block = self._workflow_step_block("pypa/gh-action-pypi-publish")
        self.assertIn("uses: pypa/gh-action-pypi-publish@release/v1", publish_block)
        self.assertNotIn("password", publish_block)
        self.assertNotIn("api-token", publish_block)
        self.assertNotIn("secrets.", publish_block)

    ## @brief Verify pyproject declares PyPI-compliant project metadata.
    # @return None.
    # @satisfies REQ-196
    def test_pyproject_declares_pypi_project_metadata(self):
        project = self._pyproject()["project"]
        self.assertEqual(project["name"], "galias")
        self.assertTrue(project["description"])
        self.assertEqual(project["readme"], "README.md")
        self.assertEqual(project["requires-python"], ">=3.11")
        self.assertTrue(project["keywords"])
        self.assertTrue(project["classifiers"])
        urls = project["urls"]
        for key in ("Homepage", "Repository"):
            self.assertIn(key, urls)
            self.assertIn("https://github.com/Ogekuri/GAlias", urls[key])

    ## @brief Verify pyproject declares a PEP 639 SPDX license.
    # @return None.
    # @satisfies REQ-197
    def test_pyproject_declares_pep639_spdx_license(self):
        project = self._pyproject()["project"]
        self.assertEqual(project["license"], "GPL-3.0-only")
        self.assertIn("LICENSE", project["license-files"])
        build_requires = self._pyproject()["build-system"]["requires"]
        setuptools_specs = [spec for spec in build_requires if spec.startswith("setuptools")]
        self.assertTrue(setuptools_specs)
        floor_versions = []
        for spec in setuptools_specs:
            version_match = re.search(r">=(\d+)", spec)
            if version_match is not None:
                floor_versions.append(int(version_match.group(1)))
        self.assertTrue(floor_versions)
        self.assertGreaterEqual(max(floor_versions), 77)

    ## @brief Verify README documents PyPI install and uvx usage.
    # @return None.
    # @satisfies REQ-198
    def test_readme_documents_pypi_install_and_uvx_usage(self):
        readme = (self.REPO_ROOT / "README.md").read_text(encoding="utf-8")
        self.assertRegex(readme, r"(?m)^\s*uv tool install galias --force\s*$")
        self.assertRegex(readme, r"(?m)^\s*uvx galias <command> \[args\.\.\.\]\s*$")
        self.assertIn("uv tool install galias --force --from git+https://github.com/Ogekuri/GAlias.git", readme)


if __name__ == "__main__":
    unittest.main()
