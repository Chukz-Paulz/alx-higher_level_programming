#!/usr/bin/python3
# 1-number_of_lines.py
"""Defines a text file line-counting function."""


def number_of_lines(filename=""):
    """Return the number of lines in a text file."""
    with open(filename) as file:
        lines = sum(1 for _ in file)
    return lines
