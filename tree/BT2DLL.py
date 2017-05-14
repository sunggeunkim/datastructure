# convert binary tree to doubly linked list
# root is the root of the tree
# head is the head of the linked list

prev = None

def BT2DLL(root, head):

    #base case
    if root == None: return 

    prev = None

    # traverse to the left
    BT2DLL(root.left, head)

    # if we are at the left most node
    # set the head to the root if prev is None
    if prev == None:
        head = root

    # if prev is not pointing to None
    # create a double link to prev and root
    else:
        root.left = prev
        prev.right = root
    
    # prev is pointing to the root
    prev = root

    # do the same thing above to the right subtree.
    BT2DLL(root.right, head)

