from project.drink import Drink
from project.food import Food
from project.product_repository import ProductRepository

milk = Food("milk")
print(milk)
milk = Food("milk", 33)
print(milk)
# print(milk.increase(5))
# print(milk.decrease(55))
# print(milk.decrease(18))
print()
dao = Drink("dao_wine")
print(dao)
dao = Drink("dao_wine", 103)
print(dao)
# print(dao.increase(88))
dao.decrease(202)
dao.decrease(82)
print()
rioja = Drink("rioja_wine")
print()
repo1 = ProductRepository()
repo1.add(dao)
repo1.add(rioja)
repo1.add(milk)
repo1.find("milk")


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)


print(repo1)
