"""
Camera Validation
"""

from .validation import Validation


class CameraValidation(Validation):

    def __init__(self):

        super().__init__("Camera")

    def validate(self, frame):

        errors = []

        if frame.width <= 0:
            errors.append("Invalid Width")

        if frame.height <= 0:
            errors.append("Invalid Height")

        if len(frame.image) == 0:
            errors.append("Empty Image")

        return {

            "sensor": self.name,

            "status": len(errors) == 0,

            "errors": errors

        }