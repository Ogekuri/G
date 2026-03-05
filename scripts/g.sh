#!/bin/bash
# -*- coding: utf-8 -*-
# VERSION: 0.12.0
# AUTHORS: Ogekuri

#/**
# * @brief Capture invocation timestamp for optional logging or tracing.
# * @details Single assignment; format `YYYY-MM-DD_HH-MM-SS` derived from system clock at startup.
# * @satisfies REQ-026
# */
now=$(date '+%Y-%m-%d_%H-%M-%S')

#/**
# * @brief Resolve absolute path of executing script.
# * @details Uses `readlink -f "$0"` to canonicalize all symlinks and relative components.
# *          Result is stored for directory and name extraction.
# * @satisfies REQ-026 REQ-030
# */
FULL_PATH=$(readlink -f "$0")

#/**
# * @brief Extract directory component of resolved script path.
# * @details Derived from FULL_PATH via `dirname`. Used as SRC_DIR base.
# * @satisfies REQ-026 REQ-030
# */
SCRIPT_PATH=$(dirname "$FULL_PATH")

#/**
# * @brief Extract filename component of resolved script path.
# * @details Derived from FULL_PATH via `basename`. Available for diagnostics.
# * @satisfies REQ-026
# */
SCRIPT_NAME=$(basename "$FULL_PATH")

#/**
# * @brief Extract base directory.
# * @details Derived from SCRIPT_PATH via `dirname`. Used as BASE_DIR base.
# */
BASE_DIR=$(dirname "$SCRIPT_PATH")

###############################################################################
## @brief Resolve project root from git repository.
## @details Uses `git rev-parse --show-toplevel` to determine project root.
##          Exits non-zero with error message when invoked outside a git repo.
## @satisfies REQ-034 REQ-007 DES-001
###############################################################################
PROJECT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
if [ -z "$PROJECT_ROOT" ]; then
    echo "❌ Errore: Impossibile determinare la root del progetto."
    exit 1
fi

###############################################################################
## @brief Resolve virtual environment path.
## @details Defines canonical `.venv` location for launcher runtime setup.
## @satisfies CPT-004
###############################################################################
VENVDIR="${BASE_DIR}/.venv"

# Create virtual environment when missing.
if ! [ -d "${VENVDIR}/" ]; then
    echo -n "Create virtual environment ..."
    mkdir -p "${VENVDIR}/"
    virtualenv --python=python3 "${VENVDIR}/" >/dev/null
    echo "done."

    # Install requirements during first environment creation.
    source "${VENVDIR}/bin/activate"
    echo -n "Install python requirements ..."
    "${VENVDIR}/bin/pip" install -r "${BASE_DIR}/requirements.txt" >/dev/null
    echo "done."
else
    source "${VENVDIR}/bin/activate"
fi

# Execute application:
PYTHONPATH="${BASE_DIR}/src:${PYTHONPATH}" \
    exec ${VENVDIR}/bin/python3 -c 'from git_alias.core import main; raise SystemExit(main())' "$@"
