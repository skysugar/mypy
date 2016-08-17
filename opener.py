#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
from http import cookiejar


def makebrowser():
    UA='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36'
    cookie = cookiejar.MozillaCookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    opener.addheaders = [('User-agent',UA)]
    return opener

def fixUA(headers,referer):
    rlst = []
    for i,j in headers:
        if i != 'referer':
            rlst.append((i,j))
    rlst.append(('referer',referer))
    return rlst

a = makebrowser()
r = a.open('http://127.0.0.1/')
print(a.addheaders)
a.addheaders.append(('Referer','http://127.0.0.1/'))
r = a.open('http://127.0.0.1/b.html')
print(a.addheaders)
