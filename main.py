import serial
'''
class VitalSignDevice(comport):
    """docstring for ."""
    def __init__(self, comport):
        super(, self).__init__()
        ser = serial.Serial(comport , 115200)
    def

import serial
port = "/dev/ttyAMAO"
usart = serial.Serial (port,4800)
message_bytes = bytes.fromhex("0111050200013F0804")
usart.write(message_bytes)
'''

class VitalSignDevice:
    def __init__(self, COMPORT):
        self.COMPORT = COMPORT
        #self.ser = serial.Serial(self.COMPORT, 115200)
        print(f'CONECTING TO {COMPORT}')

    def initailFunction(self):
        '''Disable ECG parameter output '''
        # 0x55 0xAA 0x04 0x01 0x00 0xFa
        ECG_PARAM_DISABLE = bytes.fromhex("0x55 0xAA 0x04 0x01 0x00 0xFa")
        #self.ser.write(ECG_PARAM_DISABLE)
        print(ECG_PARAM_DISABLE)

    def multiple(self):
        print(self.kk * 5)


device = VitalSignDevice('COM2')
device.initailFunction()
