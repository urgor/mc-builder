import mcpi_e.block as block
from mcpi_e.vec3 import Vec3
from datetime import datetime
import pickle
from typing import Generator
import Different.Relative as Relative

class Used:
    path_to_store = 'undo_history'
    all_used = {}

    def __init__(self, a: Vec3, b: Vec3, linear_data: map):
        """
        Constructor
        :param a: start pont of Minecraft.getBlocks()
        :param b: end pont of Minecraft.getBlocks()
        :param linear_data: result of Minecraft.getBlocks()
        """
        self.used = {}
        self.add(a, b, linear_data)

    def add(self, a: Vec3, b: Vec3, linear_data: map):
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
        map_list = list(linear_data)
        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                for z in range(min_z, max_z):
                    if x not in self.used:
                        self.used[x] = {}
                    if y not in self.used[x]:
                        self.used[x][y] = {}
                    self.used[x][y][z] = map_list[idx]
                    idx += 1
        idx = 0
        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                for z in range(min_z, max_z):
                    if x not in Used.all_used:
                        Used.all_used[x] = {}
                    if y not in Used.all_used[x]:
                        Used.all_used[x][y] = {}
                    Used.all_used[x][y][z] = map_list[idx]
                    idx += 1

    def get_one(self, rel: Relative) -> block.Block:
        """
        Get one block from currently used from game, not by us!
        :param rel: Relative position
        :return: Block ID
        """
        cur = rel.get_current()
        try:
            return block.Block(self.used[cur.x][cur.y][cur.z])
        except:
            return None

    def iterate_by_y(self, rel: Relative, step: int) -> Generator:
        cur = rel.get_current()
        min_y = min(self.used[cur.x].keys())
        max_y = max(self.used[cur.x].keys())
        current_rel = rel.top(0)
        for y in range(max_y, min_y - 1, step) if step < 0 else range(min_y, max_y + 1, step):
            current_rel.get_current().y = y
            yield current_rel, self.used[cur.x][y][cur.z]

    @staticmethod
    def store():
        pickled_data = pickle.dumps(Used.all_used)
        f = open(Used.path_to_store + '/' + datetime.now().strftime('%Y-%m-%d_%H:%M:%S') + '.bin', "wb")
        f.write(pickled_data)
        f.close()

    @staticmethod
    def raise_data(file_name):
        f = open(file_name, "rb")
        data = f.read()
        return pickle.loads(data)
