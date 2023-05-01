import time
from typing import Generator

from mcpi_e.vec3 import Vec3
import Different.Relative as Relative


class Used:
    def __init__(self, a: Vec3, b: Vec3, map: map):
        """
        Constructor
        :param a: start pont of Minecraft.getBlocks()
        :param b: end pont of Minecraft.getBlocks()
        :param map: result of Minecraft.getBlocks()
        """
        self.new = {}
        self.used = {}
        self.min_y = 0
        self.max_y = 0
        self.min_x = 0
        self.max_x = 0
        xx = [a.x, b.x]
        yy = [a.y, b.y]
        zz = [a.z, b.z]
        min_x = min(xx)
        max_x = max(xx) + 1
        min_y = min(yy)
        max_y = max(yy) + 1
        min_z = min(zz)
        max_z = max(zz) + 1
        idx = 0
        map_list = list(map)
        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                for z in range(min_z, max_z):
                    if x not in self.used:
                        self.used[x] = {}
                    if y not in self.used[x]:
                        self.used[x][y] = {}
                    self.used[x][y][z] = map_list[idx]
                    idx += 1

    def get_one(self, rel: Relative) -> int:
        """
        Get one block from currently used from game, not by us!
        :param rel: Relative position
        :return: Block ID
        """
        cur = rel.get_current()
        try:
            return self.used[cur.x][cur.y][cur.z]
        except:
            return None

    def set_as_used(self, rel: Relative, block_id: int, *args):
        """
        Set block as used by us, to draw it in the future
        :param rel: Relative position
        :param block_id: Block ID
        :return:
        """
        if block_id is None:
            raise Exception('zzz')
        cur = rel.get_current()

        if cur.x not in self.new:
            self.new[cur.x] = {}
        if cur.y not in self.new[cur.x]:
            self.new[cur.x][cur.y] = {}
        self.new[cur.x][cur.y][cur.z] = (block_id, *args)
        self.min_y = min([self.min_y, cur.y])
        self.max_y = max([self.max_y, cur.y])
        self.min_x = min([self.min_x, cur.x])
        self.max_x = max([self.max_x, cur.x])

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

    def iterate_by_y(self, rel: Relative, step: int) -> Generator:
        cur = rel.get_current()
        min_y = min(self.used[cur.x].keys())
        max_y = max(self.used[cur.x].keys())
        current_rel = rel.top(0)
        for y in range(max_y, min_y + 1, step) if step < 0 else range(min_y, max_y + 1, step):
            current_rel.get_current().y = y
            yield current_rel, self.used[cur.x][y][cur.z]
