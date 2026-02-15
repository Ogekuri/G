import ast
import unittest
from pathlib import Path


class CommentFormatTest(unittest.TestCase):
    def test_no_runtime_docstrings_in_core(self):
        source = Path("src/git_alias/core.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        self.assertIsNone(ast.get_docstring(tree), msg="Module docstring must be removed")
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                self.assertIsNone(ast.get_docstring(node), msg=f"Docstring found in {node.name}")

    def test_functions_have_doxygen_brief_and_return(self):
        lines = Path("src/git_alias/core.py").read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines):
            stripped = line.lstrip()
            if stripped.startswith("def ") or stripped.startswith("async def "):
                j = idx - 1
                while j >= 0 and lines[j].strip():
                    j -= 1
                block = [item.lstrip() for item in lines[j + 1 : idx]]
                self.assertTrue(any(item.startswith("## @brief ") for item in block), msg=f"Missing @brief before line {idx + 1}")
                self.assertTrue(any(item.startswith("# @return ") for item in block), msg=f"Missing @return before line {idx + 1}")
