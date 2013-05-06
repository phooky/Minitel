#!/usr/bin/env python

# This code owes much to the image2minitel sketch:
#   https://github.com/sack/image2minitel

import PIL.Image as Image
import PIL.ImageOps as ImageOps
from argparse import ArgumentParser
import serial

# ordering of subpixels (x,y) in a block
subpixels = [(0,0),(1,0),(0,1),(1,1),(0,2),(1,2)]

def findDarkLight(image,x,y):
    """Find the darkest and lightest values for a 2x3 block"""
    c = []
    for i, j in subpixels:
        c.append(image.getpixel((x+i,y+j)))
    # select the lightest and darkest pixels
    c.sort()
    return (c[0],c[-1])

def colorhack(image,x,y):
    """Quantize a 2x3 block to two colors"""
    dark,light = findDarkLight(image,x,y)
    for i, j in subpixels:
        v = image.getpixel((x+i,y+j))
        if v-dark < light-v:
            v = dark
        else:
            v = light
        image.putpixel((x+i,y+j),v)

def convcolor(value):
    """Convert a 256-level gray tone to a 3b minitel 1 tone"""
    # take the high three bits, and move the lsb to msb
    return (value >> 6) | ((value >> 3) & (1<<2))

class Converter:
    def __init__(self,image):
        self.img = image
    def videotex_repr(self,w =80,h =72):
        '''Return a list of strings, one for each line of characters
        in the converted image. The width and height are specified in
        subpixels, and are always rounded up to an even number (for x) or
        a multiple of 3 (for y).'''
        # tweak w and h to proper values
        w = ((w+1)/2)*2
        h = ((h+2)/3)*3
        # convert image to grayscale and resize
        im = self.img.convert("L")
        im = im.resize((w,h),Image.ANTIALIAS)
        # normalize contrast
        im = ImageOps.autocontrast(im)
        # down to 3-bit
        im = ImageOps.posterize(im,3)
        # colorhack each 6-cell
        for i in range(w/2):
            for j in range(h/3):
                colorhack(im,i*2,j*3)
        
        # define gencode
        def gencode(self,image,x,y):
            """generate display codes for 2x3 block"""
            dark,light = findDarkLight(image,x,y)
            v = 0
            for i, j in subpixels:
                v = (v >> 1)
                if image.getpixel((x+i,y+j)) == light:
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
        codes = []
        for j in range(h/3):
            codeline = ''
            for i in range(w/2):
                codeline = codeline + gencode(self,im,i*2,j*3)
            codes.append(codeline)
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
    for line in r:
        f.write(line)
    f.close()



