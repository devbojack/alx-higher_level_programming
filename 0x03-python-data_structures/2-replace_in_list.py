#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    my_len = len(my_list)

    if idx <= my_len and idx >= 0:
        my_list[idx] = element
        return (my_list)
    else:
        return (my_list)
