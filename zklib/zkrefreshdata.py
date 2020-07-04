from struct import pack, unpack
from datetime import datetime, date

from .zkconst import *


def zkrefreshdata(self):
	"""Tell device to refresh data for transmisison"""
	command = CMD_REFRESHDATA

	reply_id = unpack('HHHH', self.data_recv[:8])[3]

	buf = self.createHeader(command, self.session_id, reply_id, b'')
	self.zkclient.sendto(buf,self.address)

	try:
		self.data_recv, addr = self.zkclient.recvfrom(1024)
		self.session_id = unpack('HHHH', self.data_recv[:8])[2]
		return self.data_recv[8:]
	except:
		return False
