from mcpi_e import block
from mcpi_e.minecraft import Minecraft
from typing import Generator
from Different.Relative import *


class Flume:
    def __init__(self, mc: Minecraft):
        self.mc = mc
        self.new = {}
        self.order = []
        self.used = {}
        self.min_y = 0
        self.max_y = 0
        self.min_x = 0
        self.max_x = 0

    def set_as_used(self, rel: Relative, block_obj: int | block.Block):
        """
        Set block as used by us, to draw it in the future
        :param rel: Relative position
        :param block_obj: Block ID
        :return:
        """
        cur = rel.get_current()

        if cur.x not in self.new:
            self.new[cur.x] = {}
        if cur.y not in self.new[cur.x]:
            self.new[cur.x][cur.y] = {}
        self.new[cur.x][cur.y][cur.z] = block.Block(block_obj) if isinstance(block_obj, int) else block_obj
        self.min_y = min([self.min_y, cur.y])
        self.max_y = max([self.max_y, cur.y])
        self.min_x = min([self.min_x, cur.x])
        self.max_x = max([self.max_x, cur.x])

        self.order.append(deepcopy(cur))

    def set_raw_data(self, data: dict):
        """
        Populate internal array from 3D array of Used data which could be serialized and deserialized then.
        :param data:
        :return:
        """
        x_min = min(data.keys())
        x_max = max(data.keys()) + 1
        for x in range(x_min, x_max):
            y_min = min(data[x].keys())
            y_max = max(data[x].keys()) + 1
            for y in range(y_min, y_max):
                z_min = min(data[x][y].keys())
                z_max = max(data[x][y].keys()) + 1
                for z in range(z_min, z_max):
                    if x not in data or y not in data[x] or z not in data[x][y]:
                        continue
                    self.set_as_used(Relative(Vec3(x, y, z), 0), data[x][y][z])

    def iterate_by_new(self) -> Generator:
        """
        Iterate by new block set by us, to draw them
        :return:
        """
        if not self.new:
            return iter(())
        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                if x not in self.new:
                    continue
                if y not in self.new[x]:
                    continue
                min_z = min(self.new[x][y].keys())
                max_z = max(self.new[x][y].keys())
                for z in range(min_z, max_z + 1):
                    if z not in self.new[x][y]:
                        continue
                    yield Vec3(x, y, z), self.new[x][y][z]

    def iterate_by_new_ordered(self) -> Generator:
        """
        Iterate by new block set by us, to draw them
        :return:
        """
        if not self.new:
            return iter(())
        for vec in self.order:
            yield vec, self.new[vec.x][vec.y][vec.z]

    def flush_to_mc_yxz(self):
        for (vec, block_id) in self.iterate_by_new():
            self.mc.setBlock(vec, block_id)

    def flush_to_mc(self):
        # for (vec, block_id) in self.used.iterate_by_new():
        for (vec, block_id) in self.iterate_by_new_ordered():
            self.mc.setBlock(vec, block_id)

    def get_one(self, rel: Relative) -> block.Block:
        """
        Get one block from currently used from game, not by us!
        :param rel: Relative position
        :return: Block ID
        """
        cur = rel.get_current()
        try:
            return self.new[cur.x][cur.y][cur.z]
        except:
            return None
