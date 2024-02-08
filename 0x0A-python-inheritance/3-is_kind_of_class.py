#!/usr/bin/python3
"""3-is_kind_of_class module"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is
    an isinstance of the specified class,
    else false
    """
    if type(obj is a_class):
        return True
    else:
        return False
