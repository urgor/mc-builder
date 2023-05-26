from Different.Relative import *
from mcpi_e.minecraft import Minecraft
import mcpi_e.block as block
from Different.Used import *
from Different.Flume import *
from Different.Style import Style
from Different.Relative import Relative
from Different.Direction import *

from ObjectLib.RailroadDecorator.AbstractDecorator import AbstractDecorator
from ObjectLib.RailroadStrategy.AbstractStrategy import AbstractStrategy
from ObjectLib.RailroadStrategy.DoNothing import *

PUT_POWERED_EACH = 25


class Railroad:
    liquid = [block.WATER.id, block.LAVA.id]
    fluffy = [block.AIR.id, block.WATER.id, block.LAVA.id, block.LEAVES.id, block.LEAVES2.id]
    empty = [block.AIR.id, block.GRASS.id, block.GRASS_TALL.id, block.DEAD_BUSH.id, block.CACTUS.id, block.SUGAR_CANE.id,
             block.FLOWER_CYAN.id, block.FLOWER_YELLOW.id, block.SNOW.id, block.SNOW_BLOCK.id]

    def __init__(self, mc: Minecraft, style: Style, flume: Flume):
        self.mc = mc
        self.style = style
        self.in_air = DoNothing(mc, style, flume)
        self.on_ground = DoNothing(mc, style, flume)
        self.in_water = DoNothing(mc, style, flume)
        self.in_tunnel = DoNothing(mc, style, flume)
        self.flume = flume
        self.used = None

        self.state = {
            'powered_rail_block': False,
            'iteration': 0
        }

    def set_strategy_for_air(self, strategy: AbstractStrategy | AbstractDecorator):
        self.in_air = strategy

    def set_strategy_for_ground(self, strategy: AbstractStrategy | AbstractDecorator):
        self.on_ground = strategy

    def set_strategy_for_tunnel(self, strategy: AbstractStrategy | AbstractDecorator):
        self.in_tunnel = strategy

    def draw(self, a: Relative, b: Relative):
        """
        Build railway
        :param a: build from point a
        :param b: to point b
        :param empty_strategy: Behaviour strategy for empty block
        :param busy_strategy: Behaviour strategy for existent block
        :return:
        """
        distance = a.towards(b)
        self.used = Used(a.top(3).get_current(), a.bottom(2).forward(distance).get_current(),
                         self.mc.getBlocks(a.top(3).get_current(), a.bottom(2).forward(distance).get_current()))
        cur = a.backward(1)
        for i in range(distance):
            self.state['iteration'] += 1
            self.state['powered_rail_block'] = False
            cur = cur.forward(1)  # shift cursor on next work position

            cur_block = self.used.get_one(cur)
            if cur_block in Railroad.empty:
                block_under_cur = self.used.get_one(cur.bottom(1))
                if block_under_cur in [block.AIR.id, block.WATER.id, block.LAVA.id]:
                    self.flume.set_as_used(cur, self.style.bottom)  # some gape under cur: bridging
                    self.in_air.exec(cur, self.state)
                else:
                    cur = cur.bottom(1)  # some hard block, can decrease and build
                    self.used.add(cur.top(3).get_current(), cur.bottom(2).forward(distance - i).get_current(),
                                  self.mc.getBlocks(cur.top(3).get_current(), cur.bottom(2).forward(distance - i).get_current()))
            elif cur_block not in Railroad.fluffy:  # cur in dense block
                block_above_1 = self.used.get_one(cur.top(1))  # check above
                block_above_2 = self.used.get_one(cur.top(2))  # check above
                block_above_3 = self.used.get_one(cur.top(3))  # check above

                if block_above_1 in Railroad.empty and block_above_2 in Railroad.empty:  # there is space: could build rr
                    pass
                elif block_above_1 not in Railroad.fluffy and block_above_2 in Railroad.empty and block_above_3 in Railroad.empty:  # single stair
                    cur = cur.top(1)  # can increase height and build
                    self.used.add(cur.top(3).get_current(), cur.bottom(2).forward(distance - i).get_current(),
                                  self.mc.getBlocks(cur.top(3).get_current(), cur.bottom(2).forward(distance - i).get_current()))
                elif block_above_1 not in Railroad.fluffy and block_above_2 not in Railroad.fluffy and block_above_3 in Railroad.empty:  # 2 blocks and air above
                    self.flume.set_as_used(cur.top(1), block.AIR.id)  # just remove extra blocks
                    self.flume.set_as_used(cur.top(2), block.AIR.id)
                else:
                    self.flume.set_as_used(cur.top(1), block.AIR.id)  # more than 3 dense block above: go to tunneling
                    self.in_tunnel.exec(cur, self.state)

            self.flume.set_as_used(cur, self.style.bottom)
            self.flume.set_as_used(cur.top(2), block.AIR.id)
            if self.state['iteration'] == PUT_POWERED_EACH:
                self.state['powered_rail_block'] = True
                self.state['iteration'] = 0
                self.flume.set_as_used(cur.top(1), block.RAIL_POWERED.id)
                self.flume.set_as_used(cur.bottom(2), self.style.bottom)
                if self.used.get_one(cur.bottom(1)) in Railroad.liquid:
                    self.flume.set_as_used(cur.bottom(1).left(1), self.style.bottom)
                    self.flume.set_as_used(cur.bottom(1).right(1), self.style.bottom)
                    self.flume.set_as_used(cur.bottom(1).forward(1), self.style.bottom)
                    self.flume.set_as_used(cur.bottom(1).backward(1), self.style.bottom)
                self.flume.set_as_used(cur.bottom(1), block.TORCH_REDSTONE.withData(UP))
            else:
                self.flume.set_as_used(cur.top(1), block.RAIL.id)
