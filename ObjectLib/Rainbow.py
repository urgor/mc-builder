from math import *
import mcpi_e.block as block

class Rainbow():
    colors = [14, 1, 4, 5, 3, 11, 10]

    def __init__(self, mc):
        self.mc = mc

    def draw(self, playerPos, radius, respect_block=True):
        for a in range(0, 180):
            for colour_index in range(0, len(self.colors)):
                y = playerPos.y + sin(radians(a)) * (radius + colour_index)
                z = playerPos.z + cos(radians(a)) * (radius + colour_index)
                self.mc.setBlock(playerPos.x, int(y), int(z), block.STAINED_GLASS.id, self.colors[len(self.colors) - 1 - colour_index])
                # self.mc.setBlock(int(x), int(y), playerPos.z, block.STAINED_GLASS.id, self.colors[len(self.colors) - 1 - colour_index])
        print("rainbow created at x:{} y:{} z:{}".format(playerPos.x, playerPos.y, playerPos.z))

    def erase(self, playerPos, radius):
        for a in range(0, 180):
            for colour_index in range(0, len(self.colors)):
                y = playerPos.y + sin(radians(a)) * (radius + colour_index)
                x = playerPos.x + cos(radians(a)) * (radius + colour_index)
                self.mc.setBlock(int(x), int(y), playerPos.z, block.AIR.id)
        print("rainbow erased at x:{} y:{} z:{}".format(playerPos.x, playerPos.y, playerPos.z))
