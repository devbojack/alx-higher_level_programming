#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    my_len = len(my_list)

    if idx >= 0 and idx < my_len:
        new_list = my_list.copy()
        new_list[idx] = element
        return (new_list)
    else:
        return (my_list)
