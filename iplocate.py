# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 17:14:12 2015

@author: 0_0
"""

import urllib.request
import json
import sys

ip=sys.argv[1]
try:    
    req=urllib.request.urlopen("http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip)
    r=str(req.read(),encoding='utf-8')
    data=json.loads(r)['data']
    so = ['ip','isp','country','city','county','area']
    for i in so:
        if data[i]:
            print(data[i],end=' ')
except:
    print('Taobao:API Errot ...',end='')
