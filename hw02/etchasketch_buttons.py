#!/usr/bin/python3

import curses
from curses import wrapper
import sys
import Adafruit_BBIO.GPIO as GPIO

# Cursor starting coordinates
cursorx = 2
cursory = 1
width = 0
height = 0

#Set gpio pins
LED1 = "P8_7"
button_up = "P9_26"
button_right = "P9_42"
button_down = "P9_41"
button_left = "P9_24"
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(button_up, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button_right, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button_down, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(button_left, GPIO.IN, GPIO.PUD_DOWN)


def main(stdscr):
    global height
    global width
    global cursorx
    global cursory
    
    # Clear screen
    stdscr.clear()
    stdscr.nodelay(False)
    # Read arguments and draw board
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    drawboard(stdscr, width, height)
    
    # Callback function for gpio detect event
    # Defined inside of main() so that it has access to stdscr
    def draw_point(button):
        global height
        global width
        global cursorx
        global cursory
        # Light led when button is pushed for feedback
        state = GPIO.input(button)
        GPIO.output(LED1, state)
        # Only move cursor if the button is pressed, not released
        if state == 1:
            if button == button_down:
                cursory = cursory + 1
            if button == button_up:
                cursory = cursory - 1
            if button == button_left:
                cursorx = cursorx - 2
            if button == button_right:
                cursorx = cursorx + 2
            # Keep cursor within board perimeter
            cursorx = max(2, cursorx)
            cursory = max(1, cursory)
            cursorx = min(width*2, cursorx)
            cursory = min(height, cursory)
            # Update cursor location with new coordinates and draw an X 
            stdscr.move(cursory, cursorx)
            stdscr.addch(chr(88))
            stdscr.refresh()
        
    # Detect button presses
    GPIO.add_event_detect(button_up, GPIO.BOTH, callback=draw_point, bouncetime=10)
    GPIO.add_event_detect(button_down, GPIO.BOTH, callback=draw_point, bouncetime=10)
    GPIO.add_event_detect(button_left, GPIO.BOTH, callback=draw_point, bouncetime=10)
    GPIO.add_event_detect(button_right, GPIO.BOTH, callback=draw_point, bouncetime=10)

    while True:
        # Wait for user input
        c = stdscr.getch()
        #c = 0   
        # Break loop and quit if escape is pressed
        if c == 27:
            break
        # If space is pressed clear screen and redraw board
        if c == 32:
           stdscr.clear()
           drawboard(stdscr, width, height)


# Draw board function, draws asterisks around the perimeter of the drawing area
def drawboard(stdscr, width, height):
    for i in range(0, width*2+2, 2):
        stdscr.addch(0, i, "*")
        stdscr.addch(height+1, i, "*")
    for j in range(0, height+1):
        stdscr.addch(j, 0, "*")
        stdscr.addch(j, width*2+2, "*")
    # Put instructions on screen
    stdscr.addstr(height+3, 0, "Use the arrow keys to draw, space to clear the screen, and escape to quit")

# Curses function to call main, handles curses things
wrapper(main)
