#!/bin/bash

set -e

virtualenv -p /opt/homebrew/Cellar/python@3.11/3.11.4/bin/python3.11 virtualenv
source virtualenv/bin/activate
python3.11 -m pip install --no-deps --implementation cp --only-binary=:all: --platform manylinux2010_x86_64 -r requirements.txt --target virtualenv/bin
deactivate
