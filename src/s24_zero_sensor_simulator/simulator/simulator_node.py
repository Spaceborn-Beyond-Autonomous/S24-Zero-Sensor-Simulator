"""
File: simulator_node.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Main Simulator Node.
Continuously updates all sensors, validation,
display and logger until the user stops the simulator.
"""

import time

from s24_zero_sensor_simulator.simulator.simulator import Simulator


def main():

    simulator = Simulator()

    simulator.status()

    simulator.start()

    print("\nPress Ctrl+C to stop the simulator.\n")

    try:

        while True:

            simulator.validate()

            time.sleep(1)

    except KeyboardInterrupt:

        print("\n\nStopping Simulator...")

    finally:

        simulator.stop()


if __name__ == "__main__":

    main()