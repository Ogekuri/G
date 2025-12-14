"""Tests for core GitRepo functionality."""

import os
import tempfile
import shutil
import unittest
from pathlib import Path
import git
from g.core import GitRepo
from git import InvalidGitRepositoryError


class TestGitRepo(unittest.TestCase):
    """Test cases for GitRepo class."""

    def setUp(self):
        """Set up a temporary git repository for testing."""
        self.test_dir = tempfile.mkdtemp()
        self.repo = git.Repo.init(self.test_dir)
        
        # Configure git user for commits
        with self.repo.config_writer() as config:
            config.set_value("user", "name", "Test User")
            config.set_value("user", "email", "test@example.com")
        
        # Create an initial commit
        test_file = Path(self.test_dir) / "test.txt"
        test_file.write_text("Initial content")
        self.repo.index.add(["test.txt"])
        self.repo.index.commit("Initial commit")
        
        self.git_repo = GitRepo(self.test_dir)

    def tearDown(self):
        """Clean up temporary directory."""
        shutil.rmtree(self.test_dir)

    def test_init_valid_repo(self):
        """Test initialization with valid repository."""
        self.assertIsNotNone(self.git_repo.repo)
        self.assertEqual(self.git_repo.path, self.test_dir)

    def test_init_invalid_repo(self):
        """Test initialization with invalid repository."""
        invalid_dir = tempfile.mkdtemp()
        try:
            with self.assertRaises(InvalidGitRepositoryError):
                GitRepo(invalid_dir)
        finally:
            shutil.rmtree(invalid_dir)

    def test_current_branch(self):
        """Test getting current branch name."""
        branch = self.git_repo.current_branch()
        # Default branch could be 'master' or 'main'
        self.assertIn(branch, ["master", "main"])

    def test_create_branch(self):
        """Test creating a new branch."""
        self.git_repo.create_branch("test-branch", checkout=False)
        branches = self.git_repo.branches()
        self.assertIn("test-branch", branches)

    def test_checkout_branch(self):
        """Test checking out a branch."""
        self.git_repo.create_branch("test-branch", checkout=False)
        self.git_repo.checkout("test-branch")
        self.assertEqual(self.git_repo.current_branch(), "test-branch")

    def test_status_clean(self):
        """Test status on clean repository."""
        status = self.git_repo.status()
        self.assertFalse(status["is_dirty"])
        self.assertEqual(len(status["modified"]), 0)
        self.assertEqual(len(status["untracked"]), 0)

    def test_status_with_changes(self):
        """Test status with modified files."""
        test_file = Path(self.test_dir) / "test.txt"
        test_file.write_text("Modified content")
        
        status = self.git_repo.status()
        self.assertTrue(status["is_dirty"])
        self.assertIn("test.txt", status["modified"])

    def test_add_and_commit(self):
        """Test staging and committing changes."""
        test_file = Path(self.test_dir) / "new_file.txt"
        test_file.write_text("New file content")
        
        self.git_repo.add(files=["new_file.txt"])
        commit_hash = self.git_repo.commit("Add new file")
        
        self.assertIsNotNone(commit_hash)
        self.assertEqual(len(commit_hash), 40)  # SHA-1 hash length

    def test_log(self):
        """Test getting commit history."""
        commits = self.git_repo.log(max_count=5)
        self.assertGreater(len(commits), 0)
        self.assertIn("hash", commits[0])
        self.assertIn("message", commits[0])
        self.assertIn("author", commits[0])

    def test_branches_list(self):
        """Test listing branches."""
        branches = self.git_repo.branches()
        self.assertIsInstance(branches, list)
        self.assertGreater(len(branches), 0)

    def test_stash(self):
        """Test stashing changes."""
        test_file = Path(self.test_dir) / "test.txt"
        test_file.write_text("Modified for stash")
        
        # Verify file is modified
        status_before = self.git_repo.status()
        self.assertTrue(status_before["is_dirty"])
        
        # Stash the changes
        self.git_repo.stash("Test stash")
        
        # Verify working directory is clean
        status_after = self.git_repo.status()
        self.assertFalse(status_after["is_dirty"])


if __name__ == "__main__":
    unittest.main()
