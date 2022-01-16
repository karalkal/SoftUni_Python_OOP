from typing import List

from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.software.software import Software


def find_hardware(hardware_list, hardware_name):
    for hw in hardware_list:
        if hw.name == hardware_name:
            return hw
    return None


def find_software(software_list, software_name):
    for sw in software_list:
        if sw.name == software_name:
            return sw
    return None


class System:
    _hardware: List[Hardware] = []
    _software: List[Software] = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        new_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        new_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(new_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        found_hw = find_hardware(System._hardware, hardware_name)
        if not found_hw:
            return "Hardware does not exist"

        new_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        found_hw.install(new_software)
        System._software.append(new_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        found_hw = find_hardware(System._hardware, hardware_name)
        if not found_hw:
            return "Hardware does not exist"

        new_software = LightSoftware(name, capacity_consumption, memory_consumption)
        found_hw.install(new_software)
        System._software.append(new_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware_found = find_hardware(System._hardware, hardware_name)
        software_found = find_software(System._software, software_name)

        if not hardware_found or not software_found:
            return "Some of the components do not exist"

        hardware_found.uninstall(software_found)
        System._software.remove(software_found)

    @staticmethod
    def analyze():
        str_to_return = f"System Analysis\nHardware Components: {len(System._hardware)}\nSoftware Components: {len(System._software)}\n"
        memory_used = sum(sw.memory_consumption for sw in System._software)
        capacity_used = sum(sw.capacity_consumption for sw in System._software)
        total_memory = sum([hw.memory for hw in System._hardware])
        total_capacity = sum([hw.capacity for hw in System._hardware])

        str_to_return += f"Total Operational Memory: {memory_used} / {total_memory}\n"
        str_to_return += f"Total Capacity Taken: {capacity_used} / {total_capacity}"
        return str_to_return

    @staticmethod
    def system_split():
        str_to_return = ""
        for hardware in System._hardware:
            str_to_return += f"Hardware Component - {hardware.name}\n"
            str_to_return += f"Express Software Components: " \
                             f"{len([sw for sw in hardware.software_components if sw.software_type == 'Express'])}\n"
            str_to_return += f"Light Software Components: " \
                             f"{len([sw for sw in hardware.software_components if sw.software_type == 'Light'])}\n"
            str_to_return += f"Memory Usage: {hardware.memory - hardware.remaining_memory} / {hardware.memory}\n"
            str_to_return += f"Capacity Usage: {hardware.capacity - hardware.remaining_capacity} / {hardware.capacity}\n"
            str_to_return += f"Type: {hardware.hardware_type}\n"
            software_components_names = [sw.name for sw in hardware.software_components]

            str_to_return += f"Software Components: " \
                             f"{', '.join(software_components_names) if software_components_names else 'None'}\n"

        return str_to_return.strip()
