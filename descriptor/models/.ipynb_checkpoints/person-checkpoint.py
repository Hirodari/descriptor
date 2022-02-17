"""
    This module records person attributes
"""

from descriptor.utils.validator import ValidType


class Person:
    first_name = ValidType(str, 2, 10)
    last_name = ValidType(str, 2, 15)
    age = ValidType(int, 1, 200)
    skills = ValidType(list, 1, 4)

    def __init__(self, first_name, last_name, age, skills=None):
        """
        param
        first_name(str): First name of the person
        last_name(str): Last name of the person
        age(int): Age of the person
        skills: if any a list of skills
        return: first_name, last_name, age and list of skills if any
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.skills = skills

    def __eq__(self, other):
        if not isinstance(other, Person):
            # raise NotImplemented
            raise ValueError("Cannot be compared")
        return (
            self.first_name == other.first_name and
            self.last_name == other.last_name and
            self.age == other.age and
            self.skills == other.skills
        )

    def __repr__(self):
        return f"Person(first_name={self.first_name}, last_name={self.last_name}, " \
               f"age={self.age}, skills={self.skills})"

    def __str__(self):
        return f"Person({self.first_name}, {self.last_name}, {self.age}, {self.skills})"
