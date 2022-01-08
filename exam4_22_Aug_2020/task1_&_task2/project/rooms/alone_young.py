from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    # __init__(family_name: str, salary: float)
    # This room has only one member,
    # and the budget equals the salary of the person.

    def __init__(self, name: str, budget: float):
        super().__init__(name, budget, 1)
        self.room_cost = 10
        self.appliances = [TV()]

        self.calculate_expenses(*self.appliances)

# Calculate the expenses of each appliance.

az = AloneYoung("Kurcho", 8888)

"""
N.B. If you call it again with no args like below it will 
just return zero
"""
# print(az.calculate_expenses())
print(az.expenses)

