#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    the_names = dir(hidden_4)

    for x in range(len(the_names)):
        if the_names[x][:2] != '__':
            print(the_names[x])
