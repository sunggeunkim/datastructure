"""
Given an array of equal-length strings, check if it is possible to rearrange the strings in such a way that after the rearrangement the strings at consecutive positions would differ by exactly one character.
"""

class Node:
    def __init__(self, value, n = 1, visited = False, next = None, parents=None):
        self.value = value
        self.n = n
        self.visited = visited
        self.next = next

def diff_str_by_one(s1, s2):
    d = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            d += 1
    return d == 1

def dfsHelper(root, n):
    root.visited = True
    if root.n == n:
        return True
    found = False
    if root.next:
        for next in root.next:
            if not next.visited:
                next.n = root.n + 1
                if dfsHelper(next, n):
                    found = True
                next.visited = False                
    return found
        
def stringsRearrangement(inputArray):
    nodes = []
    for i in range(len(inputArray)):
        nodes.append(Node(inputArray[i]))
    for i in range(len(inputArray)):
        for j in range(i+1, len(inputArray)):
            if diff_str_by_one(nodes[i].value, nodes[j].value):
                if nodes[i].next == None:
                    nodes[i].next = [nodes[j]]
                else:
                    nodes[i].next.append(nodes[j])
                if nodes[j].next == None:
                    nodes[j].next = [nodes[i]]
                else:
                    nodes[j].next.append(nodes[i])
    for i in range(len(inputArray)):
        for j in range(len(inputArray)):
            nodes[j].visited = False
        nodes[i].n = 1
        if dfsHelper(nodes[i], len(inputArray)):
            return True
    return False
