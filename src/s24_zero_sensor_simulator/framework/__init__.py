"""
Framework Package

S24 Zero Sensor Simulator

This package contains the core framework responsible for
managing simulator modules and providing the Hardware
Abstraction Layer (HAL).
"""

from s24_zero_sensor_simulator.framework.simulator_manager import SimulatorManager
from s24_zero_sensor_simulator.framework.sensor_manager import SensorManager
from s24_zero_sensor_simulator.framework.master_toggle import MasterToggle
from s24_zero_sensor_simulator.framework.hal_wrapper import HALWrapper

__all__ = [
    "SimulatorManager",
    "SensorManager",
    "MasterToggle",
    "HALWrapper",
]