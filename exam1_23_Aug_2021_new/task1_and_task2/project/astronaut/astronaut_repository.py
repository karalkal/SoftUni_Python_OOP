from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist


class AstronautRepository:
    def __init__(self):
        self.astronauts = []  # an empty list of astronauts

    def add(self, astronaut: Astronaut):
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
        return

#
# ivan = Biologist("ivan")
# print(ivan)
# repo = AstronautRepository()
# repo.add(ivan)
# print(repo.astronauts)
# print(repo.find_by_name("gyz"))
# print(repo.find_by_name("ivan"))

