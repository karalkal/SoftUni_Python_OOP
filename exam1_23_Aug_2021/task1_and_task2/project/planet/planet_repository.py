from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        if planet not in self.planets:
            self.planets.append(planet)

    def remove(self, planet: Planet):
        if planet in self.planets:
            self.planets.remove(planet)

    def find_by_name(self, name: str):
        for pl in self.planets:
            if pl.name == name:
                return pl
        return None
        # return "No such planet found yet, buddy!"

    # def __repr__(self):
    #     result = ""
    #     for planet in self.planets:
    #         result += f"name: {planet.name}, items: {planet.items}\n"
    #     return result

# repo = PlanetRepository()
# mars = Planet("Mars")
# repo.add(mars)
# print(repo)
# # nishto = Planet("")
#
# jupiter = Planet("Jupiter")
# repo.add(jupiter)
# print(repo)
# print(repo.find_by_name("Jupiter"))
# print(repo.find_by_name("Venus"))
# repo.remove(mars)
# print(repo)
