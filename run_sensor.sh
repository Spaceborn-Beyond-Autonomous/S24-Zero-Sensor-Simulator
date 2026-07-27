#!/bin/bash

PROJECT_DIR="/home/ashutosh/zero_sensor_simulator"

gnome-terminal -- bash -c "
cd \"$PROJECT_DIR/DummyCamera\" &&
./camera;
exec bash"

gnome-terminal -- bash -c "
cd \"$PROJECT_DIR/DummyLiDAR\" &&
./lidar;
exec bash"

gnome-terminal -- bash -c "
python3 dummy_gps.py;
exec bash"

gnome-terminal -- bash -c "
python3 imu_sensor.py;
exec bash"

gnome-terminal -- bash -c "
cd \"$PROJECT_DIR/S24-Zero-Sensor-Simulator\" &&
colcon build &&
source install/setup.bash &&
ros2 launch s24_zero_sensor_simulator battery.launch.py
exec bash"
