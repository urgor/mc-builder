from mcpi_e import block

from Different.Relative import Relative
from Different.Used import Used
from ObjectLib.RailroadDecorator.AbstractDecorator import AbstractDecorator

class FlatSupport(AbstractDecorator):
    def exec(self, rel: Relative, builder_state: dict):
        self.decorated.exec(rel, builder_state)

        if builder_state['powered_rail_block']:
            self.pillar_support(rel)

    def pillar_support(self, rel: Relative):
        a = [  # ________*__<- rel here, on the top
            [1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 0, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
        ]
        cur_rel = rel.bottom(1).backward(4)
        strategy = self.get_decorated()
        for i in range(len(a)):
            for j in range(len(a[i])):
                if a[i][j] == 0:
                    continue
                strategy.flume.set_as_used(cur_rel.bottom(i).forward(j), strategy.style.pillar)
