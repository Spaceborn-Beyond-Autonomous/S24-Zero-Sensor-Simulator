"""
File: validation_logger.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Central logger for the S24 Zero Sensor Simulator.
"""

import logging
import os

from s24_zero_sensor_simulator.utils.constants import (
    LOG_FOLDER,
    LOG_FILE,
)


class ValidationLogger:

    def __init__(self):

        os.makedirs(LOG_FOLDER, exist_ok=True)

        log_path = os.path.join(
            LOG_FOLDER,
            LOG_FILE
        )

        self.logger = logging.getLogger(
            "S24ZeroSensorSimulator"
        )

        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            file_handler = logging.FileHandler(log_path)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(message)s"
            )

            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)

        self.log_startup()

    # -------------------------------------------------
    # Simulator
    # -------------------------------------------------

    def log_startup(self):

        self.logger.info("")
        self.logger.info("=" * 60)
        self.logger.info("Simulator Started")
        self.logger.info("=" * 60)

    def log_shutdown(self):

        self.logger.info("=" * 60)
        self.logger.info("Simulator Stopped")
        self.logger.info("=" * 60)

    # -------------------------------------------------
    # Validation
    # -------------------------------------------------

    def log_validation(self, result):

        status = "PASS" if result["status"] else "FAIL"

        self.logger.info(
            f"{result['sensor']} : {status}"
        )

    # -------------------------------------------------
    # Complete Sensor Logging
    # -------------------------------------------------

    def log_sensor_data(
        self,
        battery,
        camera,
        lidar,
        imu,
        gps
    ):

        self.logger.info("")

        self.logger.info("Battery")
        self.logger.info(
            f"SOC={battery['soc']:.2f}% "
            f"Voltage={battery['voltage']:.2f}V "
            f"Current={battery['current']:.2f}A "
            f"Power={battery['power']:.2f}W "
            f"Temperature={battery['temperature']:.2f}C "
            f"Status={battery['status']}"
        )

        self.logger.info("Camera")
        self.logger.info(
            f"Frame={camera.frame_number} "
            f"Resolution={camera.width}x{camera.height} "
            f"Timestamp={camera.timestamp}"
        )

        self.logger.info("LiDAR")
        self.logger.info(
            f"Frame={lidar.frame_number} "
            f"Points={len(lidar.points)} "
            f"Timestamp={lidar.timestamp}"
        )

        self.logger.info("IMU")
        self.logger.info(
            f"Accel=({imu.accel_x:.3f}, "
            f"{imu.accel_y:.3f}, "
            f"{imu.accel_z:.3f}) "
            f"Gyro=({imu.gyro_x:.3f}, "
            f"{imu.gyro_y:.3f}, "
            f"{imu.gyro_z:.3f})"
        )

        self.logger.info("GPS")
        self.logger.info(
            f"Latitude={gps.latitude} "
            f"Longitude={gps.longitude} "
            f"Altitude={gps.altitude}"
        )

        self.logger.info("-" * 60)

    # -------------------------------------------------
    # General
    # -------------------------------------------------

    def log_message(self, message):

        self.logger.info(message)

    def log_warning(self, message):

        self.logger.warning(message)

    def log_error(self, message):

        self.logger.error(message)