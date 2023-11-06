#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        copy_l = []
        copy_l = my_list[:]
        if idx < 0 or idx >= len(my_list):
            return copy_l
        else:
            copy_l[idx] = element
            return copy_l
