#!/usr/bin/python3
def uniq_add(my_list=[]):
    uni_list = set(my_list)
    n = 0
    for x in uni_list:
        n += x
    return (n)
