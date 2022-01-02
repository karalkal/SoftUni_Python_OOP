from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.astronaut_repository = AstronautRepository()
        self.planet_repository = PlanetRepository()
        self.successful_missions, self.failed_missions = 0, 0

    def add_astronaut(self, astronaut_type: str, name: str):
        astronaut_to_add = None
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        # check if already in repo
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == name:
                return f"{name} is already added."

        # if none of the above, append to repo
        if astronaut_type == "Biologist":
            astronaut_to_add = Biologist(name)
        elif astronaut_type == "Geodesist":
            astronaut_to_add = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            astronaut_to_add = Meteorologist(name)

        self.astronaut_repository.add(astronaut_to_add)
        return f"Successfully added {astronaut_type}: {name}."

    def retire_astronaut(self, name):
        guy_to_retire = self.astronaut_repository.find_by_name(name)
        if guy_to_retire is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(guy_to_retire)
        return f"Astronaut {name} was retired!"

    def add_planet(self, name: str, items: str):
        found_planet = self.planet_repository.find_by_name(name)
        if found_planet:
            return f"{name} is already added."

        planet_to_add = Planet(name)
        planet_to_add.items = items.split(", ")
        self.planet_repository.add(planet_to_add)
        print(planet_to_add.items)
        return f"Successfully added Planet: {name}."

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10
        return

    def send_on_mission(self, planet_name: str):
        searched_planet = self.planet_repository.find_by_name(planet_name)
        if not searched_planet:
            raise Exception("Invalid planet name!")

        with_enough_oxygen = [ast for ast in self.astronaut_repository.astronauts if ast.oxygen > 30]
        if not with_enough_oxygen:
            raise Exception("You need at least one astronaut to explore the planet!")

        sorted_astronauts = list(sorted(with_enough_oxygen, key=lambda x: x.oxygen, reverse=True))

        if len(sorted_astronauts) > 5:
            astronauts_in_mission = sorted_astronauts[0:5]
        else:
            astronauts_in_mission = sorted_astronauts

        for astr_no in range(5):
            currently_exploring = astronauts_in_mission[astr_no]

            while currently_exploring.oxygen > 0:
                item_in_backpack = searched_planet.items.pop()
                currently_exploring.backpack.append(item_in_backpack)
                currently_exploring.breathe()
                if not searched_planet.items:
                    self.successful_missions += 1
                    return f"Planet: {searched_planet.name} was explored. " \
                           f"{astr_no + 1} astronauts participated in collecting items."
        # if no guys left but no return from above
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
        return result_for_print

#
# new_station = SpaceStation()
# print(new_station.add_astronaut("Biologist", "BIO"))
# print(new_station.add_astronaut("Geodesist", "GEO"))
# print(new_station.add_astronaut("Meteorologist", "METO"))
# print(new_station.add_astronaut("Meteorologist", "METO"))
# print(new_station.add_astronaut("Biologist", "meto"))
# print()
# # print(new_station.add_astronaut("Gyz", ""))
# # print(new_station.add_astronaut("Biologist", ""))
# print(new_station.retire_astronaut("meto"))
# # print(new_station.retire_astronaut("kur"))
# print(new_station.add_astronaut("Biologist", "BIO2"))
# print(new_station.add_astronaut("Meteorologist", "METO2"))
# print()
# print(new_station.add_planet("Saturn", "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"))
# # test_recharge_oxygen
# new_station.recharge_oxygen()
# # test_send_on_mission
# # print(new_station.send_on_mission("Na majnata si"))
# print(new_station.send_on_mission("Saturn"))
# print(new_station.report())
