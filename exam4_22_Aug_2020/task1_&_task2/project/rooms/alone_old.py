from project.rooms.room import Room


class AloneOld(Room):
    # __init__(family_name: str, pension: float)
    # This room has only one member, and the budget equals
    # the pension of the person.
    def __init__(self, name: str, budget: float):

        super().__init__(name, budget, 1)
        self.room_cost = 10


# dyrt = AloneOld("ivan", 1000)
# print(dyrt.name)
# print(dyrt.budget)
# print(dyrt.room_cost)
# print(dyrt.calculate_expenses())
# print(dyrt.members_count)
