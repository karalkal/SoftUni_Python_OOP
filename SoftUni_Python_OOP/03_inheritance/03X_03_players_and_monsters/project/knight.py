from project.hero import Hero


class Knight(Hero):
    def __init__(self, username, level: int):
        super().__init__(username, level)