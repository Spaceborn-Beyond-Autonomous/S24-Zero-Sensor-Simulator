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
│                       
├── CMakeLists.txt
├── config
│   ├── battery.yaml
│   └── simulator.yaml
├── docs
│   ├── architecture.md
│   ├── battery.md
│   └── logger.md
├── launch
│   └── battery.launch.py
├── requirements.txt
├── resource
│   └── s24_zero_sensor_simulator
├── src
│   └── s24_zero_sensor_simulator
│       ├── __init__.py
│       ├── battery
│       │   ├──__init__.py
│       │   ├── battery_model.py
│       │   ├── battery_node.py
│       │   └── battery_state.py  
│       ├── display
│       │   ├──__init__.py
│       │   └── display.py
│       │   
│       ├── framework
│       │   ├── __init__.py
│       │   ├── hal_wrapper.py
│       │   ├── sensor_manager.py
│       │   ├── simulator_manager.py
│       │   └── master_toggle.py
│       ├── logger
│       │   ├── __init__.py
│       │   └── validation_logger.py      
│       └── utils
│           ├── __init__.py
│           ├── config_loader.py
│           ├── constants.py
│           ├── math_utils.py         
│           └── time_utils.py
├── setup.cfg
├── setup.py
├── LICENSE.md
├── package.xml
├── README.md
└── tests
    ├── __init__.py
    ├── test_battery.py
    ├── test_display.py
    └── test_logger.py



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
