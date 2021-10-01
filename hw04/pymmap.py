#!/usr/bin/python3

from mmap import mmap
import time, struct

GPIO1_offset = 0x4804c000
GPIO1_size = 0x4804cfff-GPIO1_offset
GPIO_OE = 0x134
GPIO_SETDATAOUT = 0x194
GPIO_CLEARDATAOUT = 0x190
USR3 = 1<<24

# Button P9_22, 
GPIO0_offset = 0x44e07000
GPIO0_size = 0x44e07fff-GPIO0_offset
GPIO_DATAIN = 0x138
BUTTON1 = 1<<2 # GPIO0
BUTTON2 = 1<<17 # GPIO1

with open("/dev/mem", "r+b" ) as f:
    mem1 = mmap(f.fileno(), GPIO1_size, offset=GPIO1_offset)
    mem0 = mmap(f.fileno(), GPIO0_size, offset=GPIO0_offset)

# Set USR3 pin as output  
packed_reg = mem1[GPIO_OE:GPIO_OE+4]
reg_status = struct.unpack("<L", packed_reg)[0]
reg_status &= ~(USR3)
mem1[GPIO_OE:GPIO_OE+4] = struct.pack("<L", reg_status)

try:
    while(True):
        button1_state = struct.unpack("<L", mem0[GPIO_DATAIN:GPIO_DATAIN+4])[0] & BUTTON1
        button2_state = struct.unpack("<L", mem1[GPIO_DATAIN:GPIO_DATAIN+4])[0] & BUTTON2
        if not button2_state:
            mem1[GPIO_SETDATAOUT:GPIO_SETDATAOUT+4] = struct.pack("<L", USR3)
        elif button2_state:
            mem1[GPIO_CLEARDATAOUT:GPIO_CLEARDATAOUT+4] = struct.pack("<L", USR3)
            
except KeyboardInterrupt:
    mem1.close()
    mem0.close()