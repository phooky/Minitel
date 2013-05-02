#!/usr/bin/env python

import minitel
from minitel import Minitel
import unittest

class FakeSerial():
    def __init__(self):
        self.closed=False
        self.clear()
    def clear(self):
        self.written=''
        self.buffer=''
    def write(self,data):
        if self.closed: raise IOError('Write to closed port')
        self.written = self.written + data
    def read(self,size=1):
        if self.closed: raise IOError('Read from closed port')
        b = self.buffer[:size]
        self.buffer = self.buffer[size:]
        return b
    def addInput(self,data):
        self.buffer = self.buffer + data
    def close(self):
        if self.closed: raise IOError('Double close')
        self.closed = True
    
class testMinitel(unittest.TestCase):
    def setUp(self):
        'Give every test case a fakeserial and minitel for either mode.'
        self.fser = FakeSerial()
        self.miniv = Minitel(self.fser, mode=minitel.MODE_VIDEOTEX)
        self.minia = Minitel(self.fser, mode=minitel.MODE_ANSI)


    def testBadMode(self):
        'Ensure that a bad mode value raises a ValueError.'
        self.assertRaises(ValueError, Minitel.setMode, self.miniv, 100)

    def testClearVideotex(self):
        'Test clear screen for videotex'
        self.miniv.clearScreen()
        self.assertEquals(self.fser.written,'\x0c')

    def testClearANSI(self):
        'Test clear screen for ANSI'
        self.minia.clearScreen()
        self.assertEquals(self.fser.written,'\x1b[2J')

    def testNewline(self):
        self.minia.newline()
        self.assertIn(self.fser.written,['\n\r','\r\n'])

    def testSend(self):
        teststr = 'fdasjkl23rlfds18u89dsf'
        self.minia.send(teststr)
        self.assertEquals(self.fser.written, teststr)

    def testRecv(self):
        self.assertEquals(self.minia.recv(4),'')
        self.fser.addInput('123456')
        self.assertEquals(self.minia.recv(4),'1234')
        self.assertEquals(self.minia.recv(4),'56')
    
    def testTextmodeVideotex(self):
        'Test text modes for videotex'
        acc = ''
        self.miniv.setTextMode(minitel.NORMAL)
        self.assertEquals(self.fser.written,acc)
        self.miniv.setTextMode(minitel.TALL)
        acc = acc + '\x1b\x4d'
        self.assertEquals(self.fser.written, acc)
        self.miniv.setTextMode(minitel.TALL)
        self.assertEquals(self.fser.written, acc)
        self.miniv.setTextMode(minitel.WIDE)
        acc = acc + '\x1b\x4e'
        self.assertEquals(self.fser.written, acc)
        self.miniv.setTextMode(minitel.BLINK)
        acc = acc + '\x1b\x48'
        self.assertEquals(self.fser.written, acc)
        self.miniv.setTextMode(minitel.NORMAL)
        acc = acc + '\x1b\x4c'
        self.assertEquals(self.fser.written, acc)

    def testTextmodeANSI(self):
        'Test text modes for ANSI'
        acc = ''
        self.minia.setTextMode(minitel.NORMAL)
        self.assertEquals(self.fser.written,acc)
        self.assertRaises(ValueError, Minitel.setTextMode, self.minia, minitel.TALL)
        self.assertRaises(ValueError, Minitel.setTextMode, self.minia, minitel.WIDE)
        self.minia.setTextMode(minitel.BLINK)
        self.minia.setTextMode(minitel.NORMAL)
        self.assertEquals(self.fser.written, '\x1b[5m\x1b[0m')

    def testSetColorsVideotex(self):
        'Test set colors for videotex'
        self.miniv.setColors(5,2)
        self.miniv.setColors(5,3)
        self.miniv.setColors(6)
        self.miniv.setColors(bg=6)
        self.miniv.setColors(7,0)
        def c(x): return '\x1b'+chr(x)
        self.assertEquals(self.fser.written, c(0x45)+c(0x52)+c(0x53)+c(0x46)+c(0x56)+c(0x47)+c(0x50))

    def testSetColorsANSI(self):
        'Test set colors for ANSI'
        self.minia.setColors(5,2)
        self.minia.setColors(5,3)
        self.minia.setColors(6)
        self.minia.setColors(bg=6)
        self.minia.setColors(7,0)
        def c(x): return '\x1b['+str(x)+'m'
        self.assertEquals(self.fser.written, c(35)+c(42)+c(43)+c(36)+c(46)+c(37)+c(40))
        
if __name__ == '__main__':
    unittest.main()
