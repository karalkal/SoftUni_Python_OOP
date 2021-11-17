from project.dough import Dough
from project.pizza import Pizza
from project.topping import Topping

# def test_pizza_add_topping_update(self):
d = Dough("Sugar", "Mixing", 20)
t = Topping("Tomato", 20)
p = Pizza("Burger", d, 200)
p.add_topping(t)
p.add_topping(t)

print(p.toppings["Tomato"], 40)
