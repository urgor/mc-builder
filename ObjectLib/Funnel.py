from math import *
from mcpi_e.block import *
from math import log
from Different.Flume import Flume
from Different.Relative import Relative
from Different.Used import Used
from mcpi_e.vec3 import Vec3


class Funnel():

    def __init__(self, mc):
        self.mc = mc
        self.flume = None

    def draw(self, center: Relative, radius_start: int, radius_end: int, depth: int):
        self.flume = Flume(self.mc)
        a = center.forward(radius_start).left(radius_start).get_current()
        b = center.backward(radius_start).right(radius_start).bottom(depth).get_current()
        used = Used(a, b, self.mc.getBlocks(a, b))

        y0 = 1 / radius_start
        y1 = 1 / radius_end
        k = 100
        y = y0
        y_shift_initial = int(y * k)
        while y < y1:
            r = 1 / y
            y_shift = int(y * k) - y_shift_initial
            current_center = center.bottom(y_shift)
            self.draw_circle(current_center, r, 'wall', STONEBRICK_STONE)
            y += 0.005

        for r in range(y_shift, depth+1):
            self.draw_circle(current_center, radius_end, 'wall', STONEBRICK_STONE)
            current_center = current_center.bottom(1)

        used.store()
        self.flume.flush_to_mc()

    def calculate_wall(self, center, radius):
        for b in range(0, 90): # angle towards horizont
            y = round(sin(radians(b)) * (radius))
            current_radius = round(cos(radians(b)) * (radius))
            self.draw_circle(center, current_radius, y, 'wall', STONE)

    def visualize(self, dict, *args):
        for pos in dict.keys():
            [x, y, z] = pos.split('!')
            self.mc.setBlock(int(x), int(y), int(z), *args)

    def draw_circle(self, center, current_radius, key, *args):
        o = center.get_current()
        y = o.y
        for a in range(0, 360):
            z = o.z + round(sin(radians(a)) * (current_radius))
            x = o.x + round(cos(radians(a)) * (current_radius))
            self.flume.set_as_used(Relative(Vec3(x, y, z), 0), args)

    def calculate_bottom(self, center, radius, style):
        b = 0  # angle towards horizont
        y = round(sin(radians(b)) * (radius))
        current_radius = round(cos(radians(b)) * (radius))
        for r in range(0, current_radius):
            self.draw_circle(center, r, y, 'bottom', style.bottom)


    def calculate_filling(self, center, radius, style):
        for b in range(90, 0, -1): # angle towards horizont
            y = round(sin(radians(b)) * (radius))
            current_radius = round(cos(radians(b)) * (radius))
            for r in range(0, current_radius):
                self.draw_circle(center, r, y, 'filling', style.filling)
