'''
given size of two-dimensional array, find total number of paths possible from top-left cell to bottom-right cell.
'''
def totalPathCount(m, n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    dp = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(m):
        dp[0][j] = 1
    for i in range(1,n):
        dp[i][0] = 1
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]

print(totalPathCount(3,3))
print(totalPathCount(6,6))
        
