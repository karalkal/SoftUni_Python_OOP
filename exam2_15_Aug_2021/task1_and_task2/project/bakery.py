from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type not in ["Bread", "Cake"]:
            return
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        if food_type == "Bread":
            self.food_menu.append(Bread(name, price))
            return f"Added {name} (Bread) to the food menu"
        if food_type == "Cake":
            self.food_menu.append(Cake(name, price))
            return f"Added {name} (Cake) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type not in ["Tea", "Water"]:
            return
        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")
        if drink_type == "Tea":
            self.drinks_menu.append(Tea(name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"
        if drink_type == "Water":
            self.drinks_menu.append(Water(name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        # first check if already exists
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        # might be a problem with numbering
        if table_type == "InsideTable":
            created_table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            created_table = OutsideTable(table_number, capacity)
        else:
            return
        self.tables_repository.append(created_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):  # food_name1: str, food_name2: str)
        current_table = None
        for table in self.tables_repository:
            if table.table_number == table_number:
                current_table = table
                break
        if not current_table:
            return f"Could not find table {table_number}"

        ordered = f"Table {table_number} ordered:\n"
        not_ordered = f"{self.name} does not have in the menu:\n"
        for item in args:
            in_menu = False
            for food in self.food_menu:
                if food.name == item:
                    current_table.order_food(food)
                    ordered += str(food) + "\n"
                    in_menu = True
                    break
            if not in_menu:
                not_ordered += item + "\n"

        return ordered + not_ordered

    def order_drink(self, table_number: int, *args):  # drinks as args
        current_table = None
        for table in self.tables_repository:
            if table.table_number == table_number:
                current_table = table
                break
        if not current_table:
            return f"Could not find table {table_number}"

        ordered = f"Table {table_number} ordered:\n"
        not_ordered = f"{self.name} does not have in the menu:\n"
        for item in args:
            in_menu = False
            for drink in self.drinks_menu:
                if drink.name == item:
                    current_table.order_drink(drink)
                    ordered += str(drink) + "\n"
                    in_menu = True
                    break
            if not in_menu:
                not_ordered += item + "\n"

        return ordered + not_ordered

    def leave_table(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                bill_as_int = table.get_bill()
                self.total_income += bill_as_int
                table.clear()
                # Your string is all wrong man, check task descr.
                return f"Table: {table_number}\nBill: {bill_as_int:.2f}"
            return  # if not found

    def get_free_tables_info(self):
        result_free_tables = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                result_free_tables += table.free_table_info() + "\n"
        return result_free_tables

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

#
# bak = Bakery("BAK")
# bak.food_menu = [Bread("br1", 22), Bread("br2", 88)]
# print(bak.food_menu)
# bak.add_table("InsideTable", 1, 22)
# result = bak.order_food(1, "lajna", "govna", "smrad", "GRESHKA", "br1", "br2")
# print(result)
#
# print()
# bak.drinks_menu = [Water("wat1", 200, "evian"), Water("wat2", 170, "perrier")]
# print(bak.drinks_menu)
# bak.add_table("OutsideTable", 81, 22)
# result = bak.order_drink(81, "lajna", "govna", "smrad", "GRESHKA", "wat1", "wat2")
# print(result)
#
# print()
# print(bak.leave_table(1))
# print(bak.leave_table(81))
#
# print()
# print(bak.get_free_tables_info())
#
# print(bak.get_total_income())
