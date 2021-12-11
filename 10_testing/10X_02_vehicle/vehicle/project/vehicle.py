from typing import ClassVar


class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: ClassVar[float] = 1.25
    fuel_consumption: float
    fuel: float
    capacity: float
    horse_power: float

    def __init__(self, fuel: float, horse_power: float):
        self.fuel = fuel
        self.capacity = self.fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        fuel_needed = self.fuel_consumption * kilometers
        if self.fuel < fuel_needed:
            raise Exception("Not enough fuel")
        self.fuel -= fuel_needed

    def refuel(self, fuel):
        if self.fuel + fuel > self.capacity:
            raise Exception("Too much fuel")
        self.fuel += fuel

    def __str__(self):
        return f"The vehicle has {self.horse_power} " \
               f"horse power with {self.fuel} fuel left and {self.fuel_consumption} fuel consumption"


alfa = Vehicle(1, 1)
print(alfa.DEFAULT_FUEL_CONSUMPTION == 1.20)
print(alfa.DEFAULT_FUEL_CONSUMPTION == 1.25)

alfa.DEFAULT_FUEL_CONSUMPTION = 8888
print(alfa.fuel_consumption)
print(alfa.DEFAULT_FUEL_CONSUMPTION)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)

#
# my_car = Vehicle(70, 190)
# my_car.capacity = 80
# my_car.refuel(11)
