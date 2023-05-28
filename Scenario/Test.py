from mcpi_e.minecraft import Minecraft
from mcpi_e.vec3 import Vec3
import mcpi_e.block as block
from mcpi_e.block import Block

from ObjectLib.Railroad import Railroad
from ObjectLib.RailroadStrategy.Tunnel9 import *
from ObjectLib.RailroadStrategy.Tunnel6 import *
from ObjectLib.RailroadStrategy.DoNothing import *
from ObjectLib.RailroadDecorator.Pillar import Pillar
from ObjectLib.RailroadDecorator.FlatSupport import FlatSupport
from ObjectLib.RailroadDecorator.CorniceSupport import CorniceSupport
from ObjectLib.RailroadDecorator.TunnelRound import *
from ObjectLib.RailroadDecorator.TunnelLight import *
from ObjectLib.Block import Block as MaBlock
from Different.Relative import *
from Different.Style import *
from Different.Flume import *
from Different.FLumeNow import *
from Different.Used import *


class Test:
    def __init__(self, mc: Minecraft):
        self.mc = mc

    def exec(self):
        # patch world by stone block
        # cur = Relative.Relative(self.mc.player.getTilePos(), self.mc.player.getRotation())
        # a = cur.forward(1).left(4).bottom(1)
        # b = a.top(4).right(4).forward(100)
        # u1 = Used(a.get_current(), b.get_current(),  self.mc.getBlocks(a.get_current(), b.get_current()))
        # MaBlock(self.mc).draw_ab(a.get_current(), b.get_current(), block.DIRT.id)
        # return

        # get and print block
        # cur = self.mc.player.getTilePos()
        # blk = self.mc.getBlock(cur)
        # print('block', blk)
        # return

        ### Railroad
        relativePos = Relative.Relative(self.mc.player.getTilePos(), self.mc.player.getRotation())

        a = relativePos.bottom(1).forward(1)
        b = a.forward(100)

        style = Style(bottom=block.STONE_BRICK.id, pillar=block.STONE_BRICK.id, cornice=block.STAIRS_STONE_BRICK)
        tunnel_style = Style(top=block.STONE_BRICK.id, wall=block.STONE_BRICK.id, corner=block.STAIRS_STONE_BRICK.id,
                             rounding=block.STAIRS_STONE_BRICK)

        flume = Flume(self.mc)
        # flume = FlumeNow(self.mc)

        rr = Railroad(self.mc, style, flume)
        # rr.set_strategy_for_air(CorniceSupport(mc, (Pillar(mc, DoNothing(mc, style, flume)))))
        # rr.set_strategy_for_tunnel(TunnelRound(self.mc, Tunnel9(self.mc, tunnel_style, flume)))
        # rr.set_strategy_for_tunnel(TunnelRound(self.mc, Tunnel6(self.mc, tunnel_style, flume)))
        light_blocks = [
            block.GLOWSTONE_BLOCK,
            block.TORCH
        ]
        strategy = Tunnel6(self.mc, tunnel_style, flume)
        strategy_decorated = TunnelLight(self.mc, strategy, light_blocks=light_blocks, frequency_min=5, frequency_max=20)
        rr.set_strategy_for_tunnel(strategy_decorated)

        rr.draw(a, b)

        # @todo main strategy for env: air, water, stone

        # style = Style()
        # style.bottom = (block.BRICK_BLOCK.id)
        # style.wall = (block.GLASS.id)
        # style.filling = (block.AIR.id)
        # d = Dome(mc)
        # d.draw(playerPos, 10, style)

        # r = Rainbow(mc)
        # r.draw(playerPos, 25)

        flume.flush_to_mc()
