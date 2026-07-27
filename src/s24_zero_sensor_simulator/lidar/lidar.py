"""
LiDAR Interface

S24 Zero Sensor Simulator

Author: Chetanya Barodiya
"""

from abc import ABC, abstractmethod


class LiDAR(ABC):

    @abstractmethod
    def get_point_cloud(self):
        pass