import mtimage
import minitel
import json
import urllib2
import tempfile
import PIL.Image as Image
import time
import sys

m = minitel.Minitel('/dev/ttyUSB0')
m.clearScreen()
keydata = json.load(open('apikey'))
cons_key = keydata['Consumer Key']
apicall = 'http://api.tumblr.com/v2/tagged?tag={0}&api_key={1}'

def centeredText(m,y,text,fg=-1,bg=-1):
    x = (40 - len(text))/2
    if x < 0:
        x = 0
    m.moveCursor(x,y)
    m.setColors(fg,bg)
    m.send(text)

topics = sys.argv[1:]
if len(topics) == 0:
    m.setVTMode(minitel.VT_TEXT)
    centeredText(m,5,' WELCOME TO TUMBLR.COM ',7,5)
    centeredText(m,8,'Enter tags to browse separated',7,0)
    centeredText(m,9,'by commas. Hit return to begin.')
    m.moveCursor(0,11)
    m.send('>>> ')
    m.showCursor()
    line = m.readline()
    topics = [x.strip() for x in line.split(",")]
    print "Topics:",topics
    m.showCursor(False)
    m.clearScreen()

m.setVTMode(minitel.VT_GRAPHICS)
    
for topic in topics:
    a = json.load(urllib2.urlopen(apicall.format(topic,cons_key)))
    for elem in [x for x in a['response'] if x['type']=='photo']:
        url = elem['photos'][0]['alt_sizes'][-2]['url']
        tf=tempfile.TemporaryFile()
        print("Loading image from {0}.".format(url))
        tf.write(urllib2.urlopen(url).read())
        tf.seek(0)
        i = Image.open(tf)
        c = mtimage.Converter(i)
        r = c.videotex_repr()
        ts = elem['timestamp']
        m.send(''.join(r))
        tf.close()
        m.wait()
        time.sleep(2.2)



