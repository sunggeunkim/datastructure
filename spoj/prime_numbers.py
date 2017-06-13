import math

def isPrime(x):
    if x == 1:
        return False
    if x == 2 or x == 3:
        return True
    i = 2
    while i < math.sqrt(x):
        if x % i == 0:
            return False
        i += 1
    return True

t = int(input().strip())
rlist = []
for j in range(t):
     r = tuple(list(map(int, input().strip().split())))
     rlist.append(r)
for j in range(t):
    m = rlist[j][0]
    n = rlist[j][1]
    for x in range(m, n+1):
        if isPrime(x):
            print(x)
    print("")

        
