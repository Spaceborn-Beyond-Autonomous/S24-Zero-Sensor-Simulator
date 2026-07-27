from dataclasses import dataclass


@dataclass
class CameraFrame:

    width: int

    height: int

    image: bytes

    timestamp: int

    frame_number: int