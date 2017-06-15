import re
import threading
from selenium import webdriver

class google:

    def __init__(self):
        self.url = 'http://www.google.com'
        self.event = threading.Event()
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        self.urls = []
        while 'Google' not in self.driver.title:
            self.event.wait(1)

    def regurls(self):
        #'<a href="http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000" onmousedown="return rwt'
        #<a href="(.*?)" onmousedown="return rwt
        # print(self.driver.title)
        # print(self.driver.page_source)
        u = re.findall(r'<a href="(.*?)" onmousedown', self.driver.page_source)
        for i in u:
            if 'support.google.com' in i or i in self.urls:
                pass
            else:
                self.urls.append(i)

    def monitor(self):
        nowurl = self.driver.current_url
        while 1:
            if self.driver.current_url == nowurl:
                self.event.wait(1)
            else:
                self.regurls()
                nowurl = self.driver.current_url
                self.event.wait(1)

    def quit(self):
        self.driver.quit()


g = google()
p = threading.Thread(target=g.monitor, args=(), name='monitor')
p.start()
while True:
    if g.urls:
        print(g.urls.pop())
    else:
        g.event.wait(1)

