#!/bin/bash -e

# ******************************************************************************
#
# author: P. Guttmann
#
# This script can be `sourced` to activate the python venv, and if necessary
# create the local python venv and install the dependencies required by
# `requirements.txt`.  The storage location of the created python venv, and the
# implicitly assumed directory to activate the python venv is `.venv`.
#
# Usage:
#     . ./go_venv.sh
#
# ******************************************************************************

venv_dir=./.venv
venv_prompt=venv
venv_requirements=requirements.txt

case "$OSTYPE" in
  msys* | cygwin*)
    echo "Operating System: WINDOWS"
    venv_activate=$venv_dir/Scripts/activate
    ;;
  *)
    echo "Operating System: $OSTYPE"
    venv_activate=$venv_dir/bin/activate
    ;;
esac

if ! [ -f "$venv_activate" ]; then
    # python venv does not exist, so create it

    # create the python venv locally
    python -m venv --prompt $venv_prompt $venv_dir

    # activate the venv
    source $venv_activate

    # install dependencies
    pip install -r $venv_requirements
else
    # python venv does exist
    source $venv_activate
fi

