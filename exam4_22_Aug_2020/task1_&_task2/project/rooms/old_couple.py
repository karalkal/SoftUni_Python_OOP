from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    # __init__(family_name: str, pension_one: float, pension_two: float)
    # This room has two members, and the budget equals
    # the two pensions of the people.
    def __init__(self, name: str, pension_one: float, pension_two: float):
        super().__init__(name, pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove(), TV(), Fridge(), Stove()]

        self.calculate_expenses(*self.appliances)

