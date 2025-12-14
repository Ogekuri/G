"""Core Git automation functionality."""

import os
from typing import List, Optional, Tuple
import git
from git import Repo, InvalidGitRepositoryError, GitCommandError


class GitRepo:
    """Wrapper class for automating common git operations."""

    def __init__(self, path: str = "."):
        """
        Initialize GitRepo with a repository path.
        
        Args:
            path: Path to the git repository (default: current directory)
        
        Raises:
            InvalidGitRepositoryError: If path is not a git repository
        """
        try:
            self.repo = Repo(path, search_parent_directories=True)
            self.path = self.repo.working_dir
        except InvalidGitRepositoryError:
            raise InvalidGitRepositoryError(f"'{path}' is not a git repository")

    def status(self) -> dict:
        """
        Get the status of the repository.
        
        Returns:
            Dictionary with repository status information
        """
        return {
            "branch": self.current_branch(),
            "modified": [item.a_path for item in self.repo.index.diff(None)],
            "staged": [item.a_path for item in self.repo.index.diff("HEAD")],
            "untracked": self.repo.untracked_files,
            "is_dirty": self.repo.is_dirty(),
        }

    def current_branch(self) -> str:
        """Get the name of the current branch."""
        return self.repo.active_branch.name

    def branches(self, remote: bool = False) -> List[str]:
        """
        List all branches.
        
        Args:
            remote: If True, list remote branches; otherwise local branches
        
        Returns:
            List of branch names
        """
        if remote:
            return [ref.name for ref in self.repo.remote().refs]
        return [branch.name for branch in self.repo.branches]

    def create_branch(self, branch_name: str, checkout: bool = True) -> bool:
        """
        Create a new branch.
        
        Args:
            branch_name: Name of the new branch
            checkout: If True, checkout the new branch immediately
        
        Returns:
            True if successful
        """
        new_branch = self.repo.create_head(branch_name)
        if checkout:
            new_branch.checkout()
        return True

    def checkout(self, branch_name: str) -> bool:
        """
        Checkout a branch.
        
        Args:
            branch_name: Name of the branch to checkout
        
        Returns:
            True if successful
        """
        self.repo.git.checkout(branch_name)
        return True

    def add(self, files: Optional[List[str]] = None, all_files: bool = False) -> bool:
        """
        Stage files for commit.
        
        Args:
            files: List of file paths to stage
            all_files: If True, stage all modified and new files
        
        Returns:
            True if successful
        """
        if all_files:
            self.repo.git.add(A=True)
        elif files:
            self.repo.index.add(files)
        return True

    def commit(self, message: str, all_files: bool = False) -> str:
        """
        Commit staged changes.
        
        Args:
            message: Commit message
            all_files: If True, stage all modified files before committing
        
        Returns:
            Commit hash
        """
        if all_files:
            self.add(all_files=True)
        
        commit = self.repo.index.commit(message)
        return commit.hexsha

    def push(self, remote: str = "origin", branch: Optional[str] = None) -> bool:
        """
        Push commits to remote repository.
        
        Args:
            remote: Remote name (default: origin)
            branch: Branch name (default: current branch)
        
        Returns:
            True if successful
        """
        if branch is None:
            branch = self.current_branch()
        
        origin = self.repo.remote(name=remote)
        origin.push(branch)
        return True

    def pull(self, remote: str = "origin", branch: Optional[str] = None) -> bool:
        """
        Pull changes from remote repository.
        
        Args:
            remote: Remote name (default: origin)
            branch: Branch name (default: current branch)
        
        Returns:
            True if successful
        """
        if branch is None:
            branch = self.current_branch()
        
        origin = self.repo.remote(name=remote)
        origin.pull(branch)
        return True

    def log(self, max_count: int = 10) -> List[dict]:
        """
        Get commit history.
        
        Args:
            max_count: Maximum number of commits to return
        
        Returns:
            List of commit information dictionaries
        """
        commits = []
        for commit in self.repo.iter_commits(max_count=max_count):
            commits.append({
                "hash": commit.hexsha[:7],
                "author": str(commit.author),
                "date": commit.committed_datetime.isoformat(),
                "message": commit.message.strip(),
            })
        return commits

    def diff(self, cached: bool = False) -> str:
        """
        Show differences.
        
        Args:
            cached: If True, show staged changes; otherwise show unstaged
        
        Returns:
            Diff output as string
        """
        if cached:
            return self.repo.git.diff("--cached")
        return self.repo.git.diff()

    def stash(self, message: Optional[str] = None) -> bool:
        """
        Stash current changes.
        
        Args:
            message: Optional stash message
        
        Returns:
            True if successful
        """
        if message:
            self.repo.git.stash("push", "-m", message)
        else:
            self.repo.git.stash()
        return True

    def stash_pop(self) -> bool:
        """
        Apply and remove the most recent stash.
        
        Returns:
            True if successful
        """
        self.repo.git.stash("pop")
        return True

    def merge(self, branch_name: str) -> bool:
        """
        Merge a branch into the current branch.
        
        Args:
            branch_name: Name of the branch to merge
        
        Returns:
            True if successful
        """
        self.repo.git.merge(branch_name)
        return True

    def remote_list(self) -> List[Tuple[str, str]]:
        """
        List all remotes.
        
        Returns:
            List of tuples (remote_name, remote_url)
        """
        return [(remote.name, list(remote.urls)[0]) for remote in self.repo.remotes]

    def add_remote(self, name: str, url: str) -> bool:
        """
        Add a new remote.
        
        Args:
            name: Remote name
            url: Remote URL
        
        Returns:
            True if successful
        """
        self.repo.create_remote(name, url)
        return True

    def remove_remote(self, name: str) -> bool:
        """
        Remove a remote.
        
        Args:
            name: Remote name
        
        Returns:
            True if successful
        """
        self.repo.delete_remote(name)
        return True
