def isRotation(a1, a2):
    if len(a1) != len(a2):
        return False
    return isSubArray(a1 * 2, a2)

def isSubArray(a1, a2):
    j = 0
    for a in a1:
        if a == a2[j]:
            j += 1
        else:
            j = 0
        if j == len(a2):
            return True
    return False
import numpy as np
a1 = list(np.random.randint(1, 100, size=10000))
a2 = [101] + a1[499:] + a1[:500]
print(isRotation(a1, a2))
