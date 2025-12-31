import ast
import unittest
from pathlib import Path


class CommentFormatTest(unittest.TestCase):
    def test_no_docstrings_in_core(self):
        source = Path("src/git_alias/core.py").read_text(encoding="utf-8")
        tree = ast.parse(source)
        self.assertIsNone(ast.get_docstring(tree), msg="Module docstring must be removed")
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                doc = ast.get_docstring(node)
                self.assertIsNone(
                    doc,
                    msg=f"Docstring found in {getattr(node, 'name', '<module>')}",
                )

    def test_functions_have_preceding_comment(self):
        lines = Path("src/git_alias/core.py").read_text(encoding="utf-8").splitlines()
        for idx, line in enumerate(lines):
            stripped = line.lstrip()
            if stripped.startswith("def ") or stripped.startswith("async def "):
                j = idx - 1
                while j >= 0 and not lines[j].strip():
                    j -= 1
                self.assertGreaterEqual(j, 0, msg=f"Missing comment before line {idx + 1}")
                self.assertTrue(
                    lines[j].lstrip().startswith("#"),
                    msg=f"Missing comment before line {idx + 1}",
                )

