#!/usr/bin/env python

from argparse import ArgumentParser
import serial
import sys

# Minitel modes. Boots into Videotex.
MODE_VIDEOTEX = 0
MODE_ANSI = 1

# Text modes. Only valid in Videotex mode.
VT_NORMAL = 0
VT_TALL = 1
VT_WIDE = 2

class Minitel:
    def __init__(self,port=None,baud=4800,mode=MODE_VIDEOTEX):
        '''Construct a minitel interface on a given port.
        The port should be either a string describing the port,
        or a previously constructed serial object.'''
        self.setMode(mode)
        self.baud = baud
        if isinstance(port, basestring):
            self.portName = port
            self.ser = serial.Serial(port, baud, 
                                     parity = serial.PARITY_EVEN,
                                     bytesize = serial.SEVENBITS)
        else: # presume it's a previously opened port
            self.ser = port

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
        if self.isVT(): self.ser.write('\x0c')
        else: self.ser.write('\x1b[2J')
    
    def newline(self):
        'Send a newline/carriage return combo.'
        self.ser.write('\n\r')

    
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
                m.ser.write('\x1b{0}\x1b{1} {2}{3} '.format(chr(0x40+i),chr(0x50+j),i,j))
            m.ser.write('\n')
            if args.crlf:
                m.ser.write('\r')
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




