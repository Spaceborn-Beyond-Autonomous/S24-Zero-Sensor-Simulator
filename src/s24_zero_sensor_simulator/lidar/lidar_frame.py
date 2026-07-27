"""
LiDAR Frame

S24 Zero Sensor Simulator

Author: Chetanya Barodiya
"""

from dataclasses import dataclass
from typing import List

from s24_zero_sensor_simulator.lidar.point import Point


@dataclass
class LiDARFrame:

    points: List[Point]

    timestamp: int

    frame_number: int