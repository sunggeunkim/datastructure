'''
Given a list of strings, write a function to get the kth most frequently occurring string.

eg.

kthMostFrequent(["a","b","c","a","b","a"], 0) = "a"
kthMostFrequent(["a","b","c","a","b","a"], 1) = "b"
kthMostFrequent(["a","b","c","a","b","a"], 2) = "c"
kthMostFrequent(["a","b","c","a","b","a"], 3) = null

reference: http://www.byte-by-byte.com/kthmostfrequentstring/
'''

def kthMostFrequent(slist, k):
    if slist is None:
        raise Exception('None input.')
    if len(slist) == 0:
        raise Exception('There are no elements in the list.')
    if k < 0:
        raise Exception('Negative k is not accepted.')

    d = {}
    for s in slist:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1

    sorted_by_value = sorted(d, key=d.get, reverse=True)
    if k > len(sorted_by_value) - 1:
        return None
    return sorted_by_value[k]

print(kthMostFrequent(["a","b","c","a","b","a"], 0))
print(kthMostFrequent(["a","b","c","a","b","a"], 1))
print(kthMostFrequent(["a","b","c","a","b","a"], 2))
print(kthMostFrequent(["a","b","c","a","b","a"], 3))