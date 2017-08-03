'''
reference: http://www.geeksforgeeks.org/majority-element/
A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).

Write a function which takes an array and returns the majority element (if it exists), otherwise returns NONE as follows:
Moore’s Voting Algorithm

This is a two step process.
1. The first step gives the element that may be majority element in the array.
If there is a majority element in an array, then this step will definitely return majority element,
otherwise it will return any other element.
2. Check if the element obtained from above step is majority element.
This step is necessary as we are not always sure that element return by first step is majority element.

1. Finding a Candidate:
The algorithm for first phase that works in O(n) is known as Moore’s Voting Algorithm.
Basic idea of the algorithm is if we cancel out each occurrence of an element e with all the other elements 
that are different from e then e will exist till end if it is a majority element.

2. Check if the element obtained in step 1 is majority
'''

def findCandidate(A):
    maj_index = 0
    count = 1
    for i in range(len(A)):
        if A[maj_index] == A[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            maj_index = i
            count = 1
    return A[maj_index]
    
    # Function to check if the candidate occurs more than n/2 times
def isMajority(A, cand):
    count = 0
    for i in range(len(A)):
        if A[i] == cand:
            count += 1
    if count > len(A)/2:
        return True
    else:
        return False
            
