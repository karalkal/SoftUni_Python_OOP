from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, name, salary_one, salary_two):
        super().__init__(name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * 2

        self.expenses = self.calculate_expenses(*self.appliances, *self.children)

#
# mladite = YoungCouple("oppa", 8888, 1111)
# print(mladite.name)
# print(mladite.expenses)
# print(mladite.room_cost)
# print(mladite.appliances)
