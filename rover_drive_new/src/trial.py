#!/usr/bin/env python
import rospy
from time import sleep
import serial
import serial.tools.list_ports as ports
shoulder_elbow_rot_addr=0x83
base_elbow_addr=0x84
wrist_rot_addr=0x85
PORT='/dev/ttyUSB1'
def serial_send(a):
       
        command=str(a)
        command=command+'\n'
        ser.write(command.encode())
        print("Sent "+command)

    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = PORT
    ser.open()
    while True:
        serial_send(input("Enter pulselen: "))