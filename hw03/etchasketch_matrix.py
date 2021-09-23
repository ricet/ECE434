#!/usr/bin/python3

import smbus
import Adafruit_BBIO.GPIO as GPIO

cursorx = 0
cursory = 0

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

button_up = "P9_26"
button_right = "P9_42"
button_down = "P9_41"
button_left = "P9_24"

GPIO.setup(button_up, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button_right, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button_down, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button_left, GPIO.IN, GPIO.PUD_DOWN)

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

def clear_matrix():
    bus.write_i2c_block_data(matrix, 0x00, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

def write_led(x, y, color):
    column = 0
    if color == "GREEN" or color == "YELLOW":
        column = x * 2
        data = bus.read_byte_data(matrix, column) | (1 << y)
        bus.write_byte_data(matrix, column, data)
    if color == "RED" or color == "YELLOW":
        column = x * 2 + 1
        data = bus.read_byte_data(matrix, column) | (1 << y)
        bus.write_byte_data(matrix, column, data)

def draw_point(button):
        global cursorx
        global cursory
        state = GPIO.input(button)
        # Only move cursor if the button is pressed, not released
        if state == 1:
            if button == button_down:
                cursorx = cursorx - 1
            if button == button_up:
                cursorx = cursorx + 1
            if button == button_left:
                cursory = cursory + 1
            if button == button_right:
                cursory = cursory - 1
            cursorx = max(0, cursorx)
            cursory = max(0, cursory)
            cursorx = min(7, cursorx)
            cursory = min(7, cursory)
            write_led(cursorx, cursory, "GREEN")
        
GPIO.add_event_detect(button_up, GPIO.BOTH, callback=draw_point, bouncetime=10)
GPIO.add_event_detect(button_down, GPIO.BOTH, callback=draw_point, bouncetime=10)
GPIO.add_event_detect(button_left, GPIO.BOTH, callback=draw_point, bouncetime=10)
GPIO.add_event_detect(button_right, GPIO.BOTH, callback=draw_point, bouncetime=10)

clear_matrix()

while True:
    a = 1