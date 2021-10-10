#!/usr/bin/python3
import time, math, os, smbus, sys


if not os.path.isdir("/sys/class/i2c-adapter/i2c-2/2-0053"):
    with open("/sys/class/i2c-adapter/i2c-2/new_device", "w") as f:
        f.write("adxl345 0x53")

def read_z():
    with open("/sys/class/i2c-adapter/i2c-2/2-0053/iio:device1/in_accel_z_raw") as f:
        return int(f.read())

def read_x():
    with open("/sys/class/i2c-adapter/i2c-2/2-0053/iio:device1/in_accel_x_raw") as f:
        return int(f.read())

def read_y():
    with open("/sys/class/i2c-adapter/i2c-2/2-0053/iio:device1/in_accel_y_raw") as f:
        return int(f.read())

def magnitude(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)

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

# Read color argument
color = sys.argv[1]
if color not in ["RED", "GREEN", "YELLOW"]:
    sys.exit("Color should be RED, GREEN, or YELLOW")

colormap = {1: "GREEN", 2: "RED", 3: "YELLOW"}
mapcolor = {"GREEN": 1, "RED": 2, "YELLOW": 3}
color = mapcolor[color]

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

cursorx = 0
cursory = 0
clear_matrix()
while True:
    # Read accel
    x = read_x()
    y = read_y()
    z = read_z()
    mag = magnitude(x, y, z)

    # Clear matrix if shaken hard
    if mag > 400:
        clear_matrix()
    # Change color if upsidedown
    if z < -200:
        if color < 3:
            color = color + 1
        else:
            color = 1
        time.sleep(1)

    if x > 70:
        cursorx = cursorx - 1
    if x < -70:
        cursorx = cursorx + 1
    if y > 70:
        cursory = cursory - 1
    if y < -70:
        cursory = cursory + 1
    cursorx = max(0, cursorx)
    cursory = max(0, cursory)
    cursorx = min(7, cursorx)
    cursory = min(7, cursory)
    write_led(cursorx, cursory, colormap[color])
    time.sleep(0.5)
