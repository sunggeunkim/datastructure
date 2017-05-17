'''
Implement a LIFO stack that has a push(), pop(), and max() function,
 where max() returns the maximum value in the stack.
  All of these functions should run in O(1) time.
  
  e.g.
push(1)
max() = 1
push(2)
max() = 2
push(1)
max() = 2
pop() = 1
max() = 2
pop() = 2
max() = 1

reference: http://www.byte-by-byte.com/maxstack/
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.oldMax = None
        self.next = None

class MaxStack:
    def __init__(self):
        self.maxnode = None
        self.stack = None

    def push(self, value):
        n = Node(value)
        if self.stack is None:
            self.stack = n
        else:
            n.next = self.stack
            self.stack = n
        if self.maxnode is None or n.value > self.maxnode.value:
            n.oldMax = self.maxnode
            self.maxnode = n

    def pop(self):
        if self.stack is None:
            return None
        n = self.stack
        self.stack = n.next
        if self.maxnode == n:
            self.maxnode = n.oldMax
        return n.value

    def max(self):
        if self.maxnode is None:
            return None
        return self.maxnode.value

m = MaxStack()
m.push(1)
print(m.max())
m.push(2)
print(m.max())
m.push(1)
print(m.max())
print(m.pop())
print(m.max())
print(m.pop())
print(m.max())
