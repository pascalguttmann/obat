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

main(){
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

  check_python_version 3 12 1

  if ! [ -f "$venv_activate" ]; then
      echo python venv does not exist

      echo create the python venv locally
      python -m venv --prompt $venv_prompt $venv_dir

      echo activate the venv
      source $venv_activate

      echo install dependencies
      pip install -r $venv_requirements
  else
      echo python venv does exist

      echo activate the venv
      source $venv_activate

      echo check and install dependencies
      pip install -q -r $venv_requirements
  fi
}

# check that python semantic version is compatible with argument version
# args:
#   major version
#   minor version
#   patch version
#
# example to test for version 3.12.1
#   check_python_version 3 12 1
check_python_version(){
  local version_info="$(python -c 'import sys; print(sys.version_info[:])')"
  local version_major=$(echo $version_info | sed -n 's/^(\([0-9]*\), \([0-9].*\), \([0-9]*\), \(.*\), \([0-9]*\))$/\1/p')
  local version_minor=$(echo $version_info | sed -n 's/^(\([0-9]*\), \([0-9].*\), \([0-9]*\), \(.*\), \([0-9]*\))$/\2/p')
  local version_patch=$(echo $version_info | sed -n 's/^(\([0-9]*\), \([0-9].*\), \([0-9]*\), \(.*\), \([0-9]*\))$/\3/p')
  echo detected python version: $version_major.$version_minor.$version_patch

  if [ "$version_major" -eq "$1" ] \
    && { \
          [ "$version_minor" -eq "$2" ] && [ "$version_patch" -ge "$3" ] \
      ||  [ "$version_minor" -gt "$2" ]; \
    }; \
  then
    echo check against version: $1.$2.$3 passed
    return 0
  else
    echo check against version: $1.$2.$3 failed
    return 1
  fi
}

main "$@"; exit
