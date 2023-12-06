#!/usr/bin/python3
#100-weight_average.py

def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not my_list or not isinstance(my_list, list):
        return (0)

    total_sum = 0
    total_weight = 0

    for tup in my_list:
        total_sum += tup[0] * tup[1]
        total_weight += tup[1]

    return (total_sum / total_weight if total_weight != 0 else 0)
