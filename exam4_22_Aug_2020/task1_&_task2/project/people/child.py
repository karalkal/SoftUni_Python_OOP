class Child:
    def __init__(self, food_cost: int, *toys_cost):
        # Calculation monthly cost here might be a problem
        self.cost = sum(toys_cost) + food_cost

# ivan = Child(33, 34)
# print(ivan)
