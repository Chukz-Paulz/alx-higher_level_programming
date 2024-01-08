#!/usr/bin/python3
# 5-text_indentation.py
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sentence_endings = {'.', '?', ':'}

    start = 0
    while start < len(text) and text[start] == ' ':
        start += 1

    for char in text[start:]:
        print(char, end="")
        if char in sentence_endings:
            print("\n")
            start += 1
            while start < len(text) and text[start] == ' ':
                start += 1
    print()
