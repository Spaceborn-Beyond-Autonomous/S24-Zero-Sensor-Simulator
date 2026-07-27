"""
File: sensor_manager.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Handles registration and management of all sensor modules.
"""


class SensorManager:

    def __init__(self):

        self.sensors = {}

    def register_sensor(self, name, sensor):

        self.sensors[name] = sensor

    def unregister_sensor(self, name):

        if name in self.sensors:

            del self.sensors[name]

    def get_sensor(self, name):

        return self.sensors.get(name)

    def get_all_sensors(self):

        return self.sensors

    def sensor_exists(self, name):

        return name in self.sensors

    def total_sensors(self):

        return len(self.sensors)

    def clear(self):

        self.sensors.clear()