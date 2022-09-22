#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number_int = -(abs(number) % 10)
else:
    number_int = abs(number) % 10

if number_int > 5:
    print(f"Last digit of {number} is {number_int} and is greater than 5")
elif number_int == 0:
    print(f"Last digit of {number} is {number_int} and is 0")
elif number_int < 6 and number_int != 0:
    print(f"Last digit of {number} is {number_int} and is less than 6 and not 0")
