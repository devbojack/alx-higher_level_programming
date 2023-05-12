#!/usr/bin/python8

def multiple_returns(sentence):
    s_len = len(sentence)
    x = ""

    if s_len > 0:
        x = sentence[0]

    my_tuple = (s_len, x)
    return (my_tuple)
