from mcpi_e.minecraft import Minecraft
import mcpi_e.block as block
from ObjectLib.RailroadStrategy.AbstractStrategy import AbstractStrategy
from Different import Used, Style, Relative
from Different.Used import Used


class PutBlockAndRail(AbstractStrategy):

    def exec(self, rel: Relative):
        self.used.set_as_used(rel, self.style.bottom)
        self.iteration += 1
        self.flag['powered_rail_block'] = False
        if self.iteration == PUT_POWERED_EACH:
            self.flag['powered_rail_block'] = True
            self.iteration = 0
            self.used.set_as_used(rel.top(1), block.RAIL_POWERED.id)
            self.used.set_as_used(rel.bottom(1), block.TORCH_REDSTONE.id, {'facing': 'bottom'})
            self.used.set_as_used(rel.bottom(2), self.style.bottom)
        else:
            self.used.set_as_used(rel.top(1), block.RAIL.id)


PUT_POWERED_EACH = 25
