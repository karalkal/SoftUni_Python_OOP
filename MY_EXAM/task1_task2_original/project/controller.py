from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.race import Race
from project.driver import Driver


class Controller:
    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in ["MuscleCar", "SportsCar"]:
            return
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")

        new_car = None
        if car_type == "MuscleCar":
            new_car = MuscleCar(model, speed_limit)
        elif car_type == "SportsCar":
            new_car = SportsCar(model, speed_limit)

        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        self.drivers.append(Driver(driver_name))
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        self.races.append(Race(race_name))
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        found_driver = None
        for driver in self.drivers:
            if driver.name == driver_name:
                found_driver = driver
        if not found_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        found_car = None
        if car_type == "MuscleCar":
            for car in self.cars:
                if car.__class__.__name__ == "MuscleCar" and not car.is_taken:
                    found_car = car  # it will go all the way to last one

        if car_type == "SportsCar":
            for car in self.cars:
                if car.__class__.__name__ == "SportsCar" and not car.is_taken:
                    found_car = car  # it will go all the way to last one

        if not found_car:
            raise Exception(f"Car {car_type} could not be found!")

        # CAR WILL BE TAKEN EITHER WAY!
        found_car.is_taken = True

        if found_driver.car:  # if guy has a car
            found_driver.car.is_taken = False  # this HASN'T been mentioned explicitly
            old_model = found_driver.car.model
            new_model = found_car.model
            found_driver.car = found_car  # overwrite old car with new one
            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."
        else:  # if he hasn't got a motor
            found_driver.car = found_car  # overwrite None
            return f"Driver {driver_name} chose the car {found_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        found_race = None
        for race in self.races:
            if race.name == race_name:
                found_race = race
                break
        if not found_race:
            raise Exception(f"Race {race_name} could not be found!")

        found_driver = None
        for driver in self.drivers:
            if driver.name == driver_name:
                found_driver = driver
        if not found_driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not found_driver.car:  # guy doesn't have a motor
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if found_driver in found_race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        else:
            found_race.drivers.append(found_driver)
            return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        found_race = None
        for race in self.races:
            if race.name == race_name:
                found_race = race
                break
        if not found_race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(found_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        # otherwise, race starts
        drivers_in_race = found_race.drivers
        sorted_drivers = list(sorted(drivers_in_race, key=lambda driver: driver.car.speed_limit, reverse=True))
        fastest_drivers = sorted_drivers[:3]

        str_to_return = ""
        for winner in fastest_drivers:
            str_to_return += f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.\n"
            winner.number_of_wins += 1
        return str_to_return.strip()
