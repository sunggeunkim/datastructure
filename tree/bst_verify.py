'''
Given a binary tree, write a function to test if the tree is a binary search tree.

reference: http://www.byte-by-byte.com/binarysearchtree/
'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def bst_verify(root, min_val, max_val):
    if root is None:
        return True
    if root.value < min_val or root.value > max_val:
        return False
    return bst_verify(root.left, min_val, root.value) and\
           bst_verify(root.right, root.value, max_val)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(15)

print(bst_verify(root, -100000, 100000))