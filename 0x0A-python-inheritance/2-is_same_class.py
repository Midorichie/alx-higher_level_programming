#!/usr/bin/python3
"""2-is_same_class module"""


def is_same_class(obj, a_class):
    """ returns true if the object is exactly an
    isinstance of the specified class ; else false
    """

    if type(obj) is a_class:
        return True
    else:
        return False
