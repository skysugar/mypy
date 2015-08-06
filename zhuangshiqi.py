# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:36:44 2015

@author: 0_0
"""

def log(func):
    def walls(*args,**kw):
        print("start-----------")
        a=func(*args,**kw)
        print("end-------------")
        return a
    return walls



@log
def g(n):
    print(n+n)
    return n*n



a=g(8)
print(a)
