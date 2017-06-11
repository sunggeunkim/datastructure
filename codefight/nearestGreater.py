'''
reference: https://codefights.com

Given an array of integers a, return a new array b using the following guidelines:

For each index i in b, the value of bi is the index of the aj nearest to ai and is also greater than ai.
If there are two options for bi, put the leftmost one in bi.
If there are no options for bi, put -1 in bi.
Example

For a = [1, 4, 2, 1, 7, 6], the output should be
nearestGreater(a) = [1, 4, 1, 2, -1, 4].

for a[0], the nearest larger element is 4 at index a[1] -> b[0] contains the value 1.
for a[1], the nearest larger element is 7 at a[4] -> b[1] contains the value 4.
for a[2], the nearest larger element is 4 at a[1] (7 is also larger, but 4 has the minimal position) -> b[2] contains the value 1.
for a[3], the nearest larger element is 2 at a[2] (7 is also larger, but 2 has the minimal position) -> b[3] contains the value 2.
for a[4], there is no element larger than 7 -> b[4] contains the value -1.
for a[5], the nearest larger element is 7 at a[4] -> b[5] contains the value 4.

'''

def getOneDirectionNGE(a, left_or_right):
    NGE = [-1] * len(a)
    if left_or_right == 'right':
        stack = [(a[0], 0)]
        iterate = range(1, len(a))
    elif left_or_right == 'left':
        stack = [(a[-1], len(a)-1)]
        iterate = range(len(a)-2, -1, -1)
    for i in iterate:
        next = a[i]
        while len(stack) > 0:
            element, index = stack.pop()
            if element < next:
                NGE[index] = i
            else:
                stack.append((element, index))
                break
        stack.append((next, i))
    while len(stack) > 0:
        element, index = stack.pop()
        NGE[index] = -1
    return NGE

def getNGE(leftNGE, rightNGE):
    result = [-1] * len(leftNGE)
    for i in range(len(leftNGE)):
        if leftNGE[i] == -1:
            if rightNGE[i] == -1:
                result[i] = -1
            else:
                result[i] = rightNGE[i]
        else:
            if rightNGE[i] == -1:
                result[i] = leftNGE[i]
            else:
                if abs(rightNGE[i] - i) < abs(leftNGE[i]-i):
                    result[i] = rightNGE[i]
                else:
                    result[i] = leftNGE[i]
    return result

def nearestGreater(a):
    if len(a) == 0:
        return a
    if len(a) == 1:
        return [-1]
    rightNGE = getOneDirectionNGE(a, 'right')
    leftNGE = getOneDirectionNGE(a, 'left')
    return getNGE(leftNGE, rightNGE)

