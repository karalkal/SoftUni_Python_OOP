from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    def __init__(self):
        self._hardware = System._hardware
        self._software = System._software

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        power_hw = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hw)

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        heavy_hw = HeavyHardware(name, capacity, memory)
        System._hardware.append(heavy_hw)

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        for hw in System._hardware:
            if hw.name == hardware_name:
                express_sw = ExpressSoftware(name, capacity_consumption, memory_consumption)
                hw.install(express_sw)
                # if it cannot find it will raise the error and stop
                # otherwise:
                System._software.append(express_sw)
                return
        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        for hw in System._hardware:
            if hw.name == hardware_name:
                light_sw = LightSoftware(name, capacity_consumption, memory_consumption)
                hw.install(light_sw)
                # if it cannot find it will raise the error and stop
                # otherwise:
                System._software.append(light_sw)
                return
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        hardware_found, software_found = None, None
        for hw in System._hardware:
            if hw.name == hardware_name:
                hardware_found = hw
        for sw in System._software:
            if sw.name == software_name:
                software_found = sw
        if hardware_found and software_found:
            hardware_found.uninstall(software_found)
            System._software.remove(software_found)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = f'System Analysis\nHardware Components: {len(System._hardware)}\nSoftware Components: {len(System._software)}\n'

        software_mem_consumption = 0
        for software in System._software:
            software_mem_consumption += software.memory_consumption
        hardware_memory = 0
        for hardware in System._hardware:
            hardware_memory += hardware.memory

        software_capacity_consumption = 0
        for software in System._software:
            software_capacity_consumption += software.capacity_consumption
        hardware_capacity = 0
        for hardware in System._hardware:
            hardware_capacity += hardware.capacity

        result += f"Total Operational Memory: {software_mem_consumption} / {hardware_memory}\n"
        result += f"Total Capacity Taken: {software_capacity_consumption} / {hardware_capacity}"

        return result

    @staticmethod
    def system_split():
        result = ""
        for hardware in System._hardware:
            result += f"Hardware Component - {hardware.name}\n"
            mem_usage, cap_usage, count_express, count_light, software_list = 0, 0, 0, 0, []
            for software in hardware.software_components:
                software_list.append(software.name)
                cap_usage += software.capacity_consumption
                mem_usage += software.memory_consumption
                if software.__class__.__name__ == "ExpressSoftware":
                    count_express += 1
                if software.__class__.__name__ == "LightSoftware":
                    count_light += 1
            result += f"Express Software Components: {count_express}\n"
            result += f"Light Software Components: {count_light}\n"

            # complete upto here

            result += f"Memory Usage: {mem_usage} / {hardware.memory}\n"
            result += f"Capacity Usage: {cap_usage} / {hardware.capacity}\n"
            result += f"Type: {hardware.hardware_type}\n"
            if not software_list:
                software_components = "None"
            else:
                software_components = ', '.join(software_list)
            result += f"Software Components: {software_components}\n"

        return result
