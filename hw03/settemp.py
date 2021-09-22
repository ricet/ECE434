#!/usr/bin/python3

import smbus
import time
import sys
import Adafruit_BBIO.GPIO as GPIO


bus = smbus.SMBus(2)
addressA = 0x48
addressB = 0x4a

alertApin = "P9_12"
alertBpin = "P9_11"
GPIO.setup(alertApin, GPIO.IN)
GPIO.setup(alertBpin, GPIO.IN)

sethigh = int(sys.argv[1])
setlow = int(sys.argv[2])

#bus.write_byte_data(addressA, 3, setA)
bus.write_byte_data(addressB, 2, 0x1B)
bus.write_byte_data(addressB, 3, 0x1C)

map = {alertApin: addressA, alertBpin: addressB}

def print_temp(alertpin):
    tempB = round(bus.read_byte_data(map[alertpin], 0), 1)
    print("Alert: Temp B is " + str(tempB))
    
GPIO.add_event_detect(alertBpin, GPIO.FALLING, callback=print_temp)

while True:
    a = 1
    