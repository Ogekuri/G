## @file test_dependency_manifests.py
# @brief Unit tests validating dependency-manifest alignment.

import ast
import re
import sys
import tomllib
import unittest
from pathlib import Path


## @brief Test suite for dependency declaration alignment across manifests.
# @details Validates that requirements.txt and pyproject.toml declare only runtime/build dependencies and remain synchronized.
# @satisfies CPT-004
class DependencyManifestsTest(unittest.TestCase):
    ## @brief Repository root path used by dependency-manifest tests.
    REPO_ROOT = Path(__file__).resolve().parents[1]

    ## @brief Canonicalize a dependency specifier to a normalized package name.
    # @param spec {str} Dependency string from requirements or pyproject lists.
    # @return {str} Lowercased package name with underscores normalized to dashes.
    @staticmethod
    def _normalize_dependency_name(spec: str) -> str:
        match = re.match(r"\s*([A-Za-z0-9_.-]+)", spec)
        if match is None:
            return ""
        return match.group(1).lower().replace("_", "-")

    ## @brief Parse requirements.txt dependency names.
    # @return {set[str]} Normalized dependency-name set from requirements.txt.
    def _requirements_dependencies(self) -> set[str]:
        requirements_path = self.REPO_ROOT / "requirements.txt"
        dependencies: set[str] = set()
        for raw_line in requirements_path.read_text().splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            dependencies.add(self._normalize_dependency_name(line))
        dependencies.discard("")
        return dependencies

    ## @brief Parse pyproject.toml dependency names by scope.
    # @return {tuple[set[str], set[str]]} Tuple(runtime_dependencies, build_dependencies).
    def _pyproject_dependencies(self) -> tuple[set[str], set[str]]:
        pyproject_path = self.REPO_ROOT / "pyproject.toml"
        pyproject = tomllib.loads(pyproject_path.read_text())

        runtime_specs = pyproject.get("project", {}).get("dependencies", [])
        build_specs = pyproject.get("build-system", {}).get("requires", [])

        runtime_dependencies = {
            self._normalize_dependency_name(spec) for spec in runtime_specs
        }
        build_dependencies = {
            self._normalize_dependency_name(spec) for spec in build_specs
        }

        runtime_dependencies.discard("")
        build_dependencies.discard("")
        return runtime_dependencies, build_dependencies

    ## @brief Collect external runtime imports from source modules.
    # @return {set[str]} External dependency names imported by src/git_alias/*.py modules.
    def _runtime_external_imports(self) -> set[str]:
        src_dir = self.REPO_ROOT / "src" / "git_alias"
        imported_roots: set[str] = set()

        for source_path in src_dir.glob("*.py"):
            tree = ast.parse(source_path.read_text(), filename=str(source_path))
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imported_roots.add(alias.name.split(".")[0])
                if isinstance(node, ast.ImportFrom) and node.module:
                    if node.level > 0:
                        continue
                    imported_roots.add(node.module.split(".")[0])

                if isinstance(node, ast.Call):
                    is_import_module = (
                        isinstance(node.func, ast.Attribute)
                        and isinstance(node.func.value, ast.Name)
                        and node.func.value.id == "importlib"
                        and node.func.attr == "import_module"
                    )
                    if is_import_module and node.args:
                        first_arg = node.args[0]
                        if isinstance(first_arg, ast.Constant) and isinstance(first_arg.value, str):
                            imported_roots.add(first_arg.value.split(".")[0])

        imported_roots.discard("git_alias")
        imported_roots.discard("__future__")
        stdlib_modules = {name.lower().replace("_", "-") for name in sys.stdlib_module_names}
        return {
            name.lower().replace("_", "-")
            for name in imported_roots
            if name.lower().replace("_", "-") not in stdlib_modules
        }

    ## @brief Verify runtime dependencies exactly match runtime external imports.
    # @return None.
    # @satisfies CPT-004
    def test_runtime_dependencies_match_external_imports(self):
        runtime_dependencies, _ = self._pyproject_dependencies()
        runtime_imports = self._runtime_external_imports()
        self.assertEqual(runtime_dependencies, runtime_imports)

    ## @brief Verify requirements.txt aligns with pyproject runtime+build dependencies.
    # @return None.
    # @satisfies CPT-004
    def test_requirements_matches_pyproject_dependency_union(self):
        requirements_dependencies = self._requirements_dependencies()
        runtime_dependencies, build_dependencies = self._pyproject_dependencies()
        self.assertEqual(
            requirements_dependencies,
            runtime_dependencies.union(build_dependencies),
        )

    ## @brief Verify launcher script hashes requirements and syncs `.venv` when changed.
    # @return None.
    # @satisfies CPT-009
    def test_g_script_hash_based_venv_sync_contract(self):
        script_path = self.REPO_ROOT / "scripts" / "g.sh"
        script_text = script_path.read_text()

        self.assertIn(
            'REQUIREMENTS_HASH_FILE="${VENVDIR}/.requirements.sha256"',
            script_text,
        )
        self.assertIn('current_hash="$(compute_requirements_hash)"', script_text)
        self.assertIn('if [ "${current_hash}" != "${previous_hash}" ]; then', script_text)
        self.assertIn(
            '"${VENVDIR}/bin/pip" install -r "${REQUIREMENTS_FILE}" >/dev/null',
            script_text,
        )
        self.assertIn('source "${VENVDIR}/bin/activate"', script_text)
        self.assertIn('sync_venv_requirements', script_text)


if __name__ == "__main__":
    unittest.main()
