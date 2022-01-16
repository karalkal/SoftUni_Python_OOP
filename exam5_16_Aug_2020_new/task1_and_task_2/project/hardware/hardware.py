from project.software.software import Software
from typing import List

class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory

        self.software_components: List[Software] = []

        self.remaining_memory = self.memory
        self.remaining_capacity = self.capacity

    def install(self, software: Software):
        if software.memory_consumption <= self.remaining_memory and \
                software.capacity_consumption <= self.remaining_capacity:
            self.software_components.append(software)
            self.remaining_memory -= software.memory_consumption
            self.remaining_capacity -= software.capacity_consumption
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
            self.remaining_memory += software.memory_consumption
            self.remaining_capacity += software.capacity_consumption





