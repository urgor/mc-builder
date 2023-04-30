from math import *
import mcpi_e.block as block

class Dome():

    def __init__(self, mc):
        self.mc = mc
        self.used={
            'wall': {},
            'bottom': {},
            'filling': {}
        }

    def draw(self, center, radius, style):
        if style.bottom is not None:
            self.calculate_bottom(center, radius, style)

        self.calculate_wall(center, radius, style)

        if style.filling is not None:
            self.calculate_filling(center, radius, style)

        self.visualize(self.used['wall'], style.wall)
        if style.bottom is not None:
            self.visualize(self.used['bottom'], style.bottom)

        if style.filling is not None and style.filling == block.AIR.id:
            self.visualize(self.used['filling'], block.COBBLESTONE.id)
        self.visualize(self.used['filling'], style.filling)


        print("dome created at x:{} y:{} z:{}".format(center.x, center.y, center.z))

    def visualize(self, dict, *args):
        for pos in dict.keys():
            [x, y, z] = pos.split('!')
            self.mc.setBlock(int(x), int(y), int(z), *args)

    def draw_circle(self, center, current_radius, y, key, *args):
        y += center.y
        for a in range(0, 360):
            z = center.z + round(sin(radians(a)) * (current_radius))
            x = center.x + round(cos(radians(a)) * (current_radius))
            pos = f'{x}!{y}!{z}'
            if pos in self.used['wall'] or pos in self.used['bottom'] or pos in self.used['filling'] :
                continue
            self.used[key][pos] = args

    def calculate_bottom(self, center, radius, style):
        b = 0  # angle towards horizont
        y = round(sin(radians(b)) * (radius))
        current_radius = round(cos(radians(b)) * (radius))
        for r in range(0, current_radius):
            self.draw_circle(center, r, y, 'bottom', style.bottom)

    def calculate_wall(self, center, radius, style):
        for b in range(0, 90): # angle towards horizont
            y = round(sin(radians(b)) * (radius))
            current_radius = round(cos(radians(b)) * (radius))
            self.draw_circle(center, current_radius, y, 'wall', style.wall)

    def calculate_filling(self, center, radius, style):
        for b in range(90, 0, -1): # angle towards horizont
            y = round(sin(radians(b)) * (radius))
            current_radius = round(cos(radians(b)) * (radius))
            for r in range(0, current_radius):
                self.draw_circle(center, r, y, 'filling', style.filling)
