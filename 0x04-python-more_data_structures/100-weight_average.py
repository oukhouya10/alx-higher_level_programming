#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight = 0
    n = 0
    for element in my_list:
        n += element[0] * element[1]
        weight += element[1]
    return n / weight
