def isValid(i, j, queens):
    for qj, qi in enumerate(queens):
        if qi == i or abs(qi - i) == abs(qj + 1 - j):
            return False
    return True

def nQueens(n):
    if n == 1: return [[1]]
    queue = []
    result = []
    for i in range(1, n+1):
        queue.append([i])
    while len(queue) > 0:
        queens = queue.pop(0)
        j = len(queens) + 1
        for i in range(1, n+1):
            if isValid(i, j, queens):
                temp = list(queens)
                temp.append(i)
                if len(temp) == n:
                    result.append(temp)
                queue.append(temp)
    return result
