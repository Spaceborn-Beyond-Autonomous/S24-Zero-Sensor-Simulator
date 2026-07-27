"""
File: validation.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Base validation class.
All sensor validation classes inherit from this class.
"""


class Validation:

    def __init__(self, name):

        self.name = name

    def validate(self, data):

        """
        Override in child class.
        """

        raise NotImplementedError(
            "validate() must be implemented."
        )