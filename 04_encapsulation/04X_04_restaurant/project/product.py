class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @name.setter
    def name(self, value):
        self.__name = value

    @price.setter
    def price(self, value):
        self.__price = value
