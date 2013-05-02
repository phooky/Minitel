#!/usr/bin/env python

import minitel
from minitel import Minitel
import unittest

class FakeSerial():
    def __init__(self):
        self.closed=False
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
        
if __name__ == '__main__':
    unittest.main()
