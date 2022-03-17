#!/usr/bin/env bash

# https://stackoverflow.com/a/677212
if ! command -v coverage &> /dev/null
then
    echo "Coverage module isn't installed - try $ pip3 install --user coverage"
    echo "Also, make sure Pip's user install location (~/Library/Python/3.8/bin on macOS) is on your PATH."
    exit
fi

coverage run unit_tests.py
coverage report
coverage html
python3 -m webbrowser -t file://$(pwd)/htmlcov/index.html