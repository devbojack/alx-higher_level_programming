#!/usr/bin/python3
def remove_char_at(str, n):
    new_s = ""

    for x in range(len(str)):
        if x != n:
            new_s += str[x]

    return (new_s)
