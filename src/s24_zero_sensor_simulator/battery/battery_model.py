"""
File: battery_model.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Core Battery Simulation Engine.
"""

from s24_zero_sensor_simulator.utils.config_loader import ConfigLoader
from s24_zero_sensor_simulator.utils.math_utils import (
    battery_status,
    estimate_eta,
    power_consumption,
    clamp,
)


class BatteryModel:
    """
    Simulates a rechargeable battery.
    """

    def __init__(self):

        config = ConfigLoader().battery()

        # Battery Information
        self.name = config["name"]
        self.chemistry = config["chemistry"]

        # Capacity
        self.capacity = config["capacity_ah"]

        # State of Charge
        self.soc = config["initial_soc"]

        # Voltage
        self.max_voltage = config["voltage"]["max"]
        self.min_voltage = config["voltage"]["min"]

        # Initial Voltage
        self.voltage = (
            self.min_voltage
            + (self.max_voltage - self.min_voltage)
            * self.soc
            / 100.0
        )

        # Current
        self.idle_current = config["current"]["idle"]
        self.moving_current = config["current"]["moving"]
        self.current = self.idle_current

        # Temperature
        self.temperature = config["temperature"]["initial"]
        self.max_temperature = config["temperature"]["maximum"]

        # Discharge Rates
        self.idle_rate = config["discharge"]["idle_rate"]
        self.moving_rate = config["discharge"]["moving_rate"]

        # Warning Levels
        self.low_warning = config["warning"]["low"]
        self.critical_warning = config["warning"]["critical"]

        # Runtime Variables
        self.power = power_consumption(
            self.voltage,
            self.current
        )

        self.eta = estimate_eta(
            self.soc,
            self.idle_rate
        )

        self.status = battery_status(self.soc)

        self.is_robot_moving = False

    def update(self):
        """
        Update battery simulation.
        """

        if self.is_robot_moving:

            discharge = self.moving_rate
            self.current = self.moving_current

        else:

            discharge = self.idle_rate
            self.current = self.idle_current

        # Update SOC
        self.soc -= discharge
        self.soc = clamp(
            self.soc,
            0.0,
            100.0
        )

        # Update Voltage
        self.voltage = (
            self.min_voltage
            + (self.max_voltage - self.min_voltage)
            * self.soc
            / 100.0
        )

        # Update Power
        self.power = power_consumption(
            self.voltage,
            self.current
        )

        # Update ETA
        self.eta = estimate_eta(
            self.soc,
            discharge
        )

        # Update Status
        self.status = battery_status(
            self.soc
        )

        # Update Temperature
        if self.is_robot_moving:
            self.temperature += 0.05
        else:
            self.temperature += 0.01

        self.temperature = clamp(
            self.temperature,
            0.0,
            self.max_temperature
        )

    def robot_started(self):
        """
        Robot starts moving.
        """

        self.is_robot_moving = True

    def robot_stopped(self):
        """
        Robot stops moving.
        """

        self.is_robot_moving = False

    def shutdown(self):
        """
        Shutdown battery.
        """

        self.current = 0.0
        self.power = 0.0

    def get_state(self):
        """
        Update battery and return latest state.
        """

        self.update()

        return {

            "name": self.name,

            "chemistry": self.chemistry,

            "soc": self.soc,

            "voltage": self.voltage,

            "current": self.current,

            "power": self.power,

            "temperature": self.temperature,

            "eta": self.eta,

            "status": self.status,

        }