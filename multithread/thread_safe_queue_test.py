# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 19:46:05 2017

@author: Kim
"""

from collections import deque
from threading import Thread, Lock, Condition
import time

class Producer(Thread):

    def __init__(self, sq, list_of_numbers):
        Thread.__init__(self)
        self.sq = sq
        self.nums = list_of_numbers

    def run(self):
        for i in self.nums:
            self.sq.put(i)
            time.sleep(0.05)
        
class Consumer(Thread):

    def __init__(self, sq):
        Thread.__init__(self)
        self.sq = sq

    def run(self):
        while True:
            item = self.sq.get()
            print(item)
            time.sleep(0.01)
        
class SyncQ(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.q = deque()
        self.cond = Condition()
        self.max_num_el = 10000
        
    def put(self, value):
        with self.cond:
            while len(self.q) > self.max_num_el:
                self.cond.wait()
            self.q.append(value)
            if len(self.q) < self.max_num_el:
                # notify consumer that item is in the queue
                # so that it can be consumed. 
                self.cond.notify()

    def get(self):
        with self.cond:
            while len(self.q) == 0: # queue is empty. wait until item is in there.
                self.cond.wait()
            item = self.q.popleft()
            if len(self.q) > 0: 
                # queue is not empty.
                # notify other thread waiting for the queue to be filled.
                self.cond.notify()
        return item
    
    def empty(self):
        return len(self.q) == 0

sq = SyncQ()
t0 = Producer(sq, list(range(10)))
t1 = Producer(sq, list(range(10,20)))
t2 = Consumer(sq)
t3 = Consumer(sq)
t0.start()
t1.start()
t2.start()
t3.start()
t0.join()
t1.join()
t2.join()
t3.join()
