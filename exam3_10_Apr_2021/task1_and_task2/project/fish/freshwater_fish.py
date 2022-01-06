from project.fish.base_fish import BaseFish


# The FreshwaterFish could only live in FreshwaterAquarium!
class FreshwaterFish(BaseFish):
    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)

    def eat(self):
        self.size += 3

# sharo = FreshwaterFish("Sharo", "sharan", 5.55)
# print(sharo.name, sharo.price)
# print(sharo.size)
# sharo.eat()
# print(sharo.size)
