from abc import ABC

from project.cat import Cat


class Kitten(Cat, ABC):
    def __init__(self, name, age, gender="Female"):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Meow"


# kitten = Kitten("Kiki", 1)
# print(kitten.make_sound())
# print(kitten)
