# Git Alias Emulator

This project exposes the `p.python` script (installed as `git-alias`) to reproduce the GIT aliases defined in `gitconfig.conf`, making them runnable both as a Python package and through `uvx`.

## Requirements

- Python 3.11+
- `uvx` (Astra UV) installed to execute commands in the cloud.

## Installation

```bash
python -m pip install .
```

After installation, the `git-alias` and `g` commands become globally available. Alternatively, you can invoke `p.python` directly from the repository root.

## Usage with uvx

The package exposes a dedicated form in `pyproject.toml`, so you can run it from any folder with:

```bash
uvx --from git+https://github.com/Ogekuri/G.git git-alias -- <alias> [args...]
```

When you are in the project root, you can also call:

```bash
uvx --form git-alias -- lg
```

`uvx` forwards any following parameters (`<alias>` and `[args...]`) to the invoked `git-alias` command.

## Helper launcher scripts

If you keep the `uv`/`uvx` CLI tools in `$HOME/bin`, you can rely on the provided installer scripts:

- `$HOME/bin/g-install`: installs `git-alias` from `git+https://github.com/Ogekuri/G.git` using `uv tool install`.
- `$HOME/bin/g-upgrade`: re-installs `git-alias` with `--force` to pick up the latest changes.
- `$HOME/bin/g-remove`: removes the globally installed `git-alias`.
- `$HOME/bin/g-live`: runs `git-alias` directly via `uvx --from git+https://github.com/Ogekuri/G.git git-alias`, mirroring the live invocation path.

## Examples

- `./p.python --help` prints the alphabetized alias list.
- `./p.python lg --help` shows the help text for the `lg` alias.
- `./p.python cm "Message"` runs `git commit` with the provided message.

## Testing

```bash
.venv/bin/python -m unittest tests/test_alias_help.py
```
