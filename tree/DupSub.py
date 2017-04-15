class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

subtrees = set()

def subDup(root):
    if root == None:
        return False, ""
    lstr = ""
    rstr = ""
    xl = False
    xr = False
    if root.left:
        (xl, lstr) = subDup(root.left)
    if root.right:
        (xr, rstr) = subDup(root.right)
    if xl or xr:
        return True, ""
    s = root.value + lstr + rstr
    if len(s) > 2 and s in subtrees:
        return True, s
    subtrees.add(s)
    return False, s



root = TreeNode("A")
root.left = TreeNode("B")
root.left.left = TreeNode("E")
root.left.right = TreeNode("E")
root.right = TreeNode("C")
root.right.left = TreeNode("B")
root.right.left.left = TreeNode("E")
root.right.left.right = TreeNode("E")

print(subDup(root)[0])
