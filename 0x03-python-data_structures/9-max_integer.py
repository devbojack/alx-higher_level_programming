#!/usr/bin/python8

def max_integer(my_list=[]):
    my_len = len(my_list)
    x = 0

    if my_len > 0:
        for y in my_list:
            if y > x:
                x = y

    return (x)
