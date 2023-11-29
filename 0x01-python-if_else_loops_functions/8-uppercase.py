#!/usr/bin/python3

def uppercase(input_str):
    """Print a string in uppercase."""
    for char in input_str:
        print("{}".format(chr(ord(char) - 32) if 97 <= ord(char) <= 122 else char), end="")
    print("")
