from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, name, pension: float):
        super().__init__(name, pension, 1)
        self.room_cost = 10
        self.expenses = self.calculate_expenses(*self.appliances, *self.children)


# old_geezer = AloneOld("pesho", 8888)
# print(old_geezer.family_name)
# print(old_geezer.expenses)
# print(old_geezer.room_cost)
