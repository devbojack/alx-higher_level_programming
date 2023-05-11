#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """

    prints the number of and the list of its arguments

    """
    val_arg = sys.argv
    arg_len = len(val_arg) - 1

    if arg_len == 1:
        print(arg_len, 'argument:')
        for x in range(1, arg_len + 1):
            print("{:d}: {}".format(x, val_arg[x]))
    elif arg_len > 1:
        print(arg_len, 'arguments:')
        for x in range(1, arg_len + 1):
            print("{:d}: {}".format(x, val_arg[x]))
    elif arg_len == 0:
        print(arg_len, 'arguments.')
