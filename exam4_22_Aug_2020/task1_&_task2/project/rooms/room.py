class Room:
    def __init__(self, name: str, budget: float, members_count: int):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0
        self.appliances = []

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for obj in args:
            name_of_class = obj.__class__.__name__
            if name_of_class == "Child":
                result += obj.cost * 30
            elif name_of_class == "Appliance" or \
                    name_of_class == "TV" or \
                    name_of_class == "Laptop" or \
                    name_of_class == "Stove" or \
                    name_of_class == "Fridge":
                result += obj.get_monthly_expense()

        self.expenses = result
        return self.expenses
