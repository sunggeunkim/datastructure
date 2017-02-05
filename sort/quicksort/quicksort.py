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
	pivot_ind = high-1
        pivot = array[pivot_ind]
        swap(array, pivot_ind, high-1)
        i = low
        j = high-2
        while i < j:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot and j >= low:
                j -= 1
            if i < j:
                swap(array, i, j)
        array[high-1]=array[i]
        array[i]=pivot
        sorted1 = quicksort_helper(array, low, i)
        sorted2 = quicksort_helper(array, i+1, high)
        return sorted1 + [pivot] + sorted2
    else:
        return []
    
def quicksort(array):
    return quicksort_helper(array, 0, len(array))

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)

