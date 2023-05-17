#!/usr/bin/python3

def roman_to_int(roman_string):

    if roman_string is None or type(roman_string) is not str:
        return 0

    num = 0
    last = 0
    roman_letters = [
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]

    for letter in roman_string:
        for let_r in roman_letters:
            if letter == let_r[0]:
                if last == 0 or last >= let_r[1]:
                    num += let_r[1]
                elif last < let_r[1]:
                    num += let_r[1] - (last * 2)

                last = let_r[1]

    return num
