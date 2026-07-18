# S24 Zero Sensor Simulator

## Overview

The **S24 Zero Sensor Simulator** is a ROS 2 Python package that provides dummy sensor data for early software development, testing, validation, and continuous integration without requiring real hardware.

This project is part of the Spaceborn Autonomous Systems software stack.

---

## Current Implemented Module

✅ Battery Simulator

---

## Planned Modules

- IMU
- GPS
- LiDAR
- Camera
- Battery

---

## Project Structure


S24-Zero-Sensor-Simulator/

├── launch/
├── config/
├── docs/
├── logs/
├── tests/
├── src/
    │
    ├── framework/
    ├── battery/
    ├── logger/
    ├── display/
    └── utils/


---

## Battery Features

- Battery percentage simulation
- Voltage simulation
- Current simulation
- Power calculation
- Temperature simulation
- Battery health monitoring
- Terminal battery display
- Validation logger
- ROS2 BatteryState publisher

---

## ROS2 Topic


/battery_state


Message Type


sensor_msgs/msg/BatteryState


---

## Configuration

Configuration files are located inside


config/


Example


battery.yaml
simulator.yaml


---

## Launch


ros2 launch s24_zero_sensor_simulator battery.launch.py


---

## Build


colcon build

source install/setup.bash


---

## Run


ros2 run s24_zero_sensor_simulator battery_node


or


ros2 launch s24_zero_sensor_simulator battery.launch.py


---

## Output

========================================
S24 ZERO SENSOR SIMULATOR

🔋 BATTERY

[████████████████████]

SOC : 100 %

Voltage : 16.8 V

Current : 0.5 A

Temperature : 25 °C

Status : FULL


---
