from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist


class AstronautRepository:
    def __init__(self):
        self.astronauts: list = []  # will be list of astronaut objects

    def add(self, astronaut: Astronaut):
        if astronaut not in self.astronauts:
            self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name):
        for astr in self.astronauts:
            if astr.name == name:
                return astr
        return None
            # return "No such guy in existence"

#     def __repr__(self):
#         result = ""
#         for astr in self.astronauts:
#             result += f"name: {astr.name}, oxy: {astr.oxygen}, backpack: {astr.backpack}\n"
#         return result
#
# repo = AstronautRepository()
#
# bio = Biologist("bio")
# repo.add(bio)
# print(repo)
# geo = Geodesist("geo")
# repo.add(geo)
# print(repo)
# meto = Meteorologist("meto")
#
# repo.remove(bio)
# print(repo)
#
# not_found = repo.find_by_name("goshko")
# print(not_found)
#
# found = repo.find_by_name("geo")
# print(found, found.name, found.oxygen)
