import minitel
import time
import logging
import textwrap

def make_pager(path):
    logging.debug('Creating pager for {}'.format(path))
    def fn(m, parents):
        show_breadcrumbs(m,parents)

def show_breadcrumbs(m,parents):
    m.setMode(minitel.MODE_VIDEOTEX)
    breadcrumbs = " >".join([p.name+" " for p in parents])
    m.showCursor(False)
    m.clearScreen()
    m.setColors(7,0)
    m.setColors(1,0)
    m.send(breadcrumbs)

class Pager:
    def __init__(self,name,path):
        logging.debug('Creating pager for {}'.format(path))
        self.path = path
        self.name = name
        self.pages = []
        f = open(path)
        lines = []
        for line in f.readlines():
            lines = lines + textwrap.wrap(line,40)
        self.lines = lines
        self.pages = len(self.lines)/20
        f.close()
        
    def show(self, m, parents, page):
        show_breadcrumbs(m,parents)
        m.send("> ")
        m.setTextMode(minitel.BOLD)
        m.send(self.name)
        m.setColors(1,0)
        m.send(" page {} of {}".format(page+1,self.pages))
        li = 3
        for line in self.lines[page*20:(page+1)*20]:
            m.moveCursor(0,li)
            m.send(line)
            li = li + 1    
    def run(self, m, parents):
        page = 0
        start_time = time.time()
        self.show(m,parents,page)
        while time.time() - start_time < Menu.timeout:
            t = m.recv(1)
            if t:
                logging.debug('Keypress {}'.format(t))
                # attempt action
                try:
                    if t == '>' or t == ' ':
                        logging.info('Next.')
                        if page+1 < self.pages:
                            page = page + 1
                            m.show(m,parents,page)
                        return
                    elif t == '<' or t == 'p':
                        logging.info('Prev.')
                        if page > 0:
                            page = page - 1
                            m.show(m,parents,page)
                    elif t == 'q' or t == '\n' or t == '\r':
                        return
                start_time = time.time()
            else: time.sleep(0.1)
        logging.info('Menu timed out.')
    def __call__(self,m,parents):
        self.run(m,parents)

class Menu:
    'Create a minitel selection menu'
    timeout = 60*5 # Standard menu timeout: five minutes
    def __init__(self,name,title,entries):
        self.entries = entries
        self.name = name
        self.title = title
    def show(self,m,parents):
        show_breadcrumbs(m,parents)
        m.send("> ")
        m.setTextMode(minitel.BOLD)
        m.setTextMode(minitel.BLINK)
        m.send(self.name)
        x = (40 - len(self.title))/2
        m.moveCursor(x,3)
        m.setTextMode(minitel.TALL)
        m.send(self.title)
        m.setTextMode(minitel.NORMAL)
        for i in range(len(self.entries)):
            m.moveCursor(4,6+i)
            m.setColors(7,0)
            m.send('{}'.format(i+1))
            m.setColors(1,0)
            m.send('. {}'.format(self.entries[i][0]))
        m.setColors(1,0)
        m.moveCursor(0,8+len(self.entries))
        m.send('Enter a number from the menu above')
        if len(parents) > 0:
            m.send('\n\ror "0" to return to the previous menu')
    def __call__(self,m,parents):
        self.run(m,parents)
    def run(self,m,parents):
        logging.info('Entering menu {}.'.format(self.name))
        start_time = time.time()
        self.show(m,parents)
        while time.time() - start_time < Menu.timeout:
            t = m.recv(1)
            if t:
                logging.debug('Keypress {}'.format(t))
                # attempt action
                try:
                    val = int(t)
                    if val == 0:
                        logging.info('Returning to parent menu.')
                        return
                    elif val > 0 and val < len(self.entries)+1:
                        idx = val - 1
                        fn = self.entries[idx][1]
                        logging.debug('Calling {}'.format(fn))
                        try:
                            fn(m,parents[:]+[self])
                        except:
                            logging.exception('Exception while running function')
                        logging.debug('Returning from {}'.format(fn))
                        self.show(m,parents)
                except:
                    pass
                start_time = time.time()
            else: time.sleep(0.1)
        logging.info('Menu timed out.')
