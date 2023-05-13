#!/usr/bin/python3

def max_integer(my_list=[]):
    my_len = len(my_list)

    if my_len > 0:
        x = my_list[0]
        for y in my_list:
            if y > x:
                x = y
        return (x)
    else:
        return (None)
