from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    def __init__(self, name: str):
        super().__init__(name, 70)
        self.breath_volume = 5


# bio = Biologist("bio")
# # nikoj1 = Biologist("")
# # print(nikoj1.name)
# # nikoj2 = Biologist(" ")
# # print(nikoj2.name)
# print(bio.name)
# print(f"Oxygen: {bio.oxygen}")
# print(bio.breathe())
# print(bio.breathe())
# print(f"Oxygen: {bio.oxygen}")
# print(bio.increase_oxygen(480))
# print(f"Oxygen: {bio.oxygen}")
