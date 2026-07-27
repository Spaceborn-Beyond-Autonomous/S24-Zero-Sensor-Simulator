"""
Camera Node

S24 Zero Sensor Simulator

Author: Chetanya Barodiya
"""

import time

from s24_zero_sensor_simulator.camera.dummy_camera import DummyCamera


def main():

    camera = DummyCamera()

    while True:

        frame = camera.capture_frame()

        print("--------------------------------")

        print(f"Frame Number : {frame.frame_number}")

        print(f"Timestamp    : {frame.timestamp}")

        print(f"Resolution   : {frame.width} x {frame.height}")

        print(f"Image Bytes  : {len(frame.image)}")

        time.sleep(0.1)


if __name__ == "__main__":

    main()