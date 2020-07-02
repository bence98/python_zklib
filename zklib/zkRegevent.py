from struct import pack, unpack
from datetime import datetime, date
import sys

from .zkconst import *

def reverseHex(hexstr):
    tmp = ''
    for i in reversed( range( len(hexstr)/2 ) ):
        tmp += hexstr[i*2:(i*2)+2]

    return tmp


def zkRegevent(self):
    """register for live events"""
    print("reg event")
    command = CMD_REG_EVENT
    command_string = '\xff\xff\x00\x00'
    chksum = 0
    reply_id = unpack('HHHH', self.data_recv[:8])[3]

    buf = self.createHeader(command, chksum, self.session_id, reply_id, command_string)
    self.zkclient.sendto(buf, self.address)
    #print(buf.encode("hex"))

    self.data_recv, addr = self.zkclient.recvfrom(1024)
    #self.session_id = unpack('HHHH', self.data_recv[:8])[2]


    print("size", sys.getsizeof(self.data_recv))
    print("size", len(self.data_recv))
    lensi = len(self.data_recv) // 2
    fstri = str(lensi) + "H"
    print("fstri=", fstri)
    print("first unpack   ", unpack (fstri, self.data_recv))


    if unpack('4H',self.data_recv[:8])[0] == CMD_PREPARE_DATA:

        print("received CMD_PREPARE_DATA")
        size = unpack('I', self.data_recv[8:12])[0]

    if unpack('4H', self.data_recv[:8])[0] == CMD_ACK_OK:
        print("CMD_ACK_OK from regevent")



        print('Receiving %d %s' % (len(self.data_recv[8:]),"bytes"))
        #data_recv, addr = self.zkclient.recvfrom(43773)
        #lens = len(self.data_recv) / 2
        #fstr = str(lens) + "H"
        #print("second unpack", unpack(fstr, self.data_recv))




    i=0

    while True: #unpack('4H', data_recv[:8])[0] != CMD_ACK_OK or unpack('4H', data_recv[:8])[0] == CMD_DATA:



        print("COUNTER", i)

        self.data_recv, addr = self.zkclient.recvfrom(1024)

        header=unpack("4H", self.data_recv[:8])
        if header[0] == CMD_DATA:

            i = i +1
            print("data package " , header[0])
            lens = len(self.data_recv) // 2
            fstr = str(lens) + "H"

            print("data unpack", unpack(fstr, self.data_recv))
            if i == 1:
                self.attendancedata.append(self.data_recv)
            elif i == 2:
                        #atti.append(data_recv)
                self.attendancedata.append(self.data_recv)
            if header[0] == CMD_ACK_OK:
                print("CMD_ACK_OK")

                #acmOK(self)
        if header[0] == CMD_ACK_OK:
            print("CMD_ACK_OK")

        if header[0] == CMD_REG_EVENT:
            print("CMD_REG_EVENT")

            if header[2] == 1:
                print(" EF_ATTLOG")
                uid = unpack("H", self.data_recv[8:10])[0]
                year = self.data_recv[14] + 2000
                month = self.data_recv[15]
                day = self.data_recv[16]
                hour = self.data_recv[17]
                minute = self.data_recv[18]
                second = self.data_recv[19]
                stamp = datetime(year, month, day, hour, minute, second)
                print("  User: %d Time: " % uid, stamp)

            elif header[2] == 2:
                print(" EF_FINGER")

            elif header[2] == 4:
                print(" EF_ENROLLUSER")

            elif header[2] == 8:
                print(" EF_ENROLLFINGER")

            elif header[2] == 16:
                print(" EF_BUTTON")

            elif header[2] == 32:
                print(" EF_UNLOCK")

            elif header[2] == 128:
                print(" EF_VERIFY ", unpack('H', self.data_recv[8:10])[0])

            elif header[2] == 256:
                print(" EF_FPFTR")

            elif header[2] == 512:
                print(" EF_ALARM")

            else:
                print(" *** UNKNOWN %d ***" % header[2])

            print(self.data_recv[8:])

            """send CMD_ACK_OK"""
            command = CMD_ACK_OK
            command_string = ''
            chksum = 0
            reply_id = header[3]

            buf = self.createHeader(command, chksum, self.session_id,
                reply_id, command_string)

            self.zkclient.sendto(buf, self.address)
