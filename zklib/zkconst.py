from datetime import datetime, date

USHRT_MAX = 65535

CMD_CONNECT = 1000
CMD_EXIT = 1001
CMD_ENABLEDEVICE = 1002
CMD_DISABLEDEVICE = 1003
CMD_RESTART = 1004
CMD_POWEROFF = 1005
CMD_SLEEP = 1006
CMD_RESUME = 1007
CMD_CAPTUREFINGER = 1009
CMD_TESTTEMP = 1011
CND_CAPTUREIMAGE = 1012
CMD_REFRESHDATA = 1013
CMD_REFRESHOPTION = 1014
CMD_TESTVOICE = 1017
CMD_VERSION = 1100
CND_CHANGESPEED = 1101
CMD_AUTH = 1102

CMD_PREPARE_DATA = 1500
CMD_DATA = 1501
CMD_FREE_DATA = 1502

CMD_ACK_OK = 2000
CMD_ACK_ERROR = 2001
CMD_ACK_DATA = 2002
CMD_UDP_OK = 2005

CMD_DB_RRQ = 7
CMD_SET_USER = 8
CMD_USERTEMP_RRQ = 9
CMD_ATTLOG_RRQ = 13
CMD_CLEAR_DATA = 14
CMD_CLEAR_ATTLOG = 15
CMD_DELETEUSER = 18
CMD_CLEAR_ADMIN = 20

CMD_STARTENROLL = 61
CMD_WRITE_LCD = 66
CMD_GETFREESIZE = 50

CMD_REG_EVENT = 500

CMD_GET_TIME  = 201
CMD_SET_TIME  = 202

CMD_TZ_RRQ = 27
CMD_TZ_WRQ = 28
CMD_UNLOCK = 31

CMD_DEVICE = 11

FCT_ATTLOG = '\x01' #1 & 0xFF

LEVEL_USER = 0
LEVEL_ADMIN = 14

ENCODING='ascii'
STATE_FIRSTPACKET = 1
STATE_PACKET = 2
STATE_FINISHED = 3

CONNECTION_TYPE_UDP = 'udp'
CONNECTION_TYPE_TCP = 'tcp'

def encode_time(t):
    """Encode a timestamp send at the timeclock

    copied from zkemsdk.c - EncodeTime"""
    d = ( (t.year % 100) * 12 * 31 + ((t.month - 1) * 31) + t.day - 1) *\
         (24 * 60 * 60) + (t.hour * 60 + t.minute) * 60 + t.second

    return d


def decode_time(t):
    """Decode a timestamp retrieved from the timeclock
    copied from zkemsdk.c - DecodeTime"""
    second = t % 60
    t = t // 60

    minute = t % 60
    t = t // 60

    hour = t % 24
    t = t // 24

    day = t % 31+1
    t = t // 31

    month = t % 12+1
    t = t // 12

    year = t + 2000

    d = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

    return d

