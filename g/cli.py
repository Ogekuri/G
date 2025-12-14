"""Command-line interface for G git tool."""

import argparse
import sys
import json
from typing import List, Optional
from .core import GitRepo
from git import InvalidGitRepositoryError, GitCommandError


def format_status(status: dict) -> str:
    """Format status output."""
    lines = [f"On branch {status['branch']}\n"]
    
    if status['staged']:
        lines.append("Changes to be committed:")
        for file in status['staged']:
            lines.append(f"  modified: {file}")
        lines.append("")
    
    if status['modified']:
        lines.append("Changes not staged for commit:")
        for file in status['modified']:
            lines.append(f"  modified: {file}")
        lines.append("")
    
    if status['untracked']:
        lines.append("Untracked files:")
        for file in status['untracked']:
            lines.append(f"  {file}")
        lines.append("")
    
    if not status['is_dirty']:
        lines.append("Nothing to commit, working tree clean")
    
    return "\n".join(lines)


def cmd_status(args):
    """Handle status command."""
    try:
        repo = GitRepo(args.path)
        status = repo.status()
        if args.json:
            print(json.dumps(status, indent=2))
        else:
            print(format_status(status))
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_branch(args):
    """Handle branch command."""
    try:
        repo = GitRepo(args.path)
        if args.create:
            repo.create_branch(args.create, checkout=not args.no_checkout)
            print(f"Created branch '{args.create}'")
        elif args.list or args.remote:
            branches = repo.branches(remote=args.remote)
            for branch in branches:
                print(branch)
        else:
            print(f"Current branch: {repo.current_branch()}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_checkout(args):
    """Handle checkout command."""
    try:
        repo = GitRepo(args.path)
        repo.checkout(args.branch)
        print(f"Switched to branch '{args.branch}'")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_commit(args):
    """Handle commit command."""
    try:
        repo = GitRepo(args.path)
        commit_hash = repo.commit(args.message, all_files=args.all)
        print(f"Committed: {commit_hash[:7]}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_push(args):
    """Handle push command."""
    try:
        repo = GitRepo(args.path)
        repo.push(remote=args.remote, branch=args.branch)
        branch = args.branch or repo.current_branch()
        print(f"Pushed to {args.remote}/{branch}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_pull(args):
    """Handle pull command."""
    try:
        repo = GitRepo(args.path)
        repo.pull(remote=args.remote, branch=args.branch)
        branch = args.branch or repo.current_branch()
        print(f"Pulled from {args.remote}/{branch}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_log(args):
    """Handle log command."""
    try:
        repo = GitRepo(args.path)
        commits = repo.log(max_count=args.count)
        if args.json:
            print(json.dumps(commits, indent=2))
        else:
            for commit in commits:
                print(f"{commit['hash']} - {commit['author']}")
                print(f"  {commit['message']}")
                print(f"  Date: {commit['date']}\n")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_stash(args):
    """Handle stash command."""
    try:
        repo = GitRepo(args.path)
        if args.pop:
            repo.stash_pop()
            print("Stash popped")
        else:
            repo.stash(message=args.message)
            print("Changes stashed")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def cmd_remote(args):
    """Handle remote command."""
    try:
        repo = GitRepo(args.path)
        if args.add:
            repo.add_remote(args.add[0], args.add[1])
            print(f"Added remote '{args.add[0]}'")
        elif args.remove:
            repo.remove_remote(args.remove)
            print(f"Removed remote '{args.remove}'")
        else:
            remotes = repo.remote_list()
            for name, url in remotes:
                print(f"{name}\t{url}")
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="G - Python Git Tool for automating common git processes",
        prog="g"
    )
    parser.add_argument(
        "--path",
        default=".",
        help="Path to git repository (default: current directory)"
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Status command
    status_parser = subparsers.add_parser("status", help="Show repository status")
    status_parser.add_argument("--json", action="store_true", help="Output as JSON")
    status_parser.set_defaults(func=cmd_status)
    
    # Branch command
    branch_parser = subparsers.add_parser("branch", help="Manage branches")
    branch_parser.add_argument("-c", "--create", help="Create a new branch")
    branch_parser.add_argument("--no-checkout", action="store_true", help="Don't checkout new branch")
    branch_parser.add_argument("-l", "--list", action="store_true", help="List branches")
    branch_parser.add_argument("-r", "--remote", action="store_true", help="List remote branches")
    branch_parser.set_defaults(func=cmd_branch)
    
    # Checkout command
    checkout_parser = subparsers.add_parser("checkout", help="Checkout a branch")
    checkout_parser.add_argument("branch", help="Branch name to checkout")
    checkout_parser.set_defaults(func=cmd_checkout)
    
    # Commit command
    commit_parser = subparsers.add_parser("commit", help="Commit changes")
    commit_parser.add_argument("-m", "--message", required=True, help="Commit message")
    commit_parser.add_argument("-a", "--all", action="store_true", help="Stage all modified files")
    commit_parser.set_defaults(func=cmd_commit)
    
    # Push command
    push_parser = subparsers.add_parser("push", help="Push commits to remote")
    push_parser.add_argument("--remote", default="origin", help="Remote name (default: origin)")
    push_parser.add_argument("--branch", help="Branch name (default: current branch)")
    push_parser.set_defaults(func=cmd_push)
    
    # Pull command
    pull_parser = subparsers.add_parser("pull", help="Pull changes from remote")
    pull_parser.add_argument("--remote", default="origin", help="Remote name (default: origin)")
    pull_parser.add_argument("--branch", help="Branch name (default: current branch)")
    pull_parser.set_defaults(func=cmd_pull)
    
    # Log command
    log_parser = subparsers.add_parser("log", help="Show commit history")
    log_parser.add_argument("-n", "--count", type=int, default=10, help="Number of commits to show")
    log_parser.add_argument("--json", action="store_true", help="Output as JSON")
    log_parser.set_defaults(func=cmd_log)
    
    # Stash command
    stash_parser = subparsers.add_parser("stash", help="Stash changes")
    stash_parser.add_argument("-m", "--message", help="Stash message")
    stash_parser.add_argument("--pop", action="store_true", help="Pop stashed changes")
    stash_parser.set_defaults(func=cmd_stash)
    
    # Remote command
    remote_parser = subparsers.add_parser("remote", help="Manage remotes")
    remote_parser.add_argument("--add", nargs=2, metavar=("NAME", "URL"), help="Add a remote")
    remote_parser.add_argument("--remove", help="Remove a remote")
    remote_parser.set_defaults(func=cmd_remote)
    
    args = parser.parse_args()
    
    if not hasattr(args, "func"):
        parser.print_help()
        return 1
    
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
