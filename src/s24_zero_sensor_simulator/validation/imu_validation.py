"""
IMU Validation
"""

from .validation import Validation


class IMUValidation(Validation):

    def __init__(self):

        super().__init__("IMU")

    def validate(self, data):

        errors = []

        values = [

            data.accel_x,
            data.accel_y,
            data.accel_z,
            data.gyro_x,
            data.gyro_y,
            data.gyro_z

        ]

        for value in values:

            if value is None:

                errors.append("Invalid IMU Data")

                break

        return {

            "sensor": self.name,

            "status": len(errors) == 0,

            "errors": errors

        }