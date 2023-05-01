from __future__ import annotations
from mcpi_e.minecraft import Minecraft
from ObjectLib.RailroadStrategy.AbstractStrategy import AbstractStrategy
from Different.Relative import Relative


class AbstractDecorator:
    def __init__(self, mc: Minecraft, decorated: AbstractDecorator | AbstractStrategy):
        self.decorated = decorated
        self.mc = mc

    def get_decorated(self) -> AbstractStrategy:
        """
        Get undecorated strategy to reach some basic properties
        :return: Strategy
        """
        return self.decorated.get_decorated()

    def exec(self, rel: Relative):
        pass

