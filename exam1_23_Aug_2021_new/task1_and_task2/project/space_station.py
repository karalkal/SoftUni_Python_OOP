from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.failed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        # first check if guy is already in repo
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return f"{name} is already added."

        # then check if type is valid and create object
        if astronaut_type == "Biologist":
            new_astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            new_astronaut = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            new_astronaut = Meteorologist(name)
        else:
            raise Exception("Astronaut type is not valid!")

        # if all is alright, append
        self.astronaut_repository.add(new_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    # different approach compared to above, using methods defined in classes
    def add_planet(self, name: str, items: str):
        # use method from PlanetRepo class, if it returns value - name is already in repo
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        items_on_planet = list(items.split(", "))
        new_planet = Planet(name)
        new_planet.items = items_on_planet
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        # use method from AstronautRepo class, if it returns value - name is already in repo
        retiring_astronaut = self.astronaut_repository.find_by_name(name)
        # if not found
        if not retiring_astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")
        # else, i.e. if found
        self.astronaut_repository.remove(retiring_astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        found_planet = self.planet_repository.find_by_name(planet_name)
        if not found_planet:
            raise Exception("Invalid planet name!")

        fit_astronauts = [astro for astro in self.astronaut_repository.astronauts if astro.oxygen > 30]
        if not fit_astronauts:
            raise Exception("You need at least one astronaut to explore the planet!")

        sorted_astronauts = sorted(fit_astronauts, key=lambda x: x.oxygen, reverse=True)
        # print(sorted_astronauts)
        if len(sorted_astronauts) > 5:
            sorted_astronauts = sorted_astronauts[0:5]
        # return f"NUMBER - {len(sorted_astronauts)}"

        num_of_astronauts_exploring = 0
        for astronaut in sorted_astronauts:
            num_of_astronauts_exploring += 1

            while astronaut.oxygen > 0 and found_planet.items:
                item = found_planet.items.pop()
                astronaut.backpack.append(item)
                astronaut.breathe()
            if not found_planet.items:
                self.successful_missions += 1
                return f"Planet: {planet_name} was explored. " \
                       f"{num_of_astronauts_exploring} astronauts participated in collecting items."
        # else:
        self.failed_missions += 1
        return "Mission is not completed."

    def report(self):
        result_for_print = f"{self.successful_missions} successful missions!\n" \
                           f"{self.failed_missions} missions were not completed!\n" \
                           f"Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            backpack_items = ', '.join(astronaut.backpack)
            if not backpack_items:
                backpack_items = "none"
            result_for_print += f"Name: {astronaut.name}\n" \
                                f"Oxygen: {astronaut.oxygen}\n" \
                                f"Backpack items: {backpack_items}\n"

        return result_for_print.strip()
