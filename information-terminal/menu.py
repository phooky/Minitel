import minitel
import time

class Menu:
    'Create a minitel selection menu'
    timeout = 60*5 # Standard menu timeout: five minutes
    def __init__(self,name,title,entries):
        self.entries = entries
        self.name = name
        self.title = title
    def show(self,m,parents):
        breadcrumbs = " > ".join([p.name for p in parents])
        m.showCursor(False)
        m.clearScreen()
        m.setTextMode(minitel.NORMAL)
        m.send(breadcrumbs)
        m.send(" > ")
        m.setTextMode(minitel.BOLD)
        m.send(self.name)
        m.moveCursor(6,2)
        m.setTextMode(minitel.TALL | minitel.WIDE)
        m.send(self.title)
        m.setTextMode(minitel.NORMAL)
        for i in range(len(self.entries)):
            m.moveCursor(6,6+i)
            m.send('{}. {}'.format(i+1,self.entries[i][0]))
        m.moveCursor(0,7+len(self.entries))
        m.setTextMode(minitel.NORMAL)
        m.send('Enter a number from the menu above\n')
        m.send('or "0" to return to the previous menu')
    def __call__(self,m,parents):
        self.run(m,parents)
    def run(self,m,parents):
        self.show(m,parents)
        while time.time() - start_time < timeout:
            t = m.recv(1)
            if t:
                # attempt action
                try:
                    val = int(t)
                    if val == 0:
                        return
                    elif val < len(self.entries)+1:
                        idx = val - 1
                        fn = self.entries[idx][1]
                        fn(m,parents[:]+[self])
                start_time = time.time()
            else time.sleep(0.1)
            
