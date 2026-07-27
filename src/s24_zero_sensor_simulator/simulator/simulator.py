"""
File: simulator.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Central simulator that integrates all sensor modules.
"""

from s24_zero_sensor_simulator.framework.sensor_manager import SensorManager
from s24_zero_sensor_simulator.framework.simulator_manager import SimulatorManager
from s24_zero_sensor_simulator.framework.hal_wrapper import HALWrapper
from s24_zero_sensor_simulator.framework.master_toggle import MasterToggle

from s24_zero_sensor_simulator.validation.validation_manager import ValidationManager
from s24_zero_sensor_simulator.logger.validation_logger import ValidationLogger

from s24_zero_sensor_simulator.display.display import Display

from s24_zero_sensor_simulator.battery.battery_model import BatteryModel
from s24_zero_sensor_simulator.camera.dummy_camera import DummyCamera
from s24_zero_sensor_simulator.lidar.dummy_lidar import DummyLiDAR
from s24_zero_sensor_simulator.imu.imu_sensor import DummyIMU
from s24_zero_sensor_simulator.gps.dummy_gps import DummyGPS


class Simulator:

    def __init__(self):

        self.sensor_manager = SensorManager()

        self.simulator_manager = SimulatorManager()

        self.hal = HALWrapper()

        self.toggle = MasterToggle()

        self.validation_manager = ValidationManager()

        self.logger = ValidationLogger()

        self.display = Display()

        self.initialize()

    def initialize(self):

        # ---------------------------------------
        # Create Sensors
        # ---------------------------------------

        self.battery = BatteryModel()

        self.camera = DummyCamera()

        self.lidar = DummyLiDAR()

        self.imu = DummyIMU()

        self.gps = DummyGPS()

        # ---------------------------------------
        # Register Sensors
        # ---------------------------------------

        self.sensor_manager.register_sensor(
            "Battery",
            self.battery
        )

        self.sensor_manager.register_sensor(
            "Camera",
            self.camera
        )

        self.sensor_manager.register_sensor(
            "LiDAR",
            self.lidar
        )

        self.sensor_manager.register_sensor(
            "IMU",
            self.imu
        )

        self.sensor_manager.register_sensor(
            "GPS",
            self.gps
        )

        # ---------------------------------------
        # Register HAL Devices
        # ---------------------------------------

        for name, sensor in self.sensor_manager.get_all_sensors().items():

            self.hal.register_device(
                name,
                sensor
            )

            self.toggle.enable(name)

        # ---------------------------------------
        # Register Simulator Modules
        # ---------------------------------------

        self.simulator_manager.register_module(self.battery)
        self.simulator_manager.register_module(self.camera)
        self.simulator_manager.register_module(self.lidar)
        self.simulator_manager.register_module(self.imu)
        self.simulator_manager.register_module(self.gps)

    def start(self):

        print("\n========== Simulator ==========")

        print("Initializing Sensors...\n")

        self.logger.log_startup()

        self.simulator_manager.start()

        print("\nSimulator Started")

    def stop(self):

        self.logger.log_shutdown()

        self.simulator_manager.stop()

        print("\nSimulator Stopped")

    def status(self):

        print("\n----------- STATUS -----------")

        for name in self.toggle.get_status():

            state = self.toggle.is_enabled(name)

            print(
                f"{name:10} : "
                f"{'Enabled' if state else 'Disabled'}"
            )

        print("------------------------------")

    def validate(self):

        # ---------------------------------------
        # Read Sensor Data
        # ---------------------------------------

        sensor_data = {

            "Battery": self.battery.get_state(),

            "Camera": self.camera.capture_frame(),

            "LiDAR": self.lidar.get_point_cloud(),

            "IMU": self.imu.get_data(),

            "GPS": self.gps.get_data()

        }

        # ---------------------------------------
        # Validate Sensors
        # ---------------------------------------

        results = self.validation_manager.validate_all(
            sensor_data
        )

        # ---------------------------------------
        # Log Validation Results
        # ---------------------------------------

        for sensor, result in results.items():

            if result is None:

                continue

            self.logger.log_validation(result)

        # ---------------------------------------
        # Log Complete Sensor Data
        # ---------------------------------------

        self.logger.log_sensor_data(

            battery=sensor_data["Battery"],

            camera=sensor_data["Camera"],

            lidar=sensor_data["LiDAR"],

            imu=sensor_data["IMU"],

            gps=sensor_data["GPS"]

        )

        # ---------------------------------------
        # Display Dashboard
        # ---------------------------------------

        self.display.show(

            battery=sensor_data["Battery"],

            camera=sensor_data["Camera"],

            lidar=sensor_data["LiDAR"],

            imu=sensor_data["IMU"],

            gps=sensor_data["GPS"],

            validation=results

        )