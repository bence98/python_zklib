from struct import pack, unpack
from datetime import datetime, date

from .zkconst import *

def zkplatform(self):
    """Start a connection with the time clock"""
    command = CMD_DEVICE
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, self.session_id, reply_id, b'~Platform')
    self.zkclient.sendto(buf, self.address)
    #print buf.encode("hex")
    try:
        self.data_recv, addr = self.zkclient.recvfrom(1024)
        self.session_id = unpack('HHHH', self.data_recv[:8])[2]
        return (self.data_recv[8:]).decode("ascii")
    except:
        return False


def zkplatformVersion(self):
    """Start a connection with the time clock"""
    command = CMD_DEVICE
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, self.session_id, reply_id, b'~ZKFPVersion')
    self.zkclient.sendto(buf, self.address)
    #print buf.encode("hex")
    try:
        self.data_recv, addr = self.zkclient.recvfrom(1024)
        self.session_id = unpack('HHHH', self.data_recv[:8])[2]
        return (self.data_recv[8:]).decode("ascii")
    except:
        return False
