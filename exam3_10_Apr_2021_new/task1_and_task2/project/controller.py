from typing import List

from project.aquarium.base_aquarium import BaseAquarium
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
        self.aquariums: List[BaseAquarium] = []

    def add_aquarium(self, aquarium_type, aquarium_name: str):
        if aquarium_type not in ["FreshwaterAquarium", "SaltwaterAquarium"]:
            return "Invalid aquarium type."
        if aquarium_type == "FreshwaterAquarium":
            self.aquariums.append(FreshwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."
        if aquarium_type == "SaltwaterAquarium":
            self.aquariums.append(SaltwaterAquarium(aquarium_name))
            return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in ["Ornament", "Plant"]:
            return "Invalid decoration type."
        if decoration_type == "Ornament":
            self.decorations_repository.add(Ornament())
            return f"Successfully added {decoration_type}."
        if decoration_type == "Plant":
            self.decorations_repository.add(Plant())
            return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type: str):
        found_aq = None
        for aq in self.aquariums:
            if aq.name == aquarium_name:
                found_aq = aq
                break
        if not found_aq:
            return

        found_deco = self.decorations_repository.find_by_type(decoration_type)
        if found_deco == "None":
            return f"There isn't a decoration of type {decoration_type}."
        else:
            self.decorations_repository.remove(found_deco)
            found_aq.add_decoration(found_deco)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."

        found_aq = None
        for aq in self.aquariums:
            if aq.name == aquarium_name:
                found_aq = aq
        if not found_aq:
            return

        fish_number = len(found_aq.fish)
        aq_type = found_aq.__class__.__name__
        if fish_number == found_aq.capacity:
            return "Not enough capacity."

        if (aq_type == "FreshwaterAquarium" and fish_type == "SaltwaterFish") \
                or (aq_type == "SaltwaterAquarium" and fish_type == "FreshwaterFish"):
            return "Water not suitable."

        # adding if all is good
        if fish_type == "SaltwaterFish":
            found_aq.add_fish(SaltwaterFish(fish_name, fish_species, price))
            return f"Successfully added {fish_type} to {aquarium_name}."
        if fish_type == "FreshwaterFish":
            found_aq.add_fish(FreshwaterFish(fish_name, fish_species, price))
            return f"Successfully added {fish_type} to {aquarium_name}."

    def feed_fish(self, aquarium_name: str):
        fed_count = 0
        for aquarium in self.aquariums:
            aquarium.feed()
            fed_count += len(aquarium.fish)
        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        value = 0
        found_aq = None
        for aq in self.aquariums:
            if aq.name == aquarium_name:
                found_aq = aq
        value += sum(f.price for f in found_aq.fish)
        value += sum(d.price for d in found_aq.decorations)
        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        result = ""
        for aq in self.aquariums:
            result += str(aq) + "\n"
        return result.strip()
