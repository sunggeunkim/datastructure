# -*- coding: utf-8 -*-
"""
Created on Fri Aug 04 18:21:10 2017

@author: Kim
"""

#!/usr/bin/python

import threading
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   t1 = threading.Thread( target = print_time, args = ("Thread-1", 2, ) )
   t1.start()
   t2 = threading.Thread( target = print_time, args = ("Thread-2", 2, ) )
   t2.start()
except:
   print("Error: unable to start thread")
