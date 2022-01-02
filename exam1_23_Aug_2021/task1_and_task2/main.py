from project.astronaut.meteorologist import Meteorologist
from project.space_station import SpaceStation

station1 = SpaceStation()

print(station1.astronaut_repository.astronauts)
print(station1.add_astronaut("Meteorologist", "METO"))
print(station1.astronaut_repository.astronauts)

print(station1.add_astronaut("Meteorologist", "METO"))
print(station1.astronaut_repository.astronauts)

# print(station1.add_astronaut("Gyz", "gyz"))
print(station1.planet_repository)
print(station1.add_planet("Mars", "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q , r, s, t, u, v, w, x, y, z"))
print(station1.add_planet("Mars", "1, 2"))
print(station1.add_planet("Jupiter", "1, 2, 3, 4, 5, 6, 7, 8, 9, 0"))

print(station1.planet_repository)
for planet in station1.planet_repository.planets:
    print(f"Name: {planet.name}    ==>>    Items{planet.items}")
print()

print(station1.add_astronaut("Meteorologist", "METO1"))
print(station1.add_astronaut("Geodesist", "GEO1"))
print(station1.add_astronaut("Biologist", "BIO1"))
print(station1.add_astronaut("Geodesist", "GEO2"))
print(station1.add_astronaut("Meteorologist", "METO2"))
print(station1.add_astronaut("Meteorologist", "METO2"))
print(station1.add_astronaut("Biologist", "BIO2"))
print(station1.add_astronaut("Biologist", "BIO2"))
print(station1.add_astronaut("Biologist", "BIO3"))
print(station1.add_astronaut("Biologist", "BIO4"))
print()

for astro in station1.astronaut_repository.astronauts:
    print(f"Name: {astro.name}    ==>>    {astro.oxygen}")
print()

print(station1.retire_astronaut("METO"))
for astro in station1.astronaut_repository.astronauts:
    print(f"Name: {astro.name}    ==>>    {astro.oxygen}")
# # already retired - return error
# print(station1.retire_astronaut("METO"))
# for astro in station1.astronaut_repository.astronauts:
#     print(f"Name: {astro.name}    ==>>    {astro.oxygen}")
print()
station1.recharge_oxygen()
for astro in station1.astronaut_repository.astronauts:
    print(f"Name: {astro.name}    ==>>    {astro.oxygen}")
print()
print(station1.send_on_mission("Mars"))
for astro in station1.astronaut_repository.astronauts:
    print(f"Name: {astro.name}    ==>>    {astro.oxygen}    ==>>    {astro.backpack}")
print()

print(station1.add_planet("Saturn", "1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "
                                    "1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "
                                    "1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "
                                    "1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "
                                    "1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "))

print(station1.send_on_mission("Saturn"))
for astro in station1.astronaut_repository.astronauts:
    print(f"Name: {astro.name}    ==>>    {astro.oxygen}    ==>>    {astro.backpack}")
print()
print(station1.report())

