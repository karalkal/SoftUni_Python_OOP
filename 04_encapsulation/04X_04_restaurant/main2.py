from project.beverage.beverage import Beverage
from project.beverage.coffee import Coffee
from project.beverage.tea import Tea
from project.food.cake import Cake
from project.food.dessert import Dessert
from project.food.food import Food
from project.food.main_dish import MainDish
from project.food.salmon import Salmon
from project.food.soup import Soup
from project.product import Product

product = Product("coffee", 2.5)
# product = Product("coffee", 22.5)
print(product.__class__.__name__)
print(product.name)
print(product.price)
print()

beverage = Beverage("coffee", 2.5, 50)
# beverage = Beverage("coffee", 222.5, 50)
print(beverage.__class__.__name__)
print(beverage.__class__.__bases__[0].__name__)
print(beverage.name)
print(beverage.price)
print(beverage.milliliters)
print()

some_food = Food("lajna", 7, 100)
print(some_food.__class__.__name__)
print(some_food.__class__.__bases__[0].__name__)
print(some_food.name)
print(some_food.price)
print(some_food.grams)
print()

soup = Soup("fish soup", 9.90, 230)
print(soup.__class__.__name__)
print(soup.__class__.__bases__[0].__name__)
print(soup.name)
print(soup.price)
print(soup.grams)
print()

schnitzel = MainDish("schnitzel", 99.90, 230)
print(schnitzel.__class__.__name__)
print(schnitzel.__class__.__bases__[0].__name__)
print(schnitzel.name)
print(schnitzel.price)
print(schnitzel.grams)
print()

solomon = Salmon("Solomon", 19.66)
print(solomon.__class__.__name__)
print(solomon.__class__.__bases__[0].__name__)
print(solomon.name)
print(solomon.price)
print(solomon.grams)
print()

ice_cream = Dessert("gelato", 19.66, 150, 2400)
print(ice_cream.__class__.__name__)
print(ice_cream.__class__.__bases__[0].__name__)
print(ice_cream.name)
print(ice_cream.price)
print(ice_cream.grams)
print("calories:", ice_cream.calories)
print()

cake1 = Cake("CAKE")
print(cake1.__class__.__name__)
print(cake1.__class__.__bases__[0].__name__)
print(cake1.name)
print("price:", cake1.price)
print("grams:", cake1.grams)
print("calories:", cake1.calories)
print()

jasmine_tea = Tea("Jasmine", 200, 19.66)
print(jasmine_tea.__class__.__name__)
print(jasmine_tea.__class__.__bases__[0].__name__)
print(jasmine_tea.name)
print(jasmine_tea.price)
print(jasmine_tea.milliliters)
print()

espresso = Coffee("Longo", 77.11)
print(espresso.__class__.__name__)
print(espresso.__class__.__bases__[0].__name__)
print(espresso.name)
print(espresso.price)
print(espresso.milliliters)
print()
