"""
File: master_toggle.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Enable or disable simulator modules.
"""


class MasterToggle:

    def __init__(self):

        self.modules = {}

    def enable(self, name):

        self.modules[name] = True

    def disable(self, name):

        self.modules[name] = False

    def toggle(self, name):

        if name not in self.modules:

            self.modules[name] = True

        else:

            self.modules[name] = not self.modules[name]

    def is_enabled(self, name):

        return self.modules.get(name, False)

    def enable_all(self):

        for name in self.modules:

            self.modules[name] = True

    def disable_all(self):

        for name in self.modules:

            self.modules[name] = False

    def get_status(self):

        return self.modules