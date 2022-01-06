from abc import ABC, abstractmethod
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([deco.comfort for deco in self.decorations])

    def add_fish(self, fish: BaseFish):
        if fish.__class__.__name__ not in ["FreshwaterFish", "SaltwaterFish"]:
            return

        if self.capacity == len(self.fish):  # if returns True, aquarium is full
            return "Not enough capacity."

        self.fish.append(fish)
        return f"Successfully added {fish.__class__.__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        if not self.fish:
            result += f"Fish: none\n"
        else:
            result += f"Fish: {' '.join([fish.name for fish in self.fish])}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"

        return result
