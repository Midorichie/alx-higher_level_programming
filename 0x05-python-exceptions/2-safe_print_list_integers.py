#!/usr/bin/python3
def safe_print_list_integer(my_list=[], x=0):
    count = 0
    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    Return
