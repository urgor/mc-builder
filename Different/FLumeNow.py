
from mcpi_e.minecraft import Minecraft
from typing import Generator
from Different.Relative import *
from Different.Flume import *


class FlumeNow(Flume):

    def set_as_used(self, rel: Relative, block_id: int, *args):
        """
        Set block as used by us, to draw it in the future
        :param rel: Relative position
        :param block_id: Block ID
        :return:
        """
        self.mc.setBlock(rel.get_current(), block_id, args)
        print(block_id)

    def iterate_by_new(self) -> Generator:
        """
        Iterate by new block set by us, to draw them
        :return:
        """
        return iter(())

    def iterate_by_new_ordered(self) -> Generator:
        """
        Iterate by new block set by us, to draw them
        :return:
        """
        return iter(())