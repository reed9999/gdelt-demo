#!/bin/bash
# This is a little utility script to make it easier to activate the virtualenv
# users will want to change this to match their own directory structure

# If you keep the ALIAS_NAME of act run as follows: 
# $ source alias-activate.sh ; act

VIRTUALENVS=~/.virtualenvs
VENV_NAME=gdelt-demo
ALIAS_NAME=act
alias $ALIAS_NAME="source $VIRTUALENVS/$VENV_NAME/bin/activate"

# My own bash failure--can't figure out why the next line doesn't invoke the alias.

# $ALIAS_NAME
