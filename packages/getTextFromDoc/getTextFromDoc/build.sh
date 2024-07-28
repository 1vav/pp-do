#!/bin/bash

set -e

virtualenv -p /opt/homebrew/Cellar/python@3.11/3.11.4/bin/python3.11 virtualenv 
source virtualenv/bin/activate
pip3 install -r requirements.txt
deactivate
