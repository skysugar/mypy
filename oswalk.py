#coding:utf8

import os
def findfile(path):
    flist=[]
    for i in os.walk(path):
    	for j in i[2]:
    		flist.append(os.path.join(i[0],j))
    return(flist)


for i in findfile('E:\ISO'):
    print(i)
