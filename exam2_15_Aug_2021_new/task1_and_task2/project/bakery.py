from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []  # an empty list that will contain every type of food
        self.drinks_menu = []  # an empty list that will contain every type of drink
        self.tables_repository = []  # an empty list that will contain every table at the bakery
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
        # check if already in menu
        for food in self.food_menu:
            if food.name == name:
                raise Exception(f"{food_type} {name} is already in the menu!")
        # if not:
        if food_type == "Bread":
            new_food = Bread(name, price)
        elif food_type == "Cake":
            new_food = Cake(name, price)

        self.food_menu.append(new_food)
        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type not in ["Tea", "Water"]:
            return
        # check if already in menu
        for drink in self.drinks_menu:
            if drink.name == name:
                raise Exception(f"{drink_type} {name} is already in the menu!")
        # if not:
        if drink_type == "Tea":
            new_drink = Tea(name, portion, brand)
        elif drink_type == "Water":
            new_drink = Water(name, portion, brand)

        self.drinks_menu.append(new_drink)
        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type not in ["InsideTable", "OutsideTable"]:
            return
        # check if already exists
        for table in self.tables_repository:
            if table.table_number == table_number:
                raise Exception(f"Table {table_number} is already in the bakery!")

        # and if not
        if table_type == "InsideTable":
            new_table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            new_table = OutsideTable(table_number, capacity)

        self.tables_repository.append(new_table)
        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):  # food_name1: str, food_name2: str …
        found_table = None
        for table in self.tables_repository:
            if table.table_number == table_number:
                found_table = table
                break
        if not found_table:
            return f"Could not find table {table_number}"

        not_in_menu = []
        for arg in args:
            in_menu = False
            for food in self.food_menu:
                if food.name == arg:
                    found_table.order_food(food)
                    in_menu = True
                    break
            if not in_menu:
                not_in_menu.append(arg)

            orders_as_str = f"Table {table_number} ordered:\n"
            for ordered in table.food_orders:
                orders_as_str += str(ordered) + "\n"
            orders_as_str += f"{self.name} does not have in the menu:\n"
            orders_as_str += "\n".join(not_in_menu)
        return orders_as_str

    def order_drink(self, table_number: int, *args):
        found_table = None
        for table in self.tables_repository:
            if table.table_number == table_number:
                found_table = table
                break
        if not found_table:
            return f"Could not find table {table_number}"

        not_in_menu = []
        for arg in args:
            in_menu = False
            for drink in self.drinks_menu:
                if drink.name == arg:
                    found_table.order_drink(drink)
                    in_menu = True
                    break
            if not in_menu:
                not_in_menu.append(arg)

            orders_as_str = f"Table {table_number} ordered:\n"
            for ordered in table.drink_orders:
                orders_as_str += str(ordered) + "\n"
            orders_as_str += f"{self.name} does not have in the menu:\n"
            orders_as_str += "\n".join(not_in_menu)
        return orders_as_str

    def leave_table(self, table_number: int):
        for table in self.tables_repository:
            if table.table_number == table_number:
                total_bill = table.get_bill()
                table.clear()
                self.total_income += total_bill
                return f"Table: {table_number}\nBill: {total_bill:.2f}"

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                result += table.free_table_info() + "\n"
        return result.strip()

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"
