from project.animals.birds import Animal, Owl, Hen
from project.animals.mammals import Cat, Dog, Tiger
from project.food import Meat, Vegetable, Fruit, Seed

owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
print()

hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)
print()

ivan = Dog("Ivan", 11, "Gabrovo")
print(ivan)
meat = Meat(8)
seeds = Seed(40)
print(ivan.make_sound())
print(ivan.feed(seeds))
ivan.feed(meat)
print(ivan)
print()

stefka = Cat("Stefka-Котянциту", 11, "Gabrovo")
print(stefka)
meat = Meat(8)
vegetable = Vegetable(25)
meat = Meat(8)
seeds = Seed(11)
fruit = Fruit(40)
print(stefka.make_sound())
print(stefka.feed(seeds))
stefka.feed(meat)
print(stefka)
print(stefka.feed(fruit))
stefka.feed(vegetable)
print(stefka)
print()

marko = Tiger("Marko", 10, "London")
print(marko)
print(marko.make_sound())
print(marko.feed(seeds))
print(marko.feed(vegetable))
print(marko.feed(fruit))
