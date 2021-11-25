from abc import ABC

from project.animals.animal import Animal, Mammal
from project.food import Food


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super(Mouse, self).__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Vegetable" and \
                food.__class__.__name__ != "Fruit":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += .10 * food.quantity
            self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super(Dog, self).__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += .40 * food.quantity
            self.food_eaten += food.quantity


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super(Cat, self).__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat" and \
                food.__class__.__name__ != "Vegetable":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += .3 * food.quantity
            self.food_eaten += food.quantity


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super(Tiger, self).__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += 1 * food.quantity
            self.food_eaten += food.quantity

# ivan = Dog("Ivan", 11, "Gabrovo")
# print(ivan)
# meat = Meat(8)
# seeds = Seed(40)
# print(ivan.make_sound())
# print(ivan.feed(seeds))
# ivan.feed(meat)
# print(ivan)
#
# stefka = Cat("Stefka-Котянциту", 11, "Gabrovo")
# print(stefka)
# meat = Meat(8)
# vegetable = Vegetable(25)
# meat = Meat(8)
# seeds = Seed(11)
# fruit = Fruit(40)
# print(stefka.make_sound())
# print(stefka.feed(seeds))
# stefka.feed(meat)
# print(stefka)
# print(stefka.feed(fruit))
# stefka.feed(vegetable)
# print(stefka)
