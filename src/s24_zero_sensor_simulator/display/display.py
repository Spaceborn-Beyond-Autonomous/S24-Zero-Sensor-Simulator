"""
File: display.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Terminal Dashboard for S24 Zero Sensor Simulator.
Displays live information from all sensors.
"""

import os


class Display:

    def __init__(self):

        self.bar_length = 20

    # ---------------------------------------------------------
    # Battery Progress Bar
    # ---------------------------------------------------------

    def battery_bar(self, soc):

        filled = int((soc / 100) * self.bar_length)

        empty = self.bar_length - filled

        return "█" * filled + "░" * empty

    # ---------------------------------------------------------
    # Dashboard
    # ---------------------------------------------------------

    def show(
        self,
        battery,
        camera,
        lidar,
        imu,
        gps,
        validation
    ):

        os.system("clear")

        print("=" * 60)
        print("         S24 ZERO SENSOR SIMULATOR")
        print("=" * 60)

        # =====================================================
        # Battery
        # =====================================================

        print("\n🔋 Battery")
        print("-" * 60)

        print(f"[{self.battery_bar(battery['soc'])}]")

        print(f"SOC         : {battery['soc']:.2f} %")
        print(f"Voltage     : {battery['voltage']:.2f} V")
        print(f"Current     : {battery['current']:.2f} A")
        print(f"Power       : {battery['power']:.2f} W")
        print(f"Temperature : {battery['temperature']:.2f} °C")
        print(f"ETA         : {battery['eta']:.2f} s")
        print(f"Status      : {battery['status']}")

        # =====================================================
        # Camera
        # =====================================================

        print("\n📷 Camera")
        print("-" * 60)

        print(f"Frame       : {camera.frame_number}")
        print(f"Resolution  : {camera.width} x {camera.height}")
        print(f"Timestamp   : {camera.timestamp}")

        # =====================================================
        # LiDAR
        # =====================================================

        print("\n📡 LiDAR")
        print("-" * 60)

        print(f"Frame       : {lidar.frame_number}")
        print(f"Points      : {len(lidar.points)}")
        print(f"Timestamp   : {lidar.timestamp}")

        # =====================================================
        # IMU
        # =====================================================

        print("\n🧭 IMU")
        print("-" * 60)

        print("Acceleration (m/s²)")
        print(f"  X : {imu.accel_x:.4f}")
        print(f"  Y : {imu.accel_y:.4f}")
        print(f"  Z : {imu.accel_z:.4f}")

        print()

        print("Gyroscope (rad/s)")
        print(f"  X : {imu.gyro_x:.4f}")
        print(f"  Y : {imu.gyro_y:.4f}")
        print(f"  Z : {imu.gyro_z:.4f}")

        # =====================================================
        # GPS
        # =====================================================

        print("\n🛰 GPS")
        print("-" * 60)

        print(f"Latitude    : {gps.latitude}")
        print(f"Longitude   : {gps.longitude}")
        print(f"Altitude    : {gps.altitude} m")
        print(f"Timestamp   : {gps.timestamp}")

        # =====================================================
        # Validation
        # =====================================================

        print("\n✅ Validation")
        print("-" * 60)

        for sensor, result in validation.items():

            if result is None:

                continue

            status = "PASS" if result["status"] else "FAIL"

            print(f"{sensor:<12}: {status}")

        print("\n" + "=" * 60)