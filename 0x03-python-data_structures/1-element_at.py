#!/usr/bin/python3

def element_at(my_list, idx):
    my_len = len(my_list)

    if idx <= my_len and idx >= 0:
        return (my_list[idx])
    else:
        return None
