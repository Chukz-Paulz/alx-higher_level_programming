#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

def print_usage_and_exit():
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

if __name__ == "__main__":
    if len(argv) != 4:
        print_usage_and_exit()

    a, op, b = int(argv[1]), argv[2], int(argv[3])

    if op in {"+", "-", "*", "/"}:
        if op == "+":
            result = add(a, b)
        elif op == "-":
            result = sub(a, b)
        elif op == "*":
            result = mul(a, b)
        elif op == "/":
            result = div(a, b)

        print("{:d} {} {:d} = {:d}".format(a, op, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
