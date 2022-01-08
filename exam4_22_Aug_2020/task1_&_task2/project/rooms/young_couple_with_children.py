from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    # __init__(family_name: str, salary_one: float, salary_two: float, *children)
    # This room has two members, and the budget equals
    # the two pensions of the people.
    def __init__(self, name: str, salary_one: float, salary_two: float, *children):
        super().__init__(name, salary_one + salary_two, len(children) + 2)
        self.room_cost = 30

        self.children = [ch for ch in children]
        num_of_people = len(children) + 2

        appliances = []
        for i in range(num_of_people):
            appliances.append(TV())
            appliances.append(Laptop())
            appliances.append(Fridge())
        self.appliances = appliances

        self.calculate_expenses(*self.appliances, *self.children)

# ivancho = Child(31, 23)
# marijka = Child(35, 6)
#
# penchevi = YoungCoupleWithChildren("penchevi", 8888, 4444, [ivancho, marijka])
# print(penchevi.children)
# print()
# print(penchevi.appliances)
# print()
# print(penchevi.calculate_expenses(*penchevi.appliances))
# print(len(penchevi.appliances))
