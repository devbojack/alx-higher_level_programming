#!/usr/bin/python3

import sys

if __name__ == '__main__':
    """

    prints the result of the addition of all arguments

    """
    arg_val = sys.argv
    len_arg = len(arg_val)
    sum = 0

    if len_arg > 1:
        for x in range(1, len_arg):
            sum += int(arg_val[x])

    print("{:d}".format(sum))
