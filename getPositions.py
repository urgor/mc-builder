from mcpi_e.minecraft import Minecraft
from Different.Relative import Relative

import collections
collections.Iterable = collections.abc.Iterable  # to prevent "AttributeError: module 'collections' has no attribute 'Iterable'"

serverAddress = "127.0.0.1"
pythonApiPort = 4711  # default port for RaspberryJuice plugin is 4711, it could be changed in plugins\RaspberryJuice\config.yml
playerName = "Urgorka"  # change to your username

mc = Minecraft.create(serverAddress, pythonApiPort, playerName)

while True:
    pos = mc.player.getTilePos()
    rot = mc.player.getRotation()
    print(pos, rot)
    data = input("Press enter:\n")