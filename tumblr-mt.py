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
m.setVTMode(minitel.VT_GRAPHICS)
cons_key = 'HIyjBXdm0j0KPBh7HOjZRQHKCYsRbA5YcYTY9Q1aL4rette2zO'
apicall = 'http://api.tumblr.com/v2/tagged?tag={0}&api_key={1}'

for topic in sys.argv[1:]:
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
        m.send(r)
        tf.close()
        m.wait()
        time.sleep(2.2)



