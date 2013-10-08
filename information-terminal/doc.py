import minitel
import time
import logging
import textwrap
from screen import Screen

height=20
timeout = 60 * 5

class Doc(Screen):
    def initialize(self,block):
        logging.debug('Creating document for {}'.format(block.name))
        self.name = block.name
        self.pages = []
        lines = []
        for line in block.lines:
            lines = lines + textwrap.wrap(line,40)
        self.lines = lines
        self.pages = (len(self.lines)+height-1)/height
        self.curpage = 0

    def draw(self, m):
        page = self.curpage
	logging.debug("page {}".format(page))
        m.clearScreen()
        self.show_breadcrumbs(m)
        m.setColors(1,0)
        m.send(" page {} of {}".format(page+1,self.pages))
        li = 2
        for line in self.lines[page*height:(page+1)*height]:
            m.moveCursor(0,li)
            m.send(line)
            li = li + 1    
        m.moveCursor(0,23)
        m.setColors(1,0)
        m.send("N: next page  P: previous page  Q: exit")

    def run(self, m):
        self.curpage = 0
        start_time = time.time()
        self.draw(m)
        while time.time() - start_time < timeout:
            t = m.recv(1)
            if t:
                logging.debug('Keypress {}'.format(t))
                # attempt action
                try:
                    if t in '>nN ':
                        logging.info('Next.')
                        if self.curpage+1 < self.pages:
                            self.curpage = self.curpage + 1
                            self.draw(m)
                    elif t in '<pPbB':
                        logging.info('Prev.')
                        if self.curpage > 0:
                            self.curpage = self.curpage - 1
                            self.draw(m)
                    elif t in 'Qq0\n\r':
                        return
                except:
                    logging.exception('oops')
                start_time = time.time()
            else: time.sleep(0.1)
        logging.info('Menu timed out.')
    def __call__(self,m,parents):
        self.parents = parents
        self.run(m)
