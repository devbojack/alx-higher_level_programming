#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    mult = 0
    divs = 0

    for x in my_list:
        mult += x[0] * x[1]
        divs += x[1]

    return (mult / divs)
