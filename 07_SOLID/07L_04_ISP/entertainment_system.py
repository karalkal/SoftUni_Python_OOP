class EntertainmentDevice:
    def connect_device_to_power_outlet(self, device):
        return f"connected {device} to power supply"


class HDMIConnectable(EntertainmentDevice):
    def connect_to_device_via_hdmi_cable(self, device):
        return f"connected {self} to {device} via HDMI connection"


class RCIConnectable(EntertainmentDevice):
    def connect_to_device_via_rca_cable(self, device):
        return f"connected {self} to {device} via RCI connection"


class EthernetConnectable(EntertainmentDevice):
    def connect_to_device_via_ethernet_cable(self, device):
        return f"connected {self} to {device} via Ethernet connection"


class Television(RCIConnectable, HDMIConnectable):
    def connect_to_dvd(self, dvd_player):
        return self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        return self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)


class DVDPlayer(HDMIConnectable):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)


class GameConsole(HDMIConnectable, EthernetConnectable):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        return self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)


class Router(EthernetConnectable):
    def connect_to_tv(self, television):
        return self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        return self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        return self.connect_device_to_power_outlet(self)


cisco = Router()
nintendo = GameConsole()
grundig = Television()
sony = DVDPlayer()
print(cisco.plug_in_power())
print(sony.plug_in_power())
print(sony.connect_to_device_via_hdmi_cable(grundig))
print(sony.connect_to_tv(grundig))
print(cisco.connect_to_tv(grundig))
print(cisco.connect_to_device_via_ethernet_cable(grundig))
