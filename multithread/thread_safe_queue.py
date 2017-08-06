from collections import deque
import threading

def producer(syncq):
    error = None
    while error == None:
        item = read_from_network_socket()
        error = syncq.push(item)

q.drain() # eventually drain
return error

def consumer(syncq)
    error = None
    while error == None
        item = syncq.pop()
        error = write_item_to_disk(item)

q.cancel(error) # << we are going to write this << 
return error


class SyncQ(object):
    def __init__(self):
        self.q = deque() # thread safe...
        self.cond = threading.Condition() # condition variable
        self.max_num_el = 10000
        self.error = None # thread safe

    # must return the error, if there has been an error
    def push(self, item):        
        with (self.cond):
            while len(self.q) > self.max_num_el or self.error:
                self.cond.wait() # there's been an error, I get woken up...but I'm in a while loop...
            if self.error:
                return self.error
            self.q.push(item) # this line by itself is unsafe, two threads could be concurrently accessing the queue.
            if len(self.q) < self.max_num_el:
                self.cond.signal() # << t2 signals...wakes up t1...signal only wakes one waiter.
        
    def pop(self):
        # I want to wait for data to come into the queue
        with (self.cond):
            while len(self.q) == 0:
                self.cond.wait() # << waiting for data to arrive.
            item = self.q.pop() # this throws exception if queue is empty
            if len(self.q) > 0:
                self.cond.signal()
            return item

    def cancel(error):
        with self.cond:
            self.error = error
            self.cond.broadcast()
