# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 19:46:05 2017

@author: Kim
"""

from queue import Queue
from threading import Thread, Lock, Condition
import time

class Producer(Thread):

    def __init__(self, sq):
        Thread.__init__(self)
        self.sq = sq

    def run(self):
        i = 0
        while i <= 20:
            self.sq.put(i)
            time.sleep(0.05)
            i += 1
        self.sq.cancel()
        
class Consumer(Thread):

    def __init__(self, sq):
        Thread.__init__(self)
        self.sq = sq

    def run(self):
        i = 0
        while i < 20:
            item = self.sq.get()
            print(item)
            time.sleep(0.1)
            i += 1
        self.sq.cancel()
        
class SyncQ(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.q = Queue()
        self.cond = Condition()
        self.max_num_el = 10000
        self.exitFlag = False
        
    def put(self, value):
        with self.cond:
            while self.q.qsize() > self.max_num_el:
                self.cond.wait()
            if self.exitFlag:
                return
            print("{} is putting item".format(self.getName()))
            self.q.put(value)
            if self.q.qsize() < self.max_num_el:
                self.cond.notify() 

    def get(self):
        with self.cond:
            while self.q.empty():
                print("{} is waiting...".format(self.getName()))
                self.cond.wait()
            print("{} is getting item...".format(self.getName()))
            item = self.q.get()
            if not self.q.empty():
                self.cond.notify()
        return item

    def cancel(self):
        with self.cond:
            self.exitFlag = True
            self.cond.notifyAll()
    
    def empty(self):
        return self.q.empty()

sq = SyncQ()
t1 = Producer(sq)
t2 = Consumer(sq)
t1.start()
t2.start()
t1.join()
t2.join()
