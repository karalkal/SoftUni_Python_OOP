from project.fish.base_fish import BaseFish


# The SaltwaterFish could only live in SaltwaterAquarium!
class SaltwaterFish(BaseFish):
    def __init__(self, name, species, price):
        super().__init__(name, species, 5, price)

    def eat(self):
        self.size += 2

# caca = SaltwaterFish("CACA", "ocean_fish", 1.55)
# print(caca.name, caca.price)
# print(caca.size)
# caca.eat()
# print(caca.size)
