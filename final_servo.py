import signal
import sys
import os
from time import sleep
import serial
import serial.tools.list_ports as ports
PORT='/dev/ttyUSB1'
def serial_send(a):
       
        command=str(a)
        command=command+'\n'
        ser.write(command.encode())
        print("Sent "+command)
        
        # print(ser.read(6).decode())
if __name__ == "__main__":

    # com_ports = list(ports.comports())  # create a list of com ['COM1','COM2']
    # for i in com_ports:
	#     print(i.device)  # returns 'COMx'

    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = PORT
    ser.open()

    
    while True:
        angle=input('Enter angle: ')
        new_angle="{:>03}".format(angle)
        serial_send(new_angle)