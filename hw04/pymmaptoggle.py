#!/usr/bin/python3

from mmap import mmap
import time, struct

GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190

# Change
OUT_PIN = 1<<24

with open("/dev/mem", "r+b" ) as f:
    mem1 = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)

# Set OUT_PIN pin as output  
packed_reg = mem1[GPIO_OE:GPIO_OE+4]
reg_status = struct.unpack("<L", packed_reg)[0]
reg_status &= ~(OUT_PIN)
mem1[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)

try:
    while(True):
            # Toggle as fast as possible
            mem1[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", OUT_PIN)
            mem1[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", OUT_PIN)
            
except KeyboardInterrupt:
    mem1.close()