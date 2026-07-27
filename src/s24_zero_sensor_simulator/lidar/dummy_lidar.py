"""
Dummy LiDAR

S24 Zero Sensor Simulator

Original Author: Chetanya Barodiya

Changes by: Chetanya Barodiya

Reason for Changes:
- Added compatibility wrapper (get_data()) for integration
  with the Sensor Manager and Validation Manager.
- LiDAR point cloud generation remains unchanged.
"""

import time

from s24_zero_sensor_simulator.lidar.lidar import LiDAR
from s24_zero_sensor_simulator.lidar.lidar_frame import LiDARFrame
from s24_zero_sensor_simulator.lidar.point import Point


class DummyLiDAR(LiDAR):

    def __init__(self):

        self.frame_counter = 0

    def get_point_cloud(self):

        self.frame_counter += 1

        points = []

        for i in range(10):

            points.append(
                Point(
                    float(i),
                    float(i * 2),
                    float(i * 3),
                )
            )

        return LiDARFrame(

            points=points,

            timestamp=int(time.time() * 1000),

            frame_number=self.frame_counter,
        )


    def get_data(self):

        return self.get_point_cloud()