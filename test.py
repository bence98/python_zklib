from zklib.zklib import ZKLib




maquina = ZKLib(ip='10.0.8.11', port=4370)
maquina.connect()


print(maquina.getUser())
# print(maquina.getAttendance())

maquina.disconnect()
