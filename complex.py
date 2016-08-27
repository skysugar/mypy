#!/usr/bin/env python
# -*- coding:utf-8 -*-

#运算符重载
#help(int)

class A:
    def __init__(self,x):
        self.n = x
    def __add__(self, other):
        return A(self.n + other.n)
    def __sub__(self, other):
        return self.n - other.n

#A.__add__ = lambda self,other:print('fuck it')

a = A(8)
b = A(3)

c = a + b
d = a - b
print(c.n)
print(c)
print(d)
