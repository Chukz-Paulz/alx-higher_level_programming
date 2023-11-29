#!/usr/bin/python3

"""Print all possible different combinations of two digits in ascending order.

    The two digits must be different - 01 and 10 are considered identical.
    """
for digit1 in range(10):
    for digit2 in range(digit1 + 1, 10):
        separator = ", " if digit1 < 8 or digit2 < 9 else ""
        print(f"{digit1}{digit2}{separator}", end="")

