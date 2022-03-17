#!/usr/bin/env bash

# https://stackoverflow.com/a/677212
if ! command -v interrogate &> /dev/null
then
    echo "Coverage module isn't installed - try $ pip3 install --user interrogate"
    echo "Also, make sure Pip's user install location (~/Library/Python/3.8/bin on macOS) is on your PATH."
    exit
fi

interrogate -vv -n -e unit_tests.py .