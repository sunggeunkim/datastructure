'''
Given a 2D array, return all of the elements of the matrix in spiral order.
'''

def matrixElementsInSpiralOrder(matrix):
    m = len(matrix)
    if m == 0:
        return []
    n = len(matrix[0])
    if n == 0:
        return []
    if n == 1 and m == 1:
        return [matrix[0][0]]
    '''
        k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator
    '''
    result = []
    k = 0
    l = 0
    while k < m and l < n:
        i = l
        #the first row from the remaining rows
        while i < n:
            result.append(matrix[k][i])
            i += 1
        k += 1
        i = k
        #the last column from the remaining columns
        while i < m:
            result.append(matrix[i][n-1])
            i += 1
        n -= 1
        #the last row from the remaining rows
        if k < m:
            i = n - 1
            while i >= l:
                result.append(matrix[m-1][i])
                i -= 1
            m -= 1
        #the first column from the remaining columns
        if l < n:
            i = m - 1
            while i >= k:
                result.append(matrix[i][l])
                i -= 1
            l += 1 
    return result
