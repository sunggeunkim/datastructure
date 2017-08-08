# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 19:46:05 2017

@author: Kim
"""

from collections import deque
from threading import Thread, Lock, Condition
import time, random

class Producer(Thread):

    def __init__(self, sq):
        Thread.__init__(self)
        self.sq = sq

    def run(self):
       while True: 
            item = random.randint(0, 100)
            self.sq.put(item)
            self.log(item)
            time.sleep(0.001)

    def log(self, item):
        print("** {} produced {}.".format(self.getName(), item))
        
class Consumer(Thread):

    def __init__(self, sq):
        Thread.__init__(self)
        self.sq = sq

    def run(self):
        while True:
            item = self.sq.get()
            self.log(item)
            time.sleep(0.1)

    def log(self, item):
        print("{} consumed {}.".format(self.getName(), item))
        
class SyncQ(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.q = deque()
        self.cond = Condition()
        self.max_num_el = 100
        
    def put(self, value):
        with self.cond:
            while self.full():
                self.cond.wait()
            self.q.append(value)
            if not self.empty():
                # notify consumer that item is in the queue so that it can be consumed. 
                self.cond.notify()

    def get(self):
        with self.cond:
            while self.empty():
                # queue is empty. wait until the queue is populated.
                self.cond.wait()
            item = self.q.popleft()
            print("{} item left in the queue".format(len(self.q)))
            # notify producer to wake up to fill the queue
            if not self.full():
                self.cond.notify()
        return item
    
    def empty(self):
        return len(self.q) == 0

    def full(self):
        return len(self.q) >= self.max_num_el

sq = SyncQ()
Threads = []
for i in range(5):
    Threads.append(Producer(sq))
for i in range(5):
    Threads.append(Consumer(sq))

for t in Threads:
    t.start()
for t in Threads:
    t.join()
