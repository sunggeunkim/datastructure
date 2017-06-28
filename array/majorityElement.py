class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        counter = 1
        majority = A[0]
        i = 1
        while i < len(A):
            if A[i] != majority:
                counter -= 1
            else:
                counter += 1
            if counter == 0:
                i += 1
                majority = A[i]
                counter = 1
            i += 1
        return majority
            
