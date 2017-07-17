'''
reference: https://codefights.com/interview-practice/task/mkobsYSSQo3JpvYNN/description

You have a 2D binary matrix that's filled with 0s and 1s. In the matrix, find the largest square that contains only 1s and return its area.

Example

For

matrix = [
    ['1', '0', '1', '1', '1'],
    ['1', '0', '1', '1', '1'],
    ['1', '1', '1', '1', '1'],
    ['1', '0', '0', '1', '0'],
    ['1', '0', '0', '1', '0']
]
the output should be
maximalSquare(matrix) = 9.

Input/Output

[time limit] 4000ms (py3)
[input] array.array.char matrix

Guaranteed constraints:
0 ≤ matrix.length ≤ 100,
1 ≤ matrix[i].length ≤ 100,
0 ≤ matrix[i][j] ≤ 1.

[output] integer

An integer that represents the area of the largest square in the given matrix that is composed only of 1s.
'''

def maximalSquare(matrix):
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '1':
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                result = max(result, dp[i][j])
    return result * result
