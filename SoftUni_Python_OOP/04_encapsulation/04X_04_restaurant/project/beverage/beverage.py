from project.product import Product


class Beverage(Product):
    def __init__(self, name, price, milliliters: float):
        super().__init__(name, price)
        self.milliliters: float = milliliters

    # def __init__(self, *args):
    #     super().__init__(args[0], args[1])
    #     self.milliliters: float = args[2]

    @property
    def milliliters(self):
        return self.__milliliters

    @milliliters.setter
    def milliliters(self, value):
        self.__milliliters = value
