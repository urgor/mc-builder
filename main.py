import time, sys

from mcpi_e.minecraft import Minecraft
from mcpi_e.vec3 import Vec3
import mcpi_e.block as block


from Different.Relative import Relative
from Different.Style import Style
from Different.Used import Used
from ObjectLib.Railroad import Railroad
from ObjectLib.RailroadStrategy.PutBlockAndRail import PutBlockAndRail
from ObjectLib.RailroadStrategy.CheckDigAndPutRail import CheckDigAndPutRail
from ObjectLib.RailroadStrategy.ChickenStop import ChickenStop



import collections


collections.Iterable = collections.abc.Iterable # to prevent "AttributeError: module 'collections' has no attribute 'Iterable'"

serverAddress="127.0.0.1"
pythonApiPort=4711 #default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName="Urgorka" # change to your username

mc = Minecraft.create(serverAddress,pythonApiPort,playerName)

# playerPos.y+=15
# b = Block(mc)
# b.draw(playerPos, 60, 38, 60, block.AIR)

### Railroad
# relativePos = Relative(Vec3(238,8,-1260), 90)  # Vec3(-844,8,-1260) Polar station
relativePos = Relative(mc.player.getTilePos(), mc.player.getRotation())
length = 1100
a = relativePos.bottom(1).get_current()
b = relativePos.bottom(1).forward(length).get_current()
used = Used(a, b, mc.getBlocks(a, b))
style = Style()
style.bottom = block.BRICK_BLOCK.id
style.pillar = block.BRICK_BLOCK.id

rr = Railroad(mc, used)
rr.draw(
    relativePos,
    length,
    PutBlockAndRail(mc, used, style),
    ChickenStop(mc, used, style) # CheckDigAndPutRail(mc, used, style)
)

# style = Style()
# style.bottom = (block.BRICK_BLOCK.id)
# style.wall = (block.GLASS.id)
# style.filling = (block.AIR.id)
# d = Dome(mc)
# d.draw(playerPos, 10, style)

# r = Rainbow(mc)
# r.draw(playerPos, 25)

