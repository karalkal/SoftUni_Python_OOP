from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, name, pension_one, pension_two):
        super().__init__(name, pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * 2

        self.expenses = self.calculate_expenses(*self.appliances, *self.children)

#
# dyrtite = OldCouple("dyrtite", 8888, 1111)
# print(dyrtite.family_name)
# print(dyrtite.expenses)
# print(dyrtite.room_cost)
