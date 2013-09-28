import minitel
import minitel_curses
import logging
from os import getenv
import sys

from menu import Menu        

def mpass(m,parents):
    pass

top = Menu('Main Menu','Welcome to NYC Resistor', [
    ('Introduction',mpass),
    ('Submenu',Menu('Submenu A', 'Submenu A', [
        ('Submenu',Menu('Submenu B', 'Submenu B', [('ha',mpass),('woo',mpass)])),
        ('foo',mpass),
        ('bar',mpass)])),
    ('Post-introduction',mpass)])

if __name__ == '__main__':
    logging.basicConfig(filename='/var/run/minitel/main.log',level=logging.DEBUG)
    port = getenv('PORT','/dev/ttyUSB0')
    baud = int(getenv('BAUD','4800'))
    logging.info('Opening minitel on port {} at {} 8N1'.format(port,baud))
    try:
        #m = minitel.Minitel(port,baud)
        m = minitel_curses.MinitelCurses()
        while True:
            top.run(m,[])
    except:
        logging.exception('Could not open connection to minitel; aborting.')
        sys.exit(1)

    
