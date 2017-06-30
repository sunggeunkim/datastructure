def climbingStaircase(n, k):
    if n == 0:
        return [[]]
    result = []
    for i in range(1,k+1):
        if n-i < 0:
            continue
        for x in climbingStaircase(n-i, k):
            result.append([i] + x)
    return result

print(climbingStaircase(4,2))
