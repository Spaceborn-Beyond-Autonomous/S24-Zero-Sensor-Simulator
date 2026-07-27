"""
GPS Validation
"""

from .validation import Validation


class GPSValidation(Validation):

    def __init__(self):

        super().__init__("GPS")

    def validate(self, data):

        errors = []

        if hasattr(data, "latitude"):

            if data.latitude < -90 or data.latitude > 90:

                errors.append("Invalid Latitude")

        if hasattr(data, "longitude"):

            if data.longitude < -180 or data.longitude > 180:

                errors.append("Invalid Longitude")

        return {

            "sensor": self.name,

            "status": len(errors) == 0,

            "errors": errors

        }