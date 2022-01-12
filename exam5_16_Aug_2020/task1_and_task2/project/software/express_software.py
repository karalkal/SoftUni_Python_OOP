from project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Express", capacity_consumption, memory_consumption * 2)

# game = ExpressSoftware("game", 100, 150)
# print(game.name)
# print(game.software_type)
# print(game.capacity_consumption)
# print(game.memory_consumption)