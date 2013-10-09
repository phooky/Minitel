import minitel
import time
import logging
import textwrap
from screen import Screen
from run_process import make_run_process

class Menu(Screen):
    'Create a minitel selection menu'
    timeout = 60*5 # Standard menu timeout: five minutes
    def initialize(self,block):
        self.block = block
        self.name = block.name
        self.entries = []
        if len(block.lines) < 1:
            raise BlockParsingException("Empty menu")
        if block.lines[0].startswith('+'):
            logging.info("Warning: menu with no title.")
            self.title = ''
            items = block.lines[:]
        else:
            self.title = block.lines[0]
            items = block.lines[1:]
        for item in items:
            if not item:
                pass # ignore blank lines
            elif not item.startswith('+'):
                raise BlockParsingException("Bad menu entry {}".format(item))
            else:
                s = item[1:].split(':',1)
                if len(s) < 2:
                    raise BlockParsingException("No colon in entry {}".format(item))
                self.entries.append(s)

    def show(self,m):
        m.clearScreen()
        self.show_breadcrumbs(m)
        if self.title:
            x = (40 - len(self.title))/2
            m.moveCursor(x,3)
            m.setTextMode(minitel.TALL)
            m.send(self.title)
            m.setTextMode(minitel.NORMAL)
        for i in range(len(self.entries)):
            m.moveCursor(4,6+i)
            m.setColors(7)
            m.send('{}'.format(i+1))
            m.setColors(5)
            m.send('. {}'.format(self.entries[i][0]))
        m.setColors(1,0)
        m.moveCursor(0,8+len(self.entries))
        m.send('Enter a number from the menu above')
        if len(self.parents) > 0:
            m.send('\n\ror "0" to return to the previous menu')

    def __call__(self,m,parents):
        self.parents = parents
        self.run(m)

    def invoke(self,m,key):
        fn = self.content.get(key,None)
        if not fn:
            kval = key.split(' ')
            ktype = kval.pop(0)
            if ktype == 'run':
                logging.debug('running...')
                args = {}
                try:
                    while len(kval) and kval[0].find('=') != -1:
                        argk,argv = kval.pop(0).split('=',1)
                        args[argk]=argv
                    args['command'] = kval
                except:
                    logging.exception('oops')
                logging.debug('call with {}'.format(args))
                fn = make_run_process(**args)

        logging.debug('Calling {}'.format(fn))
        try:
            fn(m,self.parents[:]+[self])
        except:
            logging.exception('Exception while running function')
            logging.debug('Returning from {}'.format(fn))
        finally:
            logging.debug("VIDEOTEX NOW")
            m.setMode(minitel.MODE_VIDEOTEX)
            

    def run(self,m):
        logging.info('Entering menu {}.'.format(self.name))
        start_time = time.time()
        self.show(m)
        while time.time() - start_time < Menu.timeout:
            t = m.recv(1)
            if t:
                logging.debug('Keypress {}'.format(t))
                # attempt action
                if t == 0xED:
                    logging.info("Wakeup recieved.")
                    self.show(m)
                try:
                    val = int(t)
                    if val == 0 and len(self.parents) > 0:
                        logging.info('Returning to parent menu.')
                        return
                    elif val > 0 and val < len(self.entries)+1:
                        idx = val - 1
                        key = self.entries[idx][1]
                        self.invoke(m,key)
                        self.show(m)
                except:
                    pass
                start_time = time.time()
            else: time.sleep(0.1)
        logging.info('Menu timed out.')
