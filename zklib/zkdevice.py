from struct import pack, unpack
from datetime import datetime, date

from .zkconst import *

def zkdevicename(self):
    """Start a connection with the time clock"""
    command = CMD_DEVICE
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, self.session_id, reply_id, b'~DeviceName')
    self.zkclient.sendto(buf, self.address)
    #print buf.encode("hex")
    try:
        self.data_recv, addr = self.zkclient.recvfrom(1024)
        self.session_id = unpack('HHHH', self.data_recv[:8])[2]
        return (self.data_recv[8:]).decode("ascii")
    except:
        return False

def zkpoweroff(self):
    """Start a connection with the time clock"""
    command = CMD_POWEROFF
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, self.session_id, reply_id, b'')
    self.zkclient.sendto(buf, self.address)
    #print buf.encode("hex")
    try:
        self.data_recv, addr = self.zkclient.recvfrom(1024)
        self.session_id = unpack('HHHH', self.data_recv[:8])[2]
        return self.data_recv[8:]
    except:
        return False

def zkrestart(self):
    """Start a connection with the time clock"""
    command = CMD_RESTART
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, self.session_id, reply_id, b'')
    self.zkclient.sendto(buf, self.address)
    #print buf.encode("hex")
    try:
        self.data_recv, addr = self.zkclient.recvfrom(1024)
        self.session_id = unpack('HHHH', self.data_recv[:8])[2]
        return self.data_recv[8:]
    except:
        return False

def zkenabledevice(self):
    """Start a connection with the time clock"""
    command = CMD_ENABLEDEVICE
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, self.session_id, reply_id, b'')
    self.zkclient.sendto(buf, self.address)
    #print buf.encode("hex")
    try:
        self.data_recv, addr = self.zkclient.recvfrom(1024)
        self.session_id = unpack('HHHH', self.data_recv[:8])[2]
        return (self.data_recv[8:]).decode("ascii")
    except:
        return False

def zkdisabledevice(self):
    """Start a connection with the time clock"""
    command = CMD_DISABLEDEVICE
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, self.session_id, reply_id, b'\x00\x00')
    self.zkclient.sendto(buf, self.address)
    #print buf.encode("hex")
    try:
        self.data_recv, addr = self.zkclient.recvfrom(1024)
        self.session_id = unpack('HHHH', self.data_recv[:8])[2]
        return (self.data_recv[8:]).decode("ascii")
    except:
        return False
