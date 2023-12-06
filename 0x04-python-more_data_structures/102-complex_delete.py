#!/usr/bin/python3
# 102-complex_delete.py

def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    return {k: v for k, v in a_dictionary.items() if v != value}
