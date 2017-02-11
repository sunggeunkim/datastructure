class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert_helper(self, node, value):
        if value < node.value:
            if node.left:
                self.insert_helper(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self.insert_helper(node.right, value)
            else:
                node.right = Node(value)
            
    def insert(self, new_val):
        if self.root:
            self.insert_helper(self.root, new_val)
        else:
            self.root = Node(new_val)
        
        
    def search_helper(self, node, value):
        if node:
            if value < node.value:
                return self.search_helper(node.left, value)
            elif value > node.value:
                return self.search_helper(node.right, value)
            else:
                return True
        return False

    def search(self, find_val):
        if self.root:
            return self.search_helper(self.root, find_val)
        else:
            return False
        
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
