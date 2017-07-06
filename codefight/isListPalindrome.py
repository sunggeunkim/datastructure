'''
ref: https://codefights.com/interview-practice/task/HmNvEkfFShPhREMn4
Given a singly linked list of integers, determine whether or not it's a palindrome.

Example

For l = [0, 1, 0], the output should be
isListPalindrome(l) = true;
For l = [1, 2, 2, 3], the output should be
isListPalindrome(l) = false.

Input/Output

[time limit] 4000ms (py3)
[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 5 · 105,
-109 ≤ element value ≤ 109

'''

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    if l == None or l.next == None:
        return True
    if l.next.next == None:
        return l.value == l.next.value
    if l.next.next.next == None:
        return l.value == l.next.next.value
    
    # fast pointer travels twice faster than
    # slow pointer so that after finishing traverse
    # slow pointer should point to the middle of the linkedlist
    fast, slow = l, l
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        
    # if the number of the nodes in the linkedlist is even
    # fast is None at this point
    # if odd, then we need to skip the middle element
    if fast != None:
        slow = slow.next
        
    # reverse the later half of the linkedlist
    prev = None    
    next = slow.next
    while next:
        slow.next = prev
        prev, slow = slow, next
        next = next.next
    slow.next = prev
    
    # traverse the reversed half and compare the elements to
    # that in the non-reversed first half.
    while slow:
        if slow.value != l.value:
            return False
        l = l.next
        slow = slow.next
    return True
    

