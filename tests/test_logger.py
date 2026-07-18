"""
Logger Test
"""

from src.logger.validation_logger import ValidationLogger


def test_logger():

    logger = ValidationLogger()

    state = {

        "soc":100,

        "voltage":16.8,

        "current":0.5,

        "power":8.4,

        "temperature":25,

        "eta":100,

        "status":"FULL"

    }

    logger.log_battery(state)