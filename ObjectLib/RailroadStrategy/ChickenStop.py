from Different.Relative import *
from mcpi_e.minecraft import Minecraft
from Different.Used import Used
import mcpi_e.block as block
from ObjectLib.RailroadStrategy.AbstractStrategy import AbstractStrategy


class ChickenStop(AbstractStrategy):
    """
    Stop on any block. Do nothing.
    """
    def exec(self, rel: Relative):
        pass
