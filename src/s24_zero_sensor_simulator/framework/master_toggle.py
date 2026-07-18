"""
File: master_toggle.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Enable or disable simulator modules.
"""


class MasterToggle:

    def __init__(self):

        self.enabled = True

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False

    def status(self):

        return self.enabled