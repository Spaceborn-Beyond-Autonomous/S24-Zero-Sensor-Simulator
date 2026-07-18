from launch import LaunchDescription

from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(

            package="s24_zero_sensor_simulator",

            executable="battery_node",

            name="battery_node",

            output="screen"

        )

    ])