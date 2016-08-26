import multiprocessing
import random
import os

event = multiprocessing.Event()

def produer(q):
    while True:
        n = random.randint(0,100)
        print('{} 生产出 ---> {}'.format(os.getpid(),n))
        q.put(n)
        event.wait(2)

def consumer(q):
    while True:
        n = q.get()
        print('{} 获得 <--- {}'.format(os.getpid(),n))
        event.wait(1)


q = multiprocessing.Queue()

pp = multiprocessing.Process(target=produer,name='producer',args=(q,))
pp1 = multiprocessing.Process(target=produer,name='producer1',args=(q,))
pc = multiprocessing.Process(target=consumer,name='consumer',args=(q,))

pp.start()
pp1.start()
pc.start()


pp1.join()
pp.join()
pc.join()
