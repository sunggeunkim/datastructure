# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 19:46:05 2017

@author: Kim
"""

from Queue import Queue
from threading import Thread, Lock
import time

def producer(sq):
    i = 0
    while i <= 10:
        sq.put(i)
        time.sleep(0.1)
        i += 1
        
def consumer(sq):
    error = None
    while not error and not sq.empty():
        time.sleep(0.5)
        print(sq.get())
        
class SyncQ(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.q = Queue()
        
    def put(self, value):
        self.q.put(value)
        
    def get(self):
        if self.q.empty():
            print("Nothing to get")
            return None
        else:
            return self.q.get()
    
    def empty(self):
        return self.q.empty()

sq = SyncQ()
t1 = Thread(target=producer, args=(sq,))
t2 = Thread(target=consumer, args=(sq,))
t1.start()
t2.start()
while not sq.empty():
    print(sq.get())
t1.join()
t2.join()