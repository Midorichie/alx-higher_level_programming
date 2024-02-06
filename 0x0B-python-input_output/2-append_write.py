#!/usr/bin/python3
"""2-append_write module"""


def append_write(filename="", text=""):
    """It appends a string at the end of a text file (UTF8)
    and returns the number of characters added.
    Args:
        filename: file to be opened
        text: it's what is to be appended to the file
    """
    with open(filename, "a", encoding="utf-8") as file:
        append_str = file.write(text)
        return append_str
