#!/usr/bin/env python3
def print_last_digit(number):
    if number >= 0:
        x = number % 10
    elif number < 0:
        x = (number * -1) % 10

    print(f"{x}", end="")
    return (x)
