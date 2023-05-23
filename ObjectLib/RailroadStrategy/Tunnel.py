from mcpi_e.minecraft import Minecraft
import mcpi_e.block as block
from ObjectLib.RailroadStrategy.AbstractStrategy import AbstractStrategy
from Different import Used, Style, Relative

class Tunnel(AbstractStrategy):

    def exec(self, rel: Relative, builder_state):
        # a = rel.left(2).get_current()
        # b = rel.right(2).top(4).get_current()
        # used = Used(a, b, self.mc.getBlocks(a, b))
        top = rel.top(4).left(1)
        self.flume.set_as_used(top, self.style.top)
        self.flume.set_as_used(top.right(1), self.style.top)
        self.flume.set_as_used(top.right(2), self.style.top)
        left = rel.top(3).left(2)
        self.flume.set_as_used(left, self.style.wall)
        self.flume.set_as_used(left.bottom(1), self.style.wall)
        self.flume.set_as_used(left.bottom(2), self.style.wall)
        right = rel.top(3).right(2)
        self.flume.set_as_used(right, self.style.wall)
        self.flume.set_as_used(right.bottom(1), self.style.wall)
        self.flume.set_as_used(right.bottom(2), self.style.wall)

        for i in [1,2,3]:
            row = rel.top(i).left(1)
            self.flume.set_as_used(row, block.AIR.id)
            self.flume.set_as_used(row.right(1), block.AIR.id)
            self.flume.set_as_used(row.right(2), block.AIR.id)