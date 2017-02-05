"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
from random import randint

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp
    return
    
def quicksort_helper(array, low, high):
    if low < high:
        pivot_ind = high
        pivot = array[pivot_ind]
        swap(array, pivot_ind, high)
        i = low-1
        j = high
        while True:
            while True:
                i += 1
                if array[i] >= pivot:
                    break
            while True:
                j -= 1
                if array[j] <= pivot or j <= low:
                    break
            if i < j:
                swap(array, i, j)
            else:
			    break
        array[high]=array[i]
        array[i]=pivot
        sorted1 = quicksort_helper(array, low, i-1)
        sorted2 = quicksort_helper(array, i+1, high)
        return sorted1 + [pivot] + sorted2
    elif low == high:
        return [array[low]]
    else:
        return []
    
def quicksort(array):
    return quicksort_helper(array, 0, len(array)-1)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
test = [21, 4, 21, 3, 21, 20, 25, 6, 21, 14]
print quicksort(test)

