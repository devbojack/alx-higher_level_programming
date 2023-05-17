#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    del_k = []

    for k, v in a_dictionary.items():
        if v == value:
            del_k.append(k)

    for x in del_k:
        del a_dictionary[x]

    return (a_dictionary)
