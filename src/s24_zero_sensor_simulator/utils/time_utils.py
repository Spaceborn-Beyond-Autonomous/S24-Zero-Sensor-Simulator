"""
File: time_utils.py

Author: Chetanya Barodiya

Project: S24 Zero Sensor Simulator

Description:
Time utility functions for the Battery Simulator.
"""

from datetime import datetime
import time


def current_time():
    """
    Return current date and time.
    """

    return datetime.now()


def timestamp():
    """
    Return formatted timestamp.
    """

    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def elapsed_time(start_time):
    """
    Return elapsed time in seconds.
    """

    return time.time() - start_time


def sleep(seconds):
    """
    Pause execution.
    """

    time.sleep(seconds)


def format_seconds(seconds):
    """
    Convert seconds to HH:MM:SS
    """

    hours = int(seconds // 3600)

    minutes = int((seconds % 3600) // 60)

    seconds = int(seconds % 60)

    return f"{hours:02}:{minutes:02}:{seconds:02}"