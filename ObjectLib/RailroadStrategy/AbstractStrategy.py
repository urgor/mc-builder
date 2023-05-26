from __future__ import annotations
from mcpi_e.minecraft import Minecraft
from Different import Style, Relative, Flume


class AbstractStrategy:
    def __init__(self, mc: Minecraft, style: Style, flume: Flume):
        self.style = style
        self.mc = mc
        self.flume = flume
        self.used = None

    def get_decorated(self) -> AbstractStrategy:
        """
        Get undecorated strategy to reach some basic properties
        :return: Strategy
        """
        return self

    def exec(self, rel: Relative, builder_state: dict):
        pass

    