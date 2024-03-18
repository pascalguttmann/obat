#!/bin/bash -e

# ******************************************************************************
#
# author: P. Guttmann
#
# This script can be used to activate the python venv if necessary and
# serve the mkdocs documentation website at http://localhost:8000/obat.
#
# Usage:
#     ./go_mkdocs_serve.sh
#
# ******************************************************************************

source ./go_venv.sh

python -m webbrowser http://localhost:8000/obat

mkdocs serve
