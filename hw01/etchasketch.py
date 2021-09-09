#!/usr/bin/python3

import curses
from curses import wrapper
import sys

def main(stdscr):
    # Clear screen
    stdscr.clear()

    # Draw board
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    for i in range(0, width*2, 2):
        stdscr.addch(0, i, "*")
        stdscr.addch(height, i, "*")
    for j in range(0, height):
        stdscr.addch(j, 0, "*")
        stdscr.addch(j, width*2, "*")
    stdscr.refresh()
    stdscr.getkey()

print(str(sys.argv[1]))
wrapper(main)
