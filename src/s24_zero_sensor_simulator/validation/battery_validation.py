"""
File: battery_validator.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Battery validation.
"""

from .validation import Validation


class BatteryValidation(Validation):

    def __init__(self):

        super().__init__("Battery")

    def validate(self, battery):

        errors = []

        if battery["soc"] < 0 or battery["soc"] > 100:
            errors.append("Invalid State of Charge")

        if battery["voltage"] <= 0:
            errors.append("Invalid Voltage")

        if battery["current"] < 0:
            errors.append("Invalid Current")

        if battery["temperature"] < 0:
            errors.append("Invalid Temperature")

        return {

            "sensor": self.name,

            "status": len(errors) == 0,

            "errors": errors

        }