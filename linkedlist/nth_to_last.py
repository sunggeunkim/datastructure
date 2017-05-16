class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def nth_to_last(head, n):
    if head == None:
        return head
    if n == 0:
        return None

    curr = head
    follower = head
    for _ in range(n):
        if curr == None: return None
        curr = curr.next
    if curr == None: return None
    while curr.next:
        follower = follower.next
        curr = curr.next
    return follower
    
head = Node(1, Node(2, Node(3, Node(4, Node(5)))))    

print(nth_to_last(head, 3).value)
print(nth_to_last(head, 0))
print(nth_to_last(head, 1).value)
print(nth_to_last(head, 7))
print(nth_to_last(head, 5))
