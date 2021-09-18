#!/usr/bin/python3

# Toggles a GPIO pin as fast as possible with the Adafruit BBIO library

import Adafruit_BBIO.GPIO as GPIO

LED1 = "P8_7"
GPIO.setup(LED1, GPIO.OUT)
GPIO.output(LED1, 0)

while True:
    GPIO.output(LED1, 1)
    GPIO.output(LED1, 0)