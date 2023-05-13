#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    my_len = len(my_list)

    if idx >= 0 and idx < my_len:
        del my_list[idx]

    return (my_list)
