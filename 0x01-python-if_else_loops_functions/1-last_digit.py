#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
x = ""

if last_digit > 5:
    x = "and is greater than 5"
elif last_digit == 0:
    x = "and is zero"
else:
    x = "and is less than 6 and not 0"
print(f"Last digit of {number} is {last_digit} {x}")
