#!/usr/bin/env python
#coding:utf-8

import os,sys
import time
import sys
import pycurl

URL=sys.argv[1]

c = pycurl.Curl()
c.setopt(pycurl.URL,URL)
c.setopt(pycurl.CONNECTTIMEOUT,5)
c.setopt(pycurl.TIMEOUT,5)
c.setopt(pycurl.NOPROGRESS,1)
c.setopt(pycurl.FORBID_REUSE,1)
c.setopt(pycurl.MAXREDIRS,1)
c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)

logfile=os.path.dirname(os.path.realpath(__file__))+"/content.txt"
if not os.path.isfile(logfile):
    os.mknod(logfile)

indexfile = open(logfile,'wb')
c.setopt(pycurl.WRITEHEADER,indexfile)
c.setopt(pycurl.WRITEDATA,indexfile)
try:
    c.perform()
except Exception as err:
    print("connect error:%s" % str(err))
    indexfile.close()
    sys.exit()

NAMELOOKUP_TIME = c.getinfo(c.NAMELOOKUP_TIME)
CONNECT_TIME = c.getinfo(c.CONNECT_TIME)
PRETRANSFER_TIME = c.getinfo(c.PRETRANSFER_TIME)
STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)

TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
HTTP_CODE = c.getinfo(c.HTTP_CODE)
SIZE_DOWNLOAD = c.getinfo(c.SIZE_DOWNLOAD)
HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
SPEED_DOWNLOAD = c.getinfo(c.SPEED_DOWNLOAD)

print("HTTP状态码:%s" % HTTP_CODE)
print("DNS解析时间:%.2fms" % (NAMELOOKUP_TIME*1000))
print("建立连接时间:%.2fms" % (CONNECT_TIME*1000))
print("准备传输时间:%.2fms" % (PRETRANSFER_TIME*1000))
print("传输开始时间:%.2fms" % (STARTTRANSFER_TIME*1000))
print("传输结束总时间:%.2fms" % (TOTAL_TIME*1000))
print("下载数据包大小:%d bytes/s" % SIZE_DOWNLOAD)
print("HTTP头部大小:%d bytes/s" % HEADER_SIZE)
print("平均下载速度:%d bytes/s" % SPEED_DOWNLOAD)

indexfile.close()
c.close()
