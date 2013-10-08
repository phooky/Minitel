#!/usr/bin/env python

from argparse import ArgumentParser
import serial
import sys
import time

# Minitel modes. Boots into Videotex.
MODE_VIDEOTEX = 0
MODE_ANSI = 1

# Text modes. Tall and wide only valid in Videotex mode.
NORMAL = 0
TALL = 1
WIDE = 2
BLINK = 4
BOLD = 8
INVERTED = 16
STRIKETHROUGH = 32
UNDERLINE = 64

# Videotex submodes
VT_TEXT = 0
VT_GRAPHICS = 1

ESC='\x1b'
# Control sequence introducer
CSI = ESC+'['
def SGR(param):
    'Select graphic rendition'
    return CSI + str(param) + 'm'

class Minitel:
    def __init__(self,port=None,baud=4800,mode=MODE_VIDEOTEX,hax=False):
        '''Construct a minitel interface on a given port.
        The port should be either a string describing the port,
        or a previously constructed serial object.'''
        # if true support 0xee/0xef mode switching
        self.hax = hax
        self.mode = MODE_VIDEOTEX
        self.setMode(mode)
        self.baud = baud
        self.textMode = NORMAL
        self.vtMode = -1
        self.fg = -1
        self.bg = -1
        if isinstance(port, basestring):
            self.portName = port
            self.ser = serial.Serial(port, baud, 
                                     parity = serial.PARITY_EVEN,
                                     bytesize = serial.SEVENBITS,
                                     timeout = 0.1)
        else: # presume it's a previously opened port
            self.ser = port
        if mode == MODE_VIDEOTEX:
            self.setVTMode(VT_TEXT)

    def close(self):
        self.ser.close()

    def setVTMode(self,vtMode):
        'Set graphics or character mode in videotex display mode'
        if not self.isVT():
            raise ValueError("Can't switch VT modes in ANSI mode")
        if self.vtMode == vtMode:
            return
        if vtMode == VT_TEXT:
            self.send('\x0f')
        elif vtMode == VT_GRAPHICS:
            self.send('\x0e')
        else:
            raise ValueError('Unrecognized VT mode')
        self.vtMode = vtMode

    def setMode(self,mode):
        'Set videotex or ANSI mode.'
        if mode not in [MODE_VIDEOTEX, MODE_ANSI]:
            raise ValueError('Unrecognized display mode')
        if self.hax and mode != self.mode:
            if mode == MODE_VIDEOTEX:
                self.send('\xee')
            else:
                self.send('\xef')
        self.mode = mode

            

    def isVT(self):
        'Shorthand test to check for Videotex mode.'
        return self.mode == MODE_VIDEOTEX

    def clearScreen(self):
        'Clear the terminal.'
        self.invalidate()
        if self.isVT(): self.send('\x0c')
        else: self.send('\x1b[2J')
    
    def newline(self):
        'Send a newline/carriage return combo.'
        self.send('\n\r')

    def readline(self):
        'Read a line of data from the terminal.'
        line = ''
        update_at = time.time() + 60.0
        while True:
            c = self.recv(1)
            if c in ['\n','\r']:
                return line
            line = line + c
            if time.time() > update_at:
                update_at = time.time() + 60.0
                self.showCursor()

    def send(self,data):
        'Shorthand for sending bytes to the minitel.'
        self.ser.write(data)

    def recv(self,byteCount):
        'Shorthand for retrieving a number of bytes from the minitel.'
        return self.ser.read(byteCount)
    
    def invalidate(self):
        self.textMode = None
        self.fg = -1
        self.bg = -1

    def setTextMode(self,textMode,force = False):
        if self.textMode == textMode and not force:
            return
        if self.isVT():
            if textMode & STRIKETHROUGH or textMode & UNDERLINE: 
                raise ValueError('Illegal ANSI text mode')
            if textMode == NORMAL: self.send(ESC+'\x4c')
            if textMode & TALL: self.send(ESC+'\x4d')
            if textMode & WIDE: self.send(ESC+'\x4e')
            if textMode & BLINK: self.send(ESC+'\x48')
            if textMode & BOLD: self.setColors(7,0)
            if textMode & INVERTED: self.setColors(0,7)
        else:
            if textMode & TALL or textMode & WIDE: 
                raise ValueError('Illegal ANSI text mode')
            if textMode & BLINK: self.send(SGR(5))
            if textMode & BOLD: self.send(SGR(1))
            if textMode & INVERTED: self.send(SGR(7))
            if textMode & STRIKETHROUGH: self.send(SGR(9))
            if textMode & UNDERLINE: self.send(SGR(4))
            elif textMode == NORMAL: self.send(SGR(0))
        self.textMode = textMode

    def moveCursor(self,x,y):
        if self.isVT():
            self.send('\x1f'+chr(65+y)+chr(65+x))
        else:
            self.send(CSI+str(y)+';'+str(x)+'H')

    def showCursor(self,on=True):
        if self.isVT():
            if on:
                self.send('\x11')
            else:
                self.send('\x14')

    def setColors(self,fg=-1,bg=-1):
        if fg < -1 or fg > 7:
            raise ValueError('Foreground out of range: {0}'.format(fg))
        if bg < -1 or bg > 7:
            raise ValueError('Background out of range: {0}'.format(bg))
        if fg != -1 and fg != self.fg:
            if self.isVT():
                self.send(ESC+chr(0x40 + fg))
            else:
                self.send(SGR(str(30 + fg)))
            self.fg = fg
        if bg != -1 and bg != self.bg:
            if self.isVT():
                self.send(ESC+chr(0x50 + bg))
            else:
                self.send(SGR(str(40 + bg)))
            self.bg = bg

    def wait(self):
        'Wait for all data to be transmitted.'
        self.ser.flush()
            
