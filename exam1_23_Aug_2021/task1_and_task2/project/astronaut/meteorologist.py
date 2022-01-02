from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name: str):
        super().__init__(name, 90)
        self.breath_volume = 15


# meto = Meteorologist("meto")
# print(meto.oxygen)
# meto.breathe()
# print(meto.oxygen)
# meto.breathe()
# print(meto.oxygen)

