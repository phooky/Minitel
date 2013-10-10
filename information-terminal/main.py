#!/usr/bin/python
import minitel
import minitel_curses
import logging
import os
import sys
import time
from mt_calendar import Calendar

if __name__ == '__main__':
    logging.basicConfig(filename='/var/log/minitel/main.log',level=logging.DEBUG)

from menu import Menu
from doc import Doc
from blockparser import parse_file
from run_process import make_run_process

def mpass(m,parents):
    pass

#games = Menu('Games','Fun and Games', [
#    ('TinyMUSH',make_run_process(['telnet','192.155.89.149','4201'],False)),
#    ('Adventure Time',make_run_process('/usr/games/adventure',True)),
#    ('Rogue',make_run_process('/usr/bin/rogue',False))
#])

#top = Menu('Main','Welcome to NYC Resistor', [
#    ('Frequently Asked Questions',mpass),
#    ('main.py',Pager('main code','main.py')),
#    ('Play a game',games)
#])

def eat(m):
    while len(m.recv(1)) == 0:
        pass
 
typemap = {
    'menu':Menu,
    'doc':Doc,
}

if __name__ == '__main__':
    port = os.getenv('PORT','/dev/ttyACM0')
    baud = int(os.getenv('BAUD','4800'))
    logging.info('Opening minitel on port {} at {} 8N1'.format(port,baud))
    content = {
        'calendar' : Calendar()
        }
    for (key,block) in parse_file('content/menus.mini').items():
        try:
            content[key] = typemap[block.type]()
            content[key].content = content
            content[key].initialize(block)
        except:
            content[key] = block
            logging.warning("Unknown block type {}".format(key))

    top = content['menu Main']
    
    try:
        if len(sys.argv)>1 and sys.argv[1] == 'sim':
            m = minitel_curses.MinitelCurses()
        else:
            m = minitel.Minitel(port,baud,minitel.MODE_VIDEOTEX,hax=True)
	while True:
            eat(m)
            top.run(m)
            logging.info('Top level menu exited; waiting for input.')
    except:
        logging.exception('Could not open connection to minitel; aborting.')
        sys.exit(1)
    finally:
        m.close()

    
