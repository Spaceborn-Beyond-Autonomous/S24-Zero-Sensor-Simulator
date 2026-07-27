"""
LiDAR Validation
"""

from .validation import Validation


class LidarValidation(Validation):

    def __init__(self):

        super().__init__("LiDAR")

    def validate(self, frame):

        errors = []

        if len(frame.points) == 0:
            errors.append("No Point Cloud")

        return {

            "sensor": self.name,

            "status": len(errors) == 0,

            "errors": errors

        }