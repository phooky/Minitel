import minitel
import minitel_curses
import logging
import os
import sys
import time

if __name__ == '__main__':
    logging.basicConfig(filename='/var/log/minitel/main.log',level=logging.DEBUG)

from menu import Menu        
from run_process import make_run_process

def mpass(m,parents):
    pass

games = Menu('Games','Fun and Games', [
    ('TinyMUSH',make_run_process(['telnet','192.155.89.149','4201'],False)),
    ('Adventure Time',make_run_process('/usr/games/adventure',True)),
    ('Rogue',make_run_process('/usr/bin/rogue',False))
])

top = Menu('Main','Welcome to NYC Resistor', [
    ('Frequently Asked Questions',mpass),
    ('Play a game',games)
])
 
if __name__ == '__main__':
    port = os.getenv('PORT','/dev/ttyACM0')
    baud = int(os.getenv('BAUD','4800'))
    logging.info('Opening minitel on port {} at {} 8N1'.format(port,baud))
    try:
        if port == 'SIM':
            m = minitel_curses.MinitelCurses()
        else:
            m = minitel.Minitel(port,baud,minitel.MODE_VIDEOTEX,hax=True)
	while True:
            top.run(m,[])
    except:
        logging.exception('Could not open connection to minitel; aborting.')
        sys.exit(1)
    finally:
        m.close()

    
