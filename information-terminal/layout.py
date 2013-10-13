import minitel
import mtimage
import time
import logging
import textwrap
import PIL.Image as Image
from screen import Screen

class Layout(Screen):
    'Create a minitel layout'
    def initialize(self,block):
        self.block = block
        self.name = block.name

    def draw_image(self,m,x,y,path):
        i = Image.open(path)
        c = mtimage.Converter(i)
        r = c.videotex_repr()
        for line in r:
            m.moveCursor(x,y)
            y = y + 1
            m.setVTMode(Minitel.VT_GRAPHICS)
            m.send(line)

    def draw_text(self,m,x,y,text):
        m.moveCursor(x,y)
        m.setVTMode(Minitel.VT_TEXT)
        m.setColors(7,0)
        m.send(text)

    def show(self,m):
        m.clearScreen()
        self.show_breadcrumbs(m)
        for line in block.lines:
            try:
                line = line.strip()
                if not line:
                    continue
                etype, x, y, data = line.split(' ',3)
                x = int(x)
                y = int(y)
                if etype == 'image':
                    draw_image(m,x,y,data)
                elif etype == 'text':
                    draw_text(m,x,y,text)
                else:
                    logging.error("Unrecognized line type {}".format(etype))
            except:
                logging.exception("Error parsing layout line {}".format(line))

    def __call__(self,m,parents):
        self.parents = parents
        self.run(m)
            
    def run(self,m):
        logging.info('Showing layout {}.'.format(self.name))
        self.show(m)
        while True:
            t = m.recv(1)
            if t:
                # attempt action
                if t in '0\n\rqQ':
                    return
            else: time.sleep(0.1)
