#! /usr/bin/env python3

import sys

# Read line from STDIN
for line in sys.stdin:
    # Remove leading spaces and new line from input
    l = line.strip("")
    l = line.strip("\n")
    # Split words using space
    words = l.split(" ")
    for w in words:
        # Check if word is alphanumeric before printing (STDOUT) for reducer
        # Count of each word is 1
        print(f"{w}\t{1}")
