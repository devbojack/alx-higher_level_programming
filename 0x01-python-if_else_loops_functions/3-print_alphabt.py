#!/usr/bin/python3
for x in range(97, 123):
    if x == 101 or x == 113:
        continue
    else:
        print(f"{x:c}", end="")
