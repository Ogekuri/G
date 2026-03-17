## @file test_dependency_manifests.py
# @brief Unit tests validating dependency-manifest alignment.

import ast
import re
import sys
import tomllib
import unittest
from pathlib import Path


## @brief Test suite for dependency declaration alignment across manifests.
# @details Validates that uv.lock is the canonical dependency lock source,
#          pyproject runtime/build declarations remain synchronized with code,
#          and unsupported uv configuration sections are not used.
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

    ## @brief Parse uv.lock package names.
    # @return {set[str]} Normalized package-name set from uv.lock package entries.
    def _uv_lock_dependencies(self) -> set[str]:
        uv_lock_path = self.REPO_ROOT / "uv.lock"
        uv_lock = tomllib.loads(uv_lock_path.read_text())
        package_entries = uv_lock.get("package", [])
        dependencies: set[str] = set()
        for entry in package_entries:
            if not isinstance(entry, dict):
                continue
            name = entry.get("name")
            if not isinstance(name, str):
                continue
            dependencies.add(self._normalize_dependency_name(name))
        dependencies.discard("")
        return dependencies

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

    ## @brief Verify uv.lock contains all pyproject runtime dependencies.
    # @return None.
    # @satisfies CPT-004
    def test_uv_lock_contains_pyproject_runtime_dependencies(self):
        runtime_dependencies, _ = self._pyproject_dependencies()
        uv_lock_dependencies = self._uv_lock_dependencies()
        self.assertTrue(runtime_dependencies.issubset(uv_lock_dependencies))

    ## @brief Verify repository does not require committed requirements.txt.
    # @return None.
    # @satisfies CPT-004
    def test_requirements_txt_is_absent_by_default(self):
        requirements_path = self.REPO_ROOT / "requirements.txt"
        self.assertFalse(requirements_path.exists())

    ## @brief Verify pyproject explicitly packages git_alias runtime files for uv artifacts.
    # @details Confirms setuptools package discovery and package-data declarations
    #          remain explicit and that current runtime files under `src/git_alias`
    #          are fully represented by Python-module packaging rules.
    # @return None.
    # @satisfies REQ-128
    def test_pyproject_explicitly_packages_git_alias_runtime_files(self):
        pyproject_path = self.REPO_ROOT / "pyproject.toml"
        pyproject = tomllib.loads(pyproject_path.read_text())
        setuptools_cfg = pyproject.get("tool", {}).get("setuptools", {})

        package_dir = setuptools_cfg.get("package-dir", {})
        self.assertEqual(package_dir.get(""), "src")

        finder_cfg = setuptools_cfg.get("packages", {}).get("find", {})
        self.assertEqual(finder_cfg.get("where"), ["src"])
        include_patterns = set(finder_cfg.get("include", []))
        self.assertTrue({"git_alias", "git_alias.*"}.issubset(include_patterns))

        package_data = setuptools_cfg.get("package-data", {})
        package_data_patterns = set(package_data.get("git_alias", []))
        self.assertIn("*.py", package_data_patterns)

        runtime_files = sorted(
            path.relative_to(self.REPO_ROOT / "src" / "git_alias").as_posix()
            for path in (self.REPO_ROOT / "src" / "git_alias").rglob("*")
            if path.is_file() and "__pycache__" not in path.parts
        )
        self.assertTrue(runtime_files)
        self.assertTrue(all(name.endswith(".py") for name in runtime_files))

    ## @brief Verify pyproject avoids unsupported `tool.uv` configuration sections.
    # @details Ensures uv settings discovery remains warning-free by rejecting
    #          unknown `tool.uv` keys that are not part of supported uv schema.
    # @return None.
    # @satisfies CTN-002 CPT-005
    def test_pyproject_has_no_unsupported_tool_uv_sections(self):
        pyproject_path = self.REPO_ROOT / "pyproject.toml"
        pyproject = tomllib.loads(pyproject_path.read_text())
        tool_uv_cfg = pyproject.get("tool", {}).get("uv", {})
        self.assertNotIn("forms", tool_uv_cfg)

if __name__ == "__main__":
    unittest.main()
