#!/usr/bin/python3
"""11-student module"""


class Student:
    """A class student that defines a student"""
    def __init__(self, first_name, last_name, age):
        """The class constructor.
        Args:
            first_name: the first name of the student
            last_name: the last name of the student
            age: the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation
        of a student instance.
        """
        result = {}
        if attrs is None:
            for key in self.__dict__:
                result[key] = getattr(self, key)
        else:
            for key in attrs:
                if hasattr(self, key):
                    result[key] = getattr(self, key)
        return result

    def reload_from_json(self, Json):
        """Public method that replaces all attributes of the student instance
        Args:
            jaon: It's a dictionary
        """
        for key, value in Json.items():
            setattr(self, key, value)
