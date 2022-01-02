class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Planet name cannot be empty string or whitespace!")
        else:
            self.__name = value
            return self.__name

# mars = Planet("Mars")
# print(mars.name)

# nada = Planet("    \t     \n   ")
