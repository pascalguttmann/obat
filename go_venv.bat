@echo off
rem ************************************************************************************************
rem
rem author: P. Guttmann
rem
rem This script can be used to activate the python venv, and if necessary create the local python
rem venv and install the dependencies required by `requirements.txt`.
rem The storage location of the created python venv, and the implicitly assumed directory to
rem activate the python venv is `.venv`.
rem
rem Usage:
rem     go_venv.bat
rem
rem ************************************************************************************************

set venv_dir=.venv
set venv_prompt=venv
set venv_activate=%venv_dir%\Scripts\activate
set venv_requirements=requirements.txt

if not exist %venv_activate% (
    rem python venv does not exist, so create it

    rem create the python venv locally
    python -m venv --prompt %venv_prompt% %venv_dir%

    rem activate the venv
    call %venv_activate%

    rem install dependencies
    pip install -r %venv_requirements%
) else (
    rem python venv does exist
    call %venv_activate%
)
