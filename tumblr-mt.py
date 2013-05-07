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
keydata = json.load(open('apikey'))
cons_key = keydata['Consumer Key']
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
        m.send(''.join(r))
        tf.close()
        m.wait()
        time.sleep(2.2)



