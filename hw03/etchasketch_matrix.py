#!/usr/bin/python3

import smbus
import sys
import time
import Adafruit_BBIO.GPIO as GPIO

# Initial cursor position
cursorx = 0
cursory = 0

# Read color argument
color = sys.argv[1]
if color not in ["RED", "GREEN", "YELLOW"]:
    sys.exit("Color should be RED, GREEN, or YELLOW")

colormap = {1: "GREEN", 2: "RED", 3: "YELLOW"}
mapcolor = {"GREEN": 1, "RED": 2, "YELLOW": 3}
color = mapcolor[color]

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

# Button GPIO setup
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

# Function to turn all matrix leds off
def clear_matrix():
    bus.write_i2c_block_data(matrix, 0x00, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

# Function to turn off one pixel
def clear_led(x, y):
    mask = 0xFF ^ (1 << y)
    column = x * 2
    led_green = bus.read_byte_data(matrix, column) & mask
    led_red = bus.read_byte_data(matrix, column + 1) & mask
    bus.write_i2c_block_data(matrix, column, [led_green, led_red])

# Function to turn on one pixel
def write_led(x, y, color):
    clear_led(x, y)
    if color == "GREEN" or color == "YELLOW":
        column = x * 2
        data = bus.read_byte_data(matrix, column) | (1 << y)
        bus.write_byte_data(matrix, column, data)
    if color == "RED" or color == "YELLOW":
        column = x * 2 + 1
        data = bus.read_byte_data(matrix, column) | (1 << y)
        bus.write_byte_data(matrix, column, data)

# Call back for button push
def draw_point(button):
        global cursorx
        global cursory
        global color
        global colormap
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
            # Keep within boundaries
            cursorx = max(0, cursorx)
            cursory = max(0, cursory)
            cursorx = min(7, cursorx)
            cursory = min(7, cursory)
            write_led(cursorx, cursory, colormap[color])
        
GPIO.add_event_detect(button_up, GPIO.BOTH, callback=draw_point, bouncetime=10)
GPIO.add_event_detect(button_down, GPIO.BOTH, callback=draw_point, bouncetime=10)
GPIO.add_event_detect(button_left, GPIO.BOTH, callback=draw_point, bouncetime=10)
GPIO.add_event_detect(button_right, GPIO.BOTH, callback=draw_point, bouncetime=10)

clear_matrix()

cleartime = 0
colortime = 0
blinktime = time.time()

while True:
    
    # Erase screen if right and left are pushed at the same time
    if GPIO.input(button_right) and GPIO.input(button_left):
        if cleartime == 0:
            cleartime = time.time()
        elif time.time() - cleartime >= 2:
            clear_matrix()
            cleartime = 0
    else:
        cleartime = 0
    
    # Cycle to next color if up and down are pushed at the same time
    if GPIO.input(button_up) and GPIO.input(button_down):
        if colortime == 0:
            colortime = time.time()
        elif time.time() - colortime >= 2:
            if color < 3:
                color = color + 1
            elif color == 3:
                color = 1
            colortime = 0
            write_led(cursorx, cursory, colormap[color])
    else:
        colortime = 0