#!/usr/bin/env python

# This code owes much to the image2minitel sketch:
#   https://github.com/sack/image2minitel

import PIL.Image as Image
import PIL.ImageOps as ImageOps
from argparse import ArgumentParser
import serial

class Converter:
    def __init__(self,image):
        self.img = image
    def videotex_repr(self):
        # first, convert image to grayscale
        im = self.img.convert("L")
        # resize
        im = im.resize((40*2,24*3),Image.ANTIALIAS)
        # normalize contrast
        im = ImageOps.autocontrast(im)
        # down to 3-bit
        im = ImageOps.posterize(im,3)
        def findDarkLight(image,x,y):
            """Find the darkest and lightest values for a 2x3 block"""
            c = []
            for i in range(2):
                for j in range(3):
                    c.append(im.getpixel((x+i,y+j)))
            # select the lightest and darkest pixels
            c.sort()
            return (c[0],c[-1])

        # define colorhack
        def colorhack(image,x,y):
            """Quantize a 2x3 block to two colors"""
            dark,light = findDarkLight(image,x,y)
            for i in range(2):
                for j in range(3):
                    v = im.getpixel((x+i,y+j))
                    if v-dark < light-v:
                        v = dark
                    else:
                        v = light
                    im.putpixel((x+i,y+j),v)
        # colorhack each 6-cell
        for i in range(40):
            for j in range(24):
                colorhack(im,i*2,j*3)
        def convcolor(value):
            # take the high three bits, and move the lsb to msb
            return (value >> 6) | ((value >> 3) & (1<<2))
        
        # define gencode
        def gencode(self,image,x,y):
            """generate display codes for 2x3 block"""
            dark,light = findDarkLight(image,x,y)
            v = 0
            for i, j in [(0,0),(1,0),(0,1),(1,1),(0,2),(1,2)]:
                v = (v >> 1)
                if im.getpixel((x+i,y+j)) == light:
                    v = v | (1 << 5)
            c = ''
            if light != self.lastlight:
                c = c + '\x1b' + chr(0x40+convcolor(light))
            if dark != self.lastdark:
                c = c + '\x1b' + chr(0x50+convcolor(dark))
            c = c + chr(32+v)
            self.lastlight,self.lastdark = light,dark
            return c

        # generate codes for videotex
        self.lastdark, self.lastlight = -255, -255
        codes = ''
        for j in range(24):
            for i in range(40):
                codes = codes + gencode(self,im,i*2,j*3)
            codes = codes
        return codes

if __name__ == '__main__':
    parser = ArgumentParser(description='Convert image to minitel videotex representation.')
    parser.add_argument('--output', type=str, default=None, help="write output to specified path")
    parser.add_argument('--clear', action='store_true', help="clear screen before write")
    parser.add_argument('--nomode', dest='mode', action='store_false', help="do not explicitly switch into graphics mode")
    parser.add_argument('path', nargs=1)
    args = parser.parse_args()
    c = Converter(Image.open(args.path[0]))
    r = c.videotex_repr()
    if args.output:
        f = open(args.output,'wb')
    else:
        import sys
        f = sys.stdout
    if args.mode:
        f.write('\x0e') # enter graphics mode
    if args.clear:
        f.write('\x0c')
    f.write(r)
    f.close()



