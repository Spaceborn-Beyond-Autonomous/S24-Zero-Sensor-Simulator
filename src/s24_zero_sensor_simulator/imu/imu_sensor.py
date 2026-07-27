"""
File: imu_sensor.py

Original Author: <Ashutosh Bhardwaj>

Changes by: Chetanya Barodiya

Reason for Changes:
- Converted IMU module into an import-safe Python package.
- Wrapped standalone demonstration code inside
  `if __name__ == "__main__":`
- No changes were made to IMU data generation logic.
- Required for integration with the S24 Zero Sensor Simulator
  framework and ROS2 package architecture.
"""

import time
import random
from dataclasses import dataclass


@dataclass
class IMUData:
    accel_x: float
    accel_y: float
    accel_z: float
    gyro_x: float
    gyro_y: float
    gyro_z: float


class DummyIMU:

    def __init__(self, noise=True):

        self.noise = noise

    def get_data(self):

        if self.noise:

            return IMUData(

                accel_x=random.uniform(-0.02, 0.02),
                accel_y=random.uniform(-0.02, 0.02),
                accel_z=random.uniform(-0.02, 0.02),

                gyro_x=random.uniform(-0.01, 0.01),
                gyro_y=random.uniform(-0.01, 0.01),
                gyro_z=random.uniform(-0.01, 0.01)

            )

        else:

            return IMUData(

                accel_x=0.0,
                accel_y=0.0,
                accel_z=0.0,

                gyro_x=0.0,
                gyro_y=0.0,
                gyro_z=0.0

            )


# ----------------------------------------------------
# Changes by Chetanya Barodiya
#
# This block is executed ONLY when this file is run
# directly.
#
# When imported into the simulator framework,
# this block will NOT execute.
# ----------------------------------------------------

if __name__ == "__main__":

    imu = DummyIMU(noise=True)

    while True:

        data = imu.get_data()

        print("-----------------------")

        print("Acceleration (m/s²)")
        print(f"X: {data.accel_x}")
        print(f"Y: {data.accel_y}")
        print(f"Z: {data.accel_z}")

        print("\nGyroscope (rad/s)")
        print(f"X: {data.gyro_x}")
        print(f"Y: {data.gyro_y}")
        print(f"Z: {data.gyro_z}")

        time.sleep(1)