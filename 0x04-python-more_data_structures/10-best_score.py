#!/usr/bin/python3

def best_score(a_dictionary):
    highscore = 0

    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > highscore:
                highscore = v
                high_key = k
        return (high_key)
    else:
        return (None)
