from abc import ABC, abstractmethod


class Astronaut(ABC):
    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []
        self.breath_volume = 10

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        else:
            self.__name = value
            return self.__name

    def breathe(self):
        self.oxygen -= self.breath_volume
        return self.oxygen

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
        return self.oxygen

# ivan = Astronaut("ivancho", 45)
# nikoj1 = Astronaut("", 45)
# print(nikoj1.name)
# nikoj2 = Astronaut("  \n  \n ", 55)
# print(nikoj2.name)
# print(ivan.name)
# print(ivan.breathe())
# print(ivan.breathe())
# print(ivan.oxygen)
# print(ivan.increase_oxygen(480))
# print(ivan.oxygen)
