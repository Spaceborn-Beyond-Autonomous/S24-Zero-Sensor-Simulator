"""
LiDAR Node

S24 Zero Sensor Simulator

Author: Chetanya Barodiya
"""

import time

from s24_zero_sensor_simulator.lidar.dummy_lidar import DummyLiDAR


def main():

    lidar = DummyLiDAR()

    while True:

        frame = lidar.get_point_cloud()

        print("--------------------------------------")

        print(f"Frame Number : {frame.frame_number}")

        print(f"Timestamp    : {frame.timestamp}")

        print(f"Point Count  : {len(frame.points)}")

        print("\nPoints")

        for point in frame.points:

            print(
                f"({point.x}, {point.y}, {point.z})"
            )

        time.sleep(0.1)


if __name__ == "__main__":

    main()