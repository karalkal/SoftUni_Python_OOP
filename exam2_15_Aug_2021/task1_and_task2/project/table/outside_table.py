from project.table.table import Table


class OutsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False
        self.table_type = self.__class__.__name__

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < 51 or value > 100:
            raise ValueError("Outside table's number must be between 51 and 100 inclusive!")
        else:
            self.__table_number = value
            return self.__table_number
