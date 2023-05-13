#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        my_len = len(sentence)
        return (my_len, sentence[0])
