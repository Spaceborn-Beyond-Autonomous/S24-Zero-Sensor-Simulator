"""
File: display.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Terminal display for Battery Simulator.
"""

import os


class BatteryDisplay:

    def __init__(self):

        self.bar_length = 20

    def battery_bar(self, soc):

        """
        Create battery progress bar.
        """

        filled = int((soc / 100) * self.bar_length)

        empty = self.bar_length - filled

        return "█" * filled + "░" * empty

    def show(self, state):

        """
        Display battery information.
        """

        os.system("clear")

        print("=" * 50)

        print("      S24 ZERO SENSOR SIMULATOR")

        print("=" * 50)

        print()

        print("🔋 BATTERY")

        print()

        print(f"[{self.battery_bar(state['soc'])}]")

        print()

        print(f"SOC         : {state['soc']:.2f} %")

        print(f"Voltage     : {state['voltage']:.2f} V")

        print(f"Current     : {state['current']:.2f} A")

        print(f"Power       : {state['power']:.2f} W")

        print(f"Temperature : {state['temperature']:.2f} °C")

        print(f"ETA         : {state['eta']:.2f} s")

        print(f"Status      : {state['status']}")

        print()

        print("=" * 50)