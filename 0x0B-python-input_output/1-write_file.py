#!/usr/bin/python3
"""1-write_file module"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and returns
    the number of characters written.
    Args:
        Filename: name of the file
        text: Text to be written in the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        written_str = file.write(text)

        return written_str
