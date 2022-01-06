from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium

from project.decoration.ornament import Ornament
from project.decoration.plant import Plant

from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

from project.controller import Controller

aq = FreshwaterAquarium("Test Aq")
print(aq.name)
print(aq.capacity)
print(aq.decorations)
print(aq.fish)
aq.capacity = 1
print(aq.capacity, "Changed capacity to check if it will refuse fish")

gyz = Ornament()
huy = Ornament()

print(aq.calculate_comfort())
aq.add_decoration(gyz)
aq.add_decoration(huy)
print(aq.calculate_comfort())
print(aq.decorations)
print()

sharan = FreshwaterFish("Sharo", "riba", 55)
print(aq.add_fish(sharan))

sharan1 = FreshwaterFish("Sharo1", "riba", 55)
print(aq.add_fish(sharan1))

aq1 = SaltwaterAquarium("Test Aq number 1")
print(aq1.add_fish(sharan))
print(aq1.add_fish(sharan1))
print(aq1.fish)
aq1.remove_fish(sharan1)
print(aq1.fish)
print(aq1)
print()
print(aq1.add_fish(sharan1))
print(aq1)
print()
aq1.remove_fish(sharan)
aq1.remove_fish(sharan1)
print(aq1)
print()
aq1.add_decoration(gyz)
aq1.add_decoration(huy)
print(aq1)
print()


cont = Controller()
cont.add_aquarium("FreshwaterAquarium", "gyz")
cont.add_aquarium("FreshwaterAquarium", "kur")

print(cont.report())