#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []

    for x in my_list:
        if x == search:
            x = replace
        new_list.append(x)

    return (new_list)
