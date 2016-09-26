#!/usr/bin/env python
#coding:utf-8

import pymysql


class src:
    def __init__(self,host,user,passwd,dbname):
        self.conn = pymysql.connect(host,user,passwd,dbname, use_unicode=True, charset="utf8")
        self.cursor = self.conn.cursor()
        self.data = self.getdata()

    def __iter__(self):
        return self

    def __next__(self):
        self.i = self.data.__next__()
        if self.i:
            return self.i
        raise StopIteration

    @property
    def totalnum(self):
        sql = 'select count(*) from table'
        self.cursor.execute(sql)
        totalnum = self.cursor.fetchall()
        return totalnum[0][0]

    def getdata(self):
        sql = 'select * from table'
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        yield from data




s = src('127.0.0.1', 'user', 'pass', 'dbname')
for i in s:
    print(i)

