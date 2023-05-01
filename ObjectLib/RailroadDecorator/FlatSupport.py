from mcpi_e import block

from Different.Relative import Relative
from Different.Used import Used
from ObjectLib.RailroadDecorator.AbstractDecorator import AbstractDecorator
from ObjectLib.RailroadStrategy.PutBlockAndRail import PUT_POWERED_EACH


class FlatSupport(AbstractDecorator):
    def exec(self, rel: Relative):
        self.decorated.exec(rel)

        if self.get_decorated().flag['powered_rail_block']:
            self.pillar_support(rel)

    def pillar_support(self, rel: Relative):
        a = [  # ________*__<- rel here, on the top
            [1, 0, 0, 1, 0, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
        ]
        cur_rel = rel.bottom(1).backward(4)
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == 0:
                    continue
                strategy = self.get_decorated()
                strategy.used.set_as_used(cur_rel.bottom(i).forward(j), strategy.style.pillar)
