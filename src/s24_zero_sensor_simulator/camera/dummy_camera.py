"""
Dummy Camera

S24 Zero Sensor Simulator

Original Author: Chetanya Barodiya

Changes by: Chetanya Barodiya

Reason for Changes:
- Added compatibility wrapper (get_data()) for integration
  with the Sensor Manager and Validation Manager.
- Camera capture logic remains unchanged.
"""

import time

from s24_zero_sensor_simulator.camera.camera import Camera
from s24_zero_sensor_simulator.camera.camera_frame import CameraFrame


class DummyCamera(Camera):

    def __init__(self):

        self.frame_counter = 0

        self.width = 640

        self.height = 480

    def capture_frame(self):

        self.frame_counter += 1

        frame = CameraFrame(

            width=self.width,

            height=self.height,

            image=bytes(self.width * self.height),

            timestamp=int(time.time() * 1000),

            frame_number=self.frame_counter,

        )

        return frame

    
    def get_data(self):

        return self.capture_frame()