## @file __init__.py
# @brief Package metadata and public entrypoint exports for git-alias CLI.

## @brief Semantic version string exposed by package metadata.
__version__ = "0.0.29"

from .core import main  # noqa: F401

## @brief Public symbols exported by the package root module.
__all__ = ["__version__", "main"]
