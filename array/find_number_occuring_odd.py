'''
Given an array of positive integers
All numbers occur even number of times except one number which occurs odd number of times
Find the number in O(n) time & constant space.

Example:
I/P = [1, 2, 3, 2, 3, 1, 3]
O/P = 3
ref: http://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/
'''

def find_number_occuring_odd(x):
    xor = 0
    for i in x:
        xor ^= i
    return xor

print(find_number_occuring_odd([1, 2, 3, 2, 3, 1, 3]))
