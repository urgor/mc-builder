from math import *
import mcpi_e.block as block
from mcpi_e.vec3 import Vec3

class Block:
    def __init__(self, mc):
        self.mc = mc

    def draw(self, center, x, y, z, block_type):
        half_x = int(x/2)
        half_y = int(y/2)
        half_z = int(z/2)
        self.mc.setBlocks(
            center.x - half_x, center.y - half_y, center.z - half_z,
            center.x + half_x, center.y + half_y, center.z + half_z,
            block_type.id
        )
        print("block created at x:{} y:{} z:{}".format(center.x, center.y, center.z))

    def draw_ab(self, a: Vec3, b: Vec3, id: int):
        self.mc.setBlocks(a.x, a.y, a.z, b.x, b.y, b.z, id)

    def erase(self, center, x, y, z):
        half_x = int(x/2)
        half_y = int(y/2)
        half_z = int(z/2)
        self.mc.setBlocks(
            center.x - half_x, center.y - half_y, center.z - half_z,
            center.x + half_x, center.y + half_y, center.z + half_z,
            block.AIR.id
        )
        print("block erased at x:{} y:{} z:{}".format(center.x, center.y, center.z))
