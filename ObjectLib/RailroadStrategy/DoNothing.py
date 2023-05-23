from Different.Relative import *
from ObjectLib.RailroadStrategy.AbstractStrategy import AbstractStrategy


class DoNothing(AbstractStrategy):
    """
    Do nothing.
    """
    def exec(self, rel: Relative, builder_state: dict):
        pass
