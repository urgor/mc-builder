from __future__ import annotations
from mcpi_e.minecraft import Minecraft

from Different import Used, Style, Relative


class AbstractStrategy:
    def __init__(self, mc: Minecraft, used: Used, style: Style):
        self.iteration = 0
        self.used = used
        self.style = style
        self.mc = mc
        self.flag = {
            'powered_rail_block': False
        }

    def get_decorated(self) -> AbstractStrategy:
        """
        Get undecorated strategy to reach some basic properties
        :return: Strategy
        """
        return self

    def exec(self, rel: Relative):
        pass

    