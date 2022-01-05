from project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name, portion, brand):
        super().__init__(name, portion, 1.5, brand)


# perrier = Water("Still Water", 250, "Perrier")
# print(perrier)
