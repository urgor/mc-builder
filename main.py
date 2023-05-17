import time, sys

from mcpi_e.minecraft import Minecraft
from mcpi_e.vec3 import Vec3
import mcpi_e.block as block
from mcpi_e.block import Block

from Different.Relative import Relative
from Different.Style import Style
from Different.Used import Used
from ObjectLib.Railroad import Railroad
from ObjectLib.RailroadStrategy.PutBlockAndRail import PutBlockAndRail
from ObjectLib.RailroadStrategy.CheckDigAndPutRail import CheckDigAndPutRail
from ObjectLib.RailroadStrategy.ChickenStop import ChickenStop
from ObjectLib.RailroadDecorator.Pillar import Pillar
from ObjectLib.RailroadDecorator.FlatSupport import FlatSupport
from ObjectLib.RailroadDecorator.CorniceSupport import CorniceSupport
from Different.Color import *
from Different.Direction import *

import collections

collections.Iterable = collections.abc.Iterable  # to prevent "AttributeError: module 'collections' has no attribute 'Iterable'"

serverAddress = "127.0.0.1"
pythonApiPort = 4711  # default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName = "Urgorka"  # change to your username

mc = Minecraft.create(serverAddress, pythonApiPort, playerName)

# pos = mc.player.getTilePos()
# rot = mc.player.getRotation()
# print (pos, rot)
# sys.exit()

### Railroad
relativePosA = Relative(Vec3(275,8,-1260), -91.02582)
relativePosB = Relative(Vec3(1180,8,-1260), 89.27374)

a = relativePosA.bottom(1)
b = relativePosB
used = Used(a.get_current(), a.get_current(), mc.getBlocks(a.get_current(), a.get_current()))
style = Style()
style.bottom = block.STONE_BRICK.id
style.pillar = block.STONE_BRICK.id
style.cornice = block.STAIRS_STONE_BRICK

rr = Railroad(mc, used, style)
rr.draw(
    a,
    b,
    CorniceSupport(mc, (Pillar(mc, PutBlockAndRail(mc, used, style)))),
    ChickenStop(mc, used, style)  # CheckDigAndPutRail(mc, used, style)
)

# @todo main strategy for env: air, water, stone
# @todo decorators for main strategy: tone

# style = Style()
# style.bottom = (block.BRICK_BLOCK.id)
# style.wall = (block.GLASS.id)
# style.filling = (block.AIR.id)
# d = Dome(mc)
# d.draw(playerPos, 10, style)

# r = Rainbow(mc)
# r.draw(playerPos, 25)
