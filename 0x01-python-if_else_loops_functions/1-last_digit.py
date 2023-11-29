#!/usr/bin/python3
import random

def get_last_digit(number):
    abs_number = abs(number)
    return abs_number % 10 if number >= 0 else -abs_number % 10

def classify_last_digit(digit):
    if digit > 5:
        return "greater than 5"
    elif digit == 0:
        return "0"
    else:
        return "less than 6 and not 0"

if __name__ == "__main__":
    generated_number = random.randint(-10000, 10000)
    last_digit = get_last_digit(generated_number)
    
    print("Last digit of {} is {} and is {}".format(generated_number, last_digit, classify_last_digit(last_digit)))
