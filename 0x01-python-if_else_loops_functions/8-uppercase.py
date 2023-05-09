#!/usr/bin/python3
def uppercase(str):
    upper_string = ""
    for x in range(len(str)):
        if ord(str[x]) > 96 and ord(str[x]) < 123:
            upper_string += chr(ord(str[x]) - 32)
            continue
        upper_string += str[x]

    print("{}".format(upper_string))
