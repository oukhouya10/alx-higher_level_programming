#!/usr/bin/python3
for y in range(100):
    print("{:02d}".format(y), end="\n" if y == 99 else ", ")
