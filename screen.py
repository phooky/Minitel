import mtimage
import minitel
import json

class Screen:
    def __init__(self,text):
        self.contents = json.loads(text)
    def render(self,m):
        m.clearScreen()
        for element in self.contents:
            t = element['type']
            if t == 'text':
                self.renderText(m,element)
            elif t == 'image':
                self.renderImage(m,element)
    def renderText(self,m,e):
        x = e.get('x',0)
        y = e.get('y',0)
        text = e.get('text','')
        fg = e.get('fg',7)
        bg = e.get('bg',0)
        m.moveCursor(x,y)
        m.setVTMode(minitel.VT_TEXT)
        m.setColors(fg,bg)
        m.send(text)

if __name__ == '__main__':
    m = minitel.Minitel('/dev/ttyUSB0')
    m.clearScreen()
    s = Screen('{}')
    s.renderText(m,{'x':14,'y':13,'text':'hello world'})

