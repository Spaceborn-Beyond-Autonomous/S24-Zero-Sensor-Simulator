"""
File: config_loader.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Loads configuration from YAML files.
"""

import os
import yaml

from ament_index_python.packages import get_package_share_directory


class ConfigLoader:

    def __init__(self):

        package_share = get_package_share_directory(
            "s24_zero_sensor_simulator"
        )

        config_path = os.path.join(
            package_share,
            "config",
            "battery.yaml"
        )

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get(self):
        return self.config

    def battery(self):
        return self.config["battery"]

    def logging(self):
        return self.config["logging"]

    def display(self):
        return self.config["display"]

    def ros(self):
        return self.config["ros"]