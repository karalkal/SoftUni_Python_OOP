from typing import List
from project.people.child import Child
from project.appliances.appliance import Appliance

"""
In this variant I have made the key method calculate expenses static.
It will be given args, perform calculation and RETURN a value 
which will then be assigned to the self.costs in the child classes with:
        self.expenses = self.calculate_expenses(*self.appliances, *self.children)
The other solution invokes the method in the __init__ and works more like a setter in mu humble opinion
"""

class Room:  # don't know if it's on purpose but by the task family_name argument was supposed to be just name
    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children: List[Child] = []
        self.appliances: List[Appliance] = []
        self.expenses = 0
        self.room_cost = 0

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    @staticmethod
    def calculate_expenses(*args):
        extras_cost = 0
        for arg in args:
            extra = arg.__class__.__name__
            if extra == "Child":
                extras_cost += arg.cost * 30
            elif extra == "TV" or extra == "Stove" or extra == "Laptop" or extra == "Fridge":
                extras_cost += arg.cost * 30  # for some reason cannot utilize the method * 30 in parent class
        return extras_cost

    def __repr__(self):
        result = f"{self.family_name} with {self.members_count} members. Budget: {self.budget}$, Expenses: {self.expenses}$\n"
        if self.children:
            for ch_no in range(len(self.children)):
                result += f"--- Child {ch_no + 1} monthly cost: {self.children[ch_no].cost * 30:.2f}$\n"
        if self.appliances:
            cost_of_all_appliances_for_one_month = sum([ap.cost for ap in self.appliances]) * 30
            result += f"Appliances monthly cost: {cost_of_all_appliances_for_one_month:.2f}$\n"

        return result
