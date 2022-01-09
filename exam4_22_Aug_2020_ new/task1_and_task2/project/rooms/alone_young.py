from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, name, salary: float):
        super().__init__(name, salary, 1)
        self.room_cost = 10
        self.appliances = [TV()]
        # same as above but easier to understand for the idiot that I am
        # real_tv = TV()
        # self.appliances = [real_tv]
        self.expenses = self.calculate_expenses(*self.appliances, *self.children)


me = AloneYoung("AZ", 8888)
print(me.family_name)
print(me.expenses)
print(me.room_cost)
for tv in me.appliances:
    print(tv.__class__.__name__)
    print(tv)
