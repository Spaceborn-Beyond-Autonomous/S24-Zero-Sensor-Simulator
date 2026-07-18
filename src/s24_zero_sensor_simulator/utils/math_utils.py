"""
File: math_utils.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Mathematical helper functions used by the Battery Simulator.
"""

from s24_zero_sensor_simulator.utils.constants import *


def clamp(value: float,
          minimum: float,
          maximum: float) -> float:
    """
    Restrict a value within a given range.
    """

    return max(minimum, min(value, maximum))


def soc_to_voltage(soc: float) -> float:
    """
    Convert State of Charge (%) to Voltage.
    Linear approximation.
    """

    soc = clamp(soc, MIN_SOC, MAX_SOC)

    return MIN_VOLTAGE + (
        (soc / 100.0)
        * (INITIAL_VOLTAGE - MIN_VOLTAGE)
    )


def battery_status(soc: float) -> str:
    """
    Return battery status.
    """

    if soc >= 95:
        return FULL

    elif soc >= 60:
        return GOOD

    elif soc >= 30:
        return NORMAL

    elif soc >= 10:
        return LOW

    return CRITICAL


def estimate_eta(
        soc: float,
        discharge_rate: float
):
    """
    Estimate remaining battery time.
    """

    if discharge_rate <= 0:
        return float("inf")

    return soc / discharge_rate


def calculate_current(power, voltage):
    """
    Calculate Current.

    I = P / V
    """

    if voltage <= 0:
        return 0.0

    return power / voltage


def power_consumption(
        voltage,
        current
):
    """
    Calculate Power.

    P = V × I
    """

    return voltage * current