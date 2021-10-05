# Homework 4

## Memory Map



## GPIO via mmap

pymmap.py reads buttons on P9_22 and PX_XX and toggles the USR3 and USR2 LEDs, all using mmap. One button is on GPIO0 and one is on GPIO1, necessitating two mmap calls. Run with `sudo ./pymmap.py`.

pymmaptoggle.py toggles P9_22 as fast as possible using mmap. Run with `sudo ./pymmaptoggle.py`.

## i2c via the kernel driver

kerneltemp.sh enables the kernel driver for the tmp101, reads the temperature, and then prints it to the console. 

## Control the LED matrix from the browser

etchasketch_web.py runs a flask web server that displays buttons to control the LED matrix etch-a-sketch. It has up, down, left, and right to move the cursor and draw, clear to clear the display, and green, red, and yellow buttons to change the cursor color. Run with `sudo ./etchasketch_web.py`. It needs sudo so that i2c will function. 

## TFT display

![Boris the beagle](tft_beagle.jpg)

![Altered Image](tft_text.jpg)