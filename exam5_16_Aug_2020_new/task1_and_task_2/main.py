from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.system import System


lightSW = LightSoftware("ubuntu", 100, 300)
expressSW = ExpressSoftware("mint", 440, 500)
powerHW = PowerHardware("POWER", 8000, 7000)
heavyHW = HeavyHardware("HEAVY", 8000, 7000)

print(lightSW.capacity_consumption, lightSW.memory_consumption)
print(expressSW.capacity_consumption, expressSW.memory_consumption)
print(powerHW.capacity, powerHW.memory)
print(heavyHW.capacity, heavyHW.memory)
print()

print(powerHW.remaining_capacity, powerHW.remaining_memory)
powerHW.install(lightSW)
print(powerHW.remaining_capacity, powerHW.remaining_memory)
powerHW.install(expressSW)
print(powerHW.remaining_capacity, powerHW.remaining_memory)
print(powerHW.software_components)
print()

# huge_SW = ExpressSoftware("HUGE", 444444, 8888888)
# powerHW.install(huge_SW)
# print(powerHW.software_components)

