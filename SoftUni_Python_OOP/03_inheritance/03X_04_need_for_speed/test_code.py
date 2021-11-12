from project.car import Car
from project.family_car import FamilyCar
from project.motorcycle import Motorcycle
from project.race_motorcycle import RaceMotorcycle
from project.sport_car import SportCar
from project.vehicle import Vehicle

vehicle = Vehicle(50, 150)
print(Vehicle.DEFAULT_FUEL_CONSUMPTION)
print(vehicle.fuel)
print(vehicle.horse_power)
print(vehicle.fuel_consumption)
vehicle.drive(100)
print(vehicle.fuel)
family_car = FamilyCar(150, 150)
family_car.drive(50)
print(family_car.fuel)
family_car.drive(50)
print(family_car.fuel)
print(family_car.__class__.__bases__[0].__name__)
print()
print("YAMAHA")
yamaha = Motorcycle(11, 22)
print(yamaha.fuel)
print(yamaha.horse_power)
print(yamaha.fuel_consumption)
yamaha.drive(2)
print(yamaha.fuel)
print()

print("FIAT")
fiat = Car(88,25)
print(fiat.fuel)
print(fiat.fuel_consumption)
fiat.drive(8)
print(fiat.fuel)
print()

print("HONDA")
honda_cbr = RaceMotorcycle(222, 55)
print(honda_cbr.fuel)
print(honda_cbr.fuel_consumption)
honda_cbr.drive(11)
print(honda_cbr.fuel)
print()

print("Alfa GT")
alfa = SportCar(90, 150)
print(alfa.fuel)
print(alfa.fuel_consumption)
alfa.drive(4)
print(alfa.fuel)
print()

