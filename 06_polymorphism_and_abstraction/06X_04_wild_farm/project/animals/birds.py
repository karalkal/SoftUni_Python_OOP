from project.animals.animal import Animal, Bird
from project.food import Food


class Owl(Bird):
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if food.__class__.__name__ != "Meat":
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        else:
            self.weight += .25 * food.quantity
            self.food_eaten += food.quantity


class Hen(Bird):
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += .35 * food.quantity
        self.food_eaten += food.quantity

# from project.animals.birds import Owl
# from project.food import Meat, Vegetable, Fruit
#
# owl = Owl("Pip", 10, 10)
# print(owl)
# meat = Meat(4)
# print(owl.make_sound())
# owl.feed(meat)
# veg = Vegetable(1)
# print(owl.feed(veg))
# print(owl)
#
# hen = Hen("Harry", 10, 10)
# veg = Vegetable(3)
# fruit = Fruit(5)
# meat = Meat(1)
# print(hen)
# print(hen.make_sound())
# hen.feed(veg)
# hen.feed(fruit)
# hen.feed(meat)
# print(hen)
