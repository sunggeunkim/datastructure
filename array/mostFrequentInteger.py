import random

def mostFrequentInteger(a):
    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    m = 0
    mkey = 0
    for key in d:
        if d[key] > m:
            m = d[key]
            mkey = key
    return mkey

a = []
for i in range(1000000):
    a.append(random.randint(1, 100))
print(mostFrequentInteger(a))
