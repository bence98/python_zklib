from struct import pack, unpack

from .zkconst import *

def zkunlock(self, delay):
    """Unlock door"""
    command = CMD_UNLOCK
    command_string = pack('I', delay).decode('ascii')
    chksum = 0
    session_id = self.session_id
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, chksum, session_id,
        reply_id, command_string)
    self.zkclient.sendto(buf, self.address)
    
    self.data_recv, addr = self.zkclient.recvfrom(1024)
    if unpack('4H', self.data_recv[:8])[0] == CMD_ACK_OK:
        return True

    return False
