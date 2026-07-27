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

    def unregister_module(self, module):

        if module in self.modules:

            self.modules.remove(module)

    def get_modules(self):

        return self.modules

    def total_modules(self):

        return len(self.modules)

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

    def restart(self):

        self.stop()

        self.start()