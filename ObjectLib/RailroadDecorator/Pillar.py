from mcpi_e import block

from Different.Relative import Relative
from Different.Used import Used
from ObjectLib.RailroadDecorator.AbstractDecorator import AbstractDecorator
from ObjectLib.RailroadStrategy.PutBlockAndRail import PUT_POWERED_EACH


class Pillar(AbstractDecorator):

    def exec(self, rel: Relative):
        self.decorated.exec(rel)

        if self.get_decorated().flag['powered_rail_block']:
            self.build_pillar(rel)

    def build_pillar(self, rel: Relative):
        pillars_top_rel = rel.bottom(3)
        a = pillars_top_rel.get_current()
        b = rel.bottom(100).get_current()
        pilar_used = Used(a, b, self.mc.getBlocks(a, b))
        print(a)
        for pillar_block_rel, block_id in pilar_used.iterate_by_y(pillars_top_rel, -1):
            print(pillar_block_rel, block_id)
            if block_id in [block.AIR.id, block.WATER.id]:
                self.get_decorated().used.set_as_used(pillar_block_rel, self.decorated.style.pillar)
            else:
                break
