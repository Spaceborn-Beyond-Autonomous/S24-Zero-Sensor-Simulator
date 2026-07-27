"""
File: simulator.launch.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
ROS2 Launch File for the complete
S24 Zero Sensor Simulator.

This launches the central simulator node,
which internally initializes:

- Battery
- Camera
- LiDAR
- IMU
- GPS
- Validation
- Logger
"""

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    simulator = Node(

        package="s24_zero_sensor_simulator",

        executable="simulator_node",

        name="simulator",

        output="screen",

        emulate_tty=True,

    )

    return LaunchDescription([

        simulator

    ])
    