#!/usr/bin/env python
"""Example usage of G - Python Git Tool."""

from g import GitRepo

def main():
    """Demonstrate G git tool usage."""
    # Initialize repository
    print("Initializing repository...")
    repo = GitRepo(".")
    
    # Get current status
    print("\n=== Repository Status ===")
    status = repo.status()
    print(f"Current branch: {status['branch']}")
    print(f"Is dirty: {status['is_dirty']}")
    print(f"Modified files: {len(status['modified'])}")
    print(f"Untracked files: {len(status['untracked'])}")
    
    # List branches
    print("\n=== Branches ===")
    branches = repo.branches()
    for branch in branches:
        current = " (current)" if branch == status['branch'] else ""
        print(f"  {branch}{current}")
    
    # Show commit history
    print("\n=== Recent Commits ===")
    commits = repo.log(max_count=3)
    for commit in commits:
        print(f"{commit['hash']} - {commit['message']}")
    
    # Show remotes
    print("\n=== Remotes ===")
    remotes = repo.remote_list()
    for name, url in remotes:
        print(f"  {name}: {url}")
    
    print("\n✓ Example completed successfully!")

if __name__ == "__main__":
    main()
