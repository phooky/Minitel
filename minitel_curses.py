import curses
import logging
from minitel import *
import time

# Minitel curses emulator

class MinitelCurses:
    def __init__(self,mode=MODE_VIDEOTEX):
        'Construct a minitel emulator.'
        self.setMode(mode)
        self.textMode = NORMAL
        self.vtMode = -1
        self.fg = -1
        self.bg = -1
        if mode == MODE_VIDEOTEX:
            self.setVTMode(VT_TEXT)
        self.stdscr = curses.initscr()
        self.stdscr.nodelay(True)
        self.stdscr.scrollok(True)
        curses.noecho()
        curses.cbreak()

    def close(self):
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def setVTMode(self,vtMode):
        'Set graphics or character mode in videotex display mode'
        if not self.isVT():
            raise ValueError("Can't switch VT modes in ANSI mode")
        if self.vtMode == vtMode:
            return
        if vtMode == VT_TEXT:
            pass
        elif vtMode == VT_GRAPHICS:
            pass
        else:
            raise ValueError('Unrecognized VT mode')
        self.vtMode = vtMode

    def setMode(self,mode):
        'Set videotex or ANSI mode.'
        if mode not in [MODE_VIDEOTEX, MODE_ANSI]:
            raise ValueError('Unrecognized display mode')
        self.mode = mode

    def isVT(self):
        'Shorthand test to check for Videotex mode.'
        return self.mode == MODE_VIDEOTEX

    def clearScreen(self):
        'Clear the terminal.'
        self.stdscr.clear()

    def newline(self):
        'Send a newline/carriage return combo.'
        self.stdscr.addch('\n')

    def readline(self):
        'Read a line of data from the terminal.'
        return self.stdscr.getstr()

    def send(self,data):
        'Shorthand for sending bytes to the minitel.'
        data=data.replace('\r','')
        self.stdscr.addstr(data)
        self.stdscr.refresh()
        
    def recv(self,byteCount):
        'Shorthand for retrieving a number of bytes from the minitel.'
        s = ''
        timeout = 0.1
        end = time.time() + timeout
        while len(s) < byteCount:
            c = self.stdscr.getch()
            if c < 256 and c >= 0:
                self.stdscr.echochar(chr(c))
                s = s + chr(c)
            else:
                if time.time() > end:
                    return s
                time.sleep(0.1)
        return s
    
    def setTextMode(self,textMode,force = False):
        if self.textMode == textMode:
            return
        self.textMode = textMode

    def moveCursor(self,x,y):
        self.stdscr.move(y,x)

    def showCursor(self,on=True):
        if self.isVT():
            if on:
                curses.curs_set(2)
            else:
                curses.curs_set(0)

    def setColors(self,fg=-1,bg=-1):
        if fg < -1 or fg > 7:
            raise ValueError('Foreground out of range: {0}'.format(fg))
        if bg < -1 or bg > 7:
            raise ValueError('Background out of range: {0}'.format(bg))
        if fg != -1 and fg != self.fg:
            if self.isVT():
                pass
            else:
                pass
            self.fg = fg
        if bg != -1 and bg != self.bg:
            if self.isVT():
                pass
            else:
                pass
            self.bg = bg

    def wait(self):
        'Wait for all data to be transmitted.'
        pass
