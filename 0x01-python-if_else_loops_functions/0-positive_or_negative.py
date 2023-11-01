#!/usr/bin/python3
import random
number = random.randint(-10, 10) # to generate a random num between -10 and 10
print(f"The number {number} is", end=" ")

if number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")
