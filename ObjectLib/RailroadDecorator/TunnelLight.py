from mcpi_e import block

from Different.Relative import Relative as Rltv
from ObjectLib.RailroadDecorator.AbstractDecorator import AbstractDecorator
from mcpi_e.minecraft import Minecraft
from ObjectLib.RailroadStrategy.AbstractStrategy import AbstractStrategy
import random


class TunnelLight(AbstractDecorator):
    """
    This one sets light sources into tunnel. Light blocks could be list of any block or torch (not lantern), frequency_*
    params determine minimum and maximum blocks appearance for light.
    """
    stair = [block.STAIRS_WOOD, block.STAIRS_BRICK, block.STAIRS_SANDSTONE, block.STAIRS_COBBLESTONE,
             block.STAIRS_STONE_BRICK, block.STAIRS_NETHER_BRICK]
    torch = [block.TORCH, block.TORCH_REDSTONE]

    def __init__(self, mc: Minecraft, decorated: AbstractDecorator | AbstractStrategy,
                 light_blocks: list = [block.TORCH], frequency_min: int = 15, frequency_max: int = 15):
        super().__init__(mc, decorated)
        self.light_blocks = light_blocks
        self.frequency_min = frequency_min
        self.frequency_max = frequency_max
        self.counter = 0
        self.next_in = random.randint(self.frequency_min, self.frequency_max)

    def exec(self, rel: Rltv, builder_state: dict):
        self.decorated.exec(rel, builder_state)
        self.counter += 1
        if self.counter != self.next_in:
            return

        self.counter = 0
        self.next_in = random.randrange(self.frequency_min, self.frequency_max)

        strategy = self.get_decorated()

        light_block = self.light_blocks[random.randint(0, len(self.light_blocks) - 1)]
        if light_block in TunnelLight.torch:  # torch
            cur = rel.top(2).left(2)
            if strategy.flume.get_one(cur) is not None:
                strategy.flume.set_as_used(cur.right(1), light_block.withData(rel.get_torch_abs_direction(Rltv.RIGHT)))
            else:
                cur = rel.top(2).left(1)
                if strategy.flume.get_one(cur) in TunnelLight.stair:
                    strategy.flume.set_as_used(cur, light_block.withData(rel.get_torch_abs_direction(Rltv.RIGHT)))
                else:
                    strategy.flume.set_as_used(rel.top(2),
                                               light_block.withData(rel.get_torch_abs_direction(Rltv.RIGHT)))
        else:  # lighting block
            if strategy.flume.get_one(rel.top(4)) is not None:
                strategy.flume.set_as_used(rel.top(4), light_block)
            elif strategy.flume.get_one(rel.top(3)) is not None:
                strategy.flume.set_as_used(rel.top(3), light_block)
            elif strategy.flume.get_one(rel.left(1)) is not None:
                strategy.flume.set_as_used(rel.left(1), light_block)
            elif strategy.flume.get_one(rel.right(1)) is not None:
                strategy.flume.set_as_used(rel.right(1), light_block)
