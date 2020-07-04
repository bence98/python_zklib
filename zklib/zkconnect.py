from struct import pack, unpack
from datetime import datetime, date

from .zkconst import *

def zkconnect(self):
    """Start a connection with the time clock"""
    command = CMD_CONNECT
    # reply_id = -1 + USHRT_MAX
    reply_id = 0

    buf = self.createHeader(command, self.session_id, reply_id, b'')


    self.zkclient.sendto(buf, self.address)

    try:
        self.data_recv, addr = self.zkclient.recvfrom(1024)
        self.session_id = unpack('HHHH', self.data_recv[:8])[2]
        return self.checkValid( self.data_recv )
    except:
        return False


def zkdisconnect(self):
    """Disconnect from the clock"""
    command = CMD_EXIT
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, self.session_id, reply_id, b'')

    self.zkclient.sendto(buf, self.address)

    self.data_recv, addr = self.zkclient.recvfrom(1024)
    return self.checkValid( self.data_recv )

