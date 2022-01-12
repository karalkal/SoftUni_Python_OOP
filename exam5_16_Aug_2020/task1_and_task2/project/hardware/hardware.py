from project.software.software import Software


class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []  # an empty list that will contain all software's components installed

    def install(self, software: Software):
        if software.capacity_consumption <= self.capacity \
                and software.memory_consumption <= self.memory:
            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        # if software in self.software_components:
        self.software_components.remove(software)

# comp = Hardware("comp", "PC", 100, 100)
# win = Software("Windows", "OS", 100, 100)
# print(comp.software_components)
# comp.install(win)
# print(comp.software_components)
#
# comp1 = Hardware("comp", "PC", 100, 100)
# win = Software("Windows", "OS", 101, 100)
# print(comp.software_components)
# comp1.install(win)
# print(comp1.software_components)
#
# comp1 = Hardware("comp", "PC", 100, 100)
# win = Software("Windows", "OS", 100, 101)
# print(comp.software_components)
# comp1.install(win)
# print(comp1.software_components)
