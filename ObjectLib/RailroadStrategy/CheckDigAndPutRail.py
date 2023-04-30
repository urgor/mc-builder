from Different.Relative import *
from mcpi_e.minecraft import Minecraft
from Different.Used import Used
import mcpi_e.block as block
from ObjectLib.RailroadStrategy.Strategy import Strategy


class CheckDigAndPutRail(Strategy):
    def exec(self, rel: Relative):
        self.used.set_as_used(rel, self.style.bottom)
        self.used.set_as_used(rel.top(1), block.RAIL.id)