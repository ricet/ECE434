#!/usr/bin/env python3
# From: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
# GPIO Status and Control
import Adafruit_BBIO.GPIO as GPIO
from flask import Flask, render_template, request
import smbus
app = Flask(__name__)

ledRed = "USR3"
ledRedSts = 0
GPIO.setup(ledRed, GPIO.OUT)   
GPIO.output(ledRed, GPIO.HIGH)

cursorx = 0
cursory = 0
color = "GREEN"

bus = smbus.SMBus(2)  # Use i2c bus 1
matrix = 0x70         # Use address 0x70
bus.write_byte_data(matrix, 0x21, 0)   # Start oscillator (p10)
bus.write_byte_data(matrix, 0x81, 0)   # Disp on, blink off (p11)
bus.write_byte_data(matrix, 0xe7, 0)   # Full brightness (page 15)

# Function to turn all matrix leds off
def clear_matrix():
    bus.write_i2c_block_data(matrix, 0x00, [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

clear_matrix()

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

@app.route("/")
def index():
	# Read Sensors Status
	ledRedSts = GPIO.input(ledRed)
	templateData = {
              'title' : 'GPIO output Status!',
              'ledRed'  : ledRedSts,
        }
	return render_template('index3.html', **templateData)
	
@app.route("/<action>")
def action(action):
	global cursorx
	global cursory
	global color

	if action == "up":
		cursory = cursory + 1
	if action == "down":
		cursory = cursory - 1
	if action == "left":
		cursorx = cursorx - 1
	if action == "right":
		cursorx = cursorx + 1
	if action == "clear":
		clear_matrix()
	if action == "green":
		color = "GREEN"
	if action == "red":
		color = "RED"
	if action == "yellow":
		color = "YELLOW"
	cursory = max(0, cursory)
	cursory = min(7, cursory)
	cursorx = max(0, cursorx)
	cursorx = min(7, cursorx)		
	write_led(cursorx, cursory, color)
		     
	ledRedSts = GPIO.input(ledRed)

	templateData = {
              'ledRed'  : ledRedSts,
	}
	return render_template('index3.html', **templateData)
	
if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8081, debug=True)