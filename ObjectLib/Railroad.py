from Different.Relative import *
from mcpi_e.minecraft import Minecraft
from Different.Used import Used
import mcpi_e.block as block

from ObjectLib.RailroadDecorator.AbstractDecorator import AbstractDecorator
from ObjectLib.RailroadStrategy.AbstractStrategy import AbstractStrategy


class Railroad:

    def __init__(self, mc: Minecraft, used: Used):
        self.mc = mc
        self.used = used

    def draw(self, rel: Relative, distance: int, empty_strategy: AbstractStrategy | AbstractDecorator, busy_strategy: AbstractStrategy):
        """
        Build railway
        :param rel: Relation position
        :param distance: Maximum buid distance
        :param empty_strategy: Behaviour strategy for empty block
        :param busy_strategy: Behaviour strategy for existent block
        :return:
        """
        for i in range(1, distance + 1):
            cur_rel = rel.bottom(1).forward(i)
            block_id = self.used.get_one(cur_rel)
            if block_id == block.AIR.id:
                empty_strategy.exec(cur_rel)
            # elif (block_id == block.WATER.id):
            #     pass
            else:
                busy_strategy.exec(cur_rel)

        for (vec, block_id) in self.used.iterate_by_new():
            self.mc.setBlock(vec, block_id)
