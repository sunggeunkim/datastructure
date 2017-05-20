'''
Given two integers, write a function to determine whether or not their binary representations differ by a single bit.

e.g.
gray(0, 1) = true
gray(1, 2) = false

reference: http://www.byte-by-byte.com/graycode/
'''

def isGray(a, b):
    if a == 0 and b == 0:
        return False
    x = a ^ b
    while x > 0:
        if x % 2 == 1 and x>>1 > 0:
            return False
        x = x>>1
    return True

def isGrayEfficient(a, b):
    if a == 0 and b == 0:
        return False
    x = a ^ b
    return x & (x - 1) == 0



print(isGray(0, 1))
print(isGray(1, 2))
print(isGray(1024, 1025))
print(isGray(1203498710293487, 1203498710293488))
print(isGray(0, 0))

print(isGrayEfficient(0, 1))
print(isGrayEfficient(1, 2))
print(isGrayEfficient(1024, 1025))
print(isGrayEfficient(1203498710293487, 1203498710293488))
print(isGrayEfficient(0, 0))
