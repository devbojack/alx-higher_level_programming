#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    my_len = len(my_list) - 1

    for x in range(my_len + 1):
        y = my_list[my_len - x]
        print("{:d}".format(y))
