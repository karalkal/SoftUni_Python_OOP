from project.hardware.hardware import Hardware

# MOST LIKELY ERROR SOMEWHERE HERE
class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Heavy", capacity * 2, int(memory * .75))

# deep_blue = HeavyHardware("DB", 100, 100)
# print(deep_blue.capacity)
# print(deep_blue.memory)
# print(deep_blue.hardware_type)

