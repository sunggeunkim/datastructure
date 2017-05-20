'''
Given an array, write a function to find any subarray that sums to zero, if one exists.

eg.

zero_sum([1, 2, -5, 1, 2, -1]) = [2, -5, 1, 2]
'''

def zero_sum(arr):
    if arr is None or len(arr) == 0:
        raise Exceptions
