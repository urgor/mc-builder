from Different.Relative import Relative
from ObjectLib.RailroadDecorator.AbstractDecorator import AbstractDecorator
from Different.Direction import *

class CorniceSupport(AbstractDecorator):
    def exec(self, rel: Relative, builder_state: dict):
        self.decorated.exec(rel, builder_state)

        if builder_state['powered_rail_block']:
            self.pillar_support(rel)

    def pillar_support(self, rel: Relative):
        strategy = self.get_decorated()
        cur_rel = rel.bottom(1)
        strategy.flume.set_as_used(cur_rel.north(1).east(1), strategy.style.cornice.withData(DOWN_NORTH))
        strategy.flume.set_as_used(cur_rel.south(1).east(1), strategy.style.cornice.withData(DOWN_SOUTH))
        strategy.flume.set_as_used(cur_rel.south(1).west(1), strategy.style.cornice.withData(DOWN_WEST))
        strategy.flume.set_as_used(cur_rel.north(1).west(1), strategy.style.cornice.withData(DOWN_NORTH))
        strategy.flume.set_as_used(cur_rel.north(1), strategy.style.cornice.withData(DOWN_NORTH))
        strategy.flume.set_as_used(cur_rel.east(1), strategy.style.cornice.withData(DOWN_EAST))
        strategy.flume.set_as_used(cur_rel.south(1), strategy.style.cornice.withData(DOWN_SOUTH))
        strategy.flume.set_as_used(cur_rel.west(1), strategy.style.cornice.withData(DOWN_WEST))
