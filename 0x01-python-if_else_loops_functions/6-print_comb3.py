#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if (x != y and x < y) and x < 9:
            if x == 8 and y == 9:
                print(f"{x}{y}")
            else:
                print(f"{x}{y}, ", end = "")
