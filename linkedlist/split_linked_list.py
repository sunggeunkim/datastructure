'''
Given a linked list, write a function to split the list into two equal halves.

eg.

divide(1 -> 2 -> 3 -> 4) = 1 -> 2, 3 -> 4
divide(1 -> 2 -> 3 -> 4 -> 5) = 1 -> 2 -> 3, 4 -> 5

reference: http://www.byte-by-byte.com/splitlinkedlist/
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
def print_ll(head):
    if head == None:
        return
    curr = head
    while curr != None:
        print(curr.value, end = "")
        if curr.next != None:
            print(" -> ", end = "")
        curr = curr.next


def divide(head):
    if head == None:
        return head
    if head.next == None:
        return None
    slow = head
    fast = head
    while fast != None:
        fast = fast.next
        slow = slow.next
        if fast != None:
            fast = fast.next
    return slow

head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
half = divide(head)
print_ll(half)
print("")
head = Node(1, Node(2, Node(3, Node(4, None))))
half = divide(head)
print_ll(half)

