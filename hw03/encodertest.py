#!/usr/bin/python3

from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2
import time

# Instantiate the class to access channel eQEP2, and initialize that channel
myEncoder = RotaryEncoder(eQEP2)
myEncoder.setAbsolute()
myEncoder.enable()

while True:
    print(myEncoder.position)
    time.sleep(0.2)