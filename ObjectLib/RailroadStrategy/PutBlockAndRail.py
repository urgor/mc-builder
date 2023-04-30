from mcpi_e.minecraft import Minecraft
import mcpi_e.block as block
from ObjectLib.RailroadStrategy.Strategy import Strategy
from Different import Used, Style, Relative
from Different.Used import Used


class PutBlockAndRail(Strategy):
    PUT_POWERED_EACH = 25
    def __init__(self, mc: Minecraft, used: Used, style: Style):
        super().__init__(mc, used, style)
        self.iteration = 0

    def exec(self, rel: Relative):
        self.used.set_as_used(rel, self.style.bottom)
        self.iteration += 1
        if self.iteration == self.PUT_POWERED_EACH:
            self.iteration = 0
            self.used.set_as_used(rel.top(1), block.RAIL_POWERED.id)
            self.used.set_as_used(rel.bottom(1), block.TORCH_REDSTONE.id)
            self.used.set_as_used(rel.bottom(2), self.style.bottom)

            last_pillar_block = self.build_pillar(rel)
            if rel.bottom(3).get_current().y - last_pillar_block.get_current().y > 3:
                self.pillar_support(rel)
        else:
            self.used.set_as_used(rel.top(1), block.RAIL.id)

    def pillar_support(self, rel: Relative):
        a = [  #         0 <- rel here
            [1, 0, 0, 1, 0, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
        ]
        cur_rel = rel.bottom(1).backward(4)
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == 0:
                    continue
                self.used.set_as_used(cur_rel.bottom(i).forward(j), self.style.pillar)


    def build_pillar(self, rel: Relative) -> Relative:
        last_pillar_block_rel = pillars_top_rel = rel.bottom(3)
        a = pillars_top_rel.get_current()
        b = rel.bottom(100).get_current()
        pilar_used = Used(a, b, self.mc.getBlocks(a, b))
        for pillar_block_rel, id in pilar_used.iterate_by_y(pillars_top_rel, -1):
            last_pillar_block_rel = pillar_block_rel
            if id in [block.AIR.id, block.WATER.id]:
                self.used.set_as_used(pillar_block_rel, self.style.pillar)
            else:
                break
        return last_pillar_block_rel
