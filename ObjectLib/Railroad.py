from Different.Relative import *
from mcpi_e.minecraft import Minecraft
from Different.Used import Used
import mcpi_e.block as block
from Different import Used, Style, Relative
from Different.Direction import *

from ObjectLib.RailroadDecorator.AbstractDecorator import AbstractDecorator
from ObjectLib.RailroadStrategy.AbstractStrategy import AbstractStrategy

PUT_POWERED_EACH = 25

class Railroad:

    def __init__(self, mc: Minecraft, used: Used, style: Style):
        self.mc = mc
        self.used = used
        self.style = style

        self.state = {
            'powered_rail_block': False,
            'iteration': 0
        }

    def draw(self, a: Relative, b: Relative, empty_strategy: AbstractStrategy | AbstractDecorator, busy_strategy: AbstractStrategy):
        """
        Build railway
        :param a: build from point a
        :param b: to point b
        :param empty_strategy: Behaviour strategy for empty block
        :param busy_strategy: Behaviour strategy for existent block
        :return:
        """
        distance = a.towards(b)
        for i in range(1, distance + 1):
            self.state['iteration'] += 1
            self.state['powered_rail_block'] = False
            cur = a.bottom(1).forward(i)
            self.used.set_as_used(cur, self.style.bottom)

            if self.state['iteration'] == PUT_POWERED_EACH:
                self.state['powered_rail_block'] = True
                self.state['iteration'] = 0
                self.used.set_as_used(cur.top(1), block.RAIL_POWERED.id)
                self.used.set_as_used(cur.bottom(1), block.TORCH_REDSTONE.withData(UP))
                self.used.set_as_used(cur.bottom(2), self.style.bottom)
            else:
                self.used.set_as_used(cur.top(1), block.RAIL.id)

            block_id = self.used.get_one(cur)
            # if block_id == block.AIR.id:
            empty_strategy.exec(cur, self.state)
            # elif (block_id == block.WATER.id):
            #     pass
            # else:
            #     busy_strategy.exec(cur_rel)


        # for (vec, block_id) in self.used.iterate_by_new():
        for (vec, block_id) in self.used.iterate_by_new_ordered():
            self.mc.setBlock(vec, block_id)
