"""
File: battery_node.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
ROS2 Battery Simulator Node
"""

import rclpy

from rclpy.node import Node

from sensor_msgs.msg import BatteryState

from s24_zero_sensor_simulator.battery.battery_model import BatteryModel
from s24_zero_sensor_simulator.battery.battery_state import BatteryStatePublisher
from s24_zero_sensor_simulator.logger.validation_logger import ValidationLogger
from s24_zero_sensor_simulator.display.display import BatteryDisplay
from s24_zero_sensor_simulator.utils.constants import *


class BatteryNode(Node):

    def __init__(self):

        super().__init__(NODE_NAME)

        self.publisher = self.create_publisher(
            BatteryState,
            BATTERY_TOPIC,
            10
        )

        self.battery = BatteryModel()

        self.state = BatteryStatePublisher()

        self.logger = ValidationLogger()

        self.display = BatteryDisplay()

        self.timer = self.create_timer(
            1.0,
            self.update_battery
        )

        self.get_logger().info(
            "Battery Simulator Started"
        )

    def update_battery(self):

        """
        Timer Callback
        """

        self.battery.update()

        msg = self.state.create(self.battery)

        self.publisher.publish(msg)

        state = self.battery.get_state()

        self.display.show(state)

        self.logger.log_battery(state)

    def destroy_node(self):

        self.logger.log_shutdown()

        super().destroy_node()


def main(args=None):

    rclpy.init(args=args)

    node = BatteryNode()

    try:

        rclpy.spin(node)

    except KeyboardInterrupt:

        pass

    finally:

        node.destroy_node()

        rclpy.shutdown()


if __name__ == "__main__":

    main()