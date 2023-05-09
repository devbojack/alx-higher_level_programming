#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if (x % 3) == 0 or (x % 5) == 0:
            if (x % 3) == 0 and (x % 5) == 0:
                print("FizzBuzz", end=' ')
            elif (x % 3) == 0:
                print("Fizz", end=' ')
            else:
                print("Buzz", end=' ')
        else:
            print(x, end=" ")
