from mcpi_e.block import *
from Different.Flume import Flume
from Different.Relative import Relative
from Different.Used import Used


class GroundedQR():
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

        flume = Flume(self.mc)
        a = position.bottom(30).get_current()
        b = position.forward(len(m)).right(len(m)).top(30).get_current()
        used = Used(a, b, self.mc.getBlocks(a, b))

        row = position
        for j in m:
            current_pos = row
            for item in j:
                for pos_rel, block_id in used.iterate_by_y(current_pos, -1):
                    if block_id in (37,38,39,175,6,31,32):
                        flume.set_as_used(pos_rel, AIR)
                    elif block_id != AIR.id:
                        flume.set_as_used(pos_rel, 155 if item else 173) # Quartz Block || Block of Coal
                        break
                current_pos = current_pos.forward(1)
            row = row.right(1)
        flume.flush_to_mc()
        used.store()
