from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Power", int(capacity * .25), int(memory * 1.75))

# deep_blue = PowerHardware("DB", 101, 102)
# print(deep_blue.capacity)
# print(deep_blue.memory)
# print(deep_blue.hardware_type)
#
