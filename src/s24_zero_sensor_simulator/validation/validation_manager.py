"""
File: validation_manager.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Runs validation for all registered sensors.
"""

from s24_zero_sensor_simulator.validation.battery_validation import BatteryValidation
from s24_zero_sensor_simulator.validation.camera_validation import CameraValidation
from s24_zero_sensor_simulator.validation.lidar_validation import LidarValidation
from s24_zero_sensor_simulator.validation.imu_validation import IMUValidation
from s24_zero_sensor_simulator.validation.gps_validation import GPSValidation


class ValidationManager:

    def __init__(self):

        self.validators = {

            "Battery": BatteryValidation(),

            "Camera": CameraValidation(),

            "LiDAR": LidarValidation(),

            "IMU": IMUValidation(),

            "GPS": GPSValidation()

        }

    def validate(self, sensor_name, data):

        validator = self.validators.get(sensor_name)

        if validator is None:

            return None

        return validator.validate(data)

    def validate_all(self, sensor_data):

        results = {}

        for name, data in sensor_data.items():

            results[name] = self.validate(name, data)

        return results