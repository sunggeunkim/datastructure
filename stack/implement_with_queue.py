from queue import Queue

class Stack:
    def __init__(self):
        self.primary = Queue()
        self.secondary = Queue()

    def push(self, x):
        self.secondary.put(x)
        while not self.primary.empty():
            self.secondary.put(self.primary.get())
        tmp = self.primary
        self.primary = self.secondary
        self.secondary = tmp

    def pop(self):
        if self.primary.empty():
            raise Exception('No elements to pop.')
        return self.primary.get()


s = Stack()
s.push(3)
# primary = 3

s.push(1)
# primary = 1 - 3

print(s.pop()) # pop 1
# primary = 3

s.push(2)
# primary = 2 - 3

print(s.pop()) # pop 2
# primary = 3

print(s.pop()) # pop 3
# primary = empty

print(s.pop()) # error

