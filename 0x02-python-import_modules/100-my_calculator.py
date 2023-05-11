#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    """

    handles basic calculator operations

    """

    arg_val = sys.argv
    arg_len = len(arg_val) - 1

    if arg_len == 3:
        if arg_val[2] != '+' or '-' or '*' or '/':
            operator = arg_val[2]
            a = int(arg_val[1])
            b = int(arg_val[3])

            if operator == '+':
                print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
            elif operator == '-':
                print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
            elif operator == '*':
                print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
            elif operator == '/':
                print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
            else:
                print("Unknown operator. Available operators: +, -, * and /")
                exit(1)
            exit(0)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
