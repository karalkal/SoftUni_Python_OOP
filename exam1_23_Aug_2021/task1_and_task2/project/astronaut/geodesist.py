from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name: str):
        super().__init__(name, 50)
        self.breath_volume = 10