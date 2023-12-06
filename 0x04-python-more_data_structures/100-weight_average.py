def weight_average(my_list=[]):
    """Return the weighted average of integers in a list of tuples."""
    if not my_list:
        return 0

    total_weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for _, weight in my_list)

    if total_weight == 0:
        return 0

    return total_weighted_sum / total_weight
