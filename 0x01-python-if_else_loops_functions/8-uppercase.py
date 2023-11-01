#!/usr/bin/python3
def uppercase(str):
    for x in str:
        conv = ord(x)
        if conv in range(97, 123):
            conv = conv - 32
        print("{:c}".format(conv), end="")
    print()
