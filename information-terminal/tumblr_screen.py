from tumblr-mt

import logging
import minitel
import time
from screen import Screen
from tumblr_mt import loadKey, getTopics, showTopics

class TumblrScreen(Screen):

    def __call__(self,m,parents):
        self.parents = parents
        loadKey('../apikey')
        topics = getTopics()
        showTopics(topics)

