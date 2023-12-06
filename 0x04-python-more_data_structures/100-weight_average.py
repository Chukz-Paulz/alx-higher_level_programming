#!/usr/bin/python3
#100-weight_average.py

def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    return sum(x * y for x, y in my_list) / sum(y for _, y in my_list)
