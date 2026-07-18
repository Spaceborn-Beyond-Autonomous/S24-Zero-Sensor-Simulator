"""
Display Test
"""

from src.display.display import BatteryDisplay


def test_display():

    display = BatteryDisplay()

    state = {

        "soc":75,

        "voltage":15.8,

        "current":2,

        "power":30,

        "temperature":26,

        "eta":150,

        "status":"GOOD"

    }

    display.show(state)