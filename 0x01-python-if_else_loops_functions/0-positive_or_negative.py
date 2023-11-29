#!/usr/bin/python3
import random

def classify_number(number):
    if number > 0:
        return "{} is positive".format(number)
    elif number == 0:
        return "{} is zero".format(number)
    else:
        return "{} is negative".format(number)

if __name__ == "__main__":
    generated_number = random.randint(-10, 10)
    result = classify_number(generated_number)
    print(result)
