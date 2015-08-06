# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:15:35 2015

@author: - -
"""

def oneline(file):
    try:
        with open(file) as f:
            line = f.readline()
            while line:
                yield line
                line = f.readline()
    except:
        pass


a=oneline('url.txt')
n=0
for i in a:
    print(i,end='')
    if n == 100: break
    n+=1
