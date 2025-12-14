# G

Python Git Tool - Automate common git processes

## Overview

G is a Python-based git automation tool that simplifies common git workflows. It provides both a command-line interface and a Python API for automating git operations.

## Features

- **Branch Management**: Create, list, and checkout branches
- **Commit Automation**: Stage and commit changes with simple commands
- **Remote Operations**: Push, pull, and manage remotes
- **Status Checking**: Get detailed repository status
- **Stash Management**: Stash and retrieve changes
- **Commit History**: View formatted commit logs
- **Python API**: Use G as a library in your Python projects

## Installation

### From Source

```bash
git clone https://github.com/Ogekuri/G.git
cd G
pip install -e .
```

### From PyPI (coming soon)

```bash
pip install g-git-tool
```

## Usage

### Command Line Interface

#### Check Repository Status

```bash
g status
g status --json  # Output as JSON
```

#### Branch Management

```bash
# Show current branch
g branch

# List all branches
g branch --list

# List remote branches
g branch --remote

# Create and checkout a new branch
g branch -c feature-branch

# Create branch without checking out
g branch -c feature-branch --no-checkout
```

#### Checkout Branch

```bash
g checkout main
g checkout feature-branch
```

#### Commit Changes

```bash
# Commit staged changes
g commit -m "Add new feature"

# Stage all modified files and commit
g commit -a -m "Update all files"
```

#### Push and Pull

```bash
# Push current branch to origin
g push

# Push specific branch
g push --branch feature-branch

# Push to different remote
g push --remote upstream

# Pull from origin
g pull

# Pull specific branch
g pull --branch main
```

#### View Commit History

```bash
# Show last 10 commits
g log

# Show last 20 commits
g log -n 20

# Output as JSON
g log --json
```

#### Stash Management

```bash
# Stash current changes
g stash

# Stash with message
g stash -m "Work in progress"

# Pop stashed changes
g stash --pop
```

#### Remote Management

```bash
# List remotes
g remote

# Add a remote
g remote --add upstream https://github.com/user/repo.git

# Remove a remote
g remote --remove upstream
```

### Python API

Use G as a library in your Python projects:

```python
from g import GitRepo

# Initialize repository
repo = GitRepo("path/to/repo")

# Get status
status = repo.status()
print(f"Current branch: {status['branch']}")
print(f"Modified files: {status['modified']}")

# Create and checkout a new branch
repo.create_branch("feature-branch", checkout=True)

# Stage and commit changes
repo.add(all_files=True)
commit_hash = repo.commit("Add new feature")
print(f"Created commit: {commit_hash}")

# Push to remote
repo.push(remote="origin", branch="feature-branch")

# Get commit history
commits = repo.log(max_count=5)
for commit in commits:
    print(f"{commit['hash']}: {commit['message']}")

# Stash changes
repo.stash("Work in progress")

# Merge branch
repo.checkout("main")
repo.merge("feature-branch")
```

## Requirements

- Python 3.7 or higher
- GitPython 3.1.0 or higher

## Development

### Running Tests

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Author

Ogekuri

## Links

- Repository: https://github.com/Ogekuri/G
- Issues: https://github.com/Ogekuri/G/issues
