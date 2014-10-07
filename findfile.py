#coding:utf8

import os

def dirlist(path):
    try:
        os.chdir(path)
        pwd = os.getcwd()
        for i in os.listdir(path):
            filepath=os.path.join(pwd,i)
            if os.path.isdir(filepath):
                dirlist(filepath)
            else:
                print(filepath)
    except PermissionError as strr:
        print(strr)
        pass
        


dirlist('e:\\')

