'''
Given an integer, write a function to compute the number of ones in the binary representation of the number.

e.g.
ones(0) = 0
ones(1) = 1
ones(2) = 1
ones(3) = 2
ones(7) = 3

7 & 1 = 111 & 001 = 001
7 >> 1 = 3 & 1 = 11 & 01 = 01
3 >> 1 = 1 & 1 = 1
reference: http://www.byte-by-byte.com/onesinbinary/
'''

def ones(x):
    if x is None or x == 0 or x == 1:
        return x
    count = 0
    while x >= 1:
        if x & 1 == 1:
            count += 1
        x >>= 1
    return count

print(ones(7))
print(ones(1024))
print(ones(1023))