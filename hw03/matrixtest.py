#!/usr/bin/python3

import smbus
import time
bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70

delay = 1; # Delay between images in s

bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

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

write_led(1, 1, "YELLOW")