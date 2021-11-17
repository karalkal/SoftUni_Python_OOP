from project.hero import Hero


class Elf(Hero):
    def __init__(self, username, level: int):
        super().__init__(username, level)