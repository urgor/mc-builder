from mcpi.block import *
from Different.Flume import Flume
from Different.Relative import Relative
from Different.Used import Used


class VerticalQR():
    """
    Draw vertical standing QR code in front of player
    """
    def __init__(self, mc):
        self.mc = mc

    def draw(self, text):
        position = Relative(self.mc.player.getTilePos(), self.mc.player.getRotation())
        import qrcode
        qr = qrcode.QRCode()
        qr.add_data(text)
        m = qr.get_matrix()
        row = position.forward(1)

        flume = Flume(self.mc)
        a = row.get_current()
        b = row.forward(len(m)).top(len(m)).get_current()
        used = Used(a, b, self.mc.getBlocks(a, b))

        for j in m[-1::-1]:
            column = row
            for item in j:
                flume.set_as_used(column, QUARTZ_BLOCK if item else COAL_BLOCK)
                column = column.forward(1)
            row = row.top(1)
        flume.flush_to_mc()
        used.store()