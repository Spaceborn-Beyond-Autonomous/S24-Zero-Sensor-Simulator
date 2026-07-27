"""
File: hal_wrapper.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Hardware Abstraction Layer for accessing simulator modules.
"""


class HALWrapper:

    def __init__(self):

        self.devices = {}

    def register_device(self, name, device):

        self.devices[name] = device

    def get_device(self, name):

        return self.devices.get(name)

    def device_exists(self, name):

        return name in self.devices

    def get_all_devices(self):

        return self.devices

    def clear(self):

        self.devices.clear()