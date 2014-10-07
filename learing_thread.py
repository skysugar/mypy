#coding:utf8

import time
import _thread

la = ['a','b','c','d','e','f','g']
lb = ['1','2','3','4','5','6','7']

def lislist(lis,l):
    for i in lis:
        print(i)
        time.sleep(1)
    if lock.locked():
        l.release()

lock = _thread.allocate_lock()
lock.acquire()

_thread.start_new_thread(lislist,(la,lock))
_thread.start_new_thread(lislist,(lb,lock))


while lock.locked():
    time.sleep(0.001)
    pass
