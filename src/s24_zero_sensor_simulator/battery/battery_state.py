"""
File: battery_state.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Creates and updates ROS2 BatteryState messages.
"""

from sensor_msgs.msg import BatteryState


class BatteryStatePublisher:
    """
    Converts BatteryModel data into a ROS2 BatteryState message.
    """

    def __init__(self):

        self.msg = BatteryState()

    def create(self, battery):

        """
        Populate BatteryState message from BatteryModel.
        """

        state = battery.get_state()

        self.msg.percentage = state["soc"] / 100.0

        self.msg.voltage = float(state["voltage"])

        self.msg.current = float(state["current"])

        self.msg.temperature = float(state["temperature"])

        self.msg.present = True

        self.msg.power_supply_status = (
            BatteryState.POWER_SUPPLY_STATUS_DISCHARGING
        )

        self.msg.power_supply_health = (
            BatteryState.POWER_SUPPLY_HEALTH_GOOD
        )

        self.msg.power_supply_technology = (
            BatteryState.POWER_SUPPLY_TECHNOLOGY_LIPO
        )

        return self.msg