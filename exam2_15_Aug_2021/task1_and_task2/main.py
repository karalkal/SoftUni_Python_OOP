from project.baked_food.bread import Bread
from project.drink.tea import Tea
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table
from project.bakery import Bakery

drink = Tea("black", 220, "Lipton")
drink1 = Tea("red", 250, "Lipton1")
drink2 = Tea("blue", 300, "Lipton2")
drink3 = Tea("green", 200, "Lipton3")
print(drink1)
food = Bread("french", 1.8)
food1 = Bread("german", 1.9)
food2 = Bread("italian", 2)
food3 = Bread("spanish", 1.6)
print(food3)
# table = OutsideTable(1, 8)
outside_table_1 = OutsideTable(51, 8)
outside_table_1.order_drink(drink)
outside_table_1.order_food(food)
print(outside_table_1.get_bill())

inside_table_1 = InsideTable(11, 8)
inside_table_1.reserve(6)
inside_table_1.order_drink(drink1)
inside_table_1.order_drink(drink2)
inside_table_1.order_drink(drink3)
inside_table_1.order_food(food1)
inside_table_1.order_food(food2)
inside_table_1.order_food(food3)
print(inside_table_1.get_bill())
print(inside_table_1.free_table_info())  # returns None because is_reserved = True
inside_table_1.clear()
print(inside_table_1.free_table_info())

my_bakery = Bakery("Pri Pesho")
print(my_bakery.add_food("Bread", "french", 1.8))
# print(my_bakery.add_food("Bread", "french", 1.8))
print(my_bakery.add_food("Bread", "italian", 2.8))
print(my_bakery.add_drink("Water", "still", 240, "Devin"))
# print(my_bakery.add_drink("Water", "con gas", 220, "Perrier"))
print(my_bakery.add_drink("Water", "con gas", 220, "Perrier"))
print(my_bakery.add_table("InsideTable", 44, 6))
print(my_bakery.add_table("OutsideTable", 74, 6))
print(my_bakery.reserve_table(2))
print(my_bakery.reserve_table(200))
print()
print(my_bakery.order_food(44, "french", "italian", "english"))
print(my_bakery.order_drink(44, "still", "con gas", "cognac"))

print(my_bakery.add_table("InsideTable", 34, 6))
print(my_bakery.add_table("InsideTable", 45, 6))
print(my_bakery.add_table("InsideTable", 47, 6))
print(my_bakery.add_table("InsideTable", 22, 6))
print(my_bakery.get_free_tables_info())

# print(my_bakery.add_food("Bread", "french", 1.8))

# print(my_bakery.add_table("InsideTable", 44, 6))













