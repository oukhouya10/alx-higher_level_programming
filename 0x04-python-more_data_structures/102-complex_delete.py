#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_list = []
    for i, j in a_dictionary.items():
        if j == value:
            key_list.append(i)
    for x in key_list:
        del a_dictionary[x]
    return a_dictionary
