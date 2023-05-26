
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
        super().set_as_used(rel, block_id, args)
        self.mc.setBlock(rel.get_current(), block_id, args)

        def flush_to_mc_yxz(self):
            pass

        def flush_to_mc(self):
            pass
