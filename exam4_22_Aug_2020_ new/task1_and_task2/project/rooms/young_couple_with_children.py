from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren:
    pass


class YoungCoupleWithChildren(Room):
    def __init__(self, name, salary_one, salary_two, *children):
        super().__init__(name, salary_one + salary_two, 2 + len(children))
        self.room_cost = 30
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.children = [ch for ch in children]

        self.expenses = self.calculate_expenses(*self.appliances, *self.children)

#
# sopranos = YoungCoupleWithChildren("oppa", 8888, 1111, "ivancho", "marijka", "petyrcho")
# print(sopranos.family_name)
# print(sopranos.expenses)
# print(sopranos.room_cost)
# print(sopranos.appliances)
# print(sopranos.children)
