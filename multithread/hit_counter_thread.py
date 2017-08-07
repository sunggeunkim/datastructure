# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 12:22:13 2017

@author: Kim
"""

from threading import Thread, Lock
import time

class Request:
    def __init__(self, time):
        self.time = time
        self.next = None

class HitCounter(Thread):
    def __init__(self, delay):
        Thread.__init__(self)
        self.last_sec_count = 0
        self.last_min_count = 0
        self.last_hour_count = 0
        self.request_list_tail = None
        self.sec_ago = None
        self.min_ago = None
        self.hour_ago = None
        self.delay = delay
        self.lock = Lock()
        
    def update_sec_pointer(self, t):
        self.lock.acquire()
        try:
            while self.sec_ago and t - self.sec_ago.time > 1:
                self.sec_ago = self.sec_ago.next
                self.last_sec_count -= 1
        finally:
            self.lock.release()
            
    def update_min_pointer(self, t):        
        self.lock.acquire()
        try:
            while self.min_ago and t - self.min_ago.time > 60:
                self.min_ago = self.min_ago.next
                self.last_min_count -= 1
        finally:
            self.lock.release()
            
    def update_hour_pointer(self, t):        
        self.lock.acquire()
        try:
            while self.hour_ago and t - self.hour_ago.time > 3600:
                self.hour_ago = self.hour_ago.next
                self.last_hour_count -= 1
        finally:
            self.lock.release()
    
    def add_request(self, t):        
        lock.acquire()
        try:
            self.last_sec_count += 1
            self.last_min_count += 1
            self.last_hour_count += 1
            new_request = Request(t)
            if self.sec_ago == None: self.sec_ago = new_request
            if self.min_ago == None: self.min_ago = new_request
            if self.hour_ago == None: self.hour_ago = new_request
            if self.request_list_tail == None:            
                self.request_list_tail = new_request
            else:            
                self.request_list_tail.next = new_request
                self.request_list_tail = new_request
        finally:
            lock.release()
            
    def get_last_hour_count(self):
        self.update_hour_pointer(time.time())
        return self.last_hour_count
    
    def get_last_min_count(self):
        self.update_min_pointer(time.time())
        return self.last_min_count
    
    def get_last_sec_count(self):
        self.update_sec_pointer(time.time())
        return self.last_sec_count

    def add_1000_request(self, delay):
        for i in range(1000):
            time.sleep(delay)
            self.add_request(time.time())
    
    def run(self):
        self.add_1000_request(self.delay)
        
hc = HitCounter(0.001)
hc1 = HitCounter(0.001)
hc.start()
hc1.start()
time.sleep(0.5)
print(hc.get_last_sec_count())
print(hc1.get_last_sec_count())
hc1.join()
hc.join()
print('last min count for {} is {}'.format(hc.getName(), hc.get_last_min_count()))
print('last_min_count for {} is {}'.format(hc1.getName(), hc1.get_last_min_count()))

print(hc.get_last_sec_count())
print(hc1.get_last_sec_count())