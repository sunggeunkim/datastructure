'''
Given a list of integers, write a function that returns all sets of 3 numbers in the list, a, b, and c, so that a + b + c == 0.

eg.
three_sum([-1, 0, 1, 2, -1, -4])
[-1, -1, 2]
[-1, 0, 1]


[-4, -1, -1, 0, 1, 2]
reference: http://www.byte-by-byte.com/threesum/
'''

def three_sum(arr):
    result = []
    arr.sort()
    print(arr)
    for i in range(len(arr)-2):
        if i == 0 or arr[i] > arr[i-1]:
            low = i + 1
            high = len(arr)-1
            while low < high:
                if arr[low] + arr[high] + arr[i] == 0:
                    result.append([arr[i], arr[low], arr[high]])
                if arr[low] + arr[high] + arr[i] < 0:
                    low += 1
                else:
                    high -= 1
    return result

print(three_sum([-1, 0, 1, 2, -1, -4]))
