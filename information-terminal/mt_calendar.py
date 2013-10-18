import json
import urllib
import datetime
import dateutil.parser
from screen import Screen
import time
import minitel
import logging

cal_url = "https://www.googleapis.com/calendar/v3/calendars/p2m2av9dhrh4n1ub7jlsc68s7o%40group.calendar.google.com/events?orderBy=startTime&singleEvents=true&timeMax={}Z&timeMin={}Z&key={}"

f=open('gapi_key')
gapi_key=f.read()
f.close()

timeout = 60*6

class Calendar(Screen):
    def __init__(self):
        self.parents=[]
        self.content = None
        self.name = "Upcoming Events"

    def fetch(self):
        start = datetime.datetime.now()
        td = datetime.timedelta(30)
        end = start + td
        prep = cal_url.format(urllib.quote(end.isoformat('T')),
                              urllib.quote(start.isoformat('T')),
                              gapi_key)
        items = json.load(urllib.urlopen(prep))
        def get_info(i):
            try:
                summary = i['summary']
            except KeyError:
                logging.error(json.dumps(i))
            start = dateutil.parser.parse(i['start']['dateTime'])
            return (summary,start)
        def is_visible(i):
            v = i.get('visibility','default')
            return v in ['default','public']
        return map(get_info,filter(is_visible,items['items']))

    def draw(self, m):
        m.clearScreen()
        self.show_breadcrumbs(m)
        m.moveCursor(0,1)
        for (s,d) in self.items[:10]:
            d1=d.strftime(" %a %B %d, %Y")
            d2=d.strftime("%I:%M%p")
            gap=38-(len(d1)+len(d2))
            m.setColors(1,6,True)
            m.send(d1+" "*gap+d2+"\n\r")
            m.setColors(5,0)
            m.send(s+"\n\r")
        m.moveCursor(0,23)
        m.setTextMode(minitel.NORMAL)
        m.setColors(2,0)
        m.send("  Q: exit")

    def run(self, m):
        self.curpage = 0
        start_time = time.time()
        self.items = self.fetch()
        self.draw(m)
        self.eat(m)
        while time.time() - start_time < timeout:
            t = m.recv(1)
            if t:
                logging.debug('Keypress {}'.format(t))
                # attempt action
                try:
                    if t in 'Qq0\n\r':
                        return
                except:
                    logging.exception('oops')
                start_time = time.time()
            else: time.sleep(0.1)
        logging.info('Calendar timed out.')

    def __call__(self,m,parents):
        self.parents = parents
        self.run(m)

