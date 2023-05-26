from mcpi_e import block

from Different.Relative import Relative as Rltv
from Different.Used import Used
from ObjectLib.RailroadDecorator.AbstractDecorator import AbstractDecorator
from Different.Direction import *


class TunnelRound(AbstractDecorator):
    glass = [block.GLASS.id, block.STAINED_GLASS.id, block.GLASS_PANE.id]
    def exec(self, rel: Rltv, builder_state: dict):
        self.decorated.exec(rel, builder_state)
        strategy = self.get_decorated()

        cur = rel.top(1).left(1)
        if strategy.flume.get_one(cur) == block.AIR.id and strategy.flume.get_one(cur.left(1)) not in TunnelRound.glass:
            strategy.flume.set_as_used(cur, strategy.style.rounding.withData(rel.get_abs_direction(Rltv.UP_RIGHT)))

        cur = rel.top(1).right(1)
        if strategy.flume.get_one(cur) == block.AIR.id and strategy.flume.get_one(cur.right(1)) not in TunnelRound.glass:
            strategy.flume.set_as_used(cur, strategy.style.rounding.withData(rel.get_abs_direction(Rltv.UP_LEFT)))

        cur = rel.top(3).left(1)
        if strategy.flume.get_one(cur) == block.AIR.id and strategy.flume.get_one(cur.left(1)) not in TunnelRound.glass:
            strategy.flume.set_as_used(cur, strategy.style.rounding.withData(rel.get_abs_direction(Rltv.DOWN_RIGHT)))

        cur = rel.top(3).right(1)
        if strategy.flume.get_one(cur) == block.AIR.id and strategy.flume.get_one(cur.right(1)) not in TunnelRound.glass:
            strategy.flume.set_as_used(cur, strategy.style.rounding.withData(rel.get_abs_direction(Rltv.DOWN_LEFT)))

