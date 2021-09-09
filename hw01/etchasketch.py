#!/usr/bin/python3

import curses
from curses import wrapper
import sys


def main(stdscr):
    # Clear screen
    stdscr.clear()
    stdscr.nodelay(False)
    # Draw board
    width = int(sys.argv[1])
    height = int(sys.argv[2])
    drawboard(stdscr, width, height)

    cursorx = 2
    cursory = 1
    while True:
        c = stdscr.getch()
        if c == curses.KEY_DOWN:
            cursory = cursory + 1
        if c == curses.KEY_UP:
            cursory = cursory - 1
        if c == curses.KEY_LEFT:
            cursorx = cursorx - 2
        if c == curses.KEY_RIGHT:
            cursorx = cursorx + 2
        if c == 27:
            break
        if cursorx < 2: cursorx = 2
        if cursory < 1: cursory = 1
        if cursorx >= width*2: cursorx = width*2
        if cursory > height: cursory = height
        stdscr.move(cursory, cursorx)
        stdscr.addch(chr(88))

        if c == 32:
           stdscr.clear()
           drawboard(stdscr, width, height)


def drawboard(stdscr, width, height):
    for i in range(0, width*2+2, 2):
        stdscr.addch(0, i, "*")
        stdscr.addch(height+1, i, "*")
    for j in range(0, height+1):
        stdscr.addch(j, 0, "*")
        stdscr.addch(j, width*2+2, "*")

    stdscr.addstr(height+3, 0, "Use the arrow keys to draw, space to clear the screen, and escape to quit")
wrapper(main)
