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

bus.write_byte_data(addressA, 2, setlow)
bus.write_byte_data(addressA, 3, sethigh)
bus.write_byte_data(addressB, 2, setlow)
bus.write_byte_data(addressB, 3, sethigh)

map = {alertApin: addressA, alertBpin: addressB}

def print_temp(alertpin):
    temp = round(bus.read_byte_data(map[alertpin], 0), 1)
    if alertpin == alertApin:
        print("Alert: Temp A is " + str(temp))
    elif alertpin == alertBpin:
        print("Alert: Temp B is " + str(temp))
    
GPIO.add_event_detect(alertApin, GPIO.FALLING, callback=print_temp)
GPIO.add_event_detect(alertBpin, GPIO.FALLING, callback=print_temp)

while True:
    a = 1
    