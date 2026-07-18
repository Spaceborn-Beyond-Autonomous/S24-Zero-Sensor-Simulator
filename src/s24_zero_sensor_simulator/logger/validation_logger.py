"""
File: validation_logger.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Validation Logger for Battery Simulator.
"""

import logging
import os

from s24_zero_sensor_simulator.utils.time_utils import timestamp
from s24_zero_sensor_simulator.utils.constants import LOG_FOLDER, LOG_FILE


class ValidationLogger:

    def __init__(self):

        os.makedirs(LOG_FOLDER, exist_ok=True)

        log_path = os.path.join(
            LOG_FOLDER,
            LOG_FILE
        )

        self.logger = logging.getLogger("BatteryLogger")

        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            file_handler = logging.FileHandler(log_path)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

        self.log_startup()

    def log_startup(self):

        self.logger.info(
            "Battery Simulator Started"
        )

    def log_battery(self, state):

        self.logger.info(

            f"SOC={state['soc']:.2f}% | "

            f"Voltage={state['voltage']:.2f}V | "

            f"Current={state['current']:.2f}A | "

            f"Power={state['power']:.2f}W | "

            f"Temp={state['temperature']:.2f}C | "

            f"ETA={state['eta']:.2f}s | "

            f"Status={state['status']}"

        )

        if state["soc"] <= 20:

            self.logger.warning(

                f"Low Battery ({state['soc']:.2f}%)"

            )

        if state["soc"] <= 5:

            self.logger.critical(

                f"Critical Battery ({state['soc']:.2f}%)"

            )

    def log_shutdown(self):

        self.logger.info(
            "Battery Simulator Stopped"
        )