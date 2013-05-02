#!/usr/bin/env python

from argparse import ArgumentParser
import serial
import sys

if __name__ == '__main__':
    parser = ArgumentParser(description='Write data to minitel terminal.')
    parser.add_argument('--baud', type=int, default=4800)
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

    ser = serial.Serial(args.port,args.baud,
                        parity=serial.PARITY_EVEN,
                        bytesize=serial.SEVENBITS)

    if args.clear:
        ser.write('\x1b[2J')
        ser.write('\x0c')
    if args.prechar:
        ser.write(chr(args.prechar))
    if args.hexmode:
        for c in args.paths:
            ser.write(chr(int(c,16)))
    elif len(args.paths) > 0:
        for path in args.paths:
            f = open(path)
            for line in f.readlines():
                ser.write(line)
                if args.crlf:
                    ser.write('\r')
    elif args.vidtexcolor:
        for i in range(8):
            for j in range(8):
                ser.write('\x1b{0}\x1b{1} {2}{3} '.format(chr(0x40+i),chr(0x50+j),i,j))
            ser.write('\n')
            if args.crlf:
                ser.write('\r')
    elif args.vidtexglyph:
        ser.write('\x0e')
        for i in range(32,128):
            ser.write('\x1b\x47\x1b\x50 ')
            ser.write('\x1b\x46\x1b\x54')
            ser.write(chr(i))
            if i%8 == 7:
                ser.write('\n')
                if args.crlf:
                    ser.write('\r')
                ser.write('\n')
                if args.crlf:
                    ser.write('\r')
    elif args.chartest:
        for i in range(32,128):
            ser.write('{1}  '.format(hex(i),chr(i)))
            if i%8 == 7:
                ser.write('\n')
                if args.crlf:
                    ser.write('\r')
    else:
        for line in sys.stdin:
            ser.write(line)
            if args.crlf:
                ser.write('\r')




