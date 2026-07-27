"""
File: imu_node.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
ROS2 node for Dummy IMU.
Displays IMU data continuously in terminal.
"""

import rclpy
from rclpy.node import Node

from s24_zero_sensor_simulator.imu.imu_sensor import DummyIMU


class IMUNode(Node):

    def __init__(self):

        super().__init__("imu_node")

        self.imu = DummyIMU()

        self.timer = self.create_timer(
            1.0,
            self.publish_data
        )

        self.get_logger().info("IMU Node Started")

    def publish_data(self):

        data = self.imu.get_data()

        print("\n========== IMU ==========")

        print("Acceleration (m/s²)")
        print(f"X : {data.accel_x:.4f}")
        print(f"Y : {data.accel_y:.4f}")
        print(f"Z : {data.accel_z:.4f}")

        print()

        print("Gyroscope (rad/s)")
        print(f"X : {data.gyro_x:.4f}")
        print(f"Y : {data.gyro_y:.4f}")
        print(f"Z : {data.gyro_z:.4f}")

        print("=========================\n")


def main(args=None):

    rclpy.init(args=args)

    node = IMUNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == "__main__":
    main()