## @file __main__.py
# @brief Module-execution adapter for invoking CLI main entrypoint.
from .core import main
import sys


if __name__ == "__main__":
    sys.exit(main())
