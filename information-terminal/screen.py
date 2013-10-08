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

    def show_breadcrumbs(self,m):
        m.moveCursor(0,0)
        m.setColors(1,0)
        breadcrumbs = " >".join([p.name+" " for p in self.parents])
        m.send(breadcrumbs)
        m.send("> ")
        m.setTextMode(minitel.BOLD)
        m.send(self.name)