if __name__ == '__main__':
    parser = ArgumentParser(description='Write data to minitel terminal.')
    parser.add_argument('--baud', type=int, default=4800)
    parser.add_argument('--ansi', action='store_true', help='Assume minitel in ANSI mode')
    parser.add_argument('--port', default='/dev/ttyUSB0')
    parser.add_argument('--nocrlf', dest='crlf', action='store_false')
    parser.add_argument('--clear', action='store_true')
    parser.add_argument('--prechar', type=int, default=0)
    parser.add_argument('--chartest', action='store_true')
    parser.add_argument('--vidtexcolor', action='store_true')
    parser.add_argument('--vidtexglyph', action='store_true')
    parser.add_argument('--hexmode', action='store_true')
    parser.add_argument('paths', nargs='*')
    args = parser.parse_args()

    print('Port {0}, baud {1}'.format(args.port,args.baud))

    m = Minitel(port=args.port,baud=args.baud)
    if args.ansi:
        m.setMode(MODE_ANSI)

    if args.clear:
        m.clearScreen()
    if args.prechar:
        m.ser.write(chr(args.prechar))
    if args.hexmode:
        for c in args.paths:
            m.ser.write(chr(int(c,16)))
    elif len(args.paths) > 0:
        for path in args.paths:
            f = open(path)
            for line in f.readlines():
                m.ser.write(line)
                if args.crlf:
                    m.ser.write('\r')
    elif args.vidtexcolor:
        for i in range(8):
            for j in range(8):
                m.setColors(i,j)
                m.send(' {0}{1} '.format(i,j))
            m.newline()
    elif args.vidtexglyph:
        m.ser.write('\x0e')
        for i in range(32,128):
            m.ser.write('\x1b\x47\x1b\x50 ')
            m.ser.write('\x1b\x46\x1b\x54')
            m.ser.write(chr(i))
            if i%8 == 7:
                m.ser.write('\n')
                if args.crlf:
                    m.ser.write('\r')
                m.ser.write('\n')
                if args.crlf:
                    m.ser.write('\r')
    elif args.chartest:
        for i in range(32,128):
            m.moveCursor(1+ ((i%8)*4) , 1+ ((i-32)/8))
            m.ser.write(chr(i))
    else:
        for line in sys.stdin:
            m.ser.write(line)
            if args.crlf:
                m.ser.write('\r')




