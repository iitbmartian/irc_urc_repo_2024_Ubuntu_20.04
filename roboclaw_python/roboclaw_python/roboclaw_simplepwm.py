import time
from roboclaw_3 import Roboclaw

#Windows comport name
# rc = Roboclaw("COM11",115200)
#Linux comport name
rc = Roboclaw("/dev/ttyUSB0",115200)

rc.Open()
address = 132


print(rc.GetConfig(0x84))	#1/4 power forward
