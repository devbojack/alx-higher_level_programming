#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    total_untuple = [0, 0]
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    if a_len < 2 or b_len < 2:
        while a_len < 2:
            list_a.append(0)
            a_len += 1
        while b_len < 2:
            list_b.append(0)
            b_len += 1

    for x in range(a_len):
        a = list_a[x]
        b = list_b[x]
        c = a + b
        total_untuple[x] = c

    total_tuple = tuple(total_untuple)

    return (total_tuple)
