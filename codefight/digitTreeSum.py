'''
reference: https://codefights.com/interview-practice/task/2oxNWXTS8eWBzvnRB/description
We're going to store numbers in a tree. Each node in this tree will store a single digit (from 0 to 9), and each path from root to leaf encodes a non-negative integer.

Given a binary tree t, find the sum of all the numbers encoded in it.

Example

For
t = {
    "value": 1,
    "left": {
        "value": 0,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 1,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 4,
        "left": null,
        "right": null
    }
}
the output should be
digitTreeSum(t) = 218.
There are 3 numbers encoded in this tree:

Path 1->0->3 encodes 103
Path 1->0->1 encodes 101
Path 1->4 encodes 14
and their sum is 103 + 101 + 14 = 218.
t = {
    "value": 0,
    "left": {
        "value": 9,
        "left": null,
        "right": null
    },
    "right": {
        "value": 9,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be
digitTreeSum(t) = 193.
Because 09 + 091 + 093 = 193

Input/Output

[time limit] 4000ms (py3)
[input] tree.integer t

A tree of integers. It's guaranteed that the sum of encoded integers won't exceed 252.

Guaranteed constraints:
1 ≤ tree size ≤ 2000,
1 ≤ tree depth ≤ 9,
0 ≤ node value ≤ 9.

[output] integer64

The sum of the integers encoded in t, as described above.
'''

def digitTreeSum(t):
    sum = 0
    stack = [(t, t.value)]
    while len(stack) > 0:
        curr_node, digit = stack.pop()
        if curr_node.left == None and curr_node.right == None:
            sum += digit   
        else:
            if curr_node.left:
                stack.append((curr_node.left, digit * 10 + curr_node.left.value))
            if curr_node.right:
                stack.append((curr_node.right, digit * 10 + curr_node.right.value))
    return sum
        
