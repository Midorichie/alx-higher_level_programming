#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    else: 
        maximum_integer = my_list[0]
        for m in range(len(my_list)):
            if my_list[m] > maximum_integer:
                maximum_integer = my_list[m]
        return maximum_integer
