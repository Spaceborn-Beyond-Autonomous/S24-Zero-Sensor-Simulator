"""
File: sensor_manager.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Handles registration of all sensor modules.
"""


class SensorManager:

    def __init__(self):

        self.sensors = {}

    def register_sensor(self, name, sensor):

        self.sensors[name] = sensor

    def get_sensor(self, name):

        return self.sensors.get(name)

    def get_all_sensors(self):

        return self.sensors