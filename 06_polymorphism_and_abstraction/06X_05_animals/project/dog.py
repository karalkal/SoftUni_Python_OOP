from abc import ABC

from project.animal import Animal


class Dog(Animal, ABC):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def make_sound(self):
        return "Woof!"



# dog = Dog("Rocky", 3, "Male")
# print(dog.make_sound())
# print(dog)
