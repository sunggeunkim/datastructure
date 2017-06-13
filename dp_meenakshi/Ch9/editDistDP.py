'''
Calculate edit distance of two strings.
The edit distance is the minimum number of character operations(update, delete, insert) required to convert one string into another.
'''
def editDistDP(s1, s2):
    m = len(s1)
    n = len(s2)
    editD = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for j in range(m+1):
        editD[0][j] = j
    for i in range(1,n+1):
        editD[i][0] = i
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[j-1] == s2[i-1]:
                editD[i][j] = editD[i-1][j-1]
            else:
                editD[i][j] = min(editD[i][j-1],\
                                  editD[i-1][j],\
                                  editD[i-1][j-1])+1
    return editD[n][m]

print(editDistDP("cars", "cat"))
print(editDistDP("Sunday", "Saturday"))
