#!/usr/bin/python3
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2
import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
import sys

cursorx = 0
cursory = 0

# Read color argument
color = sys.argv[1]
if color not in ["RED", "GREEN", "YELLOW"]:
    sys.exit("Color should be RED, GREEN, or YELLOW")

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

yencoder = RotaryEncoder(eQEP2)
#xencoder = RotaryEncoder()
yencoder.setAbsolute()
#xencoder.setAbsolute()
yencoder.enable()
#xencoder.enable()

# Button GPIO setup
button_red = "P9_26"
button_green = "P9_42"
button_yellow = "P9_41"
button_clear = "P9_24"
GPIO.setup(button_red, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button_green, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button_yellow, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button_clear, GPIO.IN, GPIO.PUD_DOWN)

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

def read_led(x, y):
    led_green = bus.read_byte_data(matrix, x*2) & (1 << y)
    led_red = bus.read_byte_data(matrix, x*2+1) & (1 << y)
    if led_green or led_red:
        return True
    else:
        return False
        
# Callback for button push
def handle_button(button):
        global color
        global colormap
        state = GPIO.input(button)
        # Only do something if the button is pressed, not released
        if state == 1:
            if button == button_red:
                color = "RED"
                write_led(cursorx, cursory, color)
            if button == button_green:
                color = "GREEN"
                write_led(cursorx, cursory, color)
            if button == button_yellow:
                color = "YELLOW"
                write_led(cursorx, cursory, color)
            if button == button_clear:
                clear_matrix()

GPIO.add_event_detect(button_red, GPIO.BOTH, callback=handle_button, bouncetime=10)
GPIO.add_event_detect(button_green, GPIO.BOTH, callback=handle_button, bouncetime=10)
GPIO.add_event_detect(button_yellow, GPIO.BOTH, callback=handle_button, bouncetime=10)
GPIO.add_event_detect(button_clear, GPIO.BOTH, callback=handle_button, bouncetime=10)

clear_matrix()
oldx = 0
oldy = 0
blinktimer = time.time()
while True:
    if time.time() - blinktimer >= 0.2:
        blinktimer = time.time()
        if read_led(cursorx, cursory):
            clear_led(cursorx, cursory)
        else:
            write_led(cursorx, cursory, color)
    
    if (abs(yencoder.position - oldy)) >= 4:
        write_led(cursorx, cursory, color)
        cursory += round((yencoder.position - oldy)/4)
        oldy = yencoder.position
        cursory = max(0, cursory)
        cursory = min(7, cursory)
        write_led(cursorx, cursory, color)
        
    cursorx = max(0, cursorx)
    cursorx = min(7, cursorx)
    