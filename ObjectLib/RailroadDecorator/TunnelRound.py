from mcpi_e import block
from Different.Relative import Relative as Rltv
from ObjectLib.RailroadDecorator.AbstractDecorator import AbstractDecorator
from ObjectLib.RailroadStrategy.Tunnel9 import *

class TunnelRound(AbstractDecorator):
    glass = [block.GLASS, block.STAINED_GLASS, block.GLASS_PANE]
    def exec(self, rel: Rltv, builder_state: dict):
        self.decorated.exec(rel, builder_state)
        strategy = self.get_decorated()

        cur = rel.top(1).left(1)
        if strategy.flume.get_one(cur) == block.AIR and strategy.flume.get_one(cur.left(1)) not in TunnelRound.glass:
            strategy.flume.set_as_used(cur, strategy.style.rounding.withData(rel.get_stairs_abs_direction(Rltv.UP_RIGHT)))

        cur = rel.top(1).right(1)
        if strategy.flume.get_one(cur) == block.AIR and strategy.flume.get_one(cur.right(1)) not in TunnelRound.glass:
            strategy.flume.set_as_used(cur, strategy.style.rounding.withData(rel.get_stairs_abs_direction(Rltv.UP_LEFT)))
        if isinstance(strategy, Tunnel9):
            cur = rel.top(3).left(1)
            if strategy.flume.get_one(cur) == block.AIR and strategy.flume.get_one(cur.left(1)) not in TunnelRound.glass\
                    and strategy.flume.get_one(cur.top(1)) not in TunnelRound.glass:
                strategy.flume.set_as_used(cur, strategy.style.rounding.withData(rel.get_stairs_abs_direction(Rltv.DOWN_RIGHT)))

            cur = rel.top(3).right(1)
            if strategy.flume.get_one(cur) == block.AIR and strategy.flume.get_one(cur.right(1)) not in TunnelRound.glass\
                    and strategy.flume.get_one(cur.top(1)) not in TunnelRound.glass:
                strategy.flume.set_as_used(cur, strategy.style.rounding.withData(rel.get_stairs_abs_direction(Rltv.DOWN_LEFT)))
        else :
            # in case of Tunnel6 when it is 3x2
            cur = rel.top(2).left(1)
            if strategy.flume.get_one(cur) == block.AIR and strategy.flume.get_one(cur.left(1)) not in TunnelRound.glass\
                    and strategy.flume.get_one(cur.top(1)) not in TunnelRound.glass:
                strategy.flume.set_as_used(cur, strategy.style.rounding.withData(rel.get_stairs_abs_direction(Rltv.DOWN_RIGHT)))

            cur = rel.top(2).right(1)
            if strategy.flume.get_one(cur) == block.AIR and strategy.flume.get_one(cur.right(1)) not in TunnelRound.glass\
                    and strategy.flume.get_one(cur.top(1)) not in TunnelRound.glass:
                strategy.flume.set_as_used(cur, strategy.style.rounding.withData(rel.get_stairs_abs_direction(Rltv.DOWN_LEFT)))

