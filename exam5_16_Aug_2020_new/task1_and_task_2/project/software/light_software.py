from project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, "Light", int(capacity_consumption * 1.5), int(memory_consumption / 2))

# ls = LightSoftware("ls", 22, 33)
# print(ls.software_type)
# print(ls.capacity_consumption)
# print(ls.memory_consumption)
