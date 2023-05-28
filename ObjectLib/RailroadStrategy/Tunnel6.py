from mcpi_e.minecraft import Minecraft
import mcpi_e.block as block
from ObjectLib.RailroadStrategy.AbstractStrategy import AbstractStrategy
from Different.Used import *
from Different.Style import *
from Different.Relative import *


class Tunnel6(AbstractStrategy):
    liquid = [block.WATER, block.LAVA]

    def exec(self, rel: Relative, builder_state):
        a = rel.left(2).get_current()
        b = rel.right(2).top(3).get_current()
        self.used = Used(a, b, self.mc.getBlocks(a, b))

        cur = rel.top(3).left(1)  # top
        for i in range(3):
            if self.used.get_one(cur) in Tunnel6.liquid:
                self.flume.set_as_used(cur, self.style.underwater_top)
            else:
                self.flume.set_as_used(cur, self.style.top)
            cur = cur.right(1)

        cur = rel.left(1)  # bottom
        for i in range(3):
            if self.used.get_one(cur) in Tunnel6.liquid:
                self.flume.set_as_used(cur, self.style.underwater_top)
            else:
                self.flume.set_as_used(cur, self.style.top)
            cur = cur.right(1)

        cur = rel.top(2).left(2)  # left wall
        for i in range(2):
            if self.used.get_one(cur) in Tunnel6.liquid:
                self.flume.set_as_used(cur, self.style.underwater_wall)
            else:
                self.flume.set_as_used(cur, self.style.wall)
            cur = cur.bottom(1)

        cur = rel.top(2).right(2)  # right wall
        for i in range(2):
            if self.used.get_one(cur) in Tunnel6.liquid:
                self.flume.set_as_used(cur, self.style.underwater_wall)
            else:
                self.flume.set_as_used(cur, self.style.wall)
            cur = cur.bottom(1)

        for i in [1, 2]:
            row = rel.top(i).left(1)
            self.flume.set_as_used(row, block.AIR.id)
            self.flume.set_as_used(row.right(1), block.AIR.id)
            self.flume.set_as_used(row.right(2), block.AIR.id)
