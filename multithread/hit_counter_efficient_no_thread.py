# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 21:11:29 2017

@author: Kim
"""
import time
import random

class LastCounter:
  def __init__(self):
    self.size = 60
    self.A = [0] * 60
    self.index = 0
    self.startTime = time.time()
    self.lastMinuteCount = 0
  def hit(self):
    self.lastIndex = self.index
    self.index = self.get_index()
    if self.lastIndex == self.index:
      self.A[self.index] += 1
      self.lastMinuteCount += 1
    else:
      for i in range(self.lastIndex+1, self.index+1):
        self.lastMinuteCount -= self.A[i]
        self.A[i] = 0
      self.A[self.index] = 1
      self.lastMinuteCount += 1
    s = sum(self.A)
    print("lastIndex = {}, index = {}, last minute count = {}, A = {}, sum(A) = {}"\
           .format(self.lastIndex, self.index, self.lastMinuteCount,\
                   self.A, s))     
  def get_index(self):
    curTime = time.time()
    timeElipse = int(curTime - self.startTime)
    print("timeElipse = {}".format(timeElipse))
    return timeElipse % self.size
   
    
lc = LastCounter()
for i in range(1000):
    lc.hit()
    time.sleep(random.random())
       
