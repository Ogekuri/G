# G - Quick Start Guide

## Installation

```bash
pip install -e .
```

## Basic Commands

### Status
```bash
g status                # Show repository status
g status --json         # Output as JSON
```

### Branches
```bash
g branch                # Show current branch
g branch --list         # List all local branches
g branch --remote       # List remote branches
g branch -c feature     # Create and checkout new branch
```

### Commits
```bash
g commit -m "message"   # Commit staged changes
g commit -a -m "msg"    # Stage all & commit
```

### Sync
```bash
g push                  # Push to origin
g pull                  # Pull from origin
```

### History
```bash
g log                   # Show last 10 commits
g log -n 5              # Show last 5 commits
```

### Stash
```bash
g stash                 # Stash changes
g stash -m "WIP"        # Stash with message
g stash --pop           # Pop stashed changes
```

## Python API

```python
from g import GitRepo

repo = GitRepo(".")
status = repo.status()
repo.create_branch("feature")
repo.add(all_files=True)
repo.commit("Update")
repo.push()
```

## Need Help?

```bash
g --help                # General help
g <command> --help      # Command-specific help
```
