# -*- coding: utf-8 -*-
"""
Created on Fri Aug 04 18:21:10 2017

@author: Kim
"""

#!/usr/bin/python
from multiprocessing import Process, Lock
import time

mutex = Lock()
# Define a function for the thread
def print_time( threadName, delay):
    with mutex:
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   t1 = Process( target = print_time, args = ("Thread-1", 0.1, ) )
   t1.start()
   t2 = Process( target = print_time, args = ("Thread-2", 0.1, ) )
   t2.start()
except:
   print("Error: unable to start thread")
