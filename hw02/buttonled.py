#!/usr/bin/python3
import Adafruit_BBIO.GPIO as GPIO
import time
LED1 = "P8_7"
LED2 = "P8_9"
LED3 = "P8_11"
LED4 = "P8_13"
button1 = "P9_26"
button2 = "P9_42"
button3 = "P9_41"
button4 = "P9_24"
	

GPIO.setup(button1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

map = {button1: LED1, button2: LED2, button3: LED3, button4: LED4}

def led_update(pin):
	state = GPIO.input(pin)
	GPIO.output(map[pin], state)

GPIO.add_event_detect(button1, GPIO.BOTH, callback=led_update, bouncetime=10)
GPIO.add_event_detect(button2, GPIO.BOTH, callback=led_update, bouncetime=10)
GPIO.add_event_detect(button3, GPIO.BOTH, callback=led_update, bouncetime=10)
GPIO.add_event_detect(button4, GPIO.BOTH, callback=led_update, bouncetime=10)

while True:
	potato=1


	