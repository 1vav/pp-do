#!/bin/bash

set -e

virtualenv -p /opt/homebrew/Cellar/python@3.11/3.11.4/bin/python3.11 virtualenv
python3.11 -m pip install -r requirements.txt --platform manylinux2010_x86_64 --only-binary=:all: --upgrade --target virtualenv/lib/python3.11/site-packages
