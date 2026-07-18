"""
File: hal_wrapper.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Hardware Abstraction Layer wrapper.

Acts as an interface between Mission Software
and the Zero Sensor Simulator.
"""


class HALWrapper:

    def __init__(self):

        self.connected = False

    def connect(self):

        self.connected = True

        print("[HAL] Connected")

    def disconnect(self):

        self.connected = False

        print("[HAL] Disconnected")

    def is_connected(self):

        return self.connected