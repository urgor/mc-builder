from Different.Relative import *
from mcpi_e.minecraft import Minecraft
from Different.Used import Used
import mcpi_e.block as block
from ObjectLib.RailroadStrategy.Strategy import Strategy


class ChickenStop(Strategy):
    """
    Stop on any block. Do nothing.
    """
    def exec(self, rel: Relative):
        pass
