#!/usr/bin/python3

import smbus
import time

bus = smbus.SMBus(2)
addressA = 0x48
addressB = 0x4a

while True:
    tempA = round(9/5 * bus.read_byte_data(addressA, 0) + 32, 1)
    tempB = round(9/5 * bus.read_byte_data(addressB, 0) + 32, 1)
    errorA = (bus.read_byte_data(addressA, 1) >> 7) ^ 1
    errorB = (bus.read_byte_data(addressB, 1) >> 7) ^ 1
    print("Temp A is: " + str(tempA) + "°F   Alert A: " + str(errorA) + "    Temp B is: " + str(tempB) + "°F   Alert B: " + str(errorB))
    time.sleep(1)