from mcpi_e.minecraft import Minecraft

from Different import Used, Style, Relative


class Strategy:
    def __init__(self, mc: Minecraft, used: Used, style: Style):
        self.used = used
        self.style = style
        self.mc = mc

    def exec(self, rel: Relative):
        pass

    