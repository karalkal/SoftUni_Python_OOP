from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
        elif aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
        else:
            return "Invalid aquarium type."
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
        elif decoration_type == "Plant":
            self.decorations_repository.add(Plant())
        else:
            return "Invalid decoration type."
        return f"Successfully added {decoration_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
            return f"Successfully added {decoration_type}."
        if decoration_type == "Plant":
            self.decorations_repository.add(Plant())
            return f"Successfully added {decoration_type}."

    def find_aquarium_by_name(self, name):
        for aquarium in self.aquariums:
            if aquarium.name == name:
                return aquarium


    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        try:
            decoration = \
                [d for d in self.decorations_repository.decorations if d.__class__.__name__ == decoration_type][0]
        except IndexError:
            return f"There isn't a decoration of type {decoration_type}."

        try:
            aquarium = \
                [a for a in self.aquariums if a.name == aquarium_name][0]
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."
        except IndexError:
            return

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == "SaltwaterFish":
            fish_to_put_in = SaltwaterFish(fish_name, fish_species, price)
        elif fish_type == "FreshwaterFish":
            fish_to_put_in = FreshwaterFish(fish_name, fish_species, price)
        else:
            return f"There isn't a fish of type {fish_type}."

        found_aquarium = self.find_aquarium_by_name(aquarium_name)
        if found_aquarium.__class__.__name__ == "FreshwaterAquarium" and fish_type == "FreshwaterFish":
            return found_aquarium.add_fish(fish_to_put_in)
        elif found_aquarium.__class__.__name__ == "SaltwaterAquarium" and fish_type == "SaltwaterFish":
            return found_aquarium.add_fish(fish_to_put_in)
        else:
            return "Water not suitable."

    def feed_fish(self, aquarium_name: str):
        aquarium = \
            [a for a in self.aquariums if a.name == aquarium_name][0]
        aquarium.feed()
        fed_count = len(aquarium.fish)
        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        value = 0
        found_aquarium = self.find_aquarium_by_name(aquarium_name)

        for deco in found_aquarium.decorations:
            value += deco.price
        for fish in found_aquarium.fish:
            value += fish.price
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ""
        for aqua in self.aquariums:
            result += "\n" + str(aqua)
        return result
