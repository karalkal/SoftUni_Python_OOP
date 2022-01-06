from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.decoration.ornament import Ornament


class DecorationRepository:
    def __init__(self):
        self.decorations: List[BaseDecoration] = []  # – empty list that will contain all decorations (objects).

    def add(self, decoration: BaseDecoration):
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration.__class__.__name__ == decoration_type:
                return decoration
        return "None"

# stone = Ornament()
# deco_repo = DecorationRepository()
# print(deco_repo.decorations)
# deco_repo.add(stone)
# print(deco_repo.decorations)
# print(deco_repo.remove(stone))
# print(deco_repo.decorations)
# print(deco_repo.remove(stone))
# print()
# deco_repo.add(stone)
# print(deco_repo.find_by_type("Ornament"))
# print(deco_repo.remove(stone))  # remove returns True
# print(deco_repo.find_by_type("Ornament"))
