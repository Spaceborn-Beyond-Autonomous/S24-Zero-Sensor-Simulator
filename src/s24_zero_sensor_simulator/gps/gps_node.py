"""
File: gps_node.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
ROS2 node for Dummy GPS.
Displays GPS data continuously in terminal.
"""

import rclpy
from rclpy.node import Node

from s24_zero_sensor_simulator.gps.dummy_gps import DummyGPS


class GPSNode(Node):

    def __init__(self):

        super().__init__("gps_node")

        self.gps = DummyGPS()

        self.timer = self.create_timer(
            1.0,
            self.publish_data
        )

        self.get_logger().info("GPS Node Started")

    def publish_data(self):

        data = self.gps.get_data()

        print("\n========== GPS ==========")

        print(f"Latitude  : {data.latitude}")

        print(f"Longitude : {data.longitude}")

        print(f"Altitude  : {data.altitude} m")

        print(f"Time      : {data.timestamp}")

        print("=========================\n")


def main(args=None):

    rclpy.init(args=args)

    node = GPSNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()