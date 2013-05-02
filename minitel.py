#!/usr/bin/env python

from argparse import ArgumentParser
import serial
import sys

# Minitel modes. Boots into Videotex.
MODE_VIDEOTEX = 0
MODE_ANSI = 1

# Text modes. Tall and wide only valid in Videotex mode.
NORMAL = 0
TALL = 1
WIDE = 2
BLINK = 4

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
    def __init__(self,port=None,baud=4800,mode=MODE_VIDEOTEX):
        '''Construct a minitel interface on a given port.
        The port should be either a string describing the port,
        or a previously constructed serial object.'''
        self.setMode(mode)
        self.baud = baud
        self.textMode = NORMAL
        self.vtMode = VT_TEXT
        self.fg = 7
        self.bg = 0
        if isinstance(port, basestring):
            self.portName = port
            self.ser = serial.Serial(port, baud, 
                                     parity = serial.PARITY_EVEN,
                                     bytesize = serial.SEVENBITS,
                                     timeout = 0.1)
        else: # presume it's a previously opened port
            self.ser = port

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
        self.mode = mode

    def isVT(self):
        'Shorthand test to check for Videotex mode.'
        return self.mode == MODE_VIDEOTEX

    def clearScreen(self):
        'Clear the terminal.'
        if self.isVT(): self.send('\x0c')
        else: self.send('\x1b[2J')
    
    def newline(self):
        'Send a newline/carriage return combo.'
        self.send('\n\r')

    def send(self,data):
        'Shorthand for sending bytes to the minitel.'
        self.ser.write(data)

    def recv(self,byteCount):
        'Shorthand for retrieving a number of bytes from the minitel.'
        return self.ser.read(byteCount)
    
    def setTextMode(self,textMode):
        if self.textMode == textMode:
            return
        if self.isVT():
            if textMode == NORMAL: self.send(ESC+'\x4c')
            if textMode & TALL: self.send(ESC+'\x4d')
            if textMode & WIDE: self.send(ESC+'\x4e')
            if textMode & BLINK: self.send(ESC+'\x48')
        else:
            if textMode & TALL or textMode & WIDE: raise ValueError('Illegal ANSI mode')
            if textMode & BLINK: self.send(SGR('5'))
            elif textMode == NORMAL: self.send(SGR('0'))
        self.textMode = textMode

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
            m.ser.write('{1}  '.format(hex(i),chr(i)))
            if i%8 == 7:
                m.ser.write('\n')
                if args.crlf:
                    m.ser.write('\r')
    else:
        for line in sys.stdin:
            m.ser.write(line)
            if args.crlf:
                m.ser.write('\r')




