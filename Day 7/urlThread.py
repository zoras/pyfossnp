from threading import Thread
import time
from urllib import urlopen

class url_get(Thread):
    def __init__(self,url):
        Thread.__init__(self)
        self.url = url
    
    def run(self):
            code = urlopen(self.url).read()
            print self.url, len(code)

file = open("urls.txt", 'r')
num = 1;
for line in file:
    url = 'count',num
    url = url_get(line)
    url.start()
    num = num + 1