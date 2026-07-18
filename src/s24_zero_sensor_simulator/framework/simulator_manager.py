"""
File: simulator_manager.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Main simulator manager responsible for initializing
and controlling all simulator modules.
"""


class SimulatorManager:

    def __init__(self):

        self.modules = []

    def register_module(self, module):

        self.modules.append(module)

    def start(self):

        print("[SimulatorManager] Starting simulator...")

        for module in self.modules:

            if hasattr(module, "start"):
                module.start()

    def stop(self):

        print("[SimulatorManager] Stopping simulator...")

        for module in self.modules:

            if hasattr(module, "stop"):
                module.stop()