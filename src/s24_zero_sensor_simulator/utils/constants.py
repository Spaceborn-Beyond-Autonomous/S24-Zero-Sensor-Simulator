"""
File: constants.py
Author: Chetanya Barodiya
Project: S24 Zero Sensor Simulator
Description:
Common constants used by the Battery Simulator.
"""

# -----------------------------
# Battery Configuration
# -----------------------------

INITIAL_SOC = 100.0

MIN_SOC = 0.0

MAX_SOC = 100.0

INITIAL_VOLTAGE = 16.8

MIN_VOLTAGE = 13.0

INITIAL_TEMPERATURE = 25.0

MAX_TEMPERATURE = 60.0

BATTERY_CAPACITY_AH = 5.0

# -----------------------------
# Status Levels
# -----------------------------

FULL = "FULL"

GOOD = "GOOD"

NORMAL = "NORMAL"

LOW = "LOW"

CRITICAL = "CRITICAL"

# -----------------------------
# Logging
# -----------------------------

LOG_FOLDER = "logs"

LOG_FILE = "battery.log"

# -----------------------------
# ROS2
# -----------------------------

BATTERY_TOPIC = "/battery_state"

NODE_NAME = "battery_node"