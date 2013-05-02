#!/usr/bin/env python

import minitel
import unittest

class FakeSerial():
    def __init__(self):
        self.closed=False
        self.written=''
    def write(self,data):
        if self.closed: raise IOError('Write to closed port')
        self.written = self.written + data
    def read(self):
        if self.closed: raise IOError('Read from closed port')
        return ''
    def close(self):
        if self.closed: raise IOError('Double close')
        self.closed = True
    
class testMinitel(unittest.TestCase):
    def testBadMode(self):
        m = minitel.Minitel(FakeSerial())
        self.assertRaises(ValueError, minitel.Minitel.setMode, m, 3)

if __name__ == '__main__':
    unittest.main()
