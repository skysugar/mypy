#!/usr/bin/env python
# -*- coding:utf-8 -*-

class wrapper:
    def __init__(self,cls):
        self.cls = cls
        self.newcls = None
    def __call__(self,*args,**kwargs):
        if self.newcls == None:
            a,b = args
            a += 1
            b += 1
            args = (a,b)
            self.newcls = self.cls(*args,**kwargs)
        return self.newcls

@wrapper
class A:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def sum(self):
        return self.x + self.y


a = A(3,4)
n = a.sum()
print(n)
