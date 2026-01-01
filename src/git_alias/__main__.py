"""Allow running the tool as a module."""
from .core import main
import sys


if __name__ == "__main__":
    sys.exit(main())
