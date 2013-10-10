import minitel
import time
import logging
import textwrap

class ScreenTimeoutException(Exception):
    pass

class BlockParsingException(Exception):
    def __init__(self,details):
        self.details = details
class Screen:
    def __init__(self):
        self.parents=[]
        self.content = None

    def eat(self,m):
        while len(m.recv(1)) == 0:
            pass #eat data

    def show_breadcrumbs(self,m):
        m.setTextMode(minitel.NORMAL,True)
        m.moveCursor(0,0)
        m.setColors(0,1)
        breadcrumbs = " > ".join(['']+[p.name for p in self.parents])
        m.send(breadcrumbs)
        m.send(" > ")
        m.setColors(6,1)
        m.send(self.name+' ')
        m.setColors(1,0)
