'''
Given a tree, write a function that prints out the nodes of the tree in level order.

reference: http://www.byte-by-byte.com/treelevelorder/
'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order(root):
    if root == None:
        return

    q = []
    q.append(root)
    while len(q) > 0:
        c = q.pop(0)
        print (c.value)
        if c.left:
            q.append(c.left)
        if c.right:
            q.append(c.right)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(15)

level_order(root)