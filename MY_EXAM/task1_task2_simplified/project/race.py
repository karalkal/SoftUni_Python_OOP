from typing import List
from project.driver import Driver


class Race:
    def __init__(self, name):
        self.name = name
        self.drivers: List[Driver] = []  # list of objects, obviously

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be an empty string!")
        self.__name = value
