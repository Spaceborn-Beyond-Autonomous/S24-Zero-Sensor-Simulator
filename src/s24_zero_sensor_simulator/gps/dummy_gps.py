"""
File: dummy_gps.py

Original Author: Ashutosh Bhardwaj

Changes by: Chetanya Barodiya

Reason for Changes:
- Converted GPS module into an import-safe Python package.
- Wrapped standalone execution code inside
  `if __name__ == "__main__":`
- Added a compatibility wrapper (`get_data()`) for integration
  with the S24 Zero Sensor Simulator framework.
- GPS data generation logic remains unchanged.
"""

import time
from dataclasses import dataclass
from datetime import datetime


@dataclass
class GPSData:

    latitude: float
    longitude: float
    altitude: float
    timestamp: str


class DummyGPS:

    def __init__(self):

        self.latitude = 28.6139
        self.longitude = 77.2090
        self.altitude = 216.0

    def read(self) -> GPSData:

        return GPSData(

            latitude=self.latitude,
            longitude=self.longitude,
            altitude=self.altitude,
            timestamp=datetime.now().strftime("%H:%M:%S")

        )

    # ----------------------------------------------------
    # Changes by Chetanya Barodiya
    #
    # Compatibility wrapper for the simulator framework.
    # This does NOT modify GPS functionality.
    # It simply provides a common interface used by
    # the Sensor Manager and Validation Manager.
    # ----------------------------------------------------
    def get_data(self):

        return self.read()

    def stream(self, frequency_hz=1):

        delay = 1 / frequency_hz

        while True:

            gps = self.read()

            print("=" * 40)
            print(f"Time      : {gps.timestamp}")
            print(f"Latitude  : {gps.latitude}")
            print(f"Longitude : {gps.longitude}")
            print(f"Altitude  : {gps.altitude} m")

            time.sleep(delay)


# ----------------------------------------------------
# Changes by Chetanya Barodiya
#
# This block executes only when this file is run
# directly.
#
# Importing DummyGPS inside the simulator framework
# will no longer start the streaming loop.
# ----------------------------------------------------

if __name__ == "__main__":

    gps = DummyGPS()

    gps.stream(frequency_hz=1)