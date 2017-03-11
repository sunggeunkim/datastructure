class SinglyLinkedList:
    #constructor
    def __init__(self):
        self.head = None
        
    #method for setting the head of the Linked List
    def setHead(self,head):
        self.head = head
                     
    def arrange_in_pairs(self):
        c = self.head
        if self.head == None:
            return None
        if self.head.getNext() == None:
            return self.head
        # this array saves all the nodes in the linked list
        a = []
        while c:
            a.append(c)
            c = c.getNext()
        n = len(a)
        i = 0
        j = n-1
        while i < j:
            if i != 0:
                p.setNext(a[i])
            a[i].setNext(a[j])
            p = a[j]
            i += 1
            j -= 1
        if i == j:
            p.setNext(a[i])


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
     
    def getData(self):
        return self.data
     
    def setNext(self,next):
        self.next = next
     
    def getNext(self):
        return self.next

def print_list(head):
    c = head
    while c:
        print(c.getData())
        c = c.getNext()

a = Node(1, Node(2, Node(3, Node(4))))
print_list(a)
import pdb;pdb.set_trace()
s = SinglyLinkedList()
s.setHead(a)
s.arrange_in_pairs()
print_list(a)
