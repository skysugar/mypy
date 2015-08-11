#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.request

url="http://www.baidu.com"

def webline(url):
    req = urllib.request.urlopen(url)
    line = req.readline()
    while line:
        yield line
        line = req.readline()
    req.close()

baidu=webline(url)

for i in baidu:
    si=str(i,encoding='utf-8')
    print(si)
